
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
            result = '\n'.join([i.rstrip()
                    for i in result.split('\n')]).rstrip('\n')
            if '...' in expected_result:
                for part in expected_result.split('...'):
                    pos = result.find(part)
                    if pos == -1:
                        import ipdb; ipdb.set_trace()
                    self.assertNotEqual(pos, -1)
                    result = result[pos + len(part):]
            else:
                self.assertEqual(expected_result, result)
