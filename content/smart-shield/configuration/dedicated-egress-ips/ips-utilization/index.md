---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/
  description: Monitor dedicated egress IP capacity and concurrent connections with GraphQL.
  full_title: IPs utilization · Cloudflare Smart Shield docs
  head_html: <title>IPs utilization · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor dedicated egress IP capacity and concurrent connections with GraphQL."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/index.md"><meta property="og:title" content="IPs utilization · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor dedicated egress IP capacity and concurrent connections with GraphQL."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Smart Shield"><meta name="pcx_tags" content="GraphQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/#page","headline":"IPs utilization \u00b7 Cloudflare Smart Shield docs","description":"Monitor dedicated egress IP capacity and concurrent connections with GraphQL.","url":"https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/ips-utilization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL"]}</script>
  markdown: true
  noindex: false
  route: /smart-shield/configuration/dedicated-egress-ips/ips-utilization/
  schema: 1
---
<p>Use the <a href="/analytics/graphql-api/">GraphQL API</a> to get aggregate data and monitor your dedicated IPs capacity (formerly known as Aegis).</p>
<p>Each Dedicated CDN Egress IP can support 40,000 concurrent connections per origin IP port. For example, if you have one dedicated IP and two origins (A and B), this single IP can support 40,000 concurrent connections to origin A, while simultaneously supporting 40,000 concurrent connections to origin B.</p>
<p>Refer to the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API documentation</a> for further guidance, or consider the  <a href="#example">example</a> below for a quickstart.</p>
<h2 id="graphql-schema">GraphQL schema</h2>
<p>The specific schema to get Dedicated CDN Egress IPs data is called <code>aegisIpUtilizationAdaptiveGroups</code>.</p>
<p>You can get average (<code>avg</code>) or maximum (<code>max</code>) utilization values (in percentage), and use the following dimensions:</p>
<ul>
<li>
<p><code>datetimeFiveMinutes</code> <span class="nb-type">time</span></p>
<ul>
<li>Timestamp truncated to five minutes. For example, <code>2025-01-10T00:05:00Z</code>.</li>
</ul>
</li>
<li>
<p><code>popName</code> <span class="nb-type">string</span></p>
<ul>
<li>The Cloudflare point of presence (PoP). For example, <code>sjc</code>.</li>
</ul>
</li>
<li>
<p><code>egressIp</code> <span class="nb-type">string</span></p>
<ul>
<li>Your assigned Dedicated CDN Egress IP. For example, <code>192.0.2.1</code>.</li>
</ul>
</li>
<li>
<p><code>origin</code> <span class="nb-type">string</span></p>
<ul>
<li>Origin IP and port. For example, <code>203.0.113.150:443</code>.</li>
</ul>
</li>
<li>
<p><code>popUtilizationKey</code> <span class="nb-type">string</span></p>
<ul>
<li>The Cloudflare point of presence (PoP), the Dedicated CDN Egress IP, and the origin IP and port. For example, <code>sjc 192.0.2.1 203.0.113.150:443</code>.</li>
</ul>
</li>
</ul>
<h2 id="example">Example</h2>
<p>Refer to the query below to learn how to get average utilization and maximum utilization by point of presence, and filter the results.</p>
<p>You can also select the button at the bottom to use this query for your account via the <a href="https://graphql.cloudflare.com/explorer">Cloudflare GraphQL API Explorer</a>. Make sure to provide your account ID and timestamps, and replace the placeholders for <code>popName</code>, <code>egressIp</code>, and <code>origin</code> as needed.</p>
<pre tabindex="0"><code class="language-graphql">query AegisIpUtilizationQuery(&#10;  $accountTag: string&#10;  $datetimeStart: string&#10;  $datetimeEnd: string&#10;) {&#10;  viewer {&#10;    utilization: accounts(filter: { accountTag: $accountTag }) {&#10;      avgByPopUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        avg {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      maxByPopUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      filterPopUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;          popName: &quot;&lt;CLOUDFLARE_POP&gt;&quot;&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      filterIPUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;          egressIp: &quot;&lt;YOUR_EGRESS_IP&gt;&quot;&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      filterOriginUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;          origin: &quot;&lt;ORIGIN_IP_AND_PORT&gt;&quot;&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
