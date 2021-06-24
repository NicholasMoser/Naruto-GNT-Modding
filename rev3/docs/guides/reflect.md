# Reflect

It appears that the most amount of projectiles allowed in the game at once time is 32. Obtacles, players, and puppets are not included in this count. Paper bombs are included.

When a projectile is within reflect distance, the flag 0x2000 is set at 0x80080c8c. This appears to be set to `chr_p[0x15]`. This instruction will not execute when a projectile is within reflect distance after the other player reflects.

This is checked at instruction 0x80063784. This appears to be read from `chr_p[0x15]`.

The reflect action is set at instruction 0x8006387c. This eventually is returned and set at instruction 0x80060a20, set to `chr_p[0x50]`.

The instruction at 0x8007f1bc seems to reset this flag every frame for each character.

## Codes

You can allow the ability to always reflect by using the follow gecko code:

```gecko
04063784 4800000c
```

A much cleaner way of implenting this is to nop the if checks at instruction 0x80080c8c. This prevents you from always being able to reflect, but still has the issue of not spawning a second projectile on the second reflect.

```gecko
04080c58 60000000
04080c64 60000000
```
