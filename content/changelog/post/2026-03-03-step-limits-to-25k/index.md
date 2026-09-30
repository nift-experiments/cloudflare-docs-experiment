<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 3, 2026</time><h2 id="post-title">Workflows step limit increased to 25,000 steps per instance</h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>Each Workflow on Workers Paid now supports 10,000 steps by default, configurable up to 25,000 steps in your <code>wrangler.jsonc</code> file:</p>
<pre><code class="language-json">{&#10;	&quot;workflows&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;my-workflow&quot;,&#10;			&quot;binding&quot;: &quot;MY_WORKFLOW&quot;,&#10;			&quot;class_name&quot;: &quot;MyWorkflow&quot;,&#10;			&quot;limits&quot;: {&#10;				&quot;steps&quot;: 25000&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Previously, each instance was limited to 1,024 steps. Now, Workflows can support more complex, long-running executions without the additional complexity of recursive or child workflow calls.</p>
<p>Note that the maximum persisted state limit per Workflow instance remains <strong>100 MB</strong> for Workers Free and <strong>1 GB</strong> for Workers Paid. Refer to <a href="/workflows/reference/limits/">Workflows limits</a> for more information.</p>
</div></article></div>
