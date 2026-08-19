#!/usr/bin/env bash
# 公開対象の Markdown を _build/docs に集めて MkDocs でビルドする。
# 使い方: tools/build_site.sh [serve]
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf _build/docs && mkdir -p _build/docs
for d in daily topics threads learn weekly; do
  [ -d "$d" ] && rsync -a --exclude '_seen_urls.txt' "$d" _build/docs/
done
cp index.md timeline.md feedback.md _build/docs/ 2>/dev/null || true
mkdir -p _build/docs/docs && cp docs/OPERATION.md _build/docs/docs/
mkdir -p _build/docs/tools && cp tools/extra.css _build/docs/tools/
cp tools/nav.yml _build/docs/.nav.yml
for d in daily weekly; do
  if ls _build/docs/$d/*.md >/dev/null 2>&1; then cp tools/nav_daily.yml _build/docs/$d/.nav.yml; fi
done && cp tools/tags.md _build/docs/tags.md
python3 tools/gen_indexes.py _build/docs
if [ "${1:-}" = "serve" ]; then exec mkdocs serve; fi
mkdocs build --strict
