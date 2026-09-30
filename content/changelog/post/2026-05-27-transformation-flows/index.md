<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 27, 2026</time><h2 id="post-title">Transformation flows in Images</h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/images/custom-flow.png" alt="Custom flow configuration panel" /></p>
<p>Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.</p>
<p>There are two modes for transformation flows:</p>
<ul>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-provider-flow">Provider flows</a></strong> — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.</li>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-custom-flow">Custom flows</a></strong> — Define your own conditions and actions for use cases like automatic format conversion, <a href="/images/optimization/make-responsive-images/#using-widthauto">responsive sizing</a> with <code>width=auto</code>, or directory-based optimization.</li>
</ul>
<p>To get started, go to <strong>Images</strong> &gt; <strong>Transformations</strong> &gt; <strong>Automation</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>.</p>
<p>Learn more about <a href="/images/optimization/transformations/flows/">transformation flows</a>.</p>
</div></article></div>
