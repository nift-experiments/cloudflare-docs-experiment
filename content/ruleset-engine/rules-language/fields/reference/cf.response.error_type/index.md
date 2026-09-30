---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/
  description: A string with the type of error in the response being returned.
  full_title: cf.response.error_type · Cloudflare Ruleset Engine docs
  head_html: <title>cf.response.error_type · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="A string with the type of error in the response being returned."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cf.response.error_type · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A string with the type of error in the response being returned."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/#page","headline":"cf.response.error_type \u00b7 Cloudflare Ruleset Engine docs","description":"A string with the type of error in the response being returned.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.response.error_type/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/cf.response.error_type/
  schema: 1
---
<h1 id="cf-response-error-type">cf.response.error_type</h1>

**Data type:** String

<p>A string with the type of error in the response being returned.</p>

<p>The default value is an empty string (<code>&quot;&quot;</code>).</p>
<p>The available values are the following:</p>
<ul>
<li><code>&quot;managed_challenge&quot;</code></li>
<li><code>&quot;iuam&quot;</code></li>
<li><code>&quot;legacy_challenge&quot;</code></li>
<li><code>&quot;ip_ban&quot;</code></li>
<li><code>&quot;waf&quot;</code></li>
<li><code>&quot;5xx&quot;</code></li>
<li><code>&quot;1xxx&quot;</code></li>
<li><code>&quot;always_online&quot;</code></li>
<li><code>&quot;country_challenge&quot;</code></li>
<li><code>&quot;ratelimit&quot;</code></li>
</ul>
<p>You can use this field to customize the response for a specific type of error (for example, all 1XXX errors or all WAF block actions).</p>
<p><strong>Note</strong>: This field is only available in <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> and <a href="/rules/custom-errors/">Custom Errors</a>.</p>

<h2 id="categories">Categories</h2>

- Response

**Keywords:** response, cloudflare

