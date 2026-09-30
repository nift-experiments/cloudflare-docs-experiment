---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/
  description: Migrate to new GraphQL analytics nodes.
  full_title: Migrate to new GraphQL nodes · Cloudflare Load Balancing docs
  head_html: <title>Migrate to new GraphQL nodes · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate to new GraphQL analytics nodes."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/index.md"><meta property="og:title" content="Migrate to new GraphQL nodes · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate to new GraphQL analytics nodes."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Load Balancing"><meta name="pcx_tags" content="GraphQL,Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/#page","headline":"Migrate to new GraphQL nodes \u00b7 Cloudflare Load Balancing docs","description":"Migrate to new GraphQL analytics nodes.","url":"https://developers.cloudflare.com/load-balancing/reference/migration-guides/load-balancing-graphql-nodes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL","Migration"]}</script>
  markdown: true
  noindex: false
  route: /load-balancing/reference/migration-guides/load-balancing-graphql-nodes/
  schema: 1
---
<p>After 30 September 2021, Cloudflare will make the following changes to the Load Balancing GraphQL schema:</p>
<ul>
<li>Deprecate nodes:
<ul>
<li><code>loadBalancingRequestsGroups</code> will be deprecated for <code>loadBalancingRequestsAdaptiveGroups</code></li>
<li><code>loadBalancingRequests</code> will be deprecated for <code>loadBalancingRequestsAdaptive</code></li>
</ul>
</li>
<li>Deprecate the <code>date</code> field (replace it with the existing <code>datetime</code> field)</li>
<li>Add the <code>sampleInterval</code> field</li>
</ul>
<h2 id="example-query">Example query</h2>
<p>The following example:</p>
<ul>
<li>Replaces <code>loadBalancingRequestsGroups</code> with <code>loadBalancingRequestsAdaptiveGroups</code></li>
<li>Replaces <code>date</code> with <code>datetime</code></li>
<li>Uses the new <code>sampleInterval</code> field</li>
</ul>
<pre tabindex="0"><code class="language-json">query {&#10;  viewer {&#10;    zones(filter: { zoneTag: &quot;your Zone ID&quot; }) {&#10;      loadBalancingRequestsAdaptiveGroups(&#10;        filter: {&#10;          datetime_gt: &quot;2021-06-12T04:00:00Z&quot;,&#10;          datetime_lt: &quot;2021-06-13T06:00:00Z&quot;&#10;        }&#10;      ) {&#10;        dimensions {&#10;          datetime&#10;          coloCode&#10;          ...&#10;        }&#10;        avg {&#10;          sampleInterval&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
