"""Builds the whole manassaloi.com theme mockup from the repo's real content.

Usage: python3 -I build.py <repo_dir> <gen_dir> <out_site_dir>
Needs gen_dir/posts.jsonl from render_posts.rb, plus site.css, site.js and gambarino.woff2 in gen_dir.
See README.md in this folder.
"""
import html, json, os, re, shutil, sys

REPO, GEN, OUT = (os.path.abspath(p) for p in sys.argv[1:4])
esc = html.escape

NAV = [
    ("posts", "Posts", "/posts/", "tile-1"),
    ("notes", "Book Notes", "/booksummaries/", "tile-4"),
    ("shelf", "Bookshelf", "/bookshelf/", "tile-2"),
    ("pow", "Proof of Work", "/proofofwork/", "tile-6"),
    ("uses", "Uses This", "/usesthis/", "tile-3"),
    ("links", "Links", "/links/", "tile-5"),
]

# ---------------------------------------------------------------- helpers
def mash(y, m, d):
    return f"{m}{d}{y}"

def local(url):
    return re.sub(r"^https?://(www\.)?manassaloi\.com/", "/", url)

def inline(s):
    """Tiny inline-markdown renderer for the structured pages."""
    s = esc(s.strip(), quote=False)
    def link(m):
        text, url = m.group(1), local(html.unescape(m.group(2)).strip())
        ext = url.startswith("http")
        attrs = ' target="_blank" rel="noopener"' if ext else ""
        return f'<a href="{esc(url)}"{attrs}>{text}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

def body_md(path):
    raw = open(os.path.join(REPO, path), encoding="utf-8").read()
    return raw.split("---", 2)[2] if raw.startswith("---") else raw

def updated(md):
    m = re.search(r"\(Last updated:\s*([^)]+)\)", md)
    return m.group(1).strip() if m else ""

MARK = '<span>manas</span><span><i>saloi</i>.</span>'

