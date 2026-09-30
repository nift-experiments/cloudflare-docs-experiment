<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 25, 2025</time><h2 id="post-title">Audit Logs for Cache Purge Events</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now review detailed audit logs for cache purge events, giving you visibility into what purge requests were sent, what they contained, and by whom. Audit your purge requests via the Dashboard or API for all purge methods:</p>
<ul>
<li>Purge everything</li>
<li>List of prefixes</li>
<li>List of tags</li>
<li>List of hosts</li>
<li>List of files</li>
</ul>
<h4 id="example">Example</h4>
<p>The detailed audit payload is visible within the Cloudflare Dashboard (under <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>) and via the API. Below is an example of the Audit Logs v2 payload structure:</p>
<pre><code class="language-json">{&#10;  &quot;action&quot;: {&#10;    &quot;result&quot;: &quot;success&quot;,&#10;    &quot;type&quot;: &quot;create&quot;&#10;  },&#10;  &quot;actor&quot;: {&#10;    &quot;id&quot;: &quot;1234567890abcdef&quot;,&#10;    &quot;email&quot;: &quot;user@example.com&quot;,&#10;    &quot;type&quot;: &quot;user&quot;&#10;  },&#10;  &quot;resource&quot;: {&#10;    &quot;product&quot;: &quot;purge_cache&quot;,&#10;    &quot;request&quot;: {&#10;      &quot;files&quot;: [&#10;        &quot;https://example.com/images/logo.png&quot;,&#10;        &quot;https://example.com/css/styles.css&quot;&#10;      ]&#10;    }&#10;  },&#10;  &quot;zone&quot;: {&#10;    &quot;id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;    &quot;name&quot;: &quot;example.com&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="get-started">Get started</h4>
<p>To get started, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
</div></article></div>
