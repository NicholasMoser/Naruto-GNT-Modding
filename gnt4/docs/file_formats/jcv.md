# JCV Files

## Format Information

JCV stands for Joint Connector Value. These files are part of the sysdolphin middleware and work in conjunction with .dat files to define parts of a model.

They are made of 2 parts, the bone table and the mesh table. They serve as an index of what is what, such as how the game knows bone 16 is the arm and so on. Tampering with these files without knowing what you're doing could result in animating the wrong bones or hiding the wrong meshes.

In later eighting games these files are merged into the actual model itself.

### Data Format

```
00 - Unknown usually 8
04 - 0
08 - Offset to table1
0C - Offset to table2

(Tables)
int16 - count
int16[count]
```

0. Root
1. Rot
2. Hip
3. Waist
4. Mid
5. Bust
6. Head
7. RBust
8. RShoulder
9. RArm
10. RHand
11. LBust
12. LShoulder
13. LArm
14. LHand
15. RHip
16. RLeg
17. RFoot
18. LHip
19. LLeg
20. LFoot
21. Neck
22. ?
23. ?
24. RKunai
25. RHandEffect
26. LKunai
27. LHandEffect
28. ?
29. ?
30. RBustAttachment
31. RShoulderAttachment
32. RArmAttachment
33. RArmAttachment2
34. RHandAttachment
35. LBustAttachment
36. LShoulderAttachment
37. LArmAttachment
38. LArmAttachment2
39. LHandAttachment
40. RHipAttachment
41. RLegAttachment
42. RLegAttachment2
43. RFootAttachment
44. ?
45. RFootAttachment
46. LHipAttachment
47. LLegAttachment
48. LLegAttachment2
49. LFootAttachment
50. ?
51. LRootAttachment
52. ?
53. ?
54. ?
55. ?
56. ?
57. ?
58. ?
59. ?
60. RThumb1
61. RThumb2
62. RThumb3
63. RIndex1
64. RIndex2
65. RIndex3
66. RMiddle1
67. RMiddle2
68. RMiddle3
69. RRing1
70. RRing2
71. RRing3
72. RPinky1
73. RPinky2
74. RPinky3
75. LThumb1
76. LThumb2
77. LThumb3
78. LIndex1
79. LIndex2
80. LIndex3
81. LMiddle1
82. LMiddle2
83. LMiddle3
84. LRing1
85. LRing2
86. LRing3
87. LPinky1
88. LPinky2
89. LPinky3
90. OboroOnly1
91. OboroOnly2
92. Nose
93. Mouth
94. RMouth
95. LMouth
96. ?
97. ?
98. ?
99. ?
100. InoBone
101. ?
102. Mouth2

## Credits

*Credit to Sifo and Ploaj for the information on this page*
