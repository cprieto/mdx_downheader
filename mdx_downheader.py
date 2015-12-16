# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from markdown import Extension
from markdown.treeprocessors import Treeprocessor

__version__ = "1.0.0"


class DownHeaderTreeProcessor(Treeprocessor):
    def run(self, doc):
        for elem in doc:
            if elem.tag in ['h1', 'h2', 'h3', 'h4', 'h5']:
                level = int(elem.tag[-1])
                elem.tag = 'h' + str(level + 1)



class DownHeaderExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        if 'downheader' not in md.treeprocessors.keys():
            md.treeprocessors.add('downheader', DownHeaderTreeProcessor(), '_end')


def makeExtension(*args, **kwargs):
    return DownHeaderExtension(*args, **kwargs)