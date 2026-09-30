<p>An audio visualizer component which visualizes a participants audio.
Commonly used inside <code>rtk-name-tag</code>.</p>
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
<td><code>hideMuted</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hide the visualizer if audio is muted</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isScreenShare</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Audio visualizer for screensharing, it will use screenShareTracks.audio instead of audioTrack</td>
</tr>
<tr>
<td><code>participant</code></td>
<td><code>Peer</code></td>
<td>✅</td>
<td>-</td>
<td>Participant object</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>AudioVisualizerVariant</code></td>
<td>✅</td>
<td>-</td>
<td>Variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-audio-visualizer&gt;&lt;/rtk-audio-visualizer&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-audio-visualizer&gt;&#10;&lt;/rtk-audio-visualizer&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-audio-visualizer&quot;);&#10;&#10;  el.hideMuted= true;&#10;  el.isScreenShare= true;&#10;  el.participant= participant&#10;&lt;/script&gt;&#10;</code></pre>
