---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/
  description: Redirect AI training crawlers to canonical URLs.
  full_title: Redirects for AI Training · Cloudflare AI Crawl Control docs
  head_html: <title>Redirects for AI Training · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Redirect AI training crawlers to canonical URLs."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/index.md"><meta property="og:title" content="Redirects for AI Training · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Redirect AI training crawlers to canonical URLs."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/#page","headline":"Redirects for AI Training \u00b7 Cloudflare AI Crawl Control docs","description":"Redirect AI training crawlers to canonical URLs.","url":"https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/reference/redirects-for-ai-training/
  schema: 1
---
<p>Redirects for AI Training enforces your existing <span class="nb-glossary-tooltip" title="canonical URL">�CODE6�</span> tags as 301 redirects for <a href="/bots/concepts/bot/#verified-bots">verified AI training crawlers</a>. When a verified bot with the <a href="/bots/concepts/bot/verified-bots/#legacy-categories">AI Crawler category</a> requests a page whose canonical tag points to a different same-origin URL, Cloudflare returns a <code>301 Moved Permanently</code> to the canonical. All other visitors—browsers, search engines, <a href="/bots/concepts/bot/verified-bots/#legacy-categories">AI Assistants</a>—receive the original page unchanged.</p>
<p>To learn more about why this feature can be useful, refer to the <a href="https://blog.cloudflare.com/ai-redirects/">announcement blog post</a>.</p>
<h2 id="enable-redirects-for-ai-training">Enable Redirects for AI Training</h2>
<p>Redirects for AI Training is available as a toggle in <strong>AI Crawl Control</strong> &gt; <strong>Quick Actions</strong>, alongside <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> and <a href="/bots/additional-configurations/managed-robots-txt/">Managed robots.txt</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2718.md")
</div></div>
<h2 id="how-it-works">How it works</h2>
<p>Cloudflare inspects the origin HTML response to verified AI training crawlers and:</p>
<ol>
<li>Stream-parses the <code>&lt;head&gt;</code> of the origin response to extract <code>&lt;link rel=&quot;canonical&quot; href=&quot;...&quot;&gt;</code></li>
<li>Resolves relative canonical URLs against the request URL</li>
<li>Validates that the canonical URL is same-origin and differs from the current URL</li>
<li>Returns a <code>301</code> redirect to the canonical URL</li>
</ol>
<p>If no canonical tag is found, the canonical is cross-origin, or the page is self-canonical, the origin response passes through unchanged.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="interaction-with-markdown-for-agents">Interaction with Markdown for Agents</h3>
@markup("md", "content/.markup/bodies/2713.md")
</aside>
<h3 id="canonical-tag-parsing">Canonical tag parsing</h3>
<p>The feature parses the <code>&lt;link rel=&quot;canonical&quot;&gt;</code> tag from the <code>&lt;head&gt;</code> section of the origin response:</p>
<pre tabindex="0"><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;&lt;head&gt;&#10;  &lt;link rel=&quot;canonical&quot; href=&quot;https://example.com/current-version&quot;&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;  &lt;!-- Page content --&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>Both absolute and relative URLs are supported:</p>
<pre tabindex="0"><code class="language-html">&lt;!-- Absolute URL --&gt;&#10;&lt;link rel=&quot;canonical&quot; href=&quot;https://example.com/page&quot;&gt;&#10;&#10;&lt;!-- Relative URL (resolved against request URL) --&gt;&#10;&lt;link rel=&quot;canonical&quot; href=&quot;/current-page&quot;&gt;&#10;</code></pre>
<h3 id="interaction-with-other-redirect-features">Interaction with other redirect features</h3>
<p>Redirects for AI Training operates at a different layer than <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a> and <a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>. Those redirect rules execute before the origin is contacted. Redirects for AI Training executes after the origin responds, because it needs to read the canonical tag from the origin HTML.</p>
<p>If a Single Redirect or Bulk Redirect matches first, the request is redirected before Redirects for AI Training has a chance to evaluate it.</p>
<h2 id="availability">Availability</h2>
<p>Available on Pro, Business, and Enterprise plans at no additional cost.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Only HTML responses (<code>content-type: text/html</code>) from the origin are evaluated. Other content types pass through unchanged.</li>
<li>The canonical tag must appear within the first 256 KB of the uncompressed HTML response body.</li>
<li>Only same-origin canonical URLs trigger a redirect. Cross-origin canonicals are ignored.</li>
<li>Only <a href="/bots/concepts/bot/#verified-bots">verified bots</a> with the <a href="/bots/concepts/bot/verified-bots/#legacy-categories">AI Crawler category</a> are redirected. <a href="/bots/concepts/bot/verified-bots/#legacy-categories">AI Assistants and AI Search bots</a> are not affected.</li>
<li>Self-canonical pages (where the canonical URL matches the request URL) are not redirected.</li>
<li>Best-effort loop detection uses the <code>Referer</code> header. If a crawler was just redirected from the canonical URL back to the current page, the origin HTML is served instead of redirecting. This handles common two-page canonical misconfigurations (Page A canonical points to Page B, Page B canonical points to Page A).</li>
</ul>
<h2 id="logging">Logging</h2>
<p>When a redirect is issued, Cloudflare logs the canonical target URL in your HTTP request logs via the <code>redirects_for_ai_training_target</code> field. You can use the <a href="/ai-crawl-control/reference/graphql-api/">GraphQL Analytics API</a> or <a href="/logs/logpush/">Logpush</a> to query this data.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a> - Set allow or block rules per crawler</li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a> - View request metrics by crawler, operator, and content type</li>
<li><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> - Serve HTML as markdown via content negotiation</li>
<li><a href="https://contentsignals.org/">Content Signals Policy</a> - Signal post-access content usage preferences in <code>robots.txt</code></li>
<li><a href="/ai-crawl-control/features/track-robots-txt/">Directives</a> - Monitor <code>robots.txt</code> compliance and check Agent Readiness</li>
<li><a href="/rules/url-forwarding/single-redirects/">Single Redirects</a> - Rule-based URL redirects that execute before origin</li>
<li><a href="/bots/concepts/bot/verified-bots/#legacy-categories">Verified bots</a> - Bot categories including AI Crawler, AI Assistant, and AI Search</li>
</ul>
