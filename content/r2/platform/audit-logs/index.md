---
cp9:
  canonical: https://developers.cloudflare.com/r2/platform/audit-logs/
  description: Review audit logs for configuration changes made to your R2 buckets.
  full_title: Audit Logs · Cloudflare R2 docs
  head_html: <title>Audit Logs · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Review audit logs for configuration changes made to your R2 buckets."><link rel="canonical" href="https://developers.cloudflare.com/r2/platform/audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/platform/audit-logs/index.md"><meta property="og:title" content="Audit Logs · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review audit logs for configuration changes made to your R2 buckets."><meta property="og:url" content="https://developers.cloudflare.com/r2/platform/audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/platform/audit-logs/#page","headline":"Audit Logs \u00b7 Cloudflare R2 docs","description":"Review audit logs for configuration changes made to your R2 buckets.","url":"https://developers.cloudflare.com/r2/platform/audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/platform/audit-logs/
  schema: 1
---
<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account, including those made to R2 buckets. This functionality is available on all plan types, free of charge, and is always enabled.</p>
<h2 id="viewing-audit-logs">Viewing audit logs</h2>
<p>To view audit logs for your R2 buckets, go to the <strong>Audit logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">Review audit logs</a>.</p>
<h2 id="logged-operations">Logged operations</h2>
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
<td>CreateBucket</td>
<td>Creation of a new bucket.</td>
</tr>
<tr>
<td>DeleteBucket</td>
<td>Deletion of an existing bucket.</td>
</tr>
<tr>
<td>AddCustomDomain</td>
<td>Addition of a custom domain to a bucket.</td>
</tr>
<tr>
<td>RemoveCustomDomain</td>
<td>Removal of a custom domain from a bucket.</td>
</tr>
<tr>
<td>ChangeBucketVisibility</td>
<td>Change to the managed public access (<code>r2.dev</code>) settings of a bucket.</td>
</tr>
<tr>
<td>PutBucketStorageClass</td>
<td>Change to the default storage class of a bucket.</td>
</tr>
<tr>
<td>PutBucketLifecycleConfiguration</td>
<td>Change to the object lifecycle configuration of a bucket.</td>
</tr>
<tr>
<td>DeleteBucketLifecycleConfiguration</td>
<td>Deletion of the object lifecycle configuration for a bucket.</td>
</tr>
<tr>
<td>PutBucketCors</td>
<td>Change to the CORS configuration for a bucket.</td>
</tr>
<tr>
<td>DeleteBucketCors</td>
<td>Deletion of the CORS configuration for a bucket.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11377.md")
</aside>
<h2 id="example-log-entry">Example log entry</h2>
<p>Below is an example of an audit log entry showing the creation of a new bucket:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;action&quot;: { &quot;info&quot;: &quot;CreateBucket&quot;, &quot;result&quot;: true, &quot;type&quot;: &quot;create&quot; },&#10;	&quot;actor&quot;: {&#10;		&quot;email&quot;: &quot;&lt;ACTOR_EMAIL&gt;&quot;,&#10;		&quot;id&quot;: &quot;3f7b730e625b975bc1231234cfbec091&quot;,&#10;		&quot;ip&quot;: &quot;fe32:43ed:12b5:526::1d2:13&quot;,&#10;		&quot;type&quot;: &quot;user&quot;&#10;	},&#10;	&quot;id&quot;: &quot;5eaeb6be-1234-406a-87ab-1971adc1234c&quot;,&#10;	&quot;interface&quot;: &quot;API&quot;,&#10;	&quot;metadata&quot;: { &quot;zone_name&quot;: &quot;r2.cloudflarestorage.com&quot; },&#10;	&quot;newValue&quot;: &quot;&quot;,&#10;	&quot;newValueJson&quot;: {},&#10;	&quot;oldValue&quot;: &quot;&quot;,&#10;	&quot;oldValueJson&quot;: {},&#10;	&quot;owner&quot;: { &quot;id&quot;: &quot;1234d848c0b9e484dfc37ec392b5fa8a&quot; },&#10;	&quot;resource&quot;: { &quot;id&quot;: &quot;my-bucket&quot;, &quot;type&quot;: &quot;r2.bucket&quot; },&#10;	&quot;when&quot;: &quot;2024-07-15T16:32:52.412Z&quot;&#10;}&#10;</code></pre>
