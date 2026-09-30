<p>Content negotiation is the practice of serving different versions of a resource from a single URL, tailoring the experience to the end user. Common examples include delivering content in a specific language (<code>Accept-Language</code>), optimizing for a device (<code>User-Agent</code>), or serving modern image formats (<code>Accept</code>).</p>
<p>Cloudflare's global network is designed to handle this at scale. For common scenarios such as serving next-generation images, this negotiation is streamlined with a dedicated feature. For more customized logic, Cloudflare provides a toolkit including Transform Rules, Snippets, Custom Cache Keys, and Workers, giving you granular control to ensure the right content is served to every user, every time.</p>
<hr />
<h2 id="use-query-strings">Use query strings</h2>
<p>The <a href="/rules/transform/">Transform Rule</a> method is ideal when you can create a distinct URL, such as serving content based on a visitor's location.</p>
<h3 id="geolocation-example">Geolocation example</h3>
<p>In this example, you run an e-commerce site and want to display prices in the local currency based on the visitor's country.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> and select the option <strong>URL Rewrite Rule</strong>.</li>
<li>Enter a descriptive name, such as <code>Vary by Country - Canada</code>.</li>
<li>In <strong>If incoming requests match...</strong>, select <strong>Custom filter expression</strong>.</li>
<li>Under <strong>When incoming requests match...</strong>, create the following expression:
<ul>
<li><strong>Field:</strong> <code>Country</code></li>
<li><strong>Operator:</strong> <code>equals</code></li>
<li><strong>Value:</strong> <code>Canada</code></li>
</ul>
</li>
<li>Under <strong>Then...</strong>
<ul>
<li>for <strong>Path</strong>, select <strong>Preserve</strong>.</li>
<li>for <strong>Query</strong>, select <strong>Rewrite to</strong>: <strong>Dynamic</strong> <code>loc=ca</code></li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Now, requests from Canada to <code>/products/item</code> will be transformed to <code>/products/item?loc=ca</code> before reaching your origin or the cache, creating a distinct cache entry.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/3847.md")
</aside>
<hr />
<h2 id="vary-for-images">Vary for Images</h2>
<p><a href="/cache/advanced-configuration/vary-for-images/">Vary for Images</a> tells Cloudflare which variants your origin supports. Cloudflare then caches each version separately and serves the correct one to browsers without contacting your origin each time. This feature is managed via the Cloudflare API.</p>
<h3 id="enable-vary-for-images">Enable Vary for Images</h3>
<p>To enable this feature, create a <em>variants rule</em> using the API. This rule maps file extensions to the image formats your origin can serve.</p>
<p>For example, the following API call tells Cloudflare that for <code>.jpeg</code> and <code>.jpg</code> files, your origin can serve <code>image/webp</code> and <code>image/avif</code> variants:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cache/variants \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;value&quot;: {&#10;    &quot;jpeg&quot;: [&#10;      &quot;image/webp&quot;,&#10;      &quot;image/avif&quot;&#10;    ],&#10;    &quot;jpg&quot;: [&#10;      &quot;image/webp&quot;,&#10;      &quot;image/avif&quot;&#10;    ]&#10;  }&#10;}&#x27;</code></pre>
<p>After creating the rule, Cloudflare will create distinct cache entries for each image variant, improving performance for users with modern browsers.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability-1">Availability</h3>
@markup("md", "content/.markup/bodies/3846.md")
</aside>
<h2 id="use-snippets-for-programmatic-caching">Use Snippets for programmatic caching</h2>
<p><a href="/rules/snippets/">Snippets</a> are self-contained JavaScript fetch handlers that run at the edge on your requests through Cloudflare. They allow you to programmatically interact with the cache, providing full control over the cache key and response behavior without changing the user-facing URL.</p>
<h3 id="example-a-b-testing">Example: A/B testing</h3>
<p>In this example, you run an A/B test controlled by a cookie named <code>ab-test</code> (with values <code>group-a</code> or <code>group-b</code>). You want to cache a different version of the page for each group.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Snippets</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create new Snippet</strong> and name it <code>ab-test-caching</code>.</li>
<li>Paste the following code. It modifies the cache key based on the <code>ab-test</code> cookie and caches the response for 30 days.</li>
</ol>
<pre><code class="language-js">const CACHE_DURATION = 30 * 24 * 60 * 60; // 30 days&#10;&#10;export default {&#10;  async fetch(request) {&#10;    // Construct a new URL for the cache key based on the A/B cookie&#10;    const abCookie = request.headers.get(&#x27;Cookie&#x27;)?.match(/ab-test=([^;]+)/)?.[1] || &#x27;control&#x27;;&#10;    const url = new URL(request.url);&#10;    url.pathname = `/ab-test/${abCookie}${url.pathname}`;&#10;&#10;    const cacheKey = new Request(url, request);&#10;    const cache = caches.default;&#10;&#10;    let response = await cache.match(cacheKey);&#10;    if (!response) {&#10;      // If not in cache, fetch from origin&#10;      response = await fetch(request);&#10;      response = new Response(response.body, response);&#10;      response.headers.set(&quot;Cache-Control&quot;, `s-maxage=${CACHE_DURATION}`);&#10;      // Put the response into cache with the custom key&#10;      await cache.put(cacheKey, response.clone());&#10;    }&#10;    return response;&#10;  },&#10;};&#10;</code></pre>
<ol start="4">
<li>Save and deploy the Snippet.</li>
<li>From the Snippets dashboard, select <strong>Attach to routes</strong> to assign the Snippet.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability-2">Availability</h3>
@markup("md", "content/.markup/bodies/3845.md")
</aside>
<h2 id="custom-cache-keys-enterprise">Custom Cache Keys (Enterprise)</h2>
<p>If your account is on an Enterprise plan, the <a href="/cache/how-to/cache-keys">Custom Cache Keys</a> feature provides a no-code interface to define which request properties are included in the cache key.</p>
<p>Custom Cache Key options:</p>
<ul>
<li>Cache by device type</li>
<li>Query string option <code>No query string parameters except</code></li>
<li>Include headers and values</li>
<li>Include cookie names and values</li>
<li>User: Device type, Country, Language</li>
</ul>
<h3 id="example-same-url-different-content">Example: Same URL, different content</h3>
<p>If your origin serves different content types (for example, <code>application/json</code> vs. <code>text/html</code>) at the same URL based on the <code>Accept</code> header, use a custom cache key to cache them separately.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong>.</li>
<li>Enter  rule name, such as <code>Vary by Accept Header</code>.</li>
<li>Set the condition for the rule to apply (for example, a specific hostname or path).</li>
<li>Under <strong>Cache key</strong>, select <strong>Use custom key</strong>.</li>
<li>Select <strong>Add new</strong>.
<ul>
<li><strong>Type</strong>: <code>Header</code></li>
<li><strong>Name</strong>: <code>Accept</code></li>
<li><strong>Value</strong>: Add each <code>value</code>, or leave empty for all.</li>
</ul>
</li>
<li>Select <strong>Deploy</strong>.</li>
</ol>
<p>This configuration creates separate cache entries based on the <code>Accept</code> header value, respecting your API's content negotiation.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability-3">Availability</h3>
@markup("md", "content/.markup/bodies/3844.md")
</aside>
<h2 id="use-cloudflare-workers-for-advanced-logic">Use Cloudflare Workers for advanced logic</h2>
<p>For complex caching scenarios, <a href="/cache/interaction-cloudflare-products/workers/">Cloudflare Workers</a> provide a full serverless environment ideal for custom logic at scale.</p>
<h3 id="example-device-type-free-pro-biz-without-tiered-cache">Example: Device type – Free/Pro/Biz (without Tiered Cache)</h3>
<p>This Worker detects whether a visitor is on a mobile or desktop device and creates separate cache entries for each, ensuring the correct version of the site is served and cached.</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    const userAgent = request.headers.get(&#x27;User-Agent&#x27;) || &#x27;&#x27;;&#10;    const deviceType = userAgent.includes(&#x27;Mobile&#x27;) ? &#x27;mobile&#x27; : &#x27;desktop&#x27;;&#10;&#10;    // Create a new URL for the cache key that includes the device type&#10;    const url = new URL(request.url);&#10;    url.pathname = `/${deviceType}${url.pathname}`;&#10;&#10;    const cacheKey = new Request(url, request);&#10;    const cache = caches.default;&#10;&#10;    let response = await cache.match(cacheKey);&#10;&#10;    if (!response) {&#10;      console.log(`Cache miss for ${deviceType} device. Fetching from origin.`);&#10;      response = await fetch(request);&#10;      let responseToCache = response.clone();&#10;      ctx.waitUntil(cache.put(cacheKey, responseToCache));&#10;    }&#10;&#10;    return response;&#10;  },&#10;};&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability-4">Availability</h3>
@markup("md", "content/.markup/bodies/3843.md")
</aside>
<h3 id="example-device-type-enterprise-with-tiered-cache">Example: Device type – Enterprise (with Tiered Cache)</h3>
<p>This Worker detects if a visitor is on a mobile device or a desktop and creates a separate cache entry for each, ensuring the correct version of the site is served and cached. Uses the Enterprise <code>cf.customCacheKey</code> feature.</p>
<pre><code class="language-js">export default {&#10;  async fetch(request) {&#10;    // 1. Determine the device type from the User-Agent header&#10;    const userAgent = request.headers.get(&#x27;User-Agent&#x27;) || &#x27;&#x27;;&#10;    const deviceType = userAgent.includes(&#x27;Mobile&#x27;) ? &#x27;mobile&#x27; : &#x27;desktop&#x27;;&#10;&#10;    // 2. Create a custom cache key by appending the device type to the URL&#10;    const customCacheKey = `${request.url}-${deviceType}`;&#10;&#10;    // 3. Fetch the response. Cloudflare&#x27;s cache automatically uses the&#10;    //    customCacheKey for cache operations (match, put).&#10;    const response = await fetch(request, {&#10;      cf: {&#10;        cacheKey: customCacheKey,&#10;      },&#10;    });&#10;&#10;    // Optionally, you can modify the response before returning it&#10;    // For example, add a header to indicate which cache key was used&#10;    const newResponse = new Response(response.body, response);&#10;    newResponse.headers.set(&quot;X-Cache-Key&quot;, customCacheKey);&#10;    return newResponse;&#10;  },&#10;};&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability-5">Availability</h3>
@markup("md", "content/.markup/bodies/3842.md")
</aside>
<h2 id="example-caching-next-js-rsc-payloads">Example: Caching Next.js RSC payloads</h2>
<p>A common challenge is caching content from frameworks like Next.js, which uses an <code>RSC</code> (React Server Components) request header to differentiate between HTML page loads and RSC data payloads for the same URL. Here are the best ways to handle this.</p>
<h3 id="method-1-transform-rules">Method 1: Transform Rules</h3>
<p>The simplest solution is to create a <a href="/rules/transform/">Transform Rule</a> that checks for the <code>RSC</code> header and adds a unique query parameter on the request, creating two distinct cacheable URLs: <code>/page</code> (for HTML) and <code>/page?_rsc=1</code> (for the RSC payload).</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create rule</strong> and select the option <strong>URL Rewrite Rule</strong>.</p>
</li>
<li>
<p>Enter a name, such as <code>Vary by RSC Header</code>.</p>
</li>
<li>
<p>In <strong>If incoming requests match</strong>, select <strong>Custom filter expression</strong>.</p>
</li>
<li>
<p>Under <strong>When incoming requests match</strong>, manually edit the expression so that it checks for the presence of the <code>RSC</code> header:</p>
<ul>
<li><code>has_key(http.request.headers, &quot;rsc&quot;)</code></li>
</ul>
</li>
<li>
<p>Under <strong>Then</strong>:</p>
<ul>
<li>For <strong>Path</strong>, select <strong>Preserve</strong>.</li>
<li>For <strong>Query</strong>, select <strong>Rewrite to</strong>, select <strong>Static</strong>: <code>_rsc=1</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="method-2-snippets-or-custom-cache-keys">Method 2: Snippets or Custom Cache Keys</h3>
<p>Alternatively, use <a href="/rules/snippets/">Snippets</a> or <a href="/cache/how-to/cache-keys">Custom Cache Keys</a> to add the <code>RSC</code> header directly to the cache key without modifying the visible URL. This provides a cleaner URL but requires more advanced configuration.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability-6">Availability</h3>
@markup("md", "content/.markup/bodies/3841.md")
</aside>
