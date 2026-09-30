<p>A generic grid layout view that arranges child views in a responsive grid.
Supports both portrait and landscape orientations with configurable maximum item count.</p>
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
<td><code>maxItems</code></td>
<td><code>UInt</code></td>
<td>❌</td>
<td><code>9</code></td>
<td>Maximum number of items the grid can display</td>
</tr>
<tr>
<td><code>showingCurrently</code></td>
<td><code>UInt</code></td>
<td>✅</td>
<td>-</td>
<td>Number of items currently visible in the grid</td>
</tr>
<tr>
<td><code>getChildView</code></td>
<td><code>@escaping () -&gt; CellContainerView</code></td>
<td>✅</td>
<td>-</td>
<td>Factory closure that creates a new child view for each grid cell</td>
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
<td><code>settingFrames(visibleItemCount:animation:completion:)</code></td>
<td><code>Void</code></td>
<td>Lays out child views in portrait orientation with optional animation</td>
</tr>
<tr>
<td><code>settingFramesForLandScape(visibleItemCount:animation:completion:)</code></td>
<td><code>Void</code></td>
<td>Lays out child views in landscape orientation with optional animation</td>
</tr>
<tr>
<td><code>childView(index:)</code></td>
<td><code>CellContainerView?</code></td>
<td>Returns the child view at the specified index</td>
</tr>
<tr>
<td><code>prepareForReuse(childView:)</code></td>
<td><code>Void</code></td>
<td>Prepares a child view for reuse</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let gridView = GridView(&#10;    maxItems: 6,&#10;    showingCurrently: 4,&#10;    getChildView: {&#10;        return CellContainerView()&#10;    }&#10;)&#10;view.addSubview(gridView)&#10;</code></pre>
<h3 id="update-layout">Update layout</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let gridView = GridView(&#10;    maxItems: 9,&#10;    showingCurrently: 3,&#10;    getChildView: {&#10;        return CellContainerView()&#10;    }&#10;)&#10;view.addSubview(gridView)&#10;&#10;// Update layout with animation&#10;gridView.settingFrames(&#10;    visibleItemCount: 4,&#10;    animation: true,&#10;    completion: {&#10;        print(&quot;Layout updated&quot;)&#10;    }&#10;)&#10;</code></pre>
