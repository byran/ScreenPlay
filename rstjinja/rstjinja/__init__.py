from jinja2 import Template


def rstjinja(app, docname, source):
    source[0] = Template(source[0]).render(**app.config.html_context)


def setup(app):
    app.connect("source-read", rstjinja)
