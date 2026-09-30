<h1 id="http-request-uri-args-names">http.request.uri.args.names</h1>

**Data type:** Array<String>

<p>The names of the arguments in the HTTP URI query string.</p>

<p>When a name repeats, the array contains multiple items in the order that they appear in the request.</p>
<p>The names are not pre-processed and retain the original case used in the request.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>

**Example value:**

```txt
["search"]
```

**Example usage:**

```txt
any(http.request.uri.args.names[*] == "search")
```

<h2 id="categories">Categories</h2>

- Request
- URI

**Keywords:** request, uri, url, arguments, query string, client, visitor

