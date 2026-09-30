---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/
  description: New updates and improvements at Cloudflare.
  full_title: Markdown responses for Cloudflare 1xxx errors · Changelog
  head_html: <title>Markdown responses for Cloudflare 1xxx errors · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Markdown responses for Cloudflare 1xxx errors · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/#page","headline":"Markdown responses for Cloudflare 1xxx errors \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 26, 2026</time><h2 id="post-title">Markdown responses for Cloudflare 1xxx errors</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare now returns structured Markdown responses for Cloudflare-generated 1xxx errors when clients send <code>Accept: text/markdown</code>.</p>
<p>Each response includes YAML frontmatter plus guidance sections (<code>What happened</code> / <code>What you should do</code>) so agents can make deterministic retry and escalation decisions without parsing HTML.</p>
<p>In measured 1,015 comparisons, Markdown reduced payload size and token footprint by over 98% versus HTML.</p>
<p>Included frontmatter fields:</p>
<ul>
<li><code>error_code</code>, <code>error_name</code>, <code>error_category</code>, <code>http_status</code></li>
<li><code>ray_id</code>, <code>timestamp</code>, <code>zone</code></li>
<li><code>cloudflare_error</code>, <code>retryable</code>, <code>retry_after</code> (when applicable), <code>owner_action_required</code></li>
</ul>
<p>Default behavior is unchanged: clients that do not explicitly request Markdown continue to receive HTML error pages.</p>
<h4 id="negotiation-behavior">Negotiation behavior</h4>
<p>Cloudflare uses standard HTTP content negotiation on the <code>Accept</code> header.</p>
<ul>
<li><code>Accept: text/markdown</code> -&gt; Markdown</li>
<li><code>Accept: text/markdown, text/html;q=0.9</code> -&gt; Markdown</li>
<li><code>Accept: text/*</code> -&gt; Markdown</li>
<li><code>Accept: */*</code> -&gt; HTML (default browser behavior)</li>
</ul>
<p>When multiple values are present, Cloudflare selects the highest-priority supported media type using <code>q</code> values. If Markdown is not explicitly preferred, HTML is returned.</p>
<h4 id="availability">Availability</h4>
<p>Available now for Cloudflare-generated 1xxx errors.</p>
<h4 id="get-started">Get started</h4>
<pre tabindex="0"><code class="language-bash">curl -H &quot;Accept: text/markdown&quot; https://&lt;your-domain&gt;/cdn-cgi/error/1015&#10;</code></pre>
<p>Reference: <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></p>
</div></article></div>
