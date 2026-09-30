<p>The <code>/markdown</code> endpoint retrieves a webpage's content and converts it into Markdown format. You can specify a URL and optional parameters to refine the extraction process.</p>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Normalize content for downstream processing (summaries, diffs, embeddings)</li>
<li>Save articles or docs for editing or storage</li>
<li>Strip styling/scripts and keep readable content + links</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="convert-a-url-to-markdown">Convert a URL to Markdown</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3621.md")
</div></div>
<h3 id="convert-raw-html-to-markdown">Convert raw HTML to Markdown</h3>
<p>Instead of fetching the content by specifying the URL, you can provide raw HTML content directly.</p>
<pre><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;&lt;div&gt;Hello World&lt;/div&gt;&quot;&#10;  }&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: &quot;Hello World&quot;&#10;}&#10;</code></pre>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3617.md")
</aside>
<h3 id="exclude-unwanted-requests-for-example-css">Exclude unwanted requests (for example, CSS)</h3>
<p>You can refine the Markdown extraction by using the <code>rejectRequestPattern</code> parameter. In this example, requests matching the given regex pattern (such as CSS files) are excluded.</p>
<pre><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;rejectRequestPattern&quot;: [&quot;/^.*\\.(css)/&quot;]&#10;  }&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: &quot;# Example Domain\n\nThis domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.\n\n[More information...](https://www.iana.org/domains/example)&quot;&#10;}&#10;</code></pre>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3616.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
<h2 id="other-markdown-conversion-features">Other Markdown conversion features</h2>
<ul>
<li>Workers AI <a href="/workers-ai/features/markdown-conversion/">AI.toMarkdown()</a> supports multiple document types and summarization.</li>
<li><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> allows real-time document conversion for Cloudflare zones using content negotiation headers.</li>
</ul>
