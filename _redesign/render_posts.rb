# Renders every post in _posts with kramdown (the site's own renderer) and writes one JSON line per post.
# Usage (from the repo root): bundle exec ruby render_posts.rb <posts_dir> <out.jsonl>
require "kramdown"
require "yaml"
require "json"
require "date"

posts_dir, out_path = ARGV
out = File.open(out_path, "w")

Dir.glob(File.join(posts_dir, "*.{markdown,md}")).sort.reverse.each do |path|
  name = File.basename(path)
  m = name.match(/^(\d{4})-(\d{2})-(\d{2})-(.+)\.(markdown|md)$/) or next
  y, mo, d, slug = m[1], m[2], m[3], m[4]

  raw = File.read(path, encoding: "UTF-8")
  fm = {}
  body = raw
  if raw.start_with?("---")
    _, fm_text, body = raw.split(/^---\s*$/, 3)
    fm = (YAML.safe_load(fm_text.to_s, permitted_classes: [Date, Time]) rescue {}) || {}
    body ||= ""
  end

  # The only Liquid tag posts use is the webp image include.
  body = body.gsub(/\{%-?\s*include\s+webp-image\.html\s+(.*?)-?%\}/m) do
    args = Regexp.last_match(1)
    img = args[/img\s*=\s*"([^"]+)"/, 1] || ""
    alt = args[/alt\s*=\s*"([^"]*)"/, 1] || ""
    %(<img src="/assets/img/#{img.sub(/\.png$/, ".webp")}" alt="#{alt}">)
  end
  body = body.gsub(/\{%.*?%\}/m, "").gsub(/\{\{.*?\}\}/m, "")

  html = Kramdown::Document.new(body, input: "GFM", hard_wrap: false, syntax_highlighter: nil).to_html
  html = html.gsub(%r{https?://(www\.)?manassaloi\.com/}, "/")

  cats = fm["categories"]
  cats = cats.split if cats.is_a?(String)
  cats = Array(cats).map(&:to_s)
  tags = fm["tags"]
  tags = tags.split if tags.is_a?(String)
  tags = Array(tags).map(&:to_s)
  slug = fm["slug"].to_s unless fm["slug"].to_s.empty?

  url = "/" + (cats + [y, mo, d]).join("/") + "/#{slug}.html"
  words = body.gsub(/<[^>]+>/, " ").split.size

  out.puts({
    url: url, y: y, m: mo, d: d,
    title: (fm["title"] || slug.tr("-", " ")).to_s.strip,
    book: tags.include?("booksummaries") || cats.include?("booksummaries"),
    words: words,
    html: html
  }.to_json)
end
out.close
