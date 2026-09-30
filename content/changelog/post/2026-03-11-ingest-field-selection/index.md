---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/
  description: New updates and improvements at Cloudflare.
  full_title: Ingest field selection for Log Explorer · Changelog
  head_html: <title>Ingest field selection for Log Explorer · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Ingest field selection for Log Explorer · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/#page","headline":"Ingest field selection for Log Explorer \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-11-ingest-field-selection/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 11, 2026</time><h2 id="post-title">Ingest field selection for Log Explorer</h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.</p>
<p>Previously, ingesting logs often meant taking an &quot;all or nothing&quot; approach to data fields. With <strong>Ingest Field Selection</strong>, you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.</p>
<h4 id="key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Granular control:</strong> Select only the specific fields you need when enabling a new dataset.</li>
<li><strong>Dynamic updates:</strong> Update fields for existing, already enabled logstreams at any time.</li>
<li><strong>Historical consistency:</strong> Even if you disable a field later, you can still query and receive results for that field for the period it was captured.</li>
<li><strong>Data integrity:</strong> Core fields, such as <code>Timestamp</code>, are automatically retained to ensure your logs remain searchable and chronologically accurate.</li>
</ul>
<h4 id="example-configuration">Example configuration</h4>
<p>When configuring a dataset via the dashboard or API, you can define a specific set of fields. The <code>Timestamp</code> field remains mandatory to ensure data indexability.</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;dataset&quot;: &quot;firewall_events&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;fields&quot;: [&#10;    &quot;Timestamp&quot;,&#10;    &quot;ClientRequestHost&quot;,&#10;    &quot;ClientIP&quot;,&#10;    &quot;Action&quot;,&#10;    &quot;EdgeResponseStatus&quot;,&#10;    &quot;OriginResponseStatus&quot;&#10;  ]&#10;}&#10;</code></pre>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>
</div></article></div>
