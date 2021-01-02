# Sound

GNT4 uses MusyX for sound. The public calls to the MusyX API are at the following RAM addresses in the DOL:

- `800173A0` sndFXCheck
- `800173BC` sndFXCtrl
- `800173C4` sndFXKeyOff
- `8001742C` sndFXCheck
- `800CEC10` sndFXStartPara
- `800CEC5C` sndFXStartPara
- `800CECA8` sndFXStartPara
- `800CECF4` sndFXStartPara
- `800CFF08` sndOutputMode
- `800CFF1C` sndOutputMode
- `800D0190` sndAuxCallbackUpdateSettingsReverbHI
- `800D0254` sndAuxCallbackPrepareReverbHI
- `800D0260` sndAuxCallbackPrepareDelay
- `800D0268` sndAuxCallbackReverbHI
- `800D0270` sndAuxCallbackDelay
- `800D027C` sndAuxCallbackDelay
- `800D0280` sndAuxCallbackReverbHI
- `800D029C` sndSetAuxProcessingCallbacks
- `800D057C` sndFXStartPara
- `800D05C4` sndFXCheck
- `800D06A8` sndFXCheck
- `800D0740` sndPopGroup
- `800D0898` sndPushGroup

Therefore, the APIs that are actually called are:

- sndFXCheck
- sndFXCtrl
- sndFXKeyOff
- sndFXStartPara
- sndOutputMode
- sndAuxCallbackUpdateSettingsReverbHI
- sndAuxCallbackPrepareReverbHI
- sndAuxCallbackPrepareDelay
- sndAuxCallbackReverbHI
- sndAuxCallbackDelay
- sndSetAuxProcessingCallbacks
- sndPopGroup
- sndPushGroup
