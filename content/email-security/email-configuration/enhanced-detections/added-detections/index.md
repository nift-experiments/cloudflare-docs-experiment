<p>With <strong>Added Detections</strong>, you can manage various configurations applied at the time of analyzing email traffic.</p>
<p>These settings apply particularly to trusted business partners that your organization may do business with (vendors, external providers, and more).</p>
<h2 id="available-configurations">Available configurations</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Malicious Domain Age</td>
<td>Controls the threshold for a <strong>Malicious</strong> <span class="nb-interactive-component" data-cf-component="GlossaryTooltip"></td>
</tr>
</tbody>
</table>
@markup("md", "content/.markup/bodies/8559.md")
</div> based on domain age. Maximum of 120 days. |
| Suspicious Domain Age                                                                          | Controls the threshold for a **Suspicious** [disposition](/email-security/reference/dispositions-and-attributes/#dispositions) based on domain age. Maximum of 120 days.                                                          |
| Encrypted Attachment Scanning                                                                  | Auto-scans encrypted attachments to detect sophisticated malware campaigns.                                                                                                                                                       |
| Anti-Spam Engine                                                                               | Detects bulk emails or unsolicited commercial emails and marks them with a **Bulk** [disposition](/email-security/reference/dispositions-and-attributes/#dispositions).                                                           |
| Active Fraud Prevention                                                                        | Inspects and assesses new domain traffic that could be launched from third-party partners or similar organizations.                                                                                                               |
| Blank Email Detection                                                                          | Detects emails with blank bodies and assigns a default disposition. You can choose between **Malicious** and **Suspicious** as [dispositions](/email-security/reference/dispositions-and-attributes/#dispositions).               |
| [ACH](https://en.wikipedia.org/wiki/Automated_clearing_house) change from free email detection | Detects payroll inquiries or change requests from free email domains. You can choose between **Malicious** and **Suspicious** as [dispositions](/email-security/reference/dispositions-and-attributes/#dispositions).             |
| HTML attachment email detection                                                                | Detects HTM and HTML attachments in emails. You can choose between **Malicious** and **Suspicious** as [dispositions](/email-security/reference/dispositions-and-attributes/#dispositions).                                       |
<h2 id="access-added-detections">Access Added Detections</h2>
<p>To access <strong>Added Detections</strong> and potentially adjust your settings:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Enhanced Detections</strong> &gt; <strong>Added Detections</strong>.</li>
</ol>
<p>From this view, you can adjust <a href="#available-configurations">various configurations</a>.</p>
