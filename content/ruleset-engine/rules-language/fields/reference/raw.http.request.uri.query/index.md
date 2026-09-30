<h1 id="raw-http-request-uri-query">raw.http.request.uri.query</h1>

**Data type:** String

<p>The entire query string without the <code>?</code> delimiter and without any transformation.</p>

<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.query/"><code>http.request.uri.query</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>
<p><strong>Note</strong>: This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.</p>

<h2 id="categories">Categories</h2>

- Request
- URI
- Raw fields

**Keywords:** request, uri, url, query, query string, raw, client, visitor

