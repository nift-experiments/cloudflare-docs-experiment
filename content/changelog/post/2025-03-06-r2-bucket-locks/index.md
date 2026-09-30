<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 6, 2025</time><h2 id="post-title">Set retention polices for your R2 bucket with bucket locks</h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>You can now use <a href="/r2/buckets/bucket-locks/">bucket locks</a> to set retention policies on your <a href="/r2/buckets/">R2 buckets</a> (or specific prefixes within your buckets) for a specified period — or indefinitely. This can help ensure compliance by protecting important data from accidental or malicious deletion.</p>
<p>Locks give you a few ways to ensure your objects are retained (not deleted or overwritten). You can:</p>
<ul>
<li>Lock objects for a specific duration, for example 90 days.</li>
<li>Lock objects until a certain date, for example January 1, 2030.</li>
<li>Lock objects indefinitely, until the lock is explicitly removed.</li>
</ul>
<p>Buckets can have up to 1,000 <a href="/r2/buckets/">bucket lock rules</a>. Each rule specifies which objects it covers (via prefix) and how long those objects must remain retained.</p>
<p>Here are a couple of examples showing how you can configure bucket lock rules using <a href="/workers/wrangler/">Wrangler</a>:</p>
<h4 id="ensure-all-objects-in-a-bucket-are-retained-for-at-least-180-days">Ensure all objects in a bucket are retained for at least 180 days</h4>
<pre><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name 180-days-all --retention-days 180&#10;</code></pre>
<h4 id="prevent-deletion-or-overwriting-of-all-logs-indefinitely-via-prefix">Prevent deletion or overwriting of all logs indefinitely (via prefix)</h4>
<pre><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name indefinite-logs --prefix logs/ --retention-indefinite&#10;</code></pre>
<p>For more information on bucket locks and how to set retention policies for objects in your R2 buckets, refer to our <a href="/r2/buckets/bucket-locks/">documentation</a>.</p>
</div></article></div>
