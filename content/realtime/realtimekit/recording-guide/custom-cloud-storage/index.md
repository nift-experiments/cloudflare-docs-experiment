---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/
  description: Explore how to set up custom cloud storage for RealtimeKit's recording. Follow our guide for effective configuration and integration.
  full_title: Upload Recording to Your Cloud · Cloudflare Realtime docs
  head_html: <title>Upload Recording to Your Cloud · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore how to set up custom cloud storage for RealtimeKit&#x27;s recording. Follow our guide for effective configuration and integration."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/index.md"><meta property="og:title" content="Upload Recording to Your Cloud · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore how to set up custom cloud storage for RealtimeKit&#x27;s recording. Follow our guide for effective configuration and integration."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/#page","headline":"Upload Recording to Your Cloud \u00b7 Cloudflare Realtime docs","description":"Explore how to set up custom cloud storage for RealtimeKit's recording. Follow our guide for effective configuration and integration.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/custom-cloud-storage/
  schema: 1
---
<p>You can pass an optional object <code>storage_config</code> in the start recording request
to publish the recording directly to your cloud provider. If a <code>path</code> is
specified, the recorded video will be stored there, otherwise the default is the
root of the directory.</p>
<p>The filename for recording will be the same as given in <code>output_file_name</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11813.md")
</aside>
<h2 id="set-storage-configuration">Set storage configuration</h2>
<p>You can configure storage configs for RealtimeKit Recordings in the following ways:</p>
<h3 id="set-storage-configuration-details-using-realtimekit-dashboard">Set Storage Configuration Details Using RealtimeKit Dashboard</h3>
<p>You can specify storage configuration details using RealtimeKit Dashboard for all meetings.</p>
<ol>
<li>In the Cloudflare <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">RealtimeKit Dashboard</a>, go to Recordings tab.</li>
<li>Click <strong>Setup Storage</strong>.</li>
<li>Specify the details for your cloud provider. We support transferring
recordings to Cloudflare R2, AWS S3, Azure, DigitalOcean, and Google Cloud Storage (GCS) buckets.</li>
</ol>
<p><img src="/assets/upstream/images/realtime/realtimekit/setup-recording-storage.png" alt="Recording Storage Screenshot" /></p>
<br />
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11812.md")
</aside>
<p>To familiarize yourself with the RealtimeKit REST APIs, we recommend exploring the <a href="/api/resources/realtime_kit/">RealtimeKit REST API</a>.</p>
<h3 id="using-the-storage-config-option-in-the-start-recording-api">Using the <code>storage_config</code> option in the Start Recording API</h3>
<p>This allows for the most granular level of control, and lets you specify a storage_config for a specific
<a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">recording started</a> on a meeting.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_authorization_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;  &quot;storage_config&quot;: {&#10;    &quot;type&quot;: &quot;cloudflare&quot;,&#10;    &quot;access_key&quot;: &quot;your-access-key&quot;,&#10;    &quot;secret&quot;: &quot;your-secret-key&quot;,&#10;    &quot;bucket&quot;: &quot;your-bucket-name&quot;,&#10;    &quot;path&quot;: &quot;/&quot;,&#10;    &quot;account_id&quot;: &quot;your-account-id&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<p>To familiarize yourself with the RealtimeKit REST APIs, we recommend exploring the <a href="/api/resources/realtime_kit/">RealtimeKit REST API</a>.</p>
<h2 id="supported-cloud-providers">Supported Cloud Providers</h2>
<p>Currently, the following cloud providers are supported:</p>
<h3 id="cloudflare-r2">Cloudflare R2</h3>
<p>To transfer recordings to Cloudflare R2, set the following fields in
the <code>storage_config</code> parameter:</p>
<ul>
<li>Type: Specify <code>cloudflare</code>.</li>
<li>Access Key: Enter your R2 access key ID. For more information, see <a href="/r2/api/tokens/">Create API tokens</a>.</li>
<li>Bucket: Enter the name of your R2 bucket.</li>
<li>(Optional) Path: Specify the path to a sub-folder where recordings should be
transferred. If this parameter is not passed, recordings will be transferred
to the root folder of the bucket.</li>
<li>Secret: Enter your R2 secret access key.</li>
<li>Account ID: Enter your Cloudflare account ID.</li>
</ul>
<h3 id="aws-s3">AWS S3</h3>
<p>To transfer recordings to the AWS S3 bucket, set the following fields in the
<code>storage_config</code> parameter:</p>
<ul>
<li>Type: Specify <code>aws</code>.</li>
<li>Access Key: Enter your <code>aws_access_key_id</code>.</li>
<li>Bucket: Enter your AWS S3 bucket name.</li>
<li>(Optional) Path: Specify the path to a sub-folder where recordings should be
transferred. If this parameter is not passed, recordings will be transferred
to the root folder of the bucket.</li>
<li>Secret: Enter your <code>aws_secret_access_key</code>.</li>
<li>Region: Specify the region where your bucket is hosted, for example,
<code>ap-south-1</code>.</li>
</ul>
<h3 id="azure-blob-storage">Azure Blob Storage</h3>
<p>To transfer recordings to the Azure Blob Storage, set the following fields in
the <code>storage_config</code> parameter:</p>
<ul>
<li>Type: Specify <code>azure</code>.</li>
<li>Access key: Enter your azure connection string. For more information on how to
get the access key, see
<a href="https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&amp;bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&amp;tabs=azure-portal#view-account-access-keys">View account access key</a>.</li>
<li>Bucket: Enter the name of your container. The container should be in the same
storage account as the connection string.</li>
<li>(Optional) Path: Specify the path to a sub-folder where recordings should be
transferred. If this parameter is not passed, recordings will be transferred
to the root folder of the container.</li>
<li>Secret: Set to a blank string &quot;&quot;.</li>
<li>Region: Set to a blank string &quot;&quot;.</li>
</ul>
<h3 id="digitalocean">DigitalOcean</h3>
<p>To transfer recordings to the DigitalOcean Spaces, set the following fields in
the <code>storage_config</code> parameter:</p>
<ul>
<li>Type: Specify <code>digitalocean</code>.</li>
<li>Access key: Enter your digital ocean access key. For more information, see
<a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key">Create DigitalOcean Space and API Key</a>.</li>
<li>Bucket: Enter the name of your Spaces bucket.</li>
<li>(Optional) Path: Specify the path to a sub-folder where recordings should be
transferred. If this parameter is not passed, recordings will be transferred
to the root folder of the container.</li>
<li>Secret: Enter your Spaces secret.</li>
<li>Region: Specify the region where your Spaces bucket is hosted, for example,
<code>SGP1</code>. For more information, see
<a href="https://docs.digitalocean.com/products/platform/availability-matrix/">Region Availability Matrix</a>.</li>
</ul>
<h3 id="google-cloud-storage-gcs">Google Cloud Storage (GCS)</h3>
<p>To transfer recordings to GCS, set the following fields in
the <code>storage_config</code> parameter:</p>
<ul>
<li>Type: Specify <code>gcs</code>.</li>
<li>Bucket: Enter the name of your Cloud Storage bucket.</li>
<li>(Optional) Path: Specify the path to a sub-folder where recordings should be
transferred. If this parameter is not passed, recordings will be transferred
to the root folder of the container.</li>
<li>Secret: Enter your service account credentials. For more information, see <a href="https://developers.google.com/workspace/guides/create-credentials#service-account">service account credentials</a>.</li>
<li>Region: Specify the region where your Cloud Storage bucket is hosted, for example,
<code>US multi-region</code>. For more information, see
<a href="https://cloud.google.com/storage/docs/locations">Bucket locations</a>.</li>
</ul>
<h2 id="update-the-recording-file-name">Update the Recording File Name</h2>
<p>You can change the name of the recording file using the <code>file_name_prefix</code> field. The default format for recorded file name is <code>roomname_timestamp</code>, but you can add an alphanumeric and underscore prefix to the default file name.</p>
<p>It's important to note that you can only add a prefix to the default format; you can't change the entire file name. For example, if you teach an online physics class at 9 a.m. using RealtimeKit, you could add <code>Physics_9am</code> to the file name. <code>Physics_9am_roomname_timestamp</code> would be the new file name.</p>
<p>For more information, see <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">start recording a meeting</a>.</p>
