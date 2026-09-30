<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16100.md")
</aside>
<p>Our API empowers users to upload and include static assets as part of a Worker. These static assets can be served for free, and additionally, users can also fetch assets through an optional <a href="/workers/static-assets/binding/">assets binding</a> to power more advanced applications. This guide will describe the process for attaching assets to your Worker directly with the API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workers-vs-platforms"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16103.md")
</div></div>
<p>The asset upload flow can be distilled into three distinct phases:</p>
<ol>
<li>Registration of a manifest</li>
<li>Upload of the assets</li>
<li>Deployment of the Worker</li>
</ol>
<h2 id="upload-manifest">Upload manifest</h2>
<p>The asset manifest is a ledger which keeps track of files we want to use in our Worker. This manifest is used to track assets associated with each Worker version, and eliminate the need to upload unchanged files prior to a new upload.</p>
<p>The <a href="/api/resources/workers/subresources/scripts/subresources/assets/subresources/upload/methods/create/">manifest upload request</a> describes each file which we intend to upload. Each file is its own key representing the file path and name, and is an object which contains metadata about the file.</p>
<p><code>hash</code> represents a 32 hexadecimal character hash of the file, while <code>size</code> is the size (in bytes) of the file.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workers-vs-platforms"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16106.md")
</div></div>
<p>The resulting response will contain a JWT, which provides authentication during file upload. The JWT is valid for one hour.</p>
<p>In addition to the JWT, the response instructs users how to optimally batch upload their files. These instructions are encoded in the <code>buckets</code> field. Each array in <code>buckets</code> contains a list of file hashes which should be uploaded together. Unmodified files will not be returned in the <code>buckets</code> field (as they do not need to be re-uploaded) if they have recently been uploaded in previous versions of your Worker.</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;jwt&quot;: &quot;&lt;UPLOAD_TOKEN&gt;&quot;,&#10;		&quot;buckets&quot;: [&#10;			[&quot;08f1dfda4574284ab3c21666d1&quot;, &quot;4f1c1af44620d531446ceef93f&quot;],&#10;			[&quot;54995e302614e0523757a04ec1&quot;]&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: null,&#10;	&quot;messages&quot;: null&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16099.md")
</aside>
<h3 id="limitations">Limitations</h3>
<ul>
<li>Limits differ based on account plan. Refer to <a href="/workers/platform/limits/#account-plan-limits">Account Plan Limits</a> for more information on limitations of static assets.</li>
</ul>
<h2 id="upload-static-assets">Upload Static Assets</h2>
<p>The <a href="/api/resources/workers/subresources/assets/subresources/upload/methods/create/">file upload API</a> requires files be uploaded using <code>multipart/form-data</code>. The contents of each file must be base64 encoded, and the <code>base64</code> query parameter in the URL must be set to <code>true</code>.</p>
<p>The provided <code>Content-Type</code> header of each file part will be attached when eventually serving the file. If you wish to avoid sending a <code>Content-Type</code> header in your deployment, <code>application/null</code> may be sent at upload time.</p>
<p>The <code>Authorization</code> header must be provided as a bearer token, using the JWT (upload token) from the aforementioned manifest upload call.</p>
<p>Once every file in the manifest has been uploaded, a status code of 201 will be returned, with the <code>jwt</code> field present. This JWT is a final &quot;completion&quot; token which can be used to create a deployment of a Worker with this set of assets. This completion token is valid for 1 hour.</p>
<h2 id="create-deploy-new-version">Create/Deploy New Version</h2>
<p><a href="/api/resources/workers/subresources/scripts/methods/update/">Script</a>, <a href="/api/resources/workers/subresources/scripts/subresources/versions/methods/create/">Version</a>, and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">Workers for Platform script</a> upload endpoints require specifying a metadata part in the form data. Here, we can provide the completion token from the previous (upload assets) step.</p>
<pre><code class="language-bash">{&#10;  &quot;main_module&quot;: &quot;main.js&quot;,&#10;  &quot;assets&quot;: {&#10;    &quot;jwt&quot;: &quot;&lt;completion_token&gt;&quot;&#10;  },&#10;  &quot;compatibility_date&quot;: &quot;2021-09-14&quot;&#10;}&#10;</code></pre>
<p>If this is a Worker which already has assets, and you wish to just re-use the existing set of assets, we do not have to specify the completion token again. Instead, we can pass the boolean <code>keep_assets</code> option.</p>
<pre><code class="language-bash">{&#10;  &quot;main_module&quot;: &quot;main.js&quot;,&#10;  &quot;keep_assets&quot;: true,&#10;  &quot;compatibility_date&quot;: &quot;2021-09-14&quot;&#10;}&#10;</code></pre>
<p>Asset <a href="/workers/wrangler/configuration/#assets">routing configuration</a> can be provided in the <code>assets</code> object, such as <code>html_handling</code> and <code>not_found_handling</code>.</p>
<pre><code class="language-bash">{&#10;  &quot;main_module&quot;: &quot;main.js&quot;,&#10;  &quot;assets&quot;: {&#10;    &quot;jwt&quot;: &quot;&lt;completion_token&gt;&quot;,&#10;    &quot;config&quot; {&#10;      &quot;html_handling&quot;: &quot;auto-trailing-slash&quot;&#10;    }&#10;  },&#10;  &quot;compatibility_date&quot;: &quot;2021-09-14&quot;&#10;}&#10;</code></pre>
<p>Optionally, an assets binding can be provided if you wish to fetch and serve assets from within your Worker code.</p>
<pre><code class="language-bash">{&#10;  &quot;main_module&quot;: &quot;main.js&quot;,&#10;  &quot;assets&quot;: {&#10;    ...&#10;  },&#10;  &quot;bindings&quot;: [&#10;    ...&#10;    {&#10;      &quot;name&quot;: &quot;ASSETS&quot;,&#10;      &quot;type&quot;: &quot;assets&quot;&#10;    }&#10;    ...&#10;  ]&#10;  &quot;compatibility_date&quot;: &quot;2021-09-14&quot;&#10;}&#10;</code></pre>
<h2 id="programmatic-example">Programmatic Example</h2>
<p>This example is from <a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-with-assets-upload.ts">cloudflare-typescript</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16107.md")
</div>
