<p>If your organization uses a firewall or other policies to restrict Internet traffic, you may need to make a few changes to allow Browser Isolation to connect.</p>
<h2 id="remoting-client">Remoting client</h2>
<p>Isolated pages are served by the remoting client — the software component in the user's browser that loads, displays, and communicates with the remote browser session. This client communicates to Cloudflare's network via HTTPS and WebRTC.</p>
<h3 id="remoting-client-services">Remoting Client (Services)</h3>
<p>The remoting client provides static assets and API endpoints. For Browser Isolation to function, you must allow:</p>
<ul>
<li>HTTPS traffic to <code>*.browser.run</code> on port <code>443</code></li>
</ul>
<h4 id="clientless-web-isolation">Clientless Web Isolation</h4>
<p>Users connecting through Clientless Web Isolation also require connectivity to Cloudflare Access. For users to connect to Access, you must allow:</p>
<ul>
<li>HTTPS traffic to <code>https://&lt;team-name&gt;.cloudflareaccess.com</code> on port <code>443</code></li>
</ul>
<h3 id="webrtc-channel">WebRTC channel</h3>
<p>Browser Isolation uses WebRTC (a real-time communication protocol) for low-latency communication between the local browser and the remote browser. WebRTC uses UDP rather than TCP, which means this traffic does not flow through standard HTTP/HTTPS proxy settings. The connecting device must have direct UDP connectivity to the IP ranges listed below.</p>
<p>In order to pass WebRTC traffic, the remoting client must be able to connect to the following IP addresses:</p>
<table>
<thead>
<tr>
<th>IP range</th>
<th>Port range</th>
<th>Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4: <code>162.159.201.10 - 162.159.201.255</code> <br/> IPv4: <code>172.64.73.0 - 172.64.73.255</code> <br/> IPv6: <code>2606:4700:f2::/48</code></td>
<td>10000 - 59999</td>
<td>UDP</td>
</tr>
</tbody>
</table>
<p>Each remote browser instance is randomly assigned a port, and the port that a user is allocated to will change often and without notice.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4447.md")
</aside>
