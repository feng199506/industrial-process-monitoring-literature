"""Candidate discovery for the IPM library.

  python3 -I scripts/discover_en.py run NN [--only SRC]   run the queries of category NN from seeds/queries_cn.json
  python3 -I scripts/discover_en.py show NN [--all] [--grep REGEX] [--limit N]
                                                         compact table of candidates hit by NN's queries, for screening
  python3 -I scripts/discover_en.py abs KEY [KEY ...]    print title/venue/abstract of candidates
  python3 -I scripts/discover_en.py refs DOI             backward (Crossref reference list) + forward (OpenCitations) citations

Sources: arXiv API, DOAJ article search, Europe PMC REST, Crossref works query.
Every query is logged to state/search_log_en.jsonl (date, source, query, filters, total hits, fetched).
Candidates are merged by DOI / arXiv ID / normalised title into cache/candidates_en.json.
"""
import html
import json
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from common_en import (CACHE, SEEDS, STATE, WINDOW_START, get_json, http, load, norm, save,  # noqa: E402
                       append_jsonl, strip_tags)

CAND = CACHE / "candidates_en.json"
LOG = STATE / "search_log_en.jsonl"
ATOM = "{http://www.w3.org/2005/Atom}"
ARX = "{http://arxiv.org/schemas/atom}"

PROCESS_RE = re.compile(r"process|plant|tennessee|chemical|batch|soft sensor|quality|industrial|manufactur|"
                        r"refin|distill|reactor|ferment|pharma|steel|blast furnace|cement|wastewater|"
                        r"semiconductor|wafer|paper|pulp|power plant|boiler|polymer|petro", re.I)
EQUIP_RE = re.compile(r"bearing|gearbox|gear |motor|rotating machin|wind turbine|vibration|engine|"
                      r"battery|photovoltaic|inverter|transformer|aircraft|vehicle", re.I)
CYBER_RE = re.compile(r"intrusion|cyber|attack|malware|network traffic|SCADA security", re.I)
OFFTOPIC_RE = re.compile(r"predictive process monitoring|business process|process mining|event log", re.I)


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- sources
def src_arxiv(q, maxn=100, start=WINDOW_START):
    d0 = start.replace("-", "") + "0000"
    sq = f"({q}) AND submittedDate:[{d0} TO 202610292359]"
    url = ("http://export.arxiv.org/api/query?" +
           urllib.parse.urlencode({"search_query": sq, "start": 0, "max_results": maxn,
                                   "sortBy": "relevance"}))
    st, body, _, _ = http(url, accept="application/atom+xml")
    if st != 200:
        return None, []
    root = ET.fromstring(body)
    total = root.findtext("{http://a9.com/-/spec/opensearch/1.1/}totalResults")
    out = []
    for e in root.findall(ATOM + "entry"):
        aid = e.findtext(ATOM + "id").rsplit("/abs/", 1)[-1]
        base = re.sub(r"v\d+$", "", aid)
        out.append({
            "arxiv": base, "title": " ".join(e.findtext(ATOM + "title").split()),
            "authors": [a.findtext(ATOM + "name") for a in e.findall(ATOM + "author")],
            "date": e.findtext(ATOM + "published")[:10], "date_basis": "arXiv v1 提交日",
            "venue": (e.findtext(ARX + "journal_ref") or "arXiv").strip(),
            "doi": (e.findtext(ARX + "doi") or "").lower(),
            "abstract": " ".join((e.findtext(ATOM + "summary") or "").split()),
            "comment": " ".join((e.findtext(ARX + "comment") or "").split()),
            "categories": [c.get("term") for c in e.findall(ATOM + "category")],
            "lang": "en",
        })
    return int(total or 0), out


def src_doaj(q, maxn=200, start=WINDOW_START):
    y0 = start[:4]
    full = f"({q}) AND bibjson.year:[{y0} TO 2026]"
    out, total, page = [], None, 1
    while len(out) < maxn:
        url = ("https://doaj.org/api/search/articles/" + urllib.parse.quote(full, safe="") +
               "?" + urllib.parse.urlencode({"page": page, "pageSize": 100}))
        d = get_json(url)
        if d is None:
            break
        total = d.get("total", 0)
        for r in d.get("results", []):
            b = r["bibjson"]
            doi = next((i.get("id", "") for i in b.get("identifier", []) if i.get("type") == "doi"), "")
            doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi).lower()
            month = b.get("month", "")
            month = f"{int(month):02d}" if str(month).isdigit() else ""
            j = b.get("journal", {})
            out.append({
                "doi": doi, "title": " ".join(strip_tags(b.get("title", "")).split()),
                "authors": [a.get("name", "") for a in b.get("author", [])],
                "date": f"{b.get('year', '')}" + (f"-{month}" if month else ""),
                "date_basis": "DOAJ 年/月（待 Crossref 精确化）",
                "venue": j.get("title", ""), "publisher": j.get("publisher", ""),
                "abstract": " ".join(strip_tags(b.get("abstract", "")).split()),
                "links": [l.get("url") for l in b.get("link", []) if l.get("type") == "fulltext"],
                "keywords": b.get("keywords", []),
                "lang": ",".join(j.get("language", [])).lower(),
            })
        if len(d.get("results", [])) < 100:
            break
        page += 1
    return total, out[:maxn]


