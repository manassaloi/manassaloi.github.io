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
