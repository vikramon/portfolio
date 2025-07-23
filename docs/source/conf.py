# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Vikram Srinivasan - Portfolio'
author = 'Vikram Srinivasan'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
#   'sphinx_new_tab_link', ##This will open links in a new tab if enabled.
]

# new_tab_link_show_external_link_icon = True ## This shows the open links in new tab icon.

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# html_theme = 'alabaster'
# html_static_path = ['_static']

# -- Options for other output formats ----------------------------------------

# e.g., latex_documents = [(master_doc, 'projectname.tex', 'Project Name Documentation', 'Author Name', 'manual')]

# The master toctree document.
master_doc = 'main/title_main'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'body_max_width' : 'none',
    'page_width': '2000',
}
