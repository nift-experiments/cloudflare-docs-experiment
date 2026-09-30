---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/
  description: New updates and improvements at Cloudflare.
  full_title: New CPU Pricing for Containers and Sandboxes · Changelog
  head_html: <title>New CPU Pricing for Containers and Sandboxes · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New CPU Pricing for Containers and Sandboxes · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/#page","headline":"New CPU Pricing for Containers and Sandboxes \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-21-new-cpu-pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-21-new-cpu-pricing/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 21, 2025</time><h2 id="post-title">New CPU Pricing for Containers and Sandboxes</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> pricing for CPU time is now based on active usage only, instead of provisioned resources.</p>
<p>This means that you now pay less for Containers and Sandboxes.</p>
<h4 id="an-example-before-and-after">An Example Before and After</h4>
<p>Imagine running the <code>standard-2</code> instance type for one hour, which can use up to 1 vCPU,
but on average you use only 20% of your CPU capacity.</p>
<p>CPU-time is priced at <em>$0.00002 per vCPU-second</em>.</p>
<p>Previously, you would be charged for the CPU allocated to the instance multiplied by the time it was active, in this case 1 hour.</p>
<p>CPU cost would have been: <strong>$0.072</strong> — 1 vCPU * 3600 seconds * $0.00002</p>
<p>Now, since you are only using 20% of your CPU capacity, your CPU cost is cut to 20% of the previous amount.</p>
<p>CPU cost is now: <strong>$0.0144</strong> — 1 vCPU * 3600 seconds * $0.00002 * 20% utilization</p>
<p>This can significantly reduce costs for Containers and Sandboxes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17708.md")</aside>
<p>See the documentation to learn more about <a href="/containers/get-started/">Containers</a>, <a href="/sandbox/">Sandboxes</a>,
and <a href="/containers/platform/pricing">associated pricing</a>.</p>
</div></article></div>
