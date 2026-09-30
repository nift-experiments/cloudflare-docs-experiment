<h1 id="cf-waf-signature-request-confidence">cf.waf.signature.request.confidence</h1>

**Data type:** Array<String>

<p>An array of confidence values associated with attack signatures that matched the request.</p>

<p>Supported values are <code>high</code> and <code>low</code>.</p>
<p>Available to customers with <a href="/waf/detections/attack-signature-detection/">Attack Signature Detection</a> in Security Analytics and Custom Rules. Contact your Cloudflare account team to request Early Access.</p>

**Example value:**

```txt
["high"]
```

**Example usage:**

```txt
any(cf.waf.signature.request.confidence[*] eq "high")
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, waf, attack signature, confidence

