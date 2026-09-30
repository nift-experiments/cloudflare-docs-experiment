<h1 id="cf-waf-content-scan-num-malicious-obj">cf.waf.content_scan.num_malicious_obj</h1>

**Data type:** Integer

<p>The number of malicious content objects detected in the request (zero or greater).</p>

<p>Requires a Cloudflare Enterprise plan with <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a>.</p>

**Example usage:**

```txt
# Check if requests to a specific endpoint contain more than two malicious content objects
cf.waf.content_scan.num_malicious_obj > 2 and http.request.uri.path eq "/upload"
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, content scanning, malicious uploads, client, visitor

