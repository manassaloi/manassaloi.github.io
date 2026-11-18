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

- [x] Live date, top right, in red. Today's date in the reader's browser.
- [x] Footer nav pinned to the bottom. The current section is red, and posts and book notes count as their section.
- [x] Wordmark letters rise in on load (big wordmark only). Respects reduced motion.

### Home

- [x] One ink sketch per section from `assets/img/home/`, shown as cream ink on black.
- [x] A random sketch at rest. Hovering a footer link swaps in that section's sketch.

### Posts index and Book Notes index

- [x] Every entry's date in the mashed `MMDDYYYY` style (`11182026`), from the post date.
- [x] Posts index excludes book notes; Book Notes index shows only book notes.
- [x] Book notes: the title split at the last " - " into book (bright) and author (dim).
- [x] Book Notes: the book count ("243 books"), plus the updated date from the page's own line.

### Blog post

- [x] Reading time: words in the post ÷ 230, rounded, at least 1 ("4 min read").
- [x] Mashed date in the left column.
- [x] Neighbouring posts across the top: 6 posts around this one, this one in red. Book notes are skipped.
- [x] Older / Newer links at the end, also skipping book notes.

### Book note

- [x] Title split into book (heading) and author (under it and in the left column).
- [x] Highlight count: top-level paragraphs plus top-level bullets, matching the margin numbers.
- [x] Margin numbers `001`, `002`… on every highlight, whether written as a paragraph or a bullet.
  A real list inside a highlight keeps small dots.
- [x] The opening "**Note:** …" paragraph pulled out as a preface.
- [x] Neighbouring book notes across the top, and Older / Newer, among book notes only.

### Bookshelf

- [x] Each `###` heading becomes a shelf, pinned on the left while its books scroll.
- [x] Book count per shelf ("45 books"), and the total ("307 books on 21 shelves").
- [x] Each book split at the last " - " into title and author. The subtitle after ":" is hidden but kept as a tooltip.

### Proof of Work

- [x] Summary: the "As an engineer…" line as the large lede, and the "Role at Company: description"
  list as a company / role grid.
- [x] Each company heading pinned on the left with its tenure from the heading ("6.5 years").
- [x] Year span worked out from the role dates ("2018–2025").
- [x] Each role: dates in red, title, notes, and what shipped in two columns with small "press" links.

### Uses This

- [x] Each `##` section pinned on the left with an item count ("39 things").
- [x] Each item split at ": " into name (linked) and why.
- [x] Desk photo leads Hardware, gym photo leads Health.
- [x] The archive note and "Inspired by Uses This" line in the header.

### Links

- [x] Each `##` group pinned on the left.
- [x] Links to old posts show the post's mashed date, read from the URL.
- [x] Links to other sites show "↗" instead.

All ticked items were checked in the Jekyll build on 18 Nov 2026, against this mockup, at phone,
laptop and desktop widths. One intended difference: book notes with an image (like Competing Against
Luck) no longer number the image as a highlight, so their count is one lower than the mockup's.

### Where it lives in the real site

- `_plugins/theme.rb` works out everything in the checklist above.
- `_layouts/` (default, home, blog, booksummaries, post, page) and `_includes/` (head, header, footer, row).
- `_sass/theme.scss` and `_sass/theme/` hold the styles; `assets/css/style.scss` loads them.
- `assets/js/site.js` handles the live date, wordmark entrance and home sketches.
- The footer links are `nav` in `_config.yml`.

### Going live

The site is built by `.github/workflows/pages.yml` (GitHub Actions), so the plugin runs in production.

1. In the GitHub repo: Settings → Pages → Build and deployment → Source: **GitHub Actions**.
   Do this right before merging; until then `master` keeps building the old way.
2. Merge `redesign` into `master` and push. The workflow builds and publishes the site.
3. Check the run in the Actions tab, then the live site.
4. Delete this `_redesign/` folder and the `mockup` entry in `.claude/launch.json`.
