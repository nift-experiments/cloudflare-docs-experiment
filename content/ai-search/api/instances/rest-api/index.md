---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/api/instances/rest-api/
  description: Manage AI Search instances and sync jobs over HTTP using the Instances REST API.
  full_title: REST API · Cloudflare AI Search docs
  head_html: <title>REST API · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage AI Search instances and sync jobs over HTTP using the Instances REST API."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/api/instances/rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/api/instances/rest-api/index.md"><meta property="og:title" content="REST API · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage AI Search instances and sync jobs over HTTP using the Instances REST API."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/api/instances/rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/api/instances/rest-api/#page","headline":"REST API \u00b7 Cloudflare AI Search docs","description":"Manage AI Search instances and sync jobs over HTTP using the Instances REST API.","url":"https://developers.cloudflare.com/ai-search/api/instances/rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/api/instances/rest-api/
  schema: 1
---
<p>Use the AI Search REST API to manage instances and sync jobs over HTTP.</p>
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
<p>AI Search scopes Instance APIs to a <a href="/ai-search/concepts/namespaces/">namespace</a>:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/accounts/{account_id}/ai-search/namespaces/{namespace}/instances/{id}</code></td>
<td>Operates on instances within a namespace</td>
</tr>
</tbody>
</table>
<p>Every account has a <code>default</code> namespace. Use <code>default</code> unless you created a custom namespace. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<h2 id="instances">Instances</h2>
<p>Create, list, get, update, and delete AI Search instances. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/">Instances API reference</a>.</p>
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
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/">Create</a></td>
<td><code>POST</code></td>
<td>Create a new instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/list/">List</a></td>
<td><code>GET</code></td>
<td>List all instances</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/read/">Get</a></td>
<td><code>GET</code></td>
<td>Get an instance by ID</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/update/">Update</a></td>
<td><code>PUT</code></td>
<td>Update instance configuration</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/delete/">Delete</a></td>
<td><code>DELETE</code></td>
<td>Delete an instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/stats/">Stats</a></td>
<td><code>GET</code></td>
<td>Get indexing statistics</td>
</tr>
</tbody>
</table>
<h3 id="example-create-an-instance">Example: Create an instance</h3>
<p>Create an instance in the default namespace:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="jobs">Jobs</h2>
<p>Trigger and monitor <a href="/ai-search/configuration/indexing/syncing/">sync jobs</a> that scan your data source and index new or updated content. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/">Jobs API reference</a>.</p>
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
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create/">Create</a></td>
<td><code>POST</code></td>
<td>Trigger a new sync job</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/list/">List</a></td>
<td><code>GET</code></td>
<td>List all jobs for an instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/get/">Get</a></td>
<td><code>GET</code></td>
<td>Get job details</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/logs/">Logs</a></td>
<td><code>GET</code></td>
<td>View job logs</td>
</tr>
</tbody>
</table>
<h3 id="example-trigger-a-sync-job">Example: Trigger a sync job</h3>
<p>Start a new sync job for an instance:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/jobs&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
