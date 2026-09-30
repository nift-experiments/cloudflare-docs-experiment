<h1 id="cf-timings-edge-msec">cf.timings.edge_msec</h1>

**Data type:** Integer

<p>The time spent processing a request within the Cloudflare global network in milliseconds.</p>

<p>The value corresponds to the time interval between when the Cloudflare edge server accepted the HTTP request headers for processing and just before the HTTP response headers were available to be sent to the client.</p>
<p>The value does not include:</p>
<ul>
<li>The time spent forwarding the request to the origin server (refer to <a href="/ruleset-engine/rules-language/fields/reference/cf.timings.origin_ttfb_msec/"><code>cf.timings.origin_ttfb_msec</code></a>).</li>
<li>The network transfer time to the client.</li>
</ul>

**Example value:**

```txt
28
```

**Example usage:**

```txt
# Matches requests where Cloudflare's edge processing time was greater than 500 milliseconds
cf.timings.edge_msec > 500
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timing, edge, performance

