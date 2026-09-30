---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/features/pagination/
  description: Paginate through GraphQL Analytics API results.
  full_title: Pagination · Cloudflare Analytics docs
  head_html: <title>Pagination · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Paginate through GraphQL Analytics API results."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/features/pagination/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/features/pagination/index.md"><meta property="og:title" content="Pagination · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Paginate through GraphQL Analytics API results."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/features/pagination/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/features/pagination/#page","headline":"Pagination \u00b7 Cloudflare Analytics docs","description":"Paginate through GraphQL Analytics API results.","url":"https://developers.cloudflare.com/analytics/graphql-api/features/pagination/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/features/pagination/
  schema: 1
---
<p>Pagination – breaking up your query results into smaller parts – can be done using <code>limit</code>, <code>orderBy</code>, and filtering parameters. The GraphQL Analytics API does not support cursors for pagination.</p>
<ul>
<li><code>limit</code> (integer) defines how many records to return.</li>
<li><code>orderBy</code> (string) defines the sort order for the data.</li>
</ul>
<h2 id="query-pages-without-cursors">Query pages without cursors</h2>
<p>Our examples assume that the <code>date</code> and <code>clientCountryName</code> relationships are unique.</p>
<h3 id="get-the-first-n-results-of-a-query">Get the first <em>n</em> results of a query</h3>
<p>To limit results, add the <code>limit</code> parameter as an integer. For example, query the first two records:</p>
<pre tabindex="0"><code class="language-javascript">&#10;firewallEventsAdaptive (limit: 2, orderBy: [datetime_ASC, clientCountryName_ASC]) {&#10;    datetime&#10;    clientCountryName&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3173.md")
</aside>
<p><strong>Response</strong></p>
<pre tabindex="0"><code class="language-javascript">&#10;{&#10;  &quot;firewallEventsAdaptive&quot; : [&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UM&quot;&#10;    },&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;US&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h3 id="query-for-the-next-page-using-filters">Query for the next page using filters</h3>
<p>To get the next <em>n</em> results, specify a filter to exclude the last result from the previous query. Taking the previous example, you can do this by appending the greater-than operator (<code>_gt</code>) to the <code>clientCountryName</code> field and the greater-or-equal operator (<code>_geq</code>) to the <code>datetime</code> field. This is where being specific about sort order comes into play. You are less likely to miss results using a more granular sort order.</p>
<pre tabindex="0"><code class="language-javascript">&#10;firewallEventsAdaptive (limit: 2, orderBy: [datetime_ASC, clientCountryName_ASC], filter: {datetime_geq: &quot;2018-11-12T00:00:00Z&quot;, clientCountryName_gt: &quot;US&quot;}) {&#10;    datetime&#10;    clientCountryName&#10;}&#10;</code></pre>
<p><strong>Response</strong></p>
<pre tabindex="0"><code class="language-javascript">&#10;{&#10;  &quot;firewallEventsAdaptive&quot; : [&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UY&quot;&#10;    },&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UZ&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h3 id="query-the-previous-page">Query the previous page</h3>
<p>To get the previous <em>n</em> results, reverse the filters and sort order.</p>
<pre tabindex="0"><code class="language-javascript">&#10;firewallEventsAdaptive (limit: 2, orderBy: [datetime_DESC, clientCountryName_DESC, filter: {datetime_leq: &quot;2018-11-12T00:00:00Z&quot;, clientCountryName_lt: &quot;UY&quot;}]) {&#10;  datetime&#10;  clientCountryName&#10;}&#10;</code></pre>
<p><strong>Response</strong></p>
<pre tabindex="0"><code class="language-javascript">&#10;{&#10;  &quot;firewallEventsAdaptive&quot; : [&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;US&quot;&#10;    },&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UM&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
