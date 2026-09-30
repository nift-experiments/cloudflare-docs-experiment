<p><a href="https://docs.cartesia.ai/">Cartesia</a> provides advanced text-to-speech services with customizable voice models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia&#10;</code></pre>
<h2 id="url-structure">URL Structure</h2>
<p>When making requests to Cartesia, replace <code>https://api.cartesia.ai/v1</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Cartesia, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Cartesia API token.</li>
<li>The model ID and voice ID for the Cartesia voice model you want to use.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia/tts/bytes \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;Cartesia-Version: 2024-06-10&#x27; \&#10;  &#45;-header &#x27;X-API-Key: {cartesia_api_token}&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;transcript&quot;: &quot;Welcome to Cloudflare - AI Gateway!&quot;,&#10;    &quot;model_id&quot;: &quot;sonic-english&quot;,&#10;    &quot;voice&quot;: {&#10;        &quot;mode&quot;: &quot;id&quot;,&#10;        &quot;id&quot;: &quot;694f9389-aac1-45b6-b726-9d9369183238&quot;&#10;    },&#10;    &quot;output_format&quot;: {&#10;        &quot;container&quot;: &quot;wav&quot;,&#10;        &quot;encoding&quot;: &quot;pcm_f32le&quot;,&#10;        &quot;sample_rate&quot;: 44100&#10;    }&#10;}&#10;</code></pre>
