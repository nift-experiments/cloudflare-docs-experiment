---
cp9:
  canonical: https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/
  description: Create, update, and delete tags on Cloudflare resources.
  full_title: Manage tags · Cloudflare Resource Tagging docs
  head_html: <title>Manage tags · Cloudflare Resource Tagging docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, update, and delete tags on Cloudflare resources."><link rel="canonical" href="https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/index.md"><meta property="og:title" content="Manage tags · Cloudflare Resource Tagging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, update, and delete tags on Cloudflare resources."><meta property="og:url" content="https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Resource Tagging"><meta name="algolia_product_filter" content="Resource Tagging"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/#page","headline":"Manage tags \u00b7 Cloudflare Resource Tagging docs","description":"Create, update, and delete tags on Cloudflare resources.","url":"https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /resource-tagging/how-to/manage-tags/
  schema: 1
---
<p>All tag operations use the Tagging API. Authentication requires an <a href="/fundamentals/api/get-started/account-owned-tokens/">account API token</a> or user API token with appropriate permissions.</p>
<h2 id="set-tags-on-a-resource">Set tags on a resource</h2>
<p>Use <code>PUT</code> to set tags on an account-level resource. This operation replaces all existing tags on the resource.</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$RESOURCE_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;environment&quot;: &quot;production&quot;,&#10;      &quot;team&quot;: &quot;platform&quot;,&#10;      &quot;cost-center&quot;: &quot;engineering&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>For zone-level resources, use the zone endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;zone&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$ZONE_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;environment&quot;: &quot;production&quot;,&#10;      &quot;customer&quot;: &quot;acme-corp&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Some resource types require additional fields. Refer to <a href="/resource-tagging/reference/resource-types/">supported resource types</a> for details.</p>
<h2 id="get-tags-for-a-resource">Get tags for a resource</h2>
<p>Retrieve tags for a specific resource:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&amp;resource_id=$RESOURCE_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12768.md")
</aside>
<h2 id="add-a-single-tag">Add a single tag</h2>
<p>The API does not support partial updates — <code>PUT</code> always replaces all tags. To add a tag without removing existing ones, use the <code>GET</code>, merge, <code>PUT</code> pattern:</p>
<ol>
<li><code>GET</code> the current tags.</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&amp;resource_id=$RESOURCE_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Response: {&quot;result&quot;: {&quot;tags&quot;: {&quot;environment&quot;: &quot;production&quot;, &quot;team&quot;: &quot;platform&quot;}}}&#10;</code></pre>
<ol start="2">
<li>Merge the new tag into the existing set locally.</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;environment&quot;: &quot;production&quot;,&#10;  &quot;team&quot;: &quot;platform&quot;,&#10;  &quot;cost-center&quot;: &quot;engineering&quot;&#10;}&#10;</code></pre>
<ol start="3">
<li><code>PUT</code> the complete merged tag set.</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$RESOURCE_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;environment&quot;: &quot;production&quot;,&#10;      &quot;team&quot;: &quot;platform&quot;,&#10;      &quot;cost-center&quot;: &quot;engineering&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12767.md")
</aside>
<h2 id="remove-a-single-tag">Remove a single tag</h2>
<p>Follow the same <code>GET</code>, merge, <code>PUT</code> pattern, but omit the tag you want to remove from the set before calling <code>PUT</code>.</p>
<h2 id="delete-all-tags">Delete all tags</h2>
<p>To remove all tags from a resource:</p>
<pre tabindex="0"><code class="language-bash">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$RESOURCE_ID&quot;&#x27;&quot;&#10;  }&#x27;&#10;</code></pre>
<p>This returns <code>204 No Content</code> on success. Only use <code>DELETE</code> when you want to remove all tags from a resource (for example, when decommissioning it).</p>
