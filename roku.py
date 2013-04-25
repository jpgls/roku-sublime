import sublime, sublime_plugin
import os, sys
import subprocess
import re
import zipfile
import json

def get_root_directory(self):
	folders = self.window.folders();
	
	projDir = "";
	for folder in folders:
		
		folderLen = len(folder.split(os.sep));
		
		if projDir == "" or folderLen < len(projDir.split(os.sep)):
			projDir = folder;
			
	return projDir;


def get_project_name(projDir):
	dirList = projDir.split(os.sep);
	return dirList[len(dirList)-1];
	
	
class RokuPackageCommand(sublime_plugin.WindowCommand):
	def run(self):
		print('Packaging...');
		
		projectDir = get_root_directory(self);
		projectName = get_project_name(projectDir);
		outputDirectory = projectDir + os.sep + 'build';
		ouputZip = outputDirectory + os.sep + projectName;
		
		# check for and create build directory if necessary
		if not os.path.exists(outputDirectory):
			os.makedirs(outputDirectory);
		
		print('Zipping ' + projectDir);
		
		zf = zipfile.ZipFile('%s.zip' % (ouputZip), 'w');
		abs_src = os.path.abspath(projectDir);
		
		for dirname, subdirs, files in os.walk(projectDir):
			for filename in files:
				absname = os.path.abspath(os.path.join(dirname, filename));
				arcname = absname[len(abs_src) + 1:];
				
				# messy need to fix this
				if(arcname.find('.buildpath') == -1 and 
					arcname.find('.gitignore') == -1 and 
					arcname.find('.project') == -1 and
					arcname.find('.git') == -1 and 
					arcname.find('.sublime') == -1 and
					arcname.find('build') == -1):
						print('zipping %s as %s' % (os.path.join(dirname, filename), arcname));
						zf.write(absname, arcname);
		zf.close();
			
		print('packaging complete.');

# need tofigure out how to load a settings file so we can get the ip addy
class RokuInstallCommand(sublime_plugin.WindowCommand):
	def run(self):
		print('Installing...');
		
		projectDir = get_root_directory(self);
		projectName = get_project_name(projectDir);
		projectJson = open(projectDir + os.sep + projectName + '.sublime-project');
		
		# need to add error handling for json parsing.
		projectSettings = json.load(projectJson);
		
		print(projectSettings['ip']);
		
		# result = subprocess.Popen([
		# 	'curl', '-F', 
		# 	'archive=@$1.zip;type=application/zip', 
		# 	'-F', 'mysubmit=Install', '-H',
		# 	'Content-type:multipart/form-data', 
		# 	'192.168.0.1/plugin_install'])
		# output, errors = result.communicate()
		# if result.returncode:
		# 	raise Exception(errors)
		# else: 
		# 	print(output);
		print('installation complete.');


class RokuReplaceCommand(sublime_plugin.ApplicationCommand):
	def run(args):
		print('Replacing...');
		# result = subprocess.Popen([
		# 	'curl', '-F', 
		# 	'archive=@$1.zip;type=application/zip', 
		# 	'-F', 'mysubmit=Replace', '-H',
		# 	'Content-type:multipart/form-data', 
		# 	'192.168.0.1/plugin_install'])
		# output, errors = result.communicate()
		# if result.returncode:
		# 	raise Exception(errors)
		# else: 
		# 	print(output);
		print('installation complete.');

	
# class RokuRunProcessCommand(sublime_plugin.ApplicationCommand):
# 	def run(args):
# 		print('Start running a script...');
# 		result = subprocess.Popen(['ls', '-la', '\~/'], stdout=subprocess.PIPE)
# 		output, errors = result.communicate()
# 		if result.returncode:
# 			raise Exception(errors)
# 		else: 
# 			print(output);
# 		print('...Script complete');
		
	
		
 