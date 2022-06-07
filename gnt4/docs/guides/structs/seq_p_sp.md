# seq\_p\_sp

The code at instruction 0x800c90b4 seems to indicate that there may be multiple instances of `reg_p` stored in `seq_p_sp`. Each instance of `reg_p` is 0x60 bytes and starts at index 0x60 of `seq_p_sp`.

Each of these `reg_p` may have a `reg_p->stored_pc` which will then be executed. This seems to indicate that a SEQ file can have multiple dependent SEQ files waiting to execute code.

## 0x14 trainingmode\_codepath
Pointer to the code path that lead to the training mode option branch [Set here in 0010.seq](https://nicholasmoser.github.io/iru_0010.html#64).
[Set here in 0000.seq](https://nicholasmoser.github.io/iru_0000.html#7CE4).

## 0x20 mot
Animation data

## 0x24 movement
Character movement data, takes data from seq\_p\_sp-\>field\_0x28
[Set here](https://nicholasmoser.github.io/iru_0000.html#81DC).

## 0x28
[Set here](https://nicholasmoser.github.io/iru_0000.html#81D4), [here](https://nicholasmoser.github.io/iru_0000.html#9704), [here](https://nicholasmoser.github.io/iru_0000.html#976C), [here](https://nicholasmoser.github.io/iru_0000.html#97D4)

## 0x38 chr\_p
Character information [Set here](https://nicholasmoser.github.io/iru_0000.html#7CC0).

## 0x3C foe\_chr\_p

## 0x4C
Struct where some data from 0000.seq is stored [example](https://nicholasmoser.github.io/iru_0000.html#9C0)

## 0x50
[Set here](https://nicholasmoser.github.io/iru_0000.html#7CCC)

## 0x54 seq\_file\_start

## 0x60 reg\_p
