
import subprocess
import unittest2 as unittest


class ConsoleTestCase(unittest.TestCase):

    def runTest(self):
        for command, expected_result in self.commands:
            p = subprocess.Popen(command.split(),
                                 stderr=subprocess.STDOUT,
                                 stdout=subprocess.PIPE,
                                 cwd=self.layer['buildout-directory'])
            result, _ = p.communicate()
            p.wait()
            result = result.rstrip('\n')
            self.assertEqual(expected_result, result)
