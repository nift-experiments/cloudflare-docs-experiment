---
cp9:
  canonical: https://developers.cloudflare.com/resource-tagging/reference/resource-types/
  description: Resource types that support tagging and their required fields.
  full_title: Supported resource types · Cloudflare Resource Tagging docs
  head_html: <title>Supported resource types · Cloudflare Resource Tagging docs</title><meta name="generator" content="Nift"><meta name="description" content="Resource types that support tagging and their required fields."><link rel="canonical" href="https://developers.cloudflare.com/resource-tagging/reference/resource-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/resource-tagging/reference/resource-types/index.md"><meta property="og:title" content="Supported resource types · Cloudflare Resource Tagging docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resource types that support tagging and their required fields."><meta property="og:url" content="https://developers.cloudflare.com/resource-tagging/reference/resource-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Resource Tagging"><meta name="algolia_product_filter" content="Resource Tagging"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/resource-tagging/reference/resource-types/#page","headline":"Supported resource types \u00b7 Cloudflare Resource Tagging docs","description":"Resource types that support tagging and their required fields.","url":"https://developers.cloudflare.com/resource-tagging/reference/resource-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /resource-tagging/reference/resource-types/
  schema: 1
---
<p>The Tagging API supports the following resource types across account-level and zone-level scopes.</p>
<h2 id="account-level-resources">Account-level resources</h2>
<p>Use <code>/accounts/{account_id}/tags</code> endpoints for these resource types.</p>
<table>
<thead>
<tr>
<th>Resource type</th>
<th>Required extra fields</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>account</code></td>
<td>None</td>
<td>The Cloudflare account itself</td>
</tr>
<tr>
<td><code>access_application</code></td>
<td>None</td>
<td>Access application</td>
</tr>
<tr>
<td><code>access_group</code></td>
<td>None</td>
<td>Access group</td>
</tr>
<tr>
<td><code>account_ruleset</code></td>
<td>None</td>
<td>Account-level ruleset</td>
</tr>
<tr>
<td><code>ai_gateway</code></td>
<td>None</td>
<td>AI Gateway</td>
</tr>
<tr>
<td><code>alerting_policy</code></td>
<td>None</td>
<td>Notification policy</td>
</tr>
<tr>
<td><code>alerting_webhook</code></td>
<td>None</td>
<td>Notification webhook destination</td>
</tr>
<tr>
<td><code>cloudflared_tunnel</code></td>
<td>None</td>
<td>Cloudflare Tunnel</td>
</tr>
<tr>
<td><code>d1_database</code></td>
<td>None</td>
<td>D1 database</td>
</tr>
<tr>
<td><code>durable_object_namespace</code></td>
<td>None</td>
<td>Durable Objects namespace</td>
</tr>
<tr>
<td><code>gateway_list</code></td>
<td>None</td>
<td>Gateway list</td>
</tr>
<tr>
<td><code>gateway_rule</code></td>
<td>None</td>
<td>Gateway rule</td>
</tr>
<tr>
<td><code>image</code></td>
<td>None</td>
<td>Cloudflare Image</td>
</tr>
<tr>
<td><code>infrastructure_target</code></td>
<td>None</td>
<td><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> target</td>
</tr>
<tr>
<td><code>kv_namespace</code></td>
<td>None</td>
<td>Workers KV namespace</td>
</tr>
<tr>
<td><code>load_balancer_monitor</code></td>
<td>None</td>
<td>Load Balancer monitor</td>
</tr>
<tr>
<td><code>load_balancer_pool</code></td>
<td>None</td>
<td>Load Balancer pool</td>
</tr>
<tr>
<td><code>pages_project</code></td>
<td>None</td>
<td>Pages project</td>
</tr>
<tr>
<td><code>queue</code></td>
<td>None</td>
<td>Queue</td>
</tr>
<tr>
<td><code>r2_bucket</code></td>
<td>None</td>
<td>R2 bucket</td>
</tr>
<tr>
<td><code>resource_share</code></td>
<td>None</td>
<td>Resource share</td>
</tr>
<tr>
<td><code>stream_live_input</code></td>
<td>None</td>
<td>Stream live input</td>
</tr>
<tr>
<td><code>stream_video</code></td>
<td>None</td>
<td>Stream video</td>
</tr>
<tr>
<td><code>vectorize_index</code></td>
<td>None</td>
<td>Vectorize index</td>
</tr>
<tr>
<td><code>worker</code></td>
<td>None</td>
<td>Workers script</td>
</tr>
<tr>
<td><code>worker_version</code></td>
<td><code>worker_id</code></td>
<td>Specific version of a Worker</td>
</tr>
</tbody>
</table>
<h2 id="zone-level-resources">Zone-level resources</h2>
<p>Use <code>/zones/{zone_id}/tags</code> endpoints for these resource types.</p>
<table>
<thead>
<tr>
<th>Resource type</th>
<th>Required extra fields</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>access_application_policy</code></td>
<td><code>access_application_id</code></td>
<td>Access application policy</td>
</tr>
<tr>
<td><code>api_gateway_operation</code></td>
<td>None</td>
<td>API Gateway operation</td>
</tr>
<tr>
<td><code>custom_certificate</code></td>
<td>None</td>
<td>Custom SSL certificate</td>
</tr>
<tr>
<td><code>custom_hostname</code></td>
<td>None</td>
<td>Custom hostname (SSL for SaaS)</td>
</tr>
<tr>
<td><code>dns_record</code></td>
<td>None</td>
<td>DNS record</td>
</tr>
<tr>
<td><code>healthcheck</code></td>
<td>None</td>
<td>Health check</td>
</tr>
<tr>
<td><code>load_balancer</code></td>
<td>None</td>
<td>Load Balancer</td>
</tr>
<tr>
<td><code>managed_client_certificate</code></td>
<td>None</td>
<td>Managed client certificate (mTLS)</td>
</tr>
<tr>
<td><code>worker_route</code></td>
<td>None</td>
<td>Worker route</td>
</tr>
<tr>
<td><code>zone</code></td>
<td>None</td>
<td>DNS zone</td>
</tr>
<tr>
<td><code>zone_ruleset</code></td>
<td>None</td>
<td>Zone-level ruleset</td>
</tr>
</tbody>
</table>
<h2 id="extra-fields">Extra fields</h2>
<p>Most resource types only require <code>resource_type</code> and <code>resource_id</code>. Two resource types require an additional field in both request bodies and query parameters.</p>
<h3 id="worker-version"><code>worker_version</code></h3>
<p>Include the <code>worker_id</code> field:</p>
<pre tabindex="0"><code class="language-bash">&#35; GET&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker_version&amp;resource_id=$VERSION_ID&amp;worker_id=$WORKER_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; PUT&#10;curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker_version&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$VERSION_ID&quot;&#x27;&quot;,&#10;    &quot;worker_id&quot;: &quot;&#x27;&quot;$WORKER_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;version&quot;: &quot;1.2.3&quot;,&#10;      &quot;environment&quot;: &quot;staging&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="access-application-policy"><code>access_application_policy</code></h3>
<p>Include the <code>access_application_id</code> field:</p>
<pre tabindex="0"><code class="language-bash">&#35; GET&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/tags?resource_type=access_application_policy&amp;resource_id=$POLICY_ID&amp;access_application_id=$APP_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; PUT&#10;curl -X PUT &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;access_application_policy&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$POLICY_ID&quot;&#x27;&quot;,&#10;    &quot;access_application_id&quot;: &quot;&#x27;&quot;$APP_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;sensitivity&quot;: &quot;high&quot;,&#10;      &quot;team&quot;: &quot;security&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
