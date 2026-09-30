---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/
  description: Limit Cloudflare API token usage by client IP address filtering and time-to-live (TTL) constraints.
  full_title: Restrict tokens · Cloudflare Fundamentals docs
  head_html: <title>Restrict tokens · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Limit Cloudflare API token usage by client IP address filtering and time-to-live (TTL) constraints."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/index.md"><meta property="og:title" content="Restrict tokens · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Limit Cloudflare API token usage by client IP address filtering and time-to-live (TTL) constraints."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/#page","headline":"Restrict tokens \u00b7 Cloudflare Fundamentals docs","description":"Limit Cloudflare API token usage by client IP address filtering and time-to-live (TTL) constraints.","url":"https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/how-to/restrict-tokens/
  schema: 1
---
<p>API tokens can be restricted at runtime in two ways:</p>
<ul>
<li><a href="#client-ip-address-range-filtering">Client IP address range filtering</a></li>
<li><a href="#time-to-live-ttl-constraints">Time To Live (TTL) constraints</a></li>
</ul>
<h2 id="client-ip-address-range-filtering">Client IP address range filtering</h2>
<p>Client IP address restrictions control which IP addresses can make API requests with this token. By default, if no filtering is applied, all IP addresses can use the token. Once an <code>Is in</code> rule is applied, the token can only be used from the defined IP addresses. Define ranges with <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation">CIDR notation</a>. To allow an IP range with exceptions, define <code>Is not in</code> to exempt specific IPs or smaller ranges.</p>
<p><img src="/assets/upstream/images/fundamentals/api/ip-filter.png" alt="IP Address filtering options" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8978.md")
</aside>
<h2 id="time-to-live-ttl-constraints">Time to live (TTL) constraints</h2>
<p>By default, tokens do not expire and are long lived. Defining a TTL sets when a token starts being valid and when a token is no longer valid. This is often referred to as <code>notBefore</code> and <code>notAfter</code>. Setting these timestamps limits the lifetime of the token to the defined period. Not setting the start date or <code>notBefore</code> means the token is active as soon as it is created. Not setting the end date or <code>notAfter</code> means the token does not expire.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8977.md")
</aside>
<p><img src="/assets/upstream/images/fundamentals/api/ttl.png" alt="Time to Live selection calendar" /></p>
