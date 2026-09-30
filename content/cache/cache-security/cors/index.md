<p>A cross-origin request occurs when a webpage on one origin (for example, <code>a.example.com</code>) requests a resource from a different origin (for example, <code>b.secondexample.com</code>). Cross-Origin Resource Sharing (CORS) is a mechanism that uses HTTP headers to let the server at <code>b.secondexample.com</code> indicate whether <code>a.example.com</code> is allowed to access its resources. Browsers enforce these headers and block access to responses that are not permitted.</p>
<p>Cloudflare supports CORS by:</p>
<ul>
<li>Identifying cached assets based on the <code>Host</code> Header, <code>Origin</code> Header, URL path, and query. This allows different resources to use the same <code>Host</code> header but different <code>Origin</code> headers.</li>
<li>Passing <code>Access-Control-Allow-Origin</code> headers from the origin server to the browser.</li>
</ul>
<p>The <code>Access-Control-Allow-Origin</code> header lets a server specify rules for sharing its resources with external origins. A server may respond with different <code>Access-Control-Allow-Origin</code> values depending on the <code>Origin</code> header in the request. These headers are often present on <a href="/cache/concepts/default-cache-behavior/">cacheable content</a>.</p>
<h2 id="add-or-change-cors-headers-at-the-origin-server">Add or change CORS headers at the origin server</h2>
<p>If you add or change CORS configuration at your origin web server, purging the Cloudflare cache by URL does not update the CORS headers. Force Cloudflare to retrieve the new CORS headers via one of the following options:</p>
<ul>
<li>Change the filename or URL to bypass cache to instruct Cloudflare to retrieve the latest CORS headers.</li>
<li>Use the <a href="/api/resources/cache/methods/purge/#purge-cached-content-by-url">single-file purge API</a> to specify the appropriate CORS headers along with the purge request.</li>
<li>Update the resource’s last-modified time at your origin web server. Then, complete a <a href="/cache/how-to/purge-cache/purge-everything/">full purge</a> to retrieve the latest version of your assets including updated CORS headers.</li>
</ul>
<h2 id="add-or-change-cors-headers-on-cloudflare">Add or change CORS headers on Cloudflare</h2>
<p>You can use one of following methods to set CORS headers using Cloudflare products:</p>
<ul>
<li>Use a <a href="/workers/">Worker</a>: Refer to <a href="/workers/examples/cors-header-proxy/">CORS header proxy</a> for an example.</li>
<li>Configure a <a href="/rules/snippets/">Snippet</a>: Refer to <a href="/rules/snippets/examples/define-cors-headers/">Define CORS headers</a> for an example.</li>
<li>Use <a href="/rules/transform/">Transform Rules</a>: Refer to <a href="/rules/transform/examples/add-cors-header/">Add a wildcard CORS response header</a> for an example.</li>
</ul>
