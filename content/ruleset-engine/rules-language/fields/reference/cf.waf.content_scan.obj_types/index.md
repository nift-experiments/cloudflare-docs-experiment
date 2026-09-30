<h1 id="cf-waf-content-scan-obj-types">cf.waf.content_scan.obj_types</h1>

**Data type:** Array<String>

<p>An array of file types in the order the content objects were detected in the request.</p>

<p>If Cloudflare cannot determine the file type of a content object, the corresponding value in the <code>obj_types</code> array will be <code>application/octet-stream</code>.</p>
<p>Requires a Cloudflare Enterprise plan with <a href="/waf/detections/malicious-uploads/">malicious uploads detection</a>.</p>

**Example usage:**

```txt
# Check if requests to a specific endpoint contain content objects other than PDFs
any(cf.waf.content_scan.obj_types[*] != "application/pdf") and http.request.uri.path eq "/upload"
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, content scanning, malicious uploads, client, visitor

