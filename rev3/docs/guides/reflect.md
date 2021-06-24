# Reflect

When a projectile is within reflect distance, the flag 0x2000 is set at 0x80080c8c. This appears to be set to `chr_p[0x15]`.

This is checked at instruction 0x80063784. This appears to be read from `chr_p[0x15]`.

The reflect action is set at instruction 0x8006387c.

The instruction at 0x8007f1bc seems to reset this flag every frame for each character.

## Codes

You can allow the ability to always reflect by using the follow gecko code:

```gecko
04063784 4800000c
```
