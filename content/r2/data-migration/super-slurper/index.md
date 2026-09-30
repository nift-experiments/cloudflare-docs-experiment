---
cp9:
  canonical: https://developers.cloudflare.com/r2/data-migration/super-slurper/
  description: Copy objects from other cloud providers to R2 in a one-off bulk migration job.
  full_title: Super Slurper · Cloudflare R2 docs
  head_html: <title>Super Slurper · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Copy objects from other cloud providers to R2 in a one-off bulk migration job."><link rel="canonical" href="https://developers.cloudflare.com/r2/data-migration/super-slurper/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/data-migration/super-slurper/index.md"><meta property="og:title" content="Super Slurper · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Copy objects from other cloud providers to R2 in a one-off bulk migration job."><meta property="og:url" content="https://developers.cloudflare.com/r2/data-migration/super-slurper/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/data-migration/super-slurper/#page","headline":"Super Slurper \u00b7 Cloudflare R2 docs","description":"Copy objects from other cloud providers to R2 in a one-off bulk migration job.","url":"https://developers.cloudflare.com/r2/data-migration/super-slurper/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/data-migration/super-slurper/
  schema: 1
---
<p>Super Slurper allows you to quickly and easily copy objects from other cloud providers to an R2 bucket of your choice.</p>
<p>Migration jobs:</p>
<ul>
<li>Preserve custom object metadata from source bucket by copying them on the migrated objects on R2.</li>
<li>Do not delete any objects from source bucket.</li>
<li>Use TLS encryption over HTTPS connections for safe and private object transfers.</li>
</ul>
<h2 id="when-to-use-super-slurper">When to use Super Slurper</h2>
<p>Using Super Slurper as part of your strategy can be a good choice if the cloud storage bucket you are migrating consists primarily of objects less than 1 TB. Objects greater than 1 TB will be skipped and need to be copied separately.</p>
<p>For migration use cases that do not meet the above criteria, we recommend using tools such as <a href="/r2/examples/rclone/">rclone</a>.</p>
<h2 id="use-super-slurper-to-migrate-data-to-r2">Use Super Slurper to migrate data to R2</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 data migration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Migrate files**.
3. Select the source cloud storage provider that you will be migrating data from.
4. Enter your source bucket name and associated credentials and select **Next**.
5. Enter your R2 bucket name and associated credentials and select **Next**.
6. After you finish reviewing the details of your migration, select **Migrate files**.
<p>You can view the status of your migration job at any time by selecting your migration from <strong>Data Migration</strong> page.</p>
<h3 id="source-bucket-options">Source bucket options</h3>
<h4 id="bucket-sub-path-optional">Bucket sub path (optional)</h4>
<p>This setting specifies the prefix within the source bucket where objects will be copied from.</p>
<h3 id="destination-r2-bucket-options">Destination R2 bucket options</h3>
<h4 id="overwrite-files">Overwrite files?</h4>
<p>This setting determines what happens when an object being copied from the source storage bucket matches the path of an existing object in the destination R2 bucket. There are two options:</p>
<ul>
<li>Overwrite (default)</li>
<li>Skip</li>
</ul>
<h2 id="supported-cloud-storage-providers">Supported cloud storage providers</h2>
<p>Cloudflare currently supports copying data from the following cloud object storage providers to R2:</p>
<ul>
<li>Amazon S3</li>
<li>Cloudflare R2</li>
<li>Google Cloud Storage (GCS)</li>
<li>All S3-compatible storage providers</li>
</ul>
<h3 id="tested-s3-compatible-storage-providers">Tested S3-compatible storage providers</h3>
<p>The following S3-compatible storage providers have been tested and verified to work with Super Slurper:</p>
<ul>
<li>Backblaze B2</li>
<li>DigitalOcean Spaces</li>
<li>Scaleway Object Storage</li>
<li>Wasabi Cloud Object Storage</li>
</ul>
<p>Super Slurper should support transfers from all S3-compatible storage providers, but the ones listed have been explicitly tested.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11466.md")
</aside>
<h2 id="create-credentials-for-storage-providers">Create credentials for storage providers</h2>
<h3 id="amazon-s3">Amazon S3</h3>
<p>To copy objects from Amazon S3, Super Slurper requires access permissions to your S3 bucket. While you can use any AWS Identity and Access Management (IAM) user credentials with the correct permissions, Cloudflare recommends you create a user with a narrow set of permissions.</p>
<p>To create credentials with the correct permissions:</p>
<ol>
<li>Log in to your AWS IAM account.</li>
<li>Create a policy with the following format and replace <code>&lt;BUCKET_NAME&gt;</code> with the bucket you want to grant access to:</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Action&quot;: [&quot;s3:Get*&quot;, &quot;s3:List*&quot;],&#10;			&quot;Resource&quot;: [&quot;arn:aws:s3:::&lt;BUCKET_NAME&gt;&quot;, &quot;arn:aws:s3:::&lt;BUCKET_NAME&gt;/*&quot;]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<ol start="3">
<li>Create a new user and attach the created policy to that user.</li>
</ol>
<p>You can now use both the Access Key ID and Secret Access Key when defining your source bucket.</p>
<h3 id="google-cloud-storage">Google Cloud Storage</h3>
<p>To copy objects from Google Cloud Storage (GCS), Super Slurper requires access permissions to your GCS bucket. You can use the Google Cloud predefined <code>Storage Admin</code> role, but Cloudflare recommends creating a custom role with a narrower set of permissions.</p>
<p>To create a custom role with the necessary permissions:</p>
<ol>
<li>Log in to your Google Cloud console.</li>
<li>Go to <strong>IAM &amp; Admin</strong> &gt; <strong>Roles</strong>.</li>
<li>Find the <code>Storage Object Viewer</code> role and select <strong>Create role from this role</strong>.</li>
<li>Give your new role a name.</li>
<li>Select <strong>Add permissions</strong> and add the <code>storage.buckets.get</code> permission.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>To create credentials with your custom role:</p>
<ol>
<li>Log in to your Google Cloud console.</li>
<li>Go to <strong>IAM &amp; Admin</strong> &gt; <strong>Service Accounts</strong>.</li>
<li>Create a service account with the your custom role.</li>
<li>Go to the <strong>Keys</strong> tab of the service account you created.</li>
<li>Select <strong>Add Key</strong> &gt; <strong>Create a new key</strong> and download the JSON key file.</li>
</ol>
<p>You can now use this JSON key file when enabling Super Slurper.</p>
<h2 id="caveats">Caveats</h2>
<h3 id="etags">ETags</h3>
<p>While R2's ETag generation is compatible with S3's during the regular course of operations, ETags are not guaranteed to be equal when an object is migrated using Super Slurper.
Super Slurper makes autonomous decisions about the operations it uses when migrating objects to optimize for performance and network usage. It may choose to migrate an object in multiple parts, which affects <a href="/r2/objects/upload-objects/#etags">ETag calculation</a>.</p>
<p>For example, a 320 MiB object originally uploaded to S3 using a single <code>PutObject</code> operation might be migrated to R2 via multipart operations. In this case, its ETag on R2 will not be the same as its ETag on S3.
Similarly, an object originally uploaded to S3 using multipart operations might also have a different ETag on R2 if the part sizes Super Slurper chooses for its migration differ from the part sizes this object was originally uploaded with.</p>
<p>Relying on matching ETags before and after the migration is therefore discouraged.</p>
<h3 id="archive-storage-classes">Archive storage classes</h3>
<p>Objects stored using AWS S3 <a href="https://aws.amazon.com/s3/storage-classes/#Archive">archival storage classes</a> will be skipped and need to be copied separately. Specifically:</p>
<ul>
<li>Files stored using S3 Glacier tiers (not including Glacier Instant Retrieval) will be skipped and logged in the migration log.</li>
<li>Files stored using S3 Intelligent Tiering and placed in Deep Archive tier will be skipped and logged in the migration log.</li>
</ul>
