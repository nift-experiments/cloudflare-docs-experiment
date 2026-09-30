---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/
  description: Browse available Logpush dataset fields by category.
  full_title: Datasets · Cloudflare Logs docs
  head_html: <title>Datasets · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Browse available Logpush dataset fields by category."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/index.md"><meta property="og:title" content="Datasets · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Browse available Logpush dataset fields by category."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/#page","headline":"Datasets \u00b7 Cloudflare Logs docs","description":"Browse available Logpush dataset fields by category.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/datasets/
  schema: 1
---
<h2 id="datasets">Datasets</h2>
<p>The datasets below describe the fields available by log category:</p>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/zone/">Zone-scoped datasets</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/">Account-scoped datasets</a></li>
</ul>
<h2 id="api">API</h2>
<p>The list of fields can also be accessed directly from the API using the following endpoints:</p>
<ul>
<li>
<p>For zone-scoped datasets: <code>https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/datasets/&lt;DATASET&gt;/fields</code></p>
</li>
<li>
<p>For account-scoped datasets: <code>https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/datasets/&lt;DATASET&gt;/fields</code></p>
</li>
</ul>
<p>The <code>&lt;DATASET&gt;</code> argument indicates the log category. For example, <code>http_requests</code>, <code>spectrum_events</code>, <code>firewall_events</code>, <code>nel_reports</code>, or <code>dns_logs</code>.</p>
<h2 id="availability">Availability</h2>
<ul>
<li>The availability of Logpush dataset fields depends on your subscription plan.</li>
<li>Zone-scoped HTTP requests are available in both Logpush and Logpull.</li>
<li><a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> for HTTP requests are only available in Logpush.</li>
<li>All other datasets are only available through Logpush.</li>
</ul>
<h2 id="deprecation">Deprecation</h2>
<p>Deprecated fields remain available to prevent breaking existing jobs. They may eventually become empty values if completely removed. Customers are encouraged to migrate away from deprecated fields if they are using them.</p>
<h2 id="recommendation">Recommendation</h2>
<p>For log field <strong>ClientIPClass</strong>, Cloudflare recommends using <a href="/bots/concepts/bot-tags/">bot tags</a> to classify IPs.</p>
<h2 id="additional-resources">Additional resources</h2>
<p>For more information on logs available in Cloudflare Zero Trust, refer to <a href="/cloudflare-one/insights/logs/">Zero Trust logs</a>.</p>
