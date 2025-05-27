# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import pathlib
import sys
from datetime import datetime

import toml
from sphinx_gallery.sorting import FileNameSortKey

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# Info from poetry config:
info = toml.load("../../pyproject.toml")["tool"]["poetry"]

project = "Biosignal Device Interface"
author = ", ".join(info["authors"])
release = info["version"]
version = info["version"]

copyright = (
    f"2023 - {datetime.now().year}, n-squared lab, FAU Erlangen-Nürnberg, Germany"
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
HERE = pathlib.Path(__file__).parent
with (HERE.parent.parent / "README.md").open() as f:
    out = f.read()
with (HERE / "README.md").open("w+") as f:
    f.write(out)

extensions = [
    # Core Sphinx extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.githubpages",
    
    # Third-party extensions
    "sphinx_gallery.gen_gallery",
    "sphinx_copybutton",
    "sphinx_design",
    # "myst_parser",  # Temporarily disabled
    # "enum_tools.autoenum",  # Temporarily disabled due to enum issues
    "rinoh.frontend.sphinx",
]

# -- Extension configuration -------------------------------------------------

# Autodoc configuration
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}
autoclass_content = "both"
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
autodoc_member_order = "groupwise"

# Autosummary configuration
autosummary_generate = True
autosummary_generate_overwrite = True
autosummary_imported_members = True

# Napoleon configuration (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Todo extension
todo_include_todos = True

# Add function parentheses
add_function_parentheses = True

# Source file suffixes
source_suffix = {
    '.rst': None,
    # '.md': 'myst_parser',  # Temporarily disabled
}

# MyST parser configuration
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Templates and static files
templates_path = ["_templates"]
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_title = f"{project} v{version}"

# PyData theme options
html_theme_options = {
    "logo": {
        "text": "Biosignal Device Interface",
    },
    "github_url": "https://github.com/NsquaredLab/Biosignal-Device-Interface",
    "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_align": "left",
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version"],
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/NsquaredLab/Biosignal-Device-Interface",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
    "switcher": {
        "json_url": "https://nsquaredlab.github.io/Biosignal-Device-Interface/_static/switcher.json",
        "version_match": version,
    },
    "check_switcher": False,
}

# Context for edit button
html_context = {
    "github_user": "NsquaredLab",
    "github_repo": "Biosignal-Device-Interface",
    "github_version": "main",
    "doc_path": "docs/source/",
}

# Custom CSS
html_css_files = [
    "custom.css",
]

# Favicon (commented out until file is created)
# html_favicon = "_static/favicon.ico"

# Logo (commented out until file is created)
# html_logo = "_static/logo.png"

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "PySide6": (
        "https://doc.qt.io/qtforpython-6/",
        "https://doc.qt.io/qtforpython-6/objects.inv",
    ),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
}

# -- Options for sphinx_gallery ----------------------------------------------
sphinx_gallery_conf = {
    "examples_dirs": "../../examples",  # path to your example scripts
    "gallery_dirs": "auto_examples",  # path to where to save gallery generated output
    "filename_pattern": r"\.py",
    "remove_config_comments": True,
    "show_memory": False,  # Disable memory profiling to avoid PID issues
    "within_subsection_order": FileNameSortKey,
    "plot_gallery": "True",
    "download_all_examples": False,
    "first_notebook_cell": "%matplotlib inline",
    "expected_failing_examples": ["../../examples/4_implementing_new_device.py"],
    "image_scrapers": ('matplotlib',),
    "reset_modules": ('matplotlib', 'seaborn'),
}

# -- Options for copybutton --------------------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True
copybutton_remove_prompts = True

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

latex_documents = [
    ('index', 'biosignal-device-interface.tex', 
     'Biosignal Device Interface Documentation',
     author, 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    ('index', 'biosignal-device-interface', 
     'Biosignal Device Interface Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    ('index', 'BiosignalDeviceInterface', 
     'Biosignal Device Interface Documentation',
     author, 'BiosignalDeviceInterface', 
     'A unified communication interface for biosignal devices.',
     'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
