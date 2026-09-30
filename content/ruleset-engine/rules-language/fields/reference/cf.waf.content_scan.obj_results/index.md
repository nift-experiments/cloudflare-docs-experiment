<h1 id="cf-waf-content-scan-obj-results">cf.waf.content_scan.obj_results</h1>

**Data type:** Array<String>

<p>An array of scan results in the order the content objects were detected in the request.</p>

<p>The possible values are: <code>clean</code>, <code>suspicious</code>, <code>infected</code>, and <code>not scanned</code>.</p>
<p>Requires a Cloudflare Enterprise plan with <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a>.</p>

**Example usage:**

```txt
# Check if requests to a specific endpoint contain any suspicious or infected content objects
any(cf.waf.content_scan.obj_results[*] in {"suspicious" "infected"}) and http.request.uri.path eq "/upload"
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, content scanning, malicious uploads, client, visitor

