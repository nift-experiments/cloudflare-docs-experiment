---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/
  description: Block Microsoft Exchange Autodiscover requests.
  full_title: Block Microsoft Exchange Autodiscover requests · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Block Microsoft Exchange Autodiscover requests · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Block Microsoft Exchange Autodiscover requests."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/index.md"><meta property="og:title" content="Block Microsoft Exchange Autodiscover requests · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block Microsoft Exchange Autodiscover requests."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Microsoft"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/#page","headline":"Block Microsoft Exchange Autodiscover requests \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Block Microsoft Exchange Autodiscover requests.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft"]}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/block-ms-exchange-autodiscover/
  schema: 1
---
<p>In some cases, Microsoft Exchange Autodiscover service requests can be &quot;noisy&quot;, triggering large numbers of <code>HTTP 404</code> (<code>Not found</code>) errors.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests for <code>autodiscover.xml</code> and <code>autodiscover.src</code>:</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>(ends_with(http.request.uri.path, &quot;/autodiscover.xml&quot;) or ends_with(http.request.uri.path, &quot;/autodiscover.src&quot;))</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<p>Alternatively, customers on a Business or Enterprise plan can use the <code>matches</code> <a href="/ruleset-engine/rules-language/operators/#comparison-operators">comparison operator</a> for the same purpose. For this example, the expression would be the following:</p>
<pre tabindex="0"><code class="language-txt">(http.request.uri.path matches &quot;/autodiscover.(xml|src)$&quot;)&#10;</code></pre>
