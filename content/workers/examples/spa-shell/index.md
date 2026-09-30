<p class="article-summary">Use HTMLRewriter to inject bootstrap data into an SPA shell — whether the shell is served from Workers Static Assets or fetched from an external origin.</p>
<p>This example uses a Worker and <a href="/workers/runtime-apis/html-rewriter/">HTMLRewriter</a> to inject prefetched API data into a single-page application (SPA) shell. The Worker fetches bootstrap data in parallel with the HTML shell and streams the result to the browser, so the SPA has everything it needs before its JavaScript runs.</p>
<p>Two variants are shown:</p>
<ol>
<li><strong>Static Assets</strong> — The SPA is deployed using <a href="/workers/static-assets/">Workers Static Assets</a></li>
<li><strong>External origin</strong> — The SPA is hosted outside Cloudflare, and the Worker sits in front of it as a reverse proxy, improving performance</li>
</ol>
<p>Both variants use the same HTMLRewriter injection technique and the same client-side consumption pattern. Choose the one that matches your deployment.</p>
<p>This pattern works with any SPA framework — React, Vue, Svelte, or others. For framework-specific deployment guides, refer to <a href="/workers/framework-guides/web-apps/">Web applications</a>.</p>
<hr />
<h2 id="option-1-single-page-app-spa-built-entirely-on-workers">Option 1: Single Page App (SPA) built entirely on Workers</h2>
<p>Use this variant when your SPA build output is deployed as part of your Worker using <a href="/workers/static-assets/">Static Assets</a>.</p>
<h3 id="configure-static-assets">Configure static assets</h3>
<p>Set <code>not_found_handling</code> to <code>&quot;single-page-application&quot;</code> so that every route returns <code>index.html</code>. Use <code>run_worker_first</code> to route all requests through your Worker except hashed assets under <code>/assets/*</code>, which are served directly.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16337.md")
</div>
<p>For more details on these options, refer to <a href="/workers/static-assets/routing/">Static Assets routing</a> and the <a href="/workers/static-assets/binding/#run_worker_first"><code>run_worker_first</code> reference</a>.</p>
<h3 id="inject-bootstrap-data-with-htmlrewriter">Inject bootstrap data with HTMLRewriter</h3>
<p>The Worker starts fetching API data immediately, then fetches the SPA shell from static assets. HTMLRewriter streams the <code>&lt;head&gt;</code> to the browser right away. When the <code>&lt;body&gt;</code> handler runs, it awaits the API response and prepends a <code>&lt;script&gt;</code> tag containing the serialized data.</p>
<p>If the API call fails, the shell still loads and the SPA falls back to client-side data fetching.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16338.md")
</div>
<hr />
<h2 id="option-2-spa-hosted-on-an-external-origin">Option 2: SPA hosted on an external origin</h2>
<p>Use this variant when your HTML, CSS, and JavaScript are deployed outside Cloudflare. The Worker fetches the SPA shell from the external origin, uses HTMLRewriter to inject bootstrap data, and streams the modified response to the browser.</p>
<h3 id="configure-the-worker">Configure the Worker</h3>
<p>Because the SPA is not in Workers Static Assets, you do not need an <code>assets</code> block. Instead, store the external origin URL as an environment variable. Attach the Worker to your domain with a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a> or a <a href="/workers/configuration/routing/routes/">Route</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16339.md")
</div>
<h3 id="inject-bootstrap-data-with-htmlrewriter-1">Inject bootstrap data with HTMLRewriter</h3>
<p>The Worker fetches both the SPA shell and API data in parallel. When the SPA origin responds, HTMLRewriter streams the HTML while injecting bootstrap data into <code>&lt;body&gt;</code>. Static assets (CSS, JS, images) are passed through to the external origin without modification.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16340.md")
</div>
<h2 id="consume-prefetched-data-in-your-spa">Consume prefetched data in your SPA</h2>
<p>On the client, read <code>window.__BOOTSTRAP_DATA__</code> before making any API calls. If the data exists, use it directly. Otherwise, fall back to a normal fetch.</p>
<pre><code class="language-tsx">// React example — works the same way in Vue, Svelte, or any other framework.&#10;import { useEffect, useState } from &quot;react&quot;;&#10;&#10;function App() {&#10;	const [data, setData] = useState(window.__BOOTSTRAP_DATA__ || null);&#10;	const [loading, setLoading] = useState(!data);&#10;&#10;	useEffect(() =&gt; {&#10;		if (data) return; // Already have prefetched data — skip the API call.&#10;&#10;		fetch(&quot;/api/bootstrap&quot;)&#10;			.then((res) =&gt; res.json())&#10;			.then((result) =&gt; {&#10;				setData(result);&#10;				setLoading(false);&#10;			});&#10;	}, []);&#10;&#10;	if (loading) return &lt;LoadingSpinner /&gt;;&#10;	return &lt;Dashboard data={data} /&gt;;&#10;}&#10;</code></pre>
<p>Add a type declaration so TypeScript recognizes the global property:</p>
<pre><code class="language-ts">declare global {&#10;	interface Window {&#10;		__BOOTSTRAP_DATA__?: unknown;&#10;	}&#10;}&#10;</code></pre>
<h2 id="additional-injection-techniques">Additional injection techniques</h2>
<p>You can chain multiple HTMLRewriter handlers to inject more than bootstrap data.</p>
<h3 id="set-meta-tags">Set meta tags</h3>
<p>Inject Open Graph or other <code>&lt;meta&gt;</code> tags based on the request path. This gives social-media crawlers correct previews without a full server-side rendering framework.</p>
<pre><code class="language-ts">new HTMLRewriter()&#10;	.on(&quot;head&quot;, {&#10;		element(el) {&#10;			el.append(`&lt;meta property=&quot;og:title&quot; content=&quot;${title}&quot; /&gt;`, {&#10;				html: true,&#10;			});&#10;		},&#10;	})&#10;	.transform(shell);&#10;</code></pre>
<h3 id="add-csp-nonces">Add CSP nonces</h3>
<p>Generate a nonce per request and inject it into both the Content-Security-Policy header and each inline <code>&lt;script&gt;</code> tag.</p>
<pre><code class="language-ts">const nonce = crypto.randomUUID();&#10;&#10;const response = new HTMLRewriter()&#10;	.on(&quot;script&quot;, {&#10;		element(el) {&#10;			el.setAttribute(&quot;nonce&quot;, nonce);&#10;		},&#10;	})&#10;	.transform(shell);&#10;&#10;response.headers.set(&#10;	&quot;Content-Security-Policy&quot;,&#10;	`script-src &#x27;nonce-${nonce}&#x27; &#x27;strict-dynamic&#x27;;`,&#10;);&#10;&#10;return response;&#10;</code></pre>
<h3 id="inject-user-configuration">Inject user configuration</h3>
<p>Expose feature flags or environment-specific settings to the SPA without an extra API round-trip.</p>
<pre><code class="language-ts">new HTMLRewriter()&#10;	.on(&quot;body&quot;, {&#10;		element(el) {&#10;			el.prepend(&#10;				`&lt;script&gt;window.__APP_CONFIG__=${JSON.stringify({&#10;					apiBase: env.API_BASE_URL,&#10;					featureFlags: { darkMode: true },&#10;				})}&lt;/script&gt;`,&#10;				{ html: true },&#10;			);&#10;		},&#10;	})&#10;	.transform(shell);&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/html-rewriter/">HTMLRewriter</a> — Streaming HTML parser and transformer.</li>
<li><a href="/workers/static-assets/">Workers Static Assets</a> — Serve static files alongside your Worker.</li>
<li><a href="/workers/static-assets/routing/">Static Assets routing</a> — Configure <code>run_worker_first</code> and <code>not_found_handling</code>.</li>
<li><a href="/workers/static-assets/binding/">Static Assets binding</a> — Reference for the <code>ASSETS</code> binding and routing options.</li>
<li><a href="/workers/configuration/routing/custom-domains/">Custom Domains</a> — Attach a Worker to a domain as the origin.</li>
<li><a href="/workers/configuration/routing/routes/">Routes</a> — Run a Worker in front of an existing origin server.</li>
<li><a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a> — Code patterns and configuration guidance for Workers.</li>
</ul>
