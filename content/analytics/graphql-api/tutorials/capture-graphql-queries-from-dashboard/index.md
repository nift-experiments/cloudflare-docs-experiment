---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/
  description: Capture dashboard GraphQL queries using Chrome DevTools.
  full_title: Capture GraphQL queries with Chrome DevTools · Cloudflare Analytics docs
  head_html: <title>Capture GraphQL queries with Chrome DevTools · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Capture dashboard GraphQL queries using Chrome DevTools."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/index.md"><meta property="og:title" content="Capture GraphQL queries with Chrome DevTools · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Capture dashboard GraphQL queries using Chrome DevTools."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/#page","headline":"Capture GraphQL queries with Chrome DevTools \u00b7 Cloudflare Analytics docs","description":"Capture dashboard GraphQL queries using Chrome DevTools.","url":"https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/
  schema: 1
---
<p>Using <a href="https://developer.chrome.com/docs/devtools">Chrome DevTools</a>, you can capture the queries running behind the Cloudflare Dashboard analytics. In this example, we will focus on the Network Analytics dataset, but the same process can be applied to any other analytics available in your dashboard.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Network Analytics</strong> page or any other analytics dashboard you are interested in seeing the GraphQL queries in.</li>
</ol>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/analytics/analytics-tab.png" alt="Analytics tab" /></p>
<ol start="2">
<li>Open the <a href="https://developer.chrome.com/docs/devtools">Chrome Developer Tools</a> and select <strong>Inspect</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/chrome-developer-tools.png" alt="Chrome developer tools" /></p>
<ol start="3">
<li>Select the <strong>Network</strong> tab in the Developer Tools panel.</li>
<li>In the filter bar, type <code>graphql</code> to filter out the GraphQL requests. If no requests appear, try reloading the page. As the page reloads, several network requests will populate the <strong>Network</strong> tab. Look for requests that contain <code>graphql</code> in the name.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/search-field.png" alt="Type graphql in the search field" /></p>
<ol start="5">
<li>Select one of the GraphQL requests to open its details and go to the <strong>Payload</strong> tab. There you will find the GraphQL query. Select the query line and then <strong>Copy value</strong> to capture the query.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/copy-value.png" alt="Copy query value" /></p>
<ol start="6">
<li>If you want to capture a new query, adjust the filters in the <strong>Network analytics</strong> dashboard and a new query will appear in the GraphQL requests.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/new-query.png" alt="Create a new query" /></p>
<p>You can now use this query as the basis for your API call. Refer to the <a href="/analytics/graphql-api/getting-started/">Get started</a> section for more information.</p>
