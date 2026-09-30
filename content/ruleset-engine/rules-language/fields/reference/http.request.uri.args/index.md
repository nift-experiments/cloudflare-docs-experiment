<h1 id="http-request-uri-args">http.request.uri.args</h1>

**Data type:** Map<Array<String>>

<p>The HTTP URI arguments associated with a request represented as a Map (associative array).</p>

<p>When an argument repeats, the array contains multiple items in the order they appear in the request.</p>
<p>The values are not pre-processed and retain the original case used in the request.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>

**Example value:**

```txt
{"search": ["red+apples"]}
```

**Example usage:**

```txt
any(http.request.uri.args["search"][*] == "red+apples")
```

<h2 id="categories">Categories</h2>

- Request
- URI

**Keywords:** request, uri, url, arguments, query string, client, visitor

