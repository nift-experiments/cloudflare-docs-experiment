<p>Base name tag view with an icon, title, and optional subtitle.
Serves as the foundation for <code>RtkMeetingNameTag</code>.</p>
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
<td><code>RtkImage</code></td>
<td>✅</td>
<td>-</td>
<td>The icon image displayed in the name tag</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkNameTagAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for the name tag</td>
</tr>
<tr>
<td><code>title</code></td>
<td><code>String</code></td>
<td>✅</td>
<td>-</td>
<td>The primary text displayed in the name tag</td>
</tr>
<tr>
<td><code>subtitle</code></td>
<td><code>String</code></td>
<td>❌</td>
<td><code>&quot;&quot;</code></td>
<td>Optional secondary text displayed below the title</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let nameTag = RtkNameTag(&#10;    image: RtkImage(image: UIImage(systemName: &quot;mic&quot;)),&#10;    title: &quot;John Doe&quot;&#10;)&#10;view.addSubview(nameTag)&#10;</code></pre>
<h3 id="with-subtitle">With subtitle</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let nameTag = RtkNameTag(&#10;    image: RtkImage(image: UIImage(systemName: &quot;mic&quot;)),&#10;    title: &quot;John Doe&quot;,&#10;    subtitle: &quot;Host&quot;&#10;)&#10;view.addSubview(nameTag)&#10;</code></pre>
