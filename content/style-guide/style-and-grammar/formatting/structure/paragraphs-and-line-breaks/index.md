<h2 id="paragraphs-in-markdown">Paragraphs in Markdown</h2>
<p>To start a new paragraph, leave an empty line (with no spaces) before adding the new paragraph content.</p>
<pre><code class="language-txt">This sentence is the first one in this paragraph.&#10;This second sentence also belongs to the first paragraph.&#10;&#10;This is the first sentence of the second paragraph.&#10;</code></pre>
<h2 id="line-breaks-in-markdown">Line breaks in Markdown</h2>
<p>Avoid line breaks when possible. Considering creating a separate paragraph, even inside numbered lists.</p>
<p>If you need to add a line break, use the <code>&lt;br/&gt;</code> HTML element.</p>
<p>Example inside a table:</p>
<pre><code class="language-txt">| Feature                          | Enabled |&#10;|----------------------------------|---------|&#10;| Feature name&lt;br/&gt;Additional info | Yes     |&#10;</code></pre>
<p>This is how the table looks:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Enabled</th>
</tr>
</thead>
<tbody>
<tr>
<td>Feature name<br/>Additional info</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14684.md")
</aside>
