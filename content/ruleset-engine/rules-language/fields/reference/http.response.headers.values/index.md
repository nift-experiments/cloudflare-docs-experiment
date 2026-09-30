<h1 id="http-response-headers-values">http.response.headers.values</h1>

**Data type:** Array<String>

<p>The values of the headers in the HTTP response.</p>

<p>The values are not pre-processed and retain the original case used in the response.</p>
<p>The order of header values is not guaranteed but will match <a href="/ruleset-engine/rules-language/fields/reference/http.response.headers.names/"><code>http.response.headers.names</code></a>.</p>
<p>Duplicate headers are listed multiple times.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p><strong>Note</strong>: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.</p>

**Example value:**

```txt
Example 1: ["application/json"]
Example 2: ["This header value is longer than 10 bytes"]
```

**Example usage:**

```txt
# Example 1: Check for specific header value.
any(http.response.headers.values[*] == "application/json")

# Example 2: Match requests according to the specified operator and the length/size entered for the header value.
any(len(http.response.headers.values[*])[*] gt 10)
```

<h2 id="categories">Categories</h2>

- Response
- Headers

**Keywords:** response

