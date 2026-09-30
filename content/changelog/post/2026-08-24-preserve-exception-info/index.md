<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 24, 2026</time><h2 id="post-title">Preserve exception details in console logs</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Console methods now preserve exception details in your Worker's logs. When your Worker logs an exception, the corresponding log entry includes the exception name, message, and stack.</p>
<p>For example, your Worker can catch and log an exception:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17814.md")</div>
<p>If you use <a href="/workers/observability/">Workers Observability</a>, your log is automatically enriched with structured error information. The following example shows how the enriched log appears in the Cloudflare dashboard:</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-08-24-error-info.png" alt="Workers Observability log entry showing a caught exception and its stack trace" /></p>
<p>The exception's stack trace appears directly in the log message.</p>
<p>If you send telemetry to a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a>, the Tail Worker now receives a log entry with an <code>errorInfo</code> array:</p>
<pre><code class="language-json">{&#10;	&quot;message&quot;: [&quot;Request failed:&quot;, &quot;RangeError: Value out of range&quot;],&#10;	&quot;errorInfo&quot;: [&#10;		null,&#10;		{&#10;			&quot;name&quot;: &quot;RangeError&quot;,&#10;			&quot;message&quot;: &quot;Value out of range&quot;,&#10;			&quot;stack&quot;: &quot;RangeError: Value out of range\n    at ...&quot;&#10;		}&#10;	],&#10;	&quot;level&quot;: &quot;error&quot;,&#10;	&quot;timestamp&quot;: 1784851200000&#10;}&#10;</code></pre>
<p>Each <code>errorInfo</code> item corresponds to the console argument at the same index in <code>message</code>. Arguments that are not exceptions have a <code>null</code> entry.</p>
</div></article></div>
