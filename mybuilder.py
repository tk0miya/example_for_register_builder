# -*- coding: utf-8 -*-

from sphinx.builders import Builder


class MyBuilder(Builder):
    name = 'mybuilder'

    def get_outdated_docs(self):
        return 'all documents!'

    def prepare_writing(self, docnames):
        pass

    def write_doc(self, docname, doctree):
        self.info('')
        self.info('Writing %s ...' % docname)


def setup(app):
    app.add_builder(MyBuilder)
