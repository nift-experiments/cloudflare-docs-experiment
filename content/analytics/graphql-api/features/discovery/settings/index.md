---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/
  description: Query dataset-specific limits via the Settings node.
  full_title: Settings node · Cloudflare Analytics docs
  head_html: <title>Settings node · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Query dataset-specific limits via the Settings node."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/index.md"><meta property="og:title" content="Settings node · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query dataset-specific limits via the Settings node."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/#page","headline":"Settings node \u00b7 Cloudflare Analytics docs","description":"Query dataset-specific limits via the Settings node.","url":"https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/features/discovery/settings/
  schema: 1
---
<p>Cloudflare GraphQL API exposes more than 70 datasets to its customers. These
datasets represent different Cloudflare products with very different data
shapes; thus, each has its configuration of <a href="/analytics/graphql-api/limits/">limits</a>.</p>
<p>Although we allow access to ALL plans for the essential datasets (like
<code>httpRequestsAdaptiveGroups</code>, <code>firewallEventsAdaptive</code>, etc), users on larger
plans benefit from an extended set of datasets and wider query limits.</p>
<p>In addition to <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>, users can use the Settings node that is
available for both zones and accounts scopes.</p>
<h2 id="format">Format</h2>
<p><code>Settings</code> node has all datasets from <code>zones</code> and <code>accounts</code> as fields.</p>
<pre tabindex="0"><code class="language-graphql">{&#10;  viewer {&#10;    accounts(filter: { accountTag : $accountTag }) {&#10;      settings {&#10;        &#35; any dataset(s) from accounts&#10;      }&#10;    }&#10;    zones(filter: { zoneTag : $zoneTag }) {&#10;      settings {&#10;        &#35; any dataset(s) from zones&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Every subnode of <code>settings</code> node could consist of these fields:</p>
<ul>
<li><code>enabled</code> - shows whether the node is available for a requester or not;</li>
<li><code>availableFields</code> - shows the list of fields available for a requester. If
it is a nested field, the path will be returned, like <code>sum_requests</code>;</li>
<li><code>maxPageSize</code> - retrieves the maximum number of records that can be returned</li>
<li><code>maxNumberOfFields</code> - answers on how many fields could be used in a single
query for that node;</li>
<li><code>notOlderThan</code> - returns a number of seconds on how far back in time a query
can read;</li>
<li><code>maxDuration</code> - shows how wide the requested time range could be.</li>
</ul>
<h2 id="a-sample-query">A sample query</h2>
<pre tabindex="0"><code class="language-graphql">query SampleQuery($zoneTag: string) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			settings {&#10;				firewallEventsAdaptive {&#10;					enabled&#10;					maxDuration&#10;					maxNumberOfFields&#10;					maxPageSize&#10;					notOlderThan&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;data&quot;: {&#10;		&quot;viewer&quot;: {&#10;			&quot;zones&quot;: [&#10;				{&#10;					&quot;settings&quot;: {&#10;						&quot;firewallEventsAdaptive&quot;: {&#10;							&quot;enabled&quot;: true,&#10;							&quot;maxDuration&quot;: 259200,&#10;							&quot;maxNumberOfFields&quot;: 30,&#10;							&quot;maxPageSize&quot;: 10000,&#10;							&quot;notOlderThan&quot;: 2678400&#10;						}&#10;					}&#10;				}&#10;			]&#10;		}&#10;	},&#10;	&quot;errors&quot;: null&#10;}&#10;</code></pre>
<p>To get more details on how to execute queries, please refer to our how to get
started <a href="/analytics/graphql-api/getting-started/">guides</a>.</p>
