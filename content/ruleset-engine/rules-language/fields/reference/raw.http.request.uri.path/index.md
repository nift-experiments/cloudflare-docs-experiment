<h1 id="raw-http-request-uri-path">raw.http.request.uri.path</h1>

**Data type:** String

<p>The raw URI path of the request without any transformation.</p>

<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.path/"><code>http.request.uri.path</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>
<p><strong>Note</strong>: This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.</p>

<h2 id="categories">Categories</h2>

- Request
- URI
- Raw fields

**Keywords:** request, uri, url, path, raw, client, visitor

