---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/limits/
  description: Review GraphQL Analytics API query limits.
  full_title: GraphQL API - Limits · Cloudflare Analytics docs
  head_html: <title>GraphQL API - Limits · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Review GraphQL Analytics API query limits."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/limits/index.md"><meta property="og:title" content="GraphQL API - Limits · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review GraphQL Analytics API query limits."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/limits/#page","headline":"GraphQL API - Limits \u00b7 Cloudflare Analytics docs","description":"Review GraphQL Analytics API query limits.","url":"https://developers.cloudflare.com/analytics/graphql-api/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/limits/
  schema: 1
---
<p>Cloudflare GraphQL API exposes more than 70 datasets representing products with
different configurations and data availability for different zones and accounts
plans.</p>
<p>To support this variety of products, Cloudflare GraphQL API has three layers of
limits:</p>
<ul>
<li>global limits</li>
<li>user limits</li>
<li>node (dataset) limits</li>
</ul>
<h2 id="global-limits">Global limits</h2>
<p>These limits are applied to every query for every plan:</p>
<ul>
<li>A zone-scoped query can include up to <strong>10 zones</strong></li>
<li>An account-scoped query can include only <strong>1 account</strong></li>
</ul>
<p>Additionally, there is a limited number of queries you can make per request. The total number of queries in a request is equal to the number of zone/account scopes, multiplied by the number of nodes to which they are applied.</p>
<h2 id="user-limits">User limits</h2>
<p>Cloudflare GraphQL API limits the number of GraphQL requests each user can send.
The default quota is <strong>300 GraphQL queries over 5-minute window</strong>. It allows a
user to run at least <strong>1 query every second</strong> or do a burst of 300 queries and
then wait 5 minutes before issuing another query.</p>
<p>That rate limit is applied in addition to the <a href="/fundamentals/api/reference/limits/">general rate limits enforced by
the Cloudflare API</a>.</p>
<h3 id="account-based-rate-limiting">Account-based rate limiting</h3>
<p>If you query analytics across many zones or accounts, you can opt into
<strong>account-based rate limiting</strong>, where limits apply per account and per zone
instead of per user or API token. Because each account and zone has its own
budget, a single user or token can make far more requests overall, and limit
increases can be applied per resource and take effect quickly.</p>
<p>To learn how to enable it and the query requirements, refer to
<a href="/analytics/graphql-api/account-based-rate-limiting/">Account-based rate limiting</a>.</p>
<h2 id="node-limits-and-availability">Node limits and availability</h2>
<p>Each data node has its limits, such as:</p>
<ul>
<li>how far back in time can data be requested,</li>
<li>the maximum time period (in seconds) that can be requested in one query,</li>
<li>the maximum number of fields that can be requested in one query,</li>
<li>the maximum number of records that can be returned in one query.</li>
</ul>
<p>Node limits are tied to requested <code>zoneTag</code> or <code>accountTag</code>. Higher plans have
access to a greater selection of datasets or fields, and can query over broader historical
intervals.</p>
<p>To get exact boundaries and availability for your zone(s) or account, please
refer to <a href="/analytics/graphql-api/features/discovery/settings/">settings</a>.</p>
