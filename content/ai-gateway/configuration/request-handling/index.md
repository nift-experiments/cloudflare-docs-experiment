<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2851.md")
</aside>
<p>Your AI gateway supports different strategies for handling requests to providers, which allows you to manage AI interactions effectively and ensure your applications remain responsive and reliable.</p>
<h2 id="request-timeouts">Request timeouts</h2>
<p>A request timeout allows you to return an error or trigger a retry if a provider takes too long to respond.</p>
<p>These timeouts help:</p>
<ul>
<li>Improve user experience, by preventing users from waiting too long for a response</li>
<li>Proactively handle errors, by detecting unresponsive providers</li>
</ul>
<p>A timeout is set in milliseconds. The timeout is based on when the first part of the response comes back. As long as the first part of the response returns within the specified timeframe — such as when streaming a response — your gateway will wait for the response.</p>
<h3 id="configuration">Configuration</h3>
<p>For a provider-specific endpoint, configure the timeout value by adding a <code>cf-aig-request-timeout</code> header.</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;cf-aig-request-timeout: 5000&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]&#10;  }&#x27;&#10;</code></pre>
<hr />
<h2 id="request-retries">Request retries</h2>
<p>AI Gateway supports automatic retries for failed requests, with a maximum of five retry attempts.</p>
<p>This feature improves your application's resiliency, ensuring you can recover from temporary issues without manual intervention.</p>
<p>With request retries, you can adjust a combination of three properties:</p>
<ul>
<li>Number of attempts (maximum of 5 tries)</li>
<li>How long before retrying (in milliseconds, maximum of 60 seconds)</li>
<li>Backoff method (constant, linear, or exponential)</li>
</ul>
<p>On the final retry attempt, your gateway will wait until the request completes, regardless of how long it takes.</p>
<h3 id="configuration-1">Configuration</h3>
<p>For a provider-specific endpoint, configure the retry settings by adding different header values:</p>
<ul>
<li><code>cf-aig-max-attempts</code> (number)</li>
<li><code>cf-aig-retry-delay</code> (number)</li>
<li><code>cf-aig-backoff</code> (&quot;constant&quot; | &quot;linear&quot; | &quot;exponential)</li>
</ul>
