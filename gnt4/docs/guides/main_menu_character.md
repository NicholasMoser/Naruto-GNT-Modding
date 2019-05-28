# Main Menu Character

By default, the main menu character is Sakura. This can be replaced by modifying the four byte integer at offset 0x1612C in m_title.seq:

![Main Menu Character Location](/gnt4/images/functions/main_menu_character.png?raw=true "Main Menu Character Location")

## Values

Here are the values you can change it for each respective character.

| Integer | Character           |
|---------|---------------------|
| 0       | Common              |
| 1       | Sasuke              |
| 2       | Haku                |
| 3       | Kakashi             |
| 4       | Rock Lee            |
| 5       | Iruka               |
| 6       | Zabuza              |
| 7       | Sakura              |
| 8       | Naruto              |
| 9       | Ino                 |
| A       | Shikamaru           |
| B       | Neji                |
| C       | Hinata              |
| D       | Might Guy           |
| E       | Kankurō             |
| F       | Karasu (Puppet)     |
| 10      | Kiba                |
| 11      | Akamaru (Dog)       |
| 12      | Gaara               |
| 13      | Orochimaru          |
| 14      | Oboro               |
| 15      | Mizuki              |
| 16      | Anko                |
| 17      | Jiraiya             |
| 18      | Chōji               |
| 19      | Tenten              |
| 1A      | Temari              |
| 1B      | Shino               |
| 1C      | Itachi              |
| 1D      | Tsunade             |
| 1E      | Sarutobi (Third)    |
| 1F      | Kimimaro            |
| 20      | Jirōbō              |
| 21      | Kidōmaru            |
| 22      | Sakon               |
| 23      | Tayuya              |
| 24      | Kisame              |
| 25      | Sasuke CS2          |
| 26      | Kyūbi Naruto        |
| 27      | Kabuto              |
| 28      | Awakened Hinata     |
| 29      | Tayuya's Doki Demon |

## Broken Values

Here are the list of characters from above that when used will cause crashes upon selecting a game mode:

* Itachi
* Kabuto
* Kakashi
* Kankuro
* Kiba
* Kisame
* Kyūbi Naruto
* Orochimaru
* Rock Lee
* Sakon
* Sarutobi (Third)
* Tayuya
* Tsunade