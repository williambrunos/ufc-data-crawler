# -- Project information -----------------------------------------------------

project = 'ufc-data-crawler'
author = 'William Bruno Sales de Paula Lima'
version = '0.0.1'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'pyramid'
html_static_path = ['_static']
html_css_files = ['custom.css']