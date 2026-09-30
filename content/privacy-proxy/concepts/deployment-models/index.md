<p>Privacy Proxy supports two deployment architectures: single-hop and double-hop. The right choice depends on your privacy requirements and operational preferences.</p>
<h2 id="single-hop">Single-hop</h2>
<p>In a single-hop deployment, Cloudflare operates the entire proxy infrastructure. Clients connect directly to Cloudflare's Privacy Proxy, which handles authentication, proxying, and egress.</p>
<pre><code>┌────────┐      ┌─────────────────┐      ┌─────────────┐&#10;│ Client │ ───▶ │  Privacy Proxy  │ ───▶ │ Destination │&#10;│        │      │  (Cloudflare)   │      │   Server    │&#10;└────────┘      └─────────────────┘      └─────────────┘&#10;</code></pre>
<h3 id="how-it-works">How it works</h3>
<ol>
<li>The client establishes an HTTP/2 or HTTP/3 connection to the Cloudflare proxy endpoint.</li>
<li>The client authenticates using Privacy Pass tokens or a pre-shared key.</li>
<li>The client sends CONNECT requests to establish tunnels to destination servers.</li>
<li>Cloudflare proxies traffic and selects egress IP addresses based on client geolocation.</li>
</ol>
<h3 id="use-cases">Use cases</h3>
<p>Single-hop deployment works well when:</p>
<ul>
<li>You want Cloudflare to manage the complete proxy infrastructure.</li>
<li>Your privacy model requires hiding client IP addresses from destinations, but not from the proxy operator.</li>
<li>You need a straightforward integration with minimal client-side changes.</li>
</ul>
<h4 id="example-microsoft-edge-secure-network">Example: Microsoft Edge Secure Network</h4>
<p><a href="https://blog.cloudflare.com/cloudflare-now-powering-microsoft-edge-secure-network/">Microsoft Edge Secure Network</a> uses single-hop deployment. The Edge browser connects directly to Cloudflare's Privacy Proxy, which handles authentication via Privacy Pass and proxies traffic to destination servers. Users get protection from network observers and destination servers without needing to configure additional infrastructure.</p>
<hr />
<h2 id="double-hop">Double-hop</h2>
<p>In a double-hop deployment, you operate the first proxy (Proxy A), and Cloudflare operates the second proxy (Proxy B). This creates stronger privacy separation because no single party sees both user identity and destination.</p>
<pre><code>┌────────┐      ┌─────────────┐      ┌─────────────────┐      ┌─────────────┐&#10;│ Client │ ───▶ │   Proxy A   │ ───▶ │    Proxy B      │ ───▶ │ Destination │&#10;│        │      │    (You)    │      │  (Cloudflare)   │      │   Server    │&#10;└────────┘      └─────────────┘      └─────────────────┘      └─────────────┘&#10;</code></pre>
<h3 id="how-it-works-1">How it works</h3>
<ol>
<li>The client connects to Proxy A, which you operate.</li>
<li>Proxy A authenticates the user and verifies they can use the service.</li>
<li>Proxy A establishes a tunnel to Cloudflare's Proxy B, forwarding the client's CONNECT request.</li>
<li>Proxy B connects to the destination and proxies traffic.</li>
<li>Proxy B selects egress IPs based on geolocation provided by Proxy A.</li>
</ol>
<h3 id="privacy-separation">Privacy separation</h3>
<p>The double-hop architecture ensures:</p>
<table>
<thead>
<tr>
<th>Information</th>
<th>Proxy A (you)</th>
<th>Proxy B (Cloudflare)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client IP address</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>User account</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Destination server</td>
<td>Encrypted</td>
<td>Yes</td>
</tr>
<tr>
<td>Request content</td>
<td>Encrypted</td>
<td>Encrypted</td>
</tr>
</tbody>
</table>
<p>Proxy A knows who the user is but cannot see where they are going (the destination is encrypted). Proxy B knows the destination but not who is making the request. Neither party has the complete picture.</p>
<h3 id="use-cases-1">Use cases</h3>
<p>Double-hop deployment works well when:</p>
<ul>
<li>You need stronger privacy guarantees where no single operator sees both identity and destination.</li>
<li>You want to maintain control over user authentication and account management.</li>
<li>Regulatory or compliance requirements mandate separation of user data.</li>
</ul>
<h4 id="example-icloud-private-relay">Example: iCloud Private Relay</h4>
<p><a href="https://blog.cloudflare.com/icloud-private-relay/">iCloud Private Relay</a> uses double-hop deployment. Apple operates the first-hop proxy, which authenticates users with their Apple ID and encrypts the destination. Cloudflare operates the second-hop proxy, which decrypts the destination and connects to the server. Apple knows who the user is but not where they browse. Cloudflare knows the destinations but not who is browsing.</p>
<hr />
<h2 id="comparison">Comparison</h2>
<table>
<thead>
<tr>
<th>Aspect</th>
<th>Single-hop</th>
<th>Double-hop</th>
</tr>
</thead>
<tbody>
<tr>
<td>Infrastructure</td>
<td>Cloudflare only</td>
<td>You + Cloudflare</td>
</tr>
<tr>
<td>Privacy separation</td>
<td>Proxy sees identity + destination</td>
<td>Split across two parties</td>
</tr>
<tr>
<td>Operational complexity</td>
<td>Lower</td>
<td>Higher</td>
</tr>
<tr>
<td>Authentication</td>
<td>Cloudflare-managed</td>
<td>You manage first-hop auth</td>
</tr>
<tr>
<td>Use case</td>
<td>Browser VPNs, simple privacy</td>
<td>Maximum privacy separation</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="choose-a-deployment-model">Choose a deployment model</h2>
<p>Consider these questions when selecting a deployment model:</p>
<ol>
<li>Who should manage user authentication?</li>
</ol>
<p>If you want Cloudflare to handle authentication, use single-hop. If you need control over user accounts, use double-hop.</p>
<ol start="2">
<li>What are your privacy requirements?</li>
</ol>
<p>If your threat model requires that no single party sees both user identity and browsing activity, use double-hop.</p>
<ol start="3">
<li>What operational capacity do you have?</li>
</ol>
<p>Double-hop requires you to operate and maintain a proxy. If you prefer a fully managed solution, use single-hop.</p>
<p><a href="https://www.cloudflare.com/lp/privacy-edge/">Contact us</a> to discuss which deployment model fits your use case.</p>
