"""MkDocs hook: frontmatter の tags の共通数から「関連記事（自動）」セクションを各ページ末尾に付与する。
全ページの meta が揃った後（on_page_context）で page.content に追記する。"""
import posixpath

TYPES = {"daily", "topic", "thread", "learn", "weekly"}
MAX_ITEMS = 6


def on_page_context(context, page, config, nav):
    meta = page.meta or {}
    if meta.get("type") not in TYPES:
        return context
    my_tags = set(meta.get("tags") or [])
    explicit = set(meta.get("related") or [])
    if not my_tags and not explicit:
        return context
    scored = []
    files = config.get("_files_ref")
    for f in files.documentation_pages():
        if f.page is None or f.src_uri == page.file.src_uri:
            continue
        m = f.page.meta or {}
        if m.get("type") not in TYPES:
            continue
        score = len(my_tags & set(m.get("tags") or []))
        if f.src_uri in explicit or f.src_uri.replace(".md", "") in {e.replace(".md", "") for e in explicit}:
            score += 10
        if score > 0:
            scored.append((-score, str(m.get("updated") or m.get("date") or ""), f))
    scored.sort(key=lambda t: (t[0], t[1]))
    top = scored[:MAX_ITEMS]
    if not top:
        return context
    base = posixpath.dirname(page.url) or "."
    items = []
    for neg, _, f in top:
        rel = posixpath.relpath(f.url or ".", base)
        if not rel.endswith("/") and f.url.endswith("/"):
            rel += "/"
        label = "明示" if -neg >= 10 else f"共通タグ {-neg}"
        items.append(f'<li><a href="{rel}">{f.page.title}</a> <span class="rel-score">{label}</span></li>')
    page.content += (
        '<section class="related-auto"><h2 id="related-auto">関連記事（自動）</h2><ul>'
        + "".join(items) + "</ul></section>"
    )
    return context


def on_files(files, config):
    config["_files_ref"] = files
    return files
