"""
Jinja support in Sphinx
Based on https://www.ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
"""


def rstjinja(app, docname, source):
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    rendered = app.builder.templates.render_string(
        source[0], app.config.html_context
    )
    source[0] = rendered


def setup(app):
    app.connect("source-read", rstjinja)
