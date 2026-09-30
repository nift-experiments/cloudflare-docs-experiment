---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/
  description: Push Cloudflare logs to Microsoft Azure Blob Storage.
  full_title: Enable Logpush to Microsoft Azure · Cloudflare Logs docs
  head_html: <title>Enable Logpush to Microsoft Azure · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Microsoft Azure Blob Storage."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/index.md"><meta property="og:title" content="Enable Logpush to Microsoft Azure · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Microsoft Azure Blob Storage."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/#page","headline":"Enable Logpush to Microsoft Azure \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Microsoft Azure Blob Storage.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/azure/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/azure/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs directly to Microsoft Azure via the Cloudflare dashboard or via API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10574.md")
</aside>
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
<p>In <strong>Select a destination</strong>, choose <strong>Microsoft Azure</strong>.</p>
</li>
<li>
<p>Enter or select the following destination details:</p>
<ul>
<li><strong>SAS URL</strong> - a pre-signed URL that grants access to Azure Storage resources. Refer to <a href="https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer?tabs=macos#shared-access-signature-sas-url">Azure storage documentation</a> for more information on generating a SAS URL using Azure Storage Explorer. The service must be set to Blob-only (<code>ss=b</code>), and the resource type must be set to Object-only (<code>srt=o</code>).</li>
<li><strong>Path</strong> - bucket location within the storage container</li>
<li><strong>Organize logs into daily subfolders</strong> (recommended)</li>
</ul>
</li>
</ol>
<p>When you are done entering the destination details, select <strong>Continue</strong>.</p>
<ol start="6">
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
<h2 id="create-and-get-access-to-a-blob-storage-container">Create and get access to a Blob Storage container</h2>
<p>Cloudflare uses a shared access signature (SAS) token to gain access to your Blob Storage container. You will need to provide <code>Write</code> permission and an expiration period of at least five years, which will allow you to not worry about the SAS token expiring.</p>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.
<br /></p>
<p>To enable Logpush to Azure:</p>
<ol>
<li>
<p>Create a Blob Storage container. Refer to <a href="https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal">instructions from Azure</a>.</p>
</li>
<li>
<p>Create a <a href="https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature (SAS)</a> to secure and restrict access to your blob storage container. Use <a href="https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer">Storage Explorer</a> to navigate to your container and right click to create a signature. Set the signature to expire at least five years from now and only provide write permission.</p>
</li>
<li>
<p>Provide the SAS URL when prompted by the Logpush API or UI.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/10573.md")
</aside>
<h2 id="troubleshooting-azure-destinations">Troubleshooting Azure destinations</h2>
<h3 id="signedresourcetypes-error">signedResourceTypes error</h3>
<p>When configuring an Azure destination, the SAS (Shared Access Signature) token must be set to a blob container with write-only permissions. The service must be Blob-only (<code>ss=b</code>), and the resource type must be Object-only (<code>srt=o</code>).</p>
<p>If the SAS token uses different settings, you will receive the following error:</p>
<pre tabindex="0"><code>signedResourceTypes must be Object only (srt=o)&#10;</code></pre>
<p>To resolve this error, regenerate your SAS token using <a href="https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer">Storage Explorer</a> with the correct permissions:</p>
<ul>
<li>Service: Blob-only (<code>ss=b</code>)</li>
<li>Resource type: Object-only (<code>srt=o</code>)</li>
<li>Permissions: Write-only</li>
<li>Expiration: At least five years from now</li>
</ul>
