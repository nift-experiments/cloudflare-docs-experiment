<p><a href="https://elevenlabs.io/">ElevenLabs</a> offers advanced text-to-speech services, enabling high-quality voice synthesis in multiple languages.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to ElevenLabs, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active ElevenLabs API token.</li>
<li>The model ID of the ElevenLabs voice model you want to use.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/elevenlabs/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128 \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;xi-api-key: {elevenlabs_api_token}&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;text&quot;: &quot;Welcome to Cloudflare - AI Gateway!&quot;,&#10;    &quot;model_id&quot;: &quot;eleven_multilingual_v2&quot;&#10;}&#x27;&#10;</code></pre>
