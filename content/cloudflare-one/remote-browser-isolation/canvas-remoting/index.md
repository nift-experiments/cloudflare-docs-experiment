<p>Canvas Remoting is a Browser Isolation capability that optimizes performance for web applications using the HTML5 Canvas API (a browser feature that allows web applications to draw graphics directly on the page). It sends vector draw commands to the client instead of rasterized bitmaps (pixel images), reducing bandwidth consumption and improving frame rates for productivity applications.</p>
<h2 id="how-it-works">How it works</h2>
<p>Browser Isolation uses Network Vector Rendering (NVR) to send lightweight drawing instructions to the user's browser, rather than streaming rendered pixels or video of the page. However, HTML5 Canvas content previously required server-side rasterization (converting draw commands into pixel images), sending large bitmaps for every frame.</p>
<p>Canvas Remoting extends NVR to Canvas-based applications by:</p>
<ol>
<li>Capturing draw commands made to the HTML5 Canvas element.</li>
<li>Converting and sending those commands to the client as NVR instructions.</li>
<li>Rendering the Canvas content on the client onto an offscreen texture (a hidden drawing surface used for intermediate rendering).</li>
<li>Compositing (layering) the texture into the final document output.</li>
</ol>
<h2 id="supported-applications">Supported applications</h2>
<p>Canvas Remoting improves performance for productivity applications that rely on the HTML5 Canvas API:</p>
<table>
<thead>
<tr>
<th>Application</th>
<th>Improvement</th>
</tr>
</thead>
<tbody>
<tr>
<td>Microsoft Word</td>
<td>10x bandwidth reduction</td>
</tr>
<tr>
<td>Microsoft Excel</td>
<td>Smooth scrolling and data entry</td>
</tr>
<tr>
<td>Microsoft PowerPoint</td>
<td>Fluid animations</td>
</tr>
<tr>
<td>Google Sheets</td>
<td>Consistent 30fps rendering</td>
</tr>
<tr>
<td>Google Maps</td>
<td>Smooth panning and zooming</td>
</tr>
<tr>
<td>Web-based terminals and AI notebooks</td>
<td>Fast and responsive text input and display</td>
</tr>
</tbody>
</table>
<h2 id="limitations">Limitations</h2>
<p>Canvas Remoting supports 2D Canvas contexts only. The following are not supported:</p>
<ul>
<li>WebGL and WebGPU contexts</li>
<li>3D graphics applications</li>
<li>Advanced Canvas features requiring GPU acceleration</li>
</ul>
<h2 id="enable-or-disable-canvas-remoting">Enable or disable Canvas Remoting</h2>
<p>Canvas Remoting is on by default for all Browser Isolation customers. No configuration is required.</p>
<p><img src="/assets/upstream/images/cloudflare-one/remote-browser-isolation/canvas-remoting-context-menu.png" alt="Canvas Remoting context menu option" /></p>
<h3 id="disable-canvas-remoting-for-the-current-session">Disable Canvas Remoting for the current session</h3>
<ol>
<li>Right-click on the background of the isolated webpage.</li>
<li>Select <strong>Disable Canvas Remoting</strong> from the context menu.</li>
</ol>
<h3 id="re-enable-canvas-remoting">Re-enable Canvas Remoting</h3>
<ol>
<li>Right-click on the background of the isolated webpage.</li>
<li>Select <strong>Enable Canvas Remoting</strong> from the context menu.</li>
</ol>
<h2 id="troubleshooting">Troubleshooting</h2>
<details class="nb-details"><summary>Canvas content renders slowly</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4469.md")
</div></details>
<details class="nb-details"><summary>Graphical glitches or missing elements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4470.md")
</div></details>