def shell(title, inner, current=None, body_class="", home=False):
    links = []
    for key, label, href, sketch in NAV:
        cur = ' aria-current="page"' if key == current else ""
        sk = f' data-sketch="{sketch}"' if home else ""
        links.append(f'<a href="{href}"{cur}{sk}>{label}</a>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lilex:wght@400&display=swap">
<link rel="preload" href="/theme/gambarino.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/theme/site.css">
</head>
<body class="{body_class}">
{inner}
<div class="fade" aria-hidden="true"></div>
<nav class="foot" aria-label="Site">
  {chr(10).join("  " + l for l in links).strip()}
</nav>
<script src="/theme/site.js" defer></script>
</body>
</html>
"""

def big_frame(inner):
    return (f'<a class="mark mark--big" href="/" aria-label="manas saloi, home">{MARK}</a>\n'
            f'<div class="now now--fixed" data-now></div>\n{inner}')

def compact(mid, inner, mid_class=""):
    return (f'<header class="top">\n'
            f'  <a class="mark mark--small" href="/" aria-label="manas saloi, home">{MARK}</a>\n'
            f'  <div class="top-mid {mid_class}">{mid}</div>\n'
            f'  <div class="now" data-now></div>\n'
            f'</header>\n<main class="page">\n{inner}\n</main>')

def write(rel, text):
    path = os.path.join(OUT, rel.lstrip("/"))
    if path.endswith("/"):
        path += "index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def row(url, date, title, extra="", current=False, clip=False):
    cur = ' aria-current="page"' if current else ""
    cls = "row row--clip" if clip else "row"
    return (f'<a class="{cls}" href="{esc(url)}"{cur}><time>{date}</time>'
            f'<span class="t">{esc(title)}{extra}</span></a>')

def split_book(title):
    if " - " in title:
        book, author = title.rsplit(" - ", 1)
        return book.strip(), author.strip()
    return title, ""

# ---------------------------------------------------------------- content
ALL = [json.loads(l) for l in open(os.path.join(GEN, "posts.jsonl"), encoding="utf-8")]
POSTS = [p for p in ALL if not p["book"]]
BOOKS = [p for p in ALL if p["book"]]
URLS = {p["url"] for p in ALL}

# fresh output dir
if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, "theme", "sketches"))
shutil.copy(os.path.join(GEN, "site.css"), os.path.join(OUT, "theme", "site.css"))
shutil.copy(os.path.join(GEN, "site.js"), os.path.join(OUT, "theme", "site.js"))
shutil.copy(os.path.join(GEN, "gambarino.woff2"), os.path.join(OUT, "theme", "gambarino.woff2"))
for i in range(1, 7):
    shutil.copy(os.path.join(REPO, "assets/img/home", f"tile-{i}.webp"), os.path.join(OUT, "theme/sketches"))
os.symlink(os.path.join(REPO, "assets"), os.path.join(OUT, "assets"))

# ---------------------------------------------------------------- home
write("/", shell("manas saloi",
    big_frame('<div class="stage" id="stage" aria-hidden="true"></div>'),
    body_class="home", home=True))

# ---------------------------------------------------------------- posts index
rows = "\n".join(row(p["url"], mash(p["y"], p["m"], p["d"]), p["title"]) for p in POSTS)
write("/posts/", shell("Posts · manas saloi",
    big_frame(f'<main class="index" aria-label="Posts">\n{rows}\n</main>'), current="posts"))

# ---------------------------------------------------------------- book notes index
bn_md = body_md("booksummaries.md")
rows = []
for p in BOOKS:
    book, author = split_book(p["title"])
    a = f'<span class="a">{esc(author)}</span>' if author else ""
    rows.append(row(p["url"], mash(p["y"], p["m"], p["d"]), book, extra=a))
aside = f"""<div class="aside">
  <p>Notes on some of the books I have read. It is not exhaustive; just a collection of my favourite excerpts.</p>
  <p>If you like one of these summaries, buy the book and support the author.</p>
  <p><a href="https://www.goodreads.com/user/show/9698257-manas-saloi" target="_blank" rel="noopener">Goodreads ↗</a></p>
  <p>{len(BOOKS)} books · updated {esc(updated(bn_md))}</p>
</div>"""
write("/booksummaries/", shell("Book Notes · manas saloi",
    big_frame(aside + f'\n<main class="index" aria-label="Book notes">\n{chr(10).join(rows)}\n</main>'),
    current="notes"))

# ---------------------------------------------------------------- post + book note pages
def neighbours(lst, i, label_fn):
    start = max(0, min(i - 2, len(lst) - 6))
    out = []
    for j in range(start, min(len(lst), start + 6)):
        q = lst[j]
        title, extra = label_fn(q)
        out.append(row(q["url"], mash(q["y"], q["m"], q["d"]), title, extra=extra, current=(j == i), clip=True))
    return "\n".join(out)

def pager(lst, i, older_label, newer_label, label_fn):
    parts = []
    if i + 1 < len(lst):
        q = lst[i + 1]
        parts.append(f'<a class="prev" href="{q["url"]}">← {older_label}<span>{esc(label_fn(q)[0])}</span></a>')
    if i > 0:
        q = lst[i - 1]
        parts.append(f'<a class="next" href="{q["url"]}">{newer_label} →<span>{esc(label_fn(q)[0])}</span></a>')
    return f'<nav class="pager" aria-label="More">{"".join(parts)}</nav>'

post_label = lambda q: (q["title"], "")
for i, p in enumerate(POSTS):
    mins = max(1, round(p["words"] / 230))
    left = (f'<div class="meta"><time>{mash(p["y"], p["m"], p["d"])}</time>'
            f'<span>{mins} min read</span><span class="gap"></span>'
            f'<a href="/posts/">← All posts</a></div>')
    article = (f'<article class="post"><h1>{esc(p["title"])}</h1>'
               f'<div class="prose">{p["html"]}</div>'
               f'{pager(POSTS, i, "Older", "Newer", post_label)}</article>')
    inner = f'<div class="split"><div class="left">{left}</div><div class="right">{article}</div></div>'
    write(p["url"], shell(f'{p["title"]} · manas saloi',
        compact(neighbours(POSTS, i, post_label), inner, "neighbours"), current="posts"))

from html.parser import HTMLParser

class _Highlights(HTMLParser):
    """Counts highlights the way the CSS numbers them: top-level <p>, plus <li> directly inside a top-level list."""
    VOID = {"br", "img", "hr", "input", "meta", "link", "source", "wbr"}
    def __init__(self):
        super().__init__()
        self.stack, self.n = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        if (tag == "p" and not self.stack) or (tag == "li" and len(self.stack) == 1 and self.stack[0] in ("ul", "ol")):
            self.n += 1
        self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass

def count_highlights(h):
    p = _Highlights()
    p.feed(h)
    return p.n

def book_label(q):
    book, author = split_book(q["title"])
    return book, (f'<span class="a">{esc(author)}</span>' if author else "")

for i, p in enumerate(BOOKS):
    book, author = split_book(p["title"])
    h = p["html"]
    preface = ""
    m = re.match(r"\s*<p>(<strong>Note:?</strong>.*?)</p>", h, re.S)
    if m:
        preface = f'<p class="preface">{m.group(1)}</p>'
        h = h[m.end():]
    count = count_highlights(h)
    left = (f'<div class="meta"><span>Book notes</span>'
            + (f'<span>{esc(author)}</span>' if author else "")
            + f'<span>{count} highlights</span><time>{mash(p["y"], p["m"], p["d"])}</time>'
            f'<span class="gap"></span><a href="/booksummaries/">← All book notes</a></div>')
    by = f'<p class="by">{esc(author)}</p>' if author else ""
    article = (f'<article class="note"><h1>{esc(book)}</h1>{by}{preface}'
               f'<div class="clips">{h}</div>'
               f'{pager(BOOKS, i, "Older", "Newer", book_label)}</article>')
    inner = f'<div class="split"><div class="left">{left}</div><div class="right">{article}</div></div>'
    write(p["url"], shell(f'{p["title"]} · manas saloi',
        compact(neighbours(BOOKS, i, book_label), inner, "neighbours"), current="notes"))

# ---------------------------------------------------------------- section page helper
def section(label, count, right):
    return (f'<section class="sec split"><div class="left sec-label"><h2>{esc(label)}</h2>'
            f'<span class="count">{count}</span></div><div class="right">{right}</div></section>')

def mid(name, *lines):
    return f"<p>{name}</p>" + "".join(f'<p class="dim">{l}</p>' for l in lines if l)

# ---------------------------------------------------------------- bookshelf
md = body_md("bookshelf.md")
cats, total = [], 0
for chunk in re.split(r"^###\s+", md, flags=re.M)[1:]:
    head, _, rest = chunk.partition("\n")
    books = []
    for m in re.finditer(r"^\s*[+*-]\s+\[(.+?)\]\((\S+?)\)", rest, re.M):
        full, url = m.group(1).strip(), m.group(2)
        title, author = split_book(re.sub(r"\s+", " ", full))
        short = title.split(": ")[0]
        books.append(f'<a class="book" href="{esc(url)}" target="_blank" rel="noopener" title="{esc(full)}">'
                     f'<span>{esc(short)}</span><span class="a">{esc(author)}</span></a>')
    if books:
        total += len(books)
        cats.append(section(head.strip(), f"{len(books)} books", "\n".join(books)))
top = mid("Bookshelf",
          'A list of books I\'ve found useful. Other books I have read: '
          '<a class="inline" href="https://www.goodreads.com/user/show/9698257-manas-saloi" target="_blank" rel="noopener">Goodreads</a>.',
          f"{total} books on {len(cats)} shelves · updated {esc(updated(md))}")
write("/bookshelf/", shell("Bookshelf · manas saloi", compact(top, "\n".join(cats)), current="shelf"))

# ---------------------------------------------------------------- proof of work
md = body_md("pow.md")
head, *companies = re.split(r"^###\s+", md, flags=re.M)
lede = next((l.strip() for l in head.splitlines() if l.strip().startswith("As an engineer")), "")
career = []
for m in re.finditer(r"^- (.+?) at (.+?): (.+)$", head, re.M):
    career.append(f'<span class="co">{inline(m.group(2))}</span><span class="what">{inline(m.group(1))} · {inline(m.group(3))}</span>')
blocks = [section("Summary", "", f'<p class="lede">{inline(lede)}</p><div class="career">{"".join(career)}</div>')]

for chunk in companies:
    title_line, _, rest = chunk.partition("\n")
    title_line = title_line.strip().strip("#").strip()
    tm = re.match(r"(.+?)\s*\((.+?)\)\s*$", title_line)
    name, tenure = (tm.group(1), tm.group(2)) if tm else (title_line, "")
    intro, roles, role = [], [], None
    for line in rest.splitlines():
        if not line.strip():
            continue
        top_item = re.match(r"^- (.*)$", line)
        sub_item = re.match(r"^\s{2,}[-*] (.*)$", line)
        if top_item:
            text = top_item.group(1).strip()
            dm = re.match(r"^\*\*(.+)\*\*$", text)
            if dm:
                role = {"when": dm.group(1), "title": None, "desc": [], "ship": []}
                roles.append(role)
            elif role:
                (role["desc"].append(text) if role["title"] else role.__setitem__("title", text))
            else:
                intro.append(["item", text, []])
        elif sub_item:
            if role:
                role["ship"].append(sub_item.group(1).strip())
            elif intro and intro[-1][0] == "item":
                intro[-1][2].append(sub_item.group(1).strip())
        else:
            (role["desc"].append(line.strip()) if role else intro.append(["para", line.strip(), []]))
    years = sorted({int(y) for r in roles for y in re.findall(r"\b(?:19|20)\d{2}\b", r["when"])})
    span = f"{years[0]}–{years[-1]}" if years else ""
    parts = []
    if intro:
        h = []
        for kind, text, kids in intro:
            if kind == "item":
                h.append(f"<p>{inline(text)}</p>")
                if kids:
                    h.append("<ul>" + "".join(f"<li>{inline(k)}</li>" for k in kids) + "</ul>")
            else:
                h.append(f'<p class="dim">{inline(text)}</p>')
        parts.append(f'<div class="intro">{"".join(h)}</div>')
    if roles:
        rs = []
        for r in roles:
            ship = ("<ul class=\"ship\">" + "".join(f"<li>{inline(s)}</li>" for s in r["ship"]) + "</ul>") if r["ship"] else ""
            desc = "".join(f'<p class="desc">{inline(d)}</p>' for d in r["desc"])
            rs.append(f'<div class="role"><div class="when">{esc(r["when"])}</div>'
                      f'<p class="title">{inline(r["title"] or "")}</p>{desc}{ship}</div>')
        parts.append(f'<div class="roles" style="margin-top:{"28px" if intro else "0"}">{"".join(rs)}</div>')
    meta = " · ".join(x for x in [tenure.replace("~", "~"), span] if x)
    blocks.append(section(name, esc(meta), "".join(parts)))

top = mid("Proof of Work", f"Updated {esc(updated(md))}")
write("/proofofwork/", shell("Proof of Work · manas saloi", compact(top, "\n".join(blocks)), current="pow"))

# ---------------------------------------------------------------- uses this
md = body_md("usesthis.md")
note = re.search(r"^Note:\s*(.+)$", md, re.M)
blocks = []
for chunk in re.split(r"^##\s+(?!#)", md, flags=re.M)[1:]:
    head, _, rest = chunk.partition("\n")
    groups, cur, n = [], {"label": "", "items": []}, 0
    groups.append(cur)
    for line in rest.splitlines():
        sm = re.match(r"^#{3,4}\s+(.+)$", line)
        im = re.match(r"^\s*\+\s+(.*)$", line)
        if sm:
            cur = {"label": sm.group(1).strip(), "items": []}
            groups.append(cur)
        elif im:
            text = im.group(1).strip()
            lm = re.match(r"^\[(.+?)\]\((\S*?)\)\s*:?\s*(.*)$", text)
            if lm:
                name, url, why = lm.group(1).strip(), lm.group(2), lm.group(3)
                if url and not url.startswith("http"):
                    url = "https://" + url
                left = f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(name)}</a>'
            else:
                name, _, why = text.partition(":")
                left = f"<span>{inline(name)}</span>"
            cur["items"].append(f'<div class="gear">{left}<span class="why">{inline(why)}</span></div>')
            n += 1
    photo = ""
    if head.strip() == "Hardware":
        photo = '<img class="photo" src="/assets/img/usesthis.webp" alt="Uses this" width="1600" height="1200" style="margin-bottom:36px">'
    if head.strip() == "Health":
        photo = '<img class="photo" src="/assets/img/homegym.webp" alt="Home gym" width="768" height="1024" loading="lazy" style="max-width:420px;margin-bottom:36px">'
    body = photo + "".join(
        (f'<p class="sub">{esc(g["label"])}</p>' if g["label"] else "") + f'<div class="gears">{"".join(g["items"])}</div>'
        for g in groups if g["items"])
    blocks.append(section(head.strip(), f"{n} things", body))
top = mid("Uses This",
          'Inspired by <a class="inline" href="https://usesthis.com/" target="_blank" rel="noopener">Uses This</a>, '
          "the tools, services, and techniques I'm using to get things done.",
          esc(note.group(1)) if note else "",
          f"Updated {esc(updated(md))}")
write("/usesthis/", shell("Uses This · manas saloi", compact(top, "\n".join(blocks)), current="uses"))

# ---------------------------------------------------------------- links
md = body_md("links.md")
blocks, missing = [], []
for chunk in re.split(r"^##\s+", md, flags=re.M)[1:]:
    head, _, rest = chunk.partition("\n")
    parts = []
    for line in rest.splitlines():
        line = line.strip()
        if not line:
            continue
        found = list(re.finditer(r"\[([^\]]+)\]\((\S+?)\)", line))
        is_item = line.startswith(("- ", "* ", "+ "))
        if not is_item:
            say = re.sub(r"\*\*|\[([^\]]+)\]\((\S+?)\)", "", line).strip().rstrip(":").strip()
            if say:
                parts.append(f'<p class="say">{inline(say)}</p>')
        for m in found:
            text, url = m.group(1), local(m.group(2))
            dm = re.match(r"^/(\d{4})/(\d{2})/(\d{2})/", url)
            if dm:
                if url not in URLS:
                    missing.append(url)
                parts.append(row(url, mash(*dm.groups()), text))
            else:
                parts.append(f'<a class="row" href="{esc(url)}" target="_blank" rel="noopener"><time>↗</time><span class="t">{esc(text)}</span></a>')
    blocks.append(section(head.strip(), "", "".join(parts)))
top = mid("Links", f"Updated {esc(updated(md))}")
write("/links/", shell("Links · manas saloi", compact(top, f'<div class="links">{"".join(blocks)}</div>'), current="links"))

print(f"built {len(POSTS)} posts, {len(BOOKS)} book notes, 7 pages; shelf={total} books; links missing locally: {missing}")
