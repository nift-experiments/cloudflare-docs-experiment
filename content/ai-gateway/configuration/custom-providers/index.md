---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/
  description: Create and manage custom AI providers for your account.
  full_title: Custom Providers · Cloudflare AI Gateway docs
  head_html: <title>Custom Providers · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage custom AI providers for your account."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/index.md"><meta property="og:title" content="Custom Providers · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage custom AI providers for your account."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/#page","headline":"Custom Providers \u00b7 Cloudflare AI Gateway docs","description":"Create and manage custom AI providers for your account.","url":"https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/configuration/custom-providers/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>Custom Providers allow you to integrate AI providers that are not natively supported by AI Gateway. This feature enables you to use AI Gateway's observability, caching, rate limiting, and other features with any AI provider that has an HTTPS API endpoint.</p>
<h2 id="use-cases">Use cases</h2>
<ul>
<li><strong>Internal AI models</strong>: Connect to your organization's self-hosted AI models</li>
<li><strong>Regional providers</strong>: Integrate with AI providers specific to your region</li>
<li><strong>Specialized models</strong>: Use domain-specific AI services not available through standard providers</li>
<li><strong>Custom endpoints</strong>: Route requests to your own AI infrastructure</li>
</ul>
<h2 id="before-you-begin">Before you begin</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>An active Cloudflare account with AI Gateway access</li>
<li>A valid API key from your custom AI provider</li>
<li>The HTTPS base URL for your provider's API</li>
</ul>
<h3 id="authentication">Authentication</h3>
<p>The API endpoints for creating, reading, updating, or deleting custom providers require authentication. You need to create a Cloudflare API token with the appropriate permissions.</p>
<p>To create an API token:</p>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/?to=:account/api-tokens">Cloudflare dashboard API tokens page</a></li>
<li>Click <strong>Create Token</strong></li>
<li>Select <strong>Custom Token</strong> and add the following permissions:
<ul>
<li><code>AI Gateway - Edit</code></li>
</ul>
</li>
<li>Click <strong>Continue to summary</strong> and then <strong>Create Token</strong></li>
<li>Copy the token - you'll use it in the <code>Authorization: Bearer $CLOUDFLARE_API_TOKEN</code> header</li>
</ol>
<h2 id="create-a-custom-provider">Create a custom provider</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2871.md")
</div></div>
<h2 id="list-custom-providers">List custom providers</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2874.md")
</div></div>
<h2 id="get-a-specific-custom-provider">Get a specific custom provider</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2876.md")
</div></div>
<h2 id="update-a-custom-provider">Update a custom provider</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2879.md")
</div></div>
<h2 id="delete-a-custom-provider">Delete a custom provider</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2882.md")
</div></div>
<h2 id="using-custom-providers-with-ai-gateway">Using custom providers with AI Gateway</h2>
<p>Once you've created a custom provider, you can route requests through AI Gateway using one of two approaches: the <strong>Unified API</strong> or the <strong>provider-specific endpoint</strong>. When referencing your custom provider with either approach, you must prefix the slug with <code>custom-</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-provider-prefix">Custom provider prefix</h3>
@markup("md", "content/.markup/bodies/2864.md")
</aside>
<h3 id="how-url-routing-works">How URL routing works</h3>
<p>When AI Gateway receives a request for a custom provider, it constructs the upstream URL by combining the provider's configured <code>base_url</code> with the path that comes after <code>custom-{slug}/</code> in the gateway URL.</p>
<p><strong>The <code>base_url</code> field should contain only the root domain</strong> (or domain with a fixed prefix) of the provider's API. Any API-specific path segments (like <code>/v1/chat/completions</code>) go in the request URL, not in <code>base_url</code>.</p>
<p>The formula is:</p>
<pre tabindex="0"><code>Gateway URL:   https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-{slug}/{provider-path}&#10;Upstream URL:  {base_url}/{provider-path}&#10;</code></pre>
<p>Everything after <code>custom-{slug}/</code> in your request URL is appended directly to the <code>base_url</code> to form the final upstream URL. This means <code>{provider-path}</code> can include multiple path segments, query parameters, or any path structure your provider requires.</p>
<h3 id="choosing-between-unified-api-and-provider-specific-endpoint">Choosing between Unified API and provider-specific endpoint</h3>
<table>
<thead>
<tr>
<th></th>
<th>Unified API (<code>/compat</code>)</th>
<th>Provider-specific endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Best for</strong></td>
<td>Providers with OpenAI-compatible APIs</td>
<td>Providers with any API structure</td>
</tr>
<tr>
<td><strong>Request format</strong></td>
<td>Must follow the OpenAI <code>/chat/completions</code> schema</td>
<td>Uses the provider's native request format</td>
</tr>
<tr>
<td><strong>Path control</strong></td>
<td>Fixed to <code>/compat/chat/completions</code></td>
<td>Full control over the upstream path</td>
</tr>
<tr>
<td><strong>How to specify the provider</strong></td>
<td><code>model</code> field: <code>custom-{slug}/{model-name}</code></td>
<td>URL path: <code>/custom-{slug}/{path}</code></td>
</tr>
</tbody>
</table>
<p>Use the <strong>Unified API</strong> when your custom provider accepts the OpenAI-compatible <code>/chat/completions</code> request format. This is the simplest option and works well with OpenAI SDKs.</p>
<p>Use the <strong>provider-specific endpoint</strong> when your custom provider uses a non-standard API path or request format. This gives you full control over both the URL path and the request body sent to the upstream provider.</p>
<h3 id="via-unified-api">Via Unified API</h3>
<p>The Unified API sends requests to the provider's chat completions endpoint using the OpenAI-compatible format. Specify the model using the format <code>custom-{slug}/{model-name}</code>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler auth token` to get an auth token to replace $CF_AIG_TOKEN for use with the API.&#10;curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \&#10;  &#45;H &quot;Authorization: Bearer $PROVIDER_API_KEY&quot; \&#10;  &#45;H &quot;cf-aig-authorization: Bearer $CF_AIG_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;custom-some-provider/model-name&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}]&#10;  }&#x27;&#10;</code></pre>
<h3 id="via-provider-specific-endpoint">Via provider-specific endpoint</h3>
<p>The provider-specific endpoint gives you full control over the upstream path. Everything after <code>custom-{slug}/</code> in the URL is appended to the <code>base_url</code>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Run `wrangler auth token` to get an auth token to replace $CF_AIG_TOKEN for use with the API.&#10;curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-some-provider/v1/chat/completions \&#10;  &#45;H &quot;Authorization: Bearer $PROVIDER_API_KEY&quot; \&#10;  &#45;H &quot;cf-aig-authorization: Bearer $CF_AIG_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;model-name&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>If <code>base_url</code> is <code>https://api.myprovider.com</code>, this request is proxied to: <code>https://api.myprovider.com/v1/chat/completions</code></p>
<h3 id="examples">Examples</h3>
<p>The following examples show how to configure <code>base_url</code> and construct request URLs for different types of providers.</p>
<h4 id="example-1-openai-compatible-provider-standard-v1-path">Example 1: OpenAI-compatible provider (standard <code>/v1/</code> path)</h4>
<p>Many providers follow the OpenAI convention of hosting their API at <code>{domain}/v1/chat/completions</code>.</p>
<p><strong>Configuration:</strong></p>
<ul>
<li><code>slug</code>: <code>my-openai-compat</code></li>
<li><code>base_url</code>: <code>https://api.example-provider.com</code></li>
</ul>
<p><strong>Provider-specific endpoint:</strong></p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-my-openai-compat/v1/chat/completions \&#10;  &#45;H &quot;Authorization: Bearer $PROVIDER_API_KEY&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;example-model&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p><strong>URL mapping:</strong></p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gateway URL</td>
<td><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-my-openai-compat/v1/chat/completions</code></td>
</tr>
<tr>
<td><code>base_url</code></td>
<td><code>https://api.example-provider.com</code></td>
</tr>
<tr>
<td>Provider path</td>
<td><code>/v1/chat/completions</code></td>
</tr>
<tr>
<td>Upstream URL</td>
<td><code>https://api.example-provider.com/v1/chat/completions</code></td>
</tr>
</tbody>
</table>
<p>Since this provider is OpenAI-compatible, you could also use the Unified API:</p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \&#10;  &#45;H &quot;Authorization: Bearer $PROVIDER_API_KEY&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;custom-my-openai-compat/example-model&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}]&#10;  }&#x27;&#10;</code></pre>
<h4 id="example-2-provider-with-a-non-standard-api-path">Example 2: Provider with a non-standard API path</h4>
<p>Some providers use API paths that don't follow the <code>/v1/</code> convention. For example, a provider whose chat endpoint is at <code>https://api.custom-ai.com/api/coding/paas/v4/chat/completions</code>.</p>
<p><strong>Configuration:</strong></p>
<ul>
<li><code>slug</code>: <code>custom-ai</code></li>
<li><code>base_url</code>: <code>https://api.custom-ai.com</code></li>
</ul>
<p><strong>Provider-specific endpoint:</strong></p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-custom-ai/api/coding/paas/v4/chat/completions \&#10;  &#45;H &quot;Authorization: Bearer $PROVIDER_API_KEY&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;custom-ai-model&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p><strong>URL mapping:</strong></p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gateway URL</td>
<td><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-custom-ai/api/coding/paas/v4/chat/completions</code></td>
</tr>
<tr>
<td><code>base_url</code></td>
<td><code>https://api.custom-ai.com</code></td>
</tr>
<tr>
<td>Provider path</td>
<td><code>/api/coding/paas/v4/chat/completions</code></td>
</tr>
<tr>
<td>Upstream URL</td>
<td><code>https://api.custom-ai.com/api/coding/paas/v4/chat/completions</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2863.md")
</aside>
<h4 id="example-3-self-hosted-model-with-a-path-prefix">Example 3: Self-hosted model with a path prefix</h4>
<p>If you host your own model behind a reverse proxy or on a platform that adds a path prefix, include only the fixed prefix portion in <code>base_url</code> if all your endpoints share it. Otherwise, keep <code>base_url</code> as just the domain.</p>
<p><strong>Configuration (domain-only <code>base_url</code>):</strong></p>
<ul>
<li><code>slug</code>: <code>internal-llm</code></li>
<li><code>base_url</code>: <code>https://ml.internal.example.com</code></li>
</ul>
<p><strong>Provider-specific endpoint:</strong></p>
<pre tabindex="0"><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-internal-llm/serving/models/my-model:predict \&#10;  &#45;H &quot;Authorization: Bearer $INTERNAL_API_KEY&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;instances&quot;: [{&quot;prompt&quot;: &quot;Summarize the following text:&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p><strong>URL mapping:</strong></p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gateway URL</td>
<td><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-internal-llm/serving/models/my-model:predict</code></td>
</tr>
<tr>
<td><code>base_url</code></td>
<td><code>https://ml.internal.example.com</code></td>
</tr>
<tr>
<td>Provider path</td>
<td><code>/serving/models/my-model:predict</code></td>
</tr>
<tr>
<td>Upstream URL</td>
<td><code>https://ml.internal.example.com/serving/models/my-model:predict</code></td>
</tr>
</tbody>
</table>
<h4 id="example-4-provider-using-openai-sdk-with-a-custom-base-url">Example 4: Provider using OpenAI SDK with a custom base URL</h4>
<p>When using the OpenAI SDK to connect to a custom provider through AI Gateway, set the SDK's <code>base_url</code> to the gateway's provider-specific endpoint path (up to and including the API version prefix that your provider expects).</p>
<p><strong>Configuration:</strong></p>
<ul>
<li><code>slug</code>: <code>alt-provider</code></li>
<li><code>base_url</code>: <code>https://api.alt-provider.com</code></li>
</ul>
<p><strong>Python (OpenAI SDK):</strong></p>
<pre tabindex="0"><code class="language-python">from openai import OpenAI&#10;&#10;client = OpenAI(&#10;    api_key=&quot;your-provider-api-key&quot;,&#10;    base_url=&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-alt-provider/v1&quot;,&#10;    default_headers={&#10;        &quot;cf-aig-authorization&quot;: &quot;Bearer {cf_aig_token}&quot;,&#10;    },&#10;)&#10;&#10;&#35; The SDK appends /chat/completions to the base_url automatically.&#10;&#35; Final upstream URL: https://api.alt-provider.com/v1/chat/completions&#10;response = client.chat.completions.create(&#10;    model=&quot;alt-model-v2&quot;,&#10;    messages=[{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;}],&#10;)&#10;</code></pre>
<p><strong>URL mapping:</strong></p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SDK <code>base_url</code></td>
<td><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-alt-provider/v1</code></td>
</tr>
<tr>
<td>SDK appends</td>
<td><code>/chat/completions</code></td>
</tr>
<tr>
<td>Full gateway URL</td>
<td><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/custom-alt-provider/v1/chat/completions</code></td>
</tr>
<tr>
<td>Provider <code>base_url</code></td>
<td><code>https://api.alt-provider.com</code></td>
</tr>
<tr>
<td>Provider path</td>
<td><code>/v1/chat/completions</code></td>
</tr>
<tr>
<td>Upstream URL</td>
<td><code>https://api.alt-provider.com/v1/chat/completions</code></td>
</tr>
</tbody>
</table>
<h2 id="common-errors">Common errors</h2>
<h3 id="409-conflict-duplicate-slug">409 Conflict - Duplicate slug</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 1003,&#10;			&quot;message&quot;: &quot;A custom provider with this slug already exists&quot;,&#10;			&quot;path&quot;: [&quot;body&quot;, &quot;slug&quot;]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Each custom provider slug must be unique within your account. Choose a different slug or update the existing provider.</p>
<h3 id="404-not-found">404 Not Found</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 1004,&#10;			&quot;message&quot;: &quot;Custom Provider not found&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>The specified provider ID does not exist or you don't have access to it. Verify the provider ID and your authentication credentials.</p>
<h3 id="400-bad-request-invalid-base-url">400 Bad Request - Invalid base_url</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 1002,&#10;			&quot;message&quot;: &quot;base_url must be a valid HTTPS URL starting with https://&quot;,&#10;			&quot;path&quot;: [&quot;body&quot;, &quot;base_url&quot;]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>The <code>base_url</code> field must be a valid HTTPS URL. HTTP URLs are not supported for security reasons.</p>
<h3 id="404-when-making-requests-to-a-custom-provider">404 when making requests to a custom provider</h3>
<p>If you receive a 404 from the upstream provider, the most common cause is an incorrect path mapping. Verify that:</p>
<ol>
<li>Your <code>base_url</code> is set to the provider's <strong>root domain</strong> (for example, <code>https://api.provider.com</code>) rather than including API path segments.</li>
<li>Your request URL includes the <strong>full API path</strong> after <code>custom-{slug}/</code>. For example, if the upstream endpoint is <code>https://api.provider.com/api/v2/chat</code>, your gateway URL should end in <code>/custom-{slug}/api/v2/chat</code>.</li>
<li>There is no duplicate or missing path segment. A common mistake is including <code>/v1</code> in both <code>base_url</code> and the request path, resulting in the upstream receiving <code>/v1/v1/chat/completions</code>.</li>
</ol>
<h2 id="best-practices">Best practices</h2>
<ol>
<li><strong>Use descriptive slugs</strong>: Choose slugs that clearly identify the provider (e.g., <code>internal-gpt</code>, <code>regional-ai</code>)</li>
<li><strong>Document your integrations</strong>: Use the <code>curl_example</code> and <code>js_example</code> fields to provide usage examples</li>
<li><strong>Enable gradually</strong>: Test with <code>enable: false</code> before making the provider active</li>
<li><strong>Monitor usage</strong>: Use AI Gateway's analytics to track requests to your custom providers</li>
<li><strong>Secure your endpoints</strong>: Ensure your custom provider's base URL implements proper authentication and authorization</li>
<li><strong>Use BYOK</strong>: Store provider API keys securely using <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a> instead of including them in every request</li>
</ol>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Custom providers are account-specific and not shared across Cloudflare accounts</li>
<li>The <code>base_url</code> must use HTTPS (HTTP is not supported)</li>
<li>Provider slugs must be unique within each account</li>
<li>Cache and rate limiting settings apply globally to the provider, not per-model</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ai-gateway/get-started/">Get started with AI Gateway</a></li>
<li><a href="/ai-gateway/configuration/authentication/">Configure authentication</a></li>
<li><a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK (Store Keys)</a></li>
<li><a href="/ai-gateway/features/dynamic-routing/">Dynamic routing</a></li>
<li><a href="/ai-gateway/features/caching/">Caching</a></li>
<li><a href="/ai-gateway/features/rate-limiting/">Rate limiting</a></li>
</ul>
