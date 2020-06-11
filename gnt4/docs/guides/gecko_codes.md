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

## General

### Skip Three Intro Videos [Nicholas Moser]

C200CB14 00000001  
60000000 00000000  
C200CB28 00000001  
60000000 00000000  
C200CB3C 00000001  
60000000 00000000

### Infinite Time [Ralf]

040374B8 60000000

### Unlock Everything [Ralf]

02223258 0017FFFF  
042232E8 0001FF03  
042232F0 00FFFFFF  
022232FC 0017FFFF

### Enable DPad During Fights [Ralf]

C2042C40 00000007  
54A007BD 41820008  
64A50008 54A007FF  
41820008 64A50004  
54A0077B 41820008  
64A50002 54A00739  
41820008 64A50001  
80030154 00000000

### 16:9 Aspect Ratio (Widescreen) [Ralf]

0416E15C C3A2A024  
04279CC4 3FE38E39

### Enable Training Menu (All Modes) [Ralf]

0400B520 38600003

### Enable Fight Debug Menu [Ralf]

022233A8 00000002  
04222FB8 8004CB64

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

02223228 0017FFFF

### Hit Anywhere (All Players) [Ralf]

0403C95C 60000000

### Disable Blocking (All Players) [Ralf]

0403A7E4 60000000

## Experimental (May cause unintended side effects or crash)

### No limit to Choji Chip Eating Attack Boost [Nicholas Moser]

C201703C 00000001  
60000000 00000000

### Duplicate Characters in 4-Player Mode [Nicholas Moser]

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

### No Slow Down on Kill [Nicholas Moser]

C2014868 00000001  
60000000 00000000

### Add Random Select to Character Select (Activate with Down+Start) [Nicholas Moser]

C2091ED4 00000015  
3C800145 7C043800  
40820098 2C1F0020  
4082001C 3C808022  
60842D40 80840000  
5484843E 2C041000  
41820064 2C1F0021  
4082001C 3C808022  
60842D4C 80840000  
5484843E 2C041000  
41820044 2C1F0022  
4082001C 3C808022  
60842D58 80840000  
5484843E 2C041000  
41820024 2C1F0023  
40820030 3C808022  
60842D64 80840000  
5484843E 2C041000  
40820018 7F63DB78  
3C80801C 6084CE50  
7C8903A6 4E800421  
808D8878 00000000  
C2091EE8 00000003  
2C030000 41820008  
7C601B78 7C04292E  
60000000 00000000

## Player 1 Codes

### P1 Infinite Health [Ralf]

48000000 80226358  
DE000000 80008180  
12000262 00000000  
E0000000 80008000

### P1 Infinite Chakra [Ralf]

48000000 80226358  
DE000000 80008180  
1200028E 00003C00  
E0000000 80008000

### P1 1 Hit Kills (Press B) [Ralf]

48000000 80226358  
DE000000 80008180  
120002BE 000000FF  
E0000000 80008000

### P1 Moon Jump (Press Stick Up Multiple Times) [Ralf]

06004000 0000001C  
3C608022 80636358  
7C1F1840 807F0130  
40820008 480143DC  
480143D0 00000000  
040183E4 4BFEBC1C

### P1 Low Gravity [Nicholas Moser]

