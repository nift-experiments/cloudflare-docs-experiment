---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/how-we-docs/our-site/
  description: Understand the documentation site architecture.
  full_title: Our site · Cloudflare Style Guide
  head_html: <title>Our site · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Understand the documentation site architecture."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/how-we-docs/our-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/how-we-docs/our-site/index.md"><meta property="og:title" content="Our site · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the documentation site architecture."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/how-we-docs/our-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/how-we-docs/our-site/#page","headline":"Our site \u00b7 Cloudflare Style Guide","description":"Understand the documentation site architecture.","url":"https://developers.cloudflare.com/style-guide/how-we-docs/our-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/how-we-docs/our-site/
  schema: 1
---
<p>We use a variety of tools to make our docs site work. You could use these tools to build up your own docs site and - in most cases - do so for free or starting on a free tier.</p>
<h2 id="content-management-system">Content management system</h2>
<p>Our content lives in a public GitHub repository, <a href="https://github.com/cloudflare/cloudflare-docs"><code>cloudflare-docs</code></a>.</p>
<p>GitHub offers a generous <a href="https://github.com/pricing">free tier</a>.</p>
<h2 id="search">Search</h2>
<p>We use Cloudflare's <a href="/ai-search/">AI Search</a> as our search provider.</p>
<p>We used to use Algolia, which is also great for open-source docs because you can be part of the free <a href="https://docsearch.algolia.com/">DocSearch program</a>.</p>
<h2 id="site-framework">Site framework</h2>
<p>We use <a href="https://nimbus-docs.com/">Nimbus</a> for our docs, a documentation framework built on <a href="https://astro.build/">Astro</a>.</p>
<p>Nimbus's component <a href="https://nimbus-docs.com/registry/">registry</a> and <a href="https://nimbus-docs.com/writing/linting/">linting</a> system have exponentially increased our <a href="/style-guide/build-the-page/components/">site's capabilities</a> (without much extra work).</p>
<h2 id="builds">Builds</h2>
<p>We use <a href="https://github.com/features/actions">GitHub Actions</a> to build our site, which is then <a href="#hosting">hosted</a> on Cloudflare.</p>
<p>We are moving to <a href="/workers/ci-cd/">Workers CI/CD</a>, which currently runs in the background.</p>
<p>Both of these options include a free tier.</p>
<h2 id="hosting">Hosting</h2>
<p>We host our content using <a href="/workers/static-assets/">Cloudflare Workers</a>, specifically using their built in values for <a href="/workers/framework-guides/web-apps/astro/">Astro sites</a></p>
<p>Workers offers a generous <a href="/workers/platform/pricing/">free tier</a>.</p>
<h2 id="analytics">Analytics</h2>
<p>We send analytics to multiple destinations using <a href="/zaraz/">Cloudflare Zaraz</a>, which has a generous <a href="/zaraz/pricing-info/">free tier</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14607.md")
</aside>
