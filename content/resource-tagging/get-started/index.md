---
cp9:
  canonical: https://developers.cloudflare.com/resource-tagging/get-started/
  description: Set up authentication for Resource Tagging and make your first API calls.
  full_title: Get started · Cloudflare Resource Tagging docs
  head_html: <title>Get started · Cloudflare Resource Tagging docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up authentication for Resource Tagging and make your first API calls."><link rel="canonical" href="https://developers.cloudflare.com/resource-tagging/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/resource-tagging/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Resource Tagging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up authentication for Resource Tagging and make your first API calls."><meta property="og:url" content="https://developers.cloudflare.com/resource-tagging/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Resource Tagging"><meta name="algolia_product_filter" content="Resource Tagging"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/resource-tagging/get-started/#page","headline":"Get started \u00b7 Cloudflare Resource Tagging docs","description":"Set up authentication for Resource Tagging and make your first API calls.","url":"https://developers.cloudflare.com/resource-tagging/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /resource-tagging/get-started/
  schema: 1
---
<p>This guide walks you through verifying that tagging works on your account and making your first API calls.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>At least one user with the Super Administrator, Workers Admin, or Tag Admin role. These roles can create, update, and delete tags.</li>
<li>The API is the preferred interface for managing tags. You can also use the dashboard under <strong>Manage Account</strong> &gt; <strong>Resource Tagging</strong>, but you should be comfortable making authenticated HTTP requests for automation workflows.</li>
<li>An API token with the required permissions. <a href="/fundamentals/api/get-started/account-owned-tokens/">Account Owned Tokens</a> are recommended for automation.</li>
</ul>
<h2 id="1-verify-tagging-is-enabled"><ol>
<li>Verify tagging is enabled</li>
</ol></h2>
<p>Test the API to confirm tagging is active on your account:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/keys&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot;&#10;</code></pre>
<h3 id="interpreting-the-response">Interpreting the response</h3>
<table>
<thead>
<tr>
<th>Response</th>
<th>Meaning</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>200 OK</strong> with <code>{&quot;success&quot;: true, &quot;result&quot;: [...]}</code></td>
<td>Tagging is enabled. An empty array is normal if no tags exist yet.</td>
<td>Proceed to the next step.</td>
</tr>
<tr>
<td><strong>403</strong> mentioning &quot;permission&quot; or &quot;role&quot;</td>
<td>The caller lacks required permissions.</td>
<td>Verify the caller has a Super Admin, Workers Admin, or Tag Admin role, or that the token has <code>#com.cloudflare.api.account.tag.list</code> scope.</td>
</tr>
<tr>
<td><strong>403</strong> mentioning &quot;feature&quot; or &quot;gate&quot;</td>
<td>Tagging is not enabled for this account.</td>
<td>Contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a> for assistance.</td>
</tr>
<tr>
<td><strong>401 Unauthorized</strong></td>
<td>Authentication failed.</td>
<td>Verify the token is valid, not expired, and formatted correctly in the <code>Authorization: Bearer</code> header.</td>
</tr>
<tr>
<td>Any other response</td>
<td>Unexpected error.</td>
<td>Capture the full response body and contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a> with the Account ID, request details, and timestamp.</td>
</tr>
</tbody>
</table>
<h2 id="2-create-your-first-tags"><ol start="2">
<li>Create your first tags</li>
</ol></h2>
<p>Set tags on a resource using <code>PUT</code>:</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$RESOURCE_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;environment&quot;: &quot;production&quot;,&#10;      &quot;team&quot;: &quot;platform&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Then retrieve the tags:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&amp;resource_id=$RESOURCE_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot;&#10;</code></pre>
<h2 id="3-list-tagged-resources"><ol start="3">
<li>List tagged resources</li>
</ol></h2>
<p>Query all tagged resources in the account, optionally filtering by tag:</p>
<pre tabindex="0"><code class="language-bash">&#35; All tagged resources&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Filter: only resources with environment=production&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn the full <a href="/resource-tagging/how-to/filter-resources/">tag filtering syntax</a> for complex queries.</li>
<li>Understand the <a href="/resource-tagging/how-to/manage-tags/#add-a-single-tag">GET, merge, PUT workflow</a> for modifying individual tags.</li>
<li>Review <a href="/resource-tagging/reference/resource-types/">supported resource types</a> and their required fields.</li>
<li>Review <a href="/resource-tagging/reference/limits/">API limits and validation rules</a>.</li>
</ul>
