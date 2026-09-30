---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/
  description: Restrict Cloudflare API access at the account or member level using Enterprise account controls.
  full_title: Control API Access · Cloudflare Fundamentals docs
  head_html: <title>Control API Access · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict Cloudflare API access at the account or member level using Enterprise account controls."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/index.md"><meta property="og:title" content="Control API Access · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict Cloudflare API access at the account or member level using Enterprise account controls."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/#page","headline":"Control API Access \u00b7 Cloudflare Fundamentals docs","description":"Restrict Cloudflare API access at the account or member level using Enterprise account controls.","url":"https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/how-to/control-api-access/
  schema: 1
---
<p>Super administrators of an Enterprise account are capable of selectively scoping the API access. API access can be restricted for the entire account or only for specified account members.</p>
<p>Note that the feature does not disable API calls not related to the Enterprise account.</p>
<h2 id="account-level-access-control">Account-level access control</h2>
<p>To restrict the API access for the entire account:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Members</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Locate the <strong>Enable API Access</strong> section and then update the setting.</li>
</ol>
<h2 id="member-level-access-control">Member-level access control</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8996.md")
</aside>
<p>To restrict the API access for a specific member:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Members</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Click on the member to expand and choose the intended <strong>API Access</strong>. If <code>Account Default</code>, then it follows the account level setting.</li>
</ol>
