---
cp9:
  canonical: https://developers.cloudflare.com/rules/normalization/settings/
  description: Available URL normalization types and configuration settings.
  full_title: URL normalization settings · Cloudflare Rules docs
  head_html: <title>URL normalization settings · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Available URL normalization types and configuration settings."><link rel="canonical" href="https://developers.cloudflare.com/rules/normalization/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/normalization/settings/index.md"><meta property="og:title" content="URL normalization settings · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available URL normalization types and configuration settings."><meta property="og:url" content="https://developers.cloudflare.com/rules/normalization/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/normalization/settings/#page","headline":"URL normalization settings \u00b7 Cloudflare Rules docs","description":"Available URL normalization types and configuration settings.","url":"https://developers.cloudflare.com/rules/normalization/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/normalization/settings/
  schema: 1
---
<p>The Cloudflare dashboard provides the following settings to manage URL normalization:</p>
<h2 id="normalization-type">Normalization type</h2>
<p>Default value: <em>RFC-3986</em></p>
<p>Selects the type of normalization to perform:</p>
<ul>
<li><em>RFC-3986</em> – Applies URL normalization strictly according to <a href="https://datatracker.ietf.org/doc/html/rfc3986">RFC 3986</a>.</li>
<li><em>Cloudflare</em> – In addition to what is defined in RFC 3986, applies <a href="/rules/normalization/how-it-works/#cloudflare-normalization">extra URL normalization techniques</a>.</li>
</ul>
<h2 id="normalize-incoming-urls">Normalize incoming URLs</h2>
<p>Default value: <em>On</em></p>
<p>Configures the URLs of all incoming traffic to Cloudflare:</p>
<ul>
<li>When enabled, all incoming URLs are normalized before they pass to subsequent Cloudflare features that can receive a URL as input, such as Page Rules, WAF custom rules, Workers, and Access.</li>
<li>When disabled, incoming URLs are not normalized before passing to subsequent Cloudflare features.</li>
</ul>
<h2 id="normalize-urls-to-origin">Normalize URLs to origin</h2>
<p>Default value: <em>Off</em></p>
<p>Configures URLs sent to the origin:</p>
<ul>
<li>When enabled, requests sent to the origin are normalized.</li>
<li>When disabled, requests sent to the origin are not modified.</li>
</ul>
<p>You can only view and enable this option when <strong>Normalize incoming URLs</strong> is enabled.</p>
<p>For examples of how these settings affect URL normalization, refer to the <a href="/rules/normalization/examples/">URL normalization examples</a>.</p>
