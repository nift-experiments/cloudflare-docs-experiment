<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15083.md")
</aside>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Description</th>
<th>Retry</th>
<th>Troubleshooting</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>110100</code></td>
<td>Invalid sitekey</td>
<td>No</td>
<td>Verify the sitekey in <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</td>
</tr>
<tr>
<td><code>110110</code></td>
<td>Sitekey not found</td>
<td>No</td>
<td>Check sitekey spelling and dashboard configuration.</td>
</tr>
<tr>
<td><code>110200</code></td>
<td>Domain not authorized</td>
<td>No</td>
<td>Add current domain in Hostname Management.</td>
</tr>
<tr>
<td><code>110600</code></td>
<td>Challenge timed out</td>
<td>Yes</td>
<td>The visitor's clock may be wrong, or the challenge took too long.</td>
</tr>
<tr>
<td><code>110620</code></td>
<td>Interaction timed out</td>
<td>Yes</td>
<td>The visitor did not interact with the widget in time. Reset with <code>turnstile.reset()</code>.</td>
</tr>
<tr>
<td><code>200100</code></td>
<td>Clock or cache problem</td>
<td>No</td>
<td>The visitor's clock is wrong or the challenge was cached by an intermediary.</td>
</tr>
<tr>
<td><code>200500</code></td>
<td>Iframe load error</td>
<td>Yes</td>
<td>The Turnstile iframe could not load. Check if <code>challenges.cloudflare.com</code> is blocked.</td>
</tr>
<tr>
<td><code>300*</code></td>
<td>Generic challenge failure</td>
<td>Yes</td>
<td>Bot behavior detected. Refer to <a href="#troubleshooting">troubleshooting</a>.</td>
</tr>
<tr>
<td><code>400020</code></td>
<td>Invalid sitekey</td>
<td>No</td>
<td>Verify the sitekey in <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</td>
</tr>
<tr>
<td><code>400070</code></td>
<td>Sitekey disabled</td>
<td>No</td>
<td>The sitekey is disabled. Check the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</td>
</tr>
<tr>
<td><code>600*</code></td>
<td>Generic challenge failure</td>
<td>Yes</td>
<td>Bot behavior detected. Refer to <a href="#troubleshooting">troubleshooting</a>.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="troubleshooting">Troubleshooting</h2>
<p>You can troubleshoot these error codes using the following recommendations:</p>
<ol>
<li>Verify your browser compatibility.
<ul>
<li>Turnstile supports all major browsers, except Internet Explorer.</li>
<li>Ensure your browser is up to date. For more information, refer to our <a href="/cloudflare-challenges/reference/supported-browsers/">Supported browsers</a>.</li>
<li>Run a test on the <a href="https://debug.challenges.cloudflare.com/">compatibility checking tool</a>.</li>
</ul>
</li>
<li>Disable your browser extensions.
<ul>
<li>Some browser extensions, such as ad blockers, may block the scripts Turnstile needs to operate.</li>
<li>Temporarily disable all extensions and reload the page.</li>
</ul>
</li>
<li>Enable JavaScript.
<ul>
<li>Turnstile requires JavaScript to run. Ensure it is enabled in your browser settings. Refer to your browser's documentation for instructions on enabling JavaScript.</li>
</ul>
</li>
<li>Try Incognito or Private mode.
<ul>
<li>Use your browser's incognito or private mode to rule out issues caused by extensions or cached data.</li>
</ul>
</li>
<li>Test another browser or device.
<ul>
<li>Switch to a different browser or device to see if the issue is specific to your current setup.</li>
</ul>
</li>
<li>Avoid VPNs or proxies.
<ul>
<li>Some virtual private networks (VPN) or proxies may interfere with Turnstile. Disable them temporarily to test.</li>
</ul>
</li>
<li>Switch to a different network.
<ul>
<li>Your current network may have restrictions causing Turnstile challenges to fail. Try switching to another network, such as a mobile hotspot.</li>
</ul>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="error-code-401">Error code `401`</h3>
@markup("md", "content/.markup/bodies/15082.md")
</aside>
