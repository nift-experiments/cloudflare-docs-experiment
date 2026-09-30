<h1 id="http-request-timestamp-sec">http.request.timestamp.sec</h1>

**Data type:** Integer

<p>The timestamp when Cloudflare received the request, expressed as UNIX time in seconds.</p>

<p>The field value is 10 digits long.</p>
<p>When validating HMAC tokens in an expression, pass this field as the <code>currentTimestamp</code> argument to the <a href="/ruleset-engine/rules-language/functions/#hmac-validation"><code>is_timed_hmac_valid_v0()</code></a> validation function.</p>
<p>To obtain the timestamp milliseconds, use the <a href="/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/"><code>http.request.timestamp.msec</code></a> field.</p>

**Example value:**

```txt
1484063137
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timestamp, client, visitor

