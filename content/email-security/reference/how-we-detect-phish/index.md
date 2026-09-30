<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8466.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8465.md")
</aside>
<p>Email Security (formerly Area 1) uses a variety of factors to determine whether a given email message, a web domain or URL, or specific network traffic is part of a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8467.md")
</div> campaign (marked with a `Malicious` <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8468.md")
</div>) or other common campaigns (for example, `Spam`).
<p>These small pattern assessments are dynamic in nature and — in many cases — no single one in and of itself will determine the final verdict. Instead, our automated systems use a combination of factors and non-factors to clearly distinguish between a valid phishing campaign and benign traffic.</p>
<h2 id="activesensors">ActiveSensors</h2>
<p>ActiveSensors is a proprietary sensor network that discovers emergent campaign infrastructure, and aggregates attack data from relay points that actors use to launch their threat campaign. Cloudflare's <a href="/directory/?product-group=Network+security">Network</a> and <a href="/directory/?product-group=Application+security">Application Security</a> provide early detection on phishing attacks, malware, URLs, domains, IPs, and ASNs from across the Internet.</p>
<p>ActiveSensors does the following:</p>
<ul>
<li>Infrastructure monitoring, clustering and correlation.</li>
<li>User and target impersonation-based crawls.</li>
<li>Machine learning based link analysis and content detection.</li>
<li>Payload analysis, in-the-wild sandboxing, content denotation, and reconstruction.</li>
</ul>
<h2 id="sparse-small-pattern-analytics-engine">SPARSE (Small Pattern Analytics Engine)</h2>
<p>SPARSE is a proprietary analytics engine which determines targeted attacks. SPARSE uses the ActiveSensors network, our 8+ petabyte data warehouse, and AI and ML models to make effective detections with a limited data set.</p>
<h2 id="ip-reputation">IP reputation</h2>
<p>IP reputation is just one of many factors to consider but is not consistently accurate due to the dynamic nature of phishing campaigns.</p>
<p>For example, a particular sender IP in a Comcast range might have a mix of good and bad reputation. Flagging it purely on IP would subject a larger chunk of Comcast's IP address range to detections which could lead to false positives.</p>
<h2 id="sample-attack-types-and-detections">Sample attack types and detections</h2>
<table>
<thead>
<tr>
<th>Attack type</th>
<th>Example</th>
<th>Detections applied</th>
</tr>
</thead>
<tbody>
<tr>
<td>Malicious payload attached to the message</td>
<td>Classic campaign technique which utilizes a variety of active attachment types (EXE, DOC, XLS, PPT, OLE, PDF, and more) as the malicious payload for ransomware attacks, Trojans, viruses, and malware.</td>
<td>Machine learning (ML) models on binary bitmaps of the payload as well as higher-level attributes of the payload, with specific focus on signatureless detections for maximum coverage. Additionally, for relevant active payloads, the engine invokes a real-time sandbox to assess behavior and determine maliciousness.</td>
</tr>
<tr>
<td>Encrypted malicious payload attached to the message, with password in message body as text</td>
<td>Campaigns that induce the user to apply a password within the message body to the attachment.</td>
<td>Real-time lexical parsing of message body for password extraction and ML models on binary bitmaps of the payload, signatureless detections for maximum coverage.</td>
</tr>
<tr>
<td>Encrypted malicious payload attached to the message, with password in message body as an image</td>
<td>Campaigns that induce the user to apply a password within the message body to the attachment, with the entire body or part of the body being an image.</td>
<td>Real-time OCR parsing of message body for password extraction and ML models on binary bitmaps of the payload, signatureless detections for maximum coverage.</td>
</tr>
<tr>
<td>Malicious payload within an archive attached to the message</td>
<td>Campaigns with payloads within typical archives, such as <code>.zip</code> files.</td>
<td>ML detection tree on the payload, as well as decomposition of each individual archive into component parts and fragments for compound documents.</td>
</tr>
<tr>
<td>Malicious URLs within message body</td>
<td>Typical phish campaigns with a socially engineered call to action URL that will implant malware (for example, Watering Hole attacks, Malvertizing, or scripting attacks).</td>
<td>Continuous web crawling, followed by real-time link crawling for a select group of suspicious urls, followed by machine learning applied to URL patterns in combination with other pattern rules and topic-based machine learning models for exhaustive coverage of link-based attacks.</td>
</tr>
<tr>
<td>Malicious payload linked through a URL in a message</td>
<td>Campaigns where the URL links through to a remote malicious attachment (for example, in a <code>.doc</code> or <code>.pdf</code> file)</td>
<td>Remote document and/or attachment extraction followed by ML detection tree on the payload, instant crawl of links.</td>
</tr>
<tr>
<td>Blind URL campaigns</td>
<td>Entirely new domain with intentional obfuscation, seen for the first time in a campaign.</td>
<td>Link structure analysis, link length analysis, domain age analysis, neural net models on entire URL as well as domain and IP reputation of URL host, including autonomous system name reputation and geolocation based reputation.</td>
</tr>
<tr>
<td>Malicious URLs within a benign attachment in the message</td>
<td>Campaigns obfuscating the payload within attachments.</td>
<td>URL extraction within attachments, followed by above mentioned URL detection mechanisms.</td>
</tr>
<tr>
<td>Malicious URLs within an archive attached to the message</td>
<td>Campaigns obfuscating the payload within attachments.</td>
<td>Attachments decomposed recursively (both in archive formats and compound document formats) to extract URLs, followed by above mentioned URL detection mechanisms.</td>
</tr>
<tr>
<td>Malicious URLs behind URL shortening services</td>
<td>Campaigns leveraging Bitly, Owly, and similar services at multiple levels of redirection to hide the target URL.</td>
<td>URL shorteners crawled in real time at the moment of message delivery to get to the eventual target URL, followed by URL detection methods. Real-time shorterners are intentionally not crawled ahead of time due to the dynamic nature of these services and the variation of target URLs based on time and source.</td>
</tr>
<tr>
<td>Malicious URLs associated with QR codes (QR Code Phishing Attacks, Quishing)</td>
<td>Campaigns leveraging QR code image attachment to deliver malicious payload links for malware distribution and/or credential harvesting.</td>
<td>Resolving for images resembling QR codes into URL, followed by above mentioned URL detection mechanisms.</td>
</tr>
<tr>
<td>Instant crawl of URLs within message body</td>
<td>Typical phish campaigns with a socially engineered call to action URL that will implant a malware (for example, Watering Hole attacks, Malvertizing, or scripting attacks).</td>
<td>Heuristics applied to URLs in message bodies that are not already detected from ahead of time crawling and those deemed suspicious according to strict criteria are crawled in real time.</td>
</tr>
<tr>
<td>Credential Harvesters</td>
<td>Form-based credential submission attacks, leveraging known brands (Office 365, PayPal, Dropbox, Google, and more).</td>
<td>Continuous web crawling, computer vision on top brand lures, ML models, and infrastructure association.</td>
</tr>
<tr>
<td>Domain Spoof Attacks</td>
<td>Campaigns spoofing sender domains to refer to the recipient domain or some known partner domain.</td>
<td>Header mismatches, email authentication assessments, sender reputation analysis, homographic analysis, and punycode manipulation assessments.</td>
</tr>
<tr>
<td>Domain proximity attacks</td>
<td>Campaigns taking advantage of domain similarity to confuse the end user (for example, <code>sampledoma1n.com</code> or <code>sampledomaln.com</code> compared to <code>sampledomain.com</code>).</td>
<td>Header mismatches, email authentication assessments, and sender reputation analysis.</td>
</tr>
<tr>
<td>Email Auth violations</td>
<td>Campaigns taking advantage of incorrect or invalid sender Auth records (SPF/DKIM/DMARC) and bypassing incoming Auth-based controls.</td>
<td>Assessment of sender authentication records against published SPF/DKIM/DMARC records which is applied in combination with overall message attributes.</td>
</tr>
<tr>
<td>Name Spoof Attacks / Executive Attacks <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/">(BEC)</a></td>
<td>Campaigns targeting executives and high-value targets within the organization or using the high-value targets as sources to attack other employees within the organization.</td>
<td>Display names compared with known executive names for similarity using several matching models including the Levenshtein Algorithm, and if matched, flagged when sender is originating from an unknown domain.</td>
</tr>
<tr>
<td>Fileless / Linkless campaigns <a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/">(BEC)</a></td>
<td>Typically BEC campaigns with an offline call to action (call me, wire money, invoice, or others).</td>
<td>Message lexical analysis, subject analysis, word count assessments, and sender analysis.</td>
</tr>
<tr>
<td>Deferred campaign attacks</td>
<td>Campaigns that have no malicious payload and the URL is clean when delivered, but is activated in a deferred manner (3-4 hours later), so the end user is compromised at click time.</td>
<td>URL rewrites and/or DNS blocks.</td>
</tr>
<tr>
<td>IP-based Spam</td>
<td>Volume-based, large scale spam campaigns primarily originating from compromised IP address spaces or botnets.</td>
<td>Sender and IP reputation, history, and volume analysis.</td>
</tr>
<tr>
<td>Content-based Spam</td>
<td>Commodity spam largely focused on selling wares.</td>
<td>Sender reputation, history, volume analysis, and message content analysis for commercial intent.</td>
</tr>
<tr>
<td>Web Phishing</td>
<td>Directly originated or targeted through web (for example, LinkedIn, Malvertizing, and more).</td>
<td>Web and DNS service and Network device integrations, like web proxies and Firewalls.</td>
</tr>
<tr>
<td>Mobile Phishing</td>
<td>Remote employee getting phished while outside the corporate network.</td>
<td>Employee email protection and web and DNS services enforcement in remote users (typically through an MDM integration or an Always-On VPN solution).</td>
</tr>
<tr>
<td>Network Phishing</td>
<td>C2 communications for lateral spread within the network or malicious phish downloaded from an external host. Typically seen when an end user gets infected outside the organization, comes back into the network and the C2 hosts uses the infected endpoint to download the implant based on the IP address space it is now resident in.</td>
<td>Network device integrations (Firewalls) and API-based integrations within existing orchestration services.</td>
</tr>
</tbody>
</table>
