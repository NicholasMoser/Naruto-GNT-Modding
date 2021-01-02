# Sound

GNT4 uses MusyX for sound. The game calls the MusyX APIs at the following RAM addresses in the DOL:

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
  - This function tests if the given sound effect is currently processed by the sound system.
- sndFXCtrl
  - This function sets a new 7-bit controller value.
- sndFXKeyOff
  - This function sends a "KeyOff" to the sound effect with the specified voice ID. A "KeyOff" is used to signal the sound effect to go into its final phase. In most cases it will be used to stop the sound effect.
- sndFXStartPara
  - This function starts a sound effect and immediately sets some MIDI controller values. This call encapsulates a simple sound effect start and the setting of a number of MIDI controllers in one call. This not only simplifies the process, it avoids audible artifacts caused by the sound system and callback being issued before all MIDI controller values are set. Using multiple funciton calls can cause this problem.
- sndOutputMode
  - This function sets the system to mono, stereo, or surround.
- sndAuxCallbackUpdateSettingsReverbHI
  - This function is used to update the effect's parameters. Audible artifacts may occur while switching to the new setup.
- sndAuxCallbackPrepareReverbHI
  - This function is used to initialize all fields not easily filled in by the application in the SND_AUX_REVERBHI structure. it also will allocate buffer memory as necessary using the standard MusyX allocation callbacks.
- sndAuxCallbackPrepareDelay
  - This function is used to initialize all fields not easily filled in by the application in the SND_AUX_DELAY structure. it also will allocate buffer memory as necessary using the standard MusyX allocation callbacks.
- sndAuxCallbackReverbHI
  - This callback function is to be used together with sndSetAuxProcessingCallbacks(). It implements a reverb algorithm.
- sndAuxCallbackDelay
  - This callback function is to be used together with sndSetAuxProcessingCallbacks(). It implements a delay effect.
- sndSetAuxProcessingCallbacks
  - MusyX allows registering users effects handling to be registered with each studio context. All data passed through the Aux A and/or Aux B busses of the specified studio will be passed through whatever effect engine is implemented by the user defined callback functions specified. The effect in question may be a special type of reverb, distortion, or anything else that can be done to digital audio signals. The funcitons have to handle 3 channels (left, right, surround) of signed 32-bit audio (24-bits used) at 32KHz, 5ms data at a time.
- sndPopGroup
  - This function pops a group from the soundstack. Please ensure that no sounds from a group are actively playing when popping the group from the stack.
- sndPushGroup
  - This function pushes group data onto the soundstack.
