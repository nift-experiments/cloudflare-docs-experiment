<p>A control bar button for webinar stage actions.
Supports requesting to join, joining, leaving, and canceling stage requests based on the current stage status.</p>
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
<td><code>rtkClient</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance</td>
</tr>
<tr>
<td><code>buttonState</code></td>
<td><code>WebinarStageStatus</code></td>
<td>✅</td>
<td>-</td>
<td>The current stage status that determines the button action</td>
</tr>
<tr>
<td><code>presentingViewController</code></td>
<td><code>UIViewController</code></td>
<td>✅</td>
<td>-</td>
<td>View controller used for presenting confirmation dialogs</td>
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
<td><code>dataSource</code></td>
<td><code>RtkStageActionButtonControlBarDataSource?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Data source for customizing stage action button behavior</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let stageButton = RtkStageActionButtonControlBar(&#10;    rtkClient: rtkClient,&#10;    buttonState: .requestToJoinStage,&#10;    presentingViewController: self&#10;)&#10;view.addSubview(stageButton)&#10;</code></pre>
