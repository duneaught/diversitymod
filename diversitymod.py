import shutil, os, ConfigParser
from Tkinter import *
from tkFileDialog import askopenfilename
from random import seed, sample, randint
from PIL import Image, ImageFont, ImageDraw, ImageTk

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

def restartRebirth():
	# if Rebirth is running, kill it (returns an ugly error if Rebirth is not running, but just ignore it I guess)
	try:
		print("Attempting to kill Isaac ...\n")
		os.system("taskkill /im isaac-ng.exe /f")
	except OSError:
		print("There was an error closing Rebirth.")

	# start Rebirth
	try:
		if os.path.exists(resourcepath+"/../../../../steam.exe"):
			print("Found steam ...")
			os.system('"' + resourcepath + '/../../../../steam.exe" -applaunch 250900')
		elif os.path.exists(resourcepath + "/../isaac-ng.exe"):
			print("No Steam, but found isaac-ng.exe ...")
			os.system('"' + resourcepath + '/../isaac-ng.exe"')
	except OSError:
		print("Starting Rebirth failed.\nPress Enter to close.")
		
	feedback.set("Rebirth has been restarted!")
	
def installDiversityMod():
	# if no seed entered, generate one
	if dmseed.get() == '':
		seed()
		dmseed.set(str(randint(0,999999)))
		feedback.set("\nNo seed was entered, so a random seed was generated for you.")
	# set the RNG seed
	seed(dmseed.get())
	
	# valid_items is the list of all passive items in the game EXCLUDING the 22 on the no-list
	valid_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 27, 28, 32, 46, 48, 50, 51, 52, 53, 54, 55, 57, 60, 62, 63, 64, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 79, 80, 81, 82, 87, 88, 89, 90, 91, 94, 95, 96, 98, 99, 100, 101, 103, 104, 106, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 120, 121, 122, 125, 128, 129, 131, 132, 134, 138, 139, 140, 141, 142, 143, 144, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 159, 161, 162, 163, 165, 167, 168, 169, 170, 172, 173, 174, 178, 179, 180, 182, 183, 184, 185, 187, 188, 189, 190, 191, 193, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 236, 237, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 254, 255, 256, 257, 258, 259, 260, 261, 262, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 327, 328, 329, 330, 331, 332, 333, 335, 336, 337, 340, 341, 342, 343, 345]

	# creates list of 30 unique items from the valid items list
	itemIDs = sample(valid_items, 33)

	# create string
	pxmlString = '''<players root="resources/gfx/characters/costumes/" portraitroot="resources/gfx/ui/boss/" bigportraitroot="resources/gfx/ui/stage/">
		<player id="0" name="Isaac" skin="Character_001_Isaac.png" hp="6" bombs="1"  items="105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_01_Isaac.png" bigportrait="PlayerPortraitBig_01_Isaac.png" skinColor="-1" />
		<player id="1" name="Magdalene" skin="Character_002_Magdalene.png" costume="7" hp="8" items="105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_02_Magdalene.png" bigportrait="PlayerPortraitBig_02_Magdalene.png" skinColor="-1" />
		<player id="2" name="Cain" skin="Character_003_Cain.png" costume="8" hp="4" keys="1" items="46,105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_03_Cain.png" bigportrait="PlayerPortraitBig_03_Cain.png" skinColor="-1" />
		<player id="3" name="Judas" skin="Character_004_Judas.png" costume="9" hp="2" coins="3" items="105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_04_Judas.png" bigportrait="PlayerPortraitBig_04_Judas.png" skinColor="-1" />
		<player id="4" name="???" skin="Character_006_Bluebaby.png" hp="0" armor="6" items="105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' +  '''" portrait="PlayerPortrait_06_BlueBaby.png" bigportrait="PlayerPortraitBig_06_Bluebaby.png" skinColor="2" />
		<player id="5" name="Eve" skin="Character_005_Eve.png" costume="10" hp="4" items="122,117,105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_05_Eve.png" bigportrait="PlayerPortraitBig_05_Eve.png" skinColor="-1" />
		<player id="6" name="Samson" skin="Character_007_Samson.png" costume="13" hp="6" items="157,105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_07_Samson.png" bigportrait="PlayerPortraitBig_07_Samson.png" skinColor="-1" />
		<player id="7" name="Azazel" skin="Character_008_Azazel.png" costume="11" hp="0" black="6" card="1" items="105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_08_Azazel.png" bigportrait="PlayerPortraitBig_08_Azazel.png" skinColor="1" />
		<player id="8" name="Lazarus" skin="Character_009_Lazarus.png" hp="6" pill="1" items="105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_09_Lazarus.png" bigportrait="PlayerPortraitBig_09_Lazarus.png" skinColor="-1" />
		<player id="9" name="Eden" skin="Character_009_Eden.png" items="''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" costume="12" portrait="PlayerPortrait_09_Eden.png" bigportrait="PlayerPortraitBig_09_Eden.png" skinColor="-1">
			<hair gfx="Character_009_EdenHair1.png" />
			<hair gfx="Character_009_EdenHair2.png" />
			<hair gfx="Character_009_EdenHair3.png" />
			<hair gfx="Character_009_EdenHair4.png" />
			<hair gfx="Character_009_EdenHair5.png" />
			<hair gfx="Character_009_EdenHair6.png" />
			<hair gfx="Character_009_EdenHair7.png" />
			<hair gfx="Character_009_EdenHair8.png" />
			<hair gfx="Character_009_EdenHair9.png" />
			<hair gfx="Character_009_EdenHair10.png" />
		</player>
		<player id="10" name="The Lost" skin="Character_012_TheLost.png" hp="0" armor="1" coins="1" items="105,''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + str(itemIDs.pop()) + ''',''' + '''" portrait="PlayerPortrait_12_TheLost.png" bigportrait="PlayerPortraitBig_12_TheLost.png" skinColor="0" />
		<player id="11" name="Lazarus II" skin="Character_010_Lazarus2.png" hp="2" items="214" portrait="PlayerPortrait_10_Lazarus2.png" bigportrait="PlayerPortraitBig_10_Lazarus2.png" skinColor="-1" />
		<player id="12" name="Black Judas" skin="Character_013_BlackJudas.png" black="4" portrait="PlayerPortrait_BlackJudas.png" bigportrait="PlayerPortraitBig_BlackJudas.png" skinColor="1" />
	</players>'''
	
	# clear out the files
	# remove all the files and folders EXCEPT /packed/ and /tmpdm196/
	for resourcefile in os.listdir(resourcepath):
		if resourcefile != 'packed' and resourcefile != 'tmpdm196' :
			if os.path.isfile(os.path.join(resourcepath, resourcefile)):
				os.unlink(os.path.join(resourcepath, resourcefile))
			elif os.path.isdir(os.path.join(resourcepath, resourcefile)):
				shutil.rmtree(os.path.join(resourcepath, resourcefile))
	
	# write players file
	file = open(resourcepath + "/players.xml", "w")
	file.write(pxmlString)
	file.close()
	
	# make the graphics and install them
	# create gfx folder structure
	os.makedirs(resourcepath + '/gfx/ui/main menu/')
	# open character menu graphic & write the seed on it
	img = Image.open(currentpath + "/diversitymod files/charactermenu.png")
	draw = ImageDraw.Draw(img)
	smallfont = ImageFont.truetype(os.getcwd() + "/diversitymod files/comicbd.ttf", 10)
	largefont = ImageFont.truetype(os.getcwd() + "/diversitymod files/comicbd.ttf", 16)
	w, h = draw.textsize("Diversity Mod v" + str(version) + " Seed", font = smallfont)
	w2, h2 = draw.textsize(str(dmseed.get()), font = largefont)
	draw.text((240-w/2, 213), "Diversity Mod v" + str(version) + " Seed", (54, 47, 45), font = smallfont)
	draw.text((240-w2/2, 225), str(dmseed.get()), (54, 47, 45), font = largefont)
	img.save(resourcepath + '/gfx/ui/main menu/charactermenu.png')
	# copy the title screen graphic to resources folder
	shutil.copyfile(currentpath + '/diversitymod files/titlemenu.png', resourcepath + '/gfx/ui/main menu/titlemenu.png')
	
	shutil.copyfile(currentpath + '/diversitymod files/itempools.xml', resourcepath + '/itempools.xml')
	shutil.copyfile(currentpath + '/diversitymod files/items.xml', resourcepath + '/items.xml')
	
	os.makedirs(resourcepath + '/rooms/')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/00.special rooms.stb', resourcepath + '/rooms/00.special rooms.stb')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/04.catacombs.stb', resourcepath + '/rooms/04.catacombs.stb')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/05.depths.stb', resourcepath + '/rooms/05.depths.stb')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/06.necropolis.stb', resourcepath + '/rooms/06.necropolis.stb')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/07.womb.stb', resourcepath + '/rooms/07.womb.stb')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/08.utero.stb', resourcepath + '/rooms/08.utero.stb')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/09.sheol.stb', resourcepath + '/rooms/09.sheol.stb')
	shutil.copyfile(currentpath + '/diversitymod files/rooms/12.chest.stb', resourcepath + '/rooms/12.chest.stb')

	feedback.set("Diversity Mod files have been installed.\nRestart Rebirth to play.")

	# update gui stuffs
	dm.update_idletasks()
	
def closeDiversityMod():
	# remove all the files and folders EXCEPT /packed/ and /tmpdm196/
	for resourcefile in os.listdir(resourcepath):
		if resourcefile != 'packed' and resourcefile != 'tmpdm196' :
			if os.path.isfile(os.path.join(resourcepath, resourcefile)):
				os.unlink(os.path.join(resourcepath, resourcefile))
			elif os.path.isdir(os.path.join(resourcepath, resourcefile)):
				shutil.rmtree(os.path.join(resourcepath, resourcefile))
				
	# copy all the files and folders EXCEPT the 'packed' folder to /tmpdm196/
	for tmpdm196file in os.listdir(os.path.join(resourcepath, 'tmpdm196')):
		if os.path.isfile(os.path.join(resourcepath, 'tmpdm196', tmpdm196file)):
			shutil.copyfile(os.path.join(resourcepath, 'tmpdm196', tmpdm196file), os.path.join(resourcepath, tmpdm196file))
		elif os.path.isdir(os.path.join(resourcepath, 'tmpdm196', tmpdm196file)):
			shutil.copytree(os.path.join(resourcepath, 'tmpdm196', tmpdm196file), os.path.join(resourcepath, tmpdm196file))
	# remove the temporary directory we created
	shutil.rmtree(os.path.join(resourcepath, 'tmpdm196/'))
	sys.exit()
	
def setcustompath():
	# open file dialog
	isaacpath = askopenfilename()
	# check that the file is isaac-ng.exe and the path is good
	if isaacpath [-12:] == "isaac-ng.exe" and os.path.exists(isaacpath[0:-12] + 'resources'):
		if not customs.has_section('options'):
			customs.add_section('options')
		customs.set('options', 'custompath', isaacpath [0:-12] + 'resources')
		with open('options.ini', 'wb') as configfile:
			customs.write(configfile)
		feedback.set("Your Diversity Mod path has been correctly set.\nClose this window and restart Diversity Mod.")
	else:
		feedback.set("That file appears to be incorrect. Please try again to find isaac-ng.exe")
	dm.update_idletasks()
	
	
version = 0.6
	
# dm is the gui, dmseed is the rng seed, feedback is the message for user
dm = Tk()
dmseed = StringVar()
feedback = StringVar()
feedback.set("Welcome to Diversity Mod!\nKeep this program open while playing isaac.")
# just the gui icon and title
dm.iconbitmap("diversitymod files/poop.ico")
dm.title("Diversity Mod")

# import options
customs = ConfigParser.RawConfigParser()
customs.read('options.ini')

# check and set the paths for file creation, exit if not found
currentpath = os.getcwd()
# first check custom path
if customs.has_option('options', 'custompath') and os.path.exists(customs.get('options', 'custompath')):
	resourcepath=customs.get('options', 'custompath')
# then check steam path
elif os.path.isdir(SteamPath + "/steamapps/common/The Binding of Isaac Rebirth/resources"):
	resourcepath = SteamPath + "/steamapps/common/The Binding of Isaac Rebirth/resources"
else: # if neither, then go through the motions of writing and saving a new path to options
	feedback.set("")
	Message(dm, justify = CENTER, font = "font 10", text = "Diversity Mod was unable to find your resources directory.\nNavigate to the program isaac-ng.exe in your Steam directories.", width = 600).grid(row = 0, pady = 10)
	Message(dm, justify = CENTER, font = "font 12", textvariable = feedback, width = 600).grid(row = 1)
	Button(dm, font = "font 12", text = "Navigate to isaac-ng.exe", command = setcustompath).grid(row = 2, pady = 10)
	Message(dm, justify = LEFT, font = "font 10", text = "Example:\nC:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\isaac-ng.exe", width = 800).grid(row = 3, padx = 15, pady = 10)
	mainloop()
	
# check if you're inside the resources path. give warning and close if necessary.
if os.path.normpath(resourcepath).lower() in os.path.normpath(currentpath).lower():
	Message(dm, justify = CENTER, font = "font 12", text = "Diversity Mod is in your resources directory.\nMove it elsewhere before running.", width = 600).grid(row = 0, pady = 10)
	mainloop()
	sys.exit()

# create a folder to temporarily hold files until Diversity Mod is done
#if not os.path.exists(os.path.join(resourcepath,'tmpdm196'))
os.mkdir(os.path.join(resourcepath, 'tmpdm196'))

# copy all the files and folders EXCEPT the 'packed' folder to /tmpdm196/
for resourcefile in os.listdir(resourcepath):
	if resourcefile != 'packed' and resourcefile != 'tmpdm196':
		try:
			if os.path.isfile(os.path.join(resourcepath, resourcefile)):
				shutil.copyfile(os.path.join(resourcepath, resourcefile), os.path.join(resourcepath, "tmpdm196", resourcefile))
			elif os.path.isdir(os.path.join(resourcepath, resourcefile)):
				shutil.copytree(os.path.join(resourcepath, resourcefile), os.path.join(resourcepath, "tmpdm196", resourcefile))
		except Exception, e:
			print e

Label(dm, text = "Diversity mod will create and overwrite files in:\n" + resourcepath).grid(row = 0, column = 0, columnspan = 2, padx = 25, pady = 15)

# central gui box
dmbox = LabelFrame(dm, text = "", padx = 5, pady = 5)
dmbox.grid(row = 1, column = 0, columnspan = 2, pady = 15)
# text entry for seed
Label(dmbox, text = "Enter seed (case sensitive, empty for random)", font = "font 14").grid(row = 0, pady = 10)
sentry = Entry(dmbox, justify = CENTER, font = "font 32 bold", width = 15, textvariable = dmseed)
sentry.grid(row = 1, padx = 10)
# button to install mod
dmiconimage = Image.open("diversitymod files/rainbow.png")
dmicon = ImageTk.PhotoImage(dmiconimage)
Button(dmbox, image = dmicon, text = '   Install Diversity Mod   ', compound = "left", command = installDiversityMod, font = "font 16").grid(row = 2, pady = 10)

# feedback message display for user
Label(dm, justify = CENTER, textvariable = feedback).grid(row = 2, column = 0, columnspan = 2)
Label(dm, justify = CENTER, text = "Every time you install with a new seed, characters get new random starting items.\nWhen you close this program, Diversity Mod will be uninstalled.").grid(row = 3, column = 0, columnspan = 2)

# button to restart rebirth
starticonimage = Image.open("diversitymod files/rebirth.png")
starticon = ImageTk.PhotoImage(starticonimage)
Button(dm, image = starticon, text = '  (re)Start Rebirth  ', compound = "left", font = "font 12", command = restartRebirth).grid(row = 4, column = 0, padx = 10, pady = 20, sticky = E)

# button to uninstall and close diversity mod
closeiconimage = Image.open("diversitymod files/forgetmenow.png")
closeicon = ImageTk.PhotoImage(closeiconimage)
Button(dm, text = '  Close Diversity Mod  ', image = closeicon, compound = "right", font = "font 12", command = closeDiversityMod).grid(row = 4, column = 1, padx = 10, pady = 20, sticky = W)
# also uninstall if the window is closed
dm.protocol("WM_DELETE_WINDOW", closeDiversityMod)

mainloop( )
