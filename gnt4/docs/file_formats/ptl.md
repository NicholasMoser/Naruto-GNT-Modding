# PTL Files

Used for particles. Can be edited with Struggleton's [HadalisCollider program](https://github.com/Struggleton/HadalisCollider).

## Particle Header

UInt16 ParticleType  
ParticleTypes:

* Disc = 0x00
* Line = 0x01
* Tornado = 0x02
* DiscCT = 0x03
* DiscCD = 0x04
* Rect = 0x05
* Cone = 0x06
* Cylinder = 0x07
* Sphere = 0x08

UInt16 TexGroup  
UInt16 GenLife //Amount of time in frames before particle is generated???  
UInt16 Life //Amount of time in frames particle lasts  
UInt32 Kind // Contains various parameters for the particle  
Kind bit fields:

* bit 1 - Gravy
* bit 2 - FricXYZ
* bit 3 - Tornado
* bit 4 - Nothing
* bit 5 - ComTLUT
* bit 6 - MirrorS
* bit 7 - MirrorT
* bit 8 - PrimEnv
* bit 9 - IMMRND
* bit 10, 11 - TexInterpolation
* bit 12 - ExecPause
* bit 13, 14, 15 - PNTJOBJNO
* bit 16 - PNTJOBJ
* bit 17 - BillboardG
* bit 18 - BillboardA
* bit 19 - FlipS
* bit 20 - FlipT
* bit 21 - Trail
* bit 22 - DirVec
* bit 23, 24 - Blend
* bit 25 - Fog
* bit 26 - Nothing
* bit 27 - Nothing
* bit 28 - Nothing
* bit 29 - Nothing
* bit 30 - Nothing
* bit 31 - Point
* bit 32 - Lighting

TexInterpolation Modes:

* Near = 0x00
* Linear = 0x01

Blending Modes:

* Normal = 0x00
* Add = 0x01
* Reserve = 0x02 / 0x03 // Not used in game

Float Gravity // Amount gravity affects the particle  
Float Friction // How well the particles can pass through each other??  
Vector3 VXYZ // ????

* float vx
* float vy
* float vz

Float Radius // Radius of how far particles go  
Float Angle // Angle at which particles are sent  
Float Random // Randomness of where particles travel???  
Float Size // Size of particles  
Float Param1 // ???  
Float Param2 // ???  
Float Param3 // ???  

byte[nextParticleOffset - currentOffset] TrackData // Contains data on stuff like how the particle is colored, etc

Thanks to Strugglton and Ploaj for information on this file type.
