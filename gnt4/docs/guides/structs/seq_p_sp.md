# seq_p_sp

The code at instruction 0x800c90b4 seems to indicate that there may be multiple instances of `reg_p` stored in `seq_p_sp`. Each instance of `reg_p` is 0x60 bytes and starts at index 0x60 of `seq_p_sp`.

Each of these `reg_p` may have a `reg_p->stored_pc` which will then be executed. This seems to indicate that a SEQ file can have multiple dependent SEQ files waiting to execute code.

## 0x38 chr_p

## 0x60 reg_p
