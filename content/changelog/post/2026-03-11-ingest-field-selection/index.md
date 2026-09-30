<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 11, 2026</time><h2 id="post-title">Ingest field selection for Log Explorer</h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.</p>
<p>Previously, ingesting logs often meant taking an &quot;all or nothing&quot; approach to data fields. With <strong>Ingest Field Selection</strong>, you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.</p>
<h4 id="key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Granular control:</strong> Select only the specific fields you need when enabling a new dataset.</li>
<li><strong>Dynamic updates:</strong> Update fields for existing, already enabled logstreams at any time.</li>
<li><strong>Historical consistency:</strong> Even if you disable a field later, you can still query and receive results for that field for the period it was captured.</li>
<li><strong>Data integrity:</strong> Core fields, such as <code>Timestamp</code>, are automatically retained to ensure your logs remain searchable and chronologically accurate.</li>
</ul>
<h4 id="example-configuration">Example configuration</h4>
<p>When configuring a dataset via the dashboard or API, you can define a specific set of fields. The <code>Timestamp</code> field remains mandatory to ensure data indexability.</p>
<pre><code class="language-json">{&#10;  &quot;dataset&quot;: &quot;firewall_events&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;fields&quot;: [&#10;    &quot;Timestamp&quot;,&#10;    &quot;ClientRequestHost&quot;,&#10;    &quot;ClientIP&quot;,&#10;    &quot;Action&quot;,&#10;    &quot;EdgeResponseStatus&quot;,&#10;    &quot;OriginResponseStatus&quot;&#10;  ]&#10;}&#10;</code></pre>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>
</div></article></div>
