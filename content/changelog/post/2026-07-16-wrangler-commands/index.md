<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 16, 2026</time><h2 id="post-title">Manage Flagship from the command line with Wrangler</h2>
<div class="changelog-badges"><span>flagship</span></div><div class="changelog-body"><p><strong><a href="/workers/wrangler/">Wrangler</a></strong> now includes <code>wrangler flagship</code>, a command suite for managing <a href="/flagship/">Flagship</a> apps and feature flags from your terminal.</p>
<p>Create an app and, if you use it from a Worker, add it to your <code>wrangler.json</code> or <code>wrangler.jsonc</code> file as a binding:</p>
<pre><code class="language-bash">wrangler flagship apps create &quot;My Worker App&quot; \&#10;  &#45;-binding FLAGS \&#10;  &#45;-update-config&#10;</code></pre>
<p>Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values:</p>
<pre><code class="language-bash">wrangler flagship flags create &lt;APP_ID&gt; new-checkout&#10;&#10;wrangler flagship flags create &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-variation control=old-checkout \&#10;  &#45;-variation treatment=new-checkout \&#10;  &#45;-default control \&#10;  &#45;-type string&#10;</code></pre>
<p>After a flag exists, change its default variation or use enable and disable commands as kill switches. Existing targeting rules continue to apply unless you change or clear them explicitly:</p>
<pre><code class="language-bash">wrangler flagship flags update &lt;APP_ID&gt; checkout-flow --default treatment&#10;wrangler flagship flags disable &lt;APP_ID&gt; checkout-flow&#10;wrangler flagship flags enable &lt;APP_ID&gt; checkout-flow&#10;</code></pre>
<p>For release workflows, use <code>rollout</code>, <code>split</code>, and <code>rules</code> to change exposure without redeploying your Worker:</p>
<pre><code class="language-bash">wrangler flagship flags rollout &lt;APP_ID&gt; new-checkout \&#10;  &#45;-to on \&#10;  &#45;-percentage 25 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags split &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-weight control=80 \&#10;  &#45;-weight treatment=20 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags rules update &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-priority 1 \&#10;  &#45;-when &quot;country equals US&quot;&#10;</code></pre>
<p>These commands can also be used from CI/CD pipelines, scripts, and AI agents to inspect Flagship state, update flag behavior, or roll back changes through Wrangler.</p>
<p>Refer to the <a href="/flagship/reference/wrangler-commands/"><code>wrangler flagship</code> command reference</a> for the full command guide.</p>
</div></article></div>
