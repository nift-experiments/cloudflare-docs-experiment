<h1 id="http-response-headers">http.response.headers</h1>

**Data type:** Map<Array<String>>

<p>The HTTP response headers represented as a Map (or associative array).</p>

<p>When there are repeating headers, the array includes them in the order they appear in the response. The keys convert to lowercase.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p><strong>Note</strong>: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.</p>

**Example value:**

```txt
{"server": ["nginx"]}
```

**Example usage:**

```txt
any(http.response.headers["server"][*] == "nginx")
```

<h2 id="categories">Categories</h2>

- Response
- Headers

**Keywords:** response

