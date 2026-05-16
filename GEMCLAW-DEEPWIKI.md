# 🎙️ GemClaw: Voice Services — Audio Pipeline
> L6 Satellite · Voice · ~29,453 lines TS

## 🔄 الـ 8 Flows الرئيسية

### Flow 1: Speech Recognition (1a→1e)
```
User speaks
  → 1a: new SpeechRecognition() ← browser API
  → 1b: recognition.start() ← begin capture
  → 1c: getUserMedia({audio:true}) ← mic access
  → 1d: getByteFrequencyData(dataArray) ← level analysis
  → 1e: setStreamingBuffer(transcript) ← Zustand store
```

### Flow 2: Gemini Live API Streaming (2a→2f)
```
Browser ←→ WebSocket ←→ Gemini
  → 2a: new WebSocket(wsUrl) ← connect
  → 2b: ws.send(setupMsg) ← config
  → 2c: audioWorklet.addModule(/audio-processor.js) ← audio worklet
  → 2d: buffer[writePtr] = int16 ← SharedArrayBuffer
  → 2e: vad.MicVAD.new() ← Silero VAD (voice activity detection)
  → 2f: ws.send({realtimeInput: {audioChunk}}) ← stream to Gemini
```

### Flow 3: Audio Playback (3a→3f)
```
Gemini → WebSocket → Browser
  → 3a: JSON.parse(data) ← parse WS message
  → 3b: enqueueAudio(inlineData.data) ← queue PCM chunk
  → 3c: playAudio(chunk) ← decode + play
  → 3d: audioContext.createBuffer(1, float32.length, 24000)
  → 3e: source.start() ← play audio
  → 3f: flushAudioQueue() ← interrupt on user speech (barge-in)
```

### Flow 4: TTS Synthesis (4a→4f)
```
Agent response → Speech
  → 4a: transcript[last] ← detect new agent message
  → 4b: SynthesisEngine.speak(text) ← trigger
  → 4c: speakBrowser(text) ← browser native TTS
  → 4d: new SpeechSynthesisUtterance(text) ← utterance
  → 4e: voices.find(v => ...) ← select voice profile
  → 4f: window.speechSynthesis.speak(utterance)
```

### Flow 5: Voice Command Routing (5a→5f)
```
Voice → Tool → Action
  → 5a: GEMINI_ROUTER_TOOLS ← tool definitions
  → 5b: dispatchToolCall(event) ← dispatch
  → 5c: queueRef.current.shift() ← dequeue
  → 5d: executeToolCall(event) ← execute
  → 5e: router.push(route) ← navigate
  → 5f: store.setActiveAgentId(agentId) ← activate agent
```

### Flow 6: Conversation Flow (6a→6f)
```
Voice → Agent Creation
  → 6a: CONVERSATION_FLOW[step] ← flow definition
  → 6b: VOICE_SELECTION step ← choose voice
  → 6c: getStepDataUpdate(step, input) ← parse voice
  → 6d: create_agent ← neural-handler
  → 6e: setPendingManifest(manifest) ← AIX manifest
  → 6f: dispatchEvent(aether:genesis_triggered) ← agent born
```

### Flow 7: Visual Feedback (7a→7f)
```
Mic Level → Orb Animation
  → 7a: useGemclawStore(s => s.micLevel) ← subscribe
  → 7b: targetScale = 1 + min(micLevel * 0.8, 0.4) ← scale
  → 7c: scaleSpring.set(targetScale) ← spring physics
  → 7d: getStatusColor() ← listening/speaking/idle
  → 7e: scale: 1.0 + (micLevel * 0.4) ← animate glow
  → 7f: borderColor: '#39FF14' if listening ← neon green
```

### Flow 8: Voice Biometric (8a→8d)
```
Speaker Verification
  → 8a: VoicePrint {id, embeddings: Float32Array}
  → 8b: neural embeddings ← speaker identity
  → 8c: BiometricAuthResult {verified, confidence, voicePrintId}
  → 8d: EnrollmentSession {voicePrintId, samples, isComplete}
```

## 🎯 GemClaw Summary
| المكون | التقنية |
|--------|---------|
| Speech Recognition | Browser SpeechRecognition API |
| AI Voice | Gemini Live API (WebSocket 24kHz PCM) |
| Audio Processing | AudioWorklet + SharedArrayBuffer |
| VAD | Silero VAD (barge-in support) |
| TTS | Browser SpeechSynthesis |
| State | Zustand 5-slice store (Auth, Agent, Cognitive, Sensory, UI) |
| Agent Creation | Aether Forge (11-step voice flow) |
| Visual | VoiceOrb animated with spring physics |
| Neural Router | /api/neural/router → Gemini/Claude/DeepSeek/OpenAI |
