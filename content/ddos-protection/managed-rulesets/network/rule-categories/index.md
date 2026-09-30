<p>The main categories (or tags) of Network-layer DDoS Attack Protection managed rules are the following:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gre</code></td>
<td>Rules for DDoS attacks over Generic Routing Encapsulation (GRE) that usually target GRE endpoints.</td>
</tr>
<tr>
<td><code>esp</code></td>
<td>Rules for DDoS attacks related to the Encapsulating Security Payload (ESP) protocol, which is part of the IPsec secure network protocol suite.</td>
</tr>
<tr>
<td><code>advanced</code></td>
<td>Rules related to features available to Enterprise customers, such as <a href="/ddos-protection/managed-rulesets/adaptive-protection/">Adaptive DDoS Protection</a>.</td>
</tr>
<tr>
<td><code>generic</code></td>
<td>Rules for detecting and mitigating floods of packets. These rules are useful for mitigating attacks that have no known signatures, but they may also trigger on unusually high volumes of legitimate traffic. To reduce the risk of false positives, their packet per second (pps) activation threshold is higher. These rules rate-limit traffic by default, but you can override them to block traffic if necessary.</td>
</tr>
<tr>
<td><code>read-only</code></td>
<td></td>
</tr>
</tbody>
</table>
Highly targeted rules for mitigating DDoS attacks with a high confidence rate. These rules are read-only — you cannot override their sensitivity level or action.
                                                                                                                                                                                                                                                                                                                               |
| `test`      | 
Rules used for testing the detection, mitigation, and alerting capabilities of Cloudflare's DDoS protection products.
                                                                                                                                                                                                                                                                                                                                    |
<p>There are other rule categories based on the attack vector/protocol, such as <code>dns</code>, <code>quic</code>, and <code>sip</code>. The categories list is dynamic and may change over time.</p>
