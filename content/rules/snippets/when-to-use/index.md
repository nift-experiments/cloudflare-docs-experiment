---
cp9:
  canonical: https://developers.cloudflare.com/rules/snippets/when-to-use/
  description: This guide helps you determine when to use Snippets or Workers on Cloudflare's global network.
  full_title: When to use Snippets vs Workers · Cloudflare Rules docs
  head_html: <title>When to use Snippets vs Workers · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="This guide helps you determine when to use Snippets or Workers on Cloudflare&#x27;s global network."><link rel="canonical" href="https://developers.cloudflare.com/rules/snippets/when-to-use/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/snippets/when-to-use/index.md"><meta property="og:title" content="When to use Snippets vs Workers · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This guide helps you determine when to use Snippets or Workers on Cloudflare&#x27;s global network."><meta property="og:url" content="https://developers.cloudflare.com/rules/snippets/when-to-use/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Design guide"><meta name="algolia_content_type" content="Design guide"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Request modification,Response modification,Middleware"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/snippets/when-to-use/#page","headline":"When to use Snippets vs Workers \u00b7 Cloudflare Rules docs","description":"This guide helps you determine when to use Snippets or Workers on Cloudflare's global network.","url":"https://developers.cloudflare.com/rules/snippets/when-to-use/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Request modification","Response modification","Middleware"]}</script>
  markdown: true
  noindex: false
  route: /rules/snippets/when-to-use/
  schema: 1
