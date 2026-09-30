<p>RealtimeKit supports voice calls, allowing you to build audio-only experiences such as audio rooms, support lines, or community hangouts.
In these meetings, participants use their microphones and hear others, but cannot use their camera. Voice meetings reduce bandwidth requirements and focus on audio communication.</p>
<h2 id="how-audio-calls-work">How Audio Calls Work</h2>
<p>A participant’s meeting experience is determined by the <strong>Preset</strong> applied to that participant.
To run a voice meeting, ensure all participants join with a Preset that has meeting type set to <code>Voice</code>.</p>
<p>For details on Presets and how to configure them, refer to <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.</p>
<h2 id="pricing">Pricing</h2>
<p>When a participant joins with a <code>Voice</code> meeting type Preset, they are considered an <strong>Audio-Only Participant</strong> for billing. This is different from the billing for Audio/Video Participants.</p>
<p>For detailed pricing information, refer to <a href="/realtime/realtimekit/pricing/">Pricing</a>.</p>
<h2 id="building-audio-experiences">Building Audio Experiences</h2>
<p>You can build voice meeting experiences using either the UI Kit or the Core SDK.</p>
<h3 id="ui-kit">UI Kit</h3>
<p>UI Kit provides a pre-built meeting experience with customization options.</p>
<p>When participants join with a <code>Voice</code> meeting type Preset, UI Kit automatically renders a voice-only interface.
You can use the default meeting UI or build your own UI using UI Kit components.</p>
<p>To get started, refer to <a href="/realtime/realtimekit/ui-kit/">Build using UI Kit</a>.</p>
<h3 id="core-sdk">Core SDK</h3>
<p>Core SDK provides full control to build custom audio-only interfaces. Video-related APIs are non-functional for participants with <code>Voice</code> type Presets.</p>
<p>To get started, refer to <a href="/realtime/realtimekit/core/">Build using Core SDK</a>.</p>
