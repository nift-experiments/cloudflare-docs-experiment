---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/
  description: Send IDS events to Logpush destinations.
  full_title: Use Logpush with IDS · Cloudflare Network Firewall docs
  head_html: <title>Use Logpush with IDS · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Send IDS events to Logpush destinations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/index.md"><meta property="og:title" content="Use Logpush with IDS · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send IDS events to Logpush destinations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/#page","headline":"Use Logpush with IDS \u00b7 Cloudflare Network Firewall docs","description":"Send IDS events to Logpush destinations.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/how-to/use-logpush-with-ids/
  schema: 1
---
<p>You can use Logpush with Cloudflare Network Firewall (formerly Magic Firewall) IDS to log detected risks:</p>
<ol>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/api-configuration/#destination">Logpush Destination docs</a> to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.</p>
</li>
<li>
<p>Follow the <a href="/logs/logpush/examples/example-logpush-curl/">Manage Lopush with cURL</a> tutorial to validate your Logpush destination and define a Logpush job.</p>
</li>
</ol>
<h2 id="notes-on-using-logpush-with-ids">Notes on using Logpush with IDS</h2>
<ul>
<li>
<p>Magic IDS is an account-scoped dataset. This means the string <code>/zone/&lt;ZONE_ID&gt;</code> in the Cloudflare API URLs in the tutorial should be replaced with <code>/account/&lt;ACCOUNT_ID&gt;</code>.</p>
</li>
<li>
<p>Consult the <a href="/logs/logpush/logpush-job/datasets/account/magic_ids_detections/">Magic IDS Detection fields doc</a> to know what fields you want configured for the job.</p>
</li>
<li>
<p>When creating the Logpush job, the dataset field should equal <code>magic_ids_detections</code>.</p>
</li>
<li>
<p>Timestamps by default are unixnano. Consult the <a href="/logs/logpush/logpush-job/api-configuration/#options">Logpush Options docs</a> to learn what format you can choose that will be compatible with your destination and/or expectations. Note that all options must be added <em>after</em> all fields you want from the Logpush job, akin to URL parameters.</p>
</li>
</ul>
