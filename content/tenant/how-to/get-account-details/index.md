---
cp9:
  canonical: https://developers.cloudflare.com/tenant/how-to/get-account-details/
  description: Retrieve account information for tenant-managed Cloudflare accounts using the API.
  full_title: Get account details · Cloudflare Tenant docs
  head_html: <title>Get account details · Cloudflare Tenant docs</title><meta name="generator" content="Nift"><meta name="description" content="Retrieve account information for tenant-managed Cloudflare accounts using the API."><link rel="canonical" href="https://developers.cloudflare.com/tenant/how-to/get-account-details/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tenant/how-to/get-account-details/index.md"><meta property="og:title" content="Get account details · Cloudflare Tenant docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Retrieve account information for tenant-managed Cloudflare accounts using the API."><meta property="og:url" content="https://developers.cloudflare.com/tenant/how-to/get-account-details/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Tenant"><meta name="algolia_product_filter" content="Tenant"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Tenant"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tenant/how-to/get-account-details/#page","headline":"Get account details \u00b7 Cloudflare Tenant docs","description":"Retrieve account information for tenant-managed Cloudflare accounts using the API.","url":"https://developers.cloudflare.com/tenant/how-to/get-account-details/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /tenant/how-to/get-account-details/
  schema: 1
---
<p>An <a href="/tenant/glossary/#account"><strong>Account</strong></a> will contain various settings, resources, and subscriptions to products for users. Each Tenant can have multiple associated accounts.</p>
<p>To retrieve a list of accounts associated with a Tenant details, send a <code>GET</code> request to the <code>/tenants/{tenant_id}/accounts</code> endpoint. You can find the Tenant tag and all Tenants associated with the user with the <a href="/tenant/how-to/get-tenant-details/"><strong>Tenant Details</strong></a> API. The Tenant Accounts API also requires pagination passed as query parameters:</p>
<ul>
<li>
<p><code>page</code> number</p>
<ul>
<li>Page number of accounts list response, indexed from 1</li>
</ul>
</li>
<li>
<p><code>per_page</code> number</p>
<ul>
<li>Number of accounts to display per page</li>
</ul>
</li>
<li>
<p><code>order</code> string</p>
<ul>
<li>
<p>(optional) Order by a specific column, has to be a valid top-level key from the response</p>
</li>
<li>
<p><code>direction</code> number</p>
<ul>
<li>(optional) 0 for ascending or 1 for descending, is 0 by default</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/tenants/{tenant_id}/accounts?page=1&amp;per_page=10&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>A successful request will return an HTTP status of <code>200</code> and a response body containing account information and feature flags for all accounts managed by the Tenant.</p>
