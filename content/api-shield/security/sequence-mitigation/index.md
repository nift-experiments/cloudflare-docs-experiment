---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/sequence-mitigation/
  description: Enforce expected API request patterns to detect and block malicious sequences.
  full_title: Sequence mitigation · Cloudflare API Shield docs
  head_html: <title>Sequence mitigation · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Enforce expected API request patterns to detect and block malicious sequences."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/index.md"><meta property="og:title" content="Sequence mitigation · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enforce expected API request patterns to detect and block malicious sequences."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/sequence-mitigation/#page","headline":"Sequence mitigation \u00b7 Cloudflare API Shield docs","description":"Enforce expected API request patterns to detect and block malicious sequences.","url":"https://developers.cloudflare.com/api-shield/security/sequence-mitigation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/sequence-mitigation/
  schema: 1
---
<p>Sequence mitigation allows you to enforce request patterns for authenticated clients communicating with your API.</p>
<p>You can use sequence rules to establish a set of known behavior for API clients or detect and mitigate malicious behavior.</p>
<p>For example, you may expect that API requests made during a bank funds transfer could conform to the following order in time:</p>
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
<p>You may want to enforce that an API user requests <code>GET /api/v1/users/{user_id}/accounts</code> before <code>GET /api/v1/accounts/{account_id}/balance</code> and that you request <code>GET /api/v1/accounts/{account_id}/balance</code> before <code>POST /api/v1/transferFunds</code>.</p>
<p>Using sequence mitigation, you can enforce that request pattern with two new sequence mitigation rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3254.md")
</aside>
<h2 id="process">Process</h2>
<p>You can <a href="/api-shield/security/sequence-mitigation/manage-sequence-rules/">create a sequence rule</a> to enforce behavior on your API over time using one of two approaches.</p>
<p>A positive security model blocks users who make API requests outside of your expected patterns. A negative security model blocks users who perform a known malicious sequence of API calls.</p>
<p>Sequence rules built via the Cloudflare dashboard using API Shield rules utilize a lookback window to match endpoints in the sequence. The rule will match as long as both endpoints are found within <a href="/api-shield/security/sequence-mitigation/#request-limitations">10 requests</a> (to endpoints within Endpoint Management) of each other and made within <a href="/api-shield/security/sequence-mitigation/#time-limitations">10 minutes</a> of each other.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3253.md")
</aside>
<p>If you want to add multiple endpoints, ignore the lookback window, and configure time-based constraints, refer to <a href="/api-shield/security/sequence-mitigation/custom-rules/">Sequence mitigation custom rules</a>.</p>
<p>In the bank funds transfer example, enforcing that a user requests <code>GET /api/v1/accounts/{account_id}/balance</code> before <code>POST /api/v1/transferFunds</code> is considered a positive security model, since a user may only perform a funds transfer after listing an account balance.</p>
<p>A negative security model may be useful if you see abusive behavior that is outside the norm of your application and you need to stop the requests while researching the correct positive security model to implement.</p>
<p>For example, if there was an authorization bug that allowed users to iterate through other users' profiles that contain account numbers via <code>GET /api/v1/users/{var1}/profile</code> and then a user tries to make fraudulent funds transfers, you could create a rule to block or log the sequence <code>GET /api/v1/users/{var1}/profile</code> to <code>POST /api/v1/transferFunds</code>.</p>
<h2 id="limitations">Limitations</h2>
<h3 id="endpoint-management">Endpoint Management</h3>
<p>To track requests to <span class="nb-glossary-tooltip" title="API endpoint">API endpoints</span>, they must be added to <a href="/api-shield/management-and-monitoring/">Endpoint Management</a>. Add your endpoints to endpoint management via <a href="/api-shield/security/api-discovery/">API Discovery</a>, <a href="/api-shield/security/schema-validation/">Schema validation</a>, or <a href="/api-shield/management-and-monitoring/#add-endpoints-manually">manually</a> through the Cloudflare dashboard.</p>
<h3 id="session-identifiers">Session Identifiers</h3>
<p>API Shield uses your configured <span class="nb-glossary-tooltip" title="session identifier">session identifier</span> to track sessions. You must configure a session identifier that is unique per end user of your API in order for sequence mitigation to function as expected.</p>
<h3 id="request-limitations">Request limitations</h3>
<p>By default, API Shield stores the current and previous nine requested endpoints by each individual API user identified through the session identifier. Contact your account team if the default lookback window is not sufficient for you.</p>
<p>Sequence mitigation further de-duplicates requests to the same endpoint while building the sequence.</p>
<p>To illustrate, in the original <a href="/api-shield/security/sequence-mitigation/">sequence example</a> listed above, sequence mitigation would store the following sequence:</p>
<ol>
<li><code>GET /api/v1/users/{user_id}/accounts</code></li>
<li><code>GET /api/v1/accounts/{account_id}/balance</code></li>
<li><code>POST /api/v1/transferFunds</code></li>
</ol>
<p>Sequence mitigation de-duplicated the two requests to <code>GET /api/v1/accounts/{account_id}/balance</code> and stored them as a single request.</p>
<h3 id="time-limitations">Time limitations</h3>
<p>Sequence mitigation rules have a lookback period of 10 minutes. Any two requests using the same session identifier extend the sequence if they happen no further than 10 minutes apart. A request that happens more than 10 minutes after the previous one starts a new sequence.</p>
<p>For example, if you create a rule requiring one endpoint to be requested before another, and more than 10 minutes elapses between the two requests, the rule will not match.</p>
<h2 id="availability">Availability</h2>
<p>Sequence mitigation is currently in a closed beta and is only available for Enterprise customers. If you would like to be included in the beta, contact your account team.</p>
