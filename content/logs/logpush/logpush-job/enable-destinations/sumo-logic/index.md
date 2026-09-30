---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/
  description: Push Cloudflare logs to Sumo Logic.
  full_title: Enable Logpush to Sumo Logic · Cloudflare Logs docs
  head_html: <title>Enable Logpush to Sumo Logic · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Sumo Logic."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/index.md"><meta property="og:title" content="Enable Logpush to Sumo Logic · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Sumo Logic."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/#page","headline":"Enable Logpush to Sumo Logic \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Sumo Logic.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/sumo-logic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/sumo-logic/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs directly to Sumo Logic via the Cloudflare dashboard or via API.</p>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<ol>
<li>
<p>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page at the account or or domain (also known as zone) level.</p>
<p>For account: <div class="nb-dash-button"></div></p>
<p>For domain (also known as zone): <div class="nb-dash-button"></div></p>
</li>
<li>
<p>Depending on your choice, you have access to <a href="/logs/logpush/logpush-job/datasets/account/">account-scoped datasets</a> and <a href="/logs/logpush/logpush-job/datasets/zone/">zone-scoped datasets</a>, respectively.</p>
</li>
<li>
<p>Select <strong>Create a Logpush job</strong>.</p>
</li>
<li>
<p>In <strong>Select a destination</strong>, choose <strong>Sumo Logic</strong>.</p>
</li>
<li>
<p>Enter the <strong>HTTP Source Address</strong>. To get the HTTP Source Address (URL) configure a <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/">Sumo Logic Hosted Collector</a> with an <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/logs-metrics/">HTTP Logs &amp; Metrics Source</a>. Note that the same collector can be used for multiple Logpush jobs, but each job must have a dedicated source. When you are done entering the destination details, select <strong>Continue</strong>.</p>
</li>
<li>
<p>Select the dataset to push to the storage service.</p>
</li>
<li>
<p>In the next step, you need to configure your logpush job:</p>
<ul>
<li>Enter the <strong>Job name</strong>.</li>
<li>Under <strong>If logs match</strong>, you can select the events to include and/or remove from your logs. Refer to <a href="/logs/logpush/logpush-job/filters/">Filters</a> for more information. Not all datasets have this option available.</li>
<li>In <strong>Send the following fields</strong>, you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.</li>
</ul>
</li>
<li>
<p>In <strong>Advanced Options</strong>, you can:</p>
<ul>
<li>Choose the format of timestamp fields in your logs (<code>RFC3339</code> (default), <code>Unix</code>, or <code>UnixNano</code>).</li>
<li>Select a <a href="/logs/logpush/logpush-job/api-configuration/#sampling-rate">sampling rate</a> for your logs or push a randomly-sampled percentage of logs.</li>
<li>Enable redaction for <code>CVE-2021-44228</code>. This option will replace every occurrence of <code>${</code> with <code>x{</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Submit</strong> once you are done configuring your logpush job.</p>
</li>
</ol>
<h2 id="configure-a-hosted-collector">Configure a Hosted Collector</h2>
<p>Cloudflare can send logs to a Hosted Collector with <strong>HTTP Logs &amp; Metrics</strong> as the source. Once you have set up a collector, you simply provide the HTTP Source Address (a unique URL) to which logs can be posted.</p>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.
<br /></p>
<p>To enable Logpush to Sumo Logic:</p>
<ol>
<li>
<p>Configure a Hosted Collector. Refer to <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/configure-hosted-collector/">instructions from Sumo Logic</a>.</p>
</li>
<li>
<p>Configure an HTTP Logs &amp; Metrics Source. Refer to <a href="https://help.sumologic.com/docs/send-data/hosted-collectors/http-source/">instructions from Sumo Logic</a>. The last step indicates how to get the HTTP Source Address (URL).</p>
</li>
<li>
<p>Provide the HTTP Source Address (URL) when prompted by the Logpush API or UI.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/10538.md")
</aside>
