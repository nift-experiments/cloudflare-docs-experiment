<h1 id="http-request-body-form-values">http.request.body.form.values</h1>

**Data type:** Array<String>

<p>The values of the form fields in an HTTP request.</p>

<p>Populated when the <code>Content-Type</code> header is <code>application/x-www-form-urlencoded</code>.</p>
<p>Values are not pre-processed and retain the original case used in the request. They are listed in the same order as in the request.</p>
<p>Duplicated values are listed multiple times.</p>
<p>The return value may be truncated if <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated"><code>http.request.body.truncated</code></a> is <code>true</code>.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p>Requires a Cloudflare Enterprise plan.</p>

**Example value:**

```txt
["admin"]
```

**Example usage:**

```txt
any(http.request.body.form.values[*] == "admin")
```

<aside class="nb-aside nb-aside-caution"><p>All <code>http.request.body.*</code> fields (except <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.size/"><code>http.request.body.size</code></a>) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default. For users in the Free plan, the limit is 1 MB.</p>
<p>You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, body fields contain a truncated value and <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><code>http.request.body.truncated</code></a> is set to <code>true</code>. The <code>http.request.body.size</code> field contains the full request size without truncation.</p>
<p>The maximum body size applies only to HTTP body field values; the origin server still receives the complete request body.</p></aside>

<h2 id="categories">Categories</h2>

- Request
- Body

**Keywords:** request, body, form, client, visitor

