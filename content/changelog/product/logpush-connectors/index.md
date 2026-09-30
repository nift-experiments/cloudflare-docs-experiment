---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/logpush-connectors/
  description: '2026-08-26'
  full_title: logpush-connectors changelog | Cloudflare Docs
  head_html: <title>logpush-connectors changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-26"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/logpush-connectors/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="logpush-connectors changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-26"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/logpush-connectors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/logpush-connectors/#page","headline":"logpush-connectors changelog | Cloudflare Docs","description":"2026-08-26","url":"https://developers.cloudflare.com/changelog/product/logpush-connectors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/logpush-connectors/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="azure-functions-based-microsoft-sentinel-connector-deprecation"><a href="/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/">Azure Functions-based Microsoft Sentinel connector deprecation</a></h2>
<p><em>2026-08-26</em></p>
<p>Cloudflare Enterprise customers using the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview">Azure Functions-based Microsoft Sentinel connector</a> must migrate to the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector</a> by 2026-09-14.</p>
<p>Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.</p>
<p>To migrate, follow the <a href="/analytics/analytics-integrations/sentinel/">Microsoft Sentinel integration setup guide</a>.</p>
<h4 id="2026-08-26-sentinel-functions-connector-deprecation-additional-resources">Additional resources</h4>
<ul>
<li><a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Download Cloudflare's CCF Sentinel Solution</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview">Microsoft Sentinel data lake overview</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector">About the CCF platform</a></li>
</ul>
<p>For more information, refer to Microsoft's <a href="https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell">Azure Monitor HTTP Data Collector API deprecation notice</a>.</p>



