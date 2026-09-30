<p>Review common troubleshooting scenarios for Cloudflare Browser Isolation.</p>
<h2 id="connectivity-and-sessions">Connectivity and sessions</h2>
<h3 id="no-browsers-available">No Browsers Available</h3>
If you encounter a `No Browsers Available` alert, please file feedback via the Cloudflare One Client. This error typically indicates a temporary capacity issue in the data center or a connectivity problem between your client and the remote browser.
<h3 id="maximum-sessions-reached">Maximum Sessions Reached</h3>
This alert appears if your device attempts to establish more than two concurrent remote browser instances. A browser isolation session is shared across all tabs and windows within the same browser (for example, all Chrome tabs share one session). You can use two different browsers (such as Chrome and Firefox) concurrently, but opening a third will trigger this alert. To release a session, close all tabs and windows in one of your local browsers.
<h3 id="audio-or-video-stops-when-switching-windows">Audio or video stops when switching windows</h3>
<p>Browser Isolation supports one active window at a time. When you switch to a different isolated tab or window, Browser Isolation deactivates the previous window, pausing any audio or video playing there. This is expected behavior. For more details, refer to <a href="/cloudflare-one/remote-browser-isolation/known-limitations/#single-active-window">Single active window</a>.</p>
<h2 id="rendering-and-performance">Rendering and performance</h2>
<h3 id="webgl-rendering-error">WebGL Rendering Error</h3>
Cloudflare Browser Isolation uses Network Vector Rendering (NVR), which does not support WebGL (Web Graphics Library) in all environments. If a website requires WebGL and your device lacks the necessary hardware resources in the virtualized environment, you may see a rendering error.
<p>To resolve this, try enabling software rasterization in your browser:</p>
<ol>
<li>Go to <code>chrome://flags/#override-software-rendering-list</code>.</li>
<li>Set <strong>Override software rendering list</strong> to <em>Enabled</em>.</li>
<li>Select <strong>Relaunch</strong>.</li>
</ol>
<h3 id="blank-screen-on-windows">Blank screen on Windows</h3>
On Windows devices, Clientless Web Isolation may load with a blank screen if there is a conflict between browser mDNS settings and Windows IGMP configuration.
<table>
<thead>
<tr>
<th>IGMPLevel</th>
<th>WebRTC Anonymization</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 (disabled)</td>
<td>Enabled / Default</td>
<td>❌ Blank screen</td>
</tr>
<tr>
<td>0 (disabled)</td>
<td>Disabled</td>
<td>✅ Works</td>
</tr>
<tr>
<td>2 (enabled)</td>
<td>Enabled / Default</td>
<td>✅ Works</td>
</tr>
</tbody>
</table>
<p>To fix this, either disable <strong>Anonymize local IPs exposed by WebRTC</strong> in your browser flags or ensure <code>IGMPLevel</code> is enabled (set to <code>2</code>) in your Windows network settings.</p>
<h3 id="rendering-issues-css-images">Rendering issues (CSS/Images)</h3>
If a website displays incorrectly (for example, broken CSS or missing images), it may indicate that the remote browser is unable to fetch specific resources from the origin server. Check your [Gateway HTTP logs](/cloudflare-one/traffic-policies/troubleshooting/) for any blocked subresources that might be required by the page.
<hr />
<h2 id="how-to-contact-support">How to contact Support</h2>
<p>If you cannot resolve the issue, <a href="/support/contacting-cloudflare-support/">open a support case</a>. For RBI issues, it is helpful to provide the <a href="/fundamentals/reference/cloudflare-ray-id/">Ray ID</a> from any error page and a description of the browser you are using.</p>
