---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/
  description: IDS logs in Zero Trust analytics.
  full_title: IDS logs · Cloudflare One docs
  head_html: <title>IDS logs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="IDS logs in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/index.md"><meta property="og:title" content="IDS logs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="IDS logs in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/#page","headline":"IDS logs \u00b7 Cloudflare One docs","description":"IDS logs in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/logs/logpush/ids-logs/
  schema: 1
---
<p>You can use Logpush with <a href="/cloudflare-network-firewall/about/ids/">Cloudflare Network Firewall IDS</a> (Intrusion Detection System) to export logs of detected threats. IDS monitors your network traffic for a wide range of known threat signatures, including attacks such as ransomware, data exfiltration, and network scanning.</p>
<h2 id="set-up-logpush-for-ids">Set up Logpush for IDS</h2>
<ol>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/api-configuration/#destination">Logpush Destination docs</a> to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.</p>
</li>
<li>
<p>Follow the <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> tutorial to validate your Logpush destination and define a Logpush job.</p>
</li>
</ol>
<h2 id="notes-on-using-logpush-with-ids">Notes on using Logpush with IDS</h2>
<ul>
<li>
<p>Magic IDS is an account-scoped dataset. Unlike zone-specific datasets that apply to a single domain, account-scoped datasets use a different API endpoint. Replace the string <code>/zone/&lt;ZONE_ID&gt;</code> in the Cloudflare API URLs in the tutorial with <code>/account/&lt;ACCOUNT_ID&gt;</code>.</p>
</li>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/datasets/account/magic_ids_detections/">Magic IDS Detection fields doc</a> to know what fields you want configured for the job.</p>
</li>
<li>
<p>When creating the Logpush job, the dataset field should equal <code>magic_ids_detections</code>.</p>
</li>
<li>
<p>Timestamps default to <code>unixnano</code> format (nanoseconds since the Unix epoch, January 1, 1970). If your destination expects a different format (such as RFC 3339), refer to <a href="/logs/logpush/logpush-job/api-configuration/#options">Logpush Options</a> for available timestamp formats. In the Logpush API configuration string, options are appended after the field list.</p>
</li>
</ul>
