<p>A composite view for displaying plugins and screen share content.
Includes a tab selector, plugin content area, and a floating active speaker view.</p>
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
<td><code>videoPeerViewModel</code></td>
<td><code>VideoPeerViewModel</code></td>
<td>✅</td>
<td>-</td>
<td>The view model for the active speaker video</td>
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
<td><code>activeListView</code></td>
<td><code>RtkActiveTabSelectorView</code></td>
<td>-</td>
<td>-</td>
<td>The tab selector for switching between plugins and screen shares</td>
</tr>
<tr>
<td><code>pluginVideoView</code></td>
<td><code>UIView</code></td>
<td>-</td>
<td>-</td>
<td>The container view for plugin content</td>
</tr>
<tr>
<td><code>syncButton</code></td>
<td><code>UIButton</code></td>
<td>-</td>
<td>-</td>
<td>Button to sync the plugin view with the presenter</td>
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
<td><code>setButtons(buttons:selectedIndex:clickAction:)</code></td>
<td><code>Void</code></td>
<td>Configures the tab selector buttons with a selection handler</td>
</tr>
<tr>
<td><code>show(pluginView:)</code></td>
<td><code>Void</code></td>
<td>Displays a plugin view in the content area</td>
</tr>
<tr>
<td><code>showVideoView(participant:)</code></td>
<td><code>Void</code></td>
<td>Displays a participant's video in the content area</td>
</tr>
<tr>
<td><code>showPinnedView(participant:)</code></td>
<td><code>Void</code></td>
<td>Displays a pinned participant's video</td>
</tr>
<tr>
<td><code>showActiveSpeakerView(participant:)</code></td>
<td><code>Void</code></td>
<td>Shows the floating active speaker overlay</td>
</tr>
<tr>
<td><code>hideActiveSpeaker()</code></td>
<td><code>Void</code></td>
<td>Hides the floating active speaker overlay</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let viewModel = VideoPeerViewModel(&#10;    meeting: rtkClient,&#10;    participant: participant,&#10;    showSelfPreviewVideo: false&#10;)&#10;let pluginsView = RtkPluginsView(videoPeerViewModel: viewModel)&#10;view.addSubview(pluginsView)&#10;</code></pre>
<h3 id="with-tab-buttons">With tab buttons</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let viewModel = VideoPeerViewModel(&#10;    meeting: rtkClient,&#10;    participant: participant,&#10;    showSelfPreviewVideo: false&#10;)&#10;let pluginsView = RtkPluginsView(videoPeerViewModel: viewModel)&#10;&#10;let buttons = [&#10;    RtkPluginScreenShareTabButton(image: nil, title: &quot;Screen Share&quot;),&#10;    RtkPluginScreenShareTabButton(image: nil, title: &quot;Whiteboard&quot;)&#10;]&#10;pluginsView.setButtons(&#10;    buttons: buttons,&#10;    selectedIndex: 0,&#10;    clickAction: { index in&#10;        print(&quot;Selected tab: \(index)&quot;)&#10;    }&#10;)&#10;view.addSubview(pluginsView)&#10;</code></pre>
