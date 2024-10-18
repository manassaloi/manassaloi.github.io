source "https://rubygems.org"

# Jekyll version
gem "jekyll", "~> 4.3.1"

# Theme
gem "minima", "~> 2.5"

# Plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag", "~> 2.8"  # Add SEO tag plugin
end

# Development dependencies
group :development do
  gem "webrick", "~> 1.7"  # Required for Ruby 3.0+
end

# Platform-specific dependencies
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Windows-specific gem
gem "wdm", "~> 0.1.1", platforms: [:mingw, :x64_mingw, :mswin]

# JRuby-specific gem
gem "http_parser.rb", "~> 0.6.0", platforms: [:jruby]

# Uncomment the following line if you want to use GitHub Pages
# gem "github-pages", group: :jekyll_plugins
