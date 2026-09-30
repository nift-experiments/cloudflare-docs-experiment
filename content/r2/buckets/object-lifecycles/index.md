---
cp9:
  canonical: https://developers.cloudflare.com/r2/buckets/object-lifecycles/
  description: Configure retention and storage class transition rules for objects in R2 buckets.
  full_title: Object lifecycles · Cloudflare R2 docs
  head_html: <title>Object lifecycles · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure retention and storage class transition rules for objects in R2 buckets."><link rel="canonical" href="https://developers.cloudflare.com/r2/buckets/object-lifecycles/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/buckets/object-lifecycles/index.md"><meta property="og:title" content="Object lifecycles · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure retention and storage class transition rules for objects in R2 buckets."><meta property="og:url" content="https://developers.cloudflare.com/r2/buckets/object-lifecycles/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/buckets/object-lifecycles/#page","headline":"Object lifecycles \u00b7 Cloudflare R2 docs","description":"Configure retention and storage class transition rules for objects in R2 buckets.","url":"https://developers.cloudflare.com/r2/buckets/object-lifecycles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/buckets/object-lifecycles/
  schema: 1
---
<p>Object lifecycles determine the retention period of objects uploaded to your bucket and allow you to specify when objects should transition from Standard storage to Infrequent Access storage.</p>
<p>A lifecycle configuration is a collection of lifecycle rules that define actions to apply to objects during their lifetime.</p>
<p>For example, you can create an object lifecycle rule to delete objects after 90 days, or you can set a rule to transition objects to Infrequent Access storage after 30 days.</p>
<h2 id="behavior">Behavior</h2>
<ul>
<li>Objects will typically be removed from a bucket within 24 hours of the <code>x-amz-expiration</code> value.</li>
<li>When a lifecycle configuration is applied that deletes objects, newly uploaded objects' <code>x-amz-expiration</code> value immediately reflects the expiration based on the new rules, but existing objects may experience a delay. Most objects will be transitioned within 24 hours but may take longer depending on the number of objects in the bucket. While objects are being migrated, you may see old applied rules from the previous configuration.</li>
<li>An object is no longer billable once it has been deleted.</li>
<li>Buckets have a default lifecycle rule to expire multipart uploads seven days after initiation.</li>
<li>When an object is transitioned from Standard storage to Infrequent Access storage, a <a href="/r2/pricing/#class-a-operations">Class A operation</a> is incurred.</li>
<li>When rules conflict and specify both a storage class transition and expire transition within a 24-hour period, the expire (or delete) lifecycle transition takes precedence over transitioning storage class.</li>
</ul>
<h2 id="configure-lifecycle-rules-for-your-bucket">Configure lifecycle rules for your bucket</h2>
<p>When you create an object lifecycle rule, you can specify which prefix you would like it to apply to.</p>
<ul>
<li>Note that object lifecycles currently has a 1000 rule maximum.</li>
<li>Managing object lifecycles is a bucket-level action, and requires an API token with the <a href="/r2/api/tokens/#permission-groups"><code>Workers R2 Storage Write</code></a> permission group.</li>
</ul>
<h3 id="dashboard">Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Locate and select your bucket from the list.
3. From the bucket page, select **Settings**.
4. Under **Object Lifecycle Rules**, select **Add rule**.
5. Fill out the fields for the new rule.
6. When you are done, select **Save changes**.
<h3 id="wrangler">Wrangler</h3>
<ol>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="/workers/wrangler/install-and-update/">Wrangler, the Developer Platform CLI</a>.</li>
<li>Log in to Wrangler with the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code> command</a>.</li>
<li>Add a lifecycle rule to your bucket by running the <a href="/workers/wrangler/commands/r2/#r2-bucket-lifecycle-add"><code>r2 bucket lifecycle add</code> command</a>.</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lifecycle add &lt;BUCKET_NAME&gt; [OPTIONS]&#10;</code></pre>
<p>Alternatively you can set the entire lifecycle configuration for a bucket from a JSON file using the <a href="/workers/wrangler/commands/r2/#r2-bucket-lifecycle-set"><code>r2 bucket lifecycle set</code> command</a>.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lifecycle set &lt;BUCKET_NAME&gt; --file &lt;FILE_PATH&gt;&#10;</code></pre>
<p>The JSON file should be in the format of the request body of the <a href="/api/resources/r2/subresources/buckets/subresources/lifecycle/methods/update/">put object lifecycle configuration API</a>.</p>
<h3 id="s3-api">S3 API</h3>
<p>Below is an example of configuring a lifecycle configuration (a collection of lifecycle rules) with different sets of rules for different potential use cases.</p>
<pre tabindex="0"><code class="language-js">const client = new S3({&#10;	endpoint: &quot;https://&lt;account_id&gt;.r2.cloudflarestorage.com&quot;,&#10;	credentials: {&#10;		accessKeyId: &quot;&lt;access_key_id&gt;&quot;,&#10;		secretAccessKey: &quot;&lt;access_key_secret&gt;&quot;,&#10;	},&#10;	region: &quot;auto&quot;,&#10;});&#10;</code></pre>
<pre tabindex="0"><code class="language-javascript">await client&#10;	.putBucketLifecycleConfiguration({&#10;		Bucket: &quot;testBucket&quot;,&#10;		LifecycleConfiguration: {&#10;			Rules: [&#10;				// Example: deleting objects on a specific date&#10;				// Delete 2019 documents in 2024&#10;				{&#10;					ID: &quot;Delete 2019 Documents&quot;,&#10;					Status: &quot;Enabled&quot;,&#10;					Filter: {&#10;						Prefix: &quot;2019/&quot;,&#10;					},&#10;					Expiration: {&#10;						Date: new Date(&quot;2024-01-01&quot;),&#10;					},&#10;				},&#10;				// Example: transitioning objects to Infrequent Access storage by age&#10;				// Transition objects older than 30 days to Infrequent Access storage&#10;				{&#10;					ID: &quot;Transition Objects To Infrequent Access&quot;,&#10;					Status: &quot;Enabled&quot;,&#10;					Transitions: [&#10;						{&#10;							Days: 30,&#10;							StorageClass: &quot;STANDARD_IA&quot;,&#10;						},&#10;					],&#10;				},&#10;				// Example: deleting objects by age&#10;				// Delete logs older than 90 days&#10;				{&#10;					ID: &quot;Delete Old Logs&quot;,&#10;					Status: &quot;Enabled&quot;,&#10;					Filter: {&#10;						Prefix: &quot;logs/&quot;,&#10;					},&#10;					Expiration: {&#10;						Days: 90,&#10;					},&#10;				},&#10;				// Example: abort all incomplete multipart uploads after a week&#10;				{&#10;					ID: &quot;Abort Incomplete Multipart Uploads&quot;,&#10;					Status: &quot;Enabled&quot;,&#10;					AbortIncompleteMultipartUpload: {&#10;						DaysAfterInitiation: 7,&#10;					},&#10;				},&#10;				// Example: abort user multipart uploads after a day&#10;				{&#10;					ID: &quot;Abort User Incomplete Multipart Uploads&quot;,&#10;					Status: &quot;Enabled&quot;,&#10;					Filter: {&#10;						Prefix: &quot;useruploads/&quot;,&#10;					},&#10;					AbortIncompleteMultipartUpload: {&#10;						// For uploads matching the prefix, this rule will take precedence&#10;						// over the one above due to its earlier expiration.&#10;						DaysAfterInitiation: 1,&#10;					},&#10;				},&#10;			],&#10;		},&#10;	})&#10;	.promise();&#10;</code></pre>
<h2 id="get-lifecycle-rules-for-your-bucket">Get lifecycle rules for your bucket</h2>
<h3 id="wrangler-1">Wrangler</h3>
<p>To get the list of lifecycle rules associated with your bucket, run the <a href="/workers/wrangler/commands/r2/#r2-bucket-lifecycle-list"><code>r2 bucket lifecycle list</code> command</a>.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lifecycle list &lt;BUCKET_NAME&gt;&#10;</code></pre>
<h3 id="s3-api-1">S3 API</h3>
<pre tabindex="0"><code class="language-js">import S3 from &quot;aws-sdk/clients/s3.js&quot;;&#10;&#10;// Configure the S3 client to talk to R2.&#10;const client = new S3({&#10;	endpoint: &quot;https://&lt;account_id&gt;.r2.cloudflarestorage.com&quot;,&#10;	credentials: {&#10;		accessKeyId: &quot;&lt;access_key_id&gt;&quot;,&#10;		secretAccessKey: &quot;&lt;access_key_secret&gt;&quot;,&#10;	},&#10;	region: &quot;auto&quot;,&#10;});&#10;&#10;// Get lifecycle configuration for bucket&#10;console.log(&#10;	await client&#10;		.getBucketLifecycleConfiguration({&#10;			Bucket: &quot;bucketName&quot;,&#10;		})&#10;		.promise(),&#10;);&#10;</code></pre>
<h2 id="delete-lifecycle-rules-from-your-bucket">Delete lifecycle rules from your bucket</h2>
<h3 id="dashboard-1">Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Locate and select your bucket from the list.
3. From the bucket page, select **Settings**.
4. Under **Object lifecycle rules**, select the rules you would like to delete.
5. When you are done, select **Delete rule(s)**.
<h3 id="wrangler-2">Wrangler</h3>
<p>To remove a specific lifecycle rule from your bucket, run the <a href="/workers/wrangler/commands/r2/#r2-bucket-lifecycle-remove"><code>r2 bucket lifecycle remove</code> command</a>.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lifecycle remove &lt;BUCKET_NAME&gt; --id &lt;RULE_ID&gt;&#10;</code></pre>
<h3 id="s3-api-2">S3 API</h3>
<pre tabindex="0"><code class="language-js">import S3 from &quot;aws-sdk/clients/s3.js&quot;;&#10;&#10;// Configure the S3 client to talk to R2.&#10;const client = new S3({&#10;	endpoint: &quot;https://&lt;account_id&gt;.r2.cloudflarestorage.com&quot;,&#10;	credentials: {&#10;		accessKeyId: &quot;&lt;access_key_id&gt;&quot;,&#10;		secretAccessKey: &quot;&lt;access_key_secret&gt;&quot;,&#10;	},&#10;	region: &quot;auto&quot;,&#10;});&#10;&#10;// Delete lifecycle configuration for bucket&#10;await client&#10;	.deleteBucketLifecycle({&#10;		Bucket: &quot;bucketName&quot;,&#10;	})&#10;	.promise();&#10;</code></pre>
