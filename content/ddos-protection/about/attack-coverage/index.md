<p>The <a href="/ddos-protection/managed-rulesets/">DDoS Attack Protection managed rulesets</a> provide protection against a variety of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7478.md")
</div> across L3/4 (layers 3/4) and L7 of the OSI model. Cloudflare constantly updates these managed rulesets to improve the attack coverage, increase the mitigation consistency, cover new and emerging threats, and ensure cost-efficient mitigations.
<p><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a>, <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a>, and <a href="/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/">Programmable Flow Protection</a> are available to Magic Transit customers. Advanced TCP Protection provides additional protection against sophisticated TCP-based DDoS attacks. Advanced DNS Protections protects against sophisticated and fully randomized DNS attacks. Programmable Flow Protection mitigates UDP-based attacks by executing a customer-defined program.</p>
<p>As a general guideline, various Cloudflare products operate on different open systems interconnection (OSI) layers and you are protected up to the layer on which your service operates. You can customize the DDoS settings on the layer in which you onboarded. For example, since the CDN/WAF service is a Layer 7 (HTTP/HTTPS) service, Cloudflare provides protection from DDoS attacks on L7 downwards, including L3/4 attacks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7477.md")
</aside>
<p>The following table includes a sample of covered attack vectors:</p>
<table>
<thead>
<tr>
<th>OSI Layer</th>
<th>Ruleset / Feature</th>
<th>Example of covered DDoS attack vectors</th>
</tr>
</thead>
<tbody>
<tr>
<td>L3/4</td>
<td><a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection</a></td>
<td>ACK floods<br/>BitTorrent reflection attack<br/>Carpet Bombing attacks<br/>CHARGEN reflection attacks<br/>DNS amplification attack<br/>DNS Garbage Flood<br/>DNS NXDOMAIN flood<br/>DNS Query flood<br/>DTLS amplification attacks<br/>ESP flood<br/>GRE floods<br/><span class="nb-interactive-component" data-cf-component="GlossaryTooltip"></td>
</tr>
</tbody>
</table>
@markup("md", "content/.markup/bodies/7479.md")
</div> flood attack<br/>Jenkins amplification attacks<br/>Lantronix reflection attacks<br/>mDNS DDoS attacks<br/>Memcached amplification attacks<br/>Mirai and Mirai-variant L3/4 attacks<br/>MSSQL reflection attacks<br/>NetBios DDoS attacks<br/>Out of state TCP attacks<br/>Protocol violation attacks<br/>QUIC flood attack<br/>Quote of the Day (QOTD) reflection attacks<br/>RST flood<br/>SIP attacks<br/>SNMP flood attack<br/>SPSS reflection attacks<br/>SSDP reflection attacks<br/>SYN floods<br/>SYN-ACK reflection attack<br/>TeamSpeak 3 floods<br/>Ubiquity reflection attacks<br/>UDP flood attack<br/>VxWorks DDoS attacks<br/><br/>For more DNS protection options, refer to [Getting additional DNS protection](/ddos-protection/about/attack-coverage/#getting-additional-dns-protection). |
| L3/4            | [Advanced TCP Protection](/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/) <sup><a href="#footnote-ddos-protection-ddos-attack-coverage-mdx-1">1</a></sup>               | Fully randomized and spoofed ACK floods, SYN floods, SYN-ACK reflection attacks, and other sophisticated TCP-based DDoS attacks                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| L7 (DNS)        | [Advanced DNS Protection](/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/) <sup><a href="#footnote-ddos-protection-ddos-attack-coverage-mdx-1">1</a></sup>               | Sophisticated and fully randomized DNS attacks, including Water Torture attacks, Random-prefix attacks, and DNS laundering attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| L7 (HTTP/S)     | [HTTP DDoS Attack Protection](/ddos-protection/managed-rulesets/http/)                                                 | Cache busting attacks<br/>Carpet Bombing attacks<br/>HTTP Continuation flood<br/>HTTP flood attack<br/>HTTP/2 MadeYouReset<br/>HTTP/2 Rapid Reset<br/>HULK attack<br/>Known DDoS botnets<br/>LOIC attack<br/>Mirai and Mirai-variant HTTP attacks<br/>Slowloris attack<br/>TLS/SSL exhaustion attacks<br/>TLS/SSL negotiation attacks<br/>WordPress pingback attack<br/>                                                                                                                                                                                                                                                  |
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-ddos-protection-ddos-attack-coverage-mdx-1">Available to Magic Transit customers.</li></ol></section>
<h2 id="getting-additional-dns-protection">Getting additional DNS protection</h2>
<p>The Network-layer DDoS Attack Protection managed ruleset provides protection against some types of DNS attacks.</p>
<p>Magic Transit customers have access to <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a> <span class="nb-badge">Beta</span>. Other customers might consider the following options:</p>
<ul>
<li>Use Cloudflare as your authoritative DNS provider (<a href="/dns/zone-setups/full-setup/">primary DNS</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary DNS</a>).</li>
<li>If you are running your own <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/7480.md")
</div>, use [DNS Firewall](/dns/dns-firewall/) to get additional protection against DNS attacks like random prefix attacks.
<h2 id="email-based-attacks">Email-based attacks</h2>
<p>DDoS Protection covers web and network protocols, including TCP, UDP, DNS, and HTTP/S. It does not cover email protocols such as SMTP, IMAP, or POP3.</p>
<p>For protection against email-borne threats such as phishing and malware, refer to <a href="/email-security/">Email Security</a>.</p>
