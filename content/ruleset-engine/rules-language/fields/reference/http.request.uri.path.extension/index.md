<h1 id="http-request-uri-path-extension">http.request.uri.path.extension</h1>

**Data type:** String

<p>The lowercased file extension in the URI path without the dot (<code>.</code>) character.</p>

<p>This corresponds to the string after the last dot in the URI path, excluding the query string.</p>
<p>If the first character of the last path segment is a dot and the segment does not contain other dot characters, the field value will be an empty string (<code>&quot;&quot;</code>). Having a dot as the first character does not represent a file extension and is commonly used in UNIX-like systems to denote a hidden file or directory.</p>
<p>Example values:</p>
<ul>
<li>If the URI path is <code>/articles/index.html</code>, the field value will be <code>&quot;html&quot;</code>.</li>
<li>If the URI path is <code>/articles/index.</code>, the field value will be an empty string (<code>&quot;&quot;</code>).</li>
</ul>
<p>Example values:</p>
<table>
<thead>
<tr>
<th>URI path</th>
<th>Field value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/foo</code></td>
<td><code>&quot;&quot;</code></td>
</tr>
<tr>
<td><code>/foo.mp3</code></td>
<td><code>&quot;mp3&quot;</code></td>
</tr>
<tr>
<td><code>/.mp3</code></td>
<td><code>&quot;&quot;</code></td>
</tr>
<tr>
<td><code>/.foo.mp3</code></td>
<td><code>&quot;mp3&quot;</code></td>
</tr>
<tr>
<td><code>/foo.tar.bz2</code></td>
<td><code>&quot;bz2&quot;</code></td>
</tr>
<tr>
<td><code>/foo.</code></td>
<td><code>&quot;&quot;</code></td>
</tr>
<tr>
<td><code>/foo.MP3</code></td>
<td><code>&quot;mp3&quot;</code></td>
</tr>
</tbody>
</table>

<h2 id="categories">Categories</h2>

- Request
- URI

**Keywords:** request, uri, url, path, client, visitor

