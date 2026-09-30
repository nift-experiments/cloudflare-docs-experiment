---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/
  description: Use the GraphQL Analytics API to retrieve Network Flow data.
  full_title: GraphQL Analytics · Cloudflare Network Flow docs
  head_html: <title>GraphQL Analytics · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the GraphQL Analytics API to retrieve Network Flow data."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/index.md"><meta property="og:title" content="GraphQL Analytics · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the GraphQL Analytics API to retrieve Network Flow data."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Network Flow"><meta name="pcx_tags" content="GraphQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/#page","headline":"GraphQL Analytics \u00b7 Cloudflare Network Flow docs","description":"Use the GraphQL Analytics API to retrieve Network Flow data.","url":"https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL"]}</script>
  markdown: true
  noindex: false
  route: /network-flow/tutorials/graphql-analytics/
  schema: 1
---
<p>Use the GraphQL Analytics API to retrieve Network Flow (formerly Magic Network Monitoring) <span class="nb-glossary-tooltip" title="flow data">flow data</span>.</p>
<p>Before you begin, you must have an <a href="/analytics/graphql-api/getting-started/authentication/">API token</a>. For additional help getting started with GraphQL Analytics, refer to <a href="/analytics/graphql-api/">GraphQL Analytics API</a>.</p>
<h3 id="obtain-your-cloudflare-account-id">Obtain your Cloudflare Account ID</h3>
<p>To query Network Flow data via GraphQL, you need your Cloudflare Account ID.</p>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>The URL in your browser's address bar should show <code>https://dash.cloudflare.com/</code> followed by a hex string. The hex string is your Cloudflare Account ID.</li>
</ol>
<h2 id="explore-graphql-schema-with-network-flow-example">Explore GraphQL schema with Network Flow example</h2>
<p>Run a test query to retrieve bits and packets aggregated in five-minute intervals. Copy and paste the following code into GraphiQL.</p>
<p>For additional information about the Analytics schema, refer to <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">Explore the Analytics schema with GraphiQL</a>.</p>
<pre tabindex="0"><code class="language-graphql">query MagicNetworkMonitoring($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			mnmFlowDataAdaptiveGroups(&#10;				filter: { datetime_gt: $start, datetime_leq: $end }&#10;				limit: 10&#10;				orderBy: [datetimeFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					datetimeFiveMinutes&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10800.md")
</aside>
