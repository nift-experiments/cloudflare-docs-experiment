<h1 id="http-host">http.host</h1>

**Data type:** String

<p>The hostname used in the full request URI.</p>

<p>The <code>http.host</code> field contains the <code>Host</code> header from the original client request.</p>
<p>If you have configured <a href="/rules/origin-rules/">Origin Rules</a> that change the hostname, this change is not reflected in the <code>http.host</code> value seen by other rule phases (such as custom rules, cache rules, or transform rules) or <a href="/workers/">Cloudflare Workers</a>. All rule phases and Workers evaluate against the original, unmodified host.</p>

**Example value:**

```txt
"www.example.org"
```

<h2 id="categories">Categories</h2>

- Request
- URI

**Keywords:** request, uri, url, domain, client, visitor

