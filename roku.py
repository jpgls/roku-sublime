import sublime, sublime_plugin
import os, sys
import subprocess
import re

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
		
		result = subprocess.Popen([
			'zip', '-r', projectDir + os.sep + projectName + '.zip', 
			get_root_directory(self), '-x', '*.git*'],
			stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		output, errors = result.communicate()
		
		if result.returncode:
			print(output.decode());
		else: 
			print(output.decode());
			
		print('packaging complete.');

class RokuInstallCommand(sublime_plugin.ApplicationCommand):
	def run(args):
		print('Installing...');
		result = subprocess.Popen([
			'curl', '-F', 
			'archive=@$1.zip;type=application/zip', 
			'-F', 'mysubmit=Install', '-H',
			'Content-type:multipart/form-data', 
			'192.168.0.1/plugin_install'])
		output, errors = result.communicate()
		if result.returncode:
			raise Exception(errors)
		else: 
			print(output);
		print('installation complete.');


class RokuReplaceCommand(sublime_plugin.ApplicationCommand):
	def run(args):
		print('Installing...');
		result = subprocess.Popen([
			'curl', '-F', 
			'archive=@$1.zip;type=application/zip', 
			'-F', 'mysubmit=Replace', '-H',
			'Content-type:multipart/form-data', 
			'192.168.0.1/plugin_install'])
		output, errors = result.communicate()
		if result.returncode:
			raise Exception(errors)
		else: 
			print(output);
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
		
	
		
 