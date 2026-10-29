# 下载与解压恢复说明（工业过程监控文献库，2026-10-29）

本文献库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含以下内容，不含论文、书籍和课程讲义全文：
  - 根目录的报告与登记表：`README_cn.md`、`catalog_cn.csv`、`reading_map_cn.md`、`search_log_cn.md`、`download_failures_cn.csv`、`checksums_en.sha256`；
  - `domains/` 下 14 个分类索引（`README_cn.md`）；
  - 脚本 `scripts/`；
  - 本说明、分包索引、改名明细和未发布清单。

  仓库原有的 `main` 分支没有改动。这个分支的父提交是远端 `main` 的 `e111379`。
- **Release `ipm-full-20261029`**：3 个独立的不压缩 `.tar` 包，合起来就是文献库的发布内容。

Release 页面：https://github.com/feng199506/industrial-process-monitoring-literature/releases/tag/ipm-full-20261029

## 1. 未发布的资料（仍保存在本机文献库中）

下列 2 本书的许可明确限制为个人使用、不得再分发，公开发布会超出许可范围，因此**没有放进 Release，也没有放进 Git 分支**。

- 本库 catalog 没有许可证列，许可依据取自同一作品在本机其他文献库 catalog 中的记录。
- 这 2 本书在 `catalog_cn.csv` 中仍有登记，解压后对应路径下没有文件。发布包中的 `checksums_en.sha256` 已去掉这 2 行。
- 明细和免费获取地址见 `release_excluded_cn.csv`。

| 编号 | 书籍 | 许可 |
|---|---|---|
| 14-006 | Särkkä & Svensson《Bayesian Filtering and Smoothing》第 2 版 | 作者主页经出版社许可提供，仅限个人浏览下载，不得再分发 |
| 14-017 | Deisenroth, Faisal & Ong《Mathematics for Machine Learning》 | 作者官网免费，仅限个人使用 |

## 2. 包列表

包按路径顺序切分，内容范围如下（文件名前缀都是 `industrial_process_monitoring_literature_20261029_`，后缀都是 `_cn_en.tar`）：

| 包 | 内容范围（按路径顺序） |
|---|---|
| `batch001` | 根目录报告与登记表、`scripts/`、`books/`、`domains/`，以及 `papers/` 的前一部分 |
| `batch002` | `papers/` 其余部分，以及 `university_materials/` 的前一部分（到 Linköping TSFS06 课件的一部分） |
| `batch003` | `university_materials/` 其余部分 |

每个文件属于哪个包，见 `archive_index_cn.csv`。它是 UTF-8 带 BOM 编码，可直接用 Excel 打开，共 773 行，其中 772 个文件、1 个空目录（`scripts/annotations/`）。

- 每个包都可以**单独解压**，不需要拼接。
- 包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包没有压缩，全部解压约需 **3.5 GiB**。

## 3. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击下列文件，全部保存到**同一个下载文件夹**，例如 `D:\下载\ipm\`：
   - 3 个 `.tar` 文件；
   - `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`release_excluded_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`。
3. 单个包最大约 1.5 GB。浏览器提示“是否保留”时选择保留。下载中断时，可以在浏览器的下载列表里点“恢复”，或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，核对每个包的大小。在文件属性窗口里看“大小”一项的字节数，不要看“占用空间”。

## 4. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**，目标目录用短路径，例如 `D:\ipm\`。

1. 在下载文件夹中，按住 Ctrl 选中 3 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\ipm\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 点确定。

也可以逐个解压：每个包都右键 → WinRAR → **解压文件…**，目标路径都填同一个 `D:\ipm\`。不要用“解压到 industrial_process_monitoring_literature_20261029_batch00X_cn_en\”这个菜单项，它会给每个包各建一个子文件夹，目录结构就被拆散了。

解压后的目录结构：

```
D:\ipm\
├─ README_cn.md、catalog_cn.csv、reading_map_cn.md、search_log_cn.md、download_failures_cn.csv、checksums_en.sha256
├─ domains\（01_fundamentals_reviews … 14_books_references 的分类索引）
├─ papers\ books\ university_materials\
└─ scripts\
```

### Windows 兼容处理

- **第一层**：772 个文件都不需要改名，最长相对路径 98 个字符。
- **两个网页版课程包 `.zip` 已在发布包中重新打包**，其余内容不变：
  - 涉及：Notre Dame CBE 30338《Chemical Process Control》、BYU《Process Dynamics and Control》。
  - 包内共 6 个文件名带 `?` 等 Windows 不允许的字符，改成了 `_`。
  - 引用这些文件的 47 个网页已同步改写，离线打开时仍能正常显示。
  - 因此这 2 个 `.zip` 的字节数与文献库原件不同，发布包中的 `checksums_en.sha256` 已改为新的 SHA-256。
- 其余 18 个内层归档已逐个检查，没有改动。
- 每一处改动都逐条记在 `windows_rename_map_cn.csv` 里，文献库的本地原件没有改动。

## 5. 校验（可选）

发布包自带的 `checksums_en.sha256` 与发布内容一致，即已去掉未发布的 2 本书、已更新重新打包的 2 个 `.zip`。

- Linux / macOS：在解压目录执行 `sha256sum -c checksums_en.sha256`。
- Windows：可用 PowerShell 的 `Get-FileHash -Algorithm SHA256` 逐个核对。

## 6. Linux / macOS

```bash
mkdir -p ~/ipm
for f in industrial_process_monitoring_literature_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/ipm || echo "FAILED: $f"; done
```

## 7. 资料状态说明（来自文献库自身的报告，与打包无关）

- **只计已核验条目**：论文 573 篇，课程资料包 25 个，书籍 26 本，详见 `README_cn.md` 和 `catalog_cn.csv`。其中 2 本书属于第 1 节的未发布资料。
- **缺口与失败**：分类缺口（02、03、04、06、13、14 类）见 `README_cn.md`。下载失败、核验未通过和人工否决的条目见 `download_failures_cn.csv`，不计数。
- **快照时间**：本次按 2026-10-29 22:57（中欧时间）的文献库内容打包。打包前先把整个文献库复制成一份快照，打包用的就是这份快照。文献库最后一次写入是在 22:32。

## 8. 完整性说明

- 本次发布只登记了上传状态：GitHub API 显示附件为 `uploaded`，且远端大小等于本地大小。**没有**做下载回验，也没有另做哈希回验。
- 除第 1 节的未发布资料外，文献库中的资料文件都已打包。另外只排除了：
  - 本地 `.git/`，约 1.2 GB；
  - `scripts/__pycache__/` 中的 4 个 `.pyc`；
  - 1 个空的 `.lock` 锁文件。
