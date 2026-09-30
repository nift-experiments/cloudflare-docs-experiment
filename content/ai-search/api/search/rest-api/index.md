---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/api/search/rest-api/
  description: Query AI Search instances over HTTP using the REST API for search and chat completions.
  full_title: REST API · Cloudflare AI Search docs
  head_html: <title>REST API · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Query AI Search instances over HTTP using the REST API for search and chat completions."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/api/search/rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/api/search/rest-api/index.md"><meta property="og:title" content="REST API · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query AI Search instances over HTTP using the REST API for search and chat completions."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/api/search/rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/api/search/rest-api/#page","headline":"REST API \u00b7 Cloudflare AI Search docs","description":"Query AI Search instances over HTTP using the REST API for search and chat completions.","url":"https://developers.cloudflare.com/ai-search/api/search/rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/api/search/rest-api/
  schema: 1
---
<p>Use the AI Search REST API to query your AI Search instances over HTTP.</p>
<h2 id="authentication">Authentication</h2>
<p>All requests require an API token with <strong>AI Search:Edit</strong> and <strong>AI Search:Run</strong> permissions.</p>
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
<p>Include the token in the <code>Authorization</code> header for all requests:</p>
<pre tabindex="0"><code class="language-txt">Authorization: Bearer &lt;API_TOKEN&gt;&#10;</code></pre>
<h2 id="search-and-chat">Search and chat</h2>
<p>AI Search provides two APIs for querying an instance. Both use an OpenAI-compatible <code>messages</code> format.</p>
<ul>
<li><strong>Search</strong> returns relevant content chunks. Use this when you want to handle generation yourself or display results directly.</li>
<li><strong>Chat completions</strong> retrieves content and generates a response in one call.</li>
</ul>
<h3 id="api-paths">API paths</h3>
<p>Search and chat APIs are scoped to a <a href="/ai-search/concepts/namespaces/">namespace</a>:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/accounts/{account_id}/ai-search/namespaces/{namespace}/instances/{id}/</code></td>
<td>Operates on a specific instance within a namespace</td>
</tr>
</tbody>
</table>
<p>Every account has a <code>default</code> namespace. Use <code>default</code> unless you created a custom namespace. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<h3 id="search">Search</h3>
<p>Search a specific instance. The search endpoint also accepts a <code>query</code> string parameter. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search/">Search API reference</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/search&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="chat-completions">Chat completions</h3>
<p>Generate a response from a specific instance. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/">Chat completions API reference</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/chat/completions&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h4 id="streaming">Streaming</h4>
<p>Set <code>stream</code> to <code>true</code> to receive responses as Server-Sent Events (SSE). The retrieved chunks are sent first as a <code>chunks</code> event, followed by the streamed response.</p>
<pre tabindex="0"><code class="language-txt">event: chunks&#10;data: [{&quot;id&quot;:&quot;chunk-001&quot;,&quot;type&quot;:&quot;text&quot;,&quot;score&quot;:0.85,&quot;text&quot;:&quot;...&quot;,&quot;item&quot;:{&quot;key&quot;:&quot;about-cloudflare.md&quot;,&quot;timestamp&quot;:1775925540000},&quot;scoring_details&quot;:{&quot;vector_score&quot;:0.85}}]&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; document&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; you provided doesn&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot;&#x27;t contain&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; information&quot;}}]}&#10;&#10;data: [DONE]&#10;</code></pre>
<h2 id="cross-instance-search-and-chat">Cross-instance search and chat</h2>
<p>The search and chat completions APIs are also available at the namespace level. These work the same as the instance endpoints, but you pass an <code>instance_ids</code> array to specify which instances to query. Each chunk in the response includes an <code>instance_id</code> field identifying which instance it came from. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/&lt;NAMESPACE&gt;/search&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ],&#10;    &quot;ai_search_options&quot;: {&#10;      &quot;instance_ids&quot;: [&quot;product-docs&quot;, &quot;customer-abc123&quot;]&#10;    }&#10;  }&#x27;&#10;</code></pre>
