---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/application-security/5/
  description: '2025-12-05'
  full_title: Application security changelog - page 5 | Cloudflare Docs
  head_html: <title>Application security changelog - page 5 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-12-05"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/application-security/5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Application security changelog - page 5"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-12-05"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/application-security/5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/application-security/5/#page","headline":"Application security changelog - page 5 | Cloudflare Docs","description":"2025-12-05","url":"https://developers.cloudflare.com/changelog/product-group/application-security/5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/application-security/5/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="updating-the-waf-maximum-payload-values"><a href="/changelog/post/2025-12-05-waf-max-payload-size-change/">Updating the WAF maximum payload values</a></h2>
<p><em>2025-12-05</em></p>
<p>We are reinstating the maximum request-payload size the Cloudflare WAF inspects, with WAF on Enterprise zones inspecting up to 128 KB.</p>
<p><strong>Key Findings</strong></p>
<p>On <a href="/changelog/2025-12-05-rcs-vuln/">December 5, 2025</a>, we initially attempted to increase the maximum WAF payload limit to 1 MB across all plans. However, an automatic rollout for all customers proved impractical because the increase led to a surge in false positives for existing managed rules.</p>
<p>This issue was particularly notable within the Cloudflare Managed Ruleset and the Cloudflare OWASP Core Ruleset, impacting customer traffic.</p>
<p><strong>Impact</strong></p>
<p>Customers on paid plans can increase the limit to 1 MB for any of their zones by contacting Cloudflare Support. Free zones are already protected up to 1 MB and do not require any action.</p>


<h2 id="waf-release-2025-12-03-emergency"><a href="/changelog/post/2025-12-03-emergency-waf-release/">WAF Release - 2025-12-03 - Emergency</a></h2>
<p><em>2025-12-03</em></p>
<p>The WAF rule deployed yesterday to block unsafe deserialization-based RCE has been updated. The rule description now reads “React – RCE – CVE-2025-55182”, explicitly mapping to the recently disclosed React Server Components vulnerability. Detection logic remains unchanged.</p>
<p><strong>Key Findings</strong></p>
<p>Rule description updated to reference React – RCE – CVE-2025-55182 while retaining existing unsafe-deserialization detection.</p>
<p><strong>Impact</strong></p>
<p>Improved classification and traceability with no change to coverage against remote code execution attempts.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="33aa8a8a948b48b28d40450c5fb92fba">5fb92fba</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b5d06e34a814a889bee9a0699702280">99702280</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-12-02-emergency"><a href="/changelog/post/2025-12-02-emergency-waf-release/">WAF Release - 2025-12-02 - Emergency</a></h2>
<p><em>2025-12-02</em></p>
<p>This week's emergency release introduces a new rule to block a critical RCE vulnerability in widely-used web frameworks through unsafe deserialization patterns.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for RCE Generic Framework to block malicious POST requests containing unsafe deserialization patterns. If successfully exploited, this vulnerability allows attackers with network access via HTTP to execute arbitrary code remotely.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Successful exploitation allows unauthenticated attackers to execute arbitrary code remotely through crafted serialization payloads, enabling complete system compromise, data exfiltration, and potential lateral movement within affected environments.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="33aa8a8a948b48b28d40450c5fb92fba">5fb92fba</code>
</td>
<td>N/A</td>
<td>RCE Generic - Framework</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b5d06e34a814a889bee9a0699702280">99702280</code>
</td>
<td>N/A</td>
<td>RCE Generic - Framework</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-12-01"><a href="/changelog/post/2025-12-01-waf-release/">WAF Release - 2025-12-01</a></h2>
<p><em>2025-12-01</em></p>
<p>This week’s release introduces new detections for remote code execution attempts targeting Monsta FTP (CVE-2025-34299), alongside improvements to an existing XSS detection to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-34299 is a critical remote code execution flaw in Monsta FTP, arising from improper handling of user-supplied parameters within the file-handling interface. Certain builds allow crafted requests to bypass sanitization and reach backend PHP functions that execute arbitrary commands. Attackers can send manipulated parameters through the web panel to trigger command execution within the application’s runtime environment.</li>
</ul>
<p><strong>Impact</strong></p>
<p>If exploited, the vulnerability enables full remote command execution on the underlying server, allowing takeover of the hosting environment, unauthorized file access, and potential lateral movement. As the flaw can be triggered without authentication on exposed Monsta FTP instances, it represents a severe risk for publicly reachable deployments.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="480da5e7984542a6b8d8d88da4fcc8a8">a4fcc8a8</code>
</td>
<td>N/A</td>
<td>Monsta FTP - Remote Code Execution - CVE:CVE-2025-34299</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2380b125c53d42ac94479c42b7492846">b7492846</code>
</td>
<td>N/A</td>
<td>XSS - JS Context Escape - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "XSS - JS Context Escape" (ID: <code class="nb-rule-id" title="c1ad1bc37caa4cbeb104f44f7a3769d3">7a3769d3</code>)</td>
</tr>  
</tbody>
</table>


