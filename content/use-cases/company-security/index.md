<p>Protect employees, devices, and data with Zero Trust access, secure web gateway, and email security. Cloudflare Access and Tunnel replace VPNs with identity-verified, per-request access to internal applications. Gateway filters DNS and HTTP traffic to block threats. DLP prevents sensitive data from leaving your network. Email Security stops phishing, BEC, and malware. DMARC management prevents domain spoofing.</p>
<ul class="directory-listing"><li><a href="/use-cases/company-security/employee-access/">Access internal applications securely</a></li><li><a href="/use-cases/company-security/internet-access/">Secure your company&#x27;s Internet access</a></li><li><a href="/use-cases/company-security/email-security/">Stop email phishing attacks</a></li><li><a href="/use-cases/company-security/data-loss-prevention/">Prevent data loss</a></li><li><a href="/use-cases/company-security/device-security/">Ensure device endpoint security</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="vpn-replacement">VPN replacement</h3>
<p>Replace traditional VPNs with Zero Trust access to internal applications:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong> connects internal apps to Cloudflare without opening inbound firewall ports</li>
<li><strong>Access</strong> verifies identity and device posture on every request</li>
<li><strong>Cloudflare One client</strong> routes device traffic through Cloudflare's network</li>
</ul>
<h3 id="secure-web-gateway">Secure web gateway</h3>
<p>Filter and inspect Internet-bound traffic from employees:</p>
<ul>
<li><strong>Gateway</strong> applies DNS and HTTP filtering policies to block threats and enforce acceptable use</li>
<li><strong>Browser Isolation</strong> executes risky web content in a remote browser</li>
<li><strong>DLP</strong> inspects outbound traffic for sensitive data patterns</li>
</ul>
<h3 id="email-threat-protection">Email threat protection</h3>
<p>Stop phishing, malware, and spoofing before they reach the inbox:</p>
<ul>
<li><strong>Email Security</strong> scans inbound messages for phishing, Business Email Compromise (BEC), and malicious attachments</li>
<li><strong>DMARC management</strong> enforces email authentication and prevents domain spoofing</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A <a href="/cloudflare-one/setup/">Cloudflare One organization</a> created in the Cloudflare dashboard. Access, Gateway (Secure Web Gateway), Data Loss Prevention (DLP), Cloud Access Security Broker (CASB), Browser Isolation, and Device Posture all operate within Cloudflare One.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15239.md")
</div>
