<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 30, 2025</time><h2 id="post-title">AI Gateway Introduces New Worker Binding Methods</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>We have released new <a href="/ai-gateway/usage/worker-binding-methods/">Workers bindings API methods</a>, allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.</p>
<p>To add an AI binding to your Worker, include the following in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<p><img src="/assets/upstream/images/ai-gateway/add-binding.png" alt="Add an AI binding to your Worker." /></p>
<p>With the new AI Gateway binding methods, you can now:</p>
<ul>
<li>Send feedback and update metadata with <code>patchLog</code>.</li>
<li>Retrieve detailed log information using <code>getLog</code>.</li>
<li>Execute <a href="/ai-gateway/usage/universal/">universal requests</a> to any AI Gateway provider with <code>run</code>.</li>
</ul>
<p>For example, to send feedback and update metadata using <code>patchLog</code>:</p>
<p><img src="/assets/upstream/images/ai-gateway/send-feedback.png" alt="Send feedback and update metadata using patchLog:" /></p>
</div></article></div>
