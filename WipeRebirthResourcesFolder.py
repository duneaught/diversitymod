import shutil
import os

##
## Get Steam path (verbatim lines from http://pastebin.com/z89Gr9NM)
##

import _winreg

def regkey_value(path, name="", start_key = None):
    if isinstance(path, str):
        path = path.split("\\")
    if start_key is None:
        start_key = getattr(_winreg, path[0])
        return regkey_value(path[1:], name, start_key)
    else:
        subkey = path.pop(0)
    with _winreg.OpenKey(start_key, subkey) as handle:
        assert handle
        if path:
            return regkey_value(path, name, handle)
        else:
            desc, i = None, 0
            while not desc or desc[0] != name:
                desc = _winreg.EnumValue(handle, i)
                i += 1
            return desc[1]

SteamPath = regkey_value(r"HKEY_CURRENT_USER\Software\Valve\Steam", "SteamPath")

##
## end of copied stuff
##

# set the paths for file creation
currentpath = os.getcwd()
if os.path.isdir(SteamPath+"/steamapps/common/The Binding of Isaac Rebirth/resources/"):
	resourcepath = SteamPath+"/steamapps/common/The Binding of Isaac Rebirth/resources/"
else:
	raw_input("Sorry. Default Steam path for The Binding of Isaac: Rebirth was not found.\nPress Enter to close.\n")
	sys.exit()

# tell the user where you're deleting
print("WARNING: This program will delete ALL non-essential files in:\n" + resourcepath + "\n")

# prompt user for confirmation to delete files
try:
	confirmdelete = raw_input("Deleted files cannot be recovered.\nAre you sure you want to continue?\n\nTo delete all files, enter 'y': ")
	print("")
except ValueError:
	raw_input("\nThere was an input error.\nPress Enter to close.\n")
	sys.exit()

if confirmdelete == 'y':
	# remove all the files and folders EXCEPT the 'packed' folder
	for resourcefile in os.listdir(resourcepath):
		if resourcefile != 'packed':
			print("Deleting "+resourcefile+" ...")
			try:
				if os.path.isfile(resourcepath+resourcefile):
					os.unlink(resourcepath+resourcefile)
				elif os.path.isdir(resourcepath+resourcefile):
					shutil.rmtree(resourcepath+resourcefile)
			except Exception, e:
				print e
		else:
			print("Not deleting 'packed' folder ...")
	print("\nRebirth mod files have been deleted.\n")
else:
	print("You have chosen not to delete anything.\n")

raw_input("Press Enter to close.\n")
