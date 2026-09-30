---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/advanced/logpush/
  description: Send Zaraz event logs to Logpush destinations.
  full_title: Send Zaraz logs to Logpush · Cloudflare Zaraz docs
  head_html: <title>Send Zaraz logs to Logpush · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Send Zaraz event logs to Logpush destinations."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/advanced/logpush/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/advanced/logpush/index.md"><meta property="og:title" content="Send Zaraz logs to Logpush · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send Zaraz event logs to Logpush destinations."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/advanced/logpush/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/advanced/logpush/#page","headline":"Send Zaraz logs to Logpush \u00b7 Cloudflare Zaraz docs","description":"Send Zaraz event logs to Logpush destinations.","url":"https://developers.cloudflare.com/zaraz/advanced/logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/advanced/logpush/
  schema: 1
---
<p>Send Zaraz logs to an external storage provider like R2 or S3.</p>
<p>This is an Enterprise only feature.</p>
<h2 id="setup">Setup</h2>
<p>Follow these steps to configure Logpush support for Zaraz:</p>
<h3 id="1-create-a-logpush-job"><ol>
<li>Create a Logpush job</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create a Logpush Job</strong> and follow the steps described in the <a href="/logs/logpush/">Logpush</a> documentation.<br/>
When selecting a dataset, make sure you select <strong>Zaraz Events</strong>.</li>
</ol>
<h3 id="2-enable-logpush-from-zaraz-settings"><ol start="2">
<li>Enable Logpush from Zaraz settings</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to <strong>Delivery &amp; Performance</strong> &gt; <strong>Web tag management</strong> &gt; <strong>Tag setup</strong> &gt; select your domain &gt; <strong>Settings</strong>.</p>
<p>Alternatively, navigate directly to <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz/:zone/tools-config/tools">Zaraz settings</a></p>
</li>
<li>
<p>Enable <strong>Export Zaraz Logs</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17606.md")
</aside>
<h2 id="fields">Fields</h2>
<p>Logs will have the following fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>RequestHeaders</td>
<td><code>JSON</code></td>
<td>The headers that were sent with the request.</td>
</tr>
<tr>
<td>URL</td>
<td><code>String</code></td>
<td>The Zaraz URL to which the request was made.</td>
</tr>
<tr>
<td>IP</td>
<td><code>String</code></td>
<td>The originating IP.</td>
</tr>
<tr>
<td>Body</td>
<td><code>JSON</code></td>
<td>The body that was sent along with the request.</td>
</tr>
<tr>
<td>Event Type</td>
<td><code>String</code></td>
<td>Can be one of the following: <code>server_request</code>, <code>server_response</code>, <code>action_triggered</code>, <code>ecommerce_triggered</code>, <code>client_request</code>, <code>component_error</code>.</td>
</tr>
<tr>
<td>Event Details</td>
<td><code>JSON</code></td>
<td>Details about the event.</td>
</tr>
<tr>
<td>TimestampStart</td>
<td><code>String</code></td>
<td>The time at which the event occurred.</td>
</tr>
</tbody>
</table>
