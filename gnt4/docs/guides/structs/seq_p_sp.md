# seq\_p\_sp

The code at instruction 0x800c90b4 seems to indicate that there may be multiple instances of `reg_p` stored in `seq_p_sp`. Each instance of `reg_p` is 0x60 bytes and starts at index 0x60 of `seq_p_sp`.

Each of these `reg_p` may have a `reg_p->stored_pc` which will then be executed. This seems to indicate that a SEQ file can have multiple dependent SEQ files waiting to execute code.

## 0x08
[Set here in 0000.seq](https://nicholasmoser.github.io/iru_0000.html#7CDC)
[Set here in 0010.seq](https://nicholasmoser.github.io/iru_0010.html#5C)

## 0x0C
[Set here in 0000.seq](https://nicholasmoser.github.io/iru_0000.html#84D4)
[Set here in 0010.seq](https://nicholasmoser.github.io/iru_0010.html#8C)

## 0x10
[Set here in 0000.seq](https://nicholasmoser.github.io/iru_0000.html#7CEC)
[Set here in 0010.seq](https://nicholasmoser.github.io/iru_0010.html#6C)

## 0x14 trainingmode\_codepath
Pointer to the code path that lead to the training mode option branch 
[Set here in 0010.seq](https://nicholasmoser.github.io/iru_0010.html#64).
[Set here in 0000.seq](https://nicholasmoser.github.io/iru_0000.html#7CE4).

## 0x18
[Set here in 0000.seq](https://nicholasmoser.github.io/iru_0000.html#84F8)
[Set here in 0010.seq](https://nicholasmoser.github.io/iru_0010.html#B0)

## 0x20 mot\_p
Animation data

## 0x24 movement\_p
Character movement data, takes data from seq\_p\_sp-\>field\_0x28
[Set here in 0000.seq](https://nicholasmoser.github.io/iru_0000.html#81DC).
[Set here in 0010.seq](https://nicholasmoser.github.io/iru_0010.html#40)

## 0x28
[Set here](https://nicholasmoser.github.io/iru_0000.html#81D4), [here](https://nicholasmoser.github.io/iru_0000.html#9704), [here](https://nicholasmoser.github.io/iru_0000.html#976C), [here](https://nicholasmoser.github.io/iru_0000.html#97D4)

## 0x38 chr\_p
Character information [Set here](https://nicholasmoser.github.io/iru_0000.html#7CC0).

## 0x3C foe\_chr\_p

## 0x40 cam\_p
Most likely this, used by op\_1A1B as is, and members of the struct are used for other functions. Used in the chr\_cam section of 0000.seq [here](https://nicholasmoser.github.io/iru_0000.html#154C)
[Set here](https://nicholasmoser.github.io/iru_0010.html#4C)

## 0x44
[Set here](https://nicholasmoser.github.io/iru_0000.html#7CC8)

## 0x4C
Struct where some data from 0000.seq is stored [example](https://nicholasmoser.github.io/iru_0000.html#9C0)

## 0x50
[Set here](https://nicholasmoser.github.io/iru_0000.html#7CCC)

## 0x54 seq\_file\_start

## 0x60 reg\_p
