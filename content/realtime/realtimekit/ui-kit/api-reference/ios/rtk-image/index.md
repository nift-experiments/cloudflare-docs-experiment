<p>A struct that wraps a <code>UIImage</code> or a <code>URL</code> for image content.
Used throughout the UI Kit for icons, avatars, and custom images.</p>
<h2 id="initializer-parameters">Initializer parameters</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>image</code></td>
<td><code>UIImage?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>A local UIImage to display</td>
</tr>
<tr>
<td><code>url</code></td>
<td><code>URL?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>A remote URL to load the image from</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="with-a-local-image">With a local image</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkImage = RtkImage(image: UIImage(systemName: &quot;mic&quot;))&#10;</code></pre>
<h3 id="with-a-remote-url">With a remote URL</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkImage = RtkImage(url: URL(string: &quot;https://example.com/avatar.png&quot;))&#10;</code></pre>
