---
cp9:
  canonical: https://developers.cloudflare.com/security/web-assets/label-operations/
  description: Use labels to describe the application use case for Web Assets operations.
  full_title: Label operations · Security dashboard docs
  head_html: <title>Label operations · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="Use labels to describe the application use case for Web Assets operations."><link rel="canonical" href="https://developers.cloudflare.com/security/web-assets/label-operations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/web-assets/label-operations/index.md"><meta property="og:title" content="Label operations · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use labels to describe the application use case for Web Assets operations."><meta property="og:url" content="https://developers.cloudflare.com/security/web-assets/label-operations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Security dashboard"><meta name="pcx_tags" content="GraphQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/web-assets/label-operations/#page","headline":"Label operations \u00b7 Security dashboard docs","description":"Use labels to describe the application use case for Web Assets operations.","url":"https://developers.cloudflare.com/security/web-assets/label-operations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL"]}</script>
  markdown: true
  noindex: false
  route: /security/web-assets/label-operations/
  schema: 1
---
<p>Labels add use-case context to operations. Security detections can use labels to extend relevant focus on traffic with a specific application use case.</p>
<h2 id="managed-labels">Managed labels</h2>
<p>Cloudflare defines managed labels. They identify common operation types, such as login flows, sign-up flows, and AI-powered operations.</p>
<p>Some managed labels can be discovered automatically. Automatic discovery currently applies only to selected managed labels and selected plans.</p>
<p>The following managed labels are available:</p>
<table>
<thead>
<tr>
<th>Label</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf-api-endpoint</code></td>
<td>Operations that serve machine-readable data or facilitate programmatic interaction.</td>
</tr>
<tr>
<td><code>cf-llm</code></td>
<td>Operations that receive requests for services powered by Large Language Models (LLMs).</td>
</tr>
<tr>
<td><code>cf-mcp</code></td>
<td>Operations that implement the <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a> for AI tool and data access.</td>
</tr>
<tr>
<td><code>cf-contains-ads</code></td>
<td>Operations that serve web pages containing advertisements.</td>
</tr>
<tr>
<td><code>cf-log-in</code></td>
<td>Operations that accept user credentials.</td>
</tr>
<tr>
<td><code>cf-sign-up</code></td>
<td>Operations that create user accounts.</td>
</tr>
<tr>
<td><code>cf-content</code></td>
<td>Operations that provide unique content, such as product details, reviews, or pricing.</td>
</tr>
<tr>
<td><code>cf-purchase</code></td>
<td>Operations that complete a purchase.</td>
</tr>
<tr>
<td><code>cf-password-reset</code></td>
<td>Operations that participate in password reset flows.</td>
</tr>
<tr>
<td><code>cf-add-cart</code></td>
<td>Operations that add items to a cart or verify item availability.</td>
</tr>
<tr>
<td><code>cf-add-payment</code></td>
<td>Operations that accept credit card or bank account details.</td>
</tr>
<tr>
<td><code>cf-check-value</code></td>
<td>Operations that check rewards points, in-game currency, or other stored value.</td>
</tr>
<tr>
<td><code>cf-add-post</code></td>
<td>Operations that post messages, reviews, or similar user-generated content.</td>
</tr>
<tr>
<td><code>cf-account-update</code></td>
<td>Operations that update user account or profile details.</td>
</tr>
<tr>
<td><code>cf-rss-feed</code></td>
<td>Operations that expect traffic from RSS clients.</td>
</tr>
<tr>
<td><code>cf-web-page</code></td>
<td>Operations that serve HTML pages.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13836.md")
</aside>
<h2 id="available-detections">Available detections</h2>
<p>Some detections use labels to decide which operations to inspect. The following detections can use operation labels:</p>
<table>
<thead>
<tr>
<th>Label</th>
<th>Related detection</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf-llm</code></td>
<td><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a></td>
</tr>
<tr>
<td><code>cf-log-in</code></td>
<td><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a> and <a href="/bots/account-abuse-protection/">account abuse protection</a></td>
</tr>
<tr>
<td><code>cf-sign-up</code></td>
<td><a href="/bots/account-abuse-protection/">Account abuse protection</a></td>
</tr>
</tbody>
</table>
<p>Some detections may still require product-specific configuration. For an end-to-end workflow, refer to <a href="/security/web-assets/define-security-protections/">Define security protections</a>.</p>
<h2 id="custom-labels">Custom labels</h2>
<p>Custom labels help you organize operations by owner, application, environment, and business flow.</p>
<h2 id="apply-labels">Apply labels</h2>
<p>Apply labels to operations from Web Assets.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13837.md")
</div>
<h2 id="use-labels-in-analytics-and-logs">Use labels in analytics and logs</h2>
<p>You can review matched operations and managed labels in Security Analytics. You can also query or export this data.</p>
<h3 id="graphql-analytics-api">GraphQL Analytics API</h3>
<p>You can query matched operation and managed label data using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. The <code>webAssetsOperationId</code> and <code>webAssetsLabelsManaged</code> fields are available in the <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code> datasets.</p>
<p><code>webAssetsLabelsManaged</code> returns at most 10 labels per request.</p>
<p>The following query returns request counts by operation ID and managed label set for traffic carrying the <code>cf-llm</code> managed label:</p>
<pre tabindex="0"><code class="language-graphql">query GetAdaptiveGroups($zoneTag: string, $start: DateTime!, $end: DateTime!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			httpRequestsAdaptiveGroups(&#10;				filter: {&#10;					datetime_geq: $start&#10;					datetime_leq: $end&#10;					requestSource: &quot;eyeball&quot;&#10;					webAssetsLabelsManaged_hasany: [&quot;cf-llm&quot;]&#10;				}&#10;				limit: 25&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					webAssetsOperationId&#10;					webAssetsLabelsManaged&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Replace <code>cf-llm</code> with another <a href="#managed-labels">managed label</a>. You can also use <code>webAssetsOperationId</code> as the only dimension to group traffic by matched operation.</p>
<h3 id="logpush">Logpush</h3>
<p>You can export per-request Web Assets data to your storage or <span class="nb-glossary-tooltip" title="SIEM">SIEM system</span> using <a href="/logs/logpush/">Logpush</a>. The <code>WebAssetsOperationID</code> and <code>WebAssetsLabelsManaged</code> fields are available in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/#webassetslabelsmanaged/">HTTP requests dataset</a>.</p>
