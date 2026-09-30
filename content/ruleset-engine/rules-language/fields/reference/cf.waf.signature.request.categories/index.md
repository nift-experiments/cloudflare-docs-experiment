<h1 id="cf-waf-signature-request-categories">cf.waf.signature.request.categories</h1>

**Data type:** Array<String>

<p>An array of categories associated with attack signatures that matched the request.</p>

<p>Available to customers with <a href="/waf/detections/attack-signature-detection/">Attack Signature Detection</a> in Security Analytics and Custom Rules.</p>
<p>Contact your Cloudflare account team to request Early Access.</p>

**Example value:**

```txt
["sqli", "cve-2025-55182"]
```

**Example usage:**

```txt
any(cf.waf.signature.request.categories[*] eq "sqli")
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, waf, attack signature, category

