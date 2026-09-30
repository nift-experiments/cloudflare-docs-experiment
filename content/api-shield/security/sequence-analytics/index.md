---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/sequence-analytics/
  description: Track the order of API requests over time to discover user journeys and sequences.
  full_title: Sequence Analytics · Cloudflare API Shield docs
  head_html: <title>Sequence Analytics · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Track the order of API requests over time to discover user journeys and sequences."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/sequence-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/sequence-analytics/index.md"><meta property="og:title" content="Sequence Analytics · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track the order of API requests over time to discover user journeys and sequences."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/sequence-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/sequence-analytics/#page","headline":"Sequence Analytics \u00b7 Cloudflare API Shield docs","description":"Track the order of API requests over time to discover user journeys and sequences.","url":"https://developers.cloudflare.com/api-shield/security/sequence-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/sequence-analytics/
  schema: 1
---
<p>Sequence Analytics tracks the order of API endpoint requests over time, allowing you to discover how users interact with your API. Sequence Analytics groups and highlights important user journeys (sequences) across your API. You can enforce preferred sequences using <a href="/api-shield/security/sequence-mitigation/">Sequence mitigation</a>.</p>
<h2 id="process">Process</h2>
<h3 id="sequence-building">Sequence building</h3>
<p>A sequence is a time-ordered list of HTTP API requests made by a specific visitor as they browse a website, use a mobile app, or interact with a B2B partner via API.</p>
<p>For example, a portion of a sequence made during a bank funds transfer could look like:</p>
<table>
<thead>
<tr>
<th>Order</th>
<th>Method</th>
<th>Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><code>GET</code></td>
<td><code>/api/v1/users/{user_id}/accounts</code></td>
<td><code>user_id</code> is the active user.</td>
</tr>
<tr>
<td>2</td>
<td><code>GET</code></td>
<td><code>/api/v1/accounts/{account_id}/balance</code></td>
<td><code>account_id</code> is one of the user’s accounts.</td>
</tr>
<tr>
<td>3</td>
<td><code>GET</code></td>
<td><code>/api/v1/accounts/{account_id}/balance</code></td>
<td><code>account_id</code> is a different account belonging to the user.</td>
</tr>
<tr>
<td>4</td>
<td><code>POST</code></td>
<td><code>/api/v1/transferFunds</code></td>
<td>This contains a request body detailing an account to transfer funds from, an account to transfer funds to, and an amount of money to transfer.</td>
</tr>
</tbody>
</table>
<p>API Shield uses your configured <span class="nb-glossary-tooltip" title="session identifier">session identifier</span> and operations in the <code>full</code> or <code>candidate</code> state to build a set of ordered API operations (HTTP host, method, and path) requested per session. API Shield may surface sequences in various lengths depending on how it scores the sequences.</p>
<h3 id="sequence-scoring">Sequence scoring</h3>
<p>API Shield scores sequences by a metric called precedence score. Sequence Analytics displays sequences by the highest precedence score. High-scoring sequences contain API requests which are likely to occur together in order.</p>
<p>Using the example above, a high score means that the last operation in the sequence <code>POST /api/v1/transferFunds</code> is highly likely to be preceded by the other operations in sequence <code>GET /api/v1/users/{user_id}/accounts</code> followed by <code>GET /api/v1/accounts/{account_id}/balance</code>. The scores are probabilities, which API Shield estimates using data from the last 24 hours.</p>
<h3 id="secure-your-api">Secure your API</h3>
<p>To proactively secure your API, you should inspect your highest-scoring sequences. For each high-scoring sequence, you should confirm with your development team if the final operation in the sequence must legitimately always be preceded by the other operations in the sequence.</p>
<p>Using the above example, if <code>POST /api/v1/transferFunds</code> must legitimately always be preceded by <code>GET /api/v1/users/{user_id}/accounts</code> and <code>GET /api/v1/accounts/{account_id}/balance</code>, you should create an <strong>Allow</strong> rule in sequence mitigation on the final operation of the sequence.</p>
<p>You should also consider applying other API Shield protections to these endpoints (<a href="/api-shield/security/volumetric-abuse-detection/">rate limiting suggestions</a>, <a href="/api-shield/security/schema-validation/">Schema validation</a>, <a href="/api-shield/security/jwt-validation/">JWT validation</a>, and <a href="/api-shield/security/mtls/">mTLS</a>).</p>
<p>For more information, refer to the <a href="https://blog.cloudflare.com/api-sequence-analytics">blog post</a>.</p>
<h3 id="repeated-sequences">Repeated sequences</h3>
<p>Real-world API usage shows many successively repeated operations. To facilitate exploration, Sequence Analytics collapses successively repeated operations into one.</p>
<h2 id="availability">Availability</h2>
<p>Sequence Analytics is available for all API Shield customers. Pro, Business, and Enterprise customers who have not purchased API Shield can get started by <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield">enabling the API Shield trial</a> in the Cloudflare dashboard or contacting your account manager.</p>
<h2 id="limitations">Limitations</h2>
<p>Sequence Analytics currently requires a session identifier and operations that API Shield can match at the edge. Ensure that you have <a href="/api-shield/get-started/#session-identifiers">set up your session identifier(s)</a> and reviewed your operations in the <code>full</code> and <code>candidate</code> states in <a href="/security/web-assets/manage-operations/#operation-states">Web Assets</a>.</p>
<p>Sequences are currently limited to nine operations in length.</p>
