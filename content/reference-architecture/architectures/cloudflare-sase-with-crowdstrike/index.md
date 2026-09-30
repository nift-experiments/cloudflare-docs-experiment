---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/architectures/cloudflare-sase-with-crowdstrike/
  description: This reference architecture outlines how Cloudflare and CrowdStrike solutions integrate to create a unified security ecosystem that combines endpoint protection with zero trust network access, threat intelligence sharing, and automated remediation workflows. Organizations can leverage this integration to implement risk-based access policies, improve threat detection, and orchestrate security responses across both platforms.
  full_title: CrowdStrike and Cloudflare - A unified security ecosystem for automated, risk-based protection · Cloudflare Reference Architecture docs
  head_html: <title>CrowdStrike and Cloudflare - A unified security ecosystem for automated, risk-based protection · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="This reference architecture outlines how Cloudflare and CrowdStrike solutions integrate to create a unified security ecosystem that combines endpoint protection with zero trust network access, threat intelligence sharing, and automated remediation workflows. Organizations can leverage this integration to implement risk-based access policies, improve threat detection, and orchestrate security responses across both platforms."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/architectures/cloudflare-sase-with-crowdstrike/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/architectures/cloudflare-sase-with-crowdstrike/index.md"><meta property="og:title" content="CrowdStrike and Cloudflare - A unified security ecosystem for automated, risk-based protection · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This reference architecture outlines how Cloudflare and CrowdStrike solutions integrate to create a unified security ecosystem that combines endpoint protection with zero trust network access, threat intelligence sharing, and automated remediation workflows. Organizations can leverage this integration to implement risk-based access policies, improve threat detection, and orchestrate security responses across both platforms."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/architectures/cloudflare-sase-with-crowdstrike/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture"><meta name="algolia_content_type" content="Reference architecture"><meta name="pcx_additional_products" content="Access,Gateway,Cloudflare One Client,Logs,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/reference-architecture/architectures/cloudflare-sase-with-crowdstrike/#page","headline":"CrowdStrike and Cloudflare - A unified security ecosystem for automated, risk-based protection \u00b7 Cloudflare Reference Architecture docs","description":"This reference architecture outlines how Cloudflare and CrowdStrike solutions integrate to create a unified security ecosystem that combines endpoint protection with zero trust network access, threat intelligence sharing, and automated remediation workflows. Organizations can leverage this integration to implement risk-based access policies, improve threat detection, and orchestrate security responses across both platforms.","url":"https://developers.cloudflare.com/reference-architecture/architectures/cloudflare-sase-with-crowdstrike/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/architectures/cloudflare-sase-with-crowdstrike/
  schema: 1
