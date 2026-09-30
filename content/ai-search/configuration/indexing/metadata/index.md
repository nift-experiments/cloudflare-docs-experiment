<p>Use metadata attributes to organize your indexed documents and provide context to guide AI responses. This page covers built-in metadata attributes and custom metadata schemas. To filter search results by these attributes at query time, refer to <a href="/ai-search/configuration/retrieval/filtering/">Filtering</a>.</p>
<h2 id="built-in-metadata-attributes">Built-in metadata attributes</h2>
<p>AI Search automatically extracts the following metadata attributes from your indexed documents:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>filename</code></td>
<td>The name of the file.</td>
<td><code>guide.pdf</code> or <code>docs/getting-started/guide.pdf</code></td>
</tr>
<tr>
<td><code>folder</code></td>
<td>The folder or prefix to the object.</td>
<td>For <code>docs/getting-started/guide.pdf</code>, the folder is <code>docs/getting-started/</code></td>
</tr>
<tr>
<td><code>timestamp</code></td>
<td>Unix timestamp (milliseconds) when the object was last modified. Comparisons round down to seconds.</td>
<td><code>1735689600000</code> (2025-01-01 00:00:00 UTC)</td>
</tr>
</tbody>
</table>
<h2 id="custom-metadata-attributes">Custom metadata attributes</h2>
<p>Custom metadata allows you to define additional fields for filtering search results. You can attach structured metadata to documents and filter queries by attributes such as category, version, or any custom field.</p>
<h3 id="supported-data-types">Supported data types</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
<th>Example values</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>text</code></td>
<td>String values</td>
<td><code>&quot;documentation&quot;</code>, <code>&quot;blog-post&quot;</code></td>
</tr>
<tr>
<td><code>number</code></td>
<td>Numeric values (parsed as float)</td>
<td><code>2.5</code>, <code>100</code>, <code>-3.14</code></td>
</tr>
<tr>
<td><code>boolean</code></td>
<td>Boolean values</td>
<td><code>true</code>, <code>false</code>, <code>1</code>, <code>0</code>, <code>yes</code>, <code>no</code></td>
</tr>
<tr>
<td><code>datetime</code></td>
<td>Date and time values</td>
<td><code>&quot;2026-01-15T00:00:00Z&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="define-a-schema">Define a schema</h3>
<p>Before custom metadata can be extracted, define a schema in your AI Search configuration using the <code>custom_metadata</code> field. The schema specifies which fields to extract and their data types.</p>
<pre><code class="language-ts">custom_metadata: [&#10;	{ field_name: &quot;category&quot;, data_type: &quot;text&quot; },&#10;	{ field_name: &quot;version&quot;, data_type: &quot;number&quot; },&#10;	{ field_name: &quot;is_public&quot;, data_type: &quot;boolean&quot; },&#10;];&#10;</code></pre>
<p><strong>Schema constraints:</strong></p>
<ul>
<li>Maximum of 5 custom metadata fields per AI Search instance</li>
<li>Field names are case-insensitive and stored as lowercase</li>
<li>Field names cannot use reserved names: <code>timestamp</code>, <code>folder</code>, <code>filename</code></li>
<li>Changing the schema triggers a full re-index of all documents</li>
</ul>
<h3 id="add-custom-metadata-attributes-to-documents">Add custom metadata attributes to documents</h3>
<p>How you attach custom metadata attributes depends on your data source:</p>
<ul>
<li><strong>R2 bucket</strong>: Set metadata using S3-compatible custom headers (<code>x-amz-meta-*</code>). Refer to <a href="/ai-search/configuration/data-source/r2/#custom-metadata">R2 custom metadata</a> for examples.</li>
<li><strong>Website</strong>: Add <code>&lt;meta&gt;</code> tags to your HTML pages. Refer to <a href="/ai-search/configuration/data-source/website/custom-metadata/">Website custom metadata</a> for details.</li>
<li><strong>Built-in storage</strong>: Attach metadata when uploading files through the <a href="/ai-search/api/items/workers-binding/#upload-with-metadata">Items API</a>.</li>
</ul>
<h2 id="re-indexing-behavior">Re-indexing behavior</h2>
<p>When you modify the <code>custom_metadata</code> schema:</p>
<ol>
<li>New fields are added to the search index.</li>
<li>Removed fields are deleted from the search index.</li>
<li>A full re-index is triggered for all documents.</li>
<li>Existing vectors are updated with the new metadata structure.</li>
</ol>
<h2 id="metadata-storage-and-filtering">Metadata storage and filtering</h2>
<p>AI Search stores metadata for each vector in a shared 10 KiB compact JSON UTF-8 envelope. The envelope includes field names, JSON syntax, required AI Search system metadata, and customer metadata. It is not a per-field limit.</p>
<p>Configured custom fields take priority over undeclared source metadata. AI Search assembles metadata deterministically, retaining complete values that fit. When capacity remains, configured string values can be truncated on UTF-8 character boundaries. Required AI Search metadata is always preserved.</p>
<p>Only the first 64 UTF-8 bytes of each indexed string are filterable. Longer strings can be stored, but bytes after the first 64 are not filterable. For Vectorize details, refer to <a href="/vectorize/platform/limits/">Limits</a> and <a href="/vectorize/reference/metadata-filtering/">Metadata filtering</a>.</p>
<h2 id="limitations">Limitations</h2>
<table>
<thead>
<tr>
<th>Constraint</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum custom fields</td>
<td>5 per AI Search instance</td>
</tr>
<tr>
<td>Metadata per vector</td>
<td>10 KiB total, including system data and JSON syntax</td>
</tr>
<tr>
<td>Filterable indexed strings</td>
<td>First 64 UTF-8 bytes of each string</td>
</tr>
<tr>
<td>Reserved field names</td>
<td><code>timestamp</code>, <code>folder</code>, <code>filename</code></td>
</tr>
<tr>
<td>Field name matching</td>
<td>Case-insensitive</td>
</tr>
</tbody>
</table>
