---
cp9:
  canonical: https://developers.cloudflare.com/d1/observability/audit-logs/
  description: Review audit log entries for configuration changes made to your D1 databases.
  full_title: Audit Logs · Cloudflare D1 docs
  head_html: <title>Audit Logs · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Review audit log entries for configuration changes made to your D1 databases."><link rel="canonical" href="https://developers.cloudflare.com/d1/observability/audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/observability/audit-logs/index.md"><meta property="og:title" content="Audit Logs · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review audit log entries for configuration changes made to your D1 databases."><meta property="og:url" content="https://developers.cloudflare.com/d1/observability/audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/observability/audit-logs/#page","headline":"Audit Logs \u00b7 Cloudflare D1 docs","description":"Review audit log entries for configuration changes made to your D1 databases.","url":"https://developers.cloudflare.com/d1/observability/audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/observability/audit-logs/
  schema: 1
---
<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account, including those made to D1 databases. This functionality is available on all plan types, free of charge, and is always enabled.</p>
<h2 id="viewing-audit-logs">Viewing audit logs</h2>
<p>To view audit logs for your D1 databases, go to the <strong>Audit Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">Review audit logs</a>.</p>
<h2 id="logged-operations">Logged operations</h2>
<p>The following configuration actions are logged:</p>
<table>
<tbody>
<th colspan="5" rowspan="1" style="width:220px">
			Operation
</th>
<th colspan="5" rowspan="1">
			Description
</th>
<tr>
<td colspan="5" rowspan="1">
				CreateDatabase
</td>
<td colspan="5" rowspan="1">
				Creation of a new database.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				DeleteDatabase
</td>
<td colspan="5" rowspan="1">
				Deletion of an existing database.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				<a href="/d1/reference/time-travel">TimeTravel</a>
</td>
<td colspan="5" rowspan="1">
				Restoration of a past database version.
</td>
</tr>
</tbody>
</table>
<h2 id="example-log-entry">Example log entry</h2>
<p>Below is an example of an audit log entry showing the creation of a new database:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;action&quot;: { &quot;info&quot;: &quot;CreateDatabase&quot;, &quot;result&quot;: true, &quot;type&quot;: &quot;create&quot; },&#10;	&quot;actor&quot;: {&#10;		&quot;email&quot;: &quot;&lt;ACTOR_EMAIL&gt;&quot;,&#10;		&quot;id&quot;: &quot;b1ab1021a61b1b12612a51b128baa172&quot;,&#10;		&quot;ip&quot;: &quot;1b11:a1b2:12b1:12a::11a:1b&quot;,&#10;		&quot;type&quot;: &quot;user&quot;&#10;	},&#10;	&quot;id&quot;: &quot;a123b12a-ab11-1212-ab1a-a1aa11a11abb&quot;,&#10;	&quot;interface&quot;: &quot;API&quot;,&#10;	&quot;metadata&quot;: {},&#10;	&quot;newValue&quot;: &quot;&quot;,&#10;	&quot;newValueJson&quot;: { &quot;database_name&quot;: &quot;my-db&quot; },&#10;	&quot;oldValue&quot;: &quot;&quot;,&#10;	&quot;oldValueJson&quot;: {},&#10;	&quot;owner&quot;: { &quot;id&quot;: &quot;211b1a74121aa32a19121a88a712aa12&quot; },&#10;	&quot;resource&quot;: {&#10;		&quot;id&quot;: &quot;11a21122-1a11-12bb-11ab-1aa2aa1ab12a&quot;,&#10;		&quot;type&quot;: &quot;d1.database&quot;&#10;	},&#10;	&quot;when&quot;: &quot;2024-08-09T04:53:55.752Z&quot;&#10;}&#10;</code></pre>
