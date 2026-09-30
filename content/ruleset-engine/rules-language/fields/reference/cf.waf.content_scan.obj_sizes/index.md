<h1 id="cf-waf-content-scan-obj-sizes">cf.waf.content_scan.obj_sizes</h1>

**Data type:** Array<Integer>

<p>An array of file sizes in bytes, in the order the content objects were detected in the request.</p>

<p>Requires a Cloudflare Enterprise plan with <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a>.</p>

**Example usage:**

```txt
# Check if requests to a specific endpoint contain any content objects larger than 500 KB (512,000 bytes)
any(cf.waf.content_scan.obj_sizes[*] > 512000) and http.request.uri.path eq "/upload"
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, content scanning, malicious uploads, client, visitor

