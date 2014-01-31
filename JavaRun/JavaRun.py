import sublime, sublime_plugin, re, os
from subprocess import Popen, PIPE

class JavaRunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		path = self.view.file_name()
		name = re.search(r"(([^\\]+)$)", path).group(1)
		command = (r"java " + name)#"cd /d " + path[:-len(name)] + " & " + r"java " + name)
		command = command[:-5]
		print(command)
		try:
			os.chdir(path[:-len(name)])
			sts = Popen(command).wait()	#seems to work well!
			#output = output.decode('utf-8')
		except Exception as e:
			print(e)
			#output = ""
		#print(output)
		if (sts != 0):
			print("Something went wrong. Make sure this class has a main method and has been compiled. Sorry I can't be more specific!")