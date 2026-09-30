---
cp9:
  canonical: https://developers.cloudflare.com/flagship/sdk/client-provider/
  description: Set up the FlagshipClientProvider to evaluate feature flags synchronously in browser applications using the OpenFeature web SDK.
  full_title: TypeScript Client SDK · Cloudflare Flagship docs
  head_html: <title>TypeScript Client SDK · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up the FlagshipClientProvider to evaluate feature flags synchronously in browser applications using the OpenFeature web SDK."><link rel="canonical" href="https://developers.cloudflare.com/flagship/sdk/client-provider/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/sdk/client-provider/index.md"><meta property="og:title" content="TypeScript Client SDK · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up the FlagshipClientProvider to evaluate feature flags synchronously in browser applications using the OpenFeature web SDK."><meta property="og:url" content="https://developers.cloudflare.com/flagship/sdk/client-provider/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/sdk/client-provider/#page","headline":"TypeScript Client SDK \u00b7 Cloudflare Flagship docs","description":"Set up the FlagshipClientProvider to evaluate feature flags synchronously in browser applications using the OpenFeature web SDK.","url":"https://developers.cloudflare.com/flagship/sdk/client-provider/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/sdk/client-provider/
  schema: 1
---
<p>The <code>FlagshipClientProvider</code> implements the OpenFeature web provider interface for browser applications. It pre-fetches a declared set of flag values on initialization and resolves evaluations synchronously from an in-memory cache.</p>
<p>This makes the provider suitable for client-side rendering where synchronous access to flag values is required.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8722.md")
</aside>
<h2 id="prefetchflags">prefetchFlags</h2>
<p><code>prefetchFlags</code> is a required array of flag keys that the provider fetches during initialization and on every context change. Only flags listed in this array are available for synchronous evaluation — any flag key not included returns a <code>FLAG_NOT_FOUND</code> error at resolution time.</p>
<p><strong>Fetch behavior:</strong></p>
<ul>
<li><strong>On initialization</strong> — all flags in <code>prefetchFlags</code> are fetched in parallel and stored in an in-memory cache. The provider transitions to <code>READY</code> once all fetches complete (individual failures are non-fatal).</li>
<li><strong>On context change</strong> — the cache is invalidated and all flags are re-fetched for the new context. This is required by the <a href="https://openfeature.dev/specification/glossary/#static-context-paradigm">static context paradigm</a> used by the OpenFeature web SDK, where context is set globally and providers are expected to re-evaluate when it changes.</li>
<li><strong>At resolution time</strong> — evaluations are served synchronously from the cache. No network request is made during <code>getBooleanValue</code>, <code>getStringValue</code>, etc.</li>
</ul>
<h2 id="setup">Setup</h2>
<p>The following example initializes the provider with a set of pre-fetched flags and evaluates them in a browser application.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8723.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8721.md")
</aside>
<h2 id="configuration-options">Configuration options</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>appId</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>The Flagship app ID from the Cloudflare dashboard.</td>
</tr>
<tr>
<td><code>accountId</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>Your Cloudflare account ID.</td>
</tr>
<tr>
<td><code>authToken</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>A Cloudflare <a href="/flagship/api-tokens/">API token</a> with Flagship Evaluate or Flagship App Evaluate permission.</td>
</tr>
<tr>
<td><code>fetchOptions</code></td>
<td><code>RequestInit</code></td>
<td>No</td>
<td>Custom fetch options applied to HTTP requests.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Request timeout in milliseconds. Defaults to <code>5000</code>.</td>
</tr>
<tr>
<td><code>retries</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Retry attempts on transient errors. Defaults to <code>1</code> and is capped at <code>10</code>.</td>
</tr>
<tr>
<td><code>retryDelay</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Delay between retries in milliseconds. Defaults to <code>1000</code> and is capped at <code>30000</code>.</td>
</tr>
<tr>
<td><code>prefetchFlags</code></td>
<td><code>string[]</code></td>
<td>Yes</td>
<td>Flag keys to fetch on initialization and on every context change. Flags not in this list return <code>FLAG_NOT_FOUND</code> at evaluation time.</td>
</tr>
</tbody>
</table>
<h2 id="when-to-use-the-client-provider">When to use the client provider</h2>
<p>Use the client provider in browser applications, single-page apps, or any client-side JavaScript environment.</p>
<p>Evaluations are synchronous, so they do not block rendering. Flag values are fetched once during initialization and re-fetched whenever the evaluation context changes. To force a refresh, update the context via <code>OpenFeature.setContext(...)</code>.</p>
