---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/api/items/rest-api/
  description: Upload, list, and manage documents in AI Search instances using the Items REST API.
  full_title: REST API · Cloudflare AI Search docs
  head_html: <title>REST API · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload, list, and manage documents in AI Search instances using the Items REST API."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/api/items/rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/api/items/rest-api/index.md"><meta property="og:title" content="REST API · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload, list, and manage documents in AI Search instances using the Items REST API."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/api/items/rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/api/items/rest-api/#page","headline":"REST API \u00b7 Cloudflare AI Search docs","description":"Upload, list, and manage documents in AI Search instances using the Items REST API.","url":"https://developers.cloudflare.com/ai-search/api/items/rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/api/items/rest-api/
  schema: 1
---
<p>Use the AI Search REST API to upload, list, and manage individual documents within an instance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3073.md")
</aside>
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
<h2 id="api-paths">API paths</h2>
<p>Item APIs are scoped to a <a href="/ai-search/concepts/namespaces/">namespace</a>:</p>
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
<td>Operates on instances within a namespace</td>
</tr>
</tbody>
</table>
<p>Every account has a <code>default</code> namespace. Use <code>default</code> unless you created a custom namespace. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<h2 id="items">Items</h2>
<p>Upload, list, get, delete, and download items within an instance. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/">Items API reference</a>.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/">Upload</a></td>
<td><code>POST</code></td>
<td>Upload a document for indexing</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list/">List</a></td>
<td><code>GET</code></td>
<td>List all items in an instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get/">Get</a></td>
<td><code>GET</code></td>
<td>Get item info by ID</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/delete/">Delete</a></td>
<td><code>DELETE</code></td>
<td>Delete an item</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/download/">Download</a></td>
<td><code>GET</code></td>
<td>Download the original file</td>
</tr>
</tbody>
</table>
<h3 id="example-upload-a-document">Example: Upload a document</h3>
<p>Upload a file to an instance:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/items&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;F &quot;file=@/path/to/your/file.pdf&quot;&#10;</code></pre>
<h3 id="example-list-items">Example: List items</h3>
<p>List all items in an instance:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/items&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>To find a single item by its exact object key, pass the <code>key</code> query parameter:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/items?key=docs/readme.md&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Keys are unique per data source, so combine <code>key</code> with <code>source</code> (for example, <code>source=builtin</code>) to disambiguate when the same key exists across multiple sources.</p>
