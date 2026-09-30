---
cp9:
  canonical: https://developers.cloudflare.com/argo-smart-routing/analytics/
  description: View latency improvements and response time data for Argo Smart Routing.
  full_title: Analytics · Cloudflare Argo Smart Routing docs
  head_html: <title>Analytics · Cloudflare Argo Smart Routing docs</title><meta name="generator" content="Nift"><meta name="description" content="View latency improvements and response time data for Argo Smart Routing."><link rel="canonical" href="https://developers.cloudflare.com/argo-smart-routing/analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/argo-smart-routing/analytics/index.md"><meta property="og:title" content="Analytics · Cloudflare Argo Smart Routing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View latency improvements and response time data for Argo Smart Routing."><meta property="og:url" content="https://developers.cloudflare.com/argo-smart-routing/analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Argo Smart Routing"><meta name="algolia_product_filter" content="Argo Smart Routing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Argo Smart Routing"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/argo-smart-routing/analytics/#page","headline":"Analytics \u00b7 Cloudflare Argo Smart Routing docs","description":"View latency improvements and response time data for Argo Smart Routing.","url":"https://developers.cloudflare.com/argo-smart-routing/analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /argo-smart-routing/analytics/
  schema: 1
---
<p>Cloudflare provides analytics to show the performance benefits of Argo Smart Routing.</p>
<p>You can access Argo analytics for your domain in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> at <strong>Analytics</strong> &gt; <strong>Performance</strong>. For information on all analytics in the dashboard, refer to <a href="/analytics/">Analytics</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>Analytics collects data based on the time-to-first-byte (TTFB) from your origin to the Cloudflare network. TTFB is the delay between when Cloudflare sends a request to your server and when it receives the first byte in response. Argo Smart Routing optimizes your server's network transit time to minimize this delay.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1527.md")
</aside>
<h2 id="types-of-analytics">Types of analytics</h2>
<p>The dashboard displays two different views for performance data:</p>
<ul>
<li>
<p><strong>Origin Response Time</strong>: A histogram shows response time from your origin to the Cloudflare network. The blue bars show time-to-first-byte (TTFB) without Argo, while the orange bars show TTFB where Argo found a Smart Route.</p>
</li>
<li>
<p><strong>Geography</strong>: A map shows the improvement in response time at each Cloudflare data center.</p>
<ul>
<li>A negative value indicates that requests from that location would not have benefited from Argo Smart Routing, so instead would have been routed directly.</li>
</ul>
</li>
</ul>
