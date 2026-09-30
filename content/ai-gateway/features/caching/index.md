<p>When caching is enabled, AI Gateway can cache responses from your AI model providers, serving them directly from Cloudflare's cache for identical requests.</p>
<h2 id="benefits-of-using-caching">Benefits of Using Caching</h2>
<ul>
<li><strong>Reduced Latency:</strong> Serve responses faster to your users by avoiding a round trip to the origin AI provider for repeated requests.</li>
<li><strong>Cost Savings:</strong> Minimize the number of paid requests made to your AI provider, especially for frequently accessed or non-dynamic content.</li>
<li><strong>Increased Throughput:</strong> Offload repetitive requests from your AI provider, allowing it to handle unique requests more efficiently.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2841.md")
</aside>
<h2 id="default-configuration">Default configuration</h2>
<p>Caching is disabled by default. To enable caching globally, set the default caching configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2844.md")
</div></div>
<p>When caching is enabled globally, the default caching behavior applies to all requests that support caching. You can also opt individual requests into caching or override their cache settings with per-request headers.</p>
<p>To check whether a response comes from cache or not, <strong>cf-aig-cache-status</strong> will be designated as <code>HIT</code> or <code>MISS</code>.</p>
<h2 id="how-the-cache-key-works">How the cache key works</h2>
<p>By default, AI Gateway constructs the cache key by concatenating the following and hashing the result with SHA-256:</p>
<ul>
<li><strong>Provider</strong> (for example, <code>openai</code>, <code>anthropic</code>)</li>
<li><strong>Endpoint</strong> (the API path)</li>
<li><strong>Model</strong> (for example, <code>gpt-4o</code>)</li>
<li><strong>Provider authentication header</strong> (for example, the <code>Authorization</code> bearer token)</li>
<li><strong>Full request body</strong></li>
</ul>
<p>This means caching is based on <strong>exact match</strong> of the entire request. Any difference in the body — including messages, tools, or model parameters — will result in a separate cache entry. To override this behavior, use the <a href="#custom-cache-key-cf-aig-cache-key">custom cache key header</a>.</p>
<h2 id="per-request-caching">Per-request caching</h2>
<p>While your gateway's default cache settings provide a good baseline, you might need more granular control. These situations could include data freshness, content with varying lifespans, or dynamic or personalized responses.</p>
<p>To address these needs, AI Gateway allows you to override default cache behaviors on a per-request basis using specific HTTP headers. This gives you the precision to optimize caching for individual API calls.</p>
<p>The following headers allow you to define this per-request cache behavior:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2840.md")
</aside>
<h3 id="skip-cache-cf-aig-skip-cache">Skip cache (cf-aig-skip-cache)</h3>
<p>Skip cache refers to bypassing the cache and fetching the request directly from the original provider, without utilizing any cached copy.</p>
<p>You can use the header <strong>cf-aig-skip-cache</strong> to bypass the cached version of the request.</p>
<p>As an example, when submitting a request to OpenAI, include the header in the following manner:</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;cf-aig-skip-cache: true&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;how to build a wooden spoon in 3 short steps? give as short as answer as possible&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="cache-ttl-cf-aig-cache-ttl">Cache TTL (cf-aig-cache-ttl)</h3>
<p>Cache TTL, or Time To Live, is the duration a cached request remains valid before it expires and is refreshed from the original source. Use <code>cf-aig-cache-ttl</code> to set the caching duration for a request that already uses caching. To opt an individual request into caching, include <code>cf-aig-cache-key</code>. The minimum TTL is 60 seconds and the maximum TTL is one month.</p>
<p>For example, if you set a TTL of one hour, it means that a request is kept in the cache for an hour. Within that hour, an identical request will be served from the cache instead of the original API. After an hour, the cache expires and the request will go to the original API for a fresh response, and that response will repopulate the cache for the next hour.</p>
<p>As an example, when submitting a request to OpenAI, include the header in the following manner:</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;&#35; Use a key shared only by requests with equivalent responses.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;cf-aig-cache-key: responseWithCustomTtl&quot; \&#10;  &#45;-header &quot;cf-aig-cache-ttl: 3600&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;how to build a wooden spoon in 3 short steps? give as short as answer as possible&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="custom-cache-key-cf-aig-cache-key">Custom cache key (cf-aig-cache-key)</h3>
<p>The <code>cf-aig-cache-key</code> header lets you override the default cache key and opts the request into caching.</p>
<p>Choose a custom key that groups only requests with equivalent responses. Requests with the same custom key share a cached response. When you use the <code>cf-aig-cache-key</code> header for the first time, you will receive a response from the provider. Subsequent requests with the same custom key value will return the cached response. If you include <code>cf-aig-cache-ttl</code>, the request uses that value for its cache TTL. Otherwise, the request uses the default cache TTL configured for the gateway. For requests that include <code>cf-aig-cache-key</code>, the cache TTL is 5 minutes when neither <code>cf-aig-cache-ttl</code> nor a default gateway cache TTL is configured.</p>
<p>As an example, when submitting a request to OpenAI, include the header in the following manner:</p>
<pre><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-header &quot;cf-aig-cache-key: responseA&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;how to build a wooden spoon in 3 short steps? give as short as answer as possible&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="ai-gateway-caching-behavior">AI Gateway caching behavior</h3>
@markup("md", "content/.markup/bodies/2839.md")
</aside>
