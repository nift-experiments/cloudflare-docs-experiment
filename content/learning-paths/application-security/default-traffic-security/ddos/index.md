<p>Cloudflare automatically detects and mitigates DDoS attacks using its <a href="/ddos-protection/about/components/#autonomous-edge">Autonomous Edge</a>, which is always-on. <code>Advanced</code> protections are reserved for Magic Transit customers.</p>
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
@markup("md", "content/.markup/bodies/9628.md")
</div> flood attack<br/>Jenkins amplification attacks<br/>Lantronix reflection attacks<br/>mDNS DDoS attacks<br/>Memcached amplification attacks<br/>Mirai and Mirai-variant L3/4 attacks<br/>MSSQL reflection attacks<br/>NetBios DDoS attacks<br/>Out of state TCP attacks<br/>Protocol violation attacks<br/>QUIC flood attack<br/>Quote of the Day (QOTD) reflection attacks<br/>RST flood<br/>SIP attacks<br/>SNMP flood attack<br/>SPSS reflection attacks<br/>SSDP reflection attacks<br/>SYN floods<br/>SYN-ACK reflection attack<br/>TeamSpeak 3 floods<br/>Ubiquity reflection attacks<br/>UDP flood attack<br/>VxWorks DDoS attacks<br/><br/>For more DNS protection options, refer to [Getting additional DNS protection](/ddos-protection/about/attack-coverage/#getting-additional-dns-protection). |
| L3/4            | [Advanced TCP Protection](/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/) <sup><a href="#footnote-ddos-protection-ddos-attack-coverage-mdx-1">1</a></sup>               | Fully randomized and spoofed ACK floods, SYN floods, SYN-ACK reflection attacks, and other sophisticated TCP-based DDoS attacks                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| L7 (DNS)        | [Advanced DNS Protection](/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/) <sup><a href="#footnote-ddos-protection-ddos-attack-coverage-mdx-1">1</a></sup>               | Sophisticated and fully randomized DNS attacks, including Water Torture attacks, Random-prefix attacks, and DNS laundering attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| L7 (HTTP/S)     | [HTTP DDoS Attack Protection](/ddos-protection/managed-rulesets/http/)                                                 | Cache busting attacks<br/>Carpet Bombing attacks<br/>HTTP Continuation flood<br/>HTTP flood attack<br/>HTTP/2 MadeYouReset<br/>HTTP/2 Rapid Reset<br/>HULK attack<br/>Known DDoS botnets<br/>LOIC attack<br/>Mirai and Mirai-variant HTTP attacks<br/>Slowloris attack<br/>TLS/SSL exhaustion attacks<br/>TLS/SSL negotiation attacks<br/>WordPress pingback attack<br/>                                                                                                                                                                                                                                                  |
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-ddos-protection-ddos-attack-coverage-mdx-1">Available to Magic Transit customers.</li></ol></section>
<p>Refer to the learning path <a href="/learning-paths/prevent-ddos-attacks/concepts/">Prevent DDoS attacks</a>  to dive deeper into this subject.</p>
