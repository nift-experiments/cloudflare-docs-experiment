---
cp9:
  canonical: https://developers.cloudflare.com/rules/transform/managed-transforms/
  description: Pre-built Transform Rules managed by Cloudflare for common use cases.
  full_title: Managed Transforms · Cloudflare Rules docs
  head_html: <title>Managed Transforms · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Pre-built Transform Rules managed by Cloudflare for common use cases."><link rel="canonical" href="https://developers.cloudflare.com/rules/transform/managed-transforms/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/transform/managed-transforms/index.md"><meta property="og:title" content="Managed Transforms · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pre-built Transform Rules managed by Cloudflare for common use cases."><meta property="og:url" content="https://developers.cloudflare.com/rules/transform/managed-transforms/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/transform/managed-transforms/#page","headline":"Managed Transforms \u00b7 Cloudflare Rules docs","description":"Pre-built Transform Rules managed by Cloudflare for common use cases.","url":"https://developers.cloudflare.com/rules/transform/managed-transforms/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/transform/managed-transforms/
  schema: 1
---
<p>Managed Transforms allow you to perform common adjustments to HTTP request and response headers with pre-built, one-step configurations. The available adjustments include:</p>
<ul>
<li>Add bot protection request headers.</li>
<li>Remove or add headers related to the visitor's IP address.</li>
<li>Add request header when Cloudflare detects <a href="/waf/detections/leaked-credentials/">leaked credentials</a>.</li>
<li>Add security-related response headers.</li>
<li>Remove <code>X-Powered-By</code> response headers.</li>
</ul>
<p>For a complete list, refer to <a href="/rules/transform/managed-transforms/reference/">Available Managed Transforms</a>.</p>
<p>When you enable a Managed Transform, Cloudflare internally deploys one or more Transform Rules to handle the common configuration you selected. These generated rules will not count against the <a href="/rules/transform/#availability">maximum number of Transform Rules</a> available in your Cloudflare plan.</p>
<p>Enabled Managed Transforms will apply to all inbound requests for the <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> (domain or subdomain added to Cloudflare).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13152.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>For dashboard, API, and Terraform instructions, refer to <a href="/rules/transform/managed-transforms/configure/">Configure Managed Transforms</a>.</p>
