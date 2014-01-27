import sublime, sublime_plugin, re
from sublime import Region
from subprocess import check_output

class CorrectCheckstyleCommand(sublime_plugin.TextCommand):
	def correct(self, edit, output):
		errors = output.splitlines()
		errors = errors[1:len(errors)-1]
		errors = reversed(errors)
		for i in errors:
			if "is preceded with whitespace" in i:
				result = re.search('java:(.*):', i)
				pos = result.group(1)
				line = int(re.search('(.*):', pos).group(1)) - 2
				col = int(re.search(':(.*)', pos).group(1)) + 6
				self.view.erase(edit, Region(self.view.text_point(line, col), self.view.text_point(line, col + 1)))
				print("corrected:      " + i)
			elif "is not followed by whitespace" in i:
				result = re.search('java:(.*):', i)
				pos = result.group(1)
				line = int(re.search('(.*):', pos).group(1)) - 2
				col = int(re.search(':(.*)', pos).group(1)) + 25
				self.view.insert(edit, self.view.text_point(line, col), " ")
				print("corrected:      " + i)
			elif "is not preceded with whitespace" in i:
				result = re.search('java:(.*):', i)
				pos = result.group(1)
				line = int(re.search('(.*):', pos).group(1)) - 2
				col = int(re.search(':(.*)', pos).group(1)) + 25
				self.view.insert(edit, self.view.text_point(line, col), " ")
				print("corrected:      " + i)
			else:
				print("can't correct:  " + i)

	def run(self, edit):
		if not self.view.is_dirty():
			path = self.view.file_name()
			command = r"java -jar E:\\Users\Steven\Documents\GaTech\CS1332\checkstyle-5.6\checkstyle-5.6-all.jar -c E:\\Users\Steven\Documents\GaTech\CS1332\checkstyle-5.6\CS1332-checkstyle.xml " + "\"" + path + "\""
			try:
				output = check_output(command)
			except Exception as e:
				output = e.output
			output =  output.decode('utf-8')
			self.correct(edit, output)
		else:
			print("the file must be saved first!")

