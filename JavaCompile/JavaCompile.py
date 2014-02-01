import sublime, sublime_plugin, re, os
import subprocess

class JavaCompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name()
		name = re.search(r"(([^\\]+)$)", path).group(1)
		command = (r"javac " + name)#"cd /d " + path[:-len(name)] + " & " + r"java " + name)
		try:
			os.chdir(path[:-len(name)])
			output = check_output(command, stderr=subprocess.STDOUT)
		except Exception as e:
			output = e.output
		output =  output.decode('utf-8')
		print(output)
