---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/get-started/api/
  description: Create AI Search instances programmatically using the REST API.
  full_title: REST API · Cloudflare AI Search docs
  head_html: <title>REST API · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Create AI Search instances programmatically using the REST API."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/get-started/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/get-started/api/index.md"><meta property="og:title" content="REST API · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create AI Search instances programmatically using the REST API."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/get-started/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/get-started/api/#page","headline":"REST API \u00b7 Cloudflare AI Search docs","description":"Create AI Search instances programmatically using the REST API.","url":"https://developers.cloudflare.com/ai-search/get-started/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/get-started/api/
  schema: 1
---
<p>This guide walks you through creating an AI Search instance using the REST API.</p>
<h2 id="1-create-an-api-token"><ol>
<li>Create an API token</li>
</ol></h2>
<p>You need an API token with <strong>AI Search:Edit</strong> and <strong>AI Search:Run</strong> permissions.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong>.</li>
<li>Enter a <strong>Token name</strong>, for example <code>AI Search Manager</code>.</li>
<li>Under <strong>Permissions</strong>, add two permissions:
<ul>
<li><strong>Account</strong> &gt; <strong>AI Search:Edit</strong></li>
<li><strong>Account</strong> &gt; <strong>AI Search:Run</strong></li>
</ul>
</li>
<li>Select <strong>Continue to summary</strong>, then select <strong>Create Token</strong>.</li>
<li>Copy and save the token value. This is your <code>API_TOKEN</code>.</li>
</ol>
<h2 id="2-create-an-ai-search-instance"><ol start="2">
<li>Create an AI Search instance</li>
</ol></h2>
<p>Use the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/">Create instance API</a> to create an instance. Replace <code>&lt;ACCOUNT_ID&gt;</code> with your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;&#10;  }&#x27;&#10;</code></pre>
<h3 id="connect-a-data-source-optional">Connect a data source (optional)</h3>
<p>You can create an instance that is connected to a website or R2 bucket as a data source. AI Search indexes the content automatically.</p>
<p><strong>Website:</strong></p>
<p>Automatically crawl and index a <a href="/ai-search/configuration/data-source/website/">website</a> that you own.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source&quot;: &quot;example.com&quot;&#10;  }&#x27;&#10;</code></pre>
<p><strong>R2 bucket:</strong></p>
<p>Index documents stored in an <a href="/ai-search/configuration/data-source/r2/">R2 bucket</a>. Connecting an R2 bucket requires a <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a>. If you have never created an R2-backed instance before, you need to pass the <code>token_id</code> field in the create request. Refer to the <a href="/ai-search/configuration/indexing/service-api-token/">service API token configuration</a> for setup instructions.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;r2&quot;,&#10;    &quot;source&quot;: &quot;&lt;R2_BUCKET_NAME&gt;&quot;,&#10;    &quot;token_id&quot;: &quot;&lt;SERVICE_TOKEN_ID&gt;&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="3-add-content"><ol start="3">
<li>Add content</li>
</ol></h2>
<p>If you did not create an instance that is connected to a data source, upload files using the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/">Items API</a>. You can skip this step if you connected a website or R2 bucket.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/my-instance/items&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;F &quot;file=@/path/to/your/file.pdf&quot;&#10;</code></pre>
<p>AI Search indexes uploaded files automatically.</p>
<h2 id="4-check-indexing-status"><ol start="4">
<li>Check indexing status</li>
</ol></h2>
<p>Check if your content has finished indexing.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/my-instance/stats&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h2 id="try-it-out">Try it out</h2>
<p>Once indexing is complete, run your first query.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/my-instance/search&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I get started?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>You can also test queries in the dashboard by going to your instance and selecting the <strong>Playground</strong> tab.</p>
<h2 id="add-to-your-application">Add to your application</h2>
<div class="nb-card nb-link-card"><h3 id="card-workers-binding-ai-search-api-search-workers-binding"><a href="/ai-search/api/search/workers-binding/">Workers binding</a></h3><p>Query AI Search directly from your Workers code.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-rest-api-ai-search-api-search-rest-api"><a href="/ai-search/api/search/rest-api/">REST API</a></h3><p>Query AI Search using HTTP requests.</p></div>
