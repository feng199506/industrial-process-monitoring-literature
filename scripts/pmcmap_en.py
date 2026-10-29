"""Map candidate DOIs to PMC IDs with the NCBI ID Converter API (batches of 150).
Only records that PMC lists get a pmcid; the PDF itself comes from the official
PMC Open Access dataset on AWS (pmc-oa-opendata), see papers_en.pmc_pdf.

  python3 -I scripts/pmcmap_en.py
"""
import fcntl
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CACHE, STATE, get_json, load, save  # noqa: E402

CAND = CACHE / "candidates_en.json"


def main():
    with open(STATE / "discover.lock", "a") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        cands = load(CAND, {})
        todo = [c["doi"] for c in cands.values() if c.get("doi") and not c.get("pmcid") and not c.get("pmc_checked")]
        by = {}
        for c in cands.values():
            if c.get("doi"):
                by.setdefault(c["doi"], []).append(c)
        hit = 0
        for i in range(0, len(todo), 150):
            chunk = todo[i:i + 150]
            d = get_json("https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?" + urllib.parse.urlencode(
                {"ids": ",".join(chunk), "format": "json", "tool": "ipm_literature"}))
            if d is None:
                print("batch failed", i)
                continue
            for r in d.get("records", []):
                doi = (r.get("doi") or r.get("requested-id", "")).lower()
                for c in by.get(doi, []):
                    c["pmc_checked"] = True
                    if r.get("pmcid"):
                        c["pmcid"] = r["pmcid"]
                        hit += 1
            print(f"{i + len(chunk)}/{len(todo)} mapped, pmcid hits so far {hit}")
        save(CAND, cands)


if __name__ == "__main__":
    main()
