<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>Workflow instance methods <code>pause()</code>, <code>resume()</code>, <code>restart()</code>, and <code>terminate()</code> are now available in local development when using <code>wrangler dev</code>.</p>
<p>You can now test the full Workflow instance lifecycle locally:</p>
<pre><code class="language-ts">const instance = await env.MY_WORKFLOW.create({&#10;	id: &quot;my-instance-id&quot;,&#10;});&#10;&#10;await instance.pause(); // pauses a running workflow instance&#10;await instance.resume(); // resumes a paused instance&#10;await instance.restart(); // restarts the instance from the beginning&#10;await instance.terminate(); // terminates the instance immediately&#10;</code></pre>
</div></article></div>
