import sublime, sublime_plugin
from subprocess import check_output

class CheckstyleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if not self.view.is_dirty():
			path = self.view.file_name()
			command = r"java -jar E:\\Users\Steven\Documents\GaTech\CS1332\checkstyle-5.6\checkstyle-5.6-all.jar -c E:\\Users\Steven\Documents\GaTech\CS1332\checkstyle-5.6\CS1332-checkstyle.xml " + "\"" + path + "\""
			print(command)
			try:
				output = check_output(command)
			except Exception as e:
				output = e.output
			output =  output.decode('utf-8')
			print(output)
			print("File contains " + str(len(output.splitlines()) - 2) + " errors total.")
		else:
			print("The file must be saved before running Checkstyle!")
