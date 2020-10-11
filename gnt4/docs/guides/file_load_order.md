# File Load Order

This page contains the order of when files are loaded into the game, to help understand when they are used.

## From launch to Pakkun loading screen

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     120 kB fpack/cmn0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     618 kB fpack/game3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:      22 kB fpack/game1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:   2,905 kB fpack/seq0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     353 kB fpack/chr/cmn0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     196 kB fpack/game0000.fpk
```

## First intro video

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:   4,442 kB movie/Tomy.h4m
```

## Second intro video

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     183 kB movie/8ing.h4m
```

## Third intro video

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:  42,349 kB movie/opening.h4m
```

## Title Screen

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:   6,384 kB fpack/game0001.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:      78 kB fpack/cmn0001.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     297 kB fpack/chr/sak1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     658 kB fpack/chr/sak3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     143 kB fpack/chr/sak0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:      10 kB fpack/game0100.fpk
```

## Main Menu

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:  13,828 kB audio/bgm/m000.trk
```

## Training Mode Character Select Screen

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:   2,502 kB fpack/game0007.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:  15,302 kB audio/bgm/m001.trk
```

## Hover Naruto in Character Select Screen

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0000.fpk
```

*Note: Other characters follow this same pattern.*

## Hover Alternate Color Naruto in Character Select Screen

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0100.fpk
```

*Note: Other characters follow this same pattern.*

## Versus Loading Screen

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:   1,018 kB fpack/game0006.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     294 kB audio/bgm/m002.trk
```

## Load Hot Spring Stage (Naruto vs Sasuke)

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     552 kB fpack/stg/0190000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     552 kB fpack/stg/0190000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     676 kB fpack/chr/nar3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     676 kB fpack/chr/nar3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     612 kB fpack/chr/sas3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     612 kB fpack/chr/sas3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:       5 kB fpack/chr/nar4000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:       5 kB fpack/chr/nar4000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     310 kB fpack/chr/sas1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     135 kB fpack/chr/sas0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:       5 kB fpack/chr/sas4000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:  14,188 kB audio/bgm/m058.trk
```

## Load Hot Spring Stage (Naruto vs Naruto Alternate Color)

```log
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     552 kB fpack/stg/0190000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     552 kB fpack/stg/0190000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     676 kB fpack/chr/nar3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     676 kB fpack/chr/nar3000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:       5 kB fpack/chr/nar4000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:       5 kB fpack/chr/nar4000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0100.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:       5 kB fpack/chr/nar4000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     392 kB fpack/chr/nar1000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:     133 kB fpack/chr/nar0100.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:       5 kB fpack/chr/nar4000.fpk
core\hw\dvd\filemonitor.cpp:83 W[FileMon]:  14,188 kB audio/bgm/m058.trk
```
