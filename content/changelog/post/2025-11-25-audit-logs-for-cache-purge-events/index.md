---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/
  description: New updates and improvements at Cloudflare.
  full_title: Audit Logs for Cache Purge Events · Changelog
  head_html: <title>Audit Logs for Cache Purge Events · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Audit Logs for Cache Purge Events · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/#page","headline":"Audit Logs for Cache Purge Events \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-25-audit-logs-for-cache-purge-events/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 25, 2025</time><h2 id="post-title">Audit Logs for Cache Purge Events</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now review detailed audit logs for cache purge events, giving you visibility into what purge requests were sent, what they contained, and by whom. Audit your purge requests via the Dashboard or API for all purge methods:</p>
<ul>
<li>Purge everything</li>
<li>List of prefixes</li>
<li>List of tags</li>
<li>List of hosts</li>
<li>List of files</li>
</ul>
<h4 id="example">Example</h4>
<p>The detailed audit payload is visible within the Cloudflare Dashboard (under <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>) and via the API. Below is an example of the Audit Logs v2 payload structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;action&quot;: {&#10;    &quot;result&quot;: &quot;success&quot;,&#10;    &quot;type&quot;: &quot;create&quot;&#10;  },&#10;  &quot;actor&quot;: {&#10;    &quot;id&quot;: &quot;1234567890abcdef&quot;,&#10;    &quot;email&quot;: &quot;user@example.com&quot;,&#10;    &quot;type&quot;: &quot;user&quot;&#10;  },&#10;  &quot;resource&quot;: {&#10;    &quot;product&quot;: &quot;purge_cache&quot;,&#10;    &quot;request&quot;: {&#10;      &quot;files&quot;: [&#10;        &quot;https://example.com/images/logo.png&quot;,&#10;        &quot;https://example.com/css/styles.css&quot;&#10;      ]&#10;    }&#10;  },&#10;  &quot;zone&quot;: {&#10;    &quot;id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;    &quot;name&quot;: &quot;example.com&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="get-started">Get started</h4>
<p>To get started, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
</div></article></div>
