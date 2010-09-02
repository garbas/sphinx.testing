import os
import unittest2 as unittest
import docutils.parsers.rst

try:
    import plone.testing.layer as layer
    layer_support = True
except:
    layer_support = False


class SphinxTestSuite(unittest.TestSuite):

    def __init__(self, tests, layer=None):
        self.tests = []
        self.parser = docutils.parsers.rst.Parser()
        self.addTests(tests, layer)

    def addTests(self, tests, default_layer):
        for test in tests:
            if isinstance(test, list) or isinstance(test, tuple):
                if len(test) == 2 and layer_support and \
                   isinstance(test[1], layer.Layer):
                    self.addTest(test[0], test[1])
                else:
                    raise Exception('Test should come in pair with layer.')
            if default_layer is not None and layer_support and \
               isinstance(default_layer, layer.Layer):
                self.addTest(test, default_layer)
            else:
                self.addTest(test)

    def addTest(self, test, layer=None):
        if not isinstance(test, basestring):
            raise Exception('Test should be path to existing file.')
        if not os.path.exists(test):
            raise Exception('File does not exists: ' + test)

        test_file = os.path.abspath(test)
        test_f = open(test_file)
        rst_input = test_f.read()
        test_f.close()

        settings = docutils.frontend.OptionParser(
                            components=(self.parser,)).get_default_values()

        rst_document = docutils.utils.new_document(test_file, settings)
        try:
            self.parser.parse(rst_input, rst_document)
        except Exception, e:
            pass


        for code_block in rst_document.traverse():
            test = code_block.rawsource
            if isinstance(test, unittest.TestCase):
                if layer is not None and \
                   not getattr(test, 'layer', False):
                    test.layer = layer
                self.tests.append(test)

    def __iter__(self):
        for test in self.tests:
            yield test
