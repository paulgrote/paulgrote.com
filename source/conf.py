# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Paul Grote'
author = 'Paul Grote'
copyright = '© %Y, Paul Grote'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        "sphinx_design",
        "sphinx_iconify"
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Paul Grote'
html_theme = 'shibuya'
html_static_path = ['_static']
html_favicon = '_static/favicon-16x16.png'
html_extra_path = ['robots.txt']
html_theme_options = {
    "linkedin_url": "https://www.linkedin.com/in/paul-grote/",
    "github_url": "https://github.com/paulgrote",
    "accent_color": "blue",
    "nav_links": [
        {
            "title": "CV",
            "url": "cv"
        },
        {
            "title": "Sample Work",
            "url": "samples"
        },
    ],
    "nav_links_align": "right",
}

#--Global substitutions ------------------------------------------------------
rst_prolog = f"""
.. |author| replace:: {author}
.. |dot| unicode:: U+2219
"""
