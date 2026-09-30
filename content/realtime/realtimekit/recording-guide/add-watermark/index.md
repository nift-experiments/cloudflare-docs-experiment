<p>RealtimeKit's watermark feature enables you to include an image as a watermark in your recording. To add watermark, configure the following parameters to video_config in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<table>
<thead>
<tr>
<th><strong>Parameter</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>URL</td>
<td>Specify the URL of the watermark image</td>
</tr>
<tr>
<td>Position</td>
<td>Specify the placement of the watermark, you have the flexibility to choose between left top, right top, left bottom, or right bottom. The default position is set to left top.</td>
</tr>
<tr>
<td>Size</td>
<td>Specify the height and width of the watermark in pixels.</td>
</tr>
</tbody>
</table>
<pre><code class="language-json">{&#10;  &quot;video_config&quot;: {&#10;    &quot;watermark&quot;: {&#10;      &quot;url&quot;: &quot;https://test.io/images/client-logos-6.webp&quot;,&#10;      &quot;position&quot;: &quot;left top&quot;,&#10;      &quot;size&quot;: {&#10;        &quot;height&quot;: 20,&#10;        &quot;width&quot;: 100&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
