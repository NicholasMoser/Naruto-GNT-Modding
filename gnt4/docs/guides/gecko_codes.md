# GNT4 Gecko Codes

These are codes that modify the game in various ways. You can add them to games by right clicking on the game in Dolphin and going to properties. Go to Gecko Codes and you can add them here by either going to Edit Config or hitting the Add button (Add button only exists in latest Dolphin versions).

Most of the codes you'll find here were written by [Ralf from GC-FOREVER](http://www.gc-forever.com/forums/viewtopic.php?t=2174).

## Table of Contents

1. **[General](#general)**
2. **[Experimental](#experimental)**
3. **[Player 1 Codes](#player-1-codes)**
4. **[Player 2 Codes](#player-2-codes)**
5. **[Player 3 Codes](#player-3-codes)**
6. **[Player 4 Codes](#player-4-codes)**
7. **[Global Character Modifiers](#global-character-modifiers)**
8. **[Character Replacers](#character-replacers)**
9. **[DOL Injection Codes](#dol-injection-codes)**

## General

### Skip Three Intro Videos [Nick]

```gecko
0400CB14 60000000
0400CB28 60000000
0400CB3C 60000000
```

### Infinite Time [Ralf]

```gecko
040374B8 60000000
```

### Unlock Everything [Nick]

The original version of this code was written by Ralf, and has been modified to remove unlock notices when this code is used with no save data.

```gecko
02223258 0017FFFF
042232E8 0001FF03
042232F0 00FFFFFF
022232FC 0021FFFF
```

### Enable DPad During Fights [Ralf]

```gecko
C2042C40 00000007
54A007BD 41820008
64A50008 54A007FF
41820008 64A50004
54A0077B 41820008
64A50002 54A00739
41820008 64A50001
80030154 00000000
```

### 16:9 Aspect Ratio (Widescreen) [Ralf]

```gecko
0416E15C C3A2A024
04279CC4 3FE38E39
```

### Enable Training Menu (All Modes) [Ralf]

```gecko
0400B520 38600003
```

### Enable Fight Debug Menu [Ralf]

```gecko
022233A8 00000002
04222FB8 8004CB64
```

### Battle Mode is the Default Menu Option [Nick]

```gecko
c20d687c 00000002
38000002 b0030000
38000000 00000000
```

When you first start up the game, Battle Mode will be selected by default. This is the menu option with 1v1 and 4p mode. To change it to use a different mode instead, replace the `00000002` with a different number.

### 3MC Training Mode Uses Fight Debug Menu [Nick]

```gecko
c2045328 00000005
9003001c 3ca08022
800561ec 28000007
40820010 3ca08005
38a5cb64 90a40008
60000000 00000000
```

### 3MC Training Mode is 1v1 Training Mode and 1v1 Training Mode Uses Fight Debug Menu [Nick]

```gecko
c2045328 00000006
9003001c 3ca08022
800561ec 28000007
40820010 38000006
900561ec 48000010
3ca08005 38a5cb64
90a40008 00000000
```

### Rounds Default is 3 [Nick]

```gecko
0400b2fc b07f0192
```

### Match Time Default is 90 [Nick]

```gecko
0400b304 b09f0196
```

### Audio Plays While Paused [Nick]

```gecko
04044d28 3860ffff
0404712c 3860ffff
040477fc 3860ffff
```

The above code is actually comprised of three codes. The first plays audio when you pause in training mode.
The second plays audio when you pause in mission mode. The third plays audio when you pause in other modes.
The volume can be modified by changing the `ffff` to a different value. `0000` is mute, which is the default.
If you want the audio somewhat softer, the value `0fff` is recommended. However, using a value other than `ffff`
will result in the audio playing while paused even if audio is disabled through the in-game options.

### Fight Debug Menu

START            = Debug Menu On/Off & Go Into Sub-Menu  
Stick Up/Down    = Select Sub-Menu & Debug Option  
Stick Left/Right = Change Value  
Z + START        = Abort (Return to Title Screen)

### Fight Debug Camera

Z                  = Skip One Frame & Reset Camera  
R/L                = Zoom In/Out  
DPad               = Strafe  
C-Stick Up/Down    = Look Up/Down  
C-Stick Left/Right = Rotate Left/Right

### Mission Mode Complete [Ralf]

```gecko
02223228 0017FFFF
```

### Hit Anywhere (All Players) [Ralf]

```gecko
0403C95C 60000000
```

### Disable Blocking (All Players) [Ralf]

```gecko
0403A7E4 60000000
```

### Training Mode Default 2P Action: 2P Control [Nick]

By default, 2P Action is set to Stand in training mode. This changes the default to 2P Control.

Note: This new default will only take affect after pausing unless you modify `files/game/game00.seq` by changing 11 to 13 at offset 0x11277.

```gecko
c2045350 00000002
38000002 b003002c
60000000 00000000
0402e718 3bc00012
0402e728 3bc00012
```

### Training Mode Default Guard: ON [Nick]

By default, Guard is set to OFF in training mode. This changes the default to ON.

Note: This new default will only take affect after pausing unless you modify `files/game/game00.seq` by changing 01 to 00 at offset 0x11287

```gecko
04045360 B0A30030
```

### Training Mode Default Show Inputs: OFF [Nick]

By default, Show Inputs is set to ON in training mode. This changes the default to OFF.

```gecko
04045364 B0A30032
C204CF8C 00000004
3FE08022 3BFF61D8
83FF221C 64000080
901F0000 80010024
60000000 00000000
```

### Training Mode Default Chakra Recovery: OFF [Nick]

By default, Chakra Recovery is set to ON in training mode. This changes the default to OFF.

Note: This new default will only take affect after pausing unless you modify `files/game/game00.seq` by changing C0 to 00 at offset 0x11286

```gecko
04045380 B0A30040
```

## Experimental

These codes are experimental and may cause unintended side effects, even crashes in some cases.

### Remove Port Priority on Throw Breaks

In GNT4, throw breaking is affected by port priority. Higher port priority in this case is whoever is
P4 or closest to P4. Then a player throws another player, the throw break window is:

- 3 if the attacker has **lower** port priority than the defender
- 2 if the attacker has **higher** port priority than the defender

For example, P4 has higher port priority than all other players. Therefore when thrown, P4 always will have
a 3 frame throw break window. When P4 throws other players, they will always have a 2 frame throw break window.
The opposite is true for P1, as they will always have a 2 frame throw break window when defending and give other
players a 3 frame throw break window.

```gecko
C20632C0 00000006
80790004 80C50004
7C033000 40810014
2C000200 4082000C
38600201 906502F8
2C000000 38C00000
60000000 00000000
```

### Other Character Don't Stop Your Character From Running

When your character runs at another character, your character will stop when they touch the other character's body. This code prevents that
so that you can continue running. An example can be seen [in this video](https://imgur.com/a/h1uvV2i).

This is accomplished by removing the PF flag BODY when players touch, which may have side effects. This does not affect when you run against
the wall of a stage, which instead applies the PF flag M_KABE.

```gecko
0403985c 60000000
04039868 60000000
```

### Allow Players to Pick Tsunade Confusion Effect

If you enable the above code, it lets Tsunade decide whether to reverse buttons or reverse movement based
on what direction you're holding the control stick in the moment the confusion attack hits.

Left is always reverse buttons, right is always reverse movement. Doesn't matter which way your character is
facing. Doesn't matter if Tsunade confusion currently has your own movement swapped. If you are holding neither
movement, it continues to use the old RNG value it used to use for confusion.

One side effect is that it
retrieves the controller inputs of the player id that does it. So if a CPU does the Tsunade confusion attack,
it will read inputs from that player controller (e.g. controller 2 for 1v1 matches). That really should never
come into play, but I suppose if someone was holding left or right on P2 they could always force Tsunade CPU to
do one or the other.

```gecko
C203BAD4 00000008
901102A4 80100004
1C000040 3C608022
38632EB0 7C630214
80030024 5403035B
4182000C 38600001
907102A0 54030319
4182000C 38600000
907102A0 00000000
```

### Counter Hit Plays Sound

It will play sound effect `53` from sound effect group `02`. Group `02` is where "general" sound effects like attacks go. Sound effect `53` is a sort of fanfare noise that isn't normally used in combat. Group `00` is battle sounds. Group `01` is announcer sounds. Groups over `02` are character sounds.

You can test other sound effects by replacing the `53` in `38800253` from the above code. The `02` before the `53` is the sound group.

```gecko
c203a378 00000008
2c150080 41820030
7c771b78 38600300
38800253 38a07f00
38c00000 38e00000
3c00800c 6000e4a8
7c0903a6 4e800421
7ee3bb78 3a700166
60000000 00000000
```

### Naruto's Clone Drains Chakra Really Fast [Nick]

```gecko
0403e8dc 3803ff01
```

### Naruto's Clone Never Drains Chakra [Nick]

```gecko
0403e8dc 38030000
```

### Naruto's Clone Drains Chakra Slower [Nick]

```gecko
0403e8dc 3803ffe0
```

### Unlimited Block Guard [Nick]

```gecko
0403F0A8 60000000
```

### X Does Not Throw Break [Nick]

When you don't have full chakra, you can mash X for easy throw breaks. This disables X as a throw break button completely to disable that.

```gecko
040632f0 70000230
```

### Modify ZTK Damage Multiplier [Nick]

Normally, ZTK takes 1.5x damage on all attacks. You can modify this value using the below code. The `3f800000` is the multiplier as a float. The code below has it set to 1.0, thus makes it so that ZTK takes the same damage as all other characters.

```gecko
04278890 3f800000
```

### Modify Ukon Damage Multiplier [Nick]

Normally, Ukon takes 1.2x damage on all attacks. You can modify this value using the below code. The `3f800000` is the multiplier as a float. The code below has it set to 1.0, thus makes it so that Ukon takes the same damage as all other characters.

```gecko
04278894 3f800000
```

### Remove Sharingan Kakashi Health Drain [Nick]

```gecko
0403ea14 38030000
```

### Remove ZTK Health Drain [Nick]

```gecko
0403ea5c 38030000
```

### Remove 2-Gate Lee Health Drain [Nick]

```gecko
0403e9cc 38030000
```

### Change Number of Rounds to Win [Nick]

```gecko
0422627c 000000xx
```

Change the last byte to the number of rounds you wish to win.

### ZTK, Ukon, 1G Lee, and S. Kakashi takes 1.25x damage and 2GLee takes 1.5x damage [Nick]

```gecko
04278894 3FA00000
0403E2C0 2C000004
0403E2D0 5400077B
C203E2B0 00000007
8003001C 28000008
41820028 28000003
41820020 28000004
4082001C 80030854
5400077B 4182000C
38000004 48000008
38000022 00000000
```

This is in contrast to normal circumstances, where Ukon takes 1.2x damage and ZTK takes 1.5x damage.

### ZTK and S. Kakashi take 1.25x damage [Nick]

```gecko
04278890 3fa00000
c203e2b0 00000003
8003001c 28000003
40820008 38000008
60000000 00000000
```

This is in contrast to normal circumstances, where Ukon takes 1.2x damage and ZTK takes 1.5x damage.

### No limit to Choji Chip Eating Attack Boost [Nick]

```gecko
0401703C 60000000
```

### Duplicate Characters in 4-Player Mode [Nick]

```gecko
48000000 802a4324
de000000 80008180
140142b0 00000000
140142f8 00000000
140142b4 00000000
14014318 00000000
140142b8 00000000
14014338 00000000
140142bc 00000000
14014358 00000000
e0000000 80008000
```

### No Slow Down on Kill [Nick]

```gecko
04014868 60000000
```

### No Slow Down on Kill (Training Mode Only) [Nick]

```gecko
c2014884 00000006
3c808022 608461ec
80840000 2c040006
41800014 2c040007
4181000c 38600000
b0650000 3c608022
60000000 00000000
```

### Turn off grab break while DEF or SDEF is active [Nick]

The grab break window is set at the beginning of victim states for all throws. This sets the DF flag "TEscape" for three frames
which allows you to break a grab by inputting a face button. This gecko code makes a player unable to break this grab if the victim
is grabbed during a time when the AF flag DEF is active. Therefore, during a 4A counter, a 2X super counter, or a 4B move when the
guard frames are active, you would not be able to break the grab.

See [GNTool Issue #43](https://github.com/NicholasMoser/GNTool/issues/43) for more info.

```gecko
C20B5140 00000003
801F0128 540000C7
4082000C 5480402E
901F02F8 00000000
040b5144 60000000
```

### Add Random Select to Character Select Screen [Nick]

This replaces Akamaru with random select. Akamaru is also moved to the top of the Character Select Screen, replacing Awakened Hinata.
Awakened Hinata is move to where Akamaru was, below Normal Hinanta. Random Select will **not** select Akamaru, Karasu, Oboro, or
Tayayu's Doki Demon. If you'd prefer this code without the characters being moved, remove the last two lines of the code.

```gecko
c215b9e8 00000003
2c000011 40820008
38006dad 7c04412e
60000000 00000000
c2092154 0000000e
7ca6282e 2c056dad
40820064 9421fff0
90610004 90010008
9081000c 38600029
3ca0801c 60a5ce50
7ca903a6 4e800421
2c030000 4081ffe8
2c03000f 4182ffe0
2c030011 4182ffd8
2c030014 4182ffd0
2c030029 4080ffc8
7c651b78 8081000c
80010008 80610004
38210010 00000000
04213fb4 00000026
04214014 00000011
```

## Player 1 Codes

### P1 Infinite Health [Ralf]

```gecko
48000000 80226358
DE000000 80008180
12000262 00000000
E0000000 80008000
```

### P1 Infinite Chakra [Ralf]

```gecko
48000000 80226358
DE000000 80008180
1200028E 00003C00
E0000000 80008000
```

### P1 1 Hit Kills (Press B) [Ralf]

```gecko
48000000 80226358
DE000000 80008180
120002BE 000000FF
E0000000 80008000
```

### P1 Moon Jump (Press Stick Up Multiple Times) [Ralf]

```gecko
06004000 0000001C
3C608022 80636358
7C1F1840 807F0130
40820008 480143DC
480143D0 00000000
040183E4 4BFEBC1C
```

### P1 Low Gravity [Nick]

```gecko
48000000 80226358
DE000000 80008180
320001E0 00000000
140001E0 BCF5C28F
E0000000 80008000
```

[Notes](#gravity-adjustment)

### P1 Hit Anywhere [Ralf]

```gecko
C203C958 00000004
3C808022 80046358
7C00C800 40820008
38600001 2C030000
60000000 00000000
```

### P1 Never Blocking [Ralf]

```gecko
C203A7E0 00000004
3C608022 80036358
7C008800 40820008
3B600000 281B0000
60000000 00000000
```

### P1 Always Blocking [Ralf]

```gecko
C203A7E0 00000004
3C608022 80036358
7C008800 40820008
3B600001 281B0000
60000000 00000000
```

## Player 2 Codes

### P2 Infinite Health [Ralf]

```gecko
48000000 80226614
DE000000 80008180
12000262 00000000
E0000000 80008000
```

### P2 Infinite Chakra [Ralf]

```gecko
48000000 80226614
DE000000 80008180
1200028E 00003C00
E0000000 80008000
```

### P2 1 Hit Kills (Press B) [Ralf]

```gecko
48000000 80226614
DE000000 80008180
120002BE 000000FF
E0000000 80008000
```

### P2 Moon Jump (Press Stick Up Multiple Times) [Ralf]

```gecko
06004020 00000020
3C608022 80636614
7C1F1840 807F0130
40820008 480143BC
54600739 480143B0
040183E8 4BFEBC38
```

### P2 Low Gravity [Nick]

```gecko
48000000 80226614
DE000000 80008180
320001E0 00000000
140001E0 BCF5C28F
E0000000 80008000
```

[Notes](#gravity-adjustment)

### P2 Hit Anywhere [Ralf]

```gecko
0600391C 00000024
3C808022 80046614
7C00C800 40820008
38600001 2C030000
40820008 480390C4
48039024 00000000
0403C95C 4BFC6FC0
```

### P2 Never Blocking [Ralf]

```gecko
0600381C 00000024
3C608022 80036614
7C008800 40820008
3B600000 281B0000
40820008 48036FB0
480382A0 00000000
0403A7E4 4BFC9038
```

### P2 Always Blocking [Ralf]

```gecko
0600381C 00000024
3C608022 80036614
7C008800 40820008
3B600001 281B0000
40820008 48036FB0
480382A0 00000000
0403A7E4 4BFC9038
```

## Player 3 Codes

### P3 Infinite Health [Ralf]

```gecko
48000000 802268D0
DE000000 80008180
12000262 00000000
E0000000 80008000
```

### P3 Infinite Chakra [Ralf]

```gecko
48000000 802268D0
DE000000 80008180
1200028E 00003C00
E0000000 80008000
```

### P3 1 Hit Kills (Press B) [Ralf]

```gecko
48000000 802268D0
DE000000 80008180
120002BE 000000FF
E0000000 80008000
```

### P3 Low Gravity [Nick]

```gecko
48000000 802268D0
DE000000 80008180
320001E0 00000000
140001E0 BCF5C28F
E0000000 80008000
```

[Notes](#gravity-adjustment)

## Player 4 Codes

### P4 Infinite Health [Ralf]

```gecko
48000000 80226B8C
DE000000 80008180
12000262 00000000
E0000000 80008000
```

### P4 Infinite Chakra [Ralf]

```gecko
48000000 80226B8C
DE000000 80008180
1200028E 00003C00
E0000000 80008000
```

### P4 1 Hit Kills (Press B) [Ralf]

```gecko
48000000 80226B8C
DE000000 80008180
120002BE 000000FF
E0000000 80008000
```

### P4 Low Gravity [Nick]

```gecko
48000000 80226B8C
DE000000 80008180
320001E0 00000000
140001E0 BCF5C28F
E0000000 80008000
```

[Notes](#gravity-adjustment)

## Global Character Modifiers

These are customizable codes where you can replace it yourself. For example, to replace Oboro with Tayuya you can use the following code created from the below sections:

```gecko
04208850 80278954
```

These changes are global and therefore affect story mode, so you could replace Naruto with Orochimaru with the following code:  

```gecko
04208820 80278914
```

### Character IDs (Global Character Modifiers)

xxx = Character ID

8CC - Sasuke  
8D0 - Haku  
8D4 - Kakashi  
8D8 - Rock Lee  
8DC - Iruka  
8E0 - Zabuza  
8E4 - Sakura  
8E8 - Naruto  
8EC - Ino  
8F0 - Shikamaru  
8F4 - Neji  
8F8 - Hinata  
8FC - Might Guy  
900 - Kankuro  
904 - Karasu

908 - Kiba  
90C - Akamaru  
910 - Gaara  
914 - Orochimaru  
918 - Oboro  
91C - Mizuki  
920 - Anko  
924 - Jiraiya  
928 - Choji  
92C - Tenten  
930 - Temari  
934 - Shino  
938 - Itachi  
93C - Tsunade  
940 - Hiruzen  
944 - Kimimaro

948 - Jirobo  
94C - Kidomaru  
950 - Sakon  
954 - Tayuya  
958 - Kisame  
95C - Sasuke CS2  
960 - Naruto Kyuubi  
964 - Kabuto  
968 - Awakened Hinata  
96C - Tayuya's Doki Demon  

### Sasuke [Ralf]

```gecko
04208804 80278xxx
```

### Haku [Ralf]

```gecko
04208808 80278xxx
```

### Kakashi [Ralf]

```gecko
0420880C 80278xxx
```

### Rock Lee [Ralf]

```gecko
04208810 80278xxx
```

### Iruka [Ralf]

```gecko
04208814 80278xxx
```

### Zabuza [Ralf]

```gecko
04208818 80278xxx
```

### Sakura [Ralf]

```gecko
0420881C 80278xxx
```

### Naruto [Ralf]

```gecko
04208820 80278xxx
```

### Ino [Ralf]

```gecko
04208824 80278xxx
```

### Shikamaru [Ralf]

```gecko
04208828 80278xxx
```

### Neji [Ralf]

```gecko
0420882C 80278xxx
```

### Hinata [Ralf]

```gecko
04208830 80278xxx
```

### Might Guy [Ralf]

```gecko
04208834 80278xxx
```

### Kankuro [Ralf]

```gecko
04208838 80278xxx
```

### Karasu [Ralf]

```gecko
0420883C 80278xxx
```

### Kiba [Ralf]

```gecko
04208840 80278xxx
```

### Akamaru [Ralf]

```gecko
04208844 80278xxx
```

### Gaara [Ralf]

```gecko
04208848 80278xxx
```

### Orochimaru [Ralf]

```gecko
0420884C 80278xxx
```

### Oboro [Ralf]

```gecko
04208850 80278xxx
```

### Mizuki [Ralf]

```gecko
04208854 80278xxx
```

### Anko [Ralf]

```gecko
04208858 80278xxx
```

### Jiraiya [Ralf]

```gecko
0420885C 80278xxx
```

### Choji [Ralf]

```gecko
04208860 80278xxx
```

### Tenten [Ralf]

```gecko
04208864 80278xxx
```

### Temari [Ralf]

```gecko
04208868 80278xxx
```

### Shino [Ralf]

```gecko
0420886C 80278xxx
```

### Itachi [Ralf]

```gecko
04208870 80278xxx
```

### Tsunade [Ralf]

```gecko
04208874 80278xxx
```

### Hiruzen [Ralf]

```gecko
04208878 80278xxx
```

### Kimimaro [Ralf]

```gecko
0420887C 80278xxx
```

### Jirobo [Ralf]

```gecko
04208880 80278xxx
```

### Kidomaru [Ralf]

```gecko
04208884 80278xxx
```

### Sakon [Ralf]

```gecko
04208888 80278xxx
```

### Tayuya [Ralf]

```gecko
0420888C 80278xxx
```

### Kisame [Ralf]

```gecko
04208890 80278xxx
```

### Sasuke CS2 [Ralf]

```gecko
04208894 80278xxx
```

### Naruto Kyuubi [Ralf]

```gecko
04208898 80278xxx
```

### Kabuto [Ralf]

```gecko
0420889C 80278xxx
```

### Awakened Hinata [Ralf]

```gecko
042088A0 80278xxx
```

### Tayuya's Doki Demon [Ralf]

```gecko
042088A4 80278xxx
```

## Character Replacers

### Character Replacer (1 Character Version) [Ralf]

```gecko
06004B54 00000014
2C0500xx 40820008
38A000yy 3C808020
4E800020 00000000
040400A8 4BFC4AAD
0404032C 4BFC4829
```

xx/yy = Character IDs

Replaces Character xx with Character yy.

### Character Replacer (2 Characters Version) [Ralf]

```gecko
06004B54 00000024
2C0500vv 4082000C
38A000ww 48000010
2C0500xx 40820008
38A000yy 3C808020
4E800020 00000000
040400A8 4BFC4AAD
0404032C 4BFC4829
```

vv/ww = Character 1 IDs  
xx/yy = Character 2 IDs

Replaces Character vv with Character ww and Character xx with Character yy.

### Character Replacer (3 Characters Version) [Ralf]

```gecko
06004B54 00000034
2C0500tt 4082000C
38A000uu 48000020
2C0500vv 4082000C
38A000ww 48000010
2C0500xx 40820008
38A000yy 3C808020
4E800020 00000000
040400A8 4BFC4AAD
0404032C 4BFC4829
```

tt/uu = Character 1 IDs  
vv/ww = Character 2 IDs  
xx/yy = Character 3 IDs

Replaces Character tt with Character uu, Character vv with Character ww and Character xx with Character yy.

### Character IDs (Character Replacers)

01 - Sasuke  
02 - Haku  
03 - Kakashi  
04 - Rock Lee  
05 - Iruka  
06 - Zabuza  
07 - Sakura  
08 - Naruto  
09 - Ino  
0A - Shikamaru  
0B - Neji  
0C - Hinata  
0D - Might Guy  
0E - Kankuro  
0F - Karasu  
10 - Kiba  
11 - Akamaru  
12 - Gaara  
13 - Orochimaru  
14 - Oboro  
15 - Mizuki  
16 - Anko  
17 - Jiraiya  
18 - Choji  
19 - Tenten  
1A - Temari  
1B - Shino  
1C - Itachi  
1D - Tsunade  
1E - Hiruzen  
1F - Kimimaro  
20 - Jirobo  
21 - Kidomaru  
22 - Sakon  
23 - Tayuya  
24 - Kisame  
25 - Sasuke CS2  
26 - Naruto Kyuubi  
27 - Kabuto  
28 - Awakened Hinata  
29 - Tayuya's Doki Demon

### Replace Character With Oboro [Ralf]

```gecko
06004B00 00000020
2C0500xx 40820014
38A00014 2C060001
40820008 38C00000
7C7A1B78 4E800020
040400AC 4BFC4A55
04040330 4BFC47D1
```

xx = Character ID

### Replace Character With Tayuya's Doki Demon [Ralf]

```gecko
06004B20 00000034
2C0500xx 40820014
38A00029 2C060001
40820008 38C00000
7C9B2378 4E800020
2C030000 38000000
41820008 80030030
480A3B8C 00000000
040400A4 4BFC4A7D
04040328 4BFC47F9
040A86D8 4BF5C468
```

xx = Character ID

### Replace Akamaru With Karasu [Ralf]

```gecko
06004B54 00000014
2C050011 40820008
38A0000F 3C808020
4E800020 00000000
040400A8 4BFC4AAD
0404032C 4BFC4829
```

### Replace Naruto, Sasuke & Sakura With Hinata [Ralf]

```gecko
06004B54 00000034
2C050008 4082000C
38A0000C 48000020
2C050001 4082000C
38A0000C 48000010
2C050007 40820008
38A0000C 3C808020
4E800020 00000000
040400A8 4BFC4AAD
0404032C 4BFC4829
```

### Replace Sakura With Oboro [Ralf]

```gecko
06004B00 00000020
2C050007 40820014
38A00014 2C060001
40820008 38C00000
7C7A1B78 4E800020
040400AC 4BFC4A55
04040330 4BFC47D1
```

### Replace Ino With Tayuya's Doki Demon [Ralf]

```gecko
06004B20 00000034
2C050009 40820014
38A00029 2C060001
40820008 38C00000
7C9B2378 4E800020
2C030000 38000000
41820008 80030030
480A3B8C 00000000
040400A4 4BFC4A7D
04040328 4BFC47F9
040A86D8 4BF5C468
```

## DOL Injection Codes

When modding the game, you may want to distribute an ISO that has codes built-in. Certain codes cannot be built into an ISO since they either directly manipulate RAM or inject more code than can fit in a section of the dol. Therefore, this section contains modified forms of the above codes that can be injected into the dol.

### Unlock Everything [Nick]

For more information on the specifics of this code, see [GNTool/issues/32](https://github.com/NicholasMoser/GNTool/issues/32#issuecomment-743796834).

```gecko
c200ca80 00000012
3860ffff 3fc08022
907e3258 907e325c
907e3260 907e3264
907e3268 907e326c
907e3270 907e3274
907e3278 907e327c
907e3280 907e3284
907e32fc 907e3300
907e3304 907e3308
907e330c 907e3310
907e3314 907e3318
907e331c 907e3320
907e3324 907e3328
907e332c 907e3330
907e3334 907e3338
907e333c 3fe00002
387fff03 907e32e8
38600000 00000000
```

## Gravity Adjustment

The Gecko codes for low gravity can easily be modified to use different gravity values. This is accomplished by adjusting the value following 0x140001E0. For example, the default set for the codes listed on this page is 0xBCF5C28F. That number is the hexadecimal representation of the float -0.03. The default gravity value of the game is 0xBDAA0000 (-0.083008). Gravity in this case represents the change in speed that occurs each frame of the game. Here are the results of using -0.03 for the gravity:

![Low Gravity](/gnt4/images/gameplay/low_gravity.gif?raw=true "Low Gravity")

Here is an example of using 0xBE23D70A (-0.16):

![High Gravity](/gnt4/images/gameplay/high_gravity.gif?raw=true "High Gravity")

As you can see, any float closer to zero than -0.083008 will be lower gravity and any float further from zero will be higher gravity.

## SCON4 Codes

These are codes only used in SCON4. They aren't generally applicable as they likely involve file modifications as well, making them crash or not work if used with a vanilla copy of the game.

### Tsunade: Punch KF Flag Reverses Buttons, Kick KF Flag Reverses Movement

```gecko
C203BAD4 00000006
901102A4 80100138
540305AD 4182000C
38600001 907102A0
5403056B 4182000C
38600000 907102A0
60000000 00000000
```

### Tsunade: Punch KF Flag Reverses Buttons, Kick KF Flag Reverses Movement

```gecko
C203BAD4 00000006
901102A4 80100138
540305AD 4182000C
38600000 907102A0
5403056B 4182000C
38600001 907102A0
60000000 00000000
```

### Add Random Select and Reorder CSS [Nick]

For more info see https://github.com/NicholasMoser/GNTool/issues/68

More logic was added so that Akamaru's name always shows for random select. Akamaru's name graphic could then be replaced with Random or something.

```gecko
c215b9e8 00000003
2c000011 40820008
38006dad 7c04412e
60000000 00000000
C2092154 00000010
7CA6282E 2C056DAD
40820074 2C000098
4182000C 38A00011
48000064 9421FFF0
90610004 90010008
9081000C 38600029
3CA0801C 60A5CE50
7CA903A6 4E800421
2C030000 4081FFE8
2C03000F 4182FFE0
2C030011 4182FFD8
2C030014 4182FFD0
2C030029 4080FFC8
7C651B78 8081000C
80010008 80610004
38210010 00000000
04213F80 00000024
04213F84 00000001
04213F88 00000023
04213F8C 00000002
04213F90 00000003
04213F94 0000000A
04213F98 00000007
04213F9C 00000012
04213FA0 0000000B
04213FA4 0000000D
04213FA8 00000014
04213FAC 0000000C
04213FB0 00000013
04213FB4 0000000E
04213FB8 0000000F
04213FBC 00000026
04213FC0 00000009
04213FC4 00000015
04213FC8 00000008
04213FCC 0000001A
04213FD0 00000006
04213FD4 00000005
04213FD8 00000004
04213FDC 0000001B
04213FE0 0000001C
04213FE4 00000018
04213FE8 00000016
04213FEC 00000017
04213FF0 00000010
04213FF4 00000025
04213FF8 00000020
04213FFC 00000021
04214000 0000001E
04214004 0000001F
04214008 0000001D
0421400C 00000019
04214010 00000022
04214014 00000011
```
