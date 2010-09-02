import case
import pygments.token
import pygments.lexers
import docutils.parsers.rst

class CodeBlock(docutils.parsers.rst.Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = dict(
        layer=docutils.parsers.rst.directives.unchanged)

    def run(self):
        self.assert_has_content()
        try:
            lexer = pygments.lexers.get_lexer_by_name(self.arguments[0])
        except Exception, e:
            raise Exception('No appropriate lexer found for this '
                            'code-block: '  + self.arguments[0])

        if self.arguments[0] == 'console':
            test = case.ConsoleTestCase()
            test.commands = []
            test = self.prompt_parser(test, lexer)
        else:
            raise Exception('No testcase for code-block '
                            'found: ' + self.arguments[0])
        return [docutils.nodes.raw(test, '')]

    def prompt_parser(self, test, lexer):
        command, expected_result = '', ''
        for item in lexer.get_tokens(u'\n'.join(self.content)):
            if item[0] == pygments.token.Token.Generic.Output:
                expected_result += item[1]
            elif item[0] not in [pygments.token.Token.Generic.Prompt,
                                 pygments.token.Token.Literal.String.Escape,]:
                command += item[1]
            if command and \
               item[0] == pygments.token.Token.Generic.Prompt and \
               item[1] in ['#', '$', '%']: # FIXME: should be generic
                test.commands.append((command.strip(),
                                      expected_result.rstrip('\n')))
                command, expected_result = '', ''
        test.commands.append((command.strip(),
                              expected_result.rstrip('\n')))
        return test

docutils.parsers.rst.directives.register_directive('code-block', CodeBlock)
