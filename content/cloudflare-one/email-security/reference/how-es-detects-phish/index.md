<p>Email security uses a variety of factors to determine whether a given email message, a web domain or URL, or specific network traffic is part of a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4918.md")
</div> campaign (marked with a [`Malicious` disposition](/cloudflare-one/email-security/reference/dispositions-and-attributes/)) or other common campaigns (for example, `Spam`).
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4917.md")
</aside>
<p>These small pattern assessments are dynamic in nature and — in many cases — no single one in and of itself will determine the final verdict. Instead, our automated systems use a combination of factors and non-factors to clearly distinguish between a valid phishing campaign and benign traffic.</p>
<h2 id="scope">Scope</h2>
<p>Email Security inspects email protocols such as SMTP, IMAP, and POP3 to detect phishing, business email compromise (BEC), spoofing, and malware delivered via email.</p>
<p>For protection against DDoS attacks targeting web and network infrastructure at layers 3, 4, and 7 — including TCP, UDP, DNS, and HTTP/S traffic — refer to <a href="/ddos-protection/">DDoS Protection</a>.</p>
<h2 id="sample-attack-types-and-detections">Sample attack types and detections</h2>
<h3 id="malicious-payload-attached-to-the-message">Malicious payload attached to the message</h3>
<ul>
<li><strong>Example</strong>: Classic campaign technique which utilizes a variety of active attachment types (EXE, DOC, XLS, PPT, OLE, PDF, and more) as the malicious payload for ransomware attacks, Trojans, viruses, and malware.</li>
<li><strong>Detections applied</strong>: Machine learning (ML) models on binary bitmaps of the payload as well as higher-level attributes of the payload, with specific focus on signatureless detections for maximum coverage. Additionally, for relevant active payloads, the engine invokes a real-time sandbox to assess behavior and determine maliciousness.</li>
</ul>
<h3 id="encrypted-malicious-payload-attached-to-the-message-with-password-in-message-body-as-text">Encrypted malicious payload attached to the message, with password in message body as text</h3>
<ul>
<li><strong>Example</strong>: Campaigns that induce the user to apply a password within the message body to the attachment.</li>
<li><strong>Detections applied</strong>: Real-time lexical parsing of message body for password extraction and ML models on binary bitmaps of the payload, signatureless detections for maximum coverage.</li>
</ul>
<h3 id="encrypted-malicious-payload-attached-to-the-message-with-password-in-message-body-as-an-image">Encrypted malicious payload attached to the message, with password in message body as an image</h3>
<ul>
<li><strong>Example</strong>: Campaigns that induce the user to apply a password within the message body to the attachment, with the entire body or part of the body being an image.</li>
<li><strong>Detections applied</strong>: Real-time OCR parsing of message body for password extraction and ML models on binary bitmaps of the payload, signatureless detections for maximum coverage.</li>
</ul>
<h3 id="malicious-payload-within-an-archive-attached-to-the-message">Malicious payload within an archive attached to the message</h3>
<ul>
<li><strong>Example</strong>: Campaigns with payloads within typical archives, such as <code>.zip</code> files.</li>
<li><strong>Detections applied</strong>: ML detection tree on the payload, as well as decomposition of each individual archive into component parts and fragments for compound documents.</li>
</ul>
<h3 id="malicious-urls-within-message-body">Malicious URLs within message body</h3>
<ul>
<li><strong>Example</strong>: Typical phish campaigns with a socially engineered call to action URL that will implant malware (for example, Watering Hole attacks, Malvertizing, or scripting attacks).</li>
<li><strong>Detections applied</strong>: Continuous web crawling, followed by real-time link crawling for a select group of suspicious urls, followed by machine learning applied to URL patterns in combination with other pattern rules and topic-based machine learning models for exhaustive coverage of link-based attacks.</li>
</ul>
<h3 id="malicious-payload-linked-through-a-url-in-a-message">Malicious payload linked through a URL in a message</h3>
<ul>
<li><strong>Example</strong>: Campaigns where the URL links through to a remote malicious attachment (for example, in a <code>.doc</code> or <code>.pdf</code> file).</li>
<li><strong>Detections applied</strong>: Remote document and/or attachment extraction followed by ML detection tree on the payload, instant crawl of links.</li>
</ul>
<h3 id="blind-url-campaigns">Blind URL campaigns</h3>
<ul>
<li><strong>Example</strong>: Entirely new domain with intentional obfuscation, seen for the first time in a campaign.</li>
<li><strong>Detections applied</strong>: Link structure analysis, link length analysis, domain age analysis, neural net models on entire URL as well as domain and IP reputation of URL host, including autonomous system name reputation and geolocation based reputation.</li>
</ul>
<h3 id="malicious-urls-within-a-benign-attachment-in-the-message">Malicious URLs within a benign attachment in the message</h3>
<ul>
<li><strong>Example</strong>: Campaigns obfuscating the payload within attachments.</li>
<li><strong>Detections applied</strong>: URL extraction within attachments, followed by above mentioned URL detection mechanisms.</li>
</ul>
<h3 id="malicious-urls-within-an-archive-attached-to-the-message">Malicious URLs within an archive attached to the message</h3>
<ul>
<li><strong>Example</strong>: Campaigns obfuscating the payload within attachments.</li>
<li><strong>Detections applied</strong>: Attachments decomposed recursively (both in archive formats and compound document formats) to extract URLs, followed by above mentioned URL detection mechanisms.</li>
</ul>
<h3 id="malicious-urls-behind-url-shortening-services">Malicious URLs behind URL shortening services</h3>
<ul>
<li><strong>Example</strong>: Campaigns leveraging Bitly, Owly, and similar services at multiple levels of redirection to hide the target URL.</li>
<li><strong>Detections applied</strong>: URL shorteners crawled in real time at the moment of message delivery to get to the eventual target URL, followed by URL detection methods. Real-time shorterners are intentionally not crawled ahead of time due to the dynamic nature of these services and the variation of target URLs based on time and source.</li>
</ul>
<h3 id="malicious-urls-associated-with-qr-codes-qr-code-phishing-attacks-quishing">Malicious URLs associated with QR codes (QR Code Phishing Attacks, Quishing)</h3>
<ul>
<li><strong>Example</strong>: Campaigns leveraging QR code image attachment to deliver malicious payload links for malware distribution and/or credential harvesting.</li>
<li><strong>Detections applied</strong>: Resolving for images resembling QR codes into URL, followed by above mentioned URL detection mechanisms.</li>
</ul>
<h3 id="instant-crawl-of-urls-within-message-body">Instant crawl of URLs within message body</h3>
<ul>
<li><strong>Example</strong>: Typical phish campaigns with a socially engineered call to action URL that will implant a malware (for example, Watering Hole attacks, Malvertizing, or scripting attacks).</li>
<li><strong>Detections applied</strong>: Heuristics applied to URLs in message bodies that are not already detected from ahead of time crawling and those deemed suspicious according to strict criteria are crawled in real time.</li>
</ul>
<h3 id="credential-harvesters">Credential Harvesters</h3>
<ul>
<li><strong>Example</strong>: Form-based credential submission attacks, leveraging known brands (Office 365, PayPal, Dropbox, Google, and more).</li>
<li><strong>Detections applied</strong>: Continuous web crawling, computer vision on top brand lures, ML models, and infrastructure association.</li>
</ul>
<h3 id="domain-spoof-attacks">Domain Spoof Attacks</h3>
<ul>
<li><strong>Example</strong>: Campaigns spoofing sender domains to refer to the recipient domain or some known partner domain.</li>
<li><strong>Detections applied</strong>: Header mismatches, email authentication assessments, sender reputation analysis, homographic analysis, and punycode manipulation assessments.</li>
</ul>
<h3 id="domain-proximity-attacks">Domain proximity attacks</h3>
<ul>
<li><strong>Example</strong>: Campaigns taking advantage of domain similarity to confuse the end user (for example, <code>sampledoma1n.com</code> or <code>sampledomaln.com</code> compared to <code>sampledomain.com</code>).</li>
<li><strong>Detections applied</strong>: Header mismatches, email authentication assessments, and sender reputation analysis.</li>
</ul>
<h3 id="email-auth-violations">Email Auth violations</h3>
<ul>
<li><strong>Example</strong>: Campaigns taking advantage of incorrect or invalid sender Auth records (SPF/DKIM/DMARC) and bypassing incoming Auth-based controls.</li>
<li><strong>Detections applied</strong>: Assessment of sender authentication records against published SPF/DKIM/DMARC records which is applied in combination with overall message attributes.</li>
</ul>
<h3 id="name-spoof-attacks-executive-attacks-bec">Name Spoof Attacks / Executive Attacks (BEC)</h3>
<ul>
<li><strong>Example</strong>: Campaigns targeting executives and high-value targets within the organization or using the high-value targets as sources to attack other employees within the organization.</li>
<li><strong>Detections applied</strong>: Display names compared with known executive names for similarity using several matching models including the Levenshtein algorithm, and if matched, flagged when sender is originating from an unknown domain.</li>
</ul>
<h3 id="fileless-linkless-campaigns-bec">Fileless / Linkless campaigns (BEC)</h3>
<ul>
<li><strong>Example</strong>: Typically BEC campaigns with an offline call to action (call me, wire money, invoice, or others).</li>
<li><strong>Detections applied</strong>: Message lexical analysis, subject analysis, word count assessments, and sender analysis.</li>
</ul>
<h3 id="deferred-campaign-attacks">Deferred campaign attacks</h3>
<ul>
<li><strong>Example</strong>: Campaigns that have no malicious payload and the URL is clean when delivered, but is activated in a deferred manner (3-4 hours later), so the end user is compromised at click time.</li>
<li><strong>Detections applied</strong>: URL rewrites and/or DNS blocks.</li>
</ul>
<h3 id="ip-based-spam">IP-based spam</h3>
<ul>
<li><strong>Example</strong>: Volume-based, large scale spam campaigns primarily originating from compromised IP address spaces or botnets.</li>
<li><strong>Detections applied</strong>: Sender and IP reputation, history, and volume analysis.</li>
</ul>
<h3 id="content-based-spam">Content-based spam</h3>
<ul>
<li><strong>Example</strong>: Commodity spam largely focused on selling wares.</li>
<li><strong>Detections applied</strong>: Sender reputation, history, volume analysis, and message content analysis for commercial intent.</li>
</ul>
<h3 id="web-phishing">Web phishing</h3>
<ul>
<li><strong>Example</strong>: Directly originated or targeted through web (for example, LinkedIn, Malvertizing, and more).</li>
<li><strong>Detections applied</strong>: Web and DNS service and network device integrations, like web proxies and firewalls.</li>
</ul>
<h3 id="mobile-phishing">Mobile phishing</h3>
<ul>
<li><strong>Example</strong>: Remote employee getting phished while outside the corporate network.</li>
<li><strong>Detections applied</strong>: Employee email protection and web and DNS services enforcement in remote users (typically through an MDM integration or an always-on VPN solution).</li>
</ul>
<h3 id="network-phishing">Network phishing</h3>
<ul>
<li><strong>Example</strong>: C2 communications for lateral spread within the network or malicious phish downloaded from an external host. Typically seen when an end user gets infected outside the organization, comes back into the network and the C2 hosts uses the infected endpoint to download the implant based on the IP address space it is now resident in.</li>
<li><strong>Detections applied</strong>: Network device integrations (firewalls) and API-based integrations within existing orchestration services.</li>
</ul>
