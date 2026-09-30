---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/
  description: Understand email threat disposition categories.
  full_title: Email dispositions · Cloudflare Learning Paths
  head_html: <title>Email dispositions · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Understand email threat disposition categories."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/index.md"><meta property="og:title" content="Email dispositions · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand email threat disposition categories."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/#page","headline":"Email dispositions \u00b7 Cloudflare Learning Paths","description":"Understand email threat disposition categories.","url":"https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-your-email/enable-auto-moves/email-dispositions/
  schema: 1
---
<p>Email security returns five potential verdicts for every email it scans. Review the detections and consider how you would treat them once an auto-move is enabled. Below is an overview of the disposition and recommendation actions by Cloudflare:</p>
<table>
<thead>
<tr>
<th>Disposition</th>
<th>Description</th>
<th>Recommendation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>MALICIOUS</td>
<td>Traffic invoked multiple phishing verdict triggers, met thresholds for bad behavior, and is associated with active campaigns.</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>SUSPICIOUS</td>
<td>Traffic associated with phishing campaigns (and is under further analysis by our automated systems).</td>
<td>Research these messages internally to evaluate legitimacy.</td>
<td></td>
</tr>
<tr>
<td>SPOOF</td>
<td>Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies (<a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/">SPF</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/">DKIM</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>), or have mismatching Envelope From and Header From values.</td>
<td>Block after investigating (can be triggered by third-party mail services).</td>
<td></td>
</tr>
<tr>
<td>SPAM</td>
<td>Traffic associated with non-malicious, commercial campaigns.</td>
<td>Route to existing Spam quarantine folder.</td>
<td></td>
</tr>
<tr>
<td>BULK</td>
<td>Traffic associated with <a href="https://en.wikipedia.org/wiki/Graymail">Graymail</a>, that falls in between the definitions of SPAM and SUSPICIOUS. For example, a marketing email that intentionally obscures its unsubscribe link.</td>
<td>Monitor or tag</td>
<td></td>
</tr>
</tbody>
</table>
