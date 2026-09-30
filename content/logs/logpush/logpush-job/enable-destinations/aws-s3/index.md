---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/
  description: Push Cloudflare logs to Amazon S3.
  full_title: Enable Logpush to Amazon S3 · Cloudflare Logs docs
  head_html: <title>Enable Logpush to Amazon S3 · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Amazon S3."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/index.md"><meta property="og:title" content="Enable Logpush to Amazon S3 · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Amazon S3."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/#page","headline":"Enable Logpush to Amazon S3 \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Amazon S3.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/aws-s3/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs directly to Amazon S3 via the Cloudflare dashboard or via API. Customers that use AWS GovCloud locations should use our <strong>S3-compatible endpoint</strong> and not the <strong>Amazon S3 endpoint</strong>.</p>
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
<p>In <strong>Select a destination</strong>, choose <strong>Amazon S3</strong>.</p>
</li>
<li>
<p>Enter or select the following destination information:</p>
<ul>
<li><strong>Bucket</strong> - S3 bucket name</li>
<li><strong>Path</strong> - bucket location within the storage container</li>
<li><strong>Organize logs into daily subfolders</strong> (recommended)</li>
<li><strong>Bucket region</strong></li>
<li>If your policy requires <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html">AWS SSE-S3 AES256 Server Side Encryption</a>.</li>
<li>For <strong>Grant Cloudflare access to upload files to your bucket</strong>, make sure your bucket has a <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html#iam-policy-ex0">policy</a> (if you did not add it already):
<ul>
<li>Copy the JSON policy, then go to your bucket in the Amazon S3 console and paste the policy in <strong>Permissions</strong> &gt; <strong>Bucket Policy</strong> and select <strong>Save</strong>.</li>
</ul>
</li>
</ul>
</li>
</ol>
<p>When you are done entering the destination details, select <strong>Continue</strong>.</p>
<ol start="6">
<li>
<p>To prove ownership, Cloudflare will send a file to your designated destination. To find the token, select the <strong>Open</strong> button in the <strong>Overview</strong> tab of the ownership challenge file, then paste it into the Cloudflare dashboard to verify your access to the bucket. Enter the <strong>Ownership Token</strong> and select <strong>Continue</strong>.</p>
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
<h2 id="create-and-get-access-to-an-s3-bucket">Create and get access to an S3 bucket</h2>
<p>Cloudflare uses Amazon Identity and Access Management (IAM) to gain access to your S3 bucket. The Cloudflare IAM user needs <code>PutObject</code> permission for the bucket.</p>
<p>Logs are written into that bucket as gzipped objects using the S3 Access Control List (ACL)
<code>Bucket-owner-full-control</code> permission.</p>
<p>For illustrative purposes, imagine that you want to store logs in the bucket <code>burritobot</code>, in the <code>logs</code> directory. The S3 URL would then be <code>s3://burritobot/logs</code>.</p>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.
<br /></p>
<p>To enable Logpush to Amazon S3:</p>
<ol>
<li>Create an S3 bucket. Refer to <a href="https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html">instructions from Amazon</a>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10576.md")
</aside>
<ol start="2">
<li>Edit and paste the policy below into <strong>S3</strong> &gt; <strong>Bucket</strong> &gt; <strong>Permissions</strong> &gt; <strong>Bucket Policy</strong>, replacing the <code>Resource</code> value with your own bucket path. The <code>AWS</code> <code>Principal</code> is owned by Cloudflare and should not be changed.</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;Id&quot;: &quot;&lt;POLICY_ID&gt;&quot;,&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Sid&quot;: &quot;Stmt1506627150918&quot;,&#10;			&quot;Action&quot;: [&quot;s3:PutObject&quot;],&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Resource&quot;: &quot;arn:aws:s3:::burritobot/logs/*&quot;,&#10;			&quot;Principal&quot;: {&#10;				&quot;AWS&quot;: [&quot;arn:aws:iam::391854517948:user/cloudflare-logpush&quot;]&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/10575.md")
</aside>
