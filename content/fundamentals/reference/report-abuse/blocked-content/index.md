---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/report-abuse/blocked-content/
  description: Request removal of Trust and Safety content blocks on your domain.
  full_title: Blocked Content · Cloudflare Fundamentals docs
  head_html: <title>Blocked Content · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Request removal of Trust and Safety content blocks on your domain."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/report-abuse/blocked-content/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/report-abuse/blocked-content/index.md"><meta property="og:title" content="Blocked Content · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Request removal of Trust and Safety content blocks on your domain."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/report-abuse/blocked-content/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/report-abuse/blocked-content/#page","headline":"Blocked Content \u00b7 Cloudflare Fundamentals docs","description":"Request removal of Trust and Safety content blocks on your domain.","url":"https://developers.cloudflare.com/fundamentals/reference/report-abuse/blocked-content/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/report-abuse/blocked-content/
  schema: 1
---
<p>If your domain has content that has been blocked, Blocked Content on the dashboard gives you the ability to request the Trust and Safety team to remove a block.</p>
<p>To view Blocked Content on the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Blocked Content</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9005.md")
</aside>
<p>The Security Center dashboard displays three statuses for blocked content: active, pending, or resolved blocks.</p>
<h2 id="active-blocks">Active blocks</h2>
<p>An active block is a block that is in effect on blocking content.</p>
<p>When you select <strong>Request Review</strong>, the status changes to <strong>In Review</strong>, and the block will be reviewed by the Trust and Safety team.</p>
<h2 id="pending-blocks">Pending blocks</h2>
<p>A pending block represents a blocking action Cloudflare will take at the scheduled time.</p>
<p>You can view all your pending blocks by selecting <strong>Pending</strong> on the dashboard. Selecting <strong>Request Review</strong> cancels the pending delayed action. This means that the block will not be placed.</p>
<h2 id="resolved-blocks">Resolved blocks</h2>
<p>Resolved blocks list your recently resolved blocks. Resolved blocks are limited to 30 days of recently resolved blocks. Resolved blocks require no action. You can only sort and/or filter the list.</p>
