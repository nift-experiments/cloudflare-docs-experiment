---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/
  description: Create, edit, and delete AI Gateway instances using the dashboard or API.
  full_title: Manage gateways · Cloudflare AI Gateway docs
  head_html: <title>Manage gateways · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, edit, and delete AI Gateway instances using the dashboard or API."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/index.md"><meta property="og:title" content="Manage gateways · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, edit, and delete AI Gateway instances using the dashboard or API."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#page","headline":"Manage gateways \u00b7 Cloudflare AI Gateway docs","description":"Create, edit, and delete AI Gateway instances using the dashboard or API.","url":"https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/configuration/manage-gateway/
  schema: 1
---
<p>You have several different options for managing an AI Gateway.</p>
<h2 id="create-gateway">Create gateway</h2>
<h3 id="default-gateway">Default gateway</h3>
<p>AI Gateway can automatically create a gateway for you. If you omit the gateway ID from your request entirely, AI Gateway defaults to using <code>default</code> as the gateway ID. When no gateway named <code>default</code> exists in your account, AI Gateway creates it on the first authenticated request.</p>
<p>This means you can start sending requests without creating a gateway first — AI Gateway handles gateway creation for you.</p>
<p>The request that triggers auto-creation must be authenticated. When using the <a href="/ai-gateway/usage/rest-api/">REST API</a>, the standard <code>Authorization</code> header is sufficient. When using <a href="/ai-gateway/usage/providers/">provider-native endpoints</a> at <code>gateway.ai.cloudflare.com</code>, include a valid <code>cf-aig-authorization</code> header. For Workers AI bindings, the account identity from the binding is used instead of a header.</p>
<p>The auto-created default gateway uses the following settings:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Authentication</td>
<td>On</td>
</tr>
<tr>
<td>Log collection</td>
<td>On</td>
</tr>
<tr>
<td>Caching</td>
<td>Off (TTL of 0)</td>
</tr>
<tr>
<td>Rate limiting</td>
<td>Off</td>
</tr>
<tr>
<td>Require provider credentials</td>
<td>Off</td>
</tr>
<tr>
<td>Workers AI billing</td>
<td>Standard billing</td>
</tr>
</tbody>
</table>
<p>After creation, you can edit the default gateway settings like any other gateway. If you delete the default gateway, sending a new authenticated request to the <code>default</code> gateway ID auto-creates it again.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2853.md")
</aside>
<h3 id="create-a-gateway-manually">Create a gateway manually</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2856.md")
</div></div>
<h2 id="edit-gateway">Edit gateway</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2859.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2852.md")
</aside>
<h3 id="configure-workers-ai-billing">Configure Workers AI billing</h3>
<p>By default, Workers AI requests use <strong>Standard billing</strong>, which charges your Cloudflare account at the end of each billing cycle.</p>
<p>To use prepaid AI Gateway credits for Workers AI requests:</p>
<ol>
<li><a href="/ai-gateway/features/unified-billing/#load-credits">Load credits</a> into your Cloudflare account.</li>
<li>In the Cloudflare dashboard, go to <strong>AI</strong> &gt; <strong>AI Gateway</strong> and select your gateway.</li>
<li>Go to <strong>Settings</strong> and find <strong>Workers AI Billing</strong>.</li>
<li>Select <strong>Unified billing</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Workers AI requests routed through this gateway will deduct from your AI Gateway credit balance in real time.</p>
<h3 id="prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</h3>
<p>To prevent Unified Billing fallback for third-party provider requests, turn on <strong>Require provider credentials</strong>. Refer to <a href="/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</a> for dashboard and API instructions.</p>
<h2 id="retry-requests">Retry requests</h2>
<p>You can configure your gateway to automatically retry failed requests to upstream providers. This is useful when you do not control the client and cannot implement client-side retries or backoff logic.</p>
<p>To configure retry settings:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>AI</strong> &gt; <strong>AI Gateway</strong> and select your gateway.</li>
<li>Go to <strong>Settings</strong> and find the <strong>Retry Requests</strong> section.</li>
<li>Turn on the toggle to turn on automatic retries.</li>
<li>Configure the following settings:
<ul>
<li><strong>Retry count</strong> — the maximum number of retry attempts (up to 5).</li>
<li><strong>Delay</strong> — the base delay between retries, from 0.1 to 60 seconds.</li>
<li><strong>Backoff</strong> — the backoff strategy for subsequent retries: Constant, Linear, or Exponential.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>These gateway-level defaults apply to all requests routed through the gateway. Per-request headers can override these defaults — refer to <a href="/ai-gateway/configuration/request-handling/#request-retries">Request handling</a> for details.</p>
<p>For more complex failover scenarios where you need to fail across different providers, refer to <a href="/ai-gateway/features/dynamic-routing/">Dynamic Routing</a>.</p>
<h2 id="delete-gateway">Delete gateway</h2>
<p>Deleting your gateway is permanent and can not be undone.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2862.md")
</div></div>
