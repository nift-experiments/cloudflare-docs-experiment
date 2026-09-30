<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 17, 2025</time><h2 id="post-title">Read multiple keys from Workers KV with bulk reads</h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.</p>
<p>This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by <a href="/workers/platform/limits/#simultaneous-open-connections">Workers simultaneous connection limits</a>.</p>
<pre><code class="language-js">// Read single key&#10;const key = &quot;key-a&quot;;&#10;const value = await env.NAMESPACE.get(key);&#10;&#10;// Read multiple keys&#10;const keys = [&quot;key-a&quot;, &quot;key-b&quot;, &quot;key-c&quot;, ...] // up to 100 keys&#10;const values : Map&lt;string, string?&gt; = await env.NAMESPACE.get(keys);&#10;&#10;// Print the value of &quot;key-a&quot; to the console.&#10;console.log(`The first key is ${values.get(&quot;key-a&quot;)}.`)&#10;</code></pre>
<p>Consult the <a href="/kv/api/read-key-value-pairs/">Workers KV Read key-value pairs API</a> for full details on Workers KV's new bulk reads support.</p>
</div></article></div>
