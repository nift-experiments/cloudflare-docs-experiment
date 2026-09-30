<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 1, 2025</time><h2 id="post-title">Return markdown</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.</p>
<pre><code class="language-sh">curl https://developers.cloudflare.com/workers/ -H &#x27;Accept: text/markdown&#x27;  -v&#10;</code></pre>
<p>If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example <a href="https://github.com/cloudflare/cloudflare-docs/pull/25493">here</a>.</p>
</div></article></div>
