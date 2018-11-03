# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from markdown import Extension, version_info as markdown_vesion
from markdown.treeprocessors import Treeprocessor
__version__ = "1.0.2"


class DownHeaderTreeProcessor(Treeprocessor):
    def __init__(self, levels):
        self.levels = levels
        super(DownHeaderTreeProcessor, self).__init__()

    def run(self, doc):
        for elem in doc:
            if elem.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                original_level = int(elem.tag[-1])
                level = original_level + int(self.levels)
                level = min(6, max(1, level))
                elem.tag = 'h' + str(level)


class DownHeaderExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            'levels': [1, 'downgrade headings this many levels'],
        }
        super(DownHeaderExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        treeprocessors = md.treeprocessors.keys() if markdown_vesion[0] < 3 else md.treeprocessors

        if 'downheader' not in treeprocessors:
            treeprocessor = DownHeaderTreeProcessor(self.getConfig('levels'))
            md.treeprocessors.add('downheader', treeprocessor, '_end')


def makeExtension(*args, **kwargs):
    return DownHeaderExtension(*args, **kwargs)