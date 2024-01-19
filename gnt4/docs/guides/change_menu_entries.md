# Changing Menu Entries

This page will explain how to change menu entries.

## Change Order of Main Menu Entries

The main menu is defined in [m_title.seq](https://gnt4.online/seq/m_title.html).

The order of these entries is stored in the seq file during runtime:

![Menu Entry Order](/gnt4/images/menus/menu_entry_order.png?raw=true "Menu Entry Order")

These values are set during runtime at [0x16DD0](https://gnt4.online/seq/m_title.html#16DD0).
The value stored is set a few lines prior at [0x16DB4](https://gnt4.online/seq/m_title.html#16DB4).
These entries are set from offsets taken from
[0x1C1C0](https://gnt4.online/seq/m_title.html#1C1C0).

Because of this, we can swap menu entries by adding new SEQ code to check for a specific menu entry
number and replace it with another. All of the submenu entries are unique numbers, so we can replace
them each without fear.

```seqedit
maki/m_title.seq

SeqEdit
Name:
  Swap 3MC with 1v1 in Battle Mode
Offset:
  0x16DD0
Position:
  0x49358
Old Bytes:
  0x3C1700000001C1607FFFFF247FFFFF23
New Bytes:
  0x3C1700000001C1607FFFFF247FFFFF233B020000000493A07FFFFF23000000093C0000000000000A7FFFFF233C1700000001C1607FFFFF247FFFFF233C000000000000097FFFFF233B020000000493D87FFFFF230000000A3C000000000000097FFFFF233C1700000001C1607FFFFF247FFFFF233C0000000000000A7FFFFF23
New Bytes with branch back:
  0x3C1700000001C1607FFFFF247FFFFF233B020000000493A07FFFFF23000000093C0000000000000A7FFFFF233C1700000001C1607FFFFF247FFFFF233C000000000000097FFFFF233B020000000493D87FFFFF230000000A3C000000000000097FFFFF233C1700000001C1607FFFFF247FFFFF233C0000000000000A7FFFFF230132000000016DE0
Assembly:
op_3C17 0x00, 0x00, 0x0001C160, 0x7FFFFF24, 0x7FFFFF23
op_3B02 0x00, 0x00, 0x000493A0, 0x7FFFFF23, 0x00000009
op_3C00 0x00, 0x00, 0x0000000A, 0x7FFFFF23
op_3C17 0x00, 0x00, 0x0001C160, 0x7FFFFF24, 0x7FFFFF23
op_3C00 0x00, 0x00, 0x00000009, 0x7FFFFF23
op_3B02 0x00, 0x00, 0x000493D8, 0x7FFFFF23, 0x0000000A
op_3C00 0x00, 0x00, 0x00000009, 0x7FFFFF23
op_3C17 0x00, 0x00, 0x0001C160, 0x7FFFFF24, 0x7FFFFF23
op_3C00 0x00, 0x00, 0x0000000A, 0x7FFFFF23
```
