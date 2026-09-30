---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/
  description: Learn what account API tokens are, when to use them, and what they currently work with
  full_title: Account API tokens · Cloudflare Fundamentals docs
  head_html: <title>Account API tokens · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn what account API tokens are, when to use them, and what they currently work with"><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/index.md"><meta property="og:title" content="Account API tokens · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn what account API tokens are, when to use them, and what they currently work with"><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/#page","headline":"Account API tokens \u00b7 Cloudflare Fundamentals docs","description":"Learn what account API tokens are, when to use them, and what they currently work with","url":"https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/get-started/account-owned-tokens/
  schema: 1
---
<p>While user tokens act on behalf of a particular user and inherit a subset of that user's permissions, account API tokens allow you to set up durable integrations that can act as service principals with their own specific set of permissions. This approach is ideal for scenarios like CI/CD, or building integrations with external services like SIEMs where it is important that the integration continues working, even long after the user who configured the integration may have left your organization altogether. User tokens are better for ad hoc tasks like scripting, where acting as the user is ideal and durability is less of a concern.</p>
<p>New account API tokens use the <code>cfat_</code> prefixed <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked tokens.</p>
<h2 id="create-an-account-owned-token">Create an account owned token</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9004.md")
</aside>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Account API Tokens</strong>.</li>
<li>Select <strong>Create Token</strong> and fill in the token name, permissions, and the optional expiration date for the token.</li>
<li>Select <strong>Continue to summary</strong> and review the details.</li>
<li>Select <strong>Create Token</strong>.</li>
</ol>
<p>Alternatively, you can create a token using the <a href="/api/resources/accounts/subresources/tokens/methods/create/">account API token creation API</a>.</p>
<p>Refer to the <a href="https://blog.cloudflare.com/account-owned-tokens-automated-actions-zaraz/">blog post</a> for more information.</p>
<h2 id="compatibility-matrix">Compatibility matrix</h2>
<p>Account API tokens are generally available for all accounts. Some services may not support account API tokens yet. Refer to the compatibility matrix below for the latest status.</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Compatibility</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access</td>
<td>✅</td>
</tr>
<tr>
<td>Account Analytics</td>
<td>✅</td>
</tr>
<tr>
<td>Account Management</td>
<td>✅</td>
</tr>
<tr>
<td>AI Gateway</td>
<td>✅</td>
</tr>
<tr>
<td>API Shield</td>
<td>✅</td>
</tr>
<tr>
<td>Argo</td>
<td>✅</td>
</tr>
<tr>
<td>Billing</td>
<td>✅</td>
</tr>
<tr>
<td>Browser Run</td>
<td>✅</td>
</tr>
<tr>
<td>Bulk Redirects</td>
<td>✅</td>
</tr>
<tr>
<td>Cache</td>
<td>✅</td>
</tr>
<tr>
<td>Tiered Cache</td>
<td>✅</td>
</tr>
<tr>
<td>Client-side security (formerly Page Shield)</td>
<td>✅</td>
</tr>
<tr>
<td>Cloud Connector</td>
<td>✅</td>
</tr>
<tr>
<td>Configuration Rules</td>
<td>✅</td>
</tr>
<tr>
<td>Custom Lists</td>
<td>✅</td>
</tr>
<tr>
<td>Custom Pages</td>
<td>✅</td>
</tr>
<tr>
<td>D1</td>
<td>✅</td>
</tr>
<tr>
<td>Data Loss Prevention</td>
<td>✅</td>
</tr>
<tr>
<td>Digital Experience Monitoring</td>
<td>✅</td>
</tr>
<tr>
<td>Distributed Web</td>
<td>✅</td>
</tr>
<tr>
<td>DNS</td>
<td>✅</td>
</tr>
<tr>
<td>Durable Objects</td>
<td>✅</td>
</tr>
<tr>
<td>Email Relay</td>
<td>✅</td>
</tr>
<tr>
<td>Secure Web Gateway</td>
<td>✅</td>
</tr>
<tr>
<td>Healthchecks</td>
<td>✅</td>
</tr>
<tr>
<td>Hyperdrive</td>
<td>✅</td>
</tr>
<tr>
<td>Images</td>
<td>✅</td>
</tr>
<tr>
<td>Intel Data Platform</td>
<td>❌</td>
</tr>
<tr>
<td>Load Balancing</td>
<td>✅</td>
</tr>
<tr>
<td>Log Explorer</td>
<td>✅</td>
</tr>
<tr>
<td>Network Flow</td>
<td>✅</td>
</tr>
<tr>
<td>Magic Transit</td>
<td>✅</td>
</tr>
<tr>
<td>Cloudflare WAN</td>
<td>✅</td>
</tr>
<tr>
<td>Managed Rules</td>
<td>✅</td>
</tr>
<tr>
<td>Network Error Logging</td>
<td>✅</td>
</tr>
<tr>
<td>Page Rules</td>
<td>❌</td>
</tr>
<tr>
<td>Pages</td>
<td>✅</td>
</tr>
<tr>
<td>R2</td>
<td>✅</td>
</tr>
<tr>
<td>Radar</td>
<td>✅</td>
</tr>
<tr>
<td>Registrar</td>
<td>❌</td>
</tr>
<tr>
<td>Rulesets</td>
<td>✅</td>
</tr>
<tr>
<td>Spectrum</td>
<td>✅</td>
</tr>
<tr>
<td>Speed</td>
<td>✅</td>
</tr>
<tr>
<td>SSL/TLS</td>
<td>✅</td>
</tr>
<tr>
<td>Stream</td>
<td>✅</td>
</tr>
<tr>
<td>Super Bot Fight Mode</td>
<td>❌</td>
</tr>
<tr>
<td>Trace</td>
<td>✅</td>
</tr>
<tr>
<td>Tunnels</td>
<td>✅</td>
</tr>
<tr>
<td>Turnstile</td>
<td>❌</td>
</tr>
<tr>
<td>Vectorize</td>
<td>✅</td>
</tr>
<tr>
<td>Waiting Room</td>
<td>✅</td>
</tr>
<tr>
<td>Workers</td>
<td>✅</td>
</tr>
<tr>
<td>Workers AI</td>
<td>✅</td>
</tr>
<tr>
<td>Workers KV</td>
<td>✅</td>
</tr>
<tr>
<td>Workers Observability</td>
<td>✅</td>
</tr>
<tr>
<td>Workers Queues</td>
<td>✅</td>
</tr>
<tr>
<td>Workflows</td>
<td>✅</td>
</tr>
<tr>
<td>Zaraz</td>
<td>✅</td>
</tr>
<tr>
<td>Zero Trust Client Platform</td>
<td>❌</td>
</tr>
<tr>
<td>Zero Trust Devices and Services</td>
<td>✅</td>
</tr>
<tr>
<td>Zone/Domain Management</td>
<td>✅</td>
</tr>
</tbody>
</table>
