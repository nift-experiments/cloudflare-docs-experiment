<h1 id="cf-waf-content-scan-has-malicious-obj">cf.waf.content_scan.has_malicious_obj</h1>

**Data type:** Boolean

<p>Indicates whether the request contains at least one malicious content object.</p>

<p>Requires a Cloudflare Enterprise plan with <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a>.</p>

**Example usage:**

```txt
# Check if requests to a specific endpoint include any malicious content objects
cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq "/upload"
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, content scanning, malicious uploads, client, visitor

