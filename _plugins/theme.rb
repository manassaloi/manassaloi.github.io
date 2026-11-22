# frozen_string_literal: true

# Works out everything the theme shows that isn't typed in by hand, on every build:
# book-note titles and authors, mashed and long dates, each post's neighbours and older/newer links,
# and the sections of Bookshelf, Proof of Work, Uses This and Links.
#
# Nothing here is typed in by hand, so new and edited content stays correct on every build.
# Reading time is plain Liquid in _layouts/post.html. The design reference this was ported from
# (the _redesign/ mockup and its checklist) is in git history, in commit 8ed31e2.

require "cgi"
require "date"

module ManasTheme
  BOOK_TAG = "booksummaries"
  OWN_SITE = %r{\Ahttps?://(www\.)?manassaloi\.com/}.freeze
  LAST_UPDATED = /^\(Last updated:\s*([^)]+)\)\s*$/.freeze

  # Pages whose markdown is turned into pinned-label sections by _layouts/page.html.
  SECTION_PAGES = {
    "/bookshelf/" => "bookshelf",
    "/proofofwork/" => "pow",
    "/usesthis/" => "uses",
    "/links/" => "links",
  }.freeze

  module_function

  def book?(doc)
    (Array(doc.data["tags"]) + Array(doc.data["categories"])).include?(BOOK_TAG)
  end

  # Two date formats, and only two. List rows use the compact mash; every other date is long.

  # 18112026: day, month, year run together (epilepsywarning style, Indian order). List rows only.
  def mash(date)
    date.strftime("%d%m%Y")
  end

  # 18 Nov 2026: every date that isn't in a list row.
  def long(date)
    date.strftime("%-d %b %Y")
  end

  # A hand-typed date ("05 June 2025") in the long format ("5 Jun 2025"). Text that isn't a date stays as typed.
  def long_text(text)
    long(Date.parse(text))
  rescue ArgumentError
    text
  end

  MONTHS = %w[jan feb mar apr may jun jul aug sep oct nov dec].freeze

  # "April 2024 - April 2025" -> "Apr 2024 – Apr 2025": the long format without the day, en dash
  # between. Months match on their first three letters, so "Septmber" still reads as Sep. Anything
  # else stays as typed.
  def month_range(text)
    ends = text.split(/\s+[-–]\s+/).map do |part|
      m = part.strip.match(/\A([A-Za-z]{3})[A-Za-z]*\.?\s+((?:19|20)\d{2})\z/)
      month = m && MONTHS.index(m[1].downcase)
      return text unless month

      Date.new(m[2].to_i, month + 1, 1).strftime("%b %Y")
    end
    ends.join(" – ")
  end

  # "The Untethered Soul - Michael Alan Singer" -> ["The Untethered Soul", "Michael Alan Singer"]
  def split_book(title)
    i = title.rindex(" - ")
    i ? [title[0...i].strip, title[(i + 3)..].strip] : [title.strip, ""]
  end

  def local(url)
    url.sub(OWN_SITE, "/")
  end

  class Generator < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      @site = site
      @markdown = site.find_converter_instance(Jekyll::Converters::Markdown)

      newest_first = site.posts.docs.reverse
      books, posts = newest_first.partition { |doc| ManasTheme.book?(doc) }
      annotate(posts, false)
      annotate(books, true)

      site.pages.each do |page|
        case page.url
        when "/booksummaries/" then take_updated(page)
        when *SECTION_PAGES.keys then section_page(page)
        end
      end
    end

    private

    # ---------- posts and book notes ----------

    def annotate(list, is_book)
      list.each do |doc|
        title = doc.data["title"].to_s
        doc.data["is_book"] = is_book
        doc.data["date_mash"] = ManasTheme.mash(doc.date)
        doc.data["date_long"] = ManasTheme.long(doc.date)
        doc.data["book_title"], doc.data["book_author"] = ManasTheme.split_book(title) if is_book
      end

      list.each_with_index do |doc, i|
        start = [[i - 2, list.size - 6].min, 0].max
        doc.data["neighbours"] = list[start, 6].map { |other| entry(other, other.equal?(doc)) }
        doc.data["older"] = list[i + 1] && entry(list[i + 1])
        doc.data["newer"] = i.positive? ? entry(list[i - 1]) : nil
      end
    end

    def entry(doc, current = false)
      {
        "url" => doc.url,
        "date" => doc.data["date_mash"],
        "title" => doc.data["is_book"] ? doc.data["book_title"] : doc.data["title"].to_s,
        "author" => doc.data["is_book"] ? doc.data["book_author"] : "",
        "current" => current,
      }
    end

    # ---------- section pages ----------

    # Moves the "(Last updated: …)" line out of the body; the layout shows it in the header, as a long date.
    def take_updated(page)
      typed = page.content[LAST_UPDATED, 1]&.strip
      page.data["updated"] = typed && ManasTheme.long_text(typed)
      page.content = page.content.sub(LAST_UPDATED, "")
    end

    def section_page(page)
      take_updated(page)
      kind = SECTION_PAGES.fetch(page.url)
      page.data["kind"] = kind
      send("build_#{kind}", page, page.content)
    end

    def build_bookshelf(page, md)
      intro, *chunks = md.split(/^###\s+/)
      shelves = chunks.filter_map do |chunk|
        name, rest = chunk.split("\n", 2)
        books = rest.to_s.scan(/^\s*[+*-]\s+\[(.+?)\]\((\S+?)\)/).map do |full, url|
          full = full.gsub(/\s+/, " ").strip
          title, author = ManasTheme.split_book(full)
          { "title" => title.split(": ").first, "full" => full, "author" => author, "url" => url }
        end
        { "name" => name.strip, "books" => books } unless books.empty?
      end
      page.data["intro_html"] = render(intro)
      page.data["shelves"] = shelves
      page.data["total"] = shelves.sum { |shelf| shelf["books"].size }
    end

    def build_uses(page, md)
      intro, *chunks = md.split(/^##\s+(?!#)/)
      page.data["intro_html"] = render(intro)
      page.data["sections"] = chunks.map do |chunk|
        name, rest = chunk.split("\n", 2)
        groups = [{ "label" => "", "items" => [] }]
        photo = nil
        rest.to_s.each_line do |line|
          if (m = line.match(/^\#{3,4}\s+(.+)$/))
            groups << { "label" => m[1].strip, "items" => [] }
          elsif (m = line.match(/\{%-?\s*include\s+webp-image\.html\s+(.*?)-?%\}/))
            photo ||= photo_from_include(m[1])
          elsif (m = line.match(/^\s*\+\s+(.*)$/))
            groups.last["items"] << gear(m[1].strip)
          end
        end
        groups.reject! { |group| group["items"].empty? }
        { "name" => name.strip, "photo" => photo, "groups" => groups, "count" => groups.sum { |g| g["items"].size } }
      end
    end

    def build_links(page, md)
      _intro, *chunks = md.split(/^##\s+/)
      page.data["groups"] = chunks.map do |chunk|
        name, rest = chunk.split("\n", 2)
        entries = []
        rest.to_s.each_line do |line|
          line = line.strip
          next if line.empty?

          unless line.start_with?("- ", "* ", "+ ")
            say = line.gsub(/\*\*|\[([^\]]+)\]\((\S+?)\)/, "").strip.delete_suffix(":").strip
            entries << { "kind" => "say", "html" => inline(say) } unless say.empty?
          end
          line.scan(/\[([^\]]+)\]\((\S+?)\)/).each do |text, url|
            url = ManasTheme.local(url)
            if (d = url.match(%r{\A/(\d{4})/(\d{2})/(\d{2})/}))
              entries << { "kind" => "post", "url" => url, "date" => "#{d[3]}#{d[2]}#{d[1]}", "text" => text }
            else
              entries << { "kind" => "external", "url" => url, "text" => text }
            end
          end
        end
        { "name" => name.strip, "entries" => entries }
      end
    end

    def build_pow(page, md)
      head, *chunks = md.split(/^###\s+/)
      # The lede is the first plain line: not a "(…)" aside, not a list item.
      lede = head.lines.map(&:strip).find { |l| !l.empty? && !l.start_with?("(", "-", "*", "+", "#") }
      page.data["lede_html"] = inline(lede.to_s)
      page.data["career"] = head.scan(/^- (.+?) at (.+?): (.+)$/).map do |role, company, what|
        { "company" => inline(company), "role" => inline(role), "what" => inline(what) }
      end
      page.data["companies"] = chunks.map { |chunk| company(chunk) }
    end

    # One "### Company (tenure) ###" chunk: intro lines, then roles that each start with a bold date line.
    def company(chunk)
      title_line, rest = chunk.split("\n", 2)
      title_line = title_line.strip.gsub(/\A#+|#+\z/, "").strip
      m = title_line.match(/\A(.+?)\s*\((.+?)\)\s*\z/)
      name, tenure = m ? [m[1], m[2]] : [title_line, ""]

      intro = []
      roles = []
      role = nil
      rest.to_s.each_line do |raw|
        line = raw.chomp
        next if line.strip.empty?

        if (top = line.match(/\A- (.*)\z/))
          text = top[1].strip
          if (when_line = text.match(/\A\*\*(.+)\*\*\z/))
            role = { "when" => ManasTheme.month_range(when_line[1]), "title" => nil, "desc" => [], "ship" => [] }
            roles << role
          elsif role
            role["title"] ? role["desc"] << inline(text) : role["title"] = inline(text)
          else
            intro << { "kind" => "item", "html" => inline(text), "kids" => [] }
          end
        elsif (sub = line.match(/\A\s{2,}[-*] (.*)\z/))
          if role
            role["ship"] << inline(sub[1].strip)
          elsif intro.last && intro.last["kind"] == "item"
            intro.last["kids"] << inline(sub[1].strip)
          end
        elsif role
          role["desc"] << inline(line.strip)
        else
          intro << { "kind" => "para", "html" => inline(line.strip), "kids" => [] }
        end
      end

      years = roles.flat_map { |r| r["when"].scan(/\b(?:19|20)\d{2}\b/) }.map(&:to_i).uniq.sort
      span = years.empty? ? "" : "#{years.first}–#{years.last}"
      { "name" => name, "meta" => [tenure, span].reject(&:empty?).join(" · "), "intro" => intro, "roles" => roles }
    end

    # ---------- helpers ----------

    # "[Name](url): why it's here" -> linked name and the reason.
    def gear(text)
      if (m = text.match(/\A\[(.+?)\]\((\S*?)\)\s*:?\s*(.*)\z/))
        url = m[2]
        url = "https://#{url}" unless url.empty? || url.start_with?("http", "/")
        { "name" => CGI.escapeHTML(m[1].strip), "url" => url, "why" => inline(m[3]) }
      else
        name, why = text.split(":", 2)
        { "name" => inline(name.to_s), "url" => nil, "why" => inline(why.to_s) }
      end
    end

    # The include names a .png; the page serves its .webp twin, as _includes/webp-image.html does.
    def photo_from_include(args)
      img = args[/img\s*=\s*"([^"]+)"/, 1] or return nil
      alt = args[/alt\s*=\s*"([^"]*)"/, 1].to_s
      src = "/assets/img/#{img.sub(/\.png\z/, '.webp')}"
      width, height = webp_size(File.join(@site.source, src))
      {
        "src" => src,
        "alt" => alt,
        "width" => width,
        "height" => height,
        "portrait" => width && height && height > width,
      }
    end

    # Width and height from a WebP header, so the page can reserve space before the photo loads.
    # Handles all three WebP flavours: lossy (VP8), lossless (VP8L) and extended (VP8X).
    def webp_size(path)
      head = File.binread(path, 30)
      return [nil, nil] unless head && head.bytesize == 30 && head[0, 4] == "RIFF" && head[8, 4] == "WEBP"

      b = head.bytes
      case head[12, 4]
      when "VP8 " then [b[26] | ((b[27] & 0x3F) << 8), b[28] | ((b[29] & 0x3F) << 8)]
      when "VP8L" then [1 + (b[21] | ((b[22] & 0x3F) << 8)), 1 + ((b[22] >> 6) | (b[23] << 2) | ((b[24] & 0x0F) << 10))]
      when "VP8X" then [1 + (b[24] | (b[25] << 8) | (b[26] << 16)), 1 + (b[27] | (b[28] << 8) | (b[29] << 16))]
      else [nil, nil]
      end
    rescue Errno::ENOENT
      [nil, nil]
    end

    # Markdown to HTML with the site's own renderer, minus the "(Last updated…)" line and Liquid tags.
    def render(md)
      text = md.to_s.gsub(LAST_UPDATED, "").gsub(/\{%.*?%\}/m, "")
      localise(@markdown.convert(text).strip)
    end

    # One line of markdown to inline HTML.
    def inline(text)
      html = @markdown.convert(text.to_s.strip).strip
      localise(html.delete_prefix("<p>").delete_suffix("</p>"))
    end

    def localise(html)
      html.gsub(%r{href="https?://(www\.)?manassaloi\.com/}, 'href="/')
    end
  end

  # Book-note filters: pull the opening "**Note:** …" paragraph out as a preface.
  module Filters
    PREFACE = %r{\A\s*<p>(<strong>Note:?</strong>.*?)</p>}m.freeze

    def note_preface(html)
      html.to_s[PREFACE, 1]
    end

    def note_body(html)
      html.to_s.sub(PREFACE, "")
    end

    # A woff2 file in the repo as a data URI, so assets/css/style.scss can carry the site's two
    # fonts inside the stylesheet. Usage: {{ "assets/fonts/lilex.woff2" | font_data_uri }}
    def font_data_uri(path)
      site = @context.registers[:site]
      file = File.join(site.source, path.to_s)
      "data:font/woff2;base64,#{[File.binread(file)].pack('m0')}"
    end
  end
end

Liquid::Template.register_filter(ManasTheme::Filters)
