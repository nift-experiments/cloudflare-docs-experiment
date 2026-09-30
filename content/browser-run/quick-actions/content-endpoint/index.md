<p>The <code>/content</code> endpoint instructs the browser to navigate to a website and capture the fully rendered HTML of a page, including the <code>head</code> section, after JavaScript execution. This is ideal for capturing content from JavaScript-heavy or interactive websites.</p>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/content&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Capture the fully rendered HTML of a dynamic page</li>
<li>Extract HTML for parsing, scraping, or downstream processing</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="fetch-rendered-html-from-a-url">Fetch rendered HTML from a URL</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3646.md")
</div></div>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3642.md")
</aside>
<h3 id="block-specific-resource-types">Block specific resource types</h3>
<p>Navigate to <code>https://cloudflare.com/</code> but block images and stylesheets from loading. Undesired requests can be blocked by resource type (<code>rejectResourceTypes</code>) or by using a regex pattern (<code>rejectRequestPattern</code>). The opposite can also be done, only allow requests that match <code>allowRequestPattern</code> or <code>allowResourceTypes</code>.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/content&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;      &quot;url&quot;: &quot;https://cloudflare.com/&quot;,&#10;      &quot;rejectResourceTypes&quot;: [&quot;image&quot;],&#10;      &quot;rejectRequestPattern&quot;: [&quot;/^.*\\.(css)&quot;]&#10;		}&#x27;&#10;</code></pre>
<p>Many more options exist, like setting HTTP headers using <code>setExtraHTTPHeaders</code>, setting <code>cookies</code>, and using <code>gotoOptions</code> to control page load behaviour - check the endpoint <a href="/api/resources/browser_rendering/subresources/content/methods/create/">reference</a> for all available parameters.</p>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3641.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
