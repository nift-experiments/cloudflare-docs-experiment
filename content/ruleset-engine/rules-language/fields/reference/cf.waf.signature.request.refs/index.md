<h1 id="cf-waf-signature-request-refs">cf.waf.signature.request.refs</h1>

**Data type:** Array<String>

<p>An array containing up to 10 Refs for attack signatures that matched the request.</p>

<p>Each Ref is the same value as the corresponding Cloudflare Managed Rules public Rule ID.</p>
<p>Available to customers with <a href="/waf/detections/attack-signature-detection/">Attack Signature Detection</a> in Security Analytics and Custom Rules. Contact your Cloudflare account team to request Early Access.</p>

**Example value:**

```txt
["d68f8101f6e14e25aefcaea69c530a29"]
```

**Example usage:**

```txt
any(cf.waf.signature.request.refs[*] eq "d68f8101f6e14e25aefcaea69c530a29")
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, waf, attack signature, ref, rule id

