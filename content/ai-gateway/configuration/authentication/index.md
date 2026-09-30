---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/configuration/authentication/
  description: Add security by requiring a valid authorization token for each request.
  full_title: Authenticated Gateway · Cloudflare AI Gateway docs
  head_html: <title>Authenticated Gateway · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Add security by requiring a valid authorization token for each request."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/configuration/authentication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/configuration/authentication/index.md"><meta property="og:title" content="Authenticated Gateway · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add security by requiring a valid authorization token for each request."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/configuration/authentication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/configuration/authentication/#page","headline":"Authenticated Gateway \u00b7 Cloudflare AI Gateway docs","description":"Add security by requiring a valid authorization token for each request.","url":"https://developers.cloudflare.com/ai-gateway/configuration/authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/configuration/authentication/
  schema: 1
---
<p>AI Gateway requires a valid Cloudflare API token for each request. This prevents unauthorized access and protects against invalid requests that can inflate log storage usage.</p>
<p>When using the <a href="/ai-gateway/usage/rest-api/">REST API</a>, pass your Cloudflare API token in the standard <code>Authorization</code> header. When using <a href="/ai-gateway/usage/providers/">provider-native endpoints</a> at <code>gateway.ai.cloudflare.com</code>, use the <code>cf-aig-authorization</code> header instead.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2890.md")
</aside>
<h2 id="setting-up-authenticated-gateway-using-the-dashboard">Setting up Authenticated Gateway using the dashboard</h2>
<ol>
<li>Go to the Settings for the specific gateway you want to enable authentication for.</li>
<li>Select <strong>Create authentication token</strong> to generate a custom token with the required <code>Run</code> permissions. Be sure to securely save this token, as it will not be displayed again.</li>
<li>Include the API token in each request:
<ul>
<li>If using the REST API (<code>/ai/run</code>), include your Cloudflare API token in the standard <code>Authorization</code> header.</li>
<li>If using <a href="/ai-gateway/usage/providers/">provider-native endpoints</a> at <code>gateway.ai.cloudflare.com</code>, use the <code>cf-aig-authorization</code> header.</li>
</ul>
</li>
<li>Return to the settings page and toggle on Authenticated Gateway.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="ai-gateway-api-tokens-are-account-scoped">AI Gateway API tokens are account-scoped</h3>
@markup("md", "content/.markup/bodies/2889.md")
</aside>
<h2 id="example-requests">Example requests</h2>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,&#10;&#35; and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.&#10;curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&quot;model&quot;: &quot;openai/gpt-4.1-mini&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Using the OpenAI SDK:</p>
<pre tabindex="0"><code class="language-javascript">import OpenAI from &quot;openai&quot;;&#10;&#10;const openai = new OpenAI({&#10;	apiKey: CLOUDFLARE_API_TOKEN,&#10;	baseURL: `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/ai/v1`,&#10;});&#10;&#10;const response = await openai.chat.completions.create({&#10;	model: &quot;openai/gpt-4.1-mini&quot;,&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;</code></pre>
<p>Using the Vercel AI SDK:</p>
<pre tabindex="0"><code class="language-javascript">import { createOpenAI } from &quot;@ai-sdk/openai&quot;;&#10;&#10;const openai = createOpenAI({&#10;	apiKey: CLOUDFLARE_API_TOKEN,&#10;	baseURL: `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/ai/v1`,&#10;});&#10;</code></pre>
<h2 id="expected-behavior">Expected behavior</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2888.md")
</aside>
<p>The following table outlines gateway behavior based on the authentication settings and header status:</p>
<table>
<thead>
<tr>
<th>Authentication Setting</th>
<th>Header Info</th>
<th>Gateway State</th>
<th>Response</th>
</tr>
</thead>
<tbody>
<tr>
<td>On</td>
<td>Header present</td>
<td>Authenticated gateway</td>
<td>Request succeeds</td>
</tr>
<tr>
<td>On</td>
<td>No header</td>
<td>Error</td>
<td>Request fails due to missing authorization</td>
</tr>
<tr>
<td>Off</td>
<td>Header present</td>
<td>Unauthenticated gateway</td>
<td>Request succeeds</td>
</tr>
<tr>
<td>Off</td>
<td>No header</td>
<td>Unauthenticated gateway</td>
<td>Request succeeds</td>
</tr>
</tbody>
</table>
