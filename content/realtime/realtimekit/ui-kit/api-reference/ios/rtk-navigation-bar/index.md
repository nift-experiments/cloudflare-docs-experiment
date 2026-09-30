<p>A navigation bar with a title label and a close or back button.
Used for modal screens such as chat, polls, and participant lists.</p>
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
<td><code>title</code></td>
<td><code>String</code></td>
<td>✅</td>
<td>-</td>
<td>The title text displayed in the navigation bar</td>
</tr>
</tbody>
</table>
<h2 id="properties">Properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>titleLabel</code></td>
<td><code>RtkLabel</code></td>
<td>-</td>
<td>-</td>
<td>The label displaying the navigation bar title (read-only)</td>
</tr>
<tr>
<td><code>leftButton</code></td>
<td><code>RtkControlBarButton</code></td>
<td>-</td>
<td>-</td>
<td>The close or back button on the left side (read-only)</td>
</tr>
</tbody>
</table>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Return Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>setBackButtonClick(callBack:)</code></td>
<td><code>Void</code></td>
<td>Sets the tap handler for the back or close button</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let navBar = RtkNavigationBar(title: &quot;Participants&quot;)&#10;view.addSubview(navBar)&#10;</code></pre>
<h3 id="with-back-button-handler">With back button handler</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let navBar = RtkNavigationBar(title: &quot;Chat&quot;)&#10;navBar.setBackButtonClick {&#10;    self.dismiss(animated: true)&#10;}&#10;view.addSubview(navBar)&#10;</code></pre>
