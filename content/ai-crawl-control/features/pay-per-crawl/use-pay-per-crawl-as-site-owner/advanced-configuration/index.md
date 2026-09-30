<h2 id="disable-pay-per-crawl-by-uri-pattern">Disable Pay Per Crawl by URI pattern</h2>
<p>You may want to offer free access to certain pages while charging for others:</p>
<ul>
<li>Allow free access to <strong>homepages, category pages, or navigation</strong> to help crawlers discover paid content.</li>
<li>Exclude functional pages like <strong>login, search, or API endpoints</strong> that don't contain chargeable content.</li>
<li>Start with Pay Per Crawl on <strong>a small section of your site</strong> before expanding.</li>
<li>Offer free access to <strong>promotional or archived content</strong> while charging for premium articles.</li>
</ul>
<p>To get started, use <a href="/rules/configuration-rules/">Configuration Rules</a> to exclude specific URI patterns from charging.</p>
<ol>
<li>Go to <strong>Rules</strong> &gt; <strong>Overview</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create rule</strong> &gt; <strong>Configuration Rule</strong>.</p>
</li>
<li>
<p><strong>When incoming requests match</strong>: Set your URI pattern.</p>
<ul>
<li>Field: <code>URI Full</code></li>
<li>Operator: <code>wildcard</code></li>
<li>Value: <code>https://*example.com/public/*</code></li>
</ul>
</li>
<li>
<p>Select <strong>Disable Pay Per Crawl</strong> &gt; <strong>Add</strong></p>
</li>
<li>
<p>Select <strong>Deploy</strong>.</p>
</li>
</ol>
<p><strong>Example patterns:</strong></p>
<ul>
<li>Free homepage: <code>URI Full</code> equals <code>https://example.com/</code></li>
<li>Free directory: <code>URI Full</code> wildcard <code>https://*example.com/public/*</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2768.md")
</aside>
<h2 id="dynamic-pricing">Dynamic pricing</h2>
<p>The price you specify in Pay Per Crawl settings applies to the entire zone by default, but you can implement a differentiated pricing policy by selecting <strong>Enable dynamic pricing</strong> and having your origin HTTP responses include a <code>crawler-price</code> header. For example:</p>
<pre><code class="language-http">crawler-price: USD 3.14&#10;</code></pre>
<p>When the <code>crawler-price</code> header is present in a response, the price it specifies will be used instead of the default price specified in the Pay Per Crawl settings for the zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2767.md")
</aside>
<h3 id="request-header-for-dynamic-pricing">Request header for dynamic pricing</h3>
<p>Pay Per Crawl adds a <code>cf-pay-per-crawl</code> header to every origin request. This header indicates the pricing mode in effect, and can be used by the origin to decide whether or not to include a <code>crawler-price</code> header with the response.</p>
<pre><code class="language-http">cf-pay-per-crawl: protocol=cloudflare, pricing=in-band&#10;</code></pre>
<p>Currently, the only possible value for the <code>protocol</code> indicator is <code>cloudflare</code>. For the <code>pricing</code> indicator the value can be one of the following:</p>
<ul>
<li><strong><code>zone-default</code></strong>: When the zone does not have in-band pricing enabled.</li>
<li><strong><code>in-band</code></strong>: When the zone has dynamic pricing enabled.</li>
<li><strong><code>bypass</code></strong>: When the request is not subject to payment (for example, not a bot).</li>
</ul>
<h3 id="use-workers-for-dynamic-pricing">Use Workers for dynamic pricing</h3>
<p>If you prefer to maintain your origin as is, you can use a Worker to include the <code>crawler-price</code> header in responses. From a Worker you can, for example, select the price based on the incoming request's properties (including information added by the Cloudflare global network) or the content itself.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="snippets-limitations">Snippets limitations</h3>
@markup("md", "content/.markup/bodies/2766.md")
</aside>
<p>The following Worker script implements a simple example policy that selects the price based on the requested URL path, while still taking advantage of Cloudflare Cache:</p>
<pre><code class="language-typescript">function getContentPriceUSD(request, response) {&#10;	const requestPath = new URL(request.url).pathname;&#10;&#10;	if (requestPath.startsWith(&quot;/premium-content/&quot;)) {&#10;		return 3.14;&#10;	}&#10;&#10;	if (requestPath.startsWith(&quot;/free-content/&quot;)) {&#10;		return 0.0;&#10;	}&#10;&#10;	return null; // Use the default price set in the zone configuration.&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Obtain the response first (and allow it to be cached if possible).&#10;		let response = await fetch(request, { cf: { cacheEverything: true } });&#10;&#10;		// Indicates the pricing mode in effect (&quot;bypass&quot;, &quot;zone-default&quot;, &quot;in-band&quot;).&#10;		const cfPayPerCrawl = request.headers.get(&quot;CF-Pay-Per-Crawl&quot;) || &quot;&quot;;&#10;&#10;		// If in-band pricing is enabled, use the request/response to select a price.&#10;		if (cfPayPerCrawl.match(/\bpricing=in-band\b/)) {&#10;			const contentPrice = getContentPriceUSD(request, response);&#10;&#10;			if (contentPrice !== null) {&#10;				// Make the response mutable, to allow setting the price header.&#10;				response = new Response(response.body, response);&#10;				response.headers.set(&quot;Crawler-Price&quot;, `USD ${contentPrice.toFixed(2)}`);&#10;			}&#10;		}&#10;		return response;&#10;	}&#10;};&#10;</code></pre>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li><a href="/rules/configuration-rules/">Configuration Rules documentation</a></li>
<li><a href="/workers/">Workers documentation</a></li>
</ul>
