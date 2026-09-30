<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 21, 2025</time><h2 id="post-title">Better local deployment flow for Cloudflare Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Until now, if a Worker had been previously deployed via the <a href="https://dash.cloudflare.com">Cloudflare Dashboard</a>, a subsequent deployment done via the Cloudflare Workers CLI, <a href="/workers/wrangler/"><strong>Wrangler</strong></a>
(through the <a href="/workers/wrangler/commands/general/#deploy"><code>deploy</code> command</a>), would allow the user to override the Worker's dashboard settings without providing details on
what dashboard settings would be lost.</p>
<p>Now instead, <code>wrangler deploy</code> presents a helpful representation of the differences between the <a href="/workers/wrangler/configuration/">local configuration</a>
and the remote dashboard settings, and offers to update your local configuration file for you.</p>
<p>See example below showing a before and after for <code>wrangler deploy</code> when a local configuration is expected to override a Worker's dashboard settings:</p>
<div class="nb-example"><h3 class="nb-component-title" id="before">Before</h3>
@markup("md", "content/.markup/bodies/17791.md")</div>
<div class="nb-example"><h3 class="nb-component-title" id="after">After</h3>
@markup("md", "content/.markup/bodies/17792.md")</div>
<p>Also, if instead Wrangler detects that a deployment would override remote dashboard settings but in an additive way, without modifying or removing any of them, it will simply proceed with the deployment without requesting any user interaction.</p>
<p>Update to <a href="/workers/wrangler/">Wrangler</a> v4.50.0 or greater to take advantage of this improved deploy flow.</p>
</div></article></div>
