AUTHOR = 'Joel Harris'
SITENAME = 'Joel Harris'
SITEURL = 'https://joelharr.is'

THEME = 'theme'
PATH = 'content'

STATIC_PATHS = [
    'extra'
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Pacific/Auckland'
DEFAULT_LANG = 'en'
SUMMARY_MAX_LENGTH = 10

# Markdown settings
# I use the table of contents and code hightlighting extensions
MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {'title': 'Table of contents:'},
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {}
  },
  'output_format': 'html5'
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/joel-davidson-harris'),
    ('GitHub', 'https://github.com/joeldavidsonharris'),
    ('Mail', 'mailto:joeldavidsonharris@gmail.com')
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
