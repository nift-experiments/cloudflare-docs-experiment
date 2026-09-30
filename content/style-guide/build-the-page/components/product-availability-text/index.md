<p>The <code>ProductAvailabilityText</code> component dynamically renders a product's lifecycle status (such as &quot;Beta&quot; or &quot;Alpha&quot;) inline with the product name. It renders nothing for generally available (GA) products, so it is safe to leave in place as a product matures.</p>
<p>The <code>product</code> prop must match a file in <code>src/content/directory/</code>.</p>
<pre><code class="language-mdx">import { ProductAvailabilityText } from &quot;~/components&quot;;&#10;&#10;Cloud Connector &lt;ProductAvailabilityText product=&quot;cloud-connector&quot; /&gt; allows you to route matching traffic to a public cloud provider.&#10;</code></pre>
<h2 id="props">Props</h2>
<table>
<thead>
<tr>
<th>Prop</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>product</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>—</td>
<td>Product slug matching a file in <code>src/content/directory/</code>.</td>
</tr>
<tr>
<td><code>parentheses</code></td>
<td><code>string</code></td>
<td>No</td>
<td><code>&quot;true&quot;</code></td>
<td>When <code>&quot;true&quot;</code>, wraps the output in parentheses (for example, <code>(Beta)</code>). Set to <code>&quot;false&quot;</code> for the raw text.</td>
</tr>
</tbody>
</table>
<h2 id="behavior">Behavior</h2>
<ul>
<li>If the product availability is <strong>GA</strong>, the component renders nothing.</li>
<li>If the product or its availability data is not found, the component renders nothing (and logs a warning at build time).</li>
</ul>
