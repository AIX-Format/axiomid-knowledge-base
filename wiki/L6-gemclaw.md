---
title: "GemClaw — Voice Services (L6)"
last_updated: "2026-05-16"
status: "stable"
tags: [voice, gemini, websocket, audio, agent-creation]
layer: "L6"
related:
  - "[[stack-overview]]"
  - "[[L2-iqra]]"
  - "[[architecture]]"
---

# GemClaw — Voice Services (L6)

> ~29,453 lines TS | Next.js 15 + Firebase

## الرئيسية 8 Flows

### Flow 1: Speech Recognition
```
User speaks → new SpeechRecognition()
→ recognition.start() → getUserMedia({audio:true})
→ getByteFrequencyData(dataArray) ← level analysis
→ setStreamingBuffer(transcript) ← Zustand store
```

### Flow 2: Gemini Live API Streaming
```
Browser ←→ WebSocket ←→ Gemini
→ new WebSocket(wsUrl) → ws.send(setupMsg)
→ audioWorklet.addModule(/audio-processor.js)
→ buffer[writePtr] = int16 ← SharedArrayBuffer
→ vad.MicVAD.new() ← Silero VAD
→ ws.send({realtimeInput: {audioChunk}}) ← stream to Gemini
```

### Flow 3: Audio Playback
```
Gemini → WebSocket → Browser
→ JSON.parse(data) → enqueueAudio(inlineData.data)
→ playAudio(chunk) → decode + play
→ audioContext.createBuffer(1, float32.length, 24000)
→ source.start() → flushAudioQueue() (barge-in)
```

### Flow 4: TTS Synthesis
```
Agent response → Speech
→ SynthesisEngine.speak(text)
→ speakBrowser(text) ← browser native TTS
→ new SpeechSynthesisUtterance(text)
→ voices.find(v => ...) ← select voice profile
→ window.speechSynthesis.speak(utterance)
```

### Flow 5: Voice Command Routing
```
Voice → Tool → Action
→ GEMINI_ROUTER_TOOLS ← tool definitions
→ dispatchToolCall(event) → queueRef.current.shift()
→ executeToolCall(event) → router.push(route)
→ store.setActiveAgentId(agentId)
```

### Flow 6: Conversation Flow — Aether Forge
```
Voice → Agent Creation (11-step)
→ VOICE_SELECTION → getStepDataUpdate(step, input)
→ create_agent ← neural-handler
→ setPendingManifest(manifest) ← AIX manifest
→ dispatchEvent(aether:genesis_triggered) ← agent born
```

### Flow 7: Visual Feedback
```
Mic Level → Orb Animation
→ useGemclawStore(s => s.micLevel)
→ targetScale = 1 + min(micLevel * 0.8, 0.4)
→ scaleSpring.set(targetScale) ← spring physics
→ getStatusColor() → borderColor: '#39FF14' if listening
```

### Flow 8: Voice Biometric
```
Speaker Verification
→ VoicePrint {id, embeddings: Float32Array}
→ neural embeddings ← speaker identity
→ BiometricAuthResult {verified, confidence, voicePrintId}
→ EnrollmentSession {voicePrintId, samples, isComplete}
```

## GemClaw Summary

| Component | Technology |
|-----------|-----------|
| Speech Recognition | Browser SpeechRecognition API |
| AI Voice | Gemini Live API (WebSocket 24kHz PCM) |
| Audio Processing | AudioWorklet + SharedArrayBuffer |
| VAD | Silero VAD (barge-in support) |
| TTS | Browser SpeechSynthesis |
| State | Zustand 5-slice store |
| Agent Creation | Aether Forge (11-step voice flow) |
| Visual | VoiceOrb with spring physics |
| Neural Router | /api/neural/router → Gemini/Claude/DeepSeek/OpenAI |
