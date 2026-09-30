---
cp9:
  canonical: https://developers.cloudflare.com/flagship/api-tokens/
  description: Create account-wide or app-scoped API tokens for Flagship. App-scoped tokens can access only the Flagship apps you select.
  full_title: API tokens · Cloudflare Flagship docs
  head_html: <title>API tokens · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Create account-wide or app-scoped API tokens for Flagship. App-scoped tokens can access only the Flagship apps you select."><link rel="canonical" href="https://developers.cloudflare.com/flagship/api-tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/api-tokens/index.md"><meta property="og:title" content="API tokens · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create account-wide or app-scoped API tokens for Flagship. App-scoped tokens can access only the Flagship apps you select."><meta property="og:url" content="https://developers.cloudflare.com/flagship/api-tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/api-tokens/#page","headline":"API tokens \u00b7 Cloudflare Flagship docs","description":"Create account-wide or app-scoped API tokens for Flagship. App-scoped tokens can access only the Flagship apps you select.","url":"https://developers.cloudflare.com/flagship/api-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/api-tokens/
  schema: 1
---
<p>Flagship supports two kinds of API tokens. Both use the same <a href="/fundamentals/api/get-started/create-token/">Create API token</a> flow. The difference is the resource the permission policy applies to.</p>
<table>
<thead>
<tr>
<th>Token type</th>
<th>Resource</th>
<th>What it can access</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account-wide</td>
<td><strong>Entire Account</strong></td>
<td>Every Flagship app in the account</td>
</tr>
<tr>
<td>App-scoped</td>
<td><strong>Specified Flagship apps</strong></td>
<td>Only the Flagship apps you select</td>
</tr>
</tbody>
</table>
<p>Use an account-wide token when a trusted server-side workflow needs access to every Flagship app. Use an app-scoped token when that workflow should only touch the apps you select — for example, CI or a backend service for one product.</p>
<p>Both token types support <strong>Read</strong>, <strong>Write</strong>, and <strong>Evaluate</strong>. The names change with the resource:</p>
<table>
<thead>
<tr>
<th>Access</th>
<th>Account-wide</th>
<th>App-scoped</th>
</tr>
</thead>
<tbody>
<tr>
<td>Evaluate flags</td>
<td><strong>Flagship Evaluate</strong></td>
<td><strong>Flagship App Evaluate</strong></td>
</tr>
<tr>
<td>Read flag configuration</td>
<td><strong>Flagship Read</strong></td>
<td><strong>Flagship App Read</strong></td>
</tr>
<tr>
<td>Manage flags</td>
<td><strong>Flagship Write</strong></td>
<td><strong>Flagship App Write</strong></td>
</tr>
</tbody>
</table>
<p>You must <a href="/flagship/get-started/#create-an-app-and-a-flag">create a Flagship app</a> before you can create an app-scoped token. The dashboard can only list apps that already exist.</p>
<h2 id="create-an-account-wide-token">Create an account-wide token</h2>
<p><a href="https://dash.cloudflare.com/?to=/:account/api-tokens">Create an account-wide Flagship token</a> to open the Account API tokens page. Then create a custom token and leave the resource set to <strong>Entire Account</strong>.</p>
<p>To create the token yourself:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<p>You can also create a user token from <a href="https://dash.cloudflare.com/profile/api-tokens">My Profile</a> &gt; <strong>API Tokens</strong>.</p>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong> &gt; <strong>Get started</strong>.</li>
<li>Enter a token name.</li>
<li>Under <strong>Permission policies</strong>, leave the resource dropdown set to <strong>Entire Account</strong>.</li>
<li>Search for Flagship and select <strong>Flagship Evaluate</strong>, <strong>Flagship Read</strong>, or <strong>Flagship Write</strong>.</li>
<li>(Optional) Restrict the token with <a href="/fundamentals/api/how-to/restrict-tokens/">IP address filtering or a TTL</a>.</li>
<li>Select <strong>Review token</strong> &gt; <strong>Create Token</strong>.</li>
<li>Copy the token secret and store it securely.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/1021.md")
</aside>
<h2 id="create-an-app-scoped-token">Create an app-scoped token</h2>
<p><a href="https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&amp;scope=specified_flagship_app">Create an app-scoped Flagship token</a> to open the token form with <strong>Specified Flagship apps</strong> and <strong>Flagship App Evaluate</strong> already selected. Then choose the app and create the token.</p>
<p>To create the token yourself:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<p>You can also create a user token from <a href="https://dash.cloudflare.com/profile/api-tokens">My Profile</a> &gt; <strong>API Tokens</strong>.</p>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong> &gt; <strong>Get started</strong>.</li>
<li>Enter a token name that describes where you will use it, such as <code>checkout-service-ci</code>.</li>
<li>Under <strong>Permission policies</strong>, open the resource dropdown (it defaults to <strong>Entire Account</strong>) and select <strong>Specified Flagship apps</strong>.</li>
<li>In <strong>Select Flagship apps</strong>, choose the app or apps this token should access.</li>
<li>Under <strong>Developer Platform</strong>, select a <strong>Flagship App</strong> permission:</li>
</ol>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>Evaluate flags in the selected apps</td>
<td><strong>Flagship App Evaluate</strong></td>
</tr>
<tr>
<td>Read flag configuration for the selected apps</td>
<td><strong>Flagship App Read</strong></td>
</tr>
<tr>
<td>Manage flags in the selected apps</td>
<td><strong>Flagship App Write</strong></td>
</tr>
</tbody>
</table>
<ol start="8">
<li>(Optional) Restrict the token with <a href="/fundamentals/api/how-to/restrict-tokens/">IP address filtering or a TTL</a>.</li>
<li>Select <strong>Review token</strong> &gt; <strong>Create Token</strong>.</li>
<li>Copy the token secret and store it securely.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning-1">Warning</h3>
@markup("md", "content/.markup/bodies/1020.md")
</aside>
<h2 id="use-the-token">Use the token</h2>
<p>Pass the token to an OpenFeature SDK as <code>authToken</code> (TypeScript) or the equivalent option in <a href="/flagship/sdk/python/">Python</a> and <a href="/flagship/sdk/go/">Go</a>.</p>
<pre tabindex="0"><code class="language-ts">import { OpenFeature } from &quot;@openfeature/server-sdk&quot;;&#10;import { FlagshipServerProvider } from &quot;@cloudflare/flagship/server&quot;;&#10;&#10;await OpenFeature.setProviderAndWait(&#10;	new FlagshipServerProvider({&#10;		appId: &quot;&lt;APP_ID&gt;&quot;,&#10;		accountId: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;		authToken: &quot;&lt;APP_SCOPED_API_TOKEN&gt;&quot;,&#10;	}),&#10;);&#10;</code></pre>
<p>Replace <code>&lt;APP_ID&gt;</code> and <code>&lt;ACCOUNT_ID&gt;</code> with the app and account the token is scoped to. An app-scoped token is rejected if you evaluate a different app.</p>
<p>Inside a Cloudflare Worker, prefer the <a href="/flagship/binding/">binding</a>. The binding authenticates automatically and does not need an API token.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Set up the <a href="/flagship/sdk/server-provider/">TypeScript Server SDK</a> outside of Workers.</li>
<li>Restrict token use with <a href="/fundamentals/api/how-to/restrict-tokens/">IP filtering or a TTL</a>.</li>
</ul>
