"""_build/docs 内の各セクションに index.md（一覧）を frontmatter から生成する。"""
import os, re, sys, glob
import yaml

ROOT = sys.argv[1] if len(sys.argv) > 1 else "_build/docs"
IMPORTANCE_ICON = {"high": "🔴", "medium": "🟡", "low": "⚪"}


def read_meta(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except Exception:
            meta = {}
    title = meta.get("title")
    if not title:
        h = re.search(r"^# (.+)$", text, re.M)
        title = h.group(1).strip() if h else os.path.basename(path)
    return meta, str(title)


def entries(section, pattern="*.md"):
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, section, "**", pattern), recursive=True)):
        if os.path.basename(p) in ("index.md", "CURRICULUM.md") or os.path.basename(p).startswith("_"):
            continue
        meta, title = read_meta(p)
        rel = os.path.relpath(p, os.path.join(ROOT, section))
        out.append((meta, title, rel))
    return out


def write(section, title, lines):
    d = os.path.join(ROOT, section)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: {title}\nhide: [toc]\n---\n# {title}\n\n" + "\n".join(lines) + "\n")


def tagline(meta):
    tags = meta.get("tags") or []
    return " ".join(f"`{t}`" for t in tags[:4])


# daily: 新しい順
es = entries("daily")
es.sort(key=lambda e: str(e[0].get("date", e[2])), reverse=True)
lines = []
for meta, title, rel in es:
    lines.append(f"- [{title}]({rel}) — ニュース {meta.get('news_count', '?')} 件 ・ 約{meta.get('reading_minutes', '?')}分 {tagline(meta)}")
write("daily", "日次ダイジェスト", lines or ["（まだありません）"])

# topics: 更新順 + 五十音/アルファベット
es = entries("topics")
lines = ["## 最近更新されたトピック", ""]
for meta, title, rel in sorted(es, key=lambda e: str(e[0].get("updated", "")), reverse=True)[:15]:
    lines.append(f"- [{title}]({rel}) — 更新 {meta.get('updated', '?')} {tagline(meta)}")
lines += ["", "## すべてのトピック", ""]
for meta, title, rel in sorted(es, key=lambda e: e[1]):
    lines.append(f"- [{title}]({rel}) {tagline(meta)}")
write("topics", f"トピック（{len(es)}）", lines if es else ["（まだありません）"])

# threads
es = entries("threads")
lines = []
for meta, title, rel in sorted(es, key=lambda e: str(e[0].get("updated", "")), reverse=True):
    lines.append(f"- [{title}]({rel}) — {meta.get('status', '')} ・ 更新 {meta.get('updated', '?')} {tagline(meta)}")
write("threads", f"ストーリーライン（{len(es)}）", lines or ["（まだありません）"])

# learn: トラック別、番号順 + CURRICULUM リンク
TRACKS = [("intermediate", "中級"), ("beginner", "初心者"), ("practice", "実践"), ("instructor", "講師")]
lines = []
total = 0
for key, label in TRACKS:
    es = entries(f"learn/{key}")
    es.sort(key=lambda e: e[2])
    total += len(es)
    cur = os.path.join(ROOT, "learn", key, "CURRICULUM.md")
    lines.append(f"## {label}トラック（{len(es)} 本）")
    if os.path.exists(cur):
        lines.append(f"[カリキュラム全体を見る]({key}/CURRICULUM.md)")
    lines.append("")
    for meta, title, rel in es:
        lines.append(f"- [{title}]({key}/{rel}) — {meta.get('date', '')} ・ 約{meta.get('reading_minutes', '?')}分 {tagline(meta)}")
    lines.append("")
write("learn", f"学習トラック（{total}）", lines)

# weekly
es = entries("weekly")
lines = []
for meta, title, rel in sorted(es, key=lambda e: str(e[0].get("week", e[2])), reverse=True):
    lines.append(f"- [{title}]({rel})")
write("weekly", "週まとめ", lines or ["（まだありません）"])
print("indexes generated")
