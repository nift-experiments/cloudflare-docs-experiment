<h1 id="http-request-accepted-languages">http.request.accepted_languages</h1>

**Data type:** Array<String>

<p>List of language tags provided in the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Language"><code>Accept-Language</code></a> HTTP request header.</p>

<p>Language tags are sorted by weight (<code>;q=&lt;weight&gt;</code>, with a default weight of <code>1</code>) in descending order.</p>
<p>If the HTTP header is not present in the request or is empty, <code>http.request.accepted_languages[0]</code> will return a &quot;<a href="/ruleset-engine/rules-language/values/#notes">missing value</a>&quot;, which the <a href="/ruleset-engine/rules-language/functions/#concat"><code>concat()</code></a> function will handle as an empty string.</p>
<p>If the HTTP header includes the language tag <code>*</code> it will not be stored in the array.</p>
<p><strong>Note</strong>: This field is only available in <a href="/rules/transform/">Transform Rules</a>.</p>

**Example usage:**

```txt
# Example 1: Request with header "Accept-Language: fr-CH, fr;q=0.8, en;q=0.9, de;q=0.7, *;q=0.5".
# In this case:
http.request.accepted_languages[0] ==> "fr-CH"
http.request.accepted_languages    ==> ["fr-CH", "en", "fr", "de"]

# Example 2: Request without an `Accept-Language` HTTP header and a URI of "https://www.example.com/my-path".
# In this case:
concat("/", http.request.accepted_languages[0], http.request.uri.path) ==> "//my-path"
```

<h2 id="categories">Categories</h2>

- Request
- Headers

**Keywords:** request, client, visitor

