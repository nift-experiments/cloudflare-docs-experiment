<p>You can attach custom metadata to web pages using HTML <code>&lt;meta&gt;</code> tags. AI Search extracts metadata from the <code>&lt;head&gt;</code> section of each crawled page.</p>
<p>Before custom metadata can be extracted, you must <a href="/ai-search/configuration/indexing/metadata/#define-a-schema">define a schema</a> in your AI Search configuration.</p>
<h2 id="add-metadata-to-web-pages">Add metadata to web pages</h2>
<p>Add <code>&lt;meta&gt;</code> tags using either the <code>name</code> or <code>property</code> attribute:</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;meta name=&quot;title&quot; content=&quot;Getting Started Guide&quot; /&gt;&#10;		&lt;meta name=&quot;description&quot; content=&quot;Learn how to set up the application&quot; /&gt;&#10;		&lt;meta property=&quot;og:title&quot; content=&quot;Getting Started Guide&quot; /&gt;&#10;		&lt;meta property=&quot;og:image&quot; content=&quot;https://example.com/og-image.png&quot; /&gt;&#10;		&lt;meta name=&quot;category&quot; content=&quot;documentation&quot; /&gt;&#10;		&lt;meta name=&quot;version&quot; content=&quot;2.5&quot; /&gt;&#10;		&lt;meta name=&quot;is_public&quot; content=&quot;true&quot; /&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;!-- Page content --&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="recognized-fields">Recognized fields</h2>
<p>For the following fields, AI Search knows which meta tags to extract from. You must still define these in your schema to enable extraction.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Source</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>title</code></td>
<td><code>&lt;meta name=&quot;title&quot;&gt;</code> or <code>&lt;meta property=&quot;og:title&quot;&gt;</code></td>
</tr>
<tr>
<td><code>description</code></td>
<td><code>&lt;meta name=&quot;description&quot;&gt;</code> or <code>&lt;meta property=&quot;og:description&quot;&gt;</code></td>
</tr>
<tr>
<td><code>image</code></td>
<td><code>&lt;meta property=&quot;og:image&quot;&gt;</code></td>
</tr>
</tbody>
</table>
<p>When both a standard meta tag and an Open Graph tag are present, the standard meta tag takes precedence.</p>
<h2 id="how-metadata-extraction-works">How metadata extraction works</h2>
<p>When the crawler fetches a page:</p>
<ol>
<li>All <code>&lt;meta&gt;</code> tags with <code>name</code> or <code>property</code> attributes are parsed from the <code>&lt;head&gt;</code> section.</li>
<li>Tag names are matched against your schema (case-insensitive).</li>
<li>The <code>content</code> attribute value is cast to the configured data type.</li>
<li>Extracted metadata is stored alongside the cached HTML.</li>
<li>On subsequent processing, metadata flows into the vector index.</li>
</ol>
<h2 id="boolean-value-parsing">Boolean value parsing</h2>
<p>For <code>boolean</code> fields, the following values are accepted (case-insensitive):</p>
<table>
<thead>
<tr>
<th>True values</th>
<th>False values</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>true</code>, <code>1</code>, <code>yes</code></td>
<td><code>false</code>, <code>0</code>, <code>no</code></td>
</tr>
</tbody>
</table>
<p>Any other value is treated as invalid and the field is omitted.</p>
