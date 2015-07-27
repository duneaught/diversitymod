Diversity Mod for The Binding of Isaac: Rebirth

version 0.4+

Created by DuneAught (twitter: @duneaught)
with much help from Zamiel, Inschato, Hyphenated & #isaac on SpeedRunsLive

---

Running diversitymod.exe does 2 things:

1. Installs Diversity Mod files in the Rebirth resources folder.
2. Starts (or restarts) The Binding of Isaac: Rebirth.

Running WipeRebirthResourcesFolder.exe:

1. Deletes ALL files in the Rebirth resources folder EXCEPT the 'packed' folder.

---

Description of the Mod:

Each character starts with the D6 and 3 random passive items. Eden is unaffected by the mod. Characters who normally start with passive items keep those and get 3 additional items.

Four items (Mom's Knife, Brimstone, IPECAC, & Epic Fetus) have been removed from their respective item pools. They may be assigned as random starting items, but they will not appear in game during a playthrough.

The Special Item status has been removed from the game.

Room modifications are taken directly from Balls of Steel Weekly mod 1.2:
- All Donation Machines have been removed.
- Angel Rooms that offer only soul hearts or eternal hearts have been removed, so Angel Rooms are guaranteed to have one pedestal and an Angel statue.
- Mimics and Doppelgangers spawn off center so the player is not hit upon entering the room.
- Some enemies that spawn close to doors are moved toward the center of the room to prevent unavoidable damage.

---

Important Notes:

To uninstall Rebirth mods, remove everything from the resources directory EXCEPT the "packed" folder. (It is critically important to leave the "packed" folder and its contents unchanged.) It is recommended to uninstall other Rebirth mods before installing Diversity Mod.

Running diversitymod.exe generates and automatically installs Diversity Mod by writing files to The Binding of Isaac: Rebirth resources directory.

Conflicting mod files in the resources directory will be overwritten. Non-conflicting mod files from previously installed mods will remain and affect play.

If the resources directory is not in the default Steam location, the Diversity Mod files will be written to the directory containing diversitymod.exe, and must be manually moved to the resources directory.

Running diversitymod.exe starts The Binding of Isaac: Rebirth. If Rebirth is already running, the game is automatically closed and re-started.

---

Change log:

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
