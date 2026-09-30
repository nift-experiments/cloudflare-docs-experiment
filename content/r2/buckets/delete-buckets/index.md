---
cp9:
  canonical: https://developers.cloudflare.com/r2/buckets/delete-buckets/
  description: Empty all objects from an R2 bucket and permanently delete it.
  full_title: Delete buckets · Cloudflare R2 docs
  head_html: <title>Delete buckets · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Empty all objects from an R2 bucket and permanently delete it."><link rel="canonical" href="https://developers.cloudflare.com/r2/buckets/delete-buckets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/buckets/delete-buckets/index.md"><meta property="og:title" content="Delete buckets · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Empty all objects from an R2 bucket and permanently delete it."><meta property="og:url" content="https://developers.cloudflare.com/r2/buckets/delete-buckets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/buckets/delete-buckets/#page","headline":"Delete buckets \u00b7 Cloudflare R2 docs","description":"Empty all objects from an R2 bucket and permanently delete it.","url":"https://developers.cloudflare.com/r2/buckets/delete-buckets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/buckets/delete-buckets/
  schema: 1
---
<p>To delete an R2 bucket, you must first remove all objects from it. Once the bucket is empty, you can delete it.</p>
<h2 id="empty-a-bucket">Empty a bucket</h2>
<p>Emptying a bucket deletes every object inside it. The bucket itself and its configuration (lifecycle rules, CORS, event notifications, custom domains) are preserved.</p>
<p>Objects removed during this process cannot be recovered. If your bucket has <a href="/r2/buckets/bucket-locks/">bucket lock rules</a>, you must remove them before emptying the bucket.</p>
<p>You can empty a bucket in various ways.</p>
<h3 id="dashboard">Dashboard</h3>
<p>The dashboard provides an <strong>Empty Bucket</strong> action that handles this for you, regardless of how many objects the bucket contains. For large buckets, the operation runs in the background and the dashboard displays progress until all objects have been removed.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the bucket you want to empty.
3. Go to the **Settings** tab.
4. Scroll to the **Empty Bucket** section.
5. Select **Empty**.
6. Confirm the action in the dialog that appears.
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11490.md")
</aside>
<h3 id="object-lifecycle-rules">Object lifecycle rules</h3>
<p>You can configure an <a href="/r2/buckets/object-lifecycles/">object lifecycle rule</a> that expires all objects in the bucket.</p>
<ol>
<li>Add a lifecycle rule with no prefix filter and an expiration of 1 day.</li>
<li>Wait for the rule to take effect. Objects are typically removed within 24 hours, but large buckets may take longer.</li>
<li>After the bucket is empty, remove the lifecycle rule.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11489.md")
</aside>
<h4 id="wrangler">Wrangler</h4>
<p>Add a lifecycle rule that expires all objects after 1 day:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lifecycle add &lt;BUCKET_NAME&gt; --expire-days 1&#10;</code></pre>
<p>After the bucket is empty, remove the rule:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lifecycle remove &lt;BUCKET_NAME&gt; --id &lt;RULE_ID&gt;&#10;</code></pre>
<p>For the full list of lifecycle commands, refer to <a href="/workers/wrangler/commands/r2/#r2-bucket-lifecycle-add">Wrangler R2 commands</a>.</p>
<p>You can also configure lifecycle rules using the S3 API or the dashboard. For more information, refer to <a href="/r2/buckets/object-lifecycles/">Object lifecycles</a>.</p>
<h3 id="other-approaches">Other approaches</h3>
<p>You can also write a script that lists and deletes objects in batches using the <a href="/r2/api/s3/api/">S3 API</a> or <a href="/r2/api/workers/workers-api-usage/">Workers API</a>, or use <a href="/r2/examples/rclone/">rclone</a> to remove objects from the command line.</p>
<h2 id="delete-a-bucket">Delete a bucket</h2>
<p>Once a bucket is empty, you can permanently delete it. Deleting a bucket removes the bucket and all of its configuration, including lifecycle rules, CORS settings, event notifications, and custom domains.</p>
<p>You can delete a bucket in various ways.</p>
<h3 id="dashboard-1">Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the bucket you want to delete.
3. Go to the **Settings** tab.
4. Scroll to the **Delete Bucket** section. If the bucket is not empty, select **Empty Bucket** first to clear all objects.
5. Select **Delete**.
6. Confirm the action in the dialog that appears.
<h3 id="wrangler-1">Wrangler</h3>
<p>Use the <a href="/workers/wrangler/commands/r2/#r2-bucket-delete"><code>r2 bucket delete</code></a> command to delete an empty bucket:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket delete &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>The command fails if the bucket still contains objects. Empty the bucket before running this command.</p>
<h3 id="api">API</h3>
<p>Use the <a href="/api/resources/r2/subresources/buckets/methods/delete/">delete bucket API endpoint</a> to delete an empty bucket:</p>
<pre tabindex="0"><code class="language-sh">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/r2/buckets/&lt;BUCKET_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>If the bucket is in a <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a>, include the <code>cf-r2-jurisdiction</code> header:</p>
<pre tabindex="0"><code class="language-sh">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/r2/buckets/&lt;BUCKET_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;cf-r2-jurisdiction: eu&quot;&#10;</code></pre>
<h2 id="behavior">Behavior</h2>
<ul>
<li>A bucket must be completely empty before it can be deleted. Attempting to delete a bucket that contains objects returns an error.</li>
<li>You cannot empty a bucket that has <a href="/r2/buckets/bucket-locks/">bucket lock rules</a>. Remove all lock rules before emptying the bucket.</li>
<li><a href="/r2/buckets/event-notifications/">Event notifications</a> configured on the bucket are removed when the bucket is deleted.</li>
<li>If you use a <a href="/r2/buckets/public-buckets/#custom-domains">custom domain</a> with the bucket, remove the domain association before or after deletion to avoid dangling DNS records.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-delete-objects-r2-objects-delete-objects"><a href="/r2/objects/delete-objects/">Delete objects</a></h3><p>Delete individual objects or folders from an R2 bucket.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-bucket-locks-r2-buckets-bucket-locks"><a href="/r2/buckets/bucket-locks/">Bucket locks</a></h3><p>Prevent accidental deletion by setting retention policies on objects.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles"><a href="/r2/buckets/object-lifecycles/">Object lifecycles</a></h3><p>Automatically expire objects after a specified period instead of emptying manually.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-create-buckets-r2-buckets-create-buckets"><a href="/r2/buckets/create-buckets/">Create buckets</a></h3><p>Create a new R2 bucket after deleting an existing one.</p></div>
