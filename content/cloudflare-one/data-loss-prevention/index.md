<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4518.md")
</aside>
<div class="nb-glossary-definition"><p>Cloudflare <a href="https://www.cloudflare.com/learning/access-management/what-is-dlp/">Data Loss Prevention</a> (DLP) allows you to scan your web traffic and SaaS applications for the presence of sensitive data such as social security numbers, financial information, secret keys, and source code.</p></div>
<p>DLP scans HTTP traffic, SaaS application files, and AI prompts for sensitive data such as credit card numbers, credentials, and personally identifiable information.</p>
<p>Cloudflare does not write scanned content to disk. DLP encrypts and temporarily stores content in memory only. To retain matched content for review, configure <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">payload logging</a> for encrypted payload copies or a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination">Logpush destination</a> to export full matching HTTP requests.</p>
<p>DLP uses <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/"><strong>profiles</strong></a> to define what to detect, <a href="/cloudflare-one/data-loss-prevention/detection-entries/"><strong>detection entries</strong></a> to identify specific patterns and data, and optional <a href="/cloudflare-one/data-loss-prevention/data-classification/"><strong>Data Classification</strong></a> to organize and label findings at scale.</p>
<h2 id="data-in-transit">Data in transit</h2>
<p>Data Loss Prevention complements <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a> to detect sensitive data transferred in HTTP requests and responses. DLP scans HTTP bodies (excluding headers), which may include uploaded or downloaded files, chat messages, forms, and other web content.</p>
<p>DLP requires <a href="/cloudflare-one/traffic-policies/get-started/http/">Gateway HTTP filtering</a> with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> to read HTTPS bodies in transit. The depth of visibility varies for each site or application. DLP does not scan any traffic that bypasses Cloudflare Gateway (such as traffic that matches a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policy).</p>
<p>Before deciding what to log or block, use <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection</a> to learn which sensitive data types appear in sampled Gateway traffic and where they are found. Use those findings to create or refine a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">Gateway DLP policy</a>.</p>
<h2 id="data-at-rest">Data at rest</h2>
<p>Data Loss Prevention complements <a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> (Cloud Access Security Broker) to detect sensitive data stored in your SaaS applications. CASB connects directly to SaaS application APIs to retrieve and scan files, rather than reading files as they pass through Cloudflare Gateway. Because of this, Gateway and Cloudflare One Client settings (such as <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policies and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> configurations) do not affect data at rest scans.</p>
<p>To get started, refer to <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">Scan SaaS applications with DLP</a>.</p>
<h2 id="ai-applications-and-controls">AI applications and controls</h2>
<ul>
<li><strong>AI Gateway</strong> — Data Loss Prevention integrates with <a href="/ai-gateway/">Cloudflare AI Gateway</a> to scan AI prompts and responses for sensitive data. To enable this, refer to <a href="/ai-gateway/features/dlp/set-up-dlp/">Set up DLP for AI Gateway</a>. When enabled, DLP inspects the text content of requests sent to AI providers and responses returned from AI models, without requiring Gateway HTTP filtering or TLS decryption.</li>
<li><strong>Gateway Application Granular Controls</strong> — <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">Gateway Application Granular Controls</a> let you control specific actions within AI applications without blocking the entire application. You can add the <a href="/cloudflare-one/traffic-policies/http-policies/#dlp-profile">DLP Profile selector</a> to the same HTTP policy to scan those operations for sensitive data, as described in <a href="/cloudflare-one/data-loss-prevention/dlp-policies/">Scan HTTP traffic with DLP</a>.</li>
<li><strong>AI Security for Apps</strong> — DLP complements <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> by providing profile-based detection of sensitive data in AI traffic, while AI Security for Apps handles large language model (LLM)-specific threats such as prompt injection and unsafe topics. To detect sensitive data alongside AI Security for Apps, configure <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> and apply them to your AI traffic policies.</li>
</ul>
<h2 id="email-security">Email security</h2>
<p>Data Loss Prevention integrates with <a href="/cloudflare-one/email-security/">Cloudflare Email Security</a> to scan <a href="/cloudflare-one/email-security/outbound-dlp/">outbound emails</a> for sensitive data. Outbound DLP requires <a href="https://www.cloudflare.com/learning/cloud/what-is-microsoft-365/">Microsoft 365</a> and uses a client-side Outlook add-in to inspect emails before they are sent.</p>
<p>To get started, refer to <a href="/cloudflare-one/email-security/outbound-dlp/">Outbound Data Loss Prevention (DLP)</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For help resolving common issues with DLP, refer to <a href="/cloudflare-one/data-loss-prevention/troubleshoot-dlp/">Troubleshoot DLP</a>.</p>
<p>To check how DLP evaluates sample content against your profiles, use <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan</a>.</p>
<h2 id="supported-file-types">Supported file types</h2>
<h3 id="formats">Formats</h3>
<p>DLP supports reporting and scanning the following file types:</p>
<ul>
<li>Text and CSV</li>
<li>Microsoft Office 2007 and later (<code>.docx</code>, <code>.xlsx</code>, <code>.pptx</code>), including Microsoft 365</li>
<li>PDF</li>
<li>ZIP files containing the above</li>
</ul>
<p>DLP will scan the text contained in text, Microsoft Office, and PDF files.</p>
<p>Refer to the <a href="/cloudflare-one/data-loss-prevention/dlp-settings/#optical-character-recognition-ocr">OCR documentation</a> for supported image format information.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4517.md")
</aside>
