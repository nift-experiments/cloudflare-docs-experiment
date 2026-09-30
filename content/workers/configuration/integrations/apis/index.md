<p>To integrate with third party APIs from Cloudflare Workers, use the <a href="/workers/runtime-apis/fetch/">fetch API</a> to make HTTP requests to the API endpoint. Then use the response data to modify or manipulate your content as needed.</p>
<p>For example, if you want to integrate with a weather API, make a fetch request to the API endpoint and retrieve the current weather data. Then use this data to display the current weather conditions on your website.</p>
<p>To make the <code>fetch()</code> request, add the following code to your project's <code>src/index.js</code> file:</p>
<pre><code class="language-js">async function handleRequest(request) {&#10;	// Make the fetch request to the third party API endpoint&#10;	const response = await fetch(&quot;https://weather-api.com/endpoint&quot;, {&#10;		method: &quot;GET&quot;,&#10;		headers: {&#10;			&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;		},&#10;	});&#10;&#10;	// Retrieve the data from the response&#10;	const data = await response.json();&#10;&#10;	// Use the data to modify or manipulate your content as needed&#10;	return new Response(data);&#10;}&#10;</code></pre>
<h2 id="authentication">Authentication</h2>
<p>If your API requires authentication, use Wrangler secrets to securely store your credentials. To do this, create a secret in your Cloudflare Workers project using the following <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret</code></a> command:</p>
<pre><code class="language-sh">wrangler secret put SECRET_NAME&#10;</code></pre>
<p>Then, retrieve the secret value in your code using the following code snippet:</p>
<pre><code class="language-js">const secretValue = env.SECRET_NAME;&#10;</code></pre>
<p>Then use the secret value to authenticate with the external service. For example, if the external service requires an API key for authentication, include it in your request headers.</p>
<p>For services that require mTLS authentication, use <a href="/workers/runtime-apis/bindings/mtls">mTLS certificates</a> to present a client certificate.</p>
<h2 id="tips">Tips</h2>
<ul>
<li>
<p>Use the <a href="/workers/runtime-apis/cache/">Cache API</a> to cache data from the third party API. This allows you to optimize cacheable requests made to the API. Integrating with third party APIs from Cloudflare Workers adds additional functionality and features to your application.</p>
</li>
<li>
<p>Use <a href="/workers/configuration/routing/custom-domains/">Custom Domains</a> when communicating with external APIs, which treat your Worker as your core application.</p>
</li>
</ul>
