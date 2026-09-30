<p>A bottom sheet menu that displays meeting action options such as chat, polls, and participant list.</p>
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
<td><code>String?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Optional title displayed at the top of the menu</td>
</tr>
<tr>
<td><code>features</code></td>
<td><code>[MenuType]</code></td>
<td>✅</td>
<td>-</td>
<td>Array of menu items to display</td>
</tr>
<tr>
<td><code>onSelect</code></td>
<td><code>@escaping (MenuType) -&gt; Void</code></td>
<td>✅</td>
<td>-</td>
<td>Closure called when the user selects a menu item</td>
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
<td><code>show(on:)</code></td>
<td><code>Void</code></td>
<td>Presents the menu as a bottom sheet on the specified <code>UIView</code></td>
</tr>
<tr>
<td><code>reload(title:features:)</code></td>
<td><code>Void</code></td>
<td>Reloads the menu with a new title and set of features</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let menu = RtkMoreMenu(&#10;    features: [.chat, .polls, .participants],&#10;    onSelect: { menuType in&#10;        print(&quot;Selected: \(menuType)&quot;)&#10;    }&#10;)&#10;menu.show(on: self.view)&#10;</code></pre>
<h3 id="with-title">With title</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let menu = RtkMoreMenu(&#10;    title: &quot;More Options&quot;,&#10;    features: [.chat, .polls, .participants],&#10;    onSelect: { menuType in&#10;        switch menuType {&#10;        case .chat:&#10;            print(&quot;Open chat&quot;)&#10;        case .polls:&#10;            print(&quot;Open polls&quot;)&#10;        case .participants:&#10;            print(&quot;Open participants&quot;)&#10;        default:&#10;            break&#10;        }&#10;    }&#10;)&#10;menu.show(on: self.view)&#10;</code></pre>