---
<h2 id="abstract">Abstract</h2>
<p>This reference architecture outlines how Cloudflare and CrowdStrike solutions integrate to create a unified security ecosystem that combines endpoint protection with zero trust network access, threat intelligence sharing, and automated remediation workflows. Organizations can leverage this integration to implement risk-based access policies, improve threat detection, and orchestrate security responses across both platforms.</p>
<h2 id="introduction">Introduction</h2>
<p>Today's cybersecurity landscape presents organizations with a complex set of challenges. The expanding attack surface created by remote work, cloud migration, and sophisticated threats requires a cohesive approach that spans endpoint protection, network security, and identity management.</p>
<p>Cloudflare One and CrowdStrike Falcon® provide a powerful integrated solution to these challenges. By combining CrowdStrike's industry-leading security platform with Cloudflare's secure network and zero trust capabilities, organizations can implement comprehensive protection that secures both their devices and network traffic while simplifying management through automation and policy consistency.</p>
<h3 id="why-integrate-cloudflare-and-crowdstrike">Why integrate Cloudflare and CrowdStrike?</h3>
<p><strong>Context-aware zero trust:</strong> Identity alone is no longer sufficient for trust. Cloudflare Access ingests real-time Falcon Zero Trust Assessment (ZTA) scores to enforce dynamic, risk-based policies. This ensures that only devices verified as healthy and compliant can access sensitive resources, effectively blocking compromised endpoints even if user credentials are valid.</p>
<p><strong>Unified visibility and extended detection and response (XDR):</strong> Network and endpoint data often reside in disconnected silos. This integration streams Cloudflare's rich network logs (from Cloudflare Gateway, Cloudflare Web Application Firewall (WAF), and Cloudflare Email Security services) directly into CrowdStrike Falcon® Next-Gen SIEM. This unified view allows analysts to correlate network blocks with specific endpoint processes, providing a complete picture of the attack chain.</p>
<p><strong>Automated remediation:</strong> By connecting enforcement points, across Cloudflare and CrowdStrike, security teams can move from manual reaction to automated protection. A threat detected on the endpoint can trigger an immediate block at the network edge (and vice versa), drastically reducing risk and mean time to respond (MTTR) without increasing operational overhead.</p>
<h3 id="key-integration-points">Key integration points</h3>
<p>The integration between Cloudflare and CrowdStrike creates a powerful security ecosystem where device security posture directly influences access decisions. When a user attempts to access an application, the Cloudflare One platform verifies the request by checking multiple factors: the CrowdStrike Falcon® agent's security assessment, user identity from supported providers, and additional contextual information. Access is granted only when all policy requirements are met, ensuring that only secure devices can reach sensitive resources.</p>
<p>This continuous verification process is enhanced by bidirectional data sharing between the platforms:</p>
<ol>
<li><strong>Device posture assessment:</strong> CrowdStrike's real-time Zero Trust Assessment (ZTA) telemetry informs Cloudflare Zero Trust access decisions.</li>
<li><strong>Unified security logging:</strong> Cloudflare forwards security telemetry to CrowdStrike's Falcon Next-Gen SIEM.</li>
<li><strong>Email security intelligence:</strong> Cloudflare Email Security alerts feed into CrowdStrike's logging and analysis tools.</li>
<li><strong>Automated remediation workflows:</strong> Security events trigger coordinated, automated responses across both platforms, orchestrated via CrowdStrike Falcon Fusion SOAR.</li>
</ol>
<h2 id="integration-architecture-overview">Integration architecture overview</h2>
<p>The integration between Cloudflare and CrowdStrike establishes a comprehensive security architecture centered on a bi-directional intelligence exchange. This ecosystem connects device endpoint security with zero trust network access and automated response.</p>
<p>The architecture is defined by the following key flows:</p>
<ul>
<li><strong>Zero trust access control:</strong>
<ul>
<li>The user's endpoint runs both the Cloudflare One Client and the CrowdStrike Falcon agent.</li>
<li>CrowdStrike Falcon Device Posture and ZTA scores are shared with Cloudflare via a service-to-service API.</li>
<li>Cloudflare uses this real-time device health information as a critical factor in its Cloudflare Access decisions, enforcing zero trust policies for both public and private applications.</li>
</ul>
</li>
<li><strong>Unified security telemetry:</strong>
<ul>
<li>Cloudflare sends network and security logs (via Logpush) to CrowdStrike Falcon NextGen SIEM for centralized correlation, analysis, and threat detection.</li>
</ul>
</li>
<li><strong>Automated remediation:</strong>
<ul>
<li>Security events and threat detections within the CrowdStrike platform trigger automated containment and response workflows, orchestrated via Falcon Fusion SOAR (security orchestration, automation, and response), which leverages API automation to take bi-directional action across both platforms.</li>
</ul>
</li>
</ul>
<p>This integrated approach enables secure access to various application types:</p>
<ul>
<li>Internet applications (SaaS, web apps)</li>
<li>Self-hosted applications (on premises, data center)</li>
<li>SaaS applications (protected through identity proxy)</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-crowdstrike/Main_Arch.svg" alt="High level architecture of integration between Cloudflare and CrowdStrike" title="Figure 1: High level architecture - Integration" /></p>
<h3 id="key-use-cases">Key use cases</h3>
<p>The integration between Cloudflare and CrowdStrike enables six use cases that address critical security challenges:</p>
<h4 id="1-zero-trust-access-with-device-posture-and-user-risk-score-use-case-detail-zero-trust-with-user-and-device-risk-posture"><ol>
<li><a href="#use-case-detail-zero-trust-with-user-and-device-risk-posture">Zero trust access with device posture and user risk score</a></li>
</ol></h4>
<p><strong>Challenge:</strong> With a hybrid workforce, users access sensitive applications from personal or infected devices outside the corporate perimeter, bypassing traditional firewall controls.</p>
<p><strong>Solution:</strong> Integrate CrowdStrike Falcon ZTA scores directly into Cloudflare Access policies to enforce real-time conditional access.</p>
<h4 id="2-unified-threat-hunting-use-case-detail-unified-threat-hunting"><ol start="2">
<li><a href="#use-case-detail-unified-threat-hunting">Unified threat hunting</a></li>
</ol></h4>
<p><strong>Challenge:</strong> Security analysts struggle to correlate network alerts (e.g., a blocked malicious domain) with specific endpoint behavior because data resides in separate silos.</p>
<p><strong>Solution:</strong> Stream Cloudflare Gateway, WAF, and Email Security logs via Logpush to CrowdStrike Falcon Next-Gen SIEM for centralized analysis.</p>
<h4 id="3-automated-edge-remediation-use-case-detail-automated-edge-remediation"><ol start="3">
<li><a href="#use-case-detail-automated-edge-remediation">Automated edge remediation</a></li>
</ol></h4>
<p><strong>Challenge:</strong> Manual incident response is too slow to stop automated attacks. By the time an analyst sees an alert, the adversary may have already moved laterally or exfiltrated data.</p>
<p><strong>Solution:</strong> Leverage CrowdStrike Falcon Fusion SOAR to automatically trigger remediation actions, within Cloudflare, based on detected threats.</p>
<h4 id="4-compromised-user-lifecycle-detection-and-response-use-case-detail-compromised-user-lifecycle-detection-and-response"><ol start="4">
<li><a href="#use-case-detail-compromised-user-lifecycle--detection-and-response">Compromised user lifecycle: Detection and response</a></li>
</ol></h4>
<p><strong>Challenge:</strong> A user's laptop is infected with malware. While an endpoint detection and response (EDR) tool might detect it, the user still has valid session tokens allowing them to access SaaS apps and sensitive data.</p>
<p><strong>Solution:</strong> A closed-loop response where endpoint detection immediately revokes network access and triggers investigation.</p>
<h4 id="5-insider-threat-and-data-protection-use-case-detail-insider-threat-and-data-protection"><ol start="5">
<li><a href="#use-case-detail-insider-threat-and-data-protection">Insider threat and data protection</a></li>
</ol></h4>
<p><strong>Challenge:</strong> A departing employee attempts to upload proprietary source code to a personal cloud storage site. The traffic is encrypted, and the device is &quot;healthy,&quot; bypassing standard checks.</p>
<p><strong>Solution:</strong> Combine Cloudflare Data Loss Prevention (DLP) inspection with CrowdStrike behavioral analytics to detect and block data theft.</p>
<h4 id="6-proactive-application-defense-use-case-detail-proactive-application-defense"><ol start="6">
<li><a href="#use-case-detail-proactive-application-defense">Proactive application defense</a></li>
</ol></h4>
<p><strong>Challenge:</strong> Attackers use automated botnets to scan applications for vulnerabilities. WAFs block known signatures, but low-and-slow attacks can slip through regular filters.</p>
<p><strong>Solution:</strong> Use endpoint data to inform application security, creating an immune system for web assets.</p>
<h2 id="use-case-detail-zero-trust-with-user-and-device-risk-posture">Use case detail: Zero trust with user and device risk posture</h2>
<p>This use case demonstrates how the integration helps prevent compromised or unmanaged devices from accessing corporate resources.</p>
<h3 id="phase-1-device-and-user-risk-assessment">Phase 1: Device and user risk assessment</h3>
<p>The CrowdStrike Falcon agent continuously monitors the endpoint, calculating a ZTA score (1–100) based on OS health, patch levels, and threat activity. In parallel, Cloudflare continuously updates the user risk score based on user and entity behavior analytics (UEBA).</p>
<h3 id="phase-2-policy-evaluation">Phase 2: Policy evaluation</h3>
<p>When a user requests access to an application, Cloudflare Access intercepts the request and queries the CrowdStrike API for the device's current ZTA score.</p>
<h3 id="phase-3-access-enforcement">Phase 3: Access enforcement</h3>
<p>Cloudflare permits connection only if the ZTA score meets the minimum threshold defined in the zero trust policy; otherwise, the user is presented with a Cloudflare Access Block Page, typically instructing them to remediate the device.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-crowdstrike/UseCase01.svg" alt="Zero Trust access flow showing device posture and user risk score evaluation" title="Figure 2: Zero Trust access with device posture and user risk score" /></p>
<h2 id="use-case-detail-unified-threat-hunting">Use case detail: Unified threat hunting</h2>
<p>This use case focuses on providing comprehensive visibility, eliminating blind spots between network traffic and endpoint activity.</p>
<h3 id="phase-1-data-ingestion">Phase 1: Data ingestion</h3>
<p>Cloudflare Logpush filters and forwards HTTP requests, DNS queries, and firewall events to the Falcon Next-Gen SIEM data intake API.</p>
<h3 id="phase-2-correlation">Phase 2: Correlation</h3>
<p>Falcon Next-Gen SIEM indexes this data alongside endpoint telemetry, allowing analysts to query a single dataset.</p>
<h3 id="phase-3-investigation">Phase 3: Investigation</h3>
<p>An analyst investigating an endpoint alert can instantly pivot to see every network request that device made through Cloudflare, identifying the phishing site or C2 server that caused the infection.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-crowdstrike/UseCase02.svg" alt="Unified threat hunting workflow between Cloudflare and CrowdStrike" title="Figure 3: Unified threat hunting" /></p>
<h2 id="use-case-detail-automated-edge-remediation">Use case detail: Automated edge remediation</h2>
<p>This use case demonstrates how implementing CrowdStrike Falcon Fusion SOAR helps reduce the MTTR for rapidly evolving threats.</p>
<h3 id="phase-1-threat-detection">Phase 1: Threat detection</h3>
<p>CrowdStrike Falcon detects a specific indicator of compromise (IOC), such as a malicious IP address attacking multiple endpoints.</p>
<h3 id="phase-2-orchestration">Phase 2: Orchestration</h3>
<p>A Falcon Fusion SOAR workflow is triggered by the detection.</p>
<h3 id="phase-3-edge-mitigation">Phase 3: Edge mitigation</h3>
<p>The workflow calls the Cloudflare API to add the malicious IP to a blocklist in Cloudflare WAF or Gateway, instantly protecting the entire organization from that threat source.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-crowdstrike/UseCase03.svg" alt="Automated edge remediation workflow from threat detection to edge mitigation" title="Figure 4: Automated edge remediation" /></p>
<h2 id="use-case-detail-compromised-user-lifecycle-detection-and-response">Use case detail: Compromised user lifecycle — Detection and response</h2>
<p>This use case outlines how the combined integration pillars are leveraged to contain active endpoint compromise and prevent lateral movement.</p>
<h3 id="phase-1-detection-and-signal-sharing">Phase 1: Detection and signal sharing</h3>
<p>The Falcon agent detects malware execution. It immediately drops the device's ZTA score to &quot;Critical&quot; and sends an alert to the SIEM.</p>
<h3 id="phase-2-instant-access-revocation">Phase 2: Instant access revocation</h3>
<p>Cloudflare Access, checking the ZTA score on the very next request, blocks the user from accessing Salesforce, email, or internal tools, effectively quarantining the device from the network.</p>
<h3 id="phase-3-investigate-and-remediate">Phase 3: Investigate and remediate</h3>
<p>Falcon Fusion SOAR automates a response playbook: It isolates the endpoint (network containment) and adds the user to a custom list, in Cloudflare, effectively tagging them in the logs for deeper retrospective analysis in Falcon Next-Gen SIEM and enforcing additional policies attached to the custom list.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-crowdstrike/UseCase04.svg" alt="Compromised user lifecycle showing detection, access revocation, and remediation" title="Figure 5: Compromised user lifecycle - detection and response" /></p>
<h2 id="use-case-detail-insider-threat-and-data-protection">Use case detail: Insider threat and data protection</h2>
<p>This use case demonstrates how the unified approach helps prevent and respond to data exfiltration by trusted insider actors.</p>
<h3 id="phase-1-dlp-monitoring">Phase 1: DLP monitoring</h3>
<p>Cloudflare DLP scans upload traffic. It detects source code markers and logs the event to Falcon Next-Gen SIEM via Logpush, while momentarily blocking the specific request.</p>
<h3 id="phase-2-risk-scoring-and-correlation">Phase 2: Risk scoring and correlation</h3>
<p>Falcon Next-Gen SIEM correlates this DLP event with endpoint activity (e.g., recent USB usage or large file copies). This behavior triggers a &quot;High Risk&quot; user tag.</p>
<h3 id="phase-3-adaptive-control">Phase 3: Adaptive control</h3>
<p>Falcon Fusion SOAR updates the Cloudflare Zero Trust policy to require &quot;step-up authentication&quot; or remote browser isolation (RBI) for this specific user, preventing further data movement even for legitimate tasks until cleared by HR or security.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-crowdstrike/UseCase05.svg" alt="Insider threat and data protection workflow with DLP monitoring and adaptive controls" title="Figure 6: Insider threat and data protection" /></p>
<h2 id="use-case-detail-proactive-application-defense">Use case detail: Proactive application defense</h2>
<p>This use case explores the power of the integrated solutions to defend public applications against botnets and zero-day exploits.</p>
<h3 id="phase-1-attack-identification">Phase 1: Attack identification</h3>
<p>Cloudflare WAF blocks a series of SQL injection attempts from a specific subnet. These logs are sent to Falcon Next-Gen SIEM.</p>
<h3 id="phase-2-cross-domain-analysis">Phase 2: Cross-domain analysis</h3>
<p>CrowdStrike Threat Intelligence enriches the log data, identifying the subnet as part of a known targeted ransomware group.</p>
<h3 id="phase-3-defensive-tuning">Phase 3: Defensive tuning</h3>
<p>Falcon Fusion SOAR triggers a workflow to update Cloudflare WAF rules: It increases the &quot;Bot Fight Mode&quot; sensitivity for that region and creates a proactive block rule for the entire autonomous system number (ASN) associated with the attack, hardening the application before the main assault begins.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-crowdstrike/UseCase06.svg" alt="Proactive application defense workflow from attack identification to defensive tuning" title="Figure 7: Proactive application defense" /></p>
<h2 id="implementation-components">Implementation components</h2>
<p>The integration between Cloudflare and CrowdStrike leverages several key components from each platform to create a cohesive security ecosystem.</p>
<h3 id="cloudflare-components">Cloudflare components</h3>
<ol>
<li><strong>Zero Trust Network Access (ZTNA)</strong>: Controls access to applications based on identity, device posture, and other contextual signals
<ul>
<li>Application access policies</li>
<li>Private network access</li>
<li>Service token authentication</li>
<li>Device posture verification</li>
</ul>
</li>
<li><strong>Secure Web Gateway (SWG)</strong>: Inspects and filters Internet-bound traffic
<ul>
<li>URL filtering</li>
<li>Malware protection</li>
<li>Content categories</li>
<li>File type controls</li>
</ul>
</li>
<li><strong>Data Loss Prevention (DLP)</strong>: Prevents unauthorized data exfiltration
<ul>
<li>Built-in data profiles (PII, financial data, secrets)</li>
<li>Custom data patterns</li>
<li>Exact data matching</li>
<li>Context awareness</li>
</ul>
</li>
<li><strong>Remote Browser Isolation (RBI)</strong>: Executes web content in a secure cloud environment
<ul>
<li>File upload/download controls</li>
<li>Clipboard restrictions</li>
<li>Keyboard input controls</li>
<li>Visual presentation only</li>
</ul>
</li>
<li><strong>Email Security</strong>: Prevents email-based threats
<ul>
<li>Phishing protection</li>
<li>Malicious attachment scanning</li>
<li>Business email compromise detection</li>
<li>Link isolation</li>
</ul>
</li>
<li><strong>API-driven Cloud Access Security Broker (CASB)</strong>: Monitors SaaS usage and security
<ul>
<li>SaaS posture management</li>
<li>Permission monitoring</li>
<li>Data security scanning</li>
<li>Public share detection</li>
</ul>
</li>
<li><strong>Web Application Firewall (WAF)</strong>
<ul>
<li>Machine learning (ML) detection and blocking</li>
<li>Custom rule creation</li>
<li>Managed rule sets</li>
<li>Rate limiting</li>
</ul>
</li>
</ol>
<h3 id="crowdstrike-components">CrowdStrike components</h3>
<ol>
<li><strong>Falcon Endpoint Agent</strong>: Provides comprehensive endpoint protection
<ul>
<li>Behavior monitoring</li>
<li>Malware prevention</li>
<li>Device security posture assessment</li>
<li>Vulnerability management</li>
</ul>
</li>
<li><strong>Zero Trust Assessment (ZTA)</strong>: Evaluates device security in real time
<ul>
<li>OS security assessment</li>
<li>Sensor status monitoring</li>
<li>Overall device health scoring</li>
<li>Continuous evaluation</li>
</ul>
</li>
<li><strong>Falcon Next-Gen SIEM</strong>: Centralizes security monitoring and analysis
<ul>
<li>Log ingestion, correlation, and real-time searching</li>
<li>Threat detection rules and alert triggering</li>
<li>Security visualization with customizable dashboards</li>
<li>Alert management and long-term data storage</li>
</ul>
</li>
<li><strong>Falcon Insight XDR</strong>: Provides extended detection and response capabilities
<ul>
<li>Cross-domain detection</li>
<li>Automated investigation</li>
<li>Threat hunting</li>
<li>Guided remediation</li>
</ul>
</li>
<li><strong>Falcon Fusion SOAR:</strong> Orchestrates and automates complex security workflows across the Cloudflare and CrowdStrike platforms for unified incident response
<ul>
<li>Security orchestration</li>
<li>Playbook execution</li>
<li>Automated containment and enrichment</li>
<li>Bi-directional actioning</li>
</ul>
</li>
</ol>
<h2 id="summary">Summary</h2>
<p>The integration between Cloudflare and CrowdStrike provides organizations with a comprehensive security solution that combines endpoint security, zero trust network access, and application protection. By leveraging the strengths of both platforms, organizations can achieve better visibility into their security posture, automate responses to threats, and more effectively protect their applications and data.</p>
<p>This reference architecture demonstrates how these solutions work together to address key security challenges, including zero trust adoption, application protection, and data security. By implementing this integrated approach, organizations can enhance their security posture while reducing the operational burden on their security teams.</p>
<h2 id="resources">Resources</h2>
<ul>
<li><a href="/cloudflare-one/integrations/service-providers/crowdstrike/">Cloudflare One - CrowdStrike</a></li>
<li><a href="https://marketplace.crowdstrike.com/partners/cloudflare/">CrowdStrike Marketplace - Cloudflare</a></li>
<li><a href="https://blog.cloudflare.com/integrating-crowdstrike-falcon-fusion-soar-with-cloudflares-sase-platform/">CrowdStrike Falcon Fusion SOAR with Cloudflare SASE</a></li>
</ul>
