---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/
  description: Organize API endpoints and address vulnerabilities with managed and custom labels.
  full_title: Endpoint labeling service · Cloudflare API Shield docs
  head_html: <title>Endpoint labeling service · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Organize API endpoints and address vulnerabilities with managed and custom labels."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/index.md"><meta property="og:title" content="Endpoint labeling service · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Organize API endpoints and address vulnerabilities with managed and custom labels."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="API Shield"><meta name="pcx_tags" content="GraphQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#page","headline":"Endpoint labeling service \u00b7 Cloudflare API Shield docs","description":"Organize API endpoints and address vulnerabilities with managed and custom labels.","url":"https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL"]}</script>
  markdown: true
  noindex: false
  route: /api-shield/management-and-monitoring/endpoint-labels/
  schema: 1
---
<p>API Shield's labeling service will help you organize your endpoints and address vulnerabilities in your API. The labeling service comes with managed and user-defined labels.</p>
<p>Managed labels help you organize endpoints by use case. Managed labels will also automatically identify endpoints with informative or security risks, alerting you on endpoints that need attention.</p>
<p>User-defined labels can also be added to endpoints in API Shield by creating a label and adding it to an individual endpoint or multiple endpoints. User-defined labels will be useful for organizing your endpoints by owner, version, or type.</p>
<p>You can filter your endpoints based on the labels.</p>
<h2 id="categories">Categories</h2>
<h3 id="managed-labels">Managed labels</h3>
<p>Use managed labels to identify endpoints by use case. Cloudflare may automatically apply these labels in a future release.</p>
<p><code>cf-log-in</code>: Add this label to endpoints that accept user credentials. You may have multiple endpoints if you accept username, password, and multi-factor authentication (MFA) across multiple endpoints or requests.</p>
<p><code>cf-sign-up</code>: Add this label to endpoints that are the final step in creating user accounts for your site or application.</p>
<p><code>cf-content</code>: Add this label to endpoints that provide unique content, such as product details, user reviews, pricing, or other unique information.</p>
<p><code>cf-purchase</code>: Add this label to endpoints that are the final step in purchasing goods or services online.</p>
<p><code>cf-password-reset</code>: Add this label to endpoints that participate in the user password reset process. This includes initial password reset requests and final password reset submissions.</p>
<p><code>cf-add-cart</code>: Add this label to endpoints that add items to a user's shopping cart or verify item availability.</p>
<p><code>cf-add-payment</code>: Add this label to endpoints that accept credit card or bank account details where fraudsters may iterate through account numbers to guess valid combinations of payment information.</p>
<p><code>cf-check-value</code>: Add this label to endpoints that check the balance of rewards points, in-game currency, or other stored value products that can be earned, transferred, and redeemed for cash or physical goods.</p>
<p><code>cf-add-post</code>: Add this label to endpoints that post messages in a communication forum, or product or merchant reviews.</p>
<p><code>cf-account-update</code>: Add this label to endpoints that participate in user account or profile updates.</p>
<p><code>cf-llm</code>: Services that are (partially) powered by Large Language Model (LLM).</p>
<p><code>cf-mcp</code>: Add this label to endpoints that implement the <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a> for AI tool and data access.</p>
<p><code>cf-rss-feed</code>: Add this label to endpoints that expect traffic from RSS clients.</p>
<p><code>cf-web-page</code>: Add this label to endpoints that serve HTML pages.</p>
<p><code>cf-contains-ads</code>: Add this label to endpoints that serve web pages containing advertisements.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3218.md")
</aside>
<h3 id="risk-labels">Risk labels</h3>
<p>Cloudflare automatically runs risk scans every 24 hours on your saved endpoints. API Shield applies these labels when a scan finds security risks on your endpoints. A corresponding Security Center Insight is also raised when risks are found.</p>
<p><code>cf-risk-missing-auth</code>: Automatically added when all successful requests lack a session identifier. Refer to <a href="/api-shield/security/authentication-posture/#process">Authentication Posture</a> for more information.</p>
<p><code>cf-risk-mixed-auth</code>: Automatically added when some successful requests contain a session identifier and some successful requests lack a session identifier. Refer to <a href="/api-shield/security/authentication-posture/#process">Authentication Posture</a> for more information.</p>
<p><code>cf-risk-sensitive</code>: Automatically added to endpoints when HTTP responses match the WAF's <a href="/api-shield/management-and-monitoring/endpoint-management/#sensitive-data-detection">Sensitive Data Detection</a> ruleset.</p>
<p><code>cf-risk-error-anomaly</code>: Automatically added when an endpoint experiences a recent increase in response errors over the last 24 hours.</p>
<p><code>cf-risk-latency-anomaly</code>: Automatically added when an endpoint experiences a recent increase in response latency over the last 24 hours.</p>
<p><code>cf-risk-size-anomaly</code>: Automatically added when an endpoint experiences a spike in response body size over the last 24 hours.</p>
<p><code>cf-risk-bola-enumeration</code>: Automatically added when an endpoint experiences successful responses with drastic differences in the number of unique elements requested by different user sessions.</p>
<p><code>cf-risk-bola-pollution</code>: Automatically added when an endpoint experiences successful responses where parameters are found in multiple places in the request, as opposed to what is expected from the API's schema.</p>
<p><code>cf-risk-zombie</code>: Automatically added when a saved endpoint has not received traffic in 32 days.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3217.md")
</aside>
<h4 id="recommended-action">Recommended action</h4>
<p>How you address risks to your endpoints will depend on its label(s). The following steps provide you with general guidelines on how to take action on them.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3219.md")
</div>
<hr />
<h2 id="analytics">Analytics</h2>
<h3 id="graphql-analytics-api">GraphQL Analytics API</h3>
<p>You can query the matched operation and managed labels for individual requests using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. The <code>webAssetsOperationId</code> and <code>webAssetsLabelsManaged</code> fields are available in the <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code> datasets. Use <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a> to explore the full schema and available filter operators.</p>
<p><code>webAssetsLabelsManaged</code> returns at most 10 labels per request.</p>
<h4 id="example-query-requests-by-managed-label">Example: query requests by managed label</h4>
<p>The following query returns the count of requests per operation ID and managed label set, filtered to requests where the matched operation carries the <code>cf-log-in</code> managed label.</p>
<pre tabindex="0"><code class="language-graphql">query GetAdaptiveGroups($start: DateTime!, $end: DateTime!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			httpRequestsAdaptiveGroups(&#10;				filter: {&#10;					datetime_geq: $start&#10;					datetime_leq: $end&#10;					requestSource: &quot;eyeball&quot;&#10;					webAssetsLabelsManaged_hasany: [&quot;cf-log-in&quot;]&#10;				}&#10;				limit: 25&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					webAssetsOperationId&#10;					webAssetsLabelsManaged&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Replace <code>cf-log-in</code> with any <a href="#managed-labels">managed label</a> or <a href="#risk-labels">risk label</a>. You can also omit the <code>webAssetsLabelsManaged_hasany</code> filter and use <code>webAssetsOperationId</code> as the sole dimension to group traffic by matched operation regardless of label.</p>
<h3 id="logpush">Logpush</h3>
<p>You can export per-request Web Assets data to your storage or <span class="nb-glossary-tooltip" title="SIEM">SIEM system</span> of choice using <a href="/logs/logpush/">Logpush</a>. The <code>WebAssetsOperationID</code> and <code>WebAssetsLabelsManaged</code> fields are available in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/#webassetslabelsmanaged">HTTP requests dataset</a>.</p>
<hr />
<h2 id="create-a-label">Create a label</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3221.md")
</div>
<p>Alternatively, you can create a user-defined label via <strong>Security</strong> &gt; <strong>Web Assets</strong>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3222.md")
</div>
<h2 id="apply-a-label-to-an-individual-endpoint">Apply a label to an individual endpoint</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3223.md")
</div>
<h2 id="bulk-apply-labels-to-multiple-endpoints">Bulk apply labels to multiple endpoints</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3224.md")
</div>
<h2 id="availability">Availability</h2>
<p>Endpoint labeling is available to all customers.</p>
