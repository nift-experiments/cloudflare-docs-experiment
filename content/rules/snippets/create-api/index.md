---
cp9:
  canonical: https://developers.cloudflare.com/rules/snippets/create-api/
  description: Create Snippets using the Cloudflare API.
  full_title: Configure Snippets via API · Cloudflare Rules docs
  head_html: <title>Configure Snippets via API · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create Snippets using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/rules/snippets/create-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/snippets/create-api/index.md"><meta property="og:title" content="Configure Snippets via API · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create Snippets using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/rules/snippets/create-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/snippets/create-api/#page","headline":"Configure Snippets via API \u00b7 Cloudflare Rules docs","description":"Create Snippets using the Cloudflare API.","url":"https://developers.cloudflare.com/rules/snippets/create-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/snippets/create-api/
  schema: 1
---
<p>You can create Snippets using the <a href="/fundamentals/api/">Cloudflare API</a>.</p>
<h2 id="required-permissions">Required permissions</h2>
<p>The <a href="/fundamentals/api/get-started/create-token/">API token</a> used in API requests to manage Snippets must have at least the following permission:</p>
<ul>
<li><em>Zone</em> &gt; <em>Snippets</em> &gt; <em>Edit</em></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12790.md")
</aside>
<h2 id="endpoints">Endpoints</h2>
<p>To obtain the complete endpoint, append the Snippets endpoints listed below to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{zone_id}</code> argument is the <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a> (a hexadecimal string). You can find this value in the Cloudflare dashboard.</p>
<p>The following table summarizes the available operations.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Verb + Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>List all code snippets</td>
<td><code>GET /zones/{zone_id}/snippets</code></td>
</tr>
<tr>
<td>Create/update code snippet</td>
<td><code>PUT /zones/{zone_id}/snippets/{snippet_name}</code></td>
</tr>
<tr>
<td>Get code snippet details</td>
<td><code>GET /zones/{zone_id}/snippets/{snippet_name}</code></td>
</tr>
<tr>
<td>Get code snippet content</td>
<td><code>GET /zones/{zone_id}/snippets/{snippet_name}/content</code></td>
</tr>
<tr>
<td>Delete code snippet</td>
<td><code>DELETE /zones/{zone_id}/snippets/{snippet_name}</code></td>
</tr>
<tr>
<td>List snippet rules</td>
<td><code>GET /zones/{zone_id}/snippets/snippet_rules</code></td>
</tr>
<tr>
<td>Create/update/delete snippet rules</td>
<td><code>PUT /zones/{zone_id}/snippets/snippet_rules</code></td>
</tr>
<tr>
<td>Delete all snippet rules</td>
<td><code>DELETE /zones/{zone_id}/snippets/snippet_rules</code></td>
</tr>
</tbody>
</table>
<h2 id="example-api-calls">Example API calls</h2>
<h3 id="create-update-code-snippet">Create/update code snippet</h3>
<p>To create or update a Snippet, use the following <code>PUT</code> request. The snippet is named <code>$SNIPPET_NAME</code> and the body contains the JavaScript code.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/snippets/{snippet_name} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --form &#x27;files=@example.js&#x27; \&#10;  --form &#x27;metadata={&quot;main_module&quot;: &quot;example.js&quot;}&#x27;</code></pre>
<p>The name of a snippet can only contain the characters <code>a-z</code>, <code>0-9</code>, and <code>_</code> (underscore). The name must be unique in the context of the zone. You cannot change the snippet name after creating the snippet.</p>
<p>The required body parameters are:</p>
<ul>
<li><code>files</code>: The file with your JavaScript code.</li>
<li><code>metadata</code>: Object containing <code>main_module</code>, which must match the filename of the uploaded file.</li>
</ul>
<p>To make this example work, save your JavaScript code in a file named <code>example.js</code>, and then execute <code>curl</code> command with a <code>PUT</code> request from the folder where <code>example.js</code> is located.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;created_on&quot;: &quot;2023-07-24-00:00:00&quot;,&#10;		&quot;modified_on&quot;: &quot;2023-07-24-00:00:00&quot;,&#10;		&quot;snippet_name&quot;: &quot;snippet_name_01&quot;&#10;	}&#10;}&#10;</code></pre>
<p>To deploy a new snippet you must <a href="#createupdatedelete-snippet-rules">create a snippet rule</a>. The expression of the snippet rule defines when the snippet code will run.</p>
<h3 id="create-update-delete-snippet-rules">Create/update/delete snippet rules</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12789.md")
</aside>
<p>Once you have created a code snippet, you can link it to rules. This is done via the following <code>PUT</code> request to the <code>snippet_rules</code> endpoint.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/snippets/snippet_rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;description&quot;: &quot;Trigger snippet on specific cookie&quot;,&#10;      &quot;enabled&quot;: true,&#10;      &quot;expression&quot;: &quot;http.cookie eq \&quot;a=b\&quot;&quot;,&#10;      &quot;snippet_name&quot;: &quot;snippet_name_01&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
