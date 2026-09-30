<h1 id="http-request-uri-args-values">http.request.uri.args.values</h1>

**Data type:** Array<String>

<p>The values of arguments in the HTTP URI query string.</p>

<p>The values are not pre-processed and retain the original case used in the request. They are in the same order as in the request.</p>
<p>Duplicated values are listed multiple times.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>

**Example value:**

```txt
["red+apples"]
```

**Example usage:**

```txt
any(http.request.uri.args.values[*] == "red+apples")
```

<h2 id="categories">Categories</h2>

- Request
- URI

**Keywords:** request, uri, url, arguments, query string, client, visitor

