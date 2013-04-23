# roku-sublime
Working on creating a Sublime Text build system for Roku projects using Brightscript.

# Usage  
There are 3 commands (Cmd + Shift + P) at the moment 
1. Roku: Package (almost working - see todo list)
2. Roku: Install (not working)
3. Roku: Replace (not working)

# Installation  

* Download and extract to Sublime Text 2/3 Packages folder
	> Windows:  %APPDATA%\Sublime Text 2\Packages
	> Windows:  %APPDATA%\Sublime Text 3\Packages
	
	> Mac OS X: ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
	> Mac OS X: ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
	
	> Linux:    ~/.config/sublime-text-2/Packages
	> Linux:    ~/.config/sublime-text-3/Packages

**NOTE - ** You will need to replace 192.168.0.1 in both of the .sh files with the IP address of your Roku.

# Status  
This is very much a work in progress

# Change log  
* Created a basic SublimeText Plugin with 3 commands (roku.py)
* Pulled the .sh scripts from original project into the python scripts and tried to keep them platform agnostic.
