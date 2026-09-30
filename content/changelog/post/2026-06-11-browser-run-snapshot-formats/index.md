<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 11, 2026</time><h2 id="post-title">New formats parameter for the Browser Run /snapshot endpoint</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a>'s <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> endpoint</a> now supports a <code>formats</code> parameter that lets you return multiple page formats in a single API call. Previously, <code>/snapshot</code> returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.</p>
<p>These formats are particularly useful for AI agent workflows:</p>
<ul>
<li>Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.</li>
<li>The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.</li>
</ul>
<p>The following example returns a screenshot, Markdown, and the accessibility tree in one call:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17699.md")
</div></div>
<p>You must request at least two formats. If you only need one, use the respective single-format endpoint such as <a href="/browser-run/quick-actions/screenshot-endpoint/"><code>/screenshot</code></a> or <a href="/browser-run/quick-actions/markdown-endpoint/"><code>/markdown</code></a>.</p>
<p>Refer to the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> documentation</a> for the full list of accepted values.</p>
</div></article></div>