def src_epmc(q, maxn=200, start=WINDOW_START):
    full = f"({q}) AND FIRST_PDATE:[{start} TO 2026-10-29] AND OPEN_ACCESS:y"
    out, total, cursor = [], None, "*"
    while len(out) < maxn:
        url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" +
               urllib.parse.urlencode({"query": full, "format": "json", "resultType": "core",
                                       "pageSize": 100, "cursorMark": cursor}))
        d = get_json(url)
        if d is None:
            break
        total = d.get("hitCount", 0)
        res = d.get("resultList", {}).get("result", [])
        for r in res:
            out.append({
                "doi": (r.get("doi") or "").lower(), "pmcid": r.get("pmcid", ""),
                "title": " ".join(strip_tags(r.get("title", "")).split()).rstrip("."),
                "authors": [a.get("fullName", "") for a in r.get("authorList", {}).get("author", [])],
                "date": r.get("firstPublicationDate", ""), "date_basis": "Europe PMC firstPublicationDate",
                "venue": r.get("journalInfo", {}).get("journal", {}).get("title", ""),
                "abstract": " ".join(strip_tags(r.get("abstractText", "")).split()),
                "lang": r.get("language", ""),
            })
        nxt = d.get("nextCursorMark")
        if not res or not nxt or nxt == cursor:
            break
        cursor = nxt
    return total, out[:maxn]


def cr_date(m):
    for k in ("published-online", "published-print", "posted", "issued"):
        dp = (m.get(k) or {}).get("date-parts") or [[]]
        if dp and dp[0] and dp[0][0]:
            return "-".join(f"{x:02d}" if i else str(x) for i, x in enumerate(dp[0])), k
    return "", ""


def cr_record(m):
    d, k = cr_date(m)
    return {
        "doi": m.get("DOI", "").lower(), "title": " ".join(strip_tags((m.get("title") or [""])[0]).split()),
        "authors": [" ".join(x for x in (a.get("given"), a.get("family")) if x) or a.get("name", "")
                    for a in m.get("author", [])],
        "date": d, "date_basis": f"Crossref {k}",
        "venue": (m.get("container-title") or [""])[0], "publisher": m.get("publisher", ""),
        "abstract": " ".join(strip_tags(m.get("abstract", "")).split()),
        "license": [l.get("URL", "") for l in m.get("license", [])],
        "type": m.get("type", ""), "lang": m.get("language", ""),
    }


def src_crossref(q, maxn=200, start=WINDOW_START):
    out, total, cursor = [], None, "*"
    while len(out) < maxn:
        url = ("https://api.crossref.org/works?" + urllib.parse.urlencode({
            "query.bibliographic": q, "filter": f"from-pub-date:{start},type:journal-article",
            "rows": 100, "cursor": cursor,
            "select": "DOI,title,author,published-online,published-print,issued,container-title,"
                      "publisher,abstract,license,type,language"}))
        d = get_json(url)
        if d is None:
            break
        msg = d["message"]
        total = msg.get("total-results", 0)
        items = msg.get("items", [])
        out += [cr_record(m) for m in items]
        cursor = msg.get("next-cursor")
        if not items or not cursor:
            break
    return total, out[:maxn]


SOURCES = {"arxiv": src_arxiv, "doaj": src_doaj, "epmc": src_epmc, "crossref": src_crossref}


# ---------------------------------------------------------------- merge
def key_of(r):
    if r.get("doi"):
        return "doi:" + r["doi"]
    if r.get("arxiv"):
        return "arxiv:" + r["arxiv"]
    return "title:" + norm(r["title"])[:80]


