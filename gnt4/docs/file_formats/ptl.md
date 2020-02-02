# PTL Files

Used for particles.

## Particle Header

0x08 - Particle Count  
0x0C+ 4 * particle count  
    int offset for each particle  

Particle  
Types:

* Disc
* Line
* Tornado
* DiscCT
* DiscCD
* Rect
* Cone
* Cylinder
* Sphere

short Type: Sphere  
short TexGroup: 0  
short GenLife: 0  
short Life: 100  
int(flag) Kind:

* Gravity: On
* Fricxyz: On
* TornadoL Off
* Comtlut: Off
* Mirrors: off
* MirrorT: Off
* PrimNV: Off
* IMMRND: On
* TEXINTERP: NEAR
* EXECPAUSE: OFF
* PNTJOJBJ: Off
* PNTJOBJNO: 0
* FLIPS: OFF
* FLIPT: OFF
* TRAIL: OFF
* DIRVEC: OFF
* BLEND: ADD
* FOG: OFF
* PRIORITY: 4
* POINT: OFF
* LIGHTING: OFF
* BILLBOARDG: OFF
* BILLBOARDA: OFF

float Graivty: -0.001000  
float FRIC: 0.975000  
float VX: 1.7500000  
float VY: -0.01  
float VZ: 0  
float RADIUS: 0  
float ANGLE: 0.05236  
float RANDOM: 1.2  
float SIZE: 1  
float PARAM1: 0  
float PARAM2: 5  
float PARAM3: 0

Then some track data follows... not sure how to parse it, but it can do stuff like change colors

Thanks to Ploaj for the above information!
