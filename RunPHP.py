import sublime, sublime_plugin
from subprocess import Popen, PIPE, STDOUT

class RunPHPCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        content = self.view.substr(sublime.Region(0, self.view.size()))
        php = Popen(['/usr/local/bin/php'], stdout=PIPE, stdin=PIPE, universal_newlines=True)
        # php.stdin.write(content)
        output, errors = php.communicate(content)
        # output = php.communicate()[0]
        newtab = self.view.window().new_file()
        newtab.insert(edit, 0, output)