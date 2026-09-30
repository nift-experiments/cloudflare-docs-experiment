<h1 id="http-request-body-truncated">http.request.body.truncated</h1>

**Data type:** Boolean

<p>Indicates whether the HTTP request body is truncated.</p>

<p>When <code>true</code>, <code>http.request.body.*</code> fields may not contain all of the HTTP request body.</p>
<p>Requires a Cloudflare Enterprise plan.</p>

<aside class="nb-aside nb-aside-caution"><p>All <code>http.request.body.*</code> fields (except <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.size/"><code>http.request.body.size</code></a>) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default. For users in the Free plan, the limit is 1 MB.</p>
<p>You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, body fields contain a truncated value and <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><code>http.request.body.truncated</code></a> is set to <code>true</code>. The <code>http.request.body.size</code> field contains the full request size without truncation.</p>
<p>The maximum body size applies only to HTTP body field values; the origin server still receives the complete request body.</p></aside>

<h2 id="categories">Categories</h2>

- Request
- Body

**Keywords:** request, body, client, visitor

