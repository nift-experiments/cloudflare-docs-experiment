---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/errors/
  description: Understand GraphQL Analytics API error formats.
  full_title: Error responses · Cloudflare Analytics docs
  head_html: <title>Error responses · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand GraphQL Analytics API error formats."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/errors/index.md"><meta property="og:title" content="Error responses · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand GraphQL Analytics API error formats."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/errors/#page","headline":"Error responses \u00b7 Cloudflare Analytics docs","description":"Understand GraphQL Analytics API error formats.","url":"https://developers.cloudflare.com/analytics/graphql-api/errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/errors/
  schema: 1
---
<p>The GraphQL Analytics API is a RESTful API based on HTTPS requests and JSON responses, and will return familiar HTTP status codes (for example, <code>404</code>, <code>500</code>, <code>504</code>). However, in contrast to the common REST approach, a <code>200</code> response can contain an error, conforming to the <a href="https://graphql.github.io/graphql-spec/June2018/#sec-Errors">GraphQL specification</a>.</p>
<p>All responses contain an <code>errors</code> array, which will be <code>null</code> if there are no errors, and include at least one error object if there was an error. Non-null error objects will contain the following fields:</p>
<ul>
<li><code>message</code>: a string describing the error.</li>
<li><code>path</code>: the nodes associated with the error, starting from the root. Note that the number included in the path array, for example, <code>0</code> or <code>1</code>, specifies to which zone the error applies; <code>0</code> indicates the first zone in the list (or only zone, if only one is being queried).</li>
<li><code>timestamp</code>: UTC datetime when the error occurred.</li>
</ul>
<h2 id="example">Example</h2>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;data&quot;: null,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;message&quot;: &quot;cannot request data older than 2678400s&quot;,&#10;      &quot;path&quot;: [&quot;viewer&quot;, &quot;zones&quot;, &quot;0&quot;, &quot;firewallEventsAdaptiveGroups&quot;],&#10;      &quot;extensions&quot;: {&#10;        &quot;timestamp&quot;: &quot;2019-12-09T21:27:19.195060142Z&quot;&#10;      }&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h2 id="common-error-types">Common error types</h2>
<h3 id="service-unavailability">Service unavailability</h3>
<p>Sample error messages:</p>
<ul>
<li><code>unable to execute query, please try again later</code> (HTTP <code>503</code>)</li>
<li><code>too many queries in progress, please try again later</code> (HTTP <code>503</code>)</li>
</ul>
<p>These messages indicate a temporary server-side issue. The first message typically means the upstream database is unreachable or returned an error. The second message means the server has reached its maximum number of concurrent queries.</p>
<p>Retry the request after a short delay. If the error persists, check the <a href="https://www.cloudflarestatus.com/">Cloudflare status page</a> for ongoing incidents.</p>
<h3 id="dataset-accessibility-limits-exceeded">Dataset accessibility limits exceeded</h3>
<p>Sample error messages:</p>
<ul>
<li><code>cannot request data older than...</code> (HTTP <code>400</code>)</li>
<li><code>number of fields can't be more than...</code> (HTTP <code>400</code>)</li>
<li><code>limit must be positive number and not greater than...</code> (HTTP <code>400</code>)</li>
<li><code>query time range is too large...</code> (HTTP <code>400</code>)</li>
</ul>
<p>These messages indicate that the query exceeds what is allowed for the particular dataset under the current <a href="https://www.cloudflare.com/plans/">plan</a>, and an upgrade should be considered. Refer to <a href="/analytics/graphql-api/limits/#node-limits-and-availability">Node limits</a> for details.</p>
<h3 id="parsing-issues">Parsing issues</h3>
<p>Sample error messages:</p>
<ul>
<li><code>error parsing args...</code> (HTTP <code>400</code>)</li>
<li><code>scalar fields must have no selections</code> (HTTP <code>400</code>)</li>
<li><code>object field must have selections</code> (HTTP <code>400</code>)</li>
<li><code>unknown field...</code> (HTTP <code>400</code>)</li>
<li><code>query contains error, please review it and retry</code> (HTTP <code>400</code>)</li>
</ul>
<p>These messages indicate that the query cannot be processed because it is malformed. Check the query syntax against the <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">GraphQL schema</a> and correct the invalid fields or structure.</p>
<h3 id="rate-limits-exceeded">Rate limits exceeded</h3>
<p>Sample error messages:</p>
<ul>
<li><code>rate limiter budget depleted, try again after 5 minutes</code> (HTTP <code>429</code>)</li>
<li><code>in combination, your request queries too many nodes, zones and accounts</code> (HTTP <code>429</code>)</li>
<li><code>query consumed excessive resources, please try running smaller queries which consume fewer resources</code> (HTTP <code>429</code>)</li>
</ul>
<p>These messages indicate the query exceeded rate or resource limits. Reduce the query complexity, the number of zones or accounts per request, or wait before retrying. Refer to the <a href="/analytics/graphql-api/limits/">Limits</a> section for more details about rate limits.</p>
<h3 id="authentication-and-authorization-errors">Authentication and authorization errors</h3>
<p>Sample error messages:</p>
<ul>
<li><code>Unauthorized</code> (HTTP <code>401</code>)</li>
<li><code>not authorized for that account</code> (HTTP <code>403</code>)</li>
<li><code>zones [...] are not authorized</code> (HTTP <code>403</code>)</li>
<li><code>does not have access to the path...</code> (HTTP <code>403</code>)</li>
</ul>
<p>An <code>Unauthorized</code> response means the API token or bearer token is missing, expired, or invalid. Verify that you are passing a valid token in the <code>Authorization</code> header.</p>
<p>A <code>403</code> response means the token does not have the required permissions for the requested account or zone. Verify the token has the <strong>Analytics: Read</strong> permission for the relevant resources. Refer to the <a href="/fundamentals/api/get-started/create-token/">Tokens</a> section for more details.</p>
<h3 id="internal-server-errors">Internal server errors</h3>
<p>Sample error message:</p>
<ul>
<li><code>Internal server error</code> (HTTP <code>500</code>)</li>
</ul>
<p>This is a generic error indicating an unexpected failure. If it persists, contact <a href="https://support.cloudflare.com/">Cloudflare Support</a> with the full request and response, including the <code>Ray-ID</code> header from the HTTP response.</p>
