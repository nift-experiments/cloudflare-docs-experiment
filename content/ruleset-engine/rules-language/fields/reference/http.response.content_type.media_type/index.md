<h1 id="http-response-content-type-media-type">http.response.content_type.media_type</h1>

**Data type:** String

<p>The lowercased content type (including subtype and suffix) without any extra parameters, based on the response's <code>Content-Type</code> header.</p>

<p>The field value will not include parameters such as <code>charset</code>.</p>
<p>Example values:</p>
<table>
<thead>
<tr>
<th>Content-Type header</th>
<th>Field value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>text/html</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td><code>text/html; charset=utf-8</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td><code>text/html+extra</code></td>
<td><code>&quot;text/html+extra&quot;</code></td>
</tr>
<tr>
<td><code>text/html+extra; charset=utf-8</code></td>
<td><code>&quot;text/html+extra&quot;</code></td>
</tr>
<tr>
<td><code>text/HTML</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td><code>text/html; charset=utf-8; other=value</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
</tbody>
</table>
<p><strong>Note</strong>: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.</p>

<h2 id="categories">Categories</h2>

- Response
- Headers

**Keywords:** response

