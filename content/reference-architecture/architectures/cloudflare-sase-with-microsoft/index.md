<h2 id="introduction">Introduction</h2>
<p>In today's rapidly evolving digital landscape, organizations are increasingly embracing cloud migration to modernize their environments and enhance productivity. Microsoft has emerged as a leading provider of cloud applications and services, offering a comprehensive suite of solutions to support hybrid work. However, this shift to the cloud also presents new challenges and risks that must be addressed to ensure the security and integrity of an organization's resources.</p>
<p>As organizations migrate to hybrid and multi-cloud environments, they often face the complexity of managing a combination of Software as a Service (SaaS), self-hosted, and non-web applications. This heterogeneous ecosystem can complicate the process of securing and controlling access to these resources. Additionally relying on legacy, often on-premises, Virtual Private Network (VPN) solutions to securely connect users to applications can introduce security gaps and hinder employee productivity.
To overcome these challenges and achieve greater security outcomes, organizations can benefit from partnering with Cloudflare, a leading provider of cloud security and performance solutions. Cloudflare offers seamless integration with Microsoft's cloud ecosystem, enabling customers to eliminate security gaps, enhance performance, and ensure reliability across their hybrid work environments.</p>
<p>In this reference architecture diagram, we will explore how the combination of Cloudflare's Secure Access Service Edge (SASE) platform and Microsoft's cloud applications and services can help you attain a Zero Trust security posture and accelerate cloud modernization and productivity while providing comprehensive security for hybrid work. By leveraging Cloudflare's secure network access, risky user isolation, and application and data visibility, organizations can consolidate management through a unified interface and enable secure access to any resource, regardless of location.</p>
<h3 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h3>
<p>This reference architecture is designed for IT or security professionals with some responsibility over or familiarity with their organization's Microsoft deployments. It is designed to help you understand the different ways in which Microsoft and Cloudflare can be integrated together in terms of your Zero Trust and SASE programs.</p>
<p>To build a stronger baseline understanding of Cloudflare, we recommend the following resources:</p>
<ul>
<li>What is Cloudflare? | <a href="https://www.cloudflare.com/what-is-cloudflare/">Website</a> (5 minute read) or <a href="https://youtu.be/XHvmX3FhTwU?feature=shared">video</a> (2 minutes)</li>
</ul>
<ul>
<li>Solution Brief: <a href="https://cfl.re/SASE-SSE-platform-brief">Cloudflare One</a> (3 minute read)</li>
<li>Whitepaper: <a href="https://cfl.re/internet-native-transformation-wp">Reference Architecture for Internet-Native Transformation</a> (10 minute read)</li>
<li>Blog: <a href="https://blog.cloudflare.com/zero-trust-sase-and-sse-foundational-concepts-for-your-next-generation-network/">Zero Trust, SASE, and SSE: foundational concepts for your next-generation network</a> (14 minute read)</li>
</ul>
<p>Those who read this reference architecture will learn:</p>
<ul>
<li>How Cloudflare and Microsoft can be integrated together to protect users, devices, applications and networks from a Zero Trust perspective</li>
</ul>
<p>This document is also accompanied by a reference architecture with a more indepth look at <a href="/reference-architecture/architectures/sase/">Cloudflare and SASE</a>.</p>
<p>While this document examines Cloudflare at a technical level, it does not offer fine detail about every product in the platform. Visit the <a href="https://developers.cloudflare.com/">developer documentation</a> for further information specific to a product area or use case.</p>
<h2 id="integration-of-cloudflare-with-microsoft">Integration of Cloudflare with Microsoft</h2>
<p>Cloudflare's <a href="https://www.cloudflare.com/zero-trust/products/access/">Zero Trust Network Access</a> (ZTNA) provides a faster and safer alternative to traditional VPNs. It replaces on-premises VPN infrastructure and protects any application, regardless of whether it is hosted in an on-premises network, public cloud, or as Software as a Service (SaaS). By integrating with Microsoft Intune and Microsoft Entra ID (formerly Azure Active Directory), Cloudflare's ZTNA service enables organizations to enforce default-deny, Zero Trust rules and provide conditional access to internal resources based on user identity and device posture.</p>
<p>Microsoft and Cloudflare can be integrated in the following ways.</p>
<ul>
<li>Using Microsoft <a href="https://learn.microsoft.com/en-us/entra/fundamentals/whatis">Entra ID</a> for authentication to all Cloudflare protected resources</li>
<li>Leveraging Microsoft <a href="https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune">Intune</a> device posture in Cloudflare policies to ensure only managed, trusted devices have access to protected resources</li>
<li>Using Cloudflare <a href="/cloudflare-one/integrations/cloud-and-saas/">CASB</a> to inspect your <a href="https://www.microsoft.com/en-us/microsoft-365/what-is-microsoft-365">Microsoft 365</a> tenants and alert on security findings for incorrectly configured accounts and shared files containing sensitive data</li>
<li>Using Cloudflare's <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a> to control access to Microsoft SaaS applications such as Outlook, OneDrive and Teams</li>
<li>Using Cloudflare's <a href="/email-security/">Email security</a> service to increase protection of email from phishing attacks and business email compromise.</li>
</ul>
<h3 id="microsoft-entra-id-with-cloudflare">Microsoft Entra ID with Cloudflare</h3>
<p>Cloudflare's integration with Entra ID allows you to leverage your identities in Entra for authentication to any Cloudflare protected application. Groups can also be imported via SCIM to be used in access policies, simplifying management and abstracting access control by managing group membership in Entra ID.</p>
<ul>
<li>Entra ID enables administrators to create and enforce policies on both applications and users using Conditional Access policies.</li>
<li>It offers a wide range of parameters to control user access to applications, such as user risk level, sign-in risk level, device platform, location, client apps, and more.</li>
<li>Security teams can define their security controls in Entra ID and enforce them at the network layer, for every request, with Cloudflare's ZTNA service.</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-microsoft/cloudflare-sase-with-microsoft-fig1.svg" alt="Figure 1: Microsoft Entra ID integrates with Cloudflare for ZTNA access to SaaS and self hosted applications." title="Figure 1: Microsoft Entra ID integrates with Cloudflare for ZTNA access to SaaS and self hosted applications." /></p>
<h3 id="microsoft-intune-with-cloudflare">Microsoft Intune with Cloudflare</h3>
<p>Cloudflare is able to enforce access policies that include information about device posture. Intune can be integrated into Cloudflare so that information about Intune managed and protected devices can be used to enforce access control to Cloudflare protected resources.</p>
<ul>
<li>With a device connected using our <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">agent</a>, Cloudflare's ZTNA service can leverage the enhanced telemetry and context provided by Intune regarding a user's device posture and compliance state.</li>
<li>Intune provides detailed information about the security status and configuration of user devices, enabling more informed access control decisions.</li>
<li>This integration allows administrators to ensure that only compliant and secure devices are granted access to critical networks and applications.</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-microsoft/cloudflare-sase-with-microsoft-fig2.svg" alt="Figure 2: Figure 2: Using Intune and Cloudflare device posture data for secure application access." title="Figure 2: Using Intune and Cloudflare device posture data for secure application access." /></p>
<h3 id="cloudflare-casb-for-microsoft-365">Cloudflare CASB for Microsoft 365</h3>
<p>As companies adopt numerous SaaS applications, maintaining consistent security, visibility, and performance becomes increasingly difficult. With each application having unique configurations and security requirements, IT teams face challenges in staying compliant and protecting sensitive data across the diverse landscape.</p>
<p>Cloudflare CASB (Cloud Access Security Broker) addresses these challenges by providing extensive visibility across Microsoft 365 and other popular SaaS applications. This visibility enables organizations to quickly identify misconfigurations, exposed files, user access, and third-party access, ensuring a secure and compliant SaaS environment.</p>
<p>Learn more about how our CASB solution can <a href="/reference-architecture/diagrams/security/securing-data-at-rest/">protect data at rest here</a>.</p>
<h3 id="cloudflare-s-secure-web-gateway-for-improved-security-to-microsoft-saas-applications">Cloudflare's Secure Web Gateway for improved security to Microsoft SaaS applications</h3>
<p>Cloudflare's Secure Web Gateway (SWG) can help organizations achieve safe and secure access to Microsoft 365 in the following ways:</p>
<ol>
<li>Traffic inspection and filtering: Cloudflare's SWG inspects all user and device traffic destined for the Internet, including traffic to Microsoft 365. This allows organizations to apply security policies, content filtering, and threat prevention measures to ensure that only legitimate and authorized traffic reaches Microsoft 365 services.
As seen above, policies can be designed so that only managed, secure devices can access any part of the Microsoft 365 and Azure platform.</li>
<li>Data protection with DLP profiles: Traffic is not only inspected based on device posture and identity information, but our DLP engine can also examine the content of the request and allow/block downloads/uploads of confidential information to and from Microsoft 365 and Azure.</li>
<li>Enforce Cloudflare gateway: Microsoft 365 can be configured to accept user traffic only from a specific range of IP addresses. Cloudflare makes it possible to define and associate IP addresses attached to all traffic leaving the SWG. This means that organizations can configure Microsoft 365 to only accept traffic coming from the IP address range designated by Cloudflare SWG, ensuring that all traffic has been inspected and approved by Cloudflare's security policies before reaching Microsoft 365.</li>
</ol>
<p>By leveraging Cloudflare SWG as a secure gateway for Microsoft 365 access, organizations can benefit from advanced threat protection, granular access controls, traffic inspection, and centralized visibility, ensuring a safe and secure experience for their users while mitigating risks and maintaining compliance.</p>
<h3 id="cloudflare-s-email-security-for-improved-email-protection">Cloudflare's Email security for improved email protection</h3>
<p>Phishing is the root cause of upwards of 90% of breaches that lead to financial loss and brand damage. Cloudflare's email security solution sits in front of all email going to your Microsoft 365 tenant, filtering out spam, bulk, malicious and spoof content. The solution can leverage Microsoft <a href="/email-security/deployment/inline/setup/office-365-area1-mx/use-cases/four-user-quarantine-admin-quarantine/">rules for quarantine actions</a>, allowing you to fine tune how different email detections are handled.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-microsoft/cloudflare-sase-with-microsoft-fig3.svg" alt="Figure 3: Cloud email security protects all Microsoft 365 inboxes." title="Figure 3: Cloud email security protects all Microsoft 365 inboxes." /></p>
<p>It is also possible to configure cloud email security to scan <a href="/email-security/deployment/api/">Microsoft 365 inboxes via API</a>, avoiding the need to make changes to existing DNS records.</p>
<h2 id="summary">Summary</h2>
<p>By leveraging Cloudflare and its integrations with Microsoft, organizations can establish a Zero Trust security posture that goes beyond the limitations of traditional network security models. With Cloudflare's Zero Trust Network Access (ZTNA), organizations can replace self hosted VPNs and enforce conditional access based on user identity and device posture. The integration with Microsoft Entra ID allows for authentication and access control, while Microsoft Intune provides device posture information. Additionally, Cloudflare's CASB offers visibility into the security of Microsoft 365 configuration, the Secure Web Gateway inspects and filters traffic to Microsoft 365, and Email security protects against phishing attacks, ensuring a secure and compliant environment. This approach enables faster and more secure access to applications, while providing granular control over user access based on identity and device posture.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-sase-with-microsoft/cloudflare-sase-with-microsoft-fig4.svg" alt="Figure 4: A summary of Cloudflare SASE and Microsoft integrations." title="Figure 4: A summary of Cloudflare SASE and Microsoft integrations" /></p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://www.cloudflare.com/partners/technology-partners/microsoft/">Overview of Microsoft and Cloudflare partnership</a></li>
<li><a href="/cloudflare-one/integrations/identity-providers/entra-id/#set-up-entra-id-as-an-identity-provider">Set up Microsoft Entra ID (formerly Azure Active Directory) as an identity provider</a></li>
</ul>
