# -*- coding: utf-8 -*-

from sphinx.application import Sphinx


sphinx = Sphinx(srcdir='src',
                confdir='src',
                outdir='dummy',
                doctreedir='dummy',
                buildername='mybuilder',
                confoverrides={'extensions': 'mybuilder'})
sphinx.build()
