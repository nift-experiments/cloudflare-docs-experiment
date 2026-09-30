---
cp9:
  canonical: https://developers.cloudflare.com/queues/platform/audit-logs/
  description: Review audit log events for configuration changes made to Cloudflare Queues.
  full_title: Audit Logs · Cloudflare Queues docs
  head_html: <title>Audit Logs · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Review audit log events for configuration changes made to Cloudflare Queues."><link rel="canonical" href="https://developers.cloudflare.com/queues/platform/audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/platform/audit-logs/index.md"><meta property="og:title" content="Audit Logs · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review audit log events for configuration changes made to Cloudflare Queues."><meta property="og:url" content="https://developers.cloudflare.com/queues/platform/audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/platform/audit-logs/#page","headline":"Audit Logs \u00b7 Cloudflare Queues docs","description":"Review audit log events for configuration changes made to Cloudflare Queues.","url":"https://developers.cloudflare.com/queues/platform/audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/platform/audit-logs/
  schema: 1
---
<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account, including those made to Queues. This functionality is always enabled.</p>
<h2 id="viewing-audit-logs">Viewing audit logs</h2>
<p>To view audit logs for your Queue in the Cloudflare dashboard, go to the <strong>Audit logs</strong> page.</p>
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
        CreateQueue
</td>
<td colspan="5" rowspan="1">
        Creation of a new queue.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        DeleteQueue
</td>
<td colspan="5" rowspan="1">
        Deletion of an existing queue.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        UpdateQueue
</td>
<td colspan="5" rowspan="1">
        Updating the configuration of a queue.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        AttachConsumer
</td>
<td colspan="5" rowspan="1">
        Attaching a consumer, including HTTP pull consumers, to the Queue.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        RemoveConsumer
</td>
<td colspan="5" rowspan="1">
        Removing a consumer, including HTTP pull consumers, from the Queue.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        UpdateConsumerSettings
</td>
<td colspan="5" rowspan="1">
        Changing Queues consumer settings.
</td>
</tr>
</tbody>
</table>
