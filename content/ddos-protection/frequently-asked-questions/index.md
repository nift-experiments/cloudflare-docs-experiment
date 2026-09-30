<h2 id="what-is-a-ddos-attack-event">What is a DDoS attack event?</h2>
<p>When Cloudflare's DDoS systems detect and mitigate attacks, they drop, rate-limit, or challenge (as applicable) packets, DNS queries, or HTTP requests, based on the type of attack.</p>
<p>There are three main DDoS mitigation systems:</p>
<ol>
<li>
<p><a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a></p>
<p>a. <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS managed ruleset</a></p>
<p>b. <a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS managed ruleset</a></p>
</li>
<li>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a></p>
</li>
<li>
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a></p>
</li>
</ol>
<p>The DDoS managed ruleset includes many individual rules. Each rule provides the heuristics that instructs the system how to identify DDoS attack traffic. When the DDoS managed ruleset identifies an attack, it will generate a real-time fingerprint to match against the attack traffic, and install an ephemeral mitigation rule to mitigate the attack using that fingerprint.</p>
<p>The start time of the attack is when the mitigation rule is installed. The attack ends when there is no more traffic matching the rule. This is a single DDoS attack event.</p>
<p>A DDoS attack has a start time, end time, and additional attack metadata such as:</p>
<ul>
<li>Attack ID</li>
<li>Attack vector</li>
<li>Mitigating rule</li>
<li>Total bytes and packets</li>
<li>Attack target</li>
<li>Mitigation action</li>
</ul>
<p>This information is used to populate the <a href="/analytics/network-analytics/understand/main-dashboard/#executive-summary">Executive Summary</a> section in the <a href="/analytics/network-analytics/">Network Analytics</a> dashboard.</p>
<p>It can also be retrieved via GraphQL API using the <code>dosdAttackAnalyticsGroups</code> node.</p>
<p>Currently, the concept of a DDoS attack event only exists for the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS managed ruleset</a>. There is no such grouping of individual packets, queries, or HTTP requests for the other systems yet.</p>
<hr />
<h2 id="how-does-cloudflare-protect-against-low-and-slow-ddos-attacks">How does Cloudflare protect against &quot;low and slow&quot; DDoS attacks?</h2>
<p>A <a href="https://www.cloudflare.com/learning/ddos/ddos-low-and-slow-attack/">low and slow DDoS attack</a> is most commonly a non-volumetric attack. The attacker will send a low volume of HTTP requests, and do so slowly. This type of attack aims to be less detectable and slowly exhausts resources.</p>
<p><a href="https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/">Slowloris</a> is a type of low and slow attack where the attacker establishes <a href="/fundamentals/reference/tcp-connections/">TCP connections</a> to the target server, often using HTTP or HTTPS protocols.</p>
<p>In the case of a Slowloris attack, the attacker sends incomplete HTTP header lines, thus never completing the HTTP request. The server waits for the complete request, holding the connection open. The attacker periodically sends additional HTTP header fields or partial lines to keep the connection alive. This can be achieved by sending partial HTTP headers, or using the <code>content-length</code> header to declare a message body size larger than what is actually sent.</p>
<p>The best practice to defend against low and slow attacks is by using an HTTP reverse proxy, such as Cloudflare's <a href="/fundamentals/concepts/how-cloudflare-works/">CDN</a> or <a href="/waf/">WAF</a> service. The reverse proxy acts as a shield. It waits for a full HTTP request before forwarding it to the origin, serving from cache, or applying other actions based on user configuration. You can configure your zone so that requests are buffered by Cloudflare, which will absorb low and slow attacks. Our proxy waits for the full HTTP request before passing it on. To enable buffered requests, refer to <a href="/rules/configuration-rules/settings/#request-body-buffering">Request Body Buffering</a>.</p>
<p>The request will be served from Cloudflare's <a href="/cache/">Cache</a> or <a href="/workers/">Workers</a>, if applicable. If not, it will only be sent to the origin — assuming it was fully completed and has passed WAF checks. So the attack does not exist, similar to TCP Slowloris attacks protection.</p>
<p>Additionally, the reverse proxy will timeout incomplete HTTP requests after a series of <a href="/fundamentals/reference/tcp-connections/#tcp-connections-and-keep-alives">keepalive probes</a>.</p>
<p>There is not a minimum threshold for activation. However, to provide additional security, custom firewall rules check for payload sizes and conducts basic sanity checks to ensure the content looks like what is expected.</p>
<p>The RUDY (R-U-Dead-Yet?) DDoS attack is another type of denial-of-service (DoS) tool that performs slow-rate attacks on targeted servers.</p>
<p>Unlike conventional DDoS attacks that overwhelm servers with a high volume of requests in a short period, RUDY focuses on creating a few prolonged requests. It does this by submitting form data at an extremely slow pace to keep the web server tied up and unavailable to legitimate traffic. This approach makes RUDY attacks difficult to detect, because the traffic can appear legitimate and does not flood the server with requests that would typically trigger conventional DDoS protection mechanisms​​​​​​.</p>
<p>RUDY specifically targets the application layer (Layer 7) of web servers by exploiting the way web forms handle data submission. The attack works by injecting one byte of information into an application <code>POST</code> field at a time, then waiting. This process causes application threads to await the completion of the form submission indefinitely, effectively exhausting the server's resources and preventing it from processing legitimate requests​​​​.</p>
<p>Refer to the <a href="https://www.cloudflare.com/learning/ddos/ddos-attack-tools/r-u-dead-yet-rudy/">learning center</a> for more information on RUDY attacks.</p>
<hr />
<h2 id="how-does-cloudflare-deal-with-ssl-tls-negotiation-attacks-or-floods">How does Cloudflare deal with SSL/TLS negotiation attacks or floods?</h2>
<p>SSL/TLS based attacks such as BEAST, Poodle, and CRIME are mitigated by Cloudflare's TLS settings, configuration, and cipher limitations. Because Cloudflare serves as the HTTP reverse proxy, TLS exhaustion style attacks are mitigated by terminating TLS sessions before passing HTTP requests to origin servers. TLS traffic is not proxied to origin servers without completing a proper TLS handshake. Additionally, our automated DDoS detection and mitigation systems leverage cipher suites, packet fields, HTTP request attributes and metadata, origin health, traffic profiling, Machine Learning models, and threat intelligence to detect and mitigate additional SSL-based attacks.</p>
<hr />
<h2 id="does-cloudflare-use-bgp-flowspec-for-upstream-mitigation">Does Cloudflare use BGP Flowspec for upstream mitigation?</h2>
<p>Yes. Using our anycast network, along with Traffic Manager, Unimog, and Plurimog, we conduct automated traffic engineering to spread the load of traffic (legitimate and attack) to ensure our network is performant, especially during mitigation of large attacks.</p>
<hr />
<h2 id="where-can-i-see-latest-ddos-trends">Where can I see latest DDoS trends?</h2>
<p>Cloudflare publishes quarterly DDoS reports and coverage of significant DDoS attacks. The publications are available on our <a href="https://blog.cloudflare.com/tag/ddos-reports/">blog website</a> and as interactive reports on the <a href="https://radar.cloudflare.com/reports?q=DDoS">Cloudflare Radar Reports website</a>.</p>
<p>Learn more about the <a href="/radar/reference/quarterly-ddos-reports/">methodologies</a> behind these reports.</p>
<p>You can also view <a href="https://radar.cloudflare.com/">Cloudflare Radar</a> for near real-time insights and trends.</p>
<hr />
<h2 id="what-is-the-ping-of-death-ddos-attacks">What is the Ping of Death DDoS attacks?</h2>
<p>The Ping of Death (PoD) attack involves sending malformed or oversized packets to another computer or server, which can cause the system to freeze, crash, or reboot. Packets are pieces of data sent over the Internet, and the Ping of Death takes advantage of the fact that the IP protocol requires packets to be a maximum of 65,535 bytes in size. By sending a packet larger than this size, the attacker can exploit vulnerabilities in the target's TCP/IP stack, causing a buffer overflow and leading to unpredictable behavior, including system crashes. This type of attack is less common nowadays, as most modern systems and networking equipment have been patched to handle such anomalies.</p>
<hr />
<h2 id="what-are-loic-and-hoic">What are LOIC and HOIC?</h2>
<p>LOIC is a popular network stress testing and DoS attack application that is used to flood a server with TCP, UDP, or HTTP requests with the intention of disrupting the service. It is known for its simplicity and ability to be used by individuals with minimal hacking experience. LOIC can be directed by the user to attack a small server, which can cause the server to slow down or crash from the overload of requests. It became famous around 2010 for its use by the hacker group Anonymous in attacks against major companies and organizations.</p>
<p>HOIC is an upgrade from LOIC, designed to overcome some of its limitations, especially in terms of detection and mitigation. It allows users to launch a more powerful DoS attack by enabling attacks on multiple websites at the same time with a higher volume of requests. HOIC also incorporates a feature that makes it more difficult for defense mechanisms to identify and mitigate the attack traffic, partly because it uses a technique that allows the traffic to mimic legitimate HTTP traffic, which is more challenging for traditional network security tools to detect. HOIC supports the use of &quot;booster&quot; scripts that enable it to target various websites simultaneously, significantly increasing its potency as a tool for conducting broad-scale DoS attacks.</p>
<p>These tools and attacks exploit different aspects of network protocols and behaviors to overwhelm targets with unwanted traffic, leading to denial of service. Due to their potential for abuse, their use is illegal and unethical outside of controlled environments for testing purposes.</p>
<hr />
<h2 id="can-i-exclude-specific-user-agents-from-http-ddos-protection">Can I exclude specific user agents from HTTP DDoS protection?</h2>
<p>Yes, you can create an <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/">override</a> and use the expression fields to match against HTTP requests with the user agent. There are a variety of <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/#available-expression-fields">fields</a> that you can use.</p>
<p>You can then adjust the <a href="/ddos-protection/managed-rulesets/http/override-parameters/#sensitivity-level">sensitivity level</a> or <a href="/ddos-protection/managed-rulesets/http/override-parameters/#action">mitigation action</a>.</p>
<p>Refer to the guide on how to <a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/#create-a-ddos-override">create an override</a>.</p>
<p>The use of expression fields is subject to <a href="/ddos-protection/#availability">availability</a>.</p>
<hr />
<h2 id="does-cloudflare-charge-for-ddos-attack-traffic">Does Cloudflare charge for DDoS attack traffic?</h2>
<p>No. Since 2017, Cloudflare offers <a href="https://blog.cloudflare.com/unmetered-mitigation/">free, unmetered, and unlimited DDoS protection</a>. There is no limit to the number of DDoS attacks, their duration, or their size. Cloudflare's billing systems automatically exclude DDoS attack traffic from your usage.</p>
<hr />
<h2 id="how-does-ddos-protection-determine-whether-a-syn-flood-attack-is-mitigated-by-dosd-or-advanced-tcp-protection">How does DDoS Protection determine whether a SYN flood attack is mitigated by <code>dosd</code> or Advanced TCP Protection?</h2>
<p>DDoS <a href="/ddos-protection/managed-rulesets/">managed rules</a> detect and mitigate attacks by finding commonality between attack packets and generating a real-time fingerprint to mitigate the attack.</p>
<p>When the attacks are highly randomized and DDoS managed rules are unable to detect a common pattern among the attack packets, <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> uses its stateful TCP flowtracking capabilities to determine whether or not packets are legitimate. Advanced TCP Protection also mitigates simpler TCP-based attacks.</p>
<p>Advanced TCP Protection is only necessary and available to <a href="/magic-transit/">Magic Transit</a> customers. For <a href="/spectrum/">Spectrum</a> and our HTTP services, we leverage the reverse proxy to mitigate sophisticated randomized TCP-based DDoS attacks.</p>
<hr />
<h2 id="how-does-cloudflare-handle-hyper-localized-ddos-attacks-that-may-aim-to-overwhelm-a-specific-point-of-presence-pop">How does Cloudflare handle hyper-localized DDoS attacks that may aim to overwhelm a specific Point of Presence (PoP)?</h2>
<p>Hyper-localized DDoS attacks are attacks that target specific PoPs or data centers from botnet nodes that are close to those locations in an attempt to overwhelm them and cause an outage or service disruptions.</p>
<p>However, Cloudflare's defense approach is resilient to these attacks and uses a combination of intelligent traffic engineering, global Anycast, and real-time, autonomous DDoS mitigation to handle hyper-localized DDoS attacks — even those that may temporarily exceed the capacity of a specific Point of Presence (PoP).</p>
<h3 id="global-anycast-network">Global Anycast Network</h3>
<p>Anycast allows multiple servers (PoPs) to share the same IP address, and the Border Gateway Protocol (BGP) routing system ensures user traffic is routed to the nearest or lowest-cost node.</p>
<h4 id="process">Process</h4>
<p>When one PoP is overwhelmed due to a local DDoS flood or as a result of limited capacity, BGP route propagation can be adjusted to shift traffic away from that PoP. Cloudflare can also withdraw BGP announcements from specific peers or upstreams to force traffic to reroute through better-equipped PoPs. Because DDoS traffic originates from multiple geographic regions, Anycast and traffic engineering distributes the attack across <a href="https://www.cloudflare.com/network/">Cloudflare's full capacity Anycast network</a> to reduce the burden on a single PoP.</p>
<h3 id="intelligent-traffic-engineering">Intelligent Traffic Engineering</h3>
<p>Cloudflare uses real-time data and intelligence systems to make decisions about traffic routing, load balancing, and congestion management.</p>
<h4 id="process-1">Process</h4>
<p>If a specific PoP becomes saturated or experiences attack traffic, Cloudflare's internal traffic engineering systems dynamically steer traffic across alternative paths using traffic shaping, path-aware routing, and dynamic DNS responses.</p>
<p>The system monitors CPU load, network congestion, and traffic type to make smart decisions about whether to reroute or throttle connections.</p>
<p>For Layer 7 (application-level) attacks, Cloudflare can challenge or rate-limit traffic before it reaches application servers. This scenario is similar to some extent to when we take down certain PoPs for maintenance. This can be done automatically via Traffic Manager, and if needed, by our Site Reliability Engineers (SRE).</p>
<h3 id="real-time-ddos-mitigation">Real-Time DDoS Mitigation</h3>
<p>DDoS managed rules and Advanced DDoS Protection are autonomous and run on every single server independently, while also coordinating locally and globally, contributing to the resilience of each server and PoP. These systems run close to the network edge in every PoP, meaning detection and mitigation happen rapidly, often before any noticeable impact. If traffic exceeds the capacity of one PoP, mitigation rules are replicated to other PoPs to help absorb overflow.</p>
<ul>
<li><strong>DDoS managed rules</strong>: Detects and mitigates DDoS attacks in real-time. When it detects an attack, it deploys rules within seconds to mitigate the malicious traffic.</li>
<li><strong>Advanced TCP Protection</strong>: Identifies and drops abnormal TCP/IP behavior before it hits application servers.</li>
<li><strong>Advanced DNS Protection</strong>: Identifies and drops abnormal DNS queries behavior before it hits DNS servers.</li>
</ul>
<hr />
<h2 id="what-is-advanced-tcp-protection-s-protected-learning-functionality">What is Advanced TCP Protection's Protected Learning functionality?</h2>
<p>The Protected Learning functionality enables the <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> system to overcome Internet routing chaos while allowing your legitimate traffic through and blocking DDoS attacks at the edge.</p>
<p>Anycast and BGP are protocols that help route Internet traffic by sending it to the nearest or most optimal data center. Occasional network events—such as a data center being taken offline for maintenance or changes in Internet routing—can cause an established connection to be rerouted to a different data center.</p>
<p>Cloudflare's flow inference functionality, also known as Protected Learning, is specifically designed to handle this. When a TCP connection, such as a flow, shifts to a new data center, our system observes that it is an existing connection that does not appear in the local flow table. Instead of immediately blocking the flow as an unknown connection that may be part of a DDoS attack, our system uses a proprietary process to verify if the connection is legitimate. It might challenge the acknowledgment (ACK) packets of the flow to ensure it is not part of a DDoS attack. Once the flow passes our checks, we allow it to continue without interruption. This ensures that even rare, legitimate shifts in traffic do not break your long-running connections while keeping your network protected against DDoS attacks.</p>
<hr />
<h2 id="does-ddos-protection-protect-against-email-based-attacks">Does DDoS Protection protect against email-based attacks?</h2>
<p>No. Cloudflare DDoS Protection safeguards web and network infrastructure against DDoS attacks at layers 3, 4, and 7 of the OSI model. This includes TCP, UDP, DNS, and HTTP/S traffic.</p>
<p>DDoS Protection does not inspect or mitigate threats delivered over email protocols such as SMTP, IMAP, or POP3. To protect against email-borne threats such as phishing, business email compromise (BEC), spoofing, and malware delivered via email, use <a href="/email-security/">Cloudflare Email Security</a>.</p>