48000000 80226358  
DE000000 80008180  
320001E0 00000000  
140001E0 BCF5C28F  
E0000000 80008000  
[Notes](#gravity-adjustment)

### P1 Hit Anywhere [Ralf]

C203C958 00000004  
3C808022 80046358  
7C00C800 40820008  
38600001 2C030000  
60000000 00000000

### P1 Never Blocking [Ralf]

C203A7E0 00000004  
3C608022 80036358  
7C008800 40820008  
3B600000 281B0000  
60000000 00000000

### P1 Always Blocking [Ralf]

C203A7E0 00000004  
3C608022 80036358  
7C008800 40820008  
3B600001 281B0000  
60000000 00000000

## Player 2 Codes

### P2 Infinite Health [Ralf]

48000000 80226614  
DE000000 80008180  
12000262 00000000  
E0000000 80008000

### P2 Infinite Chakra [Ralf]

48000000 80226614  
DE000000 80008180  
1200028E 00003C00  
E0000000 80008000

### P2 1 Hit Kills (Press B) [Ralf]

48000000 80226614  
DE000000 80008180  
120002BE 000000FF  
E0000000 80008000

### P2 Moon Jump (Press Stick Up Multiple Times) [Ralf]

06004020 00000020  
3C608022 80636614  
7C1F1840 807F0130  
40820008 480143BC  
54600739 480143B0  
040183E8 4BFEBC38

### P2 Low Gravity [Nicholas Moser]

48000000 80226614  
DE000000 80008180  
320001E0 00000000  
140001E0 BCF5C28F  
E0000000 80008000  
[Notes](#gravity-adjustment)

### P2 Hit Anywhere [Ralf]

0600391C 00000024  
3C808022 80046614  
7C00C800 40820008  
38600001 2C030000  
40820008 480390C4  
48039024 00000000  
0403C95C 4BFC6FC0

### P2 Never Blocking [Ralf]

0600381C 00000024  
3C608022 80036614  
7C008800 40820008  
3B600000 281B0000  
40820008 48036FB0  
480382A0 00000000  
0403A7E4 4BFC9038

### P2 Always Blocking [Ralf]

0600381C 00000024  
3C608022 80036614  
7C008800 40820008  
3B600001 281B0000  
40820008 48036FB0  
480382A0 00000000  
0403A7E4 4BFC9038

## Player 3 Codes

### P3 Infinite Health [Ralf]

48000000 802268D0  
DE000000 80008180  
12000262 00000000  
E0000000 80008000

### P3 Infinite Chakra [Ralf]

48000000 802268D0  
DE000000 80008180  
1200028E 00003C00  
E0000000 80008000

### P3 1 Hit Kills (Press B) [Ralf]

48000000 802268D0  
DE000000 80008180  
120002BE 000000FF  
E0000000 80008000

### P3 Low Gravity [Nicholas Moser]

48000000 802268D0  
DE000000 80008180  
320001E0 00000000  
140001E0 BCF5C28F  
E0000000 80008000  
[Notes](#gravity-adjustment)

## Player 4 Codes

### P4 Infinite Health [Ralf]

48000000 80226B8C  
DE000000 80008180  
12000262 00000000  
E0000000 80008000

### P4 Infinite Chakra [Ralf]

48000000 80226B8C  
DE000000 80008180  
1200028E 00003C00  
E0000000 80008000

### P4 1 Hit Kills (Press B) [Ralf]

48000000 80226B8C  
DE000000 80008180  
120002BE 000000FF  
E0000000 80008000

### P4 Low Gravity [Nicholas Moser]

48000000 80226B8C  
DE000000 80008180  
320001E0 00000000  
140001E0 BCF5C28F  
E0000000 80008000  
[Notes](#gravity-adjustment)

## Global Character Modifiers

These are customizable codes where you can replace it yourself. For example, to replace Oboro with Tayuya you can use the following code created from the below sections:  
`04208850 80278954`

These changes are global and therefore affect story mode, so you could replace Naruto with Orochimaru with the following code:  
`04208820 80278914`

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

04208804 80278xxx

### Haku [Ralf]

04208808 80278xxx

### Kakashi [Ralf]

0420880C 80278xxx

### Rock Lee [Ralf]

04208810 80278xxx

### Iruka [Ralf]

04208814 80278xxx

### Zabuza [Ralf]

04208818 80278xxx

### Sakura [Ralf]

0420881C 80278xxx

### Naruto [Ralf]

04208820 80278xxx

### Ino [Ralf]

04208824 80278xxx

### Shikamaru [Ralf]

04208828 80278xxx

### Neji [Ralf]

0420882C 80278xxx

### Hinata [Ralf]

04208830 80278xxx

### Might Guy [Ralf]

04208834 80278xxx

### Kankuro [Ralf]

04208838 80278xxx

### Karasu [Ralf]

0420883C 80278xxx

### Kiba [Ralf]

04208840 80278xxx

### Akamaru [Ralf]

04208844 80278xxx

### Gaara [Ralf]

04208848 80278xxx

### Orochimaru [Ralf]

0420884C 80278xxx

### Oboro [Ralf]

04208850 80278xxx

### Mizuki [Ralf]

04208854 80278xxx

### Anko [Ralf]

04208858 80278xxx

### Jiraiya [Ralf]

0420885C 80278xxx

### Choji [Ralf]

04208860 80278xxx

### Tenten [Ralf]

04208864 80278xxx

### Temari [Ralf]

04208868 80278xxx

### Shino [Ralf]

0420886C 80278xxx

### Itachi [Ralf]

04208870 80278xxx

### Tsunade [Ralf]

04208874 80278xxx

### Hiruzen [Ralf]

04208878 80278xxx

### Kimimaro [Ralf]

0420887C 80278xxx

### Jirobo [Ralf]

04208880 80278xxx

### Kidomaru [Ralf]

04208884 80278xxx

### Sakon [Ralf]

04208888 80278xxx

### Tayuya [Ralf]

0420888C 80278xxx

### Kisame [Ralf]

04208890 80278xxx

### Sasuke CS2 [Ralf]

04208894 80278xxx

### Naruto Kyuubi [Ralf]

04208898 80278xxx

### Kabuto [Ralf]

0420889C 80278xxx

### Awakened Hinata [Ralf]

042088A0 80278xxx

### Tayuya's Doki Demon [Ralf]

042088A4 80278xxx

## Character Replacers

### Character Replacer (1 Character Version) [Ralf]

06004B54 00000014  
2C0500xx 40820008  
38A000yy 3C808020  
4E800020 00000000  
040400A8 4BFC4AAD  
0404032C 4BFC4829

xx/yy = Character IDs

Replaces Character xx with Character yy.

### Character Replacer (2 Characters Version) [Ralf]

06004B54 00000024  
2C0500vv 4082000C  
38A000ww 48000010  
2C0500xx 40820008  
38A000yy 3C808020  
4E800020 00000000  
040400A8 4BFC4AAD  
0404032C 4BFC4829

vv/ww = Character 1 IDs  
xx/yy = Character 2 IDs

Replaces Character vv with Character ww and Character xx with Character yy.

### Character Replacer (3 Characters Version) [Ralf]

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

06004B00 00000020  
2C0500xx 40820014  
38A00014 2C060001  
40820008 38C00000  
7C7A1B78 4E800020  
040400AC 4BFC4A55  
04040330 4BFC47D1

xx = Character ID

### Replace Character With Tayuya's Doki Demon [Ralf]

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

xx = Character ID

### Replace Akamaru With Karasu [Ralf]

06004B54 00000014  
2C050011 40820008  
38A0000F 3C808020  
4E800020 00000000  
040400A8 4BFC4AAD  
0404032C 4BFC4829

### Replace Naruto, Sasuke & Sakura With Hinata [Ralf]

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

### Replace Sakura With Oboro [Ralf]

06004B00 00000020  
2C050007 40820014  
38A00014 2C060001  
40820008 38C00000  
7C7A1B78 4E800020  
040400AC 4BFC4A55  
04040330 4BFC47D1

### Replace Ino With Tayuya's Doki Demon [Ralf]

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

## Gravity Adjustment

The Gecko codes for low gravity can easily be modified to use different gravity values. This is accomplished by adjusting the value following 0x140001E0. For example, the default set for the codes listed on this page is 0xBCF5C28F. That number is the hexadecimal representation of the float -0.03. The default gravity value of the game is 0xBDAA0000 (-0.083008). Gravity in this case represents the change in speed that occurs each frame of the game. Here are the results of using -0.03 for the gravity:

![Low Gravity](/gnt4/images/gameplay/low_gravity.gif?raw=true "Low Gravity")

Here is an example of using 0xBE23D70A (-0.16):

![High Gravity](/gnt4/images/gameplay/high_gravity.gif?raw=true "High Gravity")

As you can see, any float closer to zero than -0.083008 will be lower gravity and any float further from zero will be higher gravity.
