---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/
  description: Create a service API token to grant AI Search read access to R2 buckets for indexing.
  full_title: Service API token · Cloudflare AI Search docs
  head_html: <title>Service API token · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a service API token to grant AI Search read access to R2 buckets for indexing."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/index.md"><meta property="og:title" content="Service API token · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a service API token to grant AI Search read access to R2 buckets for indexing."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/#page","headline":"Service API token \u00b7 Cloudflare AI Search docs","description":"Create a service API token to grant AI Search read access to R2 buckets for indexing.","url":"https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/indexing/service-api-token/
  schema: 1
---
<p>A service API token grants AI Search permission to access <a href="/r2/">R2</a> buckets in your account. This token is only required if you connect an R2 bucket as a data source. If you use a website or upload files directly through the <a href="/ai-search/api/items/workers-binding/">Items API</a>, you do not need a service API token.</p>
<h2 id="when-you-need-a-service-api-token">When you need a service API token</h2>
<p>You need a service API token when you create an AI Search instance with <code>type: &quot;r2&quot;</code>. The token authorizes AI Search to read objects from your R2 bucket for indexing.</p>
<h2 id="create-via-the-dashboard-or-wrangler">Create via the dashboard or Wrangler</h2>
<p>The simplest way to get a service API token is to create an R2-backed AI Search instance through the <a href="/ai-search/get-started/dashboard/">dashboard</a> or <a href="/ai-search/get-started/wrangler/">Wrangler CLI</a> at least once. Cloudflare creates and registers a service token for you automatically during the setup flow.</p>
<p>Once created, the token is saved to your account and reused across all AI Search instances. You do not need to create a new token for each instance.</p>
<h2 id="create-via-the-api">Create via the API</h2>
<p>If you need to create a service API token programmatically, follow these steps.</p>
<h3 id="1-create-an-api-token-with-token-creation-permissions"><ol>
<li>Create an API token with token creation permissions</li>
</ol></h3>
<p>You need an <a href="/fundamentals/api/get-started/create-token/">API token</a> with permission to create other tokens.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong>.</li>
<li>Enter a <strong>Token name</strong>, for example <code>Token Creator</code>.</li>
<li>Under <strong>Permissions</strong>, select <strong>User</strong> &gt; <strong>API Tokens</strong> &gt; <strong>Edit</strong>.</li>
<li>Select <strong>Continue to summary</strong>, then select <strong>Create Token</strong>.</li>
<li>Copy and save the token value. This is your <code>CREATOR_TOKEN</code>.</li>
</ol>
<h3 id="2-create-the-service-token"><ol start="2">
<li>Create the service token</li>
</ol></h3>
<p>Use the <a href="/api/resources/user/subresources/tokens/methods/create/">Create token API</a> to create a service token with the AI Search Index Engine permission. Replace <code>&lt;CREATOR_TOKEN&gt;</code> with the token from step 1 and <code>&lt;ACCOUNT_ID&gt;</code> with your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/user/tokens&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;CREATOR_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;name&quot;: &quot;AI Search Service API Token&quot;,&#10;    &quot;policies&quot;: [&#10;      {&#10;        &quot;effect&quot;: &quot;allow&quot;,&#10;        &quot;resources&quot;: {&#10;          &quot;com.cloudflare.api.account.&lt;ACCOUNT_ID&gt;&quot;: &quot;*&quot;&#10;        },&#10;        &quot;permission_groups&quot;: [&#10;          { &quot;id&quot;: &quot;9e9b428a0bcd46fd80e580b46a69963c&quot; }&#10;        ]&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>Save the <code>id</code> and <code>value</code> from the response:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;CF_API_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;AI Search Service API Token&quot;,&#10;		&quot;status&quot;: &quot;active&quot;,&#10;		&quot;value&quot;: &quot;&lt;CF_API_KEY&gt;&quot;&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<h3 id="3-register-the-token-with-ai-search"><ol start="3">
<li>Register the token with AI Search</li>
</ol></h3>
<p>Use the <a href="/api/resources/ai_search/subresources/tokens/methods/create/">AI Search tokens API</a> to register the service token. Replace <code>&lt;API_TOKEN&gt;</code> with an API token that has AI Search Edit permissions.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/tokens&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;cf_api_id&quot;: &quot;&lt;CF_API_ID&gt;&quot;,&#10;    &quot;cf_api_key&quot;: &quot;&lt;CF_API_KEY&gt;&quot;,&#10;    &quot;name&quot;: &quot;AI Search Service Token&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Save the <code>id</code> from the response. This is your <code>token_id</code> to pass when creating R2-backed instances:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;TOKEN_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;AI Search Service Token&quot;,&#10;		&quot;cf_api_id&quot;: &quot;&lt;CF_API_ID&gt;&quot;,&#10;		&quot;created_at&quot;: &quot;2025-12-25 01:52:28&quot;,&#10;		&quot;enabled&quot;: true&#10;	}&#10;}&#10;</code></pre>
<h3 id="4-use-the-token-when-creating-an-instance"><ol start="4">
<li>Use the token when creating an instance</li>
</ol></h3>
<p>Pass the <code>token_id</code> when creating an R2-backed instance:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;id&quot;: &quot;my-r2-docs&quot;,&#10;    &quot;type&quot;: &quot;r2&quot;,&#10;    &quot;source&quot;: &quot;&lt;R2_BUCKET_NAME&gt;&quot;,&#10;    &quot;token_id&quot;: &quot;&lt;TOKEN_ID&gt;&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="manage-your-token">Manage your token</h2>
<p>Once registered, the service API token is stored securely and reused across all AI Search instances in your account.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3080.md")
</aside>
<h3 id="rotate-your-token">Rotate your token</h3>
<p>To create a new service API token from the dashboard:</p>
<ol>
<li>Go to an existing AI Search instance in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Settings</strong>.</li>
<li>Under <strong>General</strong>, find <strong>Service API Token</strong> and select the edit icon.</li>
<li>Select <strong>Create a new token</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To create a new token via the API, follow <a href="#1-create-an-api-token-with-token-creation-permissions">steps 1 through 3</a> above.</p>
<h3 id="view-registered-tokens">View registered tokens</h3>
<p>List the service API tokens registered with AI Search in your account:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/tokens \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
