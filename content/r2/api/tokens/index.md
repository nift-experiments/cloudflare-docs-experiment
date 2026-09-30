---
cp9:
  canonical: https://developers.cloudflare.com/r2/api/tokens/
  description: Generate and manage R2 API tokens for use with S3-compatible SDKs and APIs.
  full_title: Authentication · Cloudflare R2 docs
  head_html: <title>Authentication · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate and manage R2 API tokens for use with S3-compatible SDKs and APIs."><link rel="canonical" href="https://developers.cloudflare.com/r2/api/tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/api/tokens/index.md"><meta property="og:title" content="Authentication · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate and manage R2 API tokens for use with S3-compatible SDKs and APIs."><meta property="og:url" content="https://developers.cloudflare.com/r2/api/tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/api/tokens/#page","headline":"Authentication \u00b7 Cloudflare R2 docs","description":"Generate and manage R2 API tokens for use with S3-compatible SDKs and APIs.","url":"https://developers.cloudflare.com/r2/api/tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/api/tokens/
  schema: 1
---
<p>You can generate an API token to serve as the Access Key for usage with existing S3-compatible SDKs or XML APIs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11501.md")
</aside>
<p>You must purchase R2 before you can generate an API token.</p>
<p>To create an API token:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under the <strong>Account Details</strong> section, select <strong>Manage</strong> next to <strong>API Tokens</strong>.</li>
<li>Choose to create either:
<ul>
<li><strong>Create Account API token</strong> - These tokens are tied to the Cloudflare account itself and can be used by any authorized system or user. Only users with the Super Administrator role can view or create them. These tokens remain valid until manually revoked.</li>
<li><strong>Create User API token</strong> - These tokens are tied to your individual Cloudflare user. They inherit your personal permissions and become inactive if your user is removed from the account.</li>
</ul>
</li>
<li>Under <strong>Permissions</strong>, choose a permission types for your token. Refer to <a href="#permissions">Permissions</a> for information about each option.</li>
<li>(Optional) If you select the <strong>Object Read and Write</strong> or <strong>Object Read</strong> permissions, you can scope your token to a set of buckets.</li>
<li>Select <strong>Create Account API token</strong> or <strong>Create User API token</strong>.</li>
</ol>
<p>After your token has been successfully created, review your <strong>Secret Access Key</strong> and <strong>Access Key ID</strong> values. These may often be referred to as Client Secret and Client ID, respectively.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11500.md")
</aside>
<p>You will also need to configure the <code>endpoint</code> in your S3 client to <code>https://&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com</code>.</p>
<p>Find your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID in the Cloudflare dashboard</a>.</p>
<p>Buckets created with jurisdictions must be accessed via jurisdiction-specific endpoints:</p>
<ul>
<li>European Union (EU): <code>https://&lt;ACCOUNT_ID&gt;.eu.r2.cloudflarestorage.com</code></li>
<li>FedRAMP: <code>https://&lt;ACCOUNT_ID&gt;.fedramp.r2.cloudflarestorage.com</code></li>
<li>United States (US): <code>https://&lt;ACCOUNT_ID&gt;.us.r2.cloudflarestorage.com</code></li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11499.md")
</aside>
<h2 id="permissions">Permissions</h2>
<table>
<thead>
<tr>
<th>Permission</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Admin Read &amp; Write</td>
<td>Allows the ability to create, list, and delete buckets, edit bucket configuration, read, write, and list objects, and read and write to data catalog tables and associated metadata.</td>
</tr>
<tr>
<td>Admin Read only</td>
<td>Allows the ability to list buckets and view bucket configuration, read and list objects, and read from the data catalog tables and associated metadata.</td>
</tr>
<tr>
<td>Object Read &amp; Write</td>
<td>Allows the ability to read, write, and list objects in specific buckets.</td>
</tr>
<tr>
<td>Object Read only</td>
<td>Allows the ability to read and list objects in specific buckets.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="considerations">Considerations</h3>
@markup("md", "content/.markup/bodies/11498.md")
</aside>
<h2 id="create-api-tokens-via-api">Create API tokens via API</h2>
<p>You can create API tokens via the API and use them to generate corresponding Access Key ID and Secret Access Key values. To get started, refer to <a href="/fundamentals/api/how-to/create-via-api/">Create API tokens via the API</a>. Below are the specifics for R2.</p>
<h3 id="access-policy">Access Policy</h3>
<p>An Access Policy specifies what resources the token can access and the permissions it has.</p>
<h4 id="resources">Resources</h4>
<p>There are two relevant resource types for R2: <code>Account</code> and <code>Bucket</code>. For more information on the Account resource type, refer to <a href="/fundamentals/api/how-to/create-via-api/#account">Account</a>.</p>
<h5 id="bucket">Bucket</h5>
<p>Include a set of R2 buckets or all buckets in an account.</p>
<p>A specific bucket is represented as:</p>
<pre tabindex="0"><code class="language-json">&quot;com.cloudflare.edge.r2.bucket.&lt;ACCOUNT_ID&gt;_&lt;JURISDICTION&gt;_&lt;BUCKET_NAME&gt;&quot;: &quot;*&quot;&#10;</code></pre>
<ul>
<li><code>ACCOUNT_ID</code>: Refer to <a href="/fundamentals/account/find-account-and-zone-ids/#find-account-id-workers-and-pages">Find zone and account IDs</a>.</li>
<li><code>JURISDICTION</code>: The <a href="/r2/reference/data-location/#available-jurisdictions">jurisdiction</a> where the R2 bucket lives. For buckets not created in a specific jurisdiction this value will be <code>default</code>.</li>
<li><code>BUCKET_NAME</code>: The name of the bucket your Access Policy applies to.</li>
</ul>
<p>All buckets in an account are represented as:</p>
<pre tabindex="0"><code class="language-json">&quot;com.cloudflare.api.account.&lt;ACCOUNT_ID&gt;&quot;: {&#10;  &quot;com.cloudflare.edge.r2.bucket.*&quot;: &quot;*&quot;&#10;}&#10;</code></pre>
<ul>
<li><code>ACCOUNT_ID</code>: Refer to <a href="/fundamentals/account/find-account-and-zone-ids/#find-account-id-workers-and-pages">Find zone and account IDs</a>.</li>
</ul>
<h4 id="permission-groups">Permission groups</h4>
<p>Determine what <a href="/fundamentals/api/how-to/create-via-api/#permission-groups">permission groups</a> should be applied.</p>
<table>
<tbody>
<th colspan="5" rowspan="1">
			Permission group
</th>
<th colspan="5" rowspan="1">
			Resource
</th>
<th colspan="5" rowspan="1">
			Description
</th>
<tr>
<td colspan="5" rowspan="1">
				<code>Workers R2 Storage Write</code>
</td>
<td colspan="5" rowspan="1">
				Account
</td>
<td colspan="5" rowspan="1">
				Can create, delete, and list buckets, edit bucket configuration, and
				read, write, and list objects.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				<code>Workers R2 Storage Read</code>
</td>
<td colspan="5" rowspan="1">
				Account
</td>
<td colspan="5" rowspan="1">
				Can list buckets and view bucket configuration, and read and list
				objects.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				<code>Workers R2 Storage Bucket Item Write</code>
</td>
<td colspan="5" rowspan="1">
				Bucket
</td>
<td colspan="5" rowspan="1">
				Can read, write, and list objects in buckets.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				<code>Workers R2 Storage Bucket Item Read</code>
</td>
<td colspan="5" rowspan="1">
				Bucket
</td>
<td colspan="5" rowspan="1">
				Can read and list objects in buckets.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				<code>Workers R2 Data Catalog Write</code>
</td>
<td colspan="5" rowspan="1">
				Account
</td>
<td colspan="5" rowspan="1">
				Can read from and write to data catalogs. This permission allows
				access to the Iceberg REST catalog interface.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
				<code>Workers R2 Data Catalog Read</code>
</td>
<td colspan="5" rowspan="1">
				Account
</td>
<td colspan="5" rowspan="1">
				Can read from data catalogs. This permission allows read-only
				access to the Iceberg REST catalog interface.
</td>
</tr>
</tbody>
</table>
<h4 id="example-access-policy">Example Access Policy</h4>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;f267e341f3dd4697bd3b9f71dd96247f&quot;,&#10;		&quot;effect&quot;: &quot;allow&quot;,&#10;		&quot;resources&quot;: {&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_default_my-bucket&quot;: &quot;*&quot;,&#10;			&quot;com.cloudflare.edge.r2.bucket.4793d734c0b8e484dfc37ec392b5fa8a_eu_my-eu-bucket&quot;: &quot;*&quot;&#10;		},&#10;		&quot;permission_groups&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;6a018a9f2fc74eb6b293b0c548f38b39&quot;,&#10;				&quot;name&quot;: &quot;Workers R2 Storage Bucket Item Read&quot;&#10;			}&#10;		]&#10;	}&#10;]&#10;</code></pre>
<h3 id="get-s3-api-credentials-from-an-api-token">Get S3 API credentials from an API token</h3>
<p>You can get the Access Key ID and Secret Access Key values from the response of the <a href="/api/resources/user/subresources/tokens/methods/create/">Create Token</a> API:</p>
<ul>
<li>Access Key ID: The <code>id</code> of the API token.</li>
<li>Secret Access Key: The SHA-256 hash of the API token <code>value</code>.</li>
</ul>
<p>Refer to <a href="/r2/examples/authenticate-r2-auth-tokens/">Authenticate against R2 API using auth tokens</a> for a tutorial with JavaScript, Python, and Go examples.</p>
<h2 id="temporary-credentials">Temporary credentials</h2>
<p>To issue short-lived, scoped credentials derived from an API token, use <a href="/r2/api/s3/temporary-credentials/">temporary credentials</a>. R2 supports generating them via the Temporary Credentials API or locally by signing a JWT with the parent token's secret access key.</p>