---
<p>This guide helps you determine when to use Snippets or Workers on Cloudflare's global network. It provides best practices, comparisons, and real-world use cases to help you choose the right product for your workload.</p>
<h2 id="what-are-snippets">What are Snippets?</h2>
<p>Cloudflare Snippets provide a fast, declarative way to modify HTTP requests and responses at the edge — without requiring a full-stack compute platform. Snippets extend <a href="/rules/">Cloudflare Rules</a> by allowing you to write JavaScript-based logic that modifies requests before they reach an origin and responses after they return from upstream.</p>
<p>Snippets enable you to:</p>
<ul>
<li>Modify headers, validate JWTs, and implement complex rewrites or redirects.</li>
<li>Retry failed requests to different origins and apply custom caching strategies.</li>
<li>Execute multiple Snippets sequentially, with each Snippet modifying the request or response before handing it off to the next.</li>
</ul>
<p>Snippets are included at no additional cost in <a href="/rules/snippets/#availability">all paid plans</a>, making them the preferred solution for lightweight edge logic.</p>
<h2 id="what-are-workers">What are Workers?</h2>
<p>By contrast, <a href="/workers/">Cloudflare Workers</a> provide a full-stack compute platform designed for applications requiring state, compute, and integrations with Cloudflare’s <a href="/learning-paths/workers/devplat/intro-to-devplat/">Developer Platform</a>. Workers operate on a <a href="/workers/platform/pricing/">usage-based pricing model</a> and include a free tier.</p>
<hr />
<h2 id="choosing-the-right-product">Choosing the right product</h2>
<p>Snippets are ideal for fast, cost-free request and response modifications at the edge. They extend <a href="/rules/">Cloudflare Rules</a> without requiring additional infrastructure or external solutions.</p>
<h3 id="when-to-use-snippets">When to use Snippets</h3>
<ul>
<li>Ultra-fast traffic modifications applied directly on Cloudflare's network.</li>
<li>Extend Cloudflare Rules beyond built-in actions for greater control.</li>
<li>Simplify CDN migrations by replacing VCL, EdgeWorkers, or on-premise logic.</li>
<li>Modify headers, cache responses, and perform redirects.</li>
<li>Integrate edge logic into development workflows using JavaScript.</li>
</ul>
<h3 id="what-snippets-are-not-designed-for">What Snippets are not designed for</h3>
<ul>
<li>Persistent state management (for example, session storage or databases).</li>
<li>Compute-intensive tasks (for example, image transformations or <a href="/workers-ai/">AI inference</a>).</li>
<li>Deep integrations with <a href="/learning-paths/workers/devplat/intro-to-devplat/">Developer Platform</a> services like <a href="/durable-objects/">Durable Objects</a> or <a href="/d1/">D1</a>.</li>
<li>Use cases requiring advanced runtime features, such as:
<ul>
<li><a href="/workers/configuration/environment-variables/">Environment variables</a></li>
<li><a href="/workers/observability/logs/">Observability</a></li>
<li><a href="/workers/runtime-apis/bindings/">Bindings</a></li>
<li><a href="/workers/configuration/cron-triggers/">Cron triggers</a></li>
<li>High <a href="/rules/snippets/#limits">compute limits</a></li>
</ul>
</li>
</ul>
<h3 id="key-features">Key features</h3>
<ul>
<li>Ultra-fast, edge-optimized execution, powered by <a href="/ruleset-engine/">Ruleset Engine</a> and <a href="/workers/runtime-apis/">Workers runtime</a>.</li>
<li>Included at no additional cost on <a href="/rules/snippets/#availability">all paid plans</a>.</li>
<li>Granular request matching using dozens of request attributes, such as <a href="/ruleset-engine/rules-language/fields/reference/http.request.full_uri/">URI</a>, <a href="/ruleset-engine/rules-language/fields/reference/http.user_agent/">user-agent</a>, and <a href="/ruleset-engine/rules-language/fields/reference/http.request.cookies/">cookies</a>.</li>
<li>Sequential execution – multiple Snippets <a href="/rules/snippets/how-it-works/">can run</a> on the same request, applying modifications step by step.</li>
<li>Native integration with <a href="/rules/">Cloudflare Rules</a> – Snippets inherit request modifications from other products running in earlier <a href="/ruleset-engine/reference/phases-list/#request-phases">request phases</a>.</li>
<li>JavaScript and Web APIs support, including:
<ul>
<li><a href="/workers/runtime-apis/fetch/">Fetch API</a></li>
<li><a href="/workers/runtime-apis/cache/">Cache API</a></li>
</ul>
</li>
<li>Essential <a href="/workers/runtime-apis/">Workers runtime</a> features, such as:
<ul>
<li><a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>request.cf</code> object</a></li>
<li><a href="/workers/runtime-apis/html-rewriter/"><code>HTMLRewriter</code></a></li>
</ul>
</li>
<li>Automated deployment and versioning via <a href="/rules/snippets/create-terraform/">Terraform</a>.</li>
</ul>
<hr />
<h2 id="snippets-vs-workers-feature-comparison">Snippets vs Workers: Feature comparison</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th align="center">Snippets</th>
<th align="center">Workers</th>
</tr>
</thead>
<tbody>
<tr>
<td>Execute scripts based on request attributes (for example, headers, geolocation, and cookies)</td>
<td align="center">✅</td>
<td align="center">❌</td>
</tr>
<tr>
<td>Execute code on a specific URL route</td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Modify HTTP requests/responses or serve a <a href="/rules/snippets/examples/maintenance/">different response</a></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="/rules/snippets/examples/hex-timestamp/">Add</a>, <a href="/rules/snippets/examples/remove-response-headers/">remove</a>, or <a href="/rules/snippets/examples/override-set-cookies-value/">rewrite</a> headers dynamically</td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="/rules/snippets/examples/custom-cache/">Cache</a> assets at the edge</td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Route traffic dynamically between <a href="/rules/snippets/examples/serve-different-origin/">origin servers</a></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="/rules/snippets/examples/auth-with-headers/">Authenticate</a> requests, <a href="/cache/interaction-cloudflare-products/waf-snippets/">pre-sign</a> URLs, run <a href="/rules/snippets/examples/ab-testing-same-url/">A/B testing</a></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Define logic using <a href="/workers/languages/javascript/">JavaScript and Web APIs</a></td>
<td align="center">✅</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Perform compute-heavy tasks (for example, <a href="/workers-ai/">AI</a>, <a href="/images/optimization/transformations/transform-via-workers/">image transformations</a>)</td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Store persistent data (for example, <a href="/kv/">KV</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/d1/">D1</a>)</td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Build <a href="/d1/tutorials/build-a-comments-api/">APIs</a> and <a href="/pages/framework-guides/deploy-an-astro-site/#video-tutorial">full-stack applications</a></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Use TypeScript, Python, Rust, or other programming <a href="/workers/languages/">languages</a></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Support non-HTTP <a href="/workers/reference/protocols/">protocols</a></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Analyze execution <a href="/workers/observability/logs/workers-logs/">logs</a> and track performance metrics</td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Deploy via <a href="/workers/wrangler/">command-line interface (CLI)</a></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Roll out gradually, roll back to previous <a href="/workers/versions-and-deployments/">versions</a></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
<tr>
<td>Optimize execution with <a href="/workers/configuration/placement/">Smart Placement</a></td>
<td align="center">❌</td>
<td align="center">✅</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="code-examples-common-snippets-templates">Code examples: Common Snippets templates</h2>
<p>Below are practical use cases demonstrating Snippets in action. You can find more templates to get started in the <a href="/rules/snippets/examples/">Examples</a> section.</p>
<h3 id="modify-http-headers">Modify HTTP headers</h3>
<p>Modifies request and response headers dynamically.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		// Get the current timestamp&#10;		const timestamp = Date.now();&#10;&#10;		// Convert the timestamp to hexadecimal format&#10;		const hexTimestamp = timestamp.toString(16);&#10;&#10;		// Clone the request and add the custom header with HEX timestamp&#10;		const modifiedRequest = new Request(request, {&#10;			headers: new Headers(request.headers),&#10;		});&#10;		modifiedRequest.headers.set(&quot;X-Hex-Timestamp&quot;, hexTimestamp);&#10;&#10;		// Pass the modified request to the origin&#10;		const response = await fetch(modifiedRequest);&#10;&#10;		// Clone the response so that it&#x27;s no longer immutable&#10;		const newResponse = new Response(response.body, response);&#10;&#10;		// Add a custom header with a value to the response&#10;		newResponse.headers.append(&#10;			&quot;x-snippets-hello&quot;,&#10;			&quot;Hello from Cloudflare Snippets&quot;,&#10;		);&#10;&#10;		// Delete headers from the response&#10;		newResponse.headers.delete(&quot;x-header-to-delete&quot;);&#10;		newResponse.headers.delete(&quot;x-header2-to-delete&quot;);&#10;&#10;		// Adjust the value for an existing header in the response&#10;		newResponse.headers.set(&quot;x-header-to-change&quot;, &quot;NewValue&quot;);&#10;&#10;		// Serve modified response to the visitor&#10;		return newResponse;&#10;	},&#10;};&#10;</code></pre>
<h3 id="serve-a-custom-maintenance-page">Serve a custom maintenance page</h3>
<p>Routes traffic to a maintenance page when your origin is undergoing a planned maintenance.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		return new Response(&#10;			`&#10;            &lt;!DOCTYPE html&gt;&#10;            &lt;html lang=&quot;en&quot;&gt;&#10;            &lt;head&gt;&#10;                &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;                &lt;title&gt;We&#x27;ll Be Right Back!&lt;/title&gt;&#10;                &lt;style&gt; body { font-family: Arial, sans-serif; text-align: center; padding: 20px; } &lt;/style&gt;&#10;            &lt;/head&gt;&#10;            &lt;body&gt;&#10;                &lt;h1&gt;We&#x27;ll Be Right Back!&lt;/h1&gt;&#10;                &lt;p&gt;Our site is undergoing maintenance. Check back soon!&lt;/p&gt;&#10;            &lt;/body&gt;&#10;            &lt;/html&gt;&#10;        `,&#10;			{ status: 503, headers: { &quot;Content-Type&quot;: &quot;text/html&quot; } },&#10;		);&#10;	},&#10;};&#10;</code></pre>
<h3 id="custom-cache">Custom cache</h3>
<p>Performs programmatic caching at the edge to reduce origin load.</p>
<pre tabindex="0"><code class="language-javascript">const CACHE_DURATION = 30 * 24 * 60 * 60; // 30 days&#10;&#10;export default {&#10;	async fetch(request) {&#10;		const cache = caches.default;&#10;		const cacheKey = new Request(request.url, { method: &quot;GET&quot; });&#10;&#10;		let response = await cache.match(cacheKey);&#10;		if (!response) {&#10;			response = await fetch(request);&#10;			response = new Response(response.body, response);&#10;			response.headers.set(&quot;Cache-Control&quot;, `s-maxage=${CACHE_DURATION}`);&#10;			await cache.put(cacheKey, response.clone());&#10;		}&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<h3 id="redirect-based-on-country-code">Redirect based on country code</h3>
<p>Redirects visitors based on their geographic location.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		const country = request.cf.country;&#10;		const redirectMap = {&#10;			US: &quot;https://example.com/us&quot;,&#10;			EU: &quot;https://example.com/eu&quot;,&#10;		};&#10;		if (redirectMap[country])&#10;			return Response.redirect(redirectMap[country], 301);&#10;		return fetch(request);&#10;	},&#10;};&#10;</code></pre>
<h3 id="redirect-403-forbidden-to-a-different-page">Redirect 403 Forbidden to a different page</h3>
<p>If the origin responded with <code>403 Forbidden</code> error code, redirects visitor to a different page.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		// Send original request to the origin&#10;		const response = await fetch(request);&#10;		// Check if origin responded with 403 status code&#10;		if (response.status == 403) {&#10;			// If so, redirect to this URL&#10;			const destinationURL = &quot;https://example.com&quot;;&#10;			// With this status code&#10;			const statusCode = 301;&#10;			// Serve redirect&#10;			return Response.redirect(destinationURL, statusCode);&#10;		}&#10;		// Otherwise, serve origin&#x27;s response&#10;		else {&#10;			return response;&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h3 id="retry-to-another-origin">Retry to another origin</h3>
<p>If the response to the original request is not <code>200 OK</code> or a redirect, sends to another origin.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		// Send original request to the origin&#10;		const response = await fetch(request);&#10;&#10;		// If response is not 200 OK or a redirect, send to another origin&#10;		if (!response.ok &amp;&amp; !response.redirected) {&#10;			// First, clone the original request to construct a new request&#10;			const newRequest = new Request(request);&#10;			// Add a header to identify a re-routed request at the new origin&#10;			newRequest.headers.set(&quot;X-Rerouted&quot;, &quot;1&quot;);&#10;			// Clone the original URL&#10;			const url = new URL(request.url);&#10;			// Send request to a different origin / hostname&#10;			url.hostname = &quot;example.com&quot;;&#10;			// Serve response to the new request from the origin&#10;			return await fetch(url, newRequest);&#10;		}&#10;&#10;		// If response is 200 OK or a redirect, serve it&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<h3 id="remove-fields-from-api-response">Remove fields from API response</h3>
<p>If the origin responds with JSON, deletes sensitive fields before returning a response to the visitor.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		// Send original request to the origin&#10;		const response = await fetch(request);&#10;		// Check if origin responded with JSON&#10;		try {&#10;			// Parse API response as JSON&#10;			var api_response = response.json();&#10;			// Specify the fields you want to delete. For example, to delete &quot;botManagement&quot; array from parsed JSON:&#10;			delete api_response.botManagement;&#10;			// Serve modified API response&#10;			return Response.json(api_response);&#10;		} catch (err) {&#10;			// On failure, serve unmodified origin&#x27;s response&#10;			return response;&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h3 id="set-cors-headers">Set CORS headers</h3>
<p>Adjusts <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS">Cross-Origin Resource Sharing (CORS)</a> headers and handles preflight requests.</p>
<pre tabindex="0"><code class="language-javascript">// Define CORS headers&#10;const corsHeaders = {&#10;	&quot;Access-Control-Allow-Origin&quot;: &quot;*&quot;, // Replace * with your allowed origin(s)&#10;	&quot;Access-Control-Allow-Methods&quot;: &quot;GET, POST, PUT, DELETE, OPTIONS&quot;, // Adjust allowed methods as needed&#10;	&quot;Access-Control-Allow-Headers&quot;: &quot;Content-Type, Authorization&quot;, // Adjust allowed headers as needed&#10;	&quot;Access-Control-Max-Age&quot;: &quot;86400&quot;, // Adjust max age (in seconds) as needed&#10;};&#10;&#10;export default {&#10;	async fetch(request) {&#10;		// Make a copy of the request to modify its headers&#10;		const modifiedRequest = new Request(request);&#10;&#10;		// Handle preflight requests (OPTIONS)&#10;		if (request.method === &quot;OPTIONS&quot;) {&#10;			return new Response(null, {&#10;				headers: {&#10;					...corsHeaders,&#10;				},&#10;				status: 200, // Respond with OK status for preflight requests&#10;			});&#10;		}&#10;&#10;		// Pass the modified request through to the origin&#10;		const response = await fetch(modifiedRequest);&#10;&#10;		// Make a copy of the response to modify its headers&#10;		const modifiedResponse = new Response(response.body, response);&#10;&#10;		// Set CORS headers on the response&#10;		Object.keys(corsHeaders).forEach((header) =&gt; {&#10;			modifiedResponse.headers.set(header, corsHeaders[header]);&#10;		});&#10;&#10;		return modifiedResponse;&#10;	},&#10;};&#10;</code></pre>
<h3 id="rewrite-links-on-html-pages">Rewrite links on HTML pages</h3>
<p>Replaces outdated links without having to make changes on your origin.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		// Define the old hostname here.&#10;		const OLD_URL = &quot;oldsite.com&quot;;&#10;		// Then add your new hostname that should replace the old one.&#10;		const NEW_URL = &quot;newsite.com&quot;;&#10;&#10;		class AttributeRewriter {&#10;			constructor(attributeName) {&#10;				this.attributeName = attributeName;&#10;			}&#10;			element(element) {&#10;				const attribute = element.getAttribute(this.attributeName);&#10;				if (attribute) {&#10;					element.setAttribute(&#10;						this.attributeName,&#10;						attribute.replace(OLD_URL, NEW_URL),&#10;					);&#10;				}&#10;			}&#10;		}&#10;&#10;		const rewriter = new HTMLRewriter()&#10;			.on(&quot;a&quot;, new AttributeRewriter(&quot;href&quot;))&#10;			.on(&quot;img&quot;, new AttributeRewriter(&quot;src&quot;));&#10;&#10;		const res = await fetch(request);&#10;		const contentType = res.headers.get(&quot;Content-Type&quot;);&#10;&#10;		// If the response is HTML, it can be transformed with&#10;		// HTMLRewriter -- otherwise, it should pass through&#10;		if (contentType.startsWith(&quot;text/html&quot;)) {&#10;			return rewriter.transform(res);&#10;		} else {&#10;			return res;&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h3 id="slow-down-requests">Slow down requests</h3>
<p>Defines a delay to be used when incoming requests match your rule. Useful for suspicious requests.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		// Define delay&#10;		const delay_in_seconds = 5;&#10;		// Introduce a delay&#10;		await new Promise((resolve) =&gt;&#10;			setTimeout(resolve, delay_in_seconds * 1000),&#10;		); // Set delay in milliseconds&#10;&#10;		// Pass the request to the origin&#10;		const response = await fetch(request);&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<hr />
<h2 id="using-snippets-and-workers-together">Using Snippets and Workers together</h2>
<p>While Snippets and Workers have distinct capabilities, they can work together to handle complex traffic workflows.</p>
<p>To avoid conflicts, Snippets and Workers should operate on separate request paths rather than running on the same URL. Have them fetch their respective URLs as a subrequest within their logic, ensuring smooth execution and caching behavior.</p>
<h3 id="example-1-passing-data-between-snippets-and-workers">Example 1: Passing data between Snippets and Workers</h3>
<p>Snippets can modify incoming requests before they reach a Worker, and Workers can read these modifications, perform additional transformations, and pass them downstream.</p>
<h4 id="snippet-add-a-custom-header">Snippet: Add a custom header</h4>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		// Get the current timestamp&#10;		const timestamp = Date.now();&#10;		const hexTimestamp = timestamp.toString(16);&#10;&#10;		// Clone request and add a custom header&#10;		const modifiedRequest = new Request(request, {&#10;			headers: new Headers(request.headers),&#10;		});&#10;		modifiedRequest.headers.set(&quot;X-Hex-Timestamp&quot;, hexTimestamp);&#10;&#10;		console.log(`X-Hex-Timestamp: ${hexTimestamp}`);&#10;&#10;		// Pass modified request to origin&#10;		return fetch(modifiedRequest);&#10;	},&#10;};&#10;</code></pre>
<h4 id="worker-read-a-header-and-add-it-to-the-response">Worker: Read a header and add it to the response</h4>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		const response = await fetch(&quot;https://{snippets_url}&quot;, request); // Ensure {snippets_url} points to the endpoint modified by Snippets&#10;		const newResponse = new Response(response.body, response);&#10;&#10;		let hexTimestamp = request.headers.get(&quot;X-Hex-Timestamp&quot;) || &quot;null&quot;;&#10;		console.log(hexTimestamp);&#10;&#10;		newResponse.headers.set(&quot;X-Hex-Timestamp&quot;, hexTimestamp);&#10;		return newResponse;&#10;	},&#10;};&#10;</code></pre>
<p><strong>Result:</strong> The Snippet sets <code>X-Hex-Timestamp</code>, which the Worker reads and forwards to the origin.</p>
<h3 id="example-2-caching-worker-responses-using-snippets">Example 2: Caching Worker responses using Snippets</h3>
<p>A Worker performs compute-heavy processing (for example, image transformation), while a Snippet serves cached results to avoid unnecessary Worker execution. This can be helpful in situations when running Workers <a href="/cache/interaction-cloudflare-products/workers/">before cache</a> is not desirable.</p>
<h4 id="worker-transform-and-cache-responses">Worker: Transform and cache responses</h4>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		const url = new URL(request.url);&#10;		url.hostname = &quot;origin.example.com&quot;; // Ensure this hostname points to the origin where the resource is hosted&#10;&#10;		const newRequest = new Request(url, request);&#10;		const customKey = `https://${url.hostname}${url.pathname}`; // This custom cache key should be the same in both Worker and Snippet configuration for cache to work&#10;&#10;		// Fetch and modify response&#10;		const response = await fetch(newRequest);&#10;		const newResponse = new Response(response.body, response);&#10;&#10;		// Cache the transformed response&#10;		const cache = caches.default;&#10;		const cachedResponse = newResponse.clone();&#10;		cachedResponse.headers.set(&quot;X-Cached-In-Workers&quot;, &quot;true&quot;);&#10;		await cache.put(customKey, cachedResponse);&#10;&#10;		newResponse.headers.set(&quot;X-Retrieved-From-Workers&quot;, &quot;true&quot;);&#10;		return newResponse;&#10;	},&#10;};&#10;</code></pre>
<h4 id="snippet-serve-cached-responses-or-forward-to-worker">Snippet: Serve cached responses or forward to Worker</h4>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request) {&#10;		const url = new URL(request.url);&#10;		url.hostname = &quot;origin.example.com&quot;; // Ensure this hostname points to the origin where the resource is hosted&#10;		const cacheKey = `https://${url.hostname}${url.pathname}`; // This custom cache key should be the same in both Worker and Snippet configuration for cache to work&#10;&#10;		// Access cache&#10;		const cache = caches.default;&#10;		let response = await cache.match(cacheKey);&#10;&#10;		if (!response) {&#10;			console.log(`Cache miss for: ${cacheKey}. Fetching from Worker...`);&#10;			url.hostname = &quot;worker.example.com&quot;; // Ensure this hostname points to the Workers route&#10;			response = await fetch(new Request(url, request));&#10;&#10;			// Cache the response for future use&#10;			response = new Response(response.body, response);&#10;			response.headers.set(&quot;Cache-Control&quot;, `s-maxage=3600`);&#10;			response.headers.set(&quot;x-snippets-cache&quot;, &quot;stored&quot;);&#10;		} else {&#10;			console.log(`Cache hit for: ${cacheKey}`);&#10;			response = new Response(response.body, response);&#10;			response.headers.set(&quot;x-snippets-cache&quot;, &quot;hit&quot;);&#10;		}&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<p><strong>Result:</strong> The transformed response (<code>X-Cached-In-Workers: true</code>) is served from cache, avoiding redundant Worker execution (<code>X-Retrieved-From-Workers</code> is not present). When cache expires, the Snippet fetches a fresh version.</p>
<hr />
<h2 id="migration-between-snippets-and-workers">Migration between Snippets and Workers</h2>
<p>Snippets and Workers share the same <a href="/workers/runtime-apis/">Workers runtime</a>, meaning JavaScript code that does not rely on bindings, persistent storage, or advanced execution features can be migrated seamlessly between them.</p>
<h3 id="when-to-migrate-workloads-to-snippets">When to migrate workloads to Snippets</h3>
<p>You should consider migrating a Worker to Snippets if it:</p>
<ul>
<li>Only modifies headers, redirects, caching rules, or origin routing.</li>
<li>Does not require bindings, persistent storage, or external integrations.</li>
<li>Is a lightweight JavaScript function with simple logic.</li>
<li>Needs to run an unlimited number of times for free on a Pro, Business, or Enterprise plan.</li>
</ul>
<p>Migrating to Snippets allows you to:</p>
<ul>
<li>Leverage advanced request matching via the <a href="/ruleset-engine/">Ruleset Engine</a>.</li>
<li>Eliminate usage-based billing — Snippets are <a href="/rules/snippets/#availability">included at no cost</a> on all paid plans.</li>
<li>Simplify management by integrating traffic modifications directly into Cloudflare Rules.</li>
</ul>
<h3 id="when-to-migrate-workloads-to-workers">When to migrate workloads to Workers</h3>
<p>You should migrate from Snippets to Workers if your logic:</p>
<ul>
<li>Exceeds execution time, memory, or other <a href="/rules/snippets/#limits">limits</a>.</li>
<li>Requires persistent state management, such as:
<ul>
<li><a href="/kv/">Key-Value (KV) storage</a></li>
<li><a href="/d1/">SQL databases (D1)</a></li>
<li><a href="/durable-objects/">Durable Objects</a></li>
</ul>
</li>
<li>Performs compute-intensive operations, including:
<ul>
<li><a href="/workers-ai/">AI inference</a></li>
<li><a href="/vectorize/">Vector search</a></li>
<li><a href="/images/optimization/transformations/transform-via-workers/">Image transformations</a></li>
</ul>
</li>
<li>Interacts with Cloudflare's <a href="/learning-paths/workers/devplat/intro-to-devplat/">Developer Platform</a>.</li>
<li>Requires <a href="/workers/testing/">unit testing</a>.</li>
<li>Needs deployment automation via CLI (<a href="/workers/wrangler/">Wrangler</a>).</li>
</ul>
<p>If your Snippet reaches the limits of execution time, memory, or functionality, transitioning to Workers ensures your logic can scale without restrictions.</p>
<hr />
<h2 id="conclusion">Conclusion</h2>
<p>Cloudflare Snippets provide a production-ready solution for fast, declarative edge traffic logic, bridging the gap between <a href="/rules/">Cloudflare Rules</a> and <a href="/learning-paths/workers/devplat/intro-to-devplat/">Developer Platform</a>.</p>
<p>Snippets and Workers solve different problems:</p>
<ul>
<li>Use Snippets for fast, lightweight traffic modifications at the edge, including header rewrites, caching, redirects, origin routing, custom responses, A/B testing and authentication.</li>
<li>Workers are built for advanced compute, persistent state, and full-stack applications.</li>
</ul>
