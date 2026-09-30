<h1 id="raw-http-request-full-uri">raw.http.request.full_uri</h1>

**Data type:** String

<p>The raw full URI as received by the web server without any transformation.</p>

<p>The value will not include the <code>#fragment</code> part, which is not sent to web servers.</p>
<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.request.full_uri/"><code>http.request.full_uri</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>
<p><strong>Note</strong>: This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.</p>

<h2 id="categories">Categories</h2>

- Request
- URI
- Raw fields

**Keywords:** request, uri, url, raw, client, visitor

