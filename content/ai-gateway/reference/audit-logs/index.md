---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/reference/audit-logs/
  description: View audit log entries for AI Gateway configuration changes such as gateway creation, deletion, and updates.
  full_title: Audit logs · Cloudflare AI Gateway docs
  head_html: <title>Audit logs · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="View audit log entries for AI Gateway configuration changes such as gateway creation, deletion, and updates."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/reference/audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/reference/audit-logs/index.md"><meta property="og:title" content="Audit logs · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View audit log entries for AI Gateway configuration changes such as gateway creation, deletion, and updates."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/reference/audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/reference/audit-logs/#page","headline":"Audit logs \u00b7 Cloudflare AI Gateway docs","description":"View audit log entries for AI Gateway configuration changes such as gateway creation, deletion, and updates.","url":"https://developers.cloudflare.com/ai-gateway/reference/audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/reference/audit-logs/
  schema: 1
---
<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account, including those made to gateways in AI Gateway. This functionality is available on all plan types, free of charge, and is enabled by default.</p>
<h2 id="viewing-audit-logs">Viewing Audit Logs</h2>
<p>To view audit logs for AI Gateway, in the Cloudflare dashboard, go to the <strong>Audit logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">review audit logs documentation</a>.</p>
<h2 id="logged-operations">Logged Operations</h2>
<p>The following configuration actions are logged:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>gateway created</td>
<td>Creation of a new gateway.</td>
</tr>
<tr>
<td>gateway deleted</td>
<td>Deletion of an existing gateway.</td>
</tr>
<tr>
<td>gateway updated</td>
<td>Edit of an existing gateway.</td>
</tr>
</tbody>
</table>
<h2 id="example-log-entry">Example Log Entry</h2>
<p>Below is an example of an audit log entry showing the creation of a new gateway:</p>
<pre tabindex="0"><code class="language-json">{&#10; &quot;action&quot;: {&#10;     &quot;info&quot;: &quot;gateway created&quot;,&#10;     &quot;result&quot;: true,&#10;     &quot;type&quot;: &quot;create&quot;&#10; },&#10; &quot;actor&quot;: {&#10;     &quot;email&quot;: &quot;&lt;ACTOR_EMAIL&gt;&quot;,&#10;     &quot;id&quot;: &quot;3f7b730e625b975bc1231234cfbec091&quot;,&#10;     &quot;ip&quot;: &quot;fe32:43ed:12b5:526::1d2:13&quot;,&#10;     &quot;type&quot;: &quot;user&quot;&#10; },&#10; &quot;id&quot;: &quot;5eaeb6be-1234-406a-87ab-1971adc1234c&quot;,&#10; &quot;interface&quot;: &quot;UI&quot;,&#10; &quot;metadata&quot;: {},&#10; &quot;newValue&quot;: &quot;&quot;,&#10; &quot;newValueJson&quot;: {&#10;     &quot;cache_invalidate_on_update&quot;: false,&#10;     &quot;cache_ttl&quot;: 0,&#10;     &quot;collect_logs&quot;: true,&#10;     &quot;id&quot;: &quot;test&quot;,&#10;     &quot;rate_limiting_interval&quot;: 0,&#10;     &quot;rate_limiting_limit&quot;: 0,&#10;     &quot;rate_limiting_technique&quot;: &quot;fixed&quot;&#10; },&#10; &quot;oldValue&quot;: &quot;&quot;,&#10; &quot;oldValueJson&quot;: {},&#10; &quot;owner&quot;: {&#10;     &quot;id&quot;: &quot;1234d848c0b9e484dfc37ec392b5fa8a&quot;&#10; },&#10; &quot;resource&quot;: {&#10;     &quot;id&quot;: &quot;89303df8-1234-4cfa-a0f8-0bd848e831ca&quot;,&#10;     &quot;type&quot;: &quot;ai_gateway.gateway&quot;&#10; },&#10; &quot;when&quot;: &quot;2024-07-17T14:06:11.425Z&quot;&#10;}&#10;</code></pre>
