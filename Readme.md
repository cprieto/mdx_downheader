# Header Downgrader Extension for Python Markdown.

[![Build status](https://travis-ci.org/cprieto/mdx_downheader.svg?branch=master)](https://travis-ci.org/cprieto/mdx_downheader) [![Coverage](https://codecov.io/github/cprieto/mdx_downheader/coverage.svg?branch=master)](https://codecov.io/github/cprieto/mdx_downheader?branch=master) [![PyPI version](https://badge.fury.io/py/markdown-downheader.svg)](https://badge.fury.io/py/markdown-downheader)

When working with [markdown files](https://en.wikipedia.org/wiki/Markdown), sometimes you need to "downgrade" your headings for styling purposes. A good case scenario for this is using markdown with static site generators, for example, [Pelican](http://docs.getpelican.com/en/3.6.3/).

Given a piece of markdown like this:

```md
# This is header 1
## This is header 2
```

Python Markdown will generate the following HTML:

```html
<h1>This is header 1</h1>
<h2>This is header 2</h2>
```

With this extension enabled we obtain this instead:

```html
<h2>This is header 1</h2>
<h3>This is header 2</h3>
```

Easy!

## How to install

Tested with Python 2.7 and Python 3.5

It requires the awesome [Python Markdown](https://pythonhosted.org/Markdown/index.html) package, tested with Markdown 2.6.5

## Usage

Directly from python
```python
from markdown import markdown
text = '# hello world'
markdown(text, ['downheader(levels=1)',]
```

From the command line
```bash
echo '# hello world' > test.md
python -m markdown -o html5 -x 'downheader(levels=1)' -f test.html test.md
```

*Note*: Some static site generators, [like Pelican](http://docs.getpelican.com/en/3.6.3/settings.html), can use markdown extensions. You just need to install the pip package and provide the name of the markdown extension (in this case the name is simply 'downheader'). For example, for Pelican just add this to your pelicanconf.py file:

```
MD_EXTENSIONS = ['downheader']
```

As of [Pelican 3.7](http://docs.getpelican.com/en/3.7.0/settings.html) you have to define the Markdown extensions as a dictionary. Here is an example:

```python
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'downheader': {},
    },
    'output_format': 'html5',
}
```

To pass a value, you can use the following:

```python
# Markdown Plugins
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'downheader': {'levels': '2'},
    },
    'output_format': 'html5',
}
```

## Errors? bugs?

Simple, just create a ticket in Github, this will help me to maintain the library.

## Contributions? pull requests?

This is github, just fork and create a pull request, you will be always welcome to contribute!
