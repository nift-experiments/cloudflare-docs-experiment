<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="flux">flux</h1>

<p><code>@cf/deepgram/flux</code></p>

Flux is the first conversational speech recognition model built specifically for voice agents.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Automatic Speech Recognition</td></tr>
<tr><th>Terms</th><td><a href="https://deepgram.com/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>USD 0.0077 per audio minute (websocket)</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/deepgram/flux&quot;, { automatic_speech_recognition: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/deepgram/flux -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>encoding</code></td><td>string</td><td>Encoding of the audio stream. Currently only supports raw signed little-endian 16-bit PCM. Values: linear16</td></tr><tr><td><code>sample_rate</code></td><td>string</td><td>Sample rate of the audio stream in Hz.</td></tr><tr><td><code>eager_eot_threshold</code></td><td>string</td><td>End-of-turn confidence required to fire an eager end-of-turn event. When set, enables EagerEndOfTurn and TurnResumed events. Valid Values 0.3 - 0.9.</td></tr><tr><td><code>eot_threshold</code></td><td>string</td><td>End-of-turn confidence required to finish a turn. Valid Values 0.5 - 0.9. Default: 0.7</td></tr><tr><td><code>eot_timeout_ms</code></td><td>string</td><td>A turn will be finished when this much time has passed after speech, regardless of EOT confidence. Default: 5000</td></tr><tr><td><code>keyterm</code></td><td>string</td><td>Keyterm prompting can improve recognition of specialized terminology. Pass multiple keyterm query parameters to boost multiple keyterms.</td></tr><tr><td><code>mip_opt_out</code></td><td>string</td><td>Opts out requests from the Deepgram Model Improvement Program. Refer to Deepgram Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip Default: false; Values: true, false</td></tr><tr><td><code>tag</code></td><td>string</td><td>Label your requests for the purpose of identification during usage reporting</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>request_id</code></td><td>string</td><td>The unique identifier of the request (uuid)</td></tr><tr><td><code>sequence_id</code></td><td>integer</td><td>Starts at 0 and increments for each message the server sends to the client. Minimum: 0</td></tr><tr><td><code>event</code></td><td>string</td><td>The type of event being reported. Values: Update, StartOfTurn, EagerEndOfTurn, TurnResumed, EndOfTurn</td></tr><tr><td><code>turn_index</code></td><td>integer</td><td>The index of the current turn Minimum: 0</td></tr><tr><td><code>audio_window_start</code></td><td>number</td><td>Start time in seconds of the audio range that was transcribed</td></tr><tr><td><code>audio_window_end</code></td><td>number</td><td>End time in seconds of the audio range that was transcribed</td></tr><tr><td><code>transcript</code></td><td>string</td><td>Text that was said over the course of the current turn</td></tr><tr><td><code>words</code></td><td>array</td><td>The words in the transcript</td></tr><tr><td><code>words[].word</code></td><td>string</td><td>Required. The individual punctuated, properly-cased word from the transcript</td></tr><tr><td><code>words[].confidence</code></td><td>number</td><td>Required. Confidence that this word was transcribed correctly</td></tr><tr><td><code>end_of_turn_confidence</code></td><td>number</td><td>Confidence that no more speech is coming in this turn</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/flux/schema-input.json)
- [Output schema](/workers-ai/models/flux/schema-output.json)

