<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 17, 2026</time><h2 id="post-title">Delete Workflow instances individually or in batches</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>You can now delete one or up to 100 Workflow instances and their stored state via the <a href="/workflows/build/workers-api/">Workflows API</a> or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. <a href="/workflows/reference/pricing/#storage-usage">Storage billing</a> is based on the average daily peak.</p>
<p>Delete one instance by calling <a href="/workflows/build/workers-api/#delete"><code>delete()</code></a> on its handle:</p>
<pre><code class="language-ts">const instance = await env.MY_WORKFLOW.get(&quot;instance-abc&quot;);&#10;await instance.delete();&#10;</code></pre>
<p>If a Workflow deletes its own instance, execution stops during <code>await instance.delete()</code>. Code after the call does not run.</p>
<p>Delete multiple instances by calling <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch()</code></a> on the Workflow binding:</p>
<pre><code class="language-ts">const result = await env.MY_WORKFLOW.deleteBatch([&#10;	&quot;instance-abc&quot;,&#10;	&quot;instance-def&quot;,&#10;]);&#10;&#10;console.log(result.deleted);&#10;console.log(result.errors);&#10;</code></pre>
<p>The batch result contains <code>{ id }</code> entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.</p>
<p>Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use <code>latest</code> to delete the most recently created instance. Use <code>--local</code> against a local <code>wrangler dev</code> session:</p>
<pre><code class="language-json">[&quot;instance-abc&quot;, &quot;instance-def&quot;]&#10;</code></pre>
<pre><code class="language-sh">npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow latest&#10;npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; --local&#10;</code></pre>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/#delete-workflow-instances">Delete Workflow instances</a>, <a href="/workflows/build/workers-api/#delete"><code>delete</code></a>, and <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch</code></a>.</p>
</div></article></div>
