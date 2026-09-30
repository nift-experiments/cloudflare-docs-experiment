---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/
  description: Store, version, and share filesystem artifacts across Workers, APIs, and Git-compatible tools.
  full_title: Artifacts · Cloudflare Artifacts docs
  head_html: <title>Artifacts · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Store, version, and share filesystem artifacts across Workers, APIs, and Git-compatible tools."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/index.md"><meta property="og:title" content="Artifacts · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store, version, and share filesystem artifacts across Workers, APIs, and Git-compatible tools."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/artifacts/#page","headline":"Artifacts \u00b7 Cloudflare Artifacts docs","description":"Store, version, and share filesystem artifacts across Workers, APIs, and Git-compatible tools.","url":"https://developers.cloudflare.com/artifacts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1502.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1501.md")
</aside>
<p>Artifacts stores versioned file trees behind a Git-compatible interface. Create repositories programmatically, import existing repositories, and hand off a URL to any standard Git client.</p>
<p>Review <a href="/artifacts/concepts/namespaces/">Namespaces</a> before you start, then choose the namespace name you will use for these repos.</p>
<p>Use Artifacts when you need to:</p>
<ul>
<li>Store versioned file trees instead of raw blobs</li>
<li>Hand off work to Git-aware tools, agents, and automation</li>
<li>Isolate work in separate repos or branches for safer parallel execution</li>
<li>Fork from a shared baseline and diff or merge the results later</li>
</ul>
<p>The same repository can be addressed from <a href="/artifacts/get-started/workers/">Workers</a>, the REST API, and Git clients. You can create one repo per agent, user, branch, or task, keep each unit of work separate, and compare or merge the results later.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/1510.md")
</div>
