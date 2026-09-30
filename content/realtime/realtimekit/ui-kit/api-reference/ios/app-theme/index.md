<p>The application theme singleton that provides pre-configured appearance objects for UI components.
Use <code>AppTheme.shared</code> to access default appearances or call <code>setUp(theme:)</code> to apply a custom theme.</p>
<h2 id="access">Access</h2>
<pre><code class="language-swift">let theme = AppTheme.shared&#10;</code></pre>
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
<td><code>setUp(theme: AppThemeProtocol)</code></td>
<td><code>Void</code></td>
<td>Applies a custom theme conforming to <code>AppThemeProtocol</code></td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="access-default-theme">Access default theme</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let theme = AppTheme.shared&#10;let titleAppearance = theme.meetingTitleAppearance&#10;let clockAppearance = theme.clockViewAppearance&#10;</code></pre>
<h3 id="apply-a-custom-theme">Apply a custom theme</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;class CustomTheme: AppThemeProtocol {&#10;    // Implement required appearance properties&#10;}&#10;&#10;let customTheme = CustomTheme()&#10;AppTheme.shared.setUp(theme: customTheme)&#10;</code></pre>
