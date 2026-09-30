<p><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS">Cross-Origin Resource Sharing (CORS)</a> is a standardized method that prevents domain X from accessing the resources of domain Y. It does so by using special headers in HTTP responses from domain Y, that allow your browser to verify that domain Y permits domain X to access these resources.</p>
<p>While CORS can help protect your data from malicious websites, CORS is also used to interact with objects in your bucket and configure policies on your bucket.</p>
<p>CORS is used when you interact with a bucket from a web browser, and you have two options:</p>
<p><strong><a href="#use-cors-with-a-public-bucket">Set a bucket to public:</a></strong> This option makes your bucket accessible on the Internet as read-only, which means anyone can request and load objects from your bucket in their browser or anywhere else. This option is ideal if your bucket contains images used in a public blog.</p>
<p><strong><a href="#use-cors-with-a-presigned-url">Presigned URLs:</a></strong> Allows anyone with access to the unique URL to perform specific actions on your bucket.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you configure CORS, you must have:</p>
<ul>
<li>An R2 bucket with at least one object. If you need to create a bucket, refer to <a href="/r2/buckets/public-buckets/">Create a public bucket</a>.</li>
<li>A domain you can use to access the object. This can also be a <code>localhost</code>.</li>
<li>(Optional) Access keys. An access key is only required when creating a presigned URL.</li>
</ul>
<h2 id="use-cors-with-a-public-bucket">Use CORS with a public bucket</h2>
<p><a href="/r2/buckets/public-buckets/">To use CORS with a public bucket</a>, ensure your bucket is set to allow public access.</p>
<p>Next, <a href="#add-cors-policies-from-the-dashboard">add a CORS policy</a> to your bucket to allow the file to be shared.</p>
<h2 id="use-cors-with-a-presigned-url">Use CORS with a presigned URL</h2>
<p><a href="/r2/api/s3/presigned-urls/">Presigned URLs</a> allow temporary access to perform specific actions on your bucket without exposing your credentials. While presigned URLs handle authentication, you still need to configure CORS when making requests from a browser.</p>
<p>When a browser makes a request to a presigned URL on a different origin, the browser enforces CORS. Without a CORS policy, browser-based uploads and downloads using presigned URLs will fail, even though the presigned URL itself is valid.</p>
<p>Expired presigned URLs return a <code>403</code> <code>ExpiredRequest</code> response. R2 does not include CORS response headers on expired presigned URL responses, so browser JavaScript cannot read the error body. Refresh presigned URLs before they expire, or route requests through your application server if the browser needs to handle expiration errors directly.</p>
<p>To enable browser-based access with presigned URLs:</p>
<ol>
<li>
<p><a href="#add-cors-policies-from-the-dashboard">Add a CORS policy</a> to your bucket that allows requests from your application's origin.</p>
</li>
<li>
<p>Set <code>AllowedMethods</code> to match the operations your presigned URLs perform, use <code>GET</code>, <code>PUT</code>, <code>HEAD</code>, and/or <code>DELETE</code>.</p>
</li>
<li>
<p>Set <code>AllowedHeaders</code> to include any headers the client will send when using the presigned URL, such as headers for content type, checksums, caching, or custom metadata.</p>
</li>
<li>
<p>(Optional) Set <code>ExposeHeaders</code> to allow your JavaScript to read response headers like <code>ETag</code>, which contains the object's hash and is useful for verifying uploads.</p>
</li>
<li>
<p>(Optional) Set <code>MaxAgeSeconds</code> to cache the preflight response and reduce the number of preflight requests the browser makes.</p>
</li>
</ol>
<p>The following example allows browser-based uploads from <code>https://example.com</code> with a <code>Content-Type</code> header:</p>
<pre><code class="language-json">[&#10;  {&#10;    &quot;AllowedOrigins&quot;: [&quot;https://example.com&quot;],&#10;    &quot;AllowedMethods&quot;: [&quot;PUT&quot;],&#10;    &quot;AllowedHeaders&quot;: [&quot;Content-Type&quot;],&#10;    &quot;ExposeHeaders&quot;: [&quot;ETag&quot;],&#10;    &quot;MaxAgeSeconds&quot;: 3600&#10;  }&#10;]&#10;</code></pre>
<h2 id="use-cors-with-a-custom-domain">Use CORS with a custom domain</h2>
<p><a href="/r2/buckets/public-buckets/#custom-domains">Custom domains</a> connected to an R2 bucket with a CORS policy automatically return CORS response headers for <a href="https://fetch.spec.whatwg.org/#http-cors-protocol">cross-origin requests</a>.</p>
<p>Cross-origin requests must include a valid <code>Origin</code> request header, for example, <code>Origin: https://example.com</code>. If you are testing directly or using a command-line tool such as <code>curl</code>, you will not see CORS <code>Access-Control-*</code> response headers unless the <code>Origin</code> request header is included in the request.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="caching-and-cors-headers">Caching and CORS headers</h3>
@markup("md", "content/.markup/bodies/11496.md")
</aside>
<h2 id="add-cors-policies-from-the-dashboard">Add CORS policies from the dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Locate and select your bucket from the list.
3. Select **Settings**.
4. Under **CORS Policy**, select **Add CORS policy**.
5. From the **JSON** tab, manually enter or copy and paste your policy into the text box.
6. When you are done, select **Save**.
<p>Your policy displays on the <strong>Settings</strong> page for your bucket.</p>
<h2 id="add-cors-policies-via-wrangler-cli">Add CORS policies via Wrangler CLI</h2>
<p>You can configure CORS rules using the <a href="/r2/reference/wrangler-commands/">Wrangler CLI</a>.</p>
<ol>
<li>Create a JSON file with your CORS configuration:</li>
</ol>
<pre><code class="language-json">{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;allowed&quot;: {&#10;        &quot;origins&quot;: [&quot;https://example.com&quot;],&#10;        &quot;methods&quot;: [&quot;GET&quot;]&#10;      }&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<ol start="2">
<li>Apply the CORS policy to your bucket:</li>
</ol>
<pre><code class="language-sh">npx wrangler r2 bucket cors set &lt;BUCKET_NAME&gt; --file cors.json&#10;</code></pre>
<ol start="3">
<li>Verify the CORS policy was applied:</li>
</ol>
<pre><code class="language-sh">npx wrangler r2 bucket cors list &lt;BUCKET_NAME&gt;&#10;</code></pre>
<h2 id="response-headers">Response headers</h2>
<p>The following fields in an R2 CORS policy map to HTTP response headers. These response headers are only returned when the incoming HTTP request is a valid CORS request.</p>
<table>
<thead>
<tr>
<th>Field Name</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AllowedOrigins</code></td>
<td>Specifies the value for the <code>Access-Control-Allow-Origin</code> header R2 sets when requesting objects in a bucket from a browser.</td>
<td>If a website at <code>www.test.com</code> needs to access resources (e.g. fonts, scripts) on a <a href="/r2/buckets/public-buckets/#custom-domains">custom domain</a> of <code>static.example.com</code>, you would set <code>https://www.test.com</code> as an <code>AllowedOrigin</code>.</td>
</tr>
<tr>
<td><code>AllowedMethods</code></td>
<td>Specifies the value for the <code>Access-Control-Allow-Methods</code> header R2 sets when requesting objects in a bucket from a browser.</td>
<td><code>GET</code>, <code>POST</code>, <code>PUT</code></td>
</tr>
<tr>
<td><code>AllowedHeaders</code></td>
<td>Specifies the value for the <code>Access-Control-Allow-Headers</code> header R2 sets when requesting objects in this bucket from a browser.Cross-origin requests that include custom headers (e.g. <code>x-user-id</code>) should specify these headers as <code>AllowedHeaders</code>.</td>
<td><code>x-requested-by</code>, <code>User-Agent</code></td>
</tr>
<tr>
<td><code>ExposeHeaders</code></td>
<td>Specifies the headers that can be exposed back, and accessed by, the JavaScript making the cross-origin request. If you need to access headers beyond the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers#examples">safelisted response headers</a>, such as <code>Content-Encoding</code> or <code>cf-cache-status</code>, you must specify it here.</td>
<td><code>Content-Encoding</code>, <code>cf-cache-status</code>, <code>Date</code></td>
</tr>
<tr>
<td><code>MaxAgeSeconds</code></td>
<td>Specifies the amount of time (in seconds) browsers are allowed to cache CORS preflight responses. Browsers may limit this to 2 hours or less, even if the maximum value (86400) is specified.</td>
<td><code>3600</code></td>
</tr>
</tbody>
</table>
<h2 id="example">Example</h2>
<p>This example shows a CORS policy added for a bucket that contains the <code>Roboto-Light.ttf</code> object, which is a font file.</p>
<p>The <code>AllowedOrigins</code> specify the web server being used, and <code>localhost:3000</code> is the hostname where the web server is running. The <code>AllowedMethods</code> specify that only <code>GET</code> requests are allowed and can read objects in your bucket.</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;AllowedOrigins&quot;: [&quot;http://localhost:3000&quot;],&#10;		&quot;AllowedMethods&quot;: [&quot;GET&quot;]&#10;	}&#10;]&#10;</code></pre>
<p>In general, a good strategy for making sure you have set the correct CORS rules is to look at the network request that is being blocked by your browser.</p>
<ul>
<li>Make sure the rule's <code>AllowedOrigins</code> includes the origin where the request is being made from. (like <code>http://localhost:3000</code> or <code>https://yourdomain.com</code>)</li>
<li>Make sure the rule's <code>AllowedMethods</code> includes the blocked request's method.</li>
<li>Make sure the rule's <code>AllowedHeaders</code> includes the blocked request's headers.</li>
</ul>
<p>Also note that CORS rule propagation can, in rare cases, take up to 30 seconds.</p>
<h2 id="common-issues">Common Issues</h2>
<ul>
<li>Only a cross-origin request will include CORS response headers.
<ul>
<li>A cross-origin request is identified by the presence of an <code>Origin</code> HTTP request header, with the value of the <code>Origin</code> representing a valid, allowed origin as defined by the <code>AllowedOrigins</code> field of your CORS policy.</li>
<li>A request without an <code>Origin</code> HTTP request header will <em>not</em> return any CORS response headers. Origin values must match exactly.</li>
</ul>
</li>
<li>The value(s) for <code>AllowedOrigins</code> in your CORS policy must be a valid <a href="https://fetch.spec.whatwg.org/#origin-header">HTTP Origin header value</a>. A valid <code>Origin</code> header does <em>not</em> include a path component and must only be comprised of a <code>scheme://host[:port]</code> (where port is optional).
<ul>
<li>Valid <code>AllowedOrigins</code> value: <code>https://static.example.com</code> - includes the scheme and host. A port is optional and implied by the scheme.</li>
<li>Invalid <code>AllowedOrigins</code> value: <code>https://static.example.com/</code> or <code>https://static.example.com/fonts/Calibri.woff2</code> - incorrectly includes the path component.</li>
</ul>
</li>
<li>If you need to access specific header values via JavaScript on the origin page, such as when using a video player, ensure you set <code>Access-Control-Expose-Headers</code> correctly and include the headers your JavaScript needs access to, such as <code>Content-Length</code>.</li>
</ul>
