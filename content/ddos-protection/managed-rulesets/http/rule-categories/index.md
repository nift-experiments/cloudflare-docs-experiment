<p>The main categories (or tags) of HTTP DDoS Attack Protection managed rules are the following:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>botnets</code></td>
<td>Rules for requests from known botnets, with very high accuracy and low risk of false positives. It is recommended that you keep these rules enabled.</td>
</tr>
<tr>
<td><code>unusual-requests</code></td>
<td>Rules for requests with suspicious characteristics that are not usually seen in legitimate traffic.</td>
</tr>
<tr>
<td><code>advanced</code></td>
<td>Rules related to features available to Advanced DDoS Protection customers, such as <a href="/ddos-protection/managed-rulesets/adaptive-protection/">Adaptive DDoS Protection</a>.</td>
</tr>
<tr>
<td><code>generic</code></td>
<td>Rules for detecting and mitigating floods of requests. These rules are useful for mitigating attacks that have no known signatures, but they may also trigger on unusually high volumes of legitimate traffic. To reduce the risk of false positives, their request per second (rps) activation threshold is higher. These rules either rate-limit or challenge traffic by default, but you can override them to block traffic if necessary.</td>
</tr>
<tr>
<td><code>read-only</code></td>
<td></td>
</tr>
</tbody>
</table>
Highly targeted rules for mitigating DDoS attacks with a high confidence rate. These rules are read-only — you cannot override their sensitivity level or action.
                                                                                                                                                                                                                                                                                                                                                     |
| `test`             | 
Rules used for testing the detection, mitigation, and alerting capabilities of Cloudflare's DDoS protection products.
                                                                                                                                                                                                                                                                                                                                                          |
