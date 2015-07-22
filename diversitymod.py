import shutil
import os
from random import seed, sample, randint
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

# set seed to the user entered number, picks
try:
	isaacseed = raw_input("Enter seed (case sensitive) or just press Enter for a random seed: ")
	# if no seed was entered, generate one
	if isaacseed == '':
		isaacseed = str(randint(0,999999))
		print("\nRandomly generated seed: " + isaacseed + "\n")
	seed(isaacseed)
except ValueError:
	print("\nThere was an error processing that seed. Quitting...\n")
	raw_input("Script complete.\n")
	sys.exit()

# valid_items is the list of all passive items in the game EXCLUDING the 22 on the no-list
valid_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 27, 28, 32, 46, 48, 50, 51, 52, 53, 54, 55, 57, 60, 62, 63, 64, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 79, 80, 81, 82, 87, 88, 89, 90, 91, 94, 95, 96, 98, 99, 100, 101, 103, 104, 106, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 120, 121, 122, 125, 128, 129, 131, 132, 134, 138, 139, 140, 141, 142, 143, 144, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 159, 161, 162, 163, 165, 167, 168, 169, 170, 172, 173, 174, 178, 179, 180, 182, 183, 184, 185, 187, 188, 189, 190, 191, 193, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 236, 237, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 254, 255, 256, 257, 258, 259, 260, 261, 262, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 327, 328, 329, 330, 331, 332, 333, 335, 336, 337, 340, 341, 342, 343, 345]

# creates list of 30 unique items from the valid items list
itemIDs = sample(valid_items,30)

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

	w, h = draw.textsize("Diversity Mod v0.3 Seed",font=smallfont)
	w2, h2 = draw.textsize(str(isaacseed),font=largefont)
	draw.text((240-w/2, 213),"Diversity Mod v0.3 Seed",(54,47,45),font=smallfont)
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