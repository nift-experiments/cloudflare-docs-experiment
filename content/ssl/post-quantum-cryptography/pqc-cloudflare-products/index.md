<p>Cloudflare is <a href="https://blog.cloudflare.com/post-quantum-roadmap/">targeting 2029</a> to be fully post-quantum secure across its entire product suite.</p>
<p>This page shows the status of the migration. Each section below groups Cloudflare products by the underlying secure communication channel. Once a channel supports PQC, every product built on top inherits PQC support.</p>
<p>Each section captures the classes of post-quantum algorithms deployed in the secure communication channel: <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">key agreement</a> (sometimes called post-quantum encryption, which protects against <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now, decrypt-later</a> attacks) and <a href="/ssl/post-quantum-cryptography/#post-quantum-signatures">signatures</a> (sometimes called post-quantum authentication, which protects live systems against unauthorized access by quantum adversaries <a href="https://blog.cloudflare.com/post-quantum-roadmap/">after Q-Day</a>).</p>
<p>A Cloudflare-side ✅ entry only delivers end-to-end post-quantum protection when <strong>the party on the other side of the connection also supports the same post-quantum algorithms</strong>. Refer to <a href="/ssl/post-quantum-cryptography/pqc-support/">PQC support</a> for the list of browsers, libraries, and servers that support the algorithms Cloudflare has deployed.</p>
<p>For an end-to-end walkthrough of how Cloudflare One on-ramps and off-ramps fit together, refer to <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/">PQC and Cloudflare One</a>.</p>
<h2 id="visitor-to-cloudflare">Visitor to Cloudflare</h2>
<p>Inbound TLS 1.3 (including QUIC) from end-user clients to Cloudflare's edge.</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>✅ X25519MLKEM768</td>
</tr>
<tr>
<td>Signatures</td>
<td>📝 Planned via <a href="https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/">Merkle Tree Certificates</a></td>
</tr>
</tbody>
</table>
<p>Reference: <a href="https://blog.cloudflare.com/post-quantum-for-all/">PQC for all websites and APIs</a>.</p>
<p><strong>Products covered:</strong> any proxied hostname or HTTPS application behind Cloudflare, including:</p>
<ul>
<li>The Cloudflare developer platform: <a href="/workers/">Workers</a> custom domains, <code>*.workers.dev</code>, <a href="/pages/">Pages</a>, <a href="/r2/">R2</a> public buckets, <a href="/stream/">Stream</a>, and <a href="/images/">Images</a>.</li>
<li><a href="/api-shield/">API Shield</a>-protected APIs.</li>
<li>The Cloudflare API and dashboard.</li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Cloudflare Access</a> self-hosted applications (browser-to-edge leg).</li>
</ul>
<p>Customers can measure per-zone post-quantum key agreement adoption on their inbound traffic using the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/#clienttlskeyexchangegroup"><code>ClientTLSKeyExchangeGroup</code></a> field in the <code>http_requests</code> Logpush dataset, which is also queryable in <a href="/log-explorer/">Log Explorer</a>.</p>
<p>This section only covers the inbound TLS connection from the end-user client to Cloudflare's edge. When a Worker fetches data from a backend storage service (<a href="/d1/">D1</a>, <a href="/kv/">KV</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/r2/">R2</a>, <a href="/workers-ai/">Workers AI</a>, <a href="/hyperdrive/">Hyperdrive</a>, and similar), that connection is governed by the <a href="#cloudflare-internal-network">Cloudflare internal network</a> section. When a Worker calls out to a third-party origin via <code>fetch()</code>, it is governed by the <a href="#cloudflare-to-origin">Cloudflare to origin</a> section.</p>
<h2 id="cloudflare-internal-network">Cloudflare internal network</h2>
<p>Service-to-service TLS connections between Cloudflare data centers and internal services.</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>🚧 X25519MLKEM768</td>
</tr>
<tr>
<td>Signatures</td>
<td>Not yet</td>
</tr>
</tbody>
</table>
<p>Reference: <a href="https://blog.cloudflare.com/post-quantum-cryptography-ga/">PQC generally available</a>, <a href="https://blog.cloudflare.com/post-quantum-roadmap/">Roadmap</a>.</p>
<p>Most internal connections have been migrated to X25519MLKEM768. A long tail of services is still in the process of being upgraded.</p>
<h2 id="cloudflare-to-origin">Cloudflare to origin</h2>
<p>Outbound TLS 1.3 connections from Cloudflare's edge to customer origin servers.</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>✅ X25519MLKEM768</td>
</tr>
<tr>
<td>Signatures</td>
<td>✅ ML-DSA via <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a> and <a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a></td>
</tr>
</tbody>
</table>
<p>Reference: <a href="/ssl/post-quantum-cryptography/pqc-to-origin/">PQC to your origin</a>.</p>
<p><strong>Products covered:</strong> any Cloudflare-proxied zone's origin pull, and the egress leg of <a href="#cloudflare-gateway">Cloudflare Gateway</a> (SWG, HTTPS inspection) when Gateway fetches third-party origin content on behalf of the client. Gateway's post-quantum support on this leg is independent of which on-ramp the client uses to reach Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13992.md")
</aside>
<h2 id="cloudflare-tunnel">Cloudflare Tunnel</h2>
<p>Outbound TLS 1.3 tunnel from <code>cloudflared</code> on a customer origin to Cloudflare's global network.</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>✅ X25519MLKEM768</td>
</tr>
<tr>
<td>Signatures</td>
<td>Not yet</td>
</tr>
</tbody>
</table>
<p>Reference: <a href="https://blog.cloudflare.com/post-quantum-tunnel/">PQ Cloudflare Tunnel</a>, <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/">PQC and Cloudflare One</a>.</p>
<p><strong>Products covered:</strong> <a href="/workers-vpc/">Workers VPC</a> private-network access and any <a href="/cloudflare-one/">Cloudflare One</a> off-ramp that egresses via <code>cloudflared</code> (for example, <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Cloudflare Access</a> self-hosted applications).</p>
<h2 id="cloudflare-one">Cloudflare One</h2>
<p>The sections below cover the connections and services that make up <a href="/cloudflare-one/">Cloudflare One</a>. For an end-to-end walkthrough of how on-ramps and off-ramps fit together, refer to <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/">PQC and Cloudflare One</a>.</p>
<h3 id="cloudflare-one-client">Cloudflare One Client</h3>
<p>MASQUE tunnel (TLS 1.3) from an end-user device to Cloudflare's global network, established by the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> (formerly WARP).</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>✅ X25519MLKEM768</td>
</tr>
<tr>
<td>Signatures</td>
<td>Not yet</td>
</tr>
</tbody>
</table>
<p>Reference: <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/#cloudflare-one-client">PQC and Cloudflare One: Cloudflare One Client</a>.</p>
<p>This connection also serves as a post-quantum on-ramp for traffic that traverses <a href="#cloudflare-gateway">Cloudflare Gateway</a>.</p>
<h3 id="cloudflare-mesh">Cloudflare Mesh</h3>
<p><a href="/mesh/">Cloudflare Mesh</a> provides private IP connectivity between devices and servers using the Cloudflare One Client on each Mesh node and client device.</p>
<p>Mesh inherits its post-quantum protection from the <a href="#cloudflare-one-client">Cloudflare One Client</a> connection, which is used as both the on-ramp and the off-ramp for Mesh traffic.</p>
<h3 id="cloudflare-gateway">Cloudflare Gateway</h3>
<p><a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#post-quantum-support">Cloudflare Gateway</a> is a Secure Web Gateway that runs on Cloudflare's edge and filters HTTPS traffic egressing to the public Internet. Gateway has no client-side component; clients reach Gateway via one of several post-quantum on-ramps:</p>
<ul>
<li>The <a href="#cloudflare-one-client">Cloudflare One Client</a>.</li>
<li>A <a href="#cloudflare-ipsec">Cloudflare IPsec</a> tunnel.</li>
</ul>
<p>The egress leg from Gateway to third-party origin servers is covered by <a href="#cloudflare-to-origin">Cloudflare to origin</a> and is independent of the on-ramp.</p>
<p>Reference: <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/#secure-web-gateway">PQC and Cloudflare One: Secure Web Gateway</a>.</p>
<h3 id="cloudflare-ipsec">Cloudflare IPsec</h3>
<p>IKEv2 key exchange for IPsec tunnels between third-party branch connectors and Cloudflare's global network.</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>✅ ML-KEM-768/1024 + DH Group 20 (P-384) in IKEv2</td>
</tr>
<tr>
<td>Downgrade protection</td>
<td>🚧 <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#downgrade-protection"><code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code></a></td>
</tr>
<tr>
<td>Signatures</td>
<td>Not yet</td>
</tr>
</tbody>
</table>
<p>Reference: <a href="https://blog.cloudflare.com/post-quantum-sase/">PQC SASE</a>, <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability">GRE and IPsec tunnels</a>, <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/">draft-ietf-ipsecme-ikev2-mlkem</a>, <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/">draft-ietf-ipsecme-ikev2-downgrade-prevention</a>.</p>
<p>The IPsec ESP dataplane can alternatively be keyed using the <a href="#cloudflare-one-appliance">Cloudflare One Appliance</a> control plane instead of IKEv2.</p>
<h3 id="cloudflare-one-appliance">Cloudflare One Appliance</h3>
<p>TLS 1.3 control-plane connection used by the <a href="/cloudflare-wan/configuration/appliance/reference/">Cloudflare One Appliance</a> (formerly Magic WAN Connector) to establish keys for its IPsec ESP dataplane tunnels.</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>✅ X25519MLKEM768</td>
</tr>
<tr>
<td>Signatures</td>
<td>Not yet</td>
</tr>
</tbody>
</table>
<p>Reference: <a href="https://blog.cloudflare.com/post-quantum-sase/">PQC SASE</a>, <a href="/cloudflare-wan/configuration/appliance/reference/">Cloudflare One Appliance</a>, <a href="/ssl/post-quantum-cryptography/pqc-and-zero-trust/#cloudflare-ipsec">PQC and Cloudflare One</a>.</p>
<h3 id="cloudflare-email-security">Cloudflare Email Security</h3>
<p>Post-quantum protection applies to inbound and outbound TLS 1.3 SMTP connections between Cloudflare <a href="/cloudflare-one/email-security/">Email Security</a> MX deployments and third-party mail servers:</p>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key agreement</td>
<td>✅ X25519MLKEM768</td>
</tr>
<tr>
<td>Signatures</td>
<td>Not yet</td>
</tr>
</tbody>
</table>
<p>Reference: <a href="/cloudflare-one/email-security/">Email Security</a>, <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/">MX/Inline deployment</a>.</p>
<p>Post-quantum key agreement is negotiated automatically when the remote SMTP peer advertises support (for example, <a href="https://workspace.google.com/">Google Workspace</a>). Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.</p>
<h2 id="contributing">Contributing</h2>
<p>This listing is maintained alongside the rest of the Cloudflare SSL/TLS documentation. If you spot an inaccuracy or have an update after a product announcement, <a href="/style-guide/contributions/">contributions</a> are welcome.</p>
