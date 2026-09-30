<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 24, 2025</time><h2 id="post-title">Cron triggers are now supported in Python Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create Python Workers which are executed via a cron trigger.</p>
<p>This is similar to how it's done in JavaScript Workers, simply define a scheduled event
listener in your Worker:</p>
<pre><code class="language-python">from workers import handler&#10;&#10;@handler&#10;async def on_scheduled(event, env, ctx):&#10;  print(&quot;cron processed&quot;)&#10;</code></pre>
<p>Define a cron trigger configuration in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17772.md")</div>
<p>Then test your new handler by using Wrangler with the <code>--test-scheduled</code> flag and
making a request to <code>/cdn-cgi/local/scheduled?cron=*+*+*+*+*</code>:</p>
<pre><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<p>Consult the <a href="/workers/configuration/cron-triggers/">Workers Cron Triggers page</a> for full details on cron triggers in Workers.</p>
</div></article></div>
