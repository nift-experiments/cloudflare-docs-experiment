<h1 id="cf-response-1xxx-code">cf.response.1xxx_code</h1>

**Data type:** Integer

<p>Contains the specific code for 1XXX Cloudflare errors.</p>

<p>Use this field to differentiate between 1XXX errors associated with the same HTTP status code. The default value is <code>0</code>.</p>
<p>For a list of 1XXX errors, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Troubleshooting Cloudflare 1XXX errors</a>.</p>
<p><strong>Note</strong>: This field is only available in <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> and <a href="/rules/custom-errors/">Custom Errors</a>.</p>

**Example value:**

```txt
1020
```

<h2 id="categories">Categories</h2>

- Response

**Keywords:** response, cloudflare

