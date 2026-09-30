---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/
  description: Authenticate requests to the GraphQL Analytics API.
  full_title: Authentication · Cloudflare Analytics docs
  head_html: <title>Authentication · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Authenticate requests to the GraphQL Analytics API."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/index.md"><meta property="og:title" content="Authentication · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Authenticate requests to the GraphQL Analytics API."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/#page","headline":"Authentication \u00b7 Cloudflare Analytics docs","description":"Authenticate requests to the GraphQL Analytics API.","url":"https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/getting-started/authentication/
  schema: 1
---
<p>Cloudflare separates service configuration by zone. When there are multiple accounts, each with many zones, it is important to restrict GraphQL Analytics API access to only those account and zone resources that are relevant for the task at hand.</p>
<p>To secure access to your GraphQL Analytics data, use a Cloudflare API key or token to authenticate an API request.</p>
<p>This table outlines the differences between Cloudflare API keys and tokens:</p>
<table>
<thead>
<tr>
<th>Authentication Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href='/fundamentals/api/get-started/create-token/'>API Tokens</a></td>
<td>Cloudflare recommends API Tokens as the preferred way to interact with Cloudflare APIs. You can configure the scope of tokens to limit access to account and zone resources, and you can define the Cloudflare APIs to which the token authorizes access.</td>
</tr>
<tr>
<td><a href='/fundamentals/api/get-started/keys/'>API Keys</a></td>
<td><p>Unique to each Cloudflare user and used only for authentication. API keys do not authorize access to accounts or zones.</p>
        <p>Use the Global API Key for authentication.</p></td>
</tr>
</tbody>
</table>
<p>To create and configure GraphQL Analytics API tokens, refer to <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Configure an Analytics API token</a>.</p>
<p>To find and retrieve API keys, as well as edit HTTP headers for authentication in GraphiQL, refer to <a href="/analytics/graphql-api/getting-started/authentication/api-key-auth/">Authenticate with a Cloudflare API key</a>.</p>