def merge(cands, recs, cat, qid):
    index = {}
    for k, c in cands.items():
        for alias in c.get("aliases", []) + [k]:
            index[alias] = k
        index["title:" + norm(c["title"])[:80]] = k
    added = 0
    for r in recs:
        if not r.get("title"):
            continue
        aliases = [a for a in ("doi:" + r["doi"] if r.get("doi") else "",
                               "arxiv:" + r["arxiv"] if r.get("arxiv") else "",
                               "title:" + norm(r["title"])[:80]) if a]
        k = next((index[a] for a in aliases if a in index), None)
        if k is None:
            k = key_of(r)
            cands[k] = {"aliases": [], "hits": {}, **r}
            added += 1
        c = cands[k]
        for f, v in r.items():
            if v and not c.get(f):
                c[f] = v
        if r.get("arxiv") and r.get("date") and (not c.get("arxiv_date")):
            c["arxiv_date"] = r["date"]
        for a in aliases:
            if a != k and a not in c["aliases"]:
                c["aliases"].append(a)
            index[a] = k
        c["hits"].setdefault(cat, [])
        if qid not in c["hits"][cat]:
            c["hits"][cat].append(qid)
    return added


def run(cat, only=None):
    queries = load(SEEDS / "queries_cn.json", {}).get(cat, [])
    cands = load(CAND, {})
    done = {(x["cat"], x["qid"]) for x in map(json.loads, open(LOG)) } if LOG.exists() else set()
    for q in queries:
        if only and q["src"] != only:
            continue
        if (cat, q["qid"]) in done and not q.get("rerun"):
            continue
        fn = SOURCES[q["src"]]
        total, recs = fn(q["q"], q.get("max", 100), q.get("start", WINDOW_START))
        if total is None:
            print("FAILED", q["qid"], q["src"], q["q"][:80])
            continue
        added = merge(cands, recs, cat, q["qid"])
        append_jsonl(LOG, {"time": now(), "cat": cat, "qid": q["qid"], "src": q["src"], "q": q["q"],
                           "start": q.get("start", WINDOW_START), "total": total, "fetched": len(recs),
                           "new": added})
        save(CAND, cands)
        print(f"{q['qid']:8s} {q['src']:8s} total={total} fetched={len(recs)} new={added} | {q['q'][:90]}")


def flags(c):
    t = c["title"] + " " + c.get("abstract", "")[:1500]
    f = []
    if PROCESS_RE.search(t):
        f.append("P")
    if EQUIP_RE.search(t):
        f.append("E")
    if CYBER_RE.search(t):
        f.append("C")
    if OFFTOPIC_RE.search(t):
        f.append("X")
    if re.search(r"tennessee|\bTEP?\b", t, re.I):
        f.append("TE")
    return "".join(f)


def show(cat, show_all=False, grep=None, limit=400):
    cands = load(CAND, {})
    rows = [(k, c) for k, c in cands.items() if cat in c.get("hits", {}) or show_all]
    if grep:
        rows = [(k, c) for k, c in rows if re.search(grep, c["title"] + " " + c.get("abstract", ""), re.I)]
    rows.sort(key=lambda kc: (-len(kc[1]["hits"].get(cat, [])), kc[1]["title"]))
    for k, c in rows[:limit]:
        print(f"{k[:46]:46s} {c.get('date','')[:7]:7s} {flags(c):5s} {c.get('venue','')[:22]:22s} | {c['title'][:150]}")
    print(len(rows), "rows")


def show_abs(keys):
    cands = load(CAND, {})
    for k in keys:
        c = cands.get(k) or next((v for v in cands.values() if k in v.get("aliases", [])), None)
        if not c:
            print(k, "NOT FOUND")
            continue
        print(f"== {k} | {c.get('date')} | {c.get('venue')} | {'; '.join(c.get('authors', [])[:4])}")
        print("   ", c["title"])
        print("   ", c.get("abstract", "")[:1400])


def refs(doi):
    d = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if d:
        m = d["message"]
        print("BACKWARD (Crossref reference list):", len(m.get("reference", [])))
        for r in m.get("reference", []):
            print("  <-", r.get("DOI", ""), "|", r.get("year", ""), "|",
                  (r.get("article-title") or r.get("unstructured") or "")[:130])
    st, body, _, _ = http("https://api.opencitations.net/index/v2/citations/doi:" + doi,
                          accept="application/json")
    if st == 200:
        cites = json.loads(body)
        print("FORWARD (OpenCitations index v2):", len(cites))
        for r in cites:
            m = re.search(r"doi:(\S+)", r.get("citing", ""))
            print("  ->", m.group(1) if m else r.get("citing"), r.get("creation", ""))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "run":
        run(a[1], a[a.index("--only") + 1] if "--only" in a else None)
    elif a[0] == "show":
        show(a[1], "--all" in a, a[a.index("--grep") + 1] if "--grep" in a else None,
             int(a[a.index("--limit") + 1]) if "--limit" in a else 400)
    elif a[0] == "abs":
        show_abs(a[1:])
    elif a[0] == "refs":
        refs(a[1])
