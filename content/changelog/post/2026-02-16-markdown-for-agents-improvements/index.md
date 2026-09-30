<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 16, 2026</time><h2 id="post-title">Content encoding support for Markdown for Agents and other improvements</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>When AI systems request pages from any website that uses Cloudflare and has <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> enabled, they can express the preference for <code>text/markdown</code> in the request: our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.</p>
<p>This release adds the following improvements:</p>
<ul>
<li>The origin response limit was raised from 1 MB to 2 MB (2,097,152 bytes).</li>
<li>We no longer require the origin to send the <code>content-length</code> header.</li>
<li>We now support content encoded responses from the origin.</li>
</ul>
<p>If you haven’t enabled automatic Markdown conversion yet, visit the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ai">AI Crawl Control</a> section of the Cloudflare dashboard and enable <strong>Markdown for Agents</strong>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>
</div></article></div>
