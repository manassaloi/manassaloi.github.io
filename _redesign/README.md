# Redesign mockup

A static preview of the whole site in the new theme, built from the real posts and pages.
Jekyll ignores this folder (it starts with an underscore), so none of it is published.

It is a design reference, not the final implementation. Once the theme is built into the
Jekyll layouts, this folder can be deleted.

## Run it

From the repo root:

```bash
bundle exec ruby _redesign/render_posts.rb _posts _redesign/posts.jsonl
```

```bash
python3 -I _redesign/build.py . _redesign _redesign/site
```

```bash
python3 -m http.server 4016 --bind 127.0.0.1 --directory _redesign/site
```

Then open http://localhost:4016/.

## Files

- `render_posts.rb` renders every post with kramdown, the site's own markdown renderer.
- `build.py` builds every page: home, posts, book notes, bookshelf, proof of work, uses this, links.
- `site.css`, `site.js` hold the theme.
- `gambarino.woff2` is the display face, from Fontshare (ITF Free Font License). Lilex loads from Google Fonts.

`posts.jsonl` and `site/` are generated, and git ignores them.

## Production checklist

Everything below is worked out from the content, never typed in by hand. The production theme must
do all of it, recompute it on every build so new or edited content stays correct, and run on GitHub
Pages. Before merging into `master`, open each page type in the Jekyll preview next to the same page
in this mockup and tick the item off.

Things Manas writes by hand stay by hand: the "(Last updated: …)" line on each page, titles,
and the content itself.

### Every page

- [ ] Live date, top right, in red. Today's date in the reader's browser.
- [ ] Footer nav pinned to the bottom. The current section is red, and posts and book notes count as their section.
- [ ] Wordmark letters rise in on load (big wordmark only). Respects reduced motion.

### Home

- [ ] One ink sketch per section from `assets/img/home/`, shown as cream ink on black.
- [ ] A random sketch at rest. Hovering a footer link swaps in that section's sketch.

### Posts index and Book Notes index

- [ ] Every entry's date in the mashed `MMDDYYYY` style (`11182026`), from the post date.
- [ ] Posts index excludes book notes; Book Notes index shows only book notes.
- [ ] Book notes: the title split at the last " - " into book (bright) and author (dim).
- [ ] Book Notes: the book count ("243 books"), plus the updated date from the page's own line.

### Blog post

- [ ] Reading time: words in the post ÷ 230, rounded, at least 1 ("4 min read").
- [ ] Mashed date in the left column.
- [ ] Neighbouring posts across the top: 6 posts around this one, this one in red. Book notes are skipped.
- [ ] Older / Newer links at the end, also skipping book notes.

### Book note

- [ ] Title split into book (heading) and author (under it and in the left column).
- [ ] Highlight count: top-level paragraphs plus top-level bullets, matching the margin numbers.
- [ ] Margin numbers `001`, `002`… on every highlight, whether written as a paragraph or a bullet.
  A real list inside a highlight keeps small dots.
- [ ] The opening "**Note:** …" paragraph pulled out as a preface.
- [ ] Neighbouring book notes across the top, and Older / Newer, among book notes only.

### Bookshelf

- [ ] Each `###` heading becomes a shelf, pinned on the left while its books scroll.
- [ ] Book count per shelf ("45 books"), and the total ("307 books on 21 shelves").
- [ ] Each book split at the last " - " into title and author. The subtitle after ":" is hidden but kept as a tooltip.

### Proof of Work

- [ ] Summary: the "As an engineer…" line as the large lede, and the "Role at Company: description"
  list as a company / role grid.
- [ ] Each company heading pinned on the left with its tenure from the heading ("6.5 years").
- [ ] Year span worked out from the role dates ("2018–2025").
- [ ] Each role: dates in red, title, notes, and what shipped in two columns with small "press" links.

### Uses This

- [ ] Each `##` section pinned on the left with an item count ("39 things").
- [ ] Each item split at ": " into name (linked) and why.
- [ ] Desk photo leads Hardware, gym photo leads Health.
- [ ] The archive note and "Inspired by Uses This" line in the header.

### Links

- [ ] Each `##` group pinned on the left.
- [ ] Links to old posts show the post's mashed date, read from the URL.
- [ ] Links to other sites show "↗" instead.

### Open question for the build

GitHub Pages' standard build allows no custom plugins, so this has to be done in Liquid, CSS and
a little JavaScript. Most of it is easy. Proof of Work and the book-note highlight count are the
hardest. If Liquid can't match the mockup exactly, the fallback is to build the site with a GitHub
Actions workflow, which allows a small Ruby plugin to do the same parsing `build.py` does.
Decide this before starting the build. Nothing above gets dropped either way.