<h2 id="new-zombie-api-detection-for-api-shield"><a href="/changelog/post/2025-11-25-zombie-endpoint-risk-label/">New Zombie API detection for API Shield</a></h2>
<p><em>2025-11-25</em></p>
<p>API Shield now automatically detects zombie endpoints — saved endpoints that have not received traffic for an extended period. When detected, the <code>cf-risk-zombie</code> <a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">risk label</a> is applied.</p>
<p>The scan runs daily alongside existing risk scans. Endpoints are labeled after 32 days without traffic.</p>
<p>Zombie endpoints may indicate deprecated or forgotten API surface area that could pose a security risk. Review these endpoints and consider removing them from Endpoint Management if they are no longer in use. Also consider using a <a href="/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule">fallthrough rule</a> to prevent communication with endpoints removed from Endpoint Management.</p>


<h2 id="waf-release-2025-11-24"><a href="/changelog/post/2025-11-24-waf-release/">WAF Release - 2025-11-24</a></h2>
<p><em>2025-11-24</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in FortiWeb, linked to CVE-2025-64446, alongside new detection logic expanding protection against PHP Wrapper Injection techniques.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability enables an unauthenticated attacker to bypass access controls by abusing the <code>CGIINFO</code> header. The latest update strengthens detection logic to ensure a reliable identification of crafted requests attempting to exploit this flaw.</p>
<p><strong>Impact</strong></p>
<ul>
<li>FortiWeb (CVE-2025-64446): Exploitation allows a remote unauthenticated adversary to circumvent authentication mechanisms by sending a manipulated <code>CGIINFO</code> header to FortiWeb’s backend CGI handler. Successful exploitation grants unintended access to restricted administrative functionality, potentially enabling configuration tampering or system-level actions.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b957ace6e9844bf29244401c4e2e1a2e">4e2e1a2e</code>
</td>
<td>N/A</td>
<td>FortiWeb - Authentication Bypass via CGIINFO Header - CVE:CVE-2025-64446</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e3871391a93248fa98a78e03b6c44ed5">b6c44ed5</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - Body - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - Body" (ID:<code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e6b1b66e0e3b46969102baed900f4015">900f4015</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - URI - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - URI" (ID:<code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code>)</td>
</tr>
</tbody>
</table>


<h2 id="threat-insights-are-now-available-in-the-threat-events-platform"><a href="/changelog/post/2025-11-21-Threat-Events-now-show-events-insights/">Threat insights are now available in the Threat Events platform</a></h2>
<p><em>2025-11-21</em></p>
<p>The threat events platform now has threat insights available for some relevant parent events. Threat intelligence analyst users can access these insights for their threat hunting activity.
Insights are also highlighted in the Cloudflare dashboard by a small <code>lightning icon</code> and the insights can refer to multiple, connected events, potentially part of the same attack or campaign and associated with the same threat actor.</p>
<p>For more information, refer to <a href="/security-center/cloudforce-one/#analyze-threat-events">Analyze threat events</a>.</p>


<h2 id="waf-release-2025-11-21"><a href="/changelog/post/2025-11-21-emergency-waf-release/">WAF Release - 2025-11-21</a></h2>
<p><em>2025-11-21</em></p>
<p>This week’s release introduces a critical detection for CVE-2025-61757, a vulnerability in the Oracle Identity Manager REST WebServices component.</p>
<p><strong>Key Findings</strong></p>
<p>This flaw allows unauthenticated attackers with network access over HTTP to fully compromise the Identity Manager, potentially leading to a complete takeover.</p>
<p><strong>Impact</strong></p>
<p>Oracle Identity Manager (CVE-2025-61757): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fa584616fe2241608cb8bd1339fdbe7e">39fdbe7e</code>
</td>
<td>N/A</td>
<td>Oracle Identity Manager - Pre-Auth RCE - CVE:CVE-2025-61757</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-11-17"><a href="/changelog/post/2025-11-17-waf-release/">WAF Release - 2025-11-17</a></h2>
<p><em>2025-11-17</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in DELMIA Apriso, linked to CVE-2025-6205.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to gain privileged access to the application. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<ul>
<li>DELMIA Apriso (CVE-2025-6205): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ec1e2aa190e64e7cb468e16dd256f4bc">d256f4bc</code>
</td>
<td>N/A</td>
<td>DELMIA Apriso - Auth Bypass - CVE:CVE-2025-6205</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="new-bola-vulnerability-detection-for-api-shield"><a href="/changelog/post/2025-11-12-bola-attack-detection/">New BOLA Vulnerability Detection for API Shield</a></h2>
<p><em>2025-11-12</em></p>
<p>Now, API Shield automatically searches for and highlights <strong>Broken Object Level Authorization (BOLA) attacks</strong> on managed API endpoints. API Shield will highlight both BOLA enumeration attacks and BOLA pollution attacks, telling you what was attacked, by who, and for how long.</p>
<p>You can find these attacks three different ways: Security Overview, Endpoint details, or Security Analytics. If these attacks are not found on your managed API endpoints, there will not be an overview card or security analytics suspicious activity card.</p>
<p>On the Security Overview card, select the suggestion &gt; <strong>View details</strong> to review the top attacked API endpoints, endpoint details, and the attack summary:
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-card.png" alt="BOLA attack Overview card" />
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-drawer.png" alt="BOLA attack Overview drawer" /></p>
<p>From the endpoint details, you can select <strong>View attack</strong> to find details about the BOLA attacker’s sessions.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-endpoint-attack.png" alt="BOLA attack endpoint details" /></p>
<p>From here, select <strong>View in Analytics</strong> to observe attacker traffic over time for the last seven days.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-analytics-drawer.png" alt="BOLA attack analytics drawer" /></p>
<p>Your search will filter to traffic on that endpoint in the last seven days, along with the malicious session IDs found in the attack. Session IDs are hashed for privacy and will not be found in your origin logs. Refer to IP and JA4 fingerprint to cross-reference behavior at the origin.</p>
<p>At any time, you can also start your investigation into attack traffic from Security Analytics by selecting the suspicious activity card.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-suspicious-card.png" alt="Suspicious Activity card" /></p>
<p>We urge you to take all of this client information to your developer team to research the attacker behavior and ensure any broken authorization policies in your API are fixed at the source in your application, preventing further abuse.</p>
<p>In addition, this release marks the end of the beta period for these scans. All Enterprise customers with API Shield subscriptions will see these new attacks if found on their zone.</p>


<h2 id="cloudflared-proxy-dns-command-will-be-removed-starting-february-2-2026"><a href="/changelog/post/2025-11-11-cloudflared-proxy-dns/">cloudflared proxy-dns command will be removed starting February 2, 2026</a></h2>
<p><em>2025-11-11</em></p>
<p>Starting February 2, 2026, the <code>cloudflared proxy-dns</code> command will be removed from all new <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">releases</a>.</p>
<p>This change is being made to enhance security and address a potential vulnerability in an underlying DNS library. This vulnerability is specific to the <code>proxy-dns</code> command and does not affect any other <code>cloudflared</code> features, such as the core <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> service.</p>
<p>The <code>proxy-dns</code> command, which runs a client-side <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS (DoH)</a> proxy, has been an officially undocumented feature for several years. This functionality is fully and securely supported by our actively developed products.</p>
<p>Versions of <code>cloudflared</code> released before this date will not be affected and will continue to operate. However, note that our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#deprecated-releases">official support policy</a> for any <code>cloudflared</code> release is one year from its release date.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-migration-paths">Migration paths</h4>
<p>We strongly advise users of this undocumented feature to migrate to one of the following officially supported solutions before February 2, 2026, to continue benefiting from secure <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-end-user-devices">End-user devices</h4>
<p>The preferred method for enabling DNS-over-HTTPS on user devices is the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare WARP client</a>. The WARP client automatically secures and proxies all DNS traffic from your device, integrating it with your organization's <a href="/cloudflare-one/traffic-policies/">Zero Trust policies</a> and <a href="/cloudflare-one/reusable-components/posture-checks/">posture checks</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-servers-routers-and-iot-devices">Servers, routers, and IoT devices</h4>
<p>For scenarios where installing a client on every device is not possible (such as servers, routers, or IoT devices), we recommend using the <a href="/mesh/">WARP Connector</a>.</p>
<p>Instead of running <code>cloudflared proxy-dns</code> on a machine, you can install the WARP Connector on a single Linux host within your private network. This connector will act as a gateway, securely routing all DNS and network traffic from your <a href="/mesh/features/routes/">entire subnet</a> to Cloudflare for <a href="/cloudflare-one/traffic-policies/">filtering and logging</a>.</p>


<h2 id="waf-release-2025-11-10"><a href="/changelog/post/2025-11-10-waf-release/">WAF Release - 2025-11-10</a></h2>
<p><em>2025-11-10</em></p>
<p>This week’s release introduces new detections for Prototype Pollution across three common vectors: URI, Body, and Header/Form.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>These attacks can affect both API and web applications by altering normal behavior or bypassing security controls.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation may allow attackers to change internal logic or cause unexpected behavior in applications using JavaScript or Node.js frameworks. Developers should sanitize input keys and avoid merging untrusted data structures.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="32405a50728746dd8caa057b606285e6">606285e6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a7da00c63c4243d2a72456fe4f59ff26">4f59ff26</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="833078bdcfa04bb7aa7b8fb67efbeb39">7efbeb39</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Header - Form</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>        
</tbody>
</table>


<h2 id="waf-release-2025-11-05-emergency"><a href="/changelog/post/2025-11-05-emergency-waf-release/">WAF Release - 2025-11-05 - Emergency</a></h2>
<p><em>2025-11-05</em></p>
<p>This week’s emergency release introduces a new detection signature that enhances coverage for a critical vulnerability in the React Native Metro Development Server, tracked as CVE-2025-11953.</p>
<p><strong>Key Findings</strong></p>
<p>The Metro Development Server exposes an HTTP endpoint that is vulnerable to OS command injection (CWE-78). An unauthenticated network attacker can send a crafted request to this endpoint and execute arbitrary commands on the host running Metro. The vulnerability affects Metro/cli-server-api builds used by React Native Community CLI in pre-patch development releases.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-11953 may result in remote command execution on developer workstations or CI/build agents, leading to credential and secret exposure, source tampering, and potential lateral movement into internal networks. Administrators and developers are strongly advised to apply the vendor's patches and restrict Metro’s network exposure to reduce this risk.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="db6b9e1ac1494971ae8c70aac8e30c5b">c8e30c5b</code>
</td>
<td>N/A</td>
<td>React Native Metro - Command Injection - CVE:CVE-2025-11953</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-11-03"><a href="/changelog/post/2025-11-03-waf-release/">WAF Release - 2025-11-03</a></h2>
<p><em>2025-11-03</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f5295d8333b7428c816654d8cb6d5fe5">cb6d5fe5</code>
</td>
<td>100774C</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>Log</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
</tbody>
</table>


<h2 id="report-logo-misuse-to-cloudflare-directly-from-the-brand-protection-dashboard"><a href="/changelog/post/2025-10-31-brand-protection-logo-dashboard-report-abuse/">Report logo misuse to Cloudflare directly from the Brand Protection dashboard</a></h2>
<p><em>2025-10-31</em></p>
<p>The Brand Protection logo query dashboard now allows you to use the <strong>Report to Cloudflare</strong> button to submit an Abuse report directly from the Brand Protection logo queries dashboard. While you could previously report new domains that were impersonating your brand before, now you can do the same for websites found to be using your logo without your permission. The abuse reports will be prefilled and you will only need to validate a few fields before you can click the submit button, after which our team process your request.</p>
<p>Ready to start? Check out the <a href="/security-center/brand-protection/">Brand Protection docs</a>.</p>


<h2 id="new-tcp-based-fields-available-in-rulesets"><a href="/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/">New TCP-based fields available in Rulesets</a></h2>
<p><em>2025-10-30</em></p>
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-build-rules-based-on-tcp-transport-and-latency">Build rules based on TCP transport and latency</h4>
<p>Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.</p>
<hr />
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.edge.client_tcp</code></td>
<td>Boolean</td>
<td>Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC.</td>
</tr>
<tr>
<td><code>cf.timings.client_tcp_rtt_msec</code></td>
<td>Number</td>
<td>Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>cf.edge.client_tcp &amp;&amp; cf.timings.client_tcp_rtt_msec &lt; 100&#10;</code></pre>
<p>More information can be found in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="waf-release-2025-10-30-emergency"><a href="/changelog/post/2025-10-30-emergency-waf-release/">WAF Release - 2025-10-30 - Emergency</a></h2>
<p><em>2025-10-30</em></p>
<p>This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Oracle E-Business Suite, tracked as CVE-2025-61884.</p>
<p><strong>Key Findings</strong></p>
<p>The flaw is easily exploitable and allows an unauthenticated attacker with network access to compromise Oracle Configurator, which can grant access to sensitive resources and configuration data. The affected versions include 12.2.3 through 12.2.14.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-61884 may result in unauthorized access to critical business data or full exposure of information accessible through Oracle Configurator. Administrators are strongly advised to apply vendor's patches and recommended mitigations to reduce this exposure.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="2749f13f8cb34a3dbd49c8c48827402f">8827402f</code>
</td>
<td>N/A</td>
<td>Oracle E-Business Suite - SSRF - CVE:CVE-2025-61884</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="cloudforce-one-rfi-tokens-are-now-visible-in-the-dashboard"><a href="/changelog/post/2025-10-27-RFI-Tokens-in-Dash/">Cloudforce One RFI tokens are now visible in the dashboard</a></h2>
<p><em>2025-10-27</em></p>
<p>The Requests for Information (RFI) dashboard now shows users the number of tokens used by each submitted RFI to better understand usage of tokens and how they relate to each request submitted.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-24RFITokens.png" alt="Cloudforce One RFI tokens" /></p>
<p>What’s new:</p>
<ul>
<li>Users can now see the number of tokens used for a submitted request for information.</li>
<li>Users can see the remaining tokens allocated to their account for the quarter.</li>
<li>Users can only select the Routine priority for the <code>Strategic Threat Research</code> request type.</li>
</ul>
<p>Cloudforce One subscribers can try it now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/requests">Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>


<h2 id="waf-release-2025-10-24-emergency"><a href="/changelog/post/2025-10-24-emergency-waf-release/">WAF Release - 2025-10-24 - Emergency</a></h2>
<p><em>2025-10-24</em></p>
<p>This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Windows Server Update Services (WSUS), tracked as CVE-2025-59287.</p>
<p><strong>Key Findings</strong></p>
<p>The vulnerability allows unauthenticated attackers to potentially achieve remote code execution. The updated detection logic strengthens defenses by improving resilience against exploitation attempts targeting this flaw.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-59287 could enable attackers to hijack sessions, execute arbitrary commands, exfiltrate sensitive data, and disrupt storefront operations. These actions pose significant confidentiality and integrity risks to affected environments. Administrators should apply vendor patches immediately to mitigate exposure.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5eaeb5ea6e5a4bce867eb3ffbd72ba08">bd72ba08</code>
</td>
<td>N/A</td>
<td>Windows Server - Deserialization - CVE:CVE-2025-59287</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-23-emergency"><a href="/changelog/post/2025-10-23-emergency-waf-release/">WAF Release - 2025-10-23 - Emergency</a></h2>
<p><em>2025-10-23</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update enhances detection logic to provide more resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<p>Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6e04fa2b9eb34fb088034d3fc6ef59a1">c6ef59a1</code>
</td>
<td>N/A</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-20"><a href="/changelog/post/2025-10-20-waf-release/">WAF Release - 2025-10-20</a></h2>
<p><em>2025-10-20</em></p>
<p>This week’s update introduces an enhanced rule that expands detection coverage for a critical vulnerability in Oracle E-Business Suite. It also improves an existing rule to provide more reliable coverage in request processing.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for Oracle E-Business Suite (CVE-2025-61882) to block  unauthenticated attacker's network access via HTTP to compromise Oracle Concurrent Processing. If successfully exploited, this vulnerability may result in remote code execution.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Successful exploitation of CVE-2025-61882 allows unauthenticated attackers to execute arbitrary code remotely by chaining multiple weaknesses, enabling lateral movement into internal services, data exfiltration, and large-scale extortionware deployment within Oracle E-Business Suite environments.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="933fc13202cd4e8ba498c0f32b4101ab">2b4101ab</code>
</td>
<td>100598A</td>
<td>Remote Code Execution - Common Bash Bypass - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Remote Code Execution - Common Bash Bypass" (ID: <code class="nb-rule-id" title="f8238867ed3e4d3a9a7b731a50cec478">50cec478</code>)</td>
</tr>         
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="185b5df42d1e44e0aeb8f8b8a1118614">a1118614</code>
</td>
<td>100916A</td>
<td>Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882 - 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="646bccf7e9dc46918a4150d6c22b51d3">c22b51d3</code>
</td>
<td>N/A</td>
<td>HTTP Truncated</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="new-application-security-reports-closed-beta"><a href="/changelog/post/2025-10-17-app-sec-reports/">New Application Security reports (Closed Beta)</a></h2>
<p><em>2025-10-17</em></p>
<p>Cloudflare's new <strong>Application Security report</strong>, currently in Closed Beta, is now available in the dashboard.</p>
<div class="nb-dash-button"></div>
<p>The reports are generated monthly and provide cyber security insights trends for all of the Enterprise zones in your Cloudflare account.</p>
<p>The reports also include an industry benchmark, comparing your cyber security landscape to peers in your industry.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-application-security-report-mock-data.png" alt="Application Security report mock data" /></p>
<p>Learn more about the reports by referring to the <a href="/analytics/account-and-zone-analytics/app-security-reports/">Security Reports documentation</a>.</p>
<p>Use the feedback survey link at the top of the page to help us improve the reports.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-report-feedback-survey.png" alt="Application Security report survey" /></p>


<h2 id="new-detections-released-for-waf-managed-rulesets"><a href="/changelog/post/2025-10-17-emergency-waf-release/">New detections released for WAF managed rulesets</a></h2>
<p><em>2025-10-17</em></p>
<p>This week we introduced several new detections across Cloudflare Managed Rulesets, expanding coverage for high-impact vulnerability classes such as SSRF, SQLi, SSTI, Reverse Shell attempts, and Prototype Pollution. These rules aim to improve protection against attacker-controlled payloads that exploit misconfigurations or unvalidated input in web applications.</p>
<p><strong>Key Findings</strong></p>
<p>New detections added for multiple exploit categories:</p>
<p>SSRF (Server-Side Request Forgery) — new rules targeting both local and cloud metadata abuse patterns (Beta).</p>
<p>SQL Injection (SQLi) — rules for common patterns, sleep/time-based injections, and string/wait function exploitation across headers and URIs.</p>
<p>SSTI (Server-Side Template Injection) — arithmetic-based probe detections introduced across URI, header, and body fields.</p>
<p>Reverse Shell and XXE payloads — enhanced heuristics for command execution and XML external entity misuse.</p>
<p>Prototype Pollution — new Beta rule identifying common JSON payload structures used in object prototype poisoning.</p>
<p>PHP Wrapper Injection and HTTP Parameter Pollution detections — to catch path traversal and multi-parameter manipulation attempts.</p>
<p>Anomaly Header Checks — detecting CRLF injection attempts in header names.</p>
<p><strong>Impact</strong></p>
<p>These updates help detect multi-vector payloads that blend SSRF + RCE or SQLi + SSTI attacks, especially in cloud-hosted applications with exposed metadata endpoints or unsafe template rendering.</p>
<p>Prototype Pollution and HTTP parameter pollution rules address emerging JavaScript supply-chain exploitation patterns increasingly seen in real-world incidents.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="72f0ff933fb0492eb71cda50589f2a1d">589f2a1d</code></td>
<td>N/A</td>
<td>Anomaly:Header - name - CR, LF</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="5d0377e4435f467488614170132fab7e">132fab7e</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="54e32f7f802c4a699182e8921a027008">1a027008</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - Header</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="7cbda8dbafbc465d9b64a8f2958d0486">958d0486</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="b9f3420674cf481da32333dc8e0cf7ad">8e0cf7ad</code></td>
<td>N/A</td>
<td>Generic Rules - XXE - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="ad55483512f0440b81426acdbf8aab5e">bf8aab5e</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - Common Patterns - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="849c0618d1674f1c92ba6f9b2e466337">2e466337</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - Sleep Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="1b4db4c4bd0649c095c27c6cb686ab47">b686ab47</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - String Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="fa2055b84af94ba4b925f834b0633709">b0633709</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - WaitFor Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="158177dec2504acdba1f2da201a076eb">01a076eb</code></td>
<td>N/A</td>
<td>SSRF - Local - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="98bfd6bb46074d5b8d1c4b39743a63ec">743a63ec</code></td>
<td>N/A</td>
<td>SSRF - Local - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code></td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="ecd26d61a75e46f6a4449a06ab8af26f">ab8af26f</code></td>
<td>N/A</td>
<td>SSRF - Cloud - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="c16f4e133c4541f293142d02e6e8dc5b">e6e8dc5b</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="f4fd9904e7624666b8c49cd62550d794">2550d794</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - Header</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="5c0875604f774c36a4f9b69c659d12a6">659d12a6</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code></td>
<td>N/A</td>
<td>PHP Wrapper Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code></td>
<td>N/A</td>
<td>PHP Wrapper Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="cb67fe56a84747b8b64277dc091e296d">091e296d</code></td>
<td>N/A</td>
<td>HTTP parameter pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="443b54d984944cd69043805ee34214ef">e34214ef</code></td>
<td>N/A</td>
<td>Prototype Pollution - Common Payloads - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-13"><a href="/changelog/post/2025-10-13-waf-release/">WAF Release - 2025-10-13</a></h2>
<p><em>2025-10-13</em></p>
<p>This week’s highlights include a new JinJava rule targeting a sandbox-bypass flaw that could allow malicious template input to escape execution controls. The rule improves detection for unsafe template rendering paths.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for JinJava (CVE-2025-59340) to block a sandbox bypass in the template engine that permits attacker-controlled type construction and arbitrary class instantiation; in vulnerable environments this can escalate to remote code execution and full server compromise.</p>
<p><strong>Impact</strong></p>
<ul>
<li>CVE-2025-59340 — Exploitation enables attacker-supplied type descriptors / Jackson <code>ObjectMapper</code> abuse, allowing arbitrary class loading, file/URL access (LFI/SSRF primitives) and, with suitable gadget chains, potential remote code execution and system compromise.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b327d6442e2d4848b4aab3cbc04bab5f">c04bab5f</code>
</td>
<td>100892</td>
<td>JinJava - SSTI - CVE:CVE-2025-59340</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-07-emergency"><a href="/changelog/post/2025-10-07-emergency-waf-release/">WAF Release - 2025-10-07 - Emergency</a></h2>
<p><em>2025-10-07</em></p>
<p>This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device.
The initial two rules were made available on September 28, with a third rule added today, October 7, for more robust protection.</p>
<ul>
<li>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.
Administrators are strongly advised to apply vendor updates immediately.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="12f808a5315441688f3b7c8a3a4d1bd6">3a4d1bd6</code>
</td>
<td>100788B</td>
<td>Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/4/">Previous</a><span>Page 5 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/6/">Next</a></nav>
