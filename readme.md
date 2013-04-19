# roku-sublime

Working on creating a Sublime Text build system for Roku projects using Brightscript.

## Contents
* roku.sublime-project
* rokuinstall.sh
* rokureplace.sh

## Implementation
Eventually, this should be much more automatic, but for now, it assumes that you are using git and have one Roku project per repo. It also assumes that your Sublime project is defined at the same level as your repo folder.

```
	/Project
		roku.sublime-project
		/repo
			.git
			/source
			…
		...
```
Currently, I am still working on finding the correct place for the .sh files, and exactly how to call them .sublime-project. However, they function correctly for packaging a Roku project, and pushing it to the device for testing.  
**NOTE - ** You will need to replace 192.168.0.1 in both of the .sh files with the IP address of your Roku.