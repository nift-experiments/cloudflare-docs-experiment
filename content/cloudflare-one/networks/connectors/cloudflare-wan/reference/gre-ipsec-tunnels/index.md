<h2 id="tunnels-and-encapsulation">Tunnels and encapsulation</h2>
<p>To route traffic between Cloudflare's global network and your origin network, Cloudflare WAN wraps your original packets inside an outer packet — a process called encapsulation. The outer packet carries your traffic across the Internet to its destination, where it is unwrapped (decapsulated) and delivered.</p>
<p>Cloudflare WAN uses two encapsulation protocols: <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5568.md")
</div> and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5569.md")
</div>. GRE is stateless and simpler to configure but does not encrypt traffic. IPsec encrypts traffic and authenticates the source, providing stronger security. Both create tunnels — logical point-to-point connections between Cloudflare and your network. Cloudflare sets up tunnel endpoints on global network servers inside your network namespace, and you set up tunnel endpoints on routers at your data center.
<p>To accommodate additional header data introduced by encapsulation, you must adjust the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5570.md")
</div> to comply with the standard Internet routable maximum transmission unit (MTU), which is 1500 bytes.
<p>For instructions, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/get-started/#set-maximum-segment-size">Set maximum segment size</a>.</p>
<p>This diagram illustrates the flow of traffic with Cloudflare WAN.</p>
<pre class="mermaid">&#10;&#10;{`sequenceDiagram&#10;accTitle: Tunnels and encapsulation&#10;accDescr: This diagram shows the flow of traffic with Cloudflare WAN.&#10;participant A as Client machine&#10;participant B as Cloudflare Cloudflare WAN&#10;participant C as Origin router&#10;A->>B: Payload <br> Protocol <br> IP header&#10;Note left of A: Ingress <br> traffic&#10;B->>C: Payload <br> Protocol <br> IP header <br> GRE <br> IP header&#10;C->>A: IP header <br> Protocol <br> Payload&#10;Note right of C: Egress <br> traffic`}&#10;&#10;</pre>
<br />
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5567.md")
</aside>
<h2 id="anycast">Anycast</h2>
<p>Traditional tunnels connect two fixed endpoints — one device on each side. Cloudflare WAN uses a different model: <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5571.md")
</div> IP addresses for Cloudflare's tunnel endpoints. In the anycast model, any server in any Cloudflare data center can receive traffic and must be capable of encapsulating and decapsulating packets for any tunnel. This means your tunnel is not tied to a single Cloudflare server — traffic is handled by whichever data center is closest to the source.
<p>This works with <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5572.md")
</div> tunnels because the GRE protocol is stateless. Cloudflare processes each packet independently without requiring any negotiation or coordination between tunnel endpoints. Tunnel endpoints bind to IP addresses but not to specific devices. Any device that can strip off the outer headers and then route the inner packet can handle any GRE packet sent over the tunnel.
<p>For <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5573.md")
</div> tunnels, the customer's router negotiates the creation of an IPsec tunnel with Cloudflare using the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5574.md")
</div> protocol. Because IPsec is stateful (it requires shared keys and session parameters), one Cloudflare server handles the initial negotiation, then propagates the tunnel details (traffic selectors, keys, etc.) across all Cloudflare data centers. The result is that any Cloudflare server can handle traffic for that IPsec tunnel, even though only one server negotiated the setup.
<p>Cloudflare's anycast architecture provides a conduit to your tunnel for every server in every data center on Cloudflare's global network. The following image shows this architecture.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Anycast tunnel&#10;accDescr: Multiple servers in data center preparing packets to send through anycast tunnel.&#10;&#10;a(User)&#10;&#10;subgraph 1&#10;direction LR&#10;b(Cloudflare global &lt;br&gt; network server)&#10;c(Cloudflare global &lt;br&gt; network server)&#10;d(Cloudflare global &lt;br&gt; network server)&#10;e(Cloudflare global &lt;br&gt; network server)&#10;f(Cloudflare global &lt;br&gt; network server)&#10;g(Cloudflare global &lt;br&gt; network server)&#10;h(Cloudflare global &lt;br&gt; network server)&#10;end&#10;&#10;subgraph 2&#10;i(&quot;Acme router &lt;br&gt; 198.51.100.1&quot;)&#10;j(&quot;FTP server &lt;br&gt; (203.0.113.100)&quot;)&#10;end&#10;&#10;subgraph 3&#10;x(&quot;Acme router &lt;br&gt; 198.51.100.1&quot;)&#10;z(&quot;FTP server &lt;br&gt; (203.0.113.100)&quot;)&#10;end&#10;&#10;a --&gt; 1== Cloudflare anycast GRE &lt;br&gt; single endpoint ==&gt;i --&gt; j&#10;&#10;1== Cloudflare anycast IPsec &lt;br&gt; single endpoint ==&gt;x --&gt; z&#10;</code></pre>
<h2 id="ipsec-tunnels">IPsec tunnels</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="post-quantum-ipsec">Post-quantum IPsec</h3>
@markup("md", "content/.markup/bodies/5566.md")
</aside>
<p><a href="https://www.cloudflare.com/learning/network-layer/what-is-ipsec/">IPsec</a> is a group of protocols that work together to set up encrypted connections between devices. It helps keep data you send over public networks secure. Organizations often use IPsec to set up Virtual Private Networks (VPNs), and it works by encrypting IP packets and authenticating the source where the packets come from.</p>
<p>For information on how to set up an IPsec tunnel, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>. To learn more about the configuration parameters Cloudflare WAN uses to create an IPsec tunnel, keep reading.</p>
<h3 id="how-ikev2-establishes-an-ipsec-tunnel">How IKEv2 establishes an IPsec tunnel</h3>
<p>Cloudflare WAN uses the following stages to establish an IPsec tunnel:</p>
<ul>
<li><strong>Initial Exchange</strong> (<code>IKE_SA_INIT</code>): IKE peers negotiate parameters for the IKE Security Association (SA) and establish a shared secret for key derivation, and when relevant, signal support for post-quantum key exchange with <a href="https://datatracker.ietf.org/doc/rfc9370/">RFC 9370</a>. When <a href="#improved-downgrade-protection-beta">downgrade protection</a> is enabled, Cloudflare also sends an <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> notification during this exchange to signal support for full transcript authentication. After this exchange, the peers have a secure communication channel but they have not yet authenticated each other.</li>
<li><strong>Intermediate Exchange</strong> (<code>IKE_INTERMEDIATE</code>): If both peers support RFC 9370, they perform an additional key exchange using ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism), a post-quantum key exchange specified in <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/">draft-ietf-ipsecme-ikev2-mlkem</a>. This creates a hybrid shared secret by combining a secret derived from classical Diffie-Hellman (established during the <code>IKE_SA_INIT</code>) with post-quantum ML-KEM to protect against <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now, decrypt-later</a> attacks.</li>
<li><strong>Auth Exchange</strong> (<code>IKE_AUTH</code>): Using the keys established from both the <code>IKE_SA_INIT</code> and the <code>IKE_INTERMEDIATE</code> exchange, IKE peers mutually authenticate each other. After authentication, they establish the IKE security association (SA). Next, the peers negotiate and establish an IPsec tunnel, known as a Child SA.</li>
<li><strong>Rekeying</strong>: Periodically, or through manual intervention, IKE SAs can be rekeyed to generate new SAs with fresh keys for the session. This rekey operation is performed for both the IKE SA (to refresh the control plane) and the Child SAs (to refresh the data plane). When a hybrid exchange is in use (RFC 9370), the rekey process for the IKE SA will once again perform the parallel classical (DH) and post-quantum (ML-KEM) exchanges to ensure continued quantum resistance.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5565.md")
</aside>
<p>In summary, IKEv2 creates an IKE SA that uses certain cryptographic transforms. It then uses that IKE SA to create a Child SA which itself uses certain cryptographic transforms. The following configuration section details which of these transforms Cloudflare WAN currently supports for IKE SAs and Child SAs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5564.md")
</aside>
<h3 id="supported-configuration-parameters">Supported configuration parameters</h3>
<p>Choose from the following configuration parameters that Cloudflare WAN supports, based on what your appliance supports.</p>
<details class="nb-details"><summary>IKE SA (also known as Phase 1)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5575.md")
</div></details>
<details class="nb-details"><summary>Child SA (also known as Phase 2 or IPsec SA)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5576.md")
</div></details>
<details class="nb-details"><summary>Required configuration parameters</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5577.md")
</div></details>
<details class="nb-details"><summary>Optional configuration parameters</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5578.md")
</div></details>
<h3 id="tested-third-party-vendor-interoperability">Tested third-party vendor interoperability</h3>
<p>The following third-party vendors have been tested and validated to interoperate with Cloudflare IPsec for post-quantum key agreement:</p>
<table>
<thead>
<tr>
<th>Vendor</th>
<th>Product / Version</th>
<th>ML-KEM variant</th>
<th>DH group</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cisco</td>
<td>Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1</td>
<td>ML-KEM-1024</td>
<td>Group 20</td>
<td>Requires RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem support.</td>
</tr>
<tr>
<td>Fortinet</td>
<td>FortiOS 7.6.6+</td>
<td>ML-KEM-768</td>
<td>Group 20</td>
<td>Requires RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem support.</td>
</tr>
<tr>
<td>Fortinet</td>
<td>FortiOS 7.6.6+</td>
<td>ML-KEM-1024</td>
<td>Group 20</td>
<td>Requires RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem support.</td>
</tr>
</tbody>
</table>
<p>Cloudflare continues to test and validate additional third-party devices. If you have successfully configured post-quantum IPsec with a vendor not listed here, contact your account team.</p>
<h3 id="supported-ike-id-formats">Supported IKE ID formats</h3>
<p>Cloudflare WAN supports the following IKE ID types for IPsec:</p>
<details class="nb-details"><summary>Request for Comments (RFC) name �CODE14�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5579.md")
</div></details>
<details class="nb-details"><summary>RFC name �CODE17�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5580.md")
</div></details>
<details class="nb-details"><summary>RFC name �CODE20�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5581.md")
</div></details>
<p>Additionally, Cloudflare supports the IKE ID type of <code>ID_IPV4_ADDR</code> if the following two conditions are met:</p>
<ol>
<li>You set the IPsec tunnel's <code>customer_endpoint</code> value.</li>
<li>The combination of <code>cloudflare_endpoint</code> and <code>customer_endpoint</code> is unique among the customer's IPsec tunnels.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5558.md")
</aside>
<h3 id="route-based-vs-policy-based-vpns">Route-based vs. policy-based VPNs</h3>
<p>Although Cloudflare supports both route-based and policy-based VPNs, we recommend route-based VPNs.</p>
<p>If route-based VPNs are not an option and you must use policy-based VPNs, be aware of the following limitations:</p>
<ul>
<li>Cloudflare only supports a single set of traffic selectors per Child SA.</li>
<li>A policy must cover reply-style health checks — that is, they must match traffic selectors — otherwise, Cloudflare drops them, just like any other traffic from an IPsec tunnel that does not match a policy.</li>
<li>A single IPsec tunnel can only contain around 100 Child SAs. Therefore, there is effectively a limit on the number of different policies per tunnel.</li>
</ul>
<h3 id="improved-downgrade-protection-beta">Improved downgrade protection (beta)</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="beta">Beta</h3>
@markup("md", "content/.markup/bodies/5557.md")
</aside>
<p>IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable <a href="https://www.cloudflare.com/learning/security/threats/on-path-attack/">on-path attacker</a> can exploit this to create a &quot;split view&quot; of the handshake, tricking the endpoints into downgrading a post-quantum connection back to classical cryptography even when both sides support post-quantum key exchange.</p>
<p>To address this, Cloudflare supports the <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/"><code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code></a> IKEv2 extension. When enabled, both IKEv2 peers sign the entire handshake transcript during the authentication exchange, rather than only their own messages. This prevents an attacker from downgrading the connection without being detected.</p>
<p><strong>How it works:</strong></p>
<ul>
<li>When the feature flag is enabled, Cloudflare (acting as IKE responder) unconditionally includes an <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> notification in its <code>IKE_SA_INIT</code> response.</li>
<li>If the initiator also supports the extension, both sides use full transcript authentication, which improves protection again downgrade attacks.</li>
<li>If the initiator does not support the extension, the handshake proceeds with standard IKEv2 authentication. Both parties must support the extension for downgrade protection to be effective.</li>
</ul>
<p><strong>Requirements:</strong></p>
<ul>
<li>Your IKEv2 initiator must support the <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> notification as defined in <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/">draft-ietf-ipsecme-ikev2-downgrade-prevention</a>.</li>
</ul>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>For help resolving tunnel issues:</p>
<ul>
<li><a href="/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Troubleshoot tunnel health</a> - Diagnose and fix health check failures</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/ipsec_logs/">Troubleshoot with IPsec logs</a> - Use Logpush to analyze IPsec handshake issues</li>
</ul>
<h2 id="troubleshooting-1">Troubleshooting</h2>
<p>For help resolving tunnel issues:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a> - Diagnose and fix health check failures</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/ipsec-troubleshoot/">Troubleshoot with IPsec logs</a> - Use Logpush to analyze IPsec handshake issues</li>
</ul>
