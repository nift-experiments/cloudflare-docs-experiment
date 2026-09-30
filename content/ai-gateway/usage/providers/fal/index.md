<p><a href="https://fal.ai/">Fal AI</a> provides access to 600+ production-ready generative media models through a single, unified API. The service offers the world's largest collection of open image, video, voice, and audio generation models, all accessible with one line of code.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to Fal AI, replace <code>https://fal.run</code> in the URL you're currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Fal AI, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Fal AI API token.</li>
<li>The name of the Fal AI model you want to use.</li>
</ul>
<h2 id="default-synchronous-api">Default synchronous API</h2>
<p>By default, requests to the Fal AI endpoint will hit the synchronous API at <code>https://fal.run/&lt;path&gt;</code>.</p>
<h3 id="curl-example">cURL example</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal/fal-ai/fast-sdxl \&#10;  &#45;-header &#x27;Authorization: Key {fal_ai_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;prompt&quot;: &quot;Make an image of a cat flying an aeroplane&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="custom-target-urls">Custom target URLs</h2>
<p>If you need to hit a different target URL, you can supply the entire Fal target URL in the <code>x-fal-target-url</code> header.</p>
<h3 id="curl-example-with-custom-target-url">cURL example with custom target URL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal \&#10;  &#45;-header &#x27;Authorization: Bearer {fal_ai_token}&#x27; \&#10;  &#45;-header &#x27;x-fal-target-url: https://queue.fal.run/fal-ai/bytedance/seedream/v4/edit&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;prompt&quot;: &quot;Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.&quot;,&#10;    &quot;image_urls&quot;: [&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png&quot;,&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png&quot;,&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png&quot;,&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png&quot;&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h2 id="websocket-api">WebSocket API</h2>
<p>Fal AI also supports real-time interactions through WebSockets. For WebSocket connections and examples, see the <a href="/ai-gateway/usage/websockets-api/realtime-api/#fal-ai">Realtime WebSockets API documentation</a>.</p>
<h2 id="javascript-sdk-integration">JavaScript SDK integration</h2>
<p>The <code>x-fal-target-url</code> format is compliant with the Fal SDKs, so AI Gateway can be easily passed as a <code>proxyUrl</code> in the SDKs.</p>
<h3 id="javascript-sdk-example">JavaScript SDK example</h3>
<pre><code class="language-js">import { fal } from &quot;@fal-ai/client&quot;;&#10;&#10;fal.config({&#10;  credentials: &quot;{fal_ai_token}&quot;, // OR pass a cloudflare api token if using BYOK on AI Gateway&#10;  proxyUrl: &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal&quot;&#10;});&#10;&#10;const result = await fal.subscribe(&quot;fal-ai/bytedance/seedream/v4/edit&quot;, {&#10;  &quot;input&quot;: {&#10;    &quot;prompt&quot;: &quot;Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.&quot;,&#10;    &quot;image_urls&quot;: [&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png&quot;,&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png&quot;,&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png&quot;,&#10;      &quot;https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png&quot;&#10;    ]&#10;  }&#10;});&#10;&#10;console.log(result.data.images[0]);&#10;</code></pre>
