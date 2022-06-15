# Recording

This page will document efforts to re-implement Bloody Roar's recording mode in GNT4.

## Recording Struct

| Offset | Type  | Name                     |
| ------ | ----- | ------------------------ |
| 0x0    | uint  | flags                    |
| 0x4    | int*  | action_sp                |
| 0x8    | uint  | total_actions            |
| 0xC    | short | frames_until_next_action |
| 0xE    | short | action                   |
| 0x10   | uint  | recording_index          |
| 0x14   | uint  | playback_index           |

- `flags` - Contains flags relating to the current state of this recording.
- `action_sp` - The stack pointer of actions for a recording.
- `total_actions` - The total number of actions.
- `frames_until_next_action` - The number of frames until the next action.
- `action` - The action.
- `recording_index` - The index in `action_sp` to write the next action.
- `playback_index` - The index in `action_sp` to read the next action.

Each int stored in `action_sp` is actually two short values concatenated, namely `frames_until_next_action` and `action`. In other words, the recording is a series of actions and how long to play that action. Specifically:

```c
action = recording->action_sp[recording->playback_index]
recording->frames_since_last_action = (short)(action >> 0x10);
recording->action = (short)action
```

## Recording Opcodes

Most of the recording opcodes have been documented in opcode group 26.

## Matching GNT4

The Bloody Roar checks for the recording menu options are at instructions 0x8004ceb4, 0x8004fcdc/0x8004fcf8, 0x8004dcf8.

In GNT4, `files/chr/iru/0010.seq` seems to have at offset 0x8C:

```seq
0008C | i32_andc seq_p_sp->field_0x0C, 0x200 04031B3F 00000200
00094 | bnez 0xF4E4 01340000 0000F4E4
```

which branches to 0x25C, which seems to have most of the recording opcodes.

It does appear that for situations such as recording being finished it reads from here:

```seq
0129C | op_3106 0xFFFF00FF 3106003F FFFF00FF
012A4 | op_3100 with text "RECORDING" 31000000 5245434F 5244494E 47000000
012B4 | op_3106 0xFF0000FF 3106003F FF0000FF
012BC | op_3100 with text " FINISHED" 31000000 2046494E 49534845 44000000
```

Recording state seems to be affected by `*seq_p_sp->field_0x24->field_0x26`, e.g.

```seq
0172C | i16_subc *seq_p_sp->field_0x24->field_0x26, 0x40000 06116100 00000026 3F000000 00040000
0173C | beqz 0x1600 01330000 00001600
01744 | i16_subc *seq_p_sp->field_0x24->field_0x26, 0x30000 06116100 00000026 3F000000 00030000
01754 | beqz 0x1790 01330000 00001790
0175C | i16_subc *seq_p_sp->field_0x24->field_0x26, 0x20000 06116100 00000026 3F000000 00020000
```

## Adding Recording

Recording support has now been added to GNT4 via this [GNTool PR](https://github.com/NicholasMoser/GNTool/pull/111).
