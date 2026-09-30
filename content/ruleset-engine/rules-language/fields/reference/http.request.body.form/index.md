<h1 id="http-request-body-form">http.request.body.form</h1>

**Data type:** Map<Array<String>>

<p>The HTTP request body of a form represented as a Map (or associative array).</p>

<p>Populated when the <code>Content-Type</code> header is <code>application/x-www-form-urlencoded</code>.</p>
<p>The values are not pre-processed and retain the original case used in the request.</p>
<p>When a field repeats, then the array contains multiple items in the order they are in the request.</p>
<p>The return value may be truncated if <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated"><code>http.request.body.truncated</code></a> is <code>true</code>.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p>Requires a Cloudflare Enterprise plan.</p>

**Example value:**

```txt
{username": ["admin"]}
```

**Example usage:**

```txt
any(http.request.body.form["username"][*] == "admin")
```

<aside class="nb-aside nb-aside-caution"><p>All <code>http.request.body.*</code> fields (except <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.size/"><code>http.request.body.size</code></a>) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default. For users in the Free plan, the limit is 1 MB.</p>
<p>You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, body fields contain a truncated value and <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><code>http.request.body.truncated</code></a> is set to <code>true</code>. The <code>http.request.body.size</code> field contains the full request size without truncation.</p>
<p>The maximum body size applies only to HTTP body field values; the origin server still receives the complete request body.</p></aside>

<h2 id="categories">Categories</h2>

- Request
- Body

**Keywords:** request, body, form, client, visitor

