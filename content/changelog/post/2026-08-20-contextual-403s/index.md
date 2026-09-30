<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 21, 2026</time><h2 id="post-title">Enriched 403 responses for the Cloudflare API</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare API <code>403 Forbidden</code> responses now include a <code>documentation_url</code> field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.</p>
<p><strong>What's New</strong></p>
<p><strong>Enriched 403 error responses</strong>: When a Cloudflare API request is denied, the error response now includes a <code>documentation_url</code> field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.</p>
<p><strong>Faster troubleshooting</strong>: The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.</p>
<p><strong>Better support for tools and agents</strong>: Agents can use the \documentation_url` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.`</p>
<p>Example 403 response:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: false,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 10000,&#10;      &quot;message&quot;: &quot;Forbidden&quot;,&#10;      &quot;documentation_url&quot;: &quot;https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list&quot;&#10;    }&#10;  ],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: null&#10;}&#10;</code></pre>
<p>For more info:</p>
<ul>
<li><a href="/api/">Browse the Cloudflare API documentation</a></li>
<li><a href="/fundamentals/manage-members/roles/">Review Cloudflare roles</a></li>
<li><a href="/fundamentals/api/reference/permissions/">Review API token permissions</a></li>
</ul>
</div></article></div>
