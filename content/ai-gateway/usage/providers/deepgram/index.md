<p><a href="https://developers.deepgram.com/home">Deepgram</a> provides Voice AI APIs for speech-to-text, text-to-speech, and voice agents.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2980.md")
</aside>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram&#10;</code></pre>
<h2 id="url-structure">URL Structure</h2>
<p>When making requests to Deepgram, replace <code>https://api.deepgram.com/</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Deepgram, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Deepgram API token.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="sdk">SDK</h3>
<pre><code class="language-ts">import { createClient, LiveTranscriptionEvents } from &quot;@deepgram/sdk&quot;;&#10;&#10;&#10;const deepgram = createClient(&quot;{deepgram_api_key}&quot;, {&#10;    global: {&#10;      websocket: {&#10;        options: {&#10;          url: &quot;wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/&quot;,&#10;          _nodeOnlyHeaders: {&#10;            &quot;cf-aig-authorization&quot;: &quot;Bearer {CF_AIG_TOKEN}&quot;&#10;          }&#10;        }&#10;      }&#10;    }&#10;});&#10;&#10;&#10;const connection = deepgram.listen.live({&#10;    model: &quot;nova-3&quot;,&#10;    language: &quot;en-US&quot;,&#10;    smart_format: true,&#10;});&#10;&#10;connection.send(...);&#10;</code></pre>
