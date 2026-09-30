<p>Some possible combinations of origin web server settings and Cloudflare <a href="/cache/how-to/cache-rules/">Cache Rules</a> include:</p>
<h2 id="create-a-directory-for-static-content-at-your-origin-web-server">Create a directory for static content at your origin web server</h2>
<p>For example, create a <code>/static/</code> subdirectory at your origin web server and a Cache Everything Cache Rule matching the following expression:</p>
<ul>
<li>Using the Expression Builder: <code>Hostname contains &quot;example.com&quot; AND URI Path starts with &quot;/static&quot;</code></li>
<li>Using the Expression Editor: <code>(http.host contains &quot;example.com&quot; and starts_with(http.request.uri.path, &quot;/static&quot;))</code></li>
</ul>
<h2 id="append-a-unique-file-extension-to-static-pages">Append a unique file extension to static pages</h2>
<p>For example, create a <code>.shtml</code> file extension for resources at your origin web server and a Cache Everything Cache Rule matching the following expression:</p>
<ul>
<li>Using the Expression Builder: <code>Hostname contains &quot;example.com&quot; AND URI Path ends with &quot;.shtml&quot;</code></li>
<li>Using the Expression Editor: <code>(http.host contains &quot;example.com&quot; and ends_with(http.request.uri.path, &quot;.shtml&quot;))</code></li>
</ul>
<h2 id="add-a-query-string-to-a-resource-s-url-to-mark-the-content-as-static">Add a query string to a resource’s URL to mark the content as static</h2>
<p>For example, add a <code>static=true</code> query string for resources at your origin web server and a Cache Everything Cache Rule matching the following expression:</p>
<ul>
<li>Using the Expression Builder: <code>Hostname contains &quot;example.com&quot; AND URI Query String contains &quot;static=true&quot;</code></li>
<li>Using the Expression Editor: <code>(http.host contains &quot;example.com&quot; and http.request.uri.query contains &quot;static=true&quot;)</code></li>
</ul>
<p>Resources that match a Cache Everything Cache Rule are still not cached if the origin web server sends a Cache-Control header of <code>max-age=0</code>, <code>private</code>, <code>no-cache</code>, or an <code>Expires</code> header with an already expired date. Include the <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL</a> setting within the Cache Everything Cache Rule to additionally override the <code>Cache-Control</code> headers from the origin web server.</p>
