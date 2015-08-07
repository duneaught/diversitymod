Diversity Mod for The Binding of Isaac: Rebirth

version 0.6

Created by DuneAught (twitter: @duneaught)
with much help from Zamiel, Inschato, Hyphenated & #isaac on SpeedRunsLive

---

To play The Binding of Isaac: Rebirth with Diversity Mod, just run diversitymod.exe. You do not have to move any files nor uninstall other mods. The only requirement is that the Diversity Mod program should not be in the resources folder for Rebirth.

---

Description of the Mod:

All characters start with the D6 except Eden, who gets a random space-use item as usual.

All characters start with 3 additional random passive items, keeping their original items and resources.

Four items (Mom's Knife, Brimstone, IPECAC, & Epic Fetus) have been removed from their respective item pools. They may be assigned as random starting items, but they will not appear in game during a playthrough.

The Special Item status has been removed from the game.

Room modifications are taken directly from Balls of Steel Weekly mod 1.2:
- All Donation Machines have been removed.
- Angel Rooms that offer only soul hearts or eternal hearts have been removed, so Angel Rooms are guaranteed to have one pedestal and an Angel statue.
- Mimics and Doppelgangers spawn off center so the player is not hit upon entering the room.
- Some enemies that spawn close to doors are moved toward the center of the room to prevent unavoidable damage.

---

How the Diversity Mod program works:

Diversity Mod generates and installs mod files based on a user provided seed. If no seed is provided, a random seed will be generated.

The Binding of Isaac: Rebirth must be restarted for changes to take effect. (There's a button for this!)

When Diversity Mod is closed, it uninstalls the mod files it created and restores previously installed mods; so, the program must remain open for the mod to work.

When Diversity Mod is opened, previously installed mods are moved to a temporary folder.

If the resources directory is not in the default Steam location, Diversity Mod will prompt the user for the path to the Rebirth game files.

The Diversity Mod program won't work if it is inside your Rebirth resources folder.

---

Change log:

version 0.7
- fixed title graphic to not be blurry

version 0.6
- updated title graphics and character select graphics
- implemented file browser for user to define Rebirth resources folder when it is not automatically found
- check if Diversity Mod is inside the resources folder, then warn and kill if it is
- spaced code for readability
- stopped creating version.txt
- excluded w9xpopen.exe from final build

version 0.5
- added GUI
- added options.ini to hold custom path
- user is prompted to provide a valid path when the program can't find their steam path
- Diversity Mod files are removed and previous mods are restored when the program is closed
- gave Eden 3 random passive items, but she still gets a random spacebar item

version 0.4+
- packaged with WipeRebirthResourcesFolder for easy uninstall

version 0.4
- automatically starts (or restarts) isaac-ng.exe
- generates a random seed when no seed is entered
- fixed so A Quarter (ID74) is a possible starting item
- changed to have an INCLUDE list instead of an EXCLUDE list
- changed random starting items method to random.sample()

version 0.3
- added Super Bandage (ID92), Blood Bag (ID119), Magic 8 Ball (ID194), Black Lotus (226), & The Body (ID334) to list of excluded passives
- renamed diversitymod.txt to README.md

version 0.2
- changed possible starting items to all passive items from all pools (excluding 17 boring items)
- added version number to character select screen graphic
- made minor changes to the prompts and text output

version 0.1
- hello world

---

Known issues:
-Randomly chosen items can be the same as the starting items of characters. (e.g. Cain can start with 2 lucky feet.)

---

22 Passive items are EXCLUDED from the random starting items.

ID	Name
- 15	<3
- 16	Raw Liver
- 22	Lunch
- 23	Dinner
- 24	Dessert
- 25	Breakfast
- 26	Rotten Meat
- 29	Moms Underwear
- 30	Moms Heels
- 31	Moms Lipstick
- 92	Super Bandage
- 119	Blood Bag
- 176	Stem cells
- 194	Magic 8 Ball
- 226	Black Lotus
- 238	Key Piece #1
- 239	Key Piece #2
- 253	Magic scab
- 334	The Body
- 339	Safety Pin
- 344	Match Book
- 346	A Snack
