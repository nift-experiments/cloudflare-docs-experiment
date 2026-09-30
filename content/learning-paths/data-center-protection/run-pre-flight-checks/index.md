---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/
  description: Verify readiness before Magic Transit activation.
  full_title: Run pre-flight checks · Cloudflare Learning Paths
  head_html: <title>Run pre-flight checks · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Verify readiness before Magic Transit activation."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/index.md"><meta property="og:title" content="Run pre-flight checks · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify readiness before Magic Transit activation."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Magic Transit,DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/#page","headline":"Run pre-flight checks \u00b7 Cloudflare Learning Paths","description":"Verify readiness before Magic Transit activation.","url":"https://developers.cloudflare.com/learning-paths/data-center-protection/run-pre-flight-checks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/data-center-protection/run-pre-flight-checks/
  schema: 1
---
<p>After setting up your Magic Transit product, Cloudflare validates:</p>
<ul>
<li>Tunnel connectivity</li>
<li>Tunnel and endpoint <a href="/magic-transit/reference/tunnel-health-checks/#types-of-health-checks">health checks</a></li>
<li>Letter of Agency (LOA)</li>
<li>Internet Routing Registry (IRR)</li>
<li>Maximum segment size (MSS) configurations.</li>
</ul>
<p>Refer to <a href="/learning-paths/data-center-protection/get-started/">Get started</a> for information about the above topics.</p>
<p>Configurations for Cloudflare global network are applied and take around one day to rollout.</p>
<p>On your side, you should do the following:</p>
<ul>
<li>Confirm that your upstream ISPs do not have <a href="/byoip/troubleshooting/#urpf-filtering-and-packet-loss">uRPF</a> strict-mode enabled. If they do, ask them to change this setting to uRPF loose mode. Having strict-mode uRPF will result in packet loss when you advertise your prefix from Cloudflare and withdraw your prefix advertisement from your ISP.</li>
<li>Confirm you have adjusted MSS/MTU value on any IPsec or GRE tunnels with third parties that are configured on your Magic Transit prefix.</li>
<li>If you are using BGP for Magic Transit prefix advertisement, configure your own alerts/logs for the BGP peerings with Cloudflare route reflectors. Cloudflare will not notify you if these peerings go down, so you should enable this on your equipment using syslog or other event-alerting tools.</li>
</ul>
