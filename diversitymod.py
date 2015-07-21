import shutil
import os
from random import randint, seed
from PIL import Image, ImageFont, ImageDraw 

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

findpathfail = False

# set the paths for file creation
currentpath = os.getcwd()
if os.path.isdir(SteamPath+"/steamapps/common/The Binding of Isaac Rebirth/resources"):
	resourcepath = SteamPath+"/steamapps/common/The Binding of Isaac Rebirth/resources"
else:
	print("Default Steam path for The Binding of Isaac: Rebirth was not found.\n")
	resourcepath = currentpath
	findpathfail = True

# tell the user where you're writing
print("Diversity mod will create and overwrite files in:\n" + resourcepath + "\n")

# set seed to the user entered number, loops if you don't enter a number
try:
	isaacseed = raw_input("Enter alphanumeric seed (or enter no text to quit): ")
	seed(isaacseed)
except ValueError:
	print("\nThere was an error processing that seed. Quitting...\n")
	raw_input("Script complete.\n")
	sys.exit()

# if no seed was entered, just quit
if isaacseed == '':
	print("\nNo seed entered. Quitting...\n")
	raw_input("Script complete.\n")
	sys.exit()

# ntp is the list of every item ID in the range(1-346) to be excluded from the random starting items...
# they are space activated items, invalid IDs, and some boring items
ntp = [15, 16, 22, 23, 24, 25, 26, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 49, 56, 58, 59, 61, 64, 65, 66, 74, 77, 78, 83, 84, 85, 86, 93, 97, 102, 105, 107, 111, 123, 124, 126, 127, 130, 133, 135, 136, 137, 145, 146, 147, 158, 160, 164, 166, 171, 175, 176, 177, 181, 186, 192, 235, 238, 239, 253, 263, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 323, 324, 325, 326, 338, 339, 344, 346]

# create array to hold the list of items we'll give the characters
itemIDs = []

# 30 items is enough to give 3 to each of the 10 characters (we excluded eden)
for x in range(0, 30):
	while True:
		# generate a random number from all the item IDs
		id = randint(1,346)
		# check if it's on the (bad) ntp list, if it is we try another ID, and add the item to the list (so we don't pick it twice)
		if (id in ntp) == False:
			ntp.append(id)
			itemIDs.append(id)
			break

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
	<player id="9" name="Eden" skin="Character_009_Eden.png" costume="12" portrait="PlayerPortrait_09_Eden.png" bigportrait="PlayerPortraitBig_09_Eden.png" skinColor="-1">
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


# create/overwrite all the mod files

# track errors
errorcount = 0

print("\nDrawing title and menu graphics ...")
try:
	# check if folder structure exists for graphics mod, create if necessary
	if not os.path.exists(resourcepath+'/gfx/ui/main menu/'):
		print("Creating directories for graphics ...")
		os.makedirs(resourcepath+'/gfx/ui/main menu/')

	img = Image.open(currentpath+"/diversitymod files/charactermenu.png")
	draw = ImageDraw.Draw(img)

	smallfont = ImageFont.truetype(os.getcwd()+"/diversitymod files/comicbd.ttf", 10)
	largefont = ImageFont.truetype(os.getcwd()+"/diversitymod files/comicbd.ttf", 16)

	w, h = draw.textsize("Diversity Mod v0.2 Seed",font=smallfont)
	w2, h2 = draw.textsize(str(isaacseed),font=largefont)
	draw.text((240-w/2, 213),"Diversity Mod v0.2 Seed",(54,47,45),font=smallfont)
	draw.text((240-w2/2, 225),str(isaacseed),(54,47,45),font=largefont)

	img.save(resourcepath+'/gfx/ui/main menu/charactermenu.png')

	shutil.copyfile(currentpath+'/diversitymod files/titlemenu.png',resourcepath+'/gfx/ui/main menu/titlemenu.png')
except IOError, OSError:
	print("There was an error writing the graphics files.\n")
	error += 1

print("Assigning random items to characters ...")
try:
	file = open(resourcepath+"/players.xml", "w")
	file.write(pxmlString)
	file.close()
except IOError:
	print("There was an error writing the players.xml file.\n")
	error += 1

print("Removing Mom's Knife, Epic Fetus, Ipecac, & Brimstone from pools ...")
try:
	shutil.copyfile(currentpath+'/diversitymod files/itempools.xml',resourcepath+'/itempools.xml')
except IOError:
	print("There was an error writing the itempools.xml file.\n")
	error += 1

print("Removing special status from items ...")
try:
	shutil.copyfile(currentpath+'/diversitymod files/items.xml',resourcepath+'/items.xml')
except IOError:
	print("There was an error writing the items.xml file.\n")
	error += 1

print("Removing donation machines, bad angel rooms, & unavoidable damage ...")
try:
	# check if folder structure exists for rooms mod, create if necessary
	if not os.path.exists(resourcepath+'/rooms/'):
		print("Creating directories for graphics ...\n")
		os.makedirs(resourcepath+'/rooms/')

	shutil.copyfile(currentpath+'/diversitymod files/rooms/00.special rooms.stb',resourcepath+'/rooms/00.special rooms.stb')
	shutil.copyfile(currentpath+'/diversitymod files/rooms/04.catacombs.stb',resourcepath+'/rooms/04.catacombs.stb')
	shutil.copyfile(currentpath+'/diversitymod files/rooms/05.depths.stb',resourcepath+'/rooms/05.depths.stb')
	shutil.copyfile(currentpath+'/diversitymod files/rooms/06.necropolis.stb',resourcepath+'/rooms/06.necropolis.stb')
	shutil.copyfile(currentpath+'/diversitymod files/rooms/07.womb.stb',resourcepath+'/rooms/07.womb.stb')
	shutil.copyfile(currentpath+'/diversitymod files/rooms/08.utero.stb',resourcepath+'/rooms/08.utero.stb')
	shutil.copyfile(currentpath+'/diversitymod files/rooms/09.sheol.stb',resourcepath+'/rooms/09.sheol.stb')
	shutil.copyfile(currentpath+'/diversitymod files/rooms/12.chest.stb',resourcepath+'/rooms/12.chest.stb')
except IOError:
	print("There was an error writing the room files.\n")
	error += 1

# report results
if errorcount > 0:
	print("Failed to create Diversity Mod with " + str(errorcount) + " errors\n")
else:
	# tell the user where you're writing
	print("\nDiversity mod successfully created in:\n" + resourcepath + "\n")
	if findpathfail:
		print("If this is not your resources folder, move players.xml, items.xml, itempools.xml, gfx, & rooms to the correct folder to install Diversity Mod.\n")

print("Script complete.\nPress Enter to close.\n")
raw_input()