---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/
  description: Learn about configure graphql client endpoint and http headers in Cloudflare analytics.
  full_title: Configure GraphQL client endpoint and HTTP headers · Cloudflare Analytics docs
  head_html: <title>Configure GraphQL client endpoint and HTTP headers · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about configure graphql client endpoint and http headers in Cloudflare analytics."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/index.md"><meta property="og:title" content="Configure GraphQL client endpoint and HTTP headers · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about configure graphql client endpoint and http headers in Cloudflare analytics."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/#page","headline":"Configure GraphQL client endpoint and HTTP headers \u00b7 Cloudflare Analytics docs","description":"Learn about configure graphql client endpoint and http headers in Cloudflare analytics.","url":"https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/getting-started/authentication/graphql-client-headers/
  schema: 1
---
<ol>
<li>
<p>Launch <a href="https://www.gatsbyjs.com/docs/how-to/querying-data/running-queries-with-graphiql/">GraphiQL</a>.</p>
</li>
<li>
<p>Select <strong>Edit HTTP Headers</strong>.
<img src="/assets/upstream/images/analytics/GraphiQL-edit-http-headers.png" alt="Clicking Edit HTTP Headers" />
The <strong>Edit HTTP Headers</strong> window appears.
<img src="/assets/upstream/images/analytics/GraphiQL-edit-http-headers-window.png" alt="Editing HTTP Headers Window" /></p>
</li>
<li>
<p>Select <strong>Add Header</strong> to configure authentication. You can use Cloudflare Analytics API token authentication (recommended) or Cloudflare API key authentication.</p>
<ul>
<li>
<p><strong>Token authentication</strong>:</p>
<p>Enter <strong>Authorization</strong> in the <strong>Header Name</strong> field, and enter <code>Bearer {your-analytics-token}</code> in the <strong>Header value</strong> field, then select <strong>Save</strong>.</p>
</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/analytics/GraphiQL-edit-http-headers-token.png" alt="Editing HTTP Headers" /></p>
<ul>
<li>
<p><strong>Key authentication</strong>:</p>
<p>Enter <code>X-AUTH-EMAIL</code> in the <strong>Header name</strong> field and your email address registered with Cloudflare in the <strong>Header value</strong> field, and select <strong>Save</strong>.<br/></p>
<p>Select <strong>Add Header</strong> to add a second header. Enter <code>X-AUTH-KEY</code> in the <strong>Header Name</strong> field, and paste your Global API Key in the <strong>Header value</strong> field, then select <strong>Save</strong>.<br/></p>
</li>
</ul>
<ol start="4">
<li>
<p>Select anywhere outside the <strong>Edit HTTP Headers</strong> window in GraphiQL to close it and return to the main GraphiQL display.</p>
</li>
<li>
<p>Enter <code>https://api.cloudflare.com/client/v4/graphql</code> in the <strong>GraphQL Endpoint</strong> field.
<img src="/assets/upstream/images/analytics/GraphiQL-response-pane.png" alt="Editing GraphQL Endpoint" /></p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3176.md")
</aside>
<p>Now that you have configured authentication, you are ready to run queries using GraphiQL.</p>
