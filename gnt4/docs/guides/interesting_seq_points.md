# Interesting SEQ Points

## char_sel.seq

04F00: Where costume selection button inputs are processed

```
04F00 | and. *gpr4 + offset 0x28, 0x100 {04034400 00000028 3F000000 00000100}
04F10 | bnez 0xEC68 01340000 0000EC68 // A
04F18 | and. *gpr4 + offset 0x28, 0x800 {04034400 00000028 3F000000 00000800}
04F28 | bnez 0xEC98 01340000 0000EC98 // Y
04F30 | and. *gpr4 + offset 0x28, 0x400 {04034400 00000028 3F000000 00000400}
04F40 | bnez 0xECC8 01340000 0000ECC8 // X
04F48 | and. *gpr4 + offset 0x28, 0x10 {04034400 00000028 3F000000 00000010}
04F58 | bnez 0xED0C 01340000 0000ED0C // Z
04F60 | and. *gpr4 + offset 0x28, 0x200 {04034400 00000028 3F000000 00000200}
04F70 | bnez 0x5C70 01340000 00005C70 // B?
04F78 | blr 01450000
```

Note: Other buttons could be checked here. `R` is 0x20, `L` is 0x40, `Start` is 0x1000, `Control Stick` and `C-Stick` are also accessible in the top two bytes.

5708: Breaks here to offset 0x571c if extra costumes are being used

571C: Check if `chrId` is 7 or 9 (Sakura or Ino) where `chrId` is read at 0x571C.

EC68: Primary costume code.
EC98: Alt 1 costume code.
ECC8: Alt 2 costume code. Branches at 0xECD8 to 0xED50 if the 3rd costume exists. `chrId` is 7, 2, or 9 (Sakura, Haku, or Ino) where `chrId` is read at 0xECC8 from 0xF3E0.
ED0C: Alt 3 costume code. Branches at 0xED1C to 0xED80 if the 4th costume exists. `chrId` is 7, 2, or 9 (Sakura, Haku, or Ino) where `chrId` is read at 0xED0C from 0xF3E0.

EDB0: Primary costume code.
EDE0: Alt 1 costume code.
EE10: Alt 2 costume code. Branches at 0xECD8 to 0xEE20 if the 3rd costume exists. `chrId` is 7, 2, or 9 (Sakura, Haku, or Ino) where `chrId` is read at 0xEE10 from 0xF3E0.
EE54: Alt 3 costume code. Branches at 0xED1C to 0xEE64 if the 4th costume exists. `chrId` is 7, 2, or 9 (Sakura, Haku, or Ino) where `chrId` is read at 0xEE54 from 0xF3E0.

F3E0: Binary data, offset 0xB0 stores the character IDs in order on the CSS. Is read from at 0xECC8 and 

F530: Offset relating to a costume being chosen
