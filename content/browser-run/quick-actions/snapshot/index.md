<p>Browser Run provides individual endpoints for <a href="/browser-run/quick-actions/content-endpoint/">HTML content</a>, <a href="/browser-run/quick-actions/screenshot-endpoint/">screenshots</a>, <a href="/browser-run/quick-actions/markdown-endpoint/">Markdown</a>, and more. The <code>/snapshot</code> endpoint combines multiple formats into a single request, so you do not need to call each endpoint separately. By default, it returns HTML content and a screenshot. You can use the <code>formats</code> parameter to customize which formats are included, such as adding Markdown and the accessibility tree to the response.</p>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/snapshot&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Capture both the rendered HTML and a visual screenshot in a single API call</li>
<li>Archive pages with visual and structural data together</li>
<li>Build monitoring tools that compare visual and DOM differences over time</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="capture-a-snapshot-from-a-url">Capture a snapshot from a URL</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3591.md")
</div></div>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3587.md")
</aside>
<h3 id="create-a-snapshot-from-custom-html">Create a snapshot from custom HTML</h3>
<p>This example uses the <code>html</code> property to render <code>&lt;html&gt;&lt;body&gt;Advanced Snapshot&lt;/body&gt;&lt;/html&gt;</code> and does the following:</p>
<ol>
<li>Disable JavaScript.</li>
<li>Sets the screenshot to <code>fullPage</code>.</li>
<li>Changes the page size <code>(viewport)</code>.</li>
<li>Waits up to <code>30000ms</code> or until the <code>DOMContentLoaded</code> event fires.</li>
<li>Returns the rendered HTML content and a base-64 encoded screenshot of the page.</li>
</ol>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/snapshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;&lt;html&gt;&lt;body&gt;Advanced Snapshot&lt;/body&gt;&lt;/html&gt;&quot;,&#10;    &quot;setJavaScriptEnabled&quot;: false,&#10;    &quot;screenshotOptions&quot;: {&#10;       &quot;fullPage&quot;: true&#10;    },&#10;    &quot;viewport&quot;: {&#10;      &quot;width&quot;: 1200,&#10;      &quot;height&quot;: 800&#10;    },&#10;    &quot;gotoOptions&quot;: {&#10;      &quot;waitUntil&quot;: &quot;domcontentloaded&quot;,&#10;      &quot;timeout&quot;: 30000&#10;    }&#10;  }&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;screenshot&quot;: &quot;Base64EncodedScreenshotString&quot;,&#10;		&quot;content&quot;: &quot;&lt;html&gt;&lt;body&gt;Advanced Snapshot&lt;/body&gt;&lt;/html&gt;&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="choose-which-formats-to-return">Choose which formats to return</h3>
<p>Use the <code>formats</code> parameter to control which representations of the page are included in the response. Accepted values are <code>&quot;content&quot;</code>, <code>&quot;screenshot&quot;</code>, <code>&quot;markdown&quot;</code>, and <code>&quot;accessibilityTree&quot;</code>. If omitted, the default is <code>[&quot;content&quot;, &quot;screenshot&quot;]</code>.</p>
<p>You must request at least two formats. If you only need a single format, use the corresponding single-format endpoint instead: <a href="/browser-run/quick-actions/content-endpoint/"><code>/content</code></a>, <a href="/browser-run/quick-actions/screenshot-endpoint/"><code>/screenshot</code></a>, <a href="/browser-run/quick-actions/markdown-endpoint/"><code>/markdown</code></a>, or <a href="/browser-run/quick-actions/accessibility-tree-endpoint/"><code>/accessibilityTree</code></a>.</p>
<p>The following example requests a screenshot, Markdown, and the accessibility tree in one call:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3595.md")
</div></div>
<h3 id="improve-blurry-screenshot-resolution">Improve blurry screenshot resolution</h3>
<p>If you set a large viewport width and height, your screenshot may appear blurry or pixelated. This can happen if your browser's default <code>deviceScaleFactor</code> (which defaults to 1) is not high enough for the viewport.</p>
<p>To fix this, increase the value of the <code>deviceScaleFactor</code>.</p>
<pre><code class="language-json">{&#10;  &quot;url&quot;: &quot;https://cloudflare.com/&quot;,&#10;  &quot;viewport&quot;: {&#10;    &quot;width&quot;: 3600,&#10;    &quot;height&quot;: 2400,&#10;    &quot;deviceScaleFactor&quot;: 2&#10;  }&#10;}&#10;</code></pre>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3586.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
