---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/
  description: Organize, search, and filter user Workers by custom tags like customer ID or plan type in Workers for Platforms.
  full_title: Tags · Cloudflare for Platforms docs
  head_html: <title>Tags · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Organize, search, and filter user Workers by custom tags like customer ID or plan type in Workers for Platforms."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/index.md"><meta property="og:title" content="Tags · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Organize, search, and filter user Workers by custom tags like customer ID or plan type in Workers for Platforms."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare for Platforms"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/#page","headline":"Tags \u00b7 Cloudflare for Platforms docs","description":"Organize, search, and filter user Workers by custom tags like customer ID or plan type in Workers for Platforms.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/workers-for-platforms/configuration/tags/
  schema: 1
---
<p>Use tags to organize, search, and filter user Workers at scale. Tag Workers based on customer ID, plan type, project ID, or environment. After you tag user Workers, you can perform bulk operations like deleting all Workers for a specific customer.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4212.md")
</aside>
<h2 id="add-tags-via-dashboard">Add tags via dashboard</h2>
<ol>
<li>Go to <strong>Workers for Platforms</strong> in the Cloudflare dashboard and select your namespace.</li>
<li>Select a user Worker from the list.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Tags</strong>.</li>
<li>Add your tags (for example, <code>customer-123</code>, <code>pro-plan</code>, <code>production</code>).</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can also search and filter Workers by tags in the namespace view.</p>
<h2 id="tags-api-reference">Tags API reference</h2>
<p>For complete API documentation, refer to <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/">Workers for Platforms API</a>.</p>
<h3 id="get-script-tags">Get script tags</h3>
<p>Fetch all tags for a Worker script.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="set-script-tags">Set script tags</h3>
<p>Replace all tags on a Worker script. Existing tags not in the request are removed.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="add-a-single-tag">Add a single tag</h3>
<p>Add one tag to a Worker script without affecting existing tags.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="delete-a-single-tag">Delete a single tag</h3>
<p>Remove one tag from a Worker script.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="filter-workers-by-tag">Filter Workers by tag</h3>
<p>List all Workers that match a tag filter. Use <code>tag:yes</code> to include or <code>tag:no</code> to exclude.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="delete-workers-by-tag">Delete Workers by tag</h3>
<p>Delete all Workers matching a tag filter. Use this to bulk delete Workers when a customer leaves your platform.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
