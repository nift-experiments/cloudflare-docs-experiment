---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/company-security/device-security/
  description: Verify device posture before granting access.
  full_title: Ensure device endpoint security · Cloudflare use cases
  head_html: <title>Ensure device endpoint security · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Verify device posture before granting access."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/company-security/device-security/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/company-security/device-security/index.md"><meta property="og:title" content="Ensure device endpoint security · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify device posture before granting access."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/company-security/device-security/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Cloudflare One,WARP Client"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/company-security/device-security/#page","headline":"Ensure device endpoint security \u00b7 Cloudflare use cases","description":"Verify device posture before granting access.","url":"https://developers.cloudflare.com/use-cases/company-security/device-security/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/company-security/device-security/
  schema: 1
---
<p>Granting access to corporate applications without verifying device health creates risk. Cloudflare One checks OS version, disk encryption, and antivirus status before allowing a device to connect, and integrates with CrowdStrike, SentinelOne, and other Endpoint Detection and Response (EDR) tools.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="cloudflare-one">Cloudflare One</h3>
<p>Secure your organization with a cloud security platform that replaces legacy perimeters with Cloudflare's global network. <a href="/cloudflare-one/">Learn more about Cloudflare One</a>.</p>
<ul>
<li><strong>Posture checks</strong> - Verify OS version, disk encryption status, and antivirus presence before granting access</li>
<li><strong>Endpoint integration</strong> - Pull real-time device health signals from CrowdStrike, SentinelOne, and other Endpoint Detection and Response (EDR) tools</li>
<li><strong>Conditional access</strong> - Gate application access on device posture results, so only healthy devices can connect</li>
</ul>
<h3 id="cloudflare-one-client">Cloudflare One client</h3>
<p>Device agent that routes traffic through Cloudflare's network. <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Learn more about Cloudflare One client</a>.</p>
<ul>
<li><strong>Always-on protection</strong> - Route device traffic through Cloudflare One at all times, enforcing Gateway policies regardless of network</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Deploy the Cloudflare One client</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/">Configure device posture checks</a></li>
<li><a href="/cloudflare-one/access-controls/policies/">Add posture checks to Access policies</a></li>
</ol>
