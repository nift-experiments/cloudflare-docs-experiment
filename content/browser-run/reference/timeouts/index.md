<p>Browser Run uses several independent timers to manage how long different parts of a request can take. If any of these timers exceed their limit, the request returns a timeout error.</p>
<p>Each timer controls a specific part of the rendering lifecycle — from page load, to selector load, to action.</p>
<table>
<thead>
<tr>
<th>Timer</th>
<th>Scope</th>
<th>Default</th>
<th>Max</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>goToOptions.timeout</code></td>
<td>Time to wait for the page to load before timeout.</td>
<td>30 s</td>
<td>60 s</td>
</tr>
<tr>
<td><code>goToOptions.waitUntil</code></td>
<td>Determines when page load is considered complete. Refer to <a href="#waituntil-options"><code>waitUntil</code> options</a> for details.</td>
<td><code>domcontentloaded</code></td>
<td>—</td>
</tr>
<tr>
<td><code>waitForSelector</code></td>
<td>Time to wait for a specific element (any CSS selector) to appear on the page.</td>
<td>null</td>
<td>60 s</td>
</tr>
<tr>
<td><code>waitForTimeout</code></td>
<td>Additional amount of time to wait after the page has loaded to proceed with actions.</td>
<td>null</td>
<td>60 s</td>
</tr>
<tr>
<td><code>actionTimeout</code></td>
<td>Time to wait for the action itself (for example: a screenshot, PDF, or scrape) to complete after the page has loaded.</td>
<td>null</td>
<td>5 min</td>
</tr>
<tr>
<td><code>PDFOptions.timeout</code></td>
<td>Same as <code>actionTimeout</code>, but only applies to the <a href="/browser-run/quick-actions/pdf-endpoint/">/pdf endpoint</a>.</td>
<td>30 s</td>
<td>5 min</td>
</tr>
</tbody>
</table>
<h3 id="waituntil-options"><code>waitUntil</code> options</h3>
<p>The <code>goToOptions.waitUntil</code> parameter controls when the browser considers page navigation complete. This is important for JavaScript-heavy pages where content is rendered dynamically after the initial page load.</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>load</code></td>
<td>Waits for the <code>load</code> event, including all resources like images and stylesheets</td>
</tr>
<tr>
<td><code>domcontentloaded</code></td>
<td>Waits until the DOM content has been fully loaded, which fires before the <code>load</code> event (default)</td>
</tr>
<tr>
<td><code>networkidle0</code></td>
<td>Waits until there are no network connections for at least 500 ms</td>
</tr>
<tr>
<td><code>networkidle2</code></td>
<td>Waits until there are no more than two network connections for at least 500 ms</td>
</tr>
</tbody>
</table>
<p>For pages that rely on JavaScript to render content, use <code>networkidle0</code> or <code>networkidle2</code> to ensure the page is fully rendered before extraction.</p>
<h2 id="notes-and-recommendations">Notes and recommendations</h2>
<p>You can set multiple timers — as long as one is complete, the request will fire.</p>
<p>If you are not getting the expected output:</p>
<ul>
<li>Try increasing <code>goToOptions.timeout</code> (up to 60 s).</li>
<li>If waiting for a specific element, use <code>waitForSelector</code>. Otherwise, use <code>goToOptions.waitUntil</code> set to <code>networkidle2</code> to ensure the page has finished loading dynamic content.</li>
<li>If you are getting a <code>422</code>, it may be the action itself (ex: taking a screenshot, extracting the html content) that takes a long time. Try increasing the <code>actionTimeout</code> instead.</li>
</ul>
