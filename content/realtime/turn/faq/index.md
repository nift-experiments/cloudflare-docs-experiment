<h2 id="general">General</h2>
<h3 id="what-is-cloudflare-realtime-turn-pricing-how-exactly-is-it-calculated">What is Cloudflare Realtime TURN pricing? How exactly is it calculated?</h3>
<p>Cloudflare TURN pricing is based on the data sent from the Cloudflare edge to the TURN client, as described in <a href="https://datatracker.ietf.org/doc/html/rfc8656#fig-turn-model">RFC 8656 Figure 1</a>. This means data sent from the TURN server to the TURN client and captures all data, including TURN overhead, following successful authentication.</p>
<p>Pricing for Cloudflare Realtime TURN service is $0.05 per GB of data used.</p>
<p>Cloudflare's STUN service at <code>stun.cloudflare.com</code> is free and unlimited.</p>
<p>There is a free tier of 1,000 GB before any charges start. Cloudflare Realtime billing appears as a single line item on your Cloudflare bill, covering both SFU and TURN.</p>
<p>Traffic between Cloudflare Realtime TURN and Cloudflare Realtime SFU or Cloudflare Stream (WHIP/WHEP) does not incur any charges.</p>
<div class="full-img">
<pre><code class="language-mermaid">&#45;--&#10;title: Cloudflare Realtime TURN pricing&#10;&#45;--&#10;flowchart LR&#10;    Client[TURN Client]&#10;    Server[TURN Server]&#10;&#10;    Client --&gt;|&quot;Ingress (free)&quot;| Server&#10;    Server --&gt;|&quot;Egress (charged)&quot;| Client&#10;&#10;    Server &lt;--&gt;|Not part of billing| PeerA[Peer A]&#10;</code></pre>
</div>
<h3 id="is-realtime-turn-hipaa-gdpr-fedramp-compliant">Is Realtime TURN HIPAA/GDPR/FedRAMP compliant?</h3>
<p>Please view Cloudflare's <a href="https://www.cloudflare.com/trust-hub/compliance-resources/">certifications and compliance resources</a> and contact your Cloudflare enterprise account manager for more information.</p>
<h3 id="is-cloudflare-realtime-turn-fips-140-3-compliant">Is Cloudflare Realtime TURN FIPS 140-3 compliant?</h3>
<p>Cloudflare Realtime TURN supports FIPS 140-3 when encryption is used, such as TURN over TLS. TURN itself does not have any control over the encryption of the data flowing underneath the TURN data layer. For end-to-end encryption of the relayed media or data, the layer above TURN must provide that encryption (for example, DTLS when TURN is used with WebRTC).</p>
<h3 id="what-regions-does-cloudflare-realtime-turn-operate-at">What regions does Cloudflare Realtime TURN operate at?</h3>
<p>Cloudflare Realtime TURN server runs on <a href="https://www.cloudflare.com/network">Cloudflare's global network</a> - a growing global network of thousands of machines distributed across hundreds of locations, with the notable exception of the Cloudflare's <a href="/china-network/">China Network</a>.</p>
<h3 id="what-is-the-difference-between-cloudflare-realtime-turn-with-a-enterprise-plan-vs-self-serve-pay-with-your-credit-card-plans">What is the difference between Cloudflare Realtime TURN with a enterprise plan vs self-serve (pay with your credit card) plans?</h3>
<p>There is no performance or feature level difference for Cloudflare Realtime TURN service in enterprise or self-serve plans, however those on <a href="https://www.cloudflare.com/enterprise/">enterprise plans</a> will get the benefit of priority support, predictable flat-rate pricing and SLA guarantees.</p>
<h3 id="does-cloudflare-realtime-turn-run-in-the-cloudflare-china-network">Does Cloudflare Realtime TURN run in the Cloudflare China Network?</h3>
<p>Cloudflare's <a href="/china-network/">China Network</a> does not participate in serving Realtime traffic and TURN traffic from China will connect to Cloudflare locations outside of China.</p>
<h3 id="how-long-does-it-take-for-turn-activity-to-be-available-in-analytics">How long does it take for TURN activity to be available in analytics?</h3>
<p>TURN usage shows up in analytics in 30 seconds.</p>
<h2 id="architecture-and-use-cases">Architecture and use cases</h2>
<h3 id="what-data-can-cloudflare-access-when-turn-is-used-with-webrtc">What data can Cloudflare access when TURN is used with WebRTC?</h3>
<p>When Cloudflare Realtime TURN is used in conjunction with WebRTC, Cloudflare cannot access the contents of the media being relayed. This is because WebRTC employs Datagram Transport Layer Security (DTLS) encryption for all media streams, which encrypts the data end-to-end between the communicating peers before it reaches the TURN server. As a result, Cloudflare only relays encrypted packets and cannot decrypt or inspect the media content, which may include audio, video, or data channel information.</p>
<p>From a data privacy perspective, the only information Cloudflare processes to operate the TURN service is the metadata necessary for establishing and maintaining the relay connection. This includes IP addresses of the TURN clients, port numbers, and session timing information. Cloudflare does not have access to any personally identifiable information contained within the encrypted media streams themselves.</p>
<p>This architecture ensures that media communications relayed through Cloudflare Realtime TURN maintain end-to-end encryption between participants, with Cloudflare functioning solely as an intermediary relay service without visibility into the encrypted content.</p>
<h3 id="is-realtime-turn-end-to-end-encrypted">Is Realtime TURN end-to-end encrypted?</h3>
<p>TURN protocol, <a href="https://datatracker.ietf.org/doc/html/rfc8656">RFC 8656</a>, does not discuss encryption beyond wrapper protocols such as TURN over TLS. If you are using TURN with WebRTC will encrypt data at the WebRTC level.</p>
<h3 id="does-cloudflare-realtime-turn-use-the-cloudflare-backbone-or-is-there-any-magic-cloudflare-do-to-speed-connection-up">Does Cloudflare Realtime TURN use the Cloudflare Backbone or is there any &quot;magic&quot; Cloudflare do to speed connection up?</h3>
<p>Cloudflare Realtime TURN allocations are homed in the nearest available Cloudflare data center to the TURN client via anycast routing. If both ends of a connection are using Cloudflare Realtime TURN, Cloudflare will be able to control the routing and, if possible, route TURN packets through the Cloudflare backbone.</p>
<h3 id="when-should-i-use-turn-versus-sfu">When should I use TURN versus SFU?</h3>
<p>TURN and SFU solve different problems and are often used together.</p>
<p>Use TURN when you have a point-to-point connection between two peers and you need to traverse NATs or firewalls. Both peers exchange media directly through the relay without any server-side media processing.</p>
<p>Use SFU when you need fan-out, meaning one publisher sending media to many subscribers, or many publishers exchanging media in a group. The SFU forwards selected media streams between participants and supports features like simulcast and subscriber-side track selection.</p>
<p>If your use case is one-to-one communication, such as a teleoperation link between an operator and a remote device, TURN by itself is usually sufficient. Adding an SFU is unnecessary complexity for that topology.</p>
<h3 id="is-there-overhead-to-using-sfu-compared-to-forcing-turn-relay-on-every-connection">Is there overhead to using SFU compared to forcing TURN relay on every connection?</h3>
<p>No. Cloudflare Realtime TURN and SFU run on the same fleet of machines on Cloudflare's global network and share the same data path. There is no meaningful latency or throughput penalty for choosing one over the other.</p>
<p>The decision should be driven by topology, not performance:</p>
<ul>
<li>Use TURN for point-to-point relay.</li>
<li>Use SFU when you need fan-out, group calls, or selective forwarding of tracks.</li>
</ul>
<h3 id="if-only-one-peer-connects-through-turn-will-latency-be-the-same-as-when-both-peers-relay-through-turn">If only one peer connects through TURN, will latency be the same as when both peers relay through TURN?</h3>
<p>Not necessarily. When both peers relay through Cloudflare Realtime TURN, the traffic between the two Cloudflare edges can use the Cloudflare backbone, which means Cloudflare controls the path end to end. When only one peer uses TURN, the other leg traverses the public Internet, and latency and packet loss depend on the interconnect between that peer and the nearest Cloudflare data center.</p>
<p>The more consistent improvement from using TURN on both ends is reliability and packet loss behavior, not raw latency. Backbone latency is typically better than the public Internet, but the size of the latency improvement varies by geography. The reduction in packet loss is generally more predictable.</p>
<h3 id="can-i-use-cloudflare-realtime-turn-for-robotics-and-teleoperation">Can I use Cloudflare Realtime TURN for robotics and teleoperation?</h3>
<p>Yes. Cloudflare Realtime TURN is a good fit for robotics teleoperation, remote vehicle control, and fleet management workloads that require low-latency, two-way media or data channels between an operator and a remote device.</p>
<p>Teleoperation typically uses TURN in point-to-point mode, with one end on the operator's network and the other on the robot's cellular or wired uplink. WebRTC and DTLS provide end-to-end encryption of the media stream, and Cloudflare Realtime TURN handles NAT traversal and relay between the two endpoints. When both endpoints connect through TURN, traffic between Cloudflare edges can ride the Cloudflare backbone, which improves packet loss characteristics on long-distance links.</p>
<p>For workloads that need to fan out a robot's telemetry or camera feed to multiple subscribers (for example, an operator, a supervisor, and a fleet dashboard), Cloudflare Realtime SFU can be used in addition to TURN. Cloudflare's Media over QUIC (MoQ) implementation is also worth evaluating for telemetry and teleoperation when you control both ends of the connection, since it gives you more explicit control over reliability and retransmission behavior than WebRTC.</p>
<h2 id="technical">Technical</h2>
<h3 id="i-need-to-allowlist-whitelist-cloudflare-realtime-turn-ip-addresses-which-ip-addresses-should-i-use">I need to allowlist (whitelist) Cloudflare Realtime TURN IP addresses. Which IP addresses should I use?</h3>
<p>Cloudflare Realtime TURN is easy to use by IT administrators who have strict firewalls because it requires very few IP addresses to be allowlisted compared to other providers. You must allowlist both IPv6 and IPv4 addresses.</p>
<p>Please allowlist the following IP addresses:</p>
<ul>
<li><code>2a06:98c1:3200::1/128</code></li>
<li><code>2606:4700:48::1/128</code></li>
<li><code>141.101.90.1/32</code></li>
<li><code>162.159.207.1/32</code></li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="watch-for-ip-changes">Watch for IP changes</h3>
@markup("md", "content/.markup/bodies/11568.md")
</aside>
<h3 id="i-would-like-to-hardcode-ip-addresses-used-for-turn-in-my-application-to-save-a-dns-lookup">I would like to hardcode IP addresses used for TURN in my application to save a DNS lookup</h3>
<p>Although this is not recommended, we understand there is a very small set of circumstances where hardcoding IP addresses might be useful. In this case, you must set up alerting that detects changes the DNS response from <code>turn.cloudflare.com</code> (A and AAAA records) and update the hardcoded IP address(es) accordingly within 14 days of the DNS change. Note that this DNS response could return more than one IP address. In addition, you must set up a failover to a DNS query if there is a problem connecting to the hardcoded IP address. Cloudflare tries to, but cannot guarantee that the IP address used for the TURN service won't change unless this is in your enterprise contract. For more details about static IPs, guarantees and other arrangements please discuss with your enterprise account team.</p>
<h3 id="i-see-that-turn-ip-are-published-above-do-you-also-publish-ips-for-stun">I see that TURN IP are published above. Do you also publish IPs for STUN?</h3>
<p>TURN service at <code>turn.cloudflare.com</code> will also respond to binding requests (&quot;STUN requests&quot;).</p>
<h3 id="does-cloudflare-realtime-turn-support-the-expired-ietf-rfc-draft-draft-uberti-behave-turn-rest-00">Does Cloudflare Realtime TURN support the expired IETF RFC draft &quot;draft-uberti-behave-turn-rest-00&quot;?</h3>
<p>The Cloudflare Realtime credential generation function returns a JSON structure similar to the <a href="https://datatracker.ietf.org/doc/html/draft-uberti-behave-turn-rest-00">expired RFC draft &quot;draft-uberti-behave-turn-rest-00&quot;</a>, but it does not include the TTL value. If you need a response in this format, you can modify the JSON from the Cloudflare Realtime credential generation endpoint to the required format in your backend server or Cloudflare Workers.</p>
<h3 id="i-am-observing-packet-loss-when-using-cloudflare-realtime-turn-how-can-i-debug-this">I am observing packet loss when using Cloudflare Realtime TURN - how can I debug this?</h3>
<p>Packet loss is normal in UDP and can happen occasionally even on reliable connections. However, if you observe systematic packet loss, consider the following:</p>
<ul>
<li>Are you sending or receiving data at a high rate (&gt;50-100Mbps) from a single TURN client? Realtime TURN might be dropping packets to signal you to slow down.</li>
<li>Are you sending or receiving large amounts of data with very small packet sizes (high packet rate &gt; 5-10kpps) from a single TURN client? Cloudflare Realtime might be dropping packets.</li>
<li>Are you sending packets to new unique addresses at a high rate resembling to <a href="https://en.wikipedia.org/wiki/Port_scanner">port scanning</a> behavior?</li>
</ul>
<h3 id="i-plan-to-use-realtime-turn-at-scale-what-is-the-rate-at-which-i-can-issue-credentials">I plan to use Realtime TURN at scale. What is the rate at which I can issue credentials?</h3>
<p>There is no defined limit for credential issuance. Start at 500 credentials/sec and scale up linearly. Ensure you use more than 50% of the issued credentials.</p>
<h3 id="what-is-the-maximum-value-i-can-use-for-turn-credential-expiry-time">What is the maximum value I can use for TURN credential expiry time?</h3>
<p>You can set a expiration time for a credential up to 48 hours in the future. If you need your TURN allocation to last longer than this, you will need to <a href="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/setConfiguration">update</a> the TURN credentials.</p>
<h3 id="does-realtime-turn-support-ipv6">Does Realtime TURN support IPv6?</h3>
<p>Yes. Cloudflare Realtime is available over both IPv4 and IPv6 for TURN Client to TURN server communication, however it does not issue relay addresses in IPv6 as described in <a href="https://datatracker.ietf.org/doc/html/rfc6156">RFC 6156</a>.</p>
<h3 id="does-realtime-turn-issue-ipv6-relay-addresses">Does Realtime TURN issue IPv6 relay addresses?</h3>
<p>No. Realtime TURN will not respect <code>REQUESTED-ADDRESS-FAMILY</code> STUN attribute if specified and will issue IPv4 addresses only.</p>
<h3 id="does-realtime-turn-support-tcp-relaying">Does Realtime TURN support TCP relaying?</h3>
<p>No. Realtime does not implement <a href="https://datatracker.ietf.org/doc/html/rfc6062">RFC6062</a> and will not respect <code>REQUESTED-TRANSPORT</code> STUN attribute.</p>
<h3 id="i-am-unable-to-make-createpermission-or-channelbind-requests-with-certain-ip-addresses-why-is-that">I am unable to make CreatePermission or ChannelBind requests with certain IP addresses. Why is that?</h3>
<p>Cloudflare Realtime denies CreatePermission or ChannelBind requests if private IP ranges (e.g loopback addresses, linklocal unicast or multicast blocks) or IP addresses that are part of <a href="/byoip/">BYOIP</a> are used.</p>
<p>If you are a Cloudflare BYOIP customer and wish to connect to your BYOIP ranges with Realtime TURN, please reach out to your account manager for further details.</p>
<h3 id="what-is-the-maximum-duration-limit-for-a-turn-allocation">What is the maximum duration limit for a TURN allocation?</h3>
<p>There is no maximum duration limit for a TURN allocation. Per <a href="https://datatracker.ietf.org/doc/html/rfc8656#section-3.2">RFC 8656 Section 3.2</a>, once a relayed transport address is allocated, a client must keep the allocation alive. To do this, the client periodically sends a Refresh request to the server. The Refresh request needs to be authenticated with a valid TURN credential. The maximum duration for a credential is 48 hours. If a longer allocation is required, a new credential must be generated at least every 48 hours.</p>
<h3 id="how-often-does-cloudflare-perform-maintenance-on-a-server-that-is-actively-handling-a-turn-allocation-what-is-the-impact-of-this">How often does Cloudflare perform maintenance on a server that is actively handling a TURN allocation? What is the impact of this?</h3>
<p>Even though this is not common, in certain scenarios TURN allocations may be disrupted. This could be caused by maintenance on the Cloudflare server handling the allocation or could be related to Internet network topology changes that cause TURN packets to arrive at a different Cloudflare datacenter. Regardless of the reason, <a href="https://datatracker.ietf.org/doc/html/rfc8445#section-2.4">ICE restart</a> support by clients is highly recommended.</p>
<h3 id="what-will-happen-if-turn-credentials-expire-while-the-turn-allocation-is-in-use">What will happen if TURN credentials expire while the TURN allocation is in use?</h3>
<p>Cloudflare Realtime will immediately stop billing and recording usage for analytics. After a short delay, the connection will be disconnected.</p>
