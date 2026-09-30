---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/
  description: Enable Pay Per Crawl in your account settings.
  full_title: Enable in account settings · Cloudflare AI Crawl Control docs
  head_html: <title>Enable in account settings · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable Pay Per Crawl in your account settings."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/index.md"><meta property="og:title" content="Enable in account settings · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable Pay Per Crawl in your account settings."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/#page","headline":"Enable in account settings \u00b7 Cloudflare AI Crawl Control docs","description":"Enable Pay Per Crawl in your account settings.","url":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/
  schema: 1
---
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;A[Enable in&lt;br&gt;account settings]:::highlight --&gt; B[Set a pay per &lt;br/&gt;crawl price ]&#10;B --&gt; C[Select crawlers&lt;br&gt;to charge]&#10;C --&gt; D[Monitor&lt;br&gt;activity]&#10;D --&gt; E[Manage&lt;br&gt;payouts]&#10;classDef highlight fill:#F6821F,color:white&#10;&#10;click B &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/&quot;&#10;click C &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/&quot;&#10;click D &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/&quot;&#10;click E &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/&quot;&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>To configure pay per crawl, you must have the following:</p>
<ul>
<li><strong>Cloudflare account</strong>: You need an active Cloudflare account with domains added</li>
<li><strong>Domain on Cloudflare</strong>: Your domain must be using Cloudflare's nameservers, or have DNS records managed by Cloudflare</li>
<li><strong>Administrator access</strong>: You need Administrator or Super Administrator permissions for account-level configuration</li>
</ul>
<h2 id="configure-domain-access">Configure domain access</h2>
<p>An Administrator or Super Administrator with access to all domains must select which domains should show the pay per crawl controls:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2765.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="visibility-vs-security">Visibility vs Security</h3>
@markup("md", "content/.markup/bodies/2764.md")
</aside>
<p>After completing these steps, domain administrators can set a pay per crawl price and enable pay per crawl for their specific domains.</p>
