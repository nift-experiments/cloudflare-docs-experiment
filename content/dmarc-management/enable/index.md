---
cp9:
  canonical: https://developers.cloudflare.com/dmarc-management/enable/
  description: Allow Cloudflare to process DMARC reports for your apex domain.
  full_title: Enable DMARC Management · Cloudflare DMARC Management docs
  head_html: <title>Enable DMARC Management · Cloudflare DMARC Management docs</title><meta name="generator" content="Nift"><meta name="description" content="Allow Cloudflare to process DMARC reports for your apex domain."><link rel="canonical" href="https://developers.cloudflare.com/dmarc-management/enable/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dmarc-management/enable/index.md"><meta property="og:title" content="Enable DMARC Management · Cloudflare DMARC Management docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Allow Cloudflare to process DMARC reports for your apex domain."><meta property="og:url" content="https://developers.cloudflare.com/dmarc-management/enable/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DMARC Management"><meta name="algolia_product_filter" content="DMARC Management"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DMARC Management"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dmarc-management/enable/#page","headline":"Enable DMARC Management \u00b7 Cloudflare DMARC Management docs","description":"Allow Cloudflare to process DMARC reports for your apex domain.","url":"https://developers.cloudflare.com/dmarc-management/enable/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /dmarc-management/enable/
  schema: 1
---
<p>You need to enable DMARC Management to allow Cloudflare to process DMARC reports on your behalf. DMARC Management only works with <span class="nb-glossary-tooltip" title="apex domain">apex domains</span> (for example, <code>example.com</code>, not <code>blog.example.com</code>) and not domains in <a href="/dns/zone-setups/subdomain-setup/">subdomain setups</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="a-warning-on-dmarc-management-and-spf-records">A warning on DMARC Management and SPF records</h3>
@markup("md", "content/.markup/bodies/1141.md")
</aside>
<p>To enable DMARC Management:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email</strong> &gt; <strong>DMARC Management</strong>.</li>
<li>Select <strong>Enable DMARC Management</strong>.</li>
<li>DMARC Management will scan your zone for DMARC records, and will present you with two outcomes:
<ul>
<li>If no DMARC record is found, Cloudflare will automatically invite you to add one that you can edit later. Select <strong>Add</strong> to continue.</li>
<li>If a DMARC record is found in your zone, Cloudflare will add another <code>rua</code> (Reporting URI for Aggregate data) entry to it. The <code>rua</code> tag specifies the URI (typically a <code>mailto:</code> address) where aggregate DMARC reports are sent. This additional entry uses a Cloudflare email address so that Cloudflare can receive and process DMARC reports on your behalf. Select <strong>Next</strong> to continue.</li>
</ul>
</li>
</ol>
<p>DMARC Management (beta) is now active. However, it may take up to 24 hours to receive your first DMARC report and to display this information in DMARC Management.</p>
