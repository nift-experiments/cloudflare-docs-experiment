---
cp9:
  canonical: https://developers.cloudflare.com/dmarc-management/statistics/
  description: Review whether emails sent on your behalf passed DMARC, SPF, and DKIM checks.
  full_title: Review DMARC statistics · Cloudflare DMARC Management docs
  head_html: <title>Review DMARC statistics · Cloudflare DMARC Management docs</title><meta name="generator" content="Nift"><meta name="description" content="Review whether emails sent on your behalf passed DMARC, SPF, and DKIM checks."><link rel="canonical" href="https://developers.cloudflare.com/dmarc-management/statistics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dmarc-management/statistics/index.md"><meta property="og:title" content="Review DMARC statistics · Cloudflare DMARC Management docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review whether emails sent on your behalf passed DMARC, SPF, and DKIM checks."><meta property="og:url" content="https://developers.cloudflare.com/dmarc-management/statistics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DMARC Management"><meta name="algolia_product_filter" content="DMARC Management"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DMARC Management"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dmarc-management/statistics/#page","headline":"Review DMARC statistics \u00b7 Cloudflare DMARC Management docs","description":"Review whether emails sent on your behalf passed DMARC, SPF, and DKIM checks.","url":"https://developers.cloudflare.com/dmarc-management/statistics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /dmarc-management/statistics/
  schema: 1
---
<p>DMARC Management (beta) allows you to review whether emails sent on your behalf passed or failed DMARC, SPF, and DKIM authentication checks.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email</strong> &gt; <strong>DMARC Management</strong>.</li>
<li>The graph shows the volume of emails over a selected time period. Use the dropdown to select a period of up to 30 days.</li>
<li>Moving your mouse through the graph gives you details for a particular day. Select <strong>View reports</strong> for a list of DMARC reports by date.</li>
<li>Select one of the dates shown to open a window with more details.</li>
</ol>
<h2 id="source-details">Source details</h2>
<p>The Top 10 sources section shows you details about the top sources sending emails on your behalf, with information such as total volume of emails and how these sources fared regarding security policies.</p>
<p>You also have access to information about all third parties, and can drill down for further details on each of them:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email</strong> &gt; <strong>DMARC Management</strong>.</li>
<li>Select <strong>View all</strong>.</li>
<li>The next page shows you a list of all sources sending email on your behalf. You can filter this list by time period.</li>
<li>Find a source you want to inspect further, and select the three dots in front of it &gt; <strong>Details</strong> to learn more about that third party.</li>
</ol>
