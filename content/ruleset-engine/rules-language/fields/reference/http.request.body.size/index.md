<h1 id="http-request-body-size">http.request.body.size</h1>

**Data type:** Number

<p>The total size of the HTTP request body (in bytes).</p>

<p>This field may have a value larger than the one returned by <code>len(http.request.body.raw)</code>, since the <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.raw/"><code>http.request.body.raw</code></a> field only considers the request body up to a maximum size that varies according to your Cloudflare plan.</p>
<p>Requires a Cloudflare Enterprise plan.</p>

<h2 id="categories">Categories</h2>

- Request
- Body

**Keywords:** request, body, client, visitor

