---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/
  description: Host static assets on Cloudflare's global network and deliver faster load times worldwide with Workers for Platforms.
  full_title: Static assets · Cloudflare for Platforms docs
  head_html: <title>Static assets · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Host static assets on Cloudflare&#x27;s global network and deliver faster load times worldwide with Workers for Platforms."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/index.md"><meta property="og:title" content="Static assets · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Host static assets on Cloudflare&#x27;s global network and deliver faster load times worldwide with Workers for Platforms."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare for Platforms"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/#page","headline":"Static assets \u00b7 Cloudflare for Platforms docs","description":"Host static assets on Cloudflare's global network and deliver faster load times worldwide with Workers for Platforms.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/
  schema: 1
---
<p>Workers for Platforms lets you deploy front-end applications at scale. By hosting static assets on Cloudflare's global network, you can deliver faster load times worldwide and eliminate the need for external infrastructure. You can also combine these static assets with dynamic logic in Cloudflare Workers, providing a full-stack experience for your customers.</p>
<h3 id="what-you-can-build">What you can build</h3>
<h4 id="static-sites">Static sites</h4>
<p>Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites.</p>
<h4 id="full-stack-applications">Full-stack applications</h4>
<p>Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. Store and retrieve data using Cloudflare KV, D1, and R2 Storage, allowing you to serve both front-end assets and backend logic from a single Worker.</p>
<h3 id="benefits">Benefits</h3>
<h4 id="global-caching-for-faster-performance">Global caching for faster performance</h4>
<p>Cloudflare automatically caches static assets at data centers worldwide, reducing latency and improving load times by up to 2x for users everywhere.</p>
<h4 id="scalability-without-infrastructure-management">Scalability without infrastructure management</h4>
<p>Your applications scale automatically to handle high traffic without requiring you to provision or manage infrastructure. Cloudflare dynamically adjusts to demand in real time.</p>
<h4 id="unified-deployment-for-static-and-dynamic-content">Unified deployment for static and dynamic content</h4>
<p>Deploy front-end assets alongside server-side logic, all within Cloudflare Workers. This eliminates the need for a separate hosting provider and ensures a streamlined deployment process.</p>
<hr />
<h2 id="deploy-static-assets-to-user-workers">Deploy static assets to User Workers</h2>
<p>It is common that, as the Platform, you will be responsible for uploading static assets on behalf of your end users. This often looks like this:</p>
<ol>
<li>Your user uploads files (HTML, CSS, images) through your interface.</li>
<li>Your platform interacts with the Workers for Platforms APIs to attach the static assets to the User Worker script.</li>
</ol>
<p>Once you receive the static files from your users (for a new or updated site), complete the following steps to attach the files to the corresponding User Worker:</p>
<ol>
<li>Create an Upload Session</li>
<li>Upload file contents</li>
<li>Deploy/Update the Worker</li>
</ol>
<p>After these steps are completed, the User Worker's static assets will be live on the Cloudflare's global network.</p>
<h3 id="1-create-an-upload-session"><ol>
<li>Create an Upload Session</li>
</ol></h3>
<p>Before sending any file data, you need to tell Cloudflare which files you intend to upload. That list of files is called a manifest. Each item in the manifest includes:</p>
<ul>
<li>A file path (for example, <code>&quot;/index.html&quot;</code> or <code>&quot;/assets/logo.png&quot;</code>)</li>
<li>A hash (32-hex characters) representing the file contents</li>
<li>The file size in bytes</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="asset-isolation-considerations">Asset Isolation Considerations</h3>
@markup("md", "content/.markup/bodies/4215.md")
</aside>
<h4 id="example-manifest-json">Example manifest (JSON)</h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;/index.html&quot;: {&#10;		&quot;hash&quot;: &quot;08f1dfda4574284ab3c21666d1ee8c7d4&quot;,&#10;		&quot;size&quot;: 1234&#10;	},&#10;	&quot;/styles.css&quot;: {&#10;		&quot;hash&quot;: &quot;36b8be012ee77df5f269b11b975611d3&quot;,&#10;		&quot;size&quot;: 5678&#10;	}&#10;}&#10;</code></pre>
<p>To start the upload process, send a POST request to the Create Assets Upload Session <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/asset_upload/methods/create/">API endpoint</a>.</p>
<pre tabindex="0"><code class="language-bash">POST /accounts/{account_id}/workers/dispatch/namespaces/{namespace}/scripts/{script_name}/assets-upload-session&#10;</code></pre>
<p>Path Parameters:</p>
<ul>
<li><code>namespace</code>: Name of the Workers for Platforms dispatch namespace</li>
<li><code>script_name</code>: Name of the User Worker</li>
</ul>
<p>In the request body, include a JSON object listing each file path along with its hash and size. This helps Cloudflare identify which files you intend to upload and allows Cloudflare to check if any of them are already stored.</p>
<h4 id="sample-request">Sample request</h4>
<pre tabindex="0"><code class="language-bash">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$NAMESPACE_NAME/scripts/$SCRIPT_NAME/assets-upload-session&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;manifest&quot;: {&#10;      &quot;/index.html&quot;: {&#10;        &quot;hash&quot;: &quot;08f1dfda4574284ab3c21666d1ee8c7d4&quot;,&#10;        &quot;size&quot;: 1234&#10;      },&#10;      &quot;/styles.css&quot;: {&#10;        &quot;hash&quot;: &quot;36b8be012ee77df5f269b11b975611d3&quot;,&#10;        &quot;size&quot;: 5678&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="generating-the-hash">Generating the hash</h4>
<p>You can compute a SHA-256 digest of the file contents, then truncate or otherwise represent it consistently as a 32-hex-character string. Make sure to do it the same way each time so Cloudflare can reliably match files across uploads.</p>
<h4 id="api-response">API Response</h4>
<p>If all the files are already stored on Cloudflare, the response will only return the JWT token. If new or updated files are needed, the response will return:</p>
<ul>
<li><code>jwt</code>: An upload token (valid for 1 hour) which will be used in the API request to upload the file contents (Step 2).</li>
<li><code>buckets</code>: An array of file-hash groups indicating which files to upload together. Files that have been recently uploaded will not appear in buckets, since Cloudflare already has them.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4214.md")
</aside>
<h3 id="2-upload-file-contents"><ol start="2">
<li>Upload File Contents</li>
</ol></h3>
<p>If the response to the Upload Session API returns <code>buckets</code>, that means you have new or changed files that need to be uploaded to Cloudflare.</p>
<p>Use the <a href="/api/resources/workers/subresources/assets/subresources/upload/">Workers Assets Upload API</a> to transmit the raw file bytes in base64-encoded format for any missing or changed files. Once uploaded, Cloudflare will store these files so they can then be attached to a User Worker.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4213.md")
</aside>
<h4 id="api-request-authentication">API Request Authentication</h4>
<p>Unlike most Cloudflare API calls that use an account-wide API token in the Authorization header, uploading file contents requires using the short-lived JWT token returned in the <code>jwt</code> field of the <code>assets-upload-session</code> response.</p>
<p>Include it as a Bearer token in the header:</p>
<pre tabindex="0"><code class="language-bash">Authorization: Bearer &lt;upload-session-token&gt;&#10;</code></pre>
<p>This token is valid for one hour and must be supplied for each upload request to the Workers Assets Upload API.</p>
<h4 id="file-fields-multipart-form-data">File fields (multipart/form-data)</h4>
<p>You must send the files as multipart/form-data with base64-encoded content:</p>
<ul>
<li>Field name: The file hash (for example, <code>36b8be012ee77df5f269b11b975611d3</code>)</li>
<li>Field value: A Base64-encoded string of the file's raw bytes</li>
</ul>
<h4 id="example-uploading-multiple-files-within-a-single-bucket">Example: Uploading multiple files within a single bucket</h4>
<p>If your Upload Session response listed a single &quot;bucket&quot; containing two file hashes:</p>
<pre tabindex="0"><code class="language-json">&quot;buckets&quot;: [&#10;  [&#10;    &quot;08f1dfda4574284ab3c21666d1ee8c7d4&quot;,&#10;    &quot;36b8be012ee77df5f269b11b975611d3&quot;&#10;  ]&#10;]&#10;</code></pre>
<p>You can upload both files in one request, each as a form-data field:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/assets/upload?base64=true&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;upload-session-token&gt;&quot; \&#10;  &#45;F &quot;08f1dfda4574284ab3c21666d1ee8c7d4=&lt;BASE64_OF_INDEX_HTML&gt;&quot; \&#10;  &#45;F &quot;36b8be012ee77df5f269b11b975611d3=&lt;BASE64_OF_STYLES_CSS&gt;&quot;&#10;</code></pre>
<ul>
<li><code>&lt;upload-session-token&gt;</code> is the token from step 1's assets-upload-session response</li>
<li><code>&lt;BASE64_OF_INDEX_HTML&gt;</code> is the Base64-encoded content of index.html</li>
<li><code>&lt;BASE64_OF_STYLES_CSS&gt;</code> is the Base64-encoded content of styles.css</li>
</ul>
<p>If you have multiple buckets (for example, <code>[[&quot;hashA&quot;], [&quot;hashB&quot;], [&quot;hashC&quot;]]</code>), you might need to repeat this process for each bucket, making one request per bucket group.</p>
<p>Once every file in the manifest has been uploaded, a status code of <code>201</code> will be returned, with the <code>jwt</code> field present. This JWT is a final &quot;completion&quot; token which can be used to create a deployment of a Worker with this set of assets. This completion token is valid for 1 hour.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;jwt&quot;: &quot;&lt;completion-token&gt;&quot;&#10;	}&#10;}&#10;</code></pre>
<p><code>&lt;completion-token&gt;</code> indicates that Cloudflare has successfully received and stored the file contents specified by your manifest. You will use this <code>&lt;completion-token&gt;</code> in Step 3 to finalize the attachment of these files to the Worker.</p>
<h3 id="3-deploy-the-user-worker-with-static-assets"><ol start="3">
<li>Deploy the User Worker with static assets</li>
</ol></h3>
<p>Now that Cloudflare has all the files it needs (from the previous upload steps), you must attach them to the User Worker by making a PUT request to the <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">Upload User Worker API</a>. This final step links the static assets to the User Worker using the completion token you received after uploading file contents.</p>
<p>You can also specify any optional settings under the <code>assets.config</code> field to customize how your files are served (for example, to handle trailing slashes in HTML paths).</p>
<h4 id="api-request-example">API request example</h4>
<pre tabindex="0"><code class="language-bash">curl -X PUT \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$NAMESPACE_NAME/scripts/$SCRIPT_NAME&quot; \&#10;  &#45;H &quot;Content-Type: multipart/form-data&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;F &#x27;metadata={&#10;    &quot;main_module&quot;: &quot;index.js&quot;,&#10;    &quot;assets&quot;: {&#10;      &quot;jwt&quot;: &quot;&lt;completion-token&gt;&quot;,&#10;      &quot;config&quot;: {&#10;        &quot;html_handling&quot;: &quot;auto-trailing-slash&quot;&#10;      }&#10;    },&#10;    &quot;compatibility_date&quot;: &quot;2025-01-24&quot;&#10;  };type=application/json&#x27; \&#10;  &#45;F &#x27;index.js=@/path/to/index.js;type=application/javascript&#x27;&#10;</code></pre>
<ul>
<li>The <code>&quot;jwt&quot;: &quot;&lt;completion-token&gt;&quot;</code> links the newly uploaded files to the Worker</li>
<li>Including &quot;html_handling&quot; (or other fields under &quot;config&quot;) is optional and can customize how static files are served</li>
<li>If the user's Worker code has not changed, you can omit the code file or re-upload the same index.js</li>
</ul>
<p>Once this PUT request succeeds, the files are served on the User Worker. Requests routed to that Worker will serve the new or updated static assets.</p>
<hr />
<h2 id="deploying-static-assets-with-wrangler">Deploying static assets with Wrangler</h2>
<p>If you prefer a CLI-based approach and your platform setup allows direct publishing, you can use Wrangler to deploy both your Worker code and static assets. Wrangler bundles and uploads static assets (from a specified directory) along with your Worker script, so you can manage everything in one place.</p>
<p>Create or update your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to specify where Wrangler should look for static files:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4216.md")
</div>
<ul>
<li><code>directory</code>: The local folder containing your static files (for example, <code>./public</code>).</li>
<li><code>binding</code>: The binding name used to reference these assets within your Worker code.</li>
</ul>
<h3 id="1-organize-your-files"><ol>
<li>Organize your files</li>
</ol></h3>
<p>Place your static files (HTML, CSS, images, etc.) in the specified directory (in this example, <code>./public</code>). Wrangler will detect and bundle these files when you publish your Worker.</p>
<p>If you need to reference these files in your Worker script to serve them dynamically, you can use the <code>ASSETS</code> binding like this:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return env.ASSETS.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<h3 id="2-deploy-the-user-worker-with-the-static-assets"><ol start="2">
<li>Deploy the User Worker with the static assets</li>
</ol></h3>
<p>Run Wrangler to publish both your Worker code and the static assets:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy --name &lt;USER_WORKER_NAME&gt; --dispatch-namespace &lt;NAMESPACE_NAME&gt;&#10;</code></pre>
<p>Wrangler will automatically detect your static files, bundle them, and upload them to Cloudflare along with your Worker code.</p>
