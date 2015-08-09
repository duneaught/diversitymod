import os, sys, shutil, py2exe
from distutils.core import setup

#Here is where you can set the name for the release zip file and for the install dir inside it.
version = "0.7"
installName = 'DiversityMod-' + version

#target is where we assemble our final install. dist is where py2exe produces exes and their dependencies
if os.path.isdir('target/'):
  shutil.rmtree('target/')
installDir = 'target/' + installName + '/'

#then build the option builder using normal py2exe
sys.argv.append('py2exe')
setup(
	windows = ['diversitymod.py'],
	options = {
		'py2exe': {
			'includes': ['shutil','random','PIL','os','_winreg','Tkinter','ConfigParser'],
			'bundle_files': 1,
			'dll_excludes': ['w9xpopen.exe']
		}
	}
)

shutil.copytree('dist/', installDir)

shutil.copytree('diversitymod files/', installDir + 'diversitymod files/')

#shutil.copy('extra_files', installDir)
shutil.copy('README.md', installDir+"/README.txt")
shutil.copy('options.ini', installDir+"/options.ini")

#with open(installDir + "version.txt", 'w') as f:
#  f.write(version)
shutil.make_archive("target/" + installName, "zip", 'target', installName + "/")