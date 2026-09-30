<h2 id="introduction">Introduction</h2>
<p>The integration between Cloudflare One and SentinelOne provides organizations with a comprehensive security solution that combines endpoint protection with <a href="https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/">Zero Trust Network Access</a>. This integration enables organizations to make access decisions based on device security posture, ensuring that only healthy and compliant devices can access protected resources. This reference architecture describes how organizations can implement and leverage this integration to enhance their security posture. The integration can assist in advancing an organization's or agency's Zero Trust Architecture Maturity Model, with the goal of one's organization eventually achieving Advanced or Optimal across all <a href="https://www.cisa.gov/sites/default/files/2023-04/CISA_Zero_Trust_Maturity_Model_Version_2_508c.pdf">CISA's 5 Pillars of Zero Trust.</a></p>
<h2 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h2>
<p>This reference architecture is designed for IT and security professionals who are implementing or planning to implement a Zero Trust security model using Cloudflare and SentinelOne. It provides detailed guidance on integration setup, configuration options, and common deployment scenarios. To build a stronger baseline understanding of these technologies, we recommend reviewing both platforms' core documentation.</p>
<p>Recommended resources for a stronger understanding of Cloudflare's SentinelOne integration:</p>
<ul>
<li><a href="/cloudflare-one/integrations/service-providers/sentinelone/">SentinelOne device posture integration</a></li>
</ul>
<h2 id="integration-overview">Integration overview</h2>
<p>Cloudflare One can integrate with SentinelOne to enforce device-based access policies for applications and resources. The integration works through a service-to-service posture check that identifies devices based on their serial numbers. This allows organizations to ensure that only managed and secure devices can access sensitive resources.</p>
<h2 id="technical-components">Technical components</h2>
<h3 id="sentinelone-components">SentinelOne components</h3>
<p>The SentinelOne platform provides critical endpoint security capabilities:</p>
<p>The SentinelOne agent must be deployed on all managed devices and provides real-time security monitoring and threat detection. Key posture data points include:</p>
<ul>
<li>Infection status of the device</li>
<li>Number of active threats detected</li>
<li>Agent activity status</li>
<li>Network connectivity status</li>
<li>Operational state of the agent</li>
</ul>
<p>The SentinelOne Management Console provides centralized control and visibility, including the APIs necessary for integration with Cloudflare.</p>
<h3 id="cloudflare-components">Cloudflare components</h3>
<p>Cloudflare's Zero Trust infrastructure provides the policy enforcement layer:</p>
<p>The Cloudflare One Client must be deployed alongside the SentinelOne agent on managed devices. This client creates the secure connection to Cloudflare's network and enables device posture checking.</p>
<p>The Cloudflare dashboard provides the configuration interface for:</p>
<ul>
<li>Service provider integration settings</li>
<li>Device posture policies</li>
<li>Access policies that incorporate device posture checks</li>
</ul>
<h2 id="implementation-architecture">Implementation architecture</h2>
<h3 id="authentication-and-authorization-flow">Authentication and authorization flow</h3>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-sentinelone/figure1.svg" alt="Figure 1: SentinelOne is used in Cloudflare policies as part of authorization flow." title="Figure 1: SentinelOne is used in Cloudflare policies as part of authorization flow." /></p>
<p>When a user attempts to access a protected resource, the following sequence occurs:</p>
<ol>
<li>The user's device connects to Cloudflare's network through the Cloudflare One Client.</li>
<li>Cloudflare queries the SentinelOne API to check the device's security posture.</li>
<li>The SentinelOne platform returns current device status including infection state, threats, and agent health.</li>
<li>Cloudflare evaluates this information against configured policies.</li>
<li>Access is granted or denied based on policy evaluation.</li>
</ol>
<h3 id="integration-setup">Integration setup</h3>
<p>The integration requires specific configuration steps:</p>
<p>First, a service account must be created in SentinelOne with appropriate permissions. This involves generating an API token and noting the REST API URL for your instance.</p>
<p>Next, SentinelOne must be configured as a service provider in the Cloudflare Zero Trust dashboard. This includes:</p>
<ul>
<li>Providing the API token and REST API URL</li>
<li>Setting an appropriate polling frequency</li>
<li>Testing the connection to ensure proper communication</li>
</ul>
<p>Finally, device posture checks must be configured to define the security requirements for access. For detailed setup instructions, refer to <a href="/cloudflare-one/integrations/service-providers/sentinelone/">SentinelOne device posture integration</a>.</p>
<h2 id="security-capabilities">Security capabilities</h2>
<h3 id="device-posture-verification">Device posture verification</h3>
<p>The integration enables robust device security verification through multiple attributes:</p>
<p>Infection Status monitoring ensures that compromised devices cannot access sensitive resources. Active Threat Detection prevents devices with ongoing security incidents from maintaining access. Agent Health Monitoring confirms that the security stack remains functional and properly configured.</p>
<h3 id="user-risk-detection">User risk detection</h3>
<p>SentinelOne provides <a href="https://www.sentinelone.com/cybersecurity-101/endpoint-security/what-is-endpoint-detection-and-response-edr/">endpoint detection and response (EDR)</a> signals that help determine user risk scores. This allows organizations to identify and manage users who may present security risks, enabling proactive security measures before incidents occur.</p>
<h2 id="core-architecture">Core architecture</h2>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-sentinelone/figure2.svg" alt="Figure 2: SentinelOne and Cloudflare Zero Trust technical architecture." title="Figure 2: SentinelOne and Cloudflare Zero Trust technical architecture." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>The integration architecture begins at the managed endpoint device level, where two critical components coexist. The SentinelOne agent serves as the primary security enforcer, continuously monitoring the device for threats, assessing device health, and providing real-time security status updates. Alongside it, the Cloudflare One Client establishes secure connectivity and manages the device's interaction with Cloudflare's Zero Trust infrastructure. These components work in tandem to ensure both endpoint security and secure network access.</p>
<p>When a user attempts to access protected resources, the architecture initiates a sophisticated verification process. The Cloudflare One Client first establishes a secure tunnel to Cloudflare's global network, creating an encrypted channel for all communications. This connection ensures that all traffic between the device and protected resources remains secure and can be properly evaluated against security policies.</p>
<h3 id="cloudflare-zero-trust-platform-operations">Cloudflare Zero Trust platform operations</h3>
<p>At the heart of the architecture lies the Cloudflare Zero Trust platform, which consists of three main engines working in concert. The <strong>Device Posture Engine</strong> serves as the first line of defense, actively querying the SentinelOne platform to verify the device's security status. It checks multiple attributes including infection status, active threats, agent health, and network connectivity state. This information forms the foundation for access decisions.</p>
<p>The <strong>Access Policy Engine</strong> then takes this device posture information and combines it with other contextual factors to make access decisions. It evaluates predefined policies that can include criteria such as device security status, user identity, location, and other risk factors. This engine ensures that only devices meeting all security requirements can access protected resources.</p>
<p>The <strong>Secure Web Gateway</strong> adds another layer of protection by filtering all traffic, preventing access to malicious sites, and enforcing data loss prevention policies. This component ensures that even after access is granted, all traffic is continuously monitored and protected.</p>
<h3 id="sentinelone-platform-integration">SentinelOne platform integration</h3>
<p>The SentinelOne platform plays a crucial role in this architecture through three main components. The <strong>Management Console</strong> provides centralized control over all endpoints, allowing security teams to configure policies, monitor device status, and respond to security events. The <strong>API Services</strong> component facilitates real-time communication with Cloudflare, providing critical security information about managed devices.</p>
<p>The <strong>Security Analytics</strong> component continuously processes security telemetry from all endpoints, identifying threats, assessing risks, and providing detailed security insights. This information flows to Cloudflare through <strong>API Services</strong>, enabling dynamic access decisions based on the latest security intelligence.</p>
<h3 id="authentication-and-access-flow">Authentication and access flow</h3>
<p>When a user requires access to protected resources, the architecture follows a specific flow:</p>
<p>First, the device's security status is evaluated through the <strong>SentinelOne agent</strong>, which reports detailed health and security information to the SentinelOne platform. Simultaneously, the <strong>Cloudflare One Client</strong> initiates the access request to Cloudflare's Zero Trust platform.</p>
<p>Next, Cloudflare's <strong>Device Posture Engine</strong> queries the SentinelOne platform through its <strong>API Services</strong> to verify the device's security status. This check includes all current security metrics, threat status, and compliance information. The <strong>Access Policy Engine</strong> then evaluates this information against defined security policies.</p>
<p>If all security requirements are met, access is granted through the secure tunnel established by the Cloudflare One Client. Throughout the session, continuous monitoring ensures that any change in device security status can trigger immediate reevaluation of access permissions.</p>
<h3 id="security-and-monitoring-capabilities">Security and monitoring capabilities</h3>
<p>The architecture provides comprehensive security through multiple mechanisms. At the endpoint level, the SentinelOne agent provides advanced threat detection and response capabilities. The <strong>Security Analytics</strong> component processes this security telemetry in real-time, enabling quick identification of threats and security issues.</p>
<p>Cloudflare's <strong>Secure Web Gateway</strong> provides network-level protection, filtering traffic and preventing access to malicious resources. This component works in conjunction with the <strong>Access Policy Engine</strong> to ensure that all traffic, both to internal and external resources, meets security requirements.</p>
<h2 id="operational-benefits">Operational benefits</h2>
<p>This integrated architecture delivers several key operational benefits. It enables organizations to implement true Zero Trust access control, where every access request is verified based on current security status. The integration between SentinelOne and Cloudflare provides seamless security enforcement, combining endpoint protection with network-level access control.</p>
<p>The architecture also supports dynamic policy enforcement, where changes in device security status can automatically trigger access restrictions. This ensures that compromised or non-compliant devices can be quickly isolated from sensitive resources, maintaining organizational security.</p>
<h2 id="deployment-considerations">Deployment considerations</h2>
<h3 id="network-architecture">Network architecture</h3>
<p>Organizations should consider their network architecture when implementing this integration. Key factors include:</p>
<ul>
<li>Distribution of endpoints across different networks</li>
<li>Bandwidth and latency requirements for posture checks</li>
<li>Integration with existing security tools and workflows</li>
</ul>
<p>The integration between Cloudflare One and SentinelOne requires thoughtful planning to ensure successful implementation. At its foundation, organizations need to prepare their environment by having the SentinelOne agent and Cloudflare One Client deployed on all devices that will be subject to posture checks. This foundational step ensures that both security monitoring and secure network connectivity are in place before building additional security controls.</p>
<p>When implementing the integration, organizations should approach it as a service provider relationship where SentinelOne acts as a trusted source of device security information. This relationship is established through secure API communications, with careful attention paid to proper credential management and regular verification of the connection between the platforms. The integration relies on SentinelOne's ability to provide real-time device security status, which Cloudflare then uses to make access decisions.</p>
<h3 id="policy-design">Policy design</h3>
<p>Effective policy design is crucial for security and usability. Consider implementing policies that:</p>
<ul>
<li>Start with basic hygiene requirements and gradually increase security requirements</li>
<li>Account for different user roles and access needs</li>
<li>Include fallback options for exceptional circumstances</li>
</ul>
<p>Policy configuration represents another crucial aspect of the deployment. Organizations can leverage SentinelOne's detailed device posture information to create nuanced access policies. These policies can take into account multiple factors such as device infection status, active threats, and agent health. By monitoring these various attributes, organizations can ensure that only devices meeting their security requirements can access protected resources.</p>
<p>Regular testing and monitoring play vital roles in maintaining the effectiveness of the integration. Through Cloudflare's logging and testing capabilities, organizations can verify that posture checks are functioning as intended and that policies are being enforced correctly. This ongoing verification helps ensure that the security benefits of the integration are consistently realized.</p>
<h2 id="conclusion">Conclusion</h2>
<p>The integration between Cloudflare One and SentinelOne provides organizations with a powerful tool for implementing Zero Trust security principles. By combining endpoint protection with access control, organizations can ensure that only secure and compliant devices can access sensitive resources. This approach significantly reduces the risk of compromised devices accessing corporate resources while maintaining user productivity through seamless authentication and authorization processes.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://www.cloudflare.com/partners/technology-partners/sentinelone/">Overview of SentinelOne and Cloudflare partnership</a></li>
</ul>
