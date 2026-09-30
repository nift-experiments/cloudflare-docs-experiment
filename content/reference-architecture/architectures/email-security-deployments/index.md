---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/architectures/email-security-deployments/
  description: This reference architecture describes the key architecture of Cloudflare Email security.
  full_title: Understanding Email Security Deployments · Cloudflare Reference Architecture docs
  head_html: <title>Understanding Email Security Deployments · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="This reference architecture describes the key architecture of Cloudflare Email security."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/architectures/email-security-deployments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/architectures/email-security-deployments/index.md"><meta property="og:title" content="Understanding Email Security Deployments · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This reference architecture describes the key architecture of Cloudflare Email security."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/architectures/email-security-deployments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture"><meta name="algolia_content_type" content="Reference architecture"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/reference-architecture/architectures/email-security-deployments/#page","headline":"Understanding Email Security Deployments \u00b7 Cloudflare Reference Architecture docs","description":"This reference architecture describes the key architecture of Cloudflare Email security.","url":"https://developers.cloudflare.com/reference-architecture/architectures/email-security-deployments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/architectures/email-security-deployments/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Email continues to be a mission critical method for communication between people and organizations. This also makes email an ideal channel for attackers to exploit in their attempts to take over accounts, steal data, and gain access to internal systems. Being able to reduce spam, defeat phishing, and malware attacks is critical for the security of your organization. Over 90% of cybersecurity incidents begin with an email attack.</p>
<p>Cloudflare Email security service is a market leading solution that can be deployed in a variety of ways to support different needs for each organization. This document outlines the different methods to deploy Email security and why you would choose any specific model.</p>
<h2 id="strengthen-your-email-infrastructure-with-cloudflare-email-security">Strengthen your email infrastructure with Cloudflare Email security</h2>
<p>Email remains a critical communication channel for businesses of all sizes. However, email also serves as a prime target for cyber attacks, including phishing, spam, and malware. To safeguard your organization sensitive data and reputation, a robust email security solution is essential.</p>
<p>Cloudflare Email security offers a comprehensive suite of tools and technologies designed to protect your email infrastructure from a wide range of threats. By implementing Cloudflare Email security, you can significantly enhance your organization security posture and mitigate the risks associated with email-borne attacks.</p>
<p>This reference architecture provides a detailed overview of how to deploy and configure Cloudflare Email security to optimize your email security posture. This reference architecture will delve into key components and best practices to ensure the seamless integration of this solution into your existing IT infrastructure.</p>
<h3 id="who-is-this-reference-architecture-for-and-what-will-you-learn">Who is this reference architecture for and what will you learn?</h3>
<p>This reference architecture is designed for IT or security professionals who are looking at using Cloudflare to secure aspects of their business. This reference architecture is designed for a broad audience, including:</p>
<ul>
<li><strong>IT security professionals</strong>: Security engineers, architects, and administrators responsible for designing, implementing, and managing Email security solutions.</li>
<li><strong>Network engineers</strong>: Network engineers who manage network infrastructure and email gateways.</li>
<li><strong>Cloud architects</strong>: Cloud architects who design and implement cloud-based Email security solutions.</li>
<li><strong>Security and IT decision-makers</strong>: Managers and executives who need to understand the technical aspects of Email security and make informed decisions.</li>
</ul>
<p>Whether you are a seasoned security expert or a newcomer to Email security, this document will provide you with the necessary information to effectively deploy and manage Cloudflare Email security.</p>
<p>To build a stronger understanding of Cloudflare, we recommend the following resources:</p>
<ul>
<li>What is Cloudflare? | <a href="https://www.cloudflare.com/what-is-cloudflare/">Website</a> (five-minute read) or <a href="https://www.cloudflare.com/what-is-cloudflare/video">Video</a> (two minutes)</li>
<li><a href="https://blog.cloudflare.com/tag/cloud-email-security/">Cloudflare Blog</a> | <a href="https://blog.cloudflare.com/tag/cloud-email-security/">Email security</a> and <a href="https://blog.cloudflare.com/tag/phishing/">Phishing</a></li>
<li>CISA | <a href="https://www.cisa.gov/publications/phishing-guidance-stopping-attack-cycle-phase-one">Phishing Guidance: Stopping the Attack Cycle at Phase One</a></li>
</ul>
<p>By the end of this reference architecture, you will have learned how Cloudflare protects your email and what considerations should be made for choosing how to deploy. You will learn about the specific components, technologies, and configurations involved in the Cloudflare Email security solution. This includes how it integrates with existing email infrastructure and leverages cloud-based services.</p>
<h2 id="email-security-deployment-options">Email security deployment options</h2>
<p>Cloudflare Email security is a modern approach to solving phishing attacks. Cloudflare solution is built upon AI and Machine Learning utilizing elastics services in addition to benefiting from Cloudflare expansive threat intelligence network. Cloudflare Email security was designed as the only true Cloud Elastic Service with shared intelligence and <a href="https://www.ibm.com/think/topics/supervised-learning">Supervised ML</a> capable of any deployment method available for email. However, choosing the right deployment model is crucial for maximizing the benefits of Email security.</p>
<p>This document will discuss the following methods to deploy and where you would use them:</p>
<ul>
<li><a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/">Inline or MX</a></li>
<li><a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/">Microsoft 365 API integration</a></li>
<li><a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/journaling-setup/m365-journaling/">Journaling</a> or <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/">BCC</a> with auto-move</li>
<li>Mixed deployment</li>
</ul>
<h2 id="choose-a-deployment-model">Choose a deployment model</h2>
<p>Before you choose a deployment option, it is important to consider your needs and desired experience. Our best practice is typically to go with an MX deployment when we are the primary phishing protection in place. The key reasons for this are as follows:</p>
<ul>
<li><a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/">Pre-delivery</a> remediation allows us to tune how messages are delivered by appending to the subject/body, applying URL Rewriting to Cloudflare <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>, and delivering messages into the junk folder or downstream email quarantine. This enables you to design with a specific user experience in mind.</li>
<li>We can remove messages before they are consumed by systems that ingest emails such as a ServiceNow or an Archiving Solution.</li>
<li>We remove the risk of dwell time issues where there is a time difference between delivery to the inbox and when the message is moved from the inbox.</li>
<li>We can support mixed deployments such as a mix of Microsoft 365 and Microsoft Exchange or Microsoft 365 and Google Workspace.</li>
</ul>
<p>If those needs are not important or you are using layered security that does not include another API-based solution, then our API method is quick and efficient to deploy with no changes to your mail flow. If you want the benefits of API without the risk of API Throttling, then Journal/BCC is the best choice as the ingestion method does not use API calls. However, if you want the protection of an MX deployment along with the benefits of API for internal messaging, then our mixed deployment is ideal.</p>
<p>Should your needs change, know that you have the flexibility to change deployment methods as you see fit without having to repurchase our solution. The only caveat is that Advantage and CyberSafe customers are limited to Inline deployments while Enterprise licensing benefits from all capabilities.</p>
<p>Before you commit to a specific deployment, Cloudflare suggests you review all of the options, weigh your needs, and consult with your account team as needed.</p>
<h2 id="deployment-options">Deployment options</h2>
<h3 id="inline">Inline</h3>
<p>With an Inline deployment, all emails destined for one or more domains are filtered through Cloudflare before they are delivered to the user's inbox. Cloudflare can be deployed anywhere in your email processing chain. When deployed as the first <span class="nb-glossary-tooltip" title="Hops">hop</span>, you will need to update the domain's DNS MX records to point to Cloudflare. If you prefer Cloudflare to inspect messages after your existing SEG (Secure Email Gateway), Cloudflare can be inserted as a hop in the processing chain, and will then forward processed messages downstream to the next hop. Based on policies, messages are blocked and/or quarantined if they are marked as Spam, Malicious, Bulk, and more.</p>
<p><img src="/assets/upstream/images/reference-architecture/understanding-email-security-deployments/Inline_MX.svg" alt="Inline deployment" /></p>
<p>The diagram above describes the following:</p>
<ol>
<li>Email arrives at Cloudflare based on <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-mx-record/">MX records</a>.</li>
<li>Cloudflare inspects email body, header, and attachments and assigns the appropriate disposition:
<ul>
<li>Malicious</li>
<li>Spam</li>
<li>Bulk</li>
<li>Suspicious</li>
<li>Spoof</li>
<li>Clean</li>
</ul>
</li>
<li>Apply any policy, such as allow or block certain domains.</li>
<li>Quarantine high risk emails</li>
<li>All messages that received a <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a> by Cloudflare will have the header <code>X-CFEmailSecurity-Disposition</code> added. This header can be used by downstream systems to enact any special handling (rerouting, external quarantining, and more).</li>
<li>Forward on all valid email traffic.</li>
<li>Subject and/or body modifications can be applied to the messages to add visible information for the end-user about the disposition.</li>
</ol>
<p>From a security perspective, the Inline deployment is the preferred method of deployment, because it scans every email and stops malicious content from reaching the user inbox. This removes all exposure risks to users.</p>
<h4 id="benefits-of-inline-deployment">Benefits of Inline deployment</h4>
<ul>
<li>Messages are processed and blocked before delivery to the user mailbox.</li>
<li>Inline deployment allows you to modify the message, adding subject or body mark-ups such as appending [SPAM] or [EXTERNAL SPAM] to the subject.</li>
<li>Provides high availability and adaptive message pooling as Cloudflare will continue to accept incoming emails in queue, even when the downstream services are not available. When the downstream services are restored, messages will resume delivery for the queue.</li>
<li>Messages with an assigned <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a> that are not quarantined receive an <code>X-header</code> that may be used for advanced handling downstream.</li>
<li>Compatible with all mail systems including Microsoft Exchange On-Prem, Postfix, Lotus Notes, Google Workspace, Microsoft 365, and more.</li>
</ul>
<h4 id="considerations">Considerations</h4>
<p>Before deploying Email security via Inline deployment, you will need to consider the following:</p>
<ol>
<li>Redirecting deployments where mail flows into Microsoft Exchange or Microsoft 365 first, then to an Email security solution by way of mail flow rules for scanning/remediation, and then back into Microsoft 365 is not supported by Microsoft. While Cloudflare is technically capable of this deployment, it creates attribution (recognizing the original sender) and delivery issues.</li>
<li>If Cloudflare is going to be the MX, this will require DNS changes. If there are many domains, each DNS zone needs to be updated.</li>
<li>Inline deployment can increase complexity in the SMTP architecture if Cloudflare is not deployed as MX such as Inline behind a traditional SEG (Mimecast/ProofPoint).</li>
<li>Inline deployment may require policy duplication on multiple solutions and the MTA. For example, Cloudflare, SEGs, and MTA treat allow policies in significantly different ways and may all need exception handling for the same message.</li>
<li>In a layered deployment, some vendors such as Mimecast and Barracuda can only function as the MX. In this scenario, you would configure Cloudflare Inline behind those vendors.</li>
<li>When using Mimecast, it is recommended to disable URL Rewriting as it makes it impossible for Cloudflare to decode and crawl URLs. If this feature remains enabled, our link following capabilities are limited to domain reputation and age.</li>
</ol>
<h4 id="inline-cisco-connector">Inline (Cisco Connector)</h4>
<p>Cisco offers a unique capability to integrate with Cloudflare using a connector as MX or behind Cloudflare with a supportable Hairpin deployment. This deployment functions the same as Inline in all other considerations. Refer to Cisco as MX Record and Cisco - Email security as MX Record.</p>
<h3 id="api">API</h3>
<p>An alternative approach is to integrate via the Graph <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/">API</a> in Microsoft 365. In this model, emails are delivered directly to the user inbox, where Cloudflare then receives copies of messages, scans them, and moves them as configured by <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a>.</p>
<p>This is performed by subscribing to all user mailboxes on the authorized domains. You have the ability to choose if the scope should be restricted to the Inbox only, or All Folders during the authorization process. Upon delivery to the mailbox, the subscription triggers an action within Microsoft 365 that sends Cloudflare a copy of the email to be scanned and assigned a disposition. Once the disposition has been assigned, our solution will look at the <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move</a> policy and perform the desired action.</p>
<p><img src="/assets/upstream/images/reference-architecture/understanding-email-security-deployments/API.svg" alt="API deployment" /></p>
<p>The diagram above describes the following:</p>
<ol>
<li>An email is delivered directly to the user inbox via an existing route.</li>
<li>Cloudflare retrieves messages for inspection via email vendors API. Cloudflare inspects email body, header, and attachments and assigns the appropriate disposition:
<ul>
<li>Malicious</li>
<li>Spam</li>
<li>Bulk</li>
<li>Suspicious</li>
<li>Spoof</li>
<li>Clean</li>
</ul>
</li>
<li>Apply any policy, such as allow or block certain domains.</li>
<li>Messages are moved per policy in the Cloudflare solution. The following actions are available:
<ul>
<li>Inbox</li>
<li>Junk</li>
<li>Trash</li>
<li>Soft Delete (User Recoverable)</li>
<li>Hard Delete (Admin Recoverable)</li>
</ul>
</li>
</ol>
<p>Under normal circumstances, this process is typically performed in less than 2-3 seconds from inbox delivery to the move request. There is no SLA from Google or Microsoft 365 on how long they will take to perform the action. If the move action is not successful, our solution will retry numerous times every five minutes.</p>
<h4 id="benefits-of-api-deployment">Benefits of API deployment</h4>
<ul>
<li>Easy way to add protection in complex email architectures with no changes to mail flow operations.</li>
<li>Agentless deployment for Microsoft 365.</li>
<li>Microsoft 365 Defender/ATP operates on the message first.</li>
<li>This method can be used for a Proof of Value to collect and report on emails without requiring changes to mail flow. In this scenario you would leave the remediation policy not configured to prevent actions being taken.</li>
</ul>
<h4 id="considerations-1">Considerations</h4>
<p>Before deploying Email security via <a href="/cloudflare-one/email-security/setup/post-delivery-deployment/api/m365-api/">API deployment</a>, you will need to consider the following:</p>
<ul>
<li>Depending on the API infrastructure, Microsoft 365 or Google outages and maintenance windows will increase message dwell time in the inbox as emails cannot be scanned or remediated until after delivery to the user. This is a limitation of all API vendors.</li>
<li>Microsoft 365 may throttle API requests to the Graph API on a Service by Service basis. The Mail API with Graph is within the Outlook Services section. These limits could be abused by a threat actor to functionally disable any API based deployment granting an additional window for attack. The limits are as follows:
<ul>
<li>10,000 API requests in a 10 minute period</li>
<li>Four concurrent requests</li>
<li>150 megabytes (MB) upload (PATCH, POST, PUT) in a five-minute period</li>
<li>Refer to <a href="https://learn.microsoft.com/en-us/graph/throttling-limits#outlook-service-limits">Outlook service limits</a></li>
</ul>
</li>
<li>The Gmail API is subject to a daily usage limit that applies to all requests made from your application, and per-user rate limits. Each limit is identified in terms of quota units, or an abstract unit of measurement representing Gmail resource usage. The main request limits are described as follows:
<ul>
<li>Per user rate limit of 250 quota units per user per second, moving average (allows short bursts).</li>
<li>Per-method Quota Usage is based on the number of quota units consumed by a request depending on the method called.</li>
<li>For example, <code>messages.get</code> and <code>messages.attachments.get</code> consume five quota units. Refer to <a href="https://developers.google.com/gmail/api/reference/quota#per-method_quota_usage">Per-method quota usage</a></li>
</ul>
</li>
<li>Requires read/write access into mailboxes which some security/email teams may not allow.</li>
<li>Only Microsoft 365 has true API support. Google allows for API remediation but still requires a Compliance Rule to deliver emails using SMTP for scanning. On-prem Exchange requires PowerShell and does not have APIs for auto-moves.</li>
<li>Messages cannot be modified after delivery as per Microsoft 365/Google requirements. This means we cannot perform URL Rewriting to Cloudflare <a href="/cloudflare-one/email-security/investigation/search-email/#open-links">email link isolation</a> or append text to the email subject or body. Those features are only available using an Inline deployment.</li>
</ul>
<h3 id="bcc-journaling">BCC/Journaling</h3>
<p>BCC/Journaling is very similar to API deployments with the exception of how emails are delivered to Cloudflare. As with API the email is delivered to the mailbox first, but at the same time an account specific email address is added to the email so a copy is transmitted via SMTP to Cloudflare for evaluation.</p>
<p>Once Cloudflare receives the email, it will scan and determine the <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a> of the email. Once an email has a disposition our solution will look at the API authorizations and <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move</a> policy and perform the desired action. This method is less at risk to API Throttling as the APIs for Microsoft 365 and Google are only used to remediate emails.</p>
<p><img src="/assets/upstream/images/reference-architecture/understanding-email-security-deployments/Journaling_Diagram.svg" alt="BCC/Journaling deployment" /></p>
<p>During a proof of value, this deployment can be configured with any Email security solution or mail platform that allows for adding a BCC recipient to gain visibility into what those solutions are missing that Cloudflare would block.</p>
<h4 id="benefits-of-bcc-journaling-deployment">Benefits of BCC/Journaling deployment</h4>
<ul>
<li>Easy way to add protection in complex email architectures with no changes to mail flow operations.</li>
<li>Agentless deployment for Microsoft 365. Microsoft 365 would transmit emails after delivery to Cloudflare and the API Authorization can be configured with a Remediation policy to move emails with a disposition out of the inbox.</li>
<li>Google makes use of Compliance Rules for BCC which can be combined with an API Authorization to move emails after delivery. This provides for the same outcome as the API deployment detailed above.</li>
<li>Microsoft 365 and Google operate on the message first. This provides a more layered approach taking advantage of the security capabilities of Microsoft 365/Google in addition to Cloudflare.</li>
<li>You can control the scope of messages inspected (external, internal, or both)</li>
<li>This method can be used for a Proof of Value to collect and report on emails without requiring changes to mail flow. This does not require an API Authorization to be in place. If the API is configured for Microsoft 365 or Google, you would leave the Remediation policy not configured to prevent actions being taken.</li>
</ul>
<h4 id="considerations-2">Considerations</h4>
<p>Before deploying Email security via BCC/Journaling deployment, you will need to consider the following:</p>
<ul>
<li>Same limitations of API.</li>
<li>Depends on Google or Microsoft 365 to deliver messages via SMTP.</li>
<li>May require a Connector in Microsoft 365 to facilitate direct communication.</li>
<li>Messages cannot be modified after delivery as per Microsoft 365/Google requirements. This means we cannot perform URL Rewriting to Cloudflare Email Link Isolation or append text to the email Subject or Body. Those features are only available using an Inline deployment.</li>
</ul>
<h3 id="mixed">Mixed</h3>
<p>Mixed utilizes an Inline deployment for external emails and BCC/Journaling for internal emails. This is facilitated by using both deployment methods but configuring Cloudflare for two hops in BCC/Journal mode. This scenario provides all of the added benefits of an MX delivery for external messages, while also providing remediation of bad emails from internal sources. Here are some scenarios where this is helpful.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/12713.md")
</div>
<h4 id="benefits">Benefits</h4>
<p>mixed deployment combines the benefits of Inline deployment for external emails and BCC/Journaling for internal emails.</p>
<h4 id="considerations-3">Considerations</h4>
<p>When you choose mixed deployment, you need to consider that:</p>
<ul>
<li>Internal email detections are limited due to a lack of information such as Email Authentication, Sending Server, and Delivery Path. Only the content within the body of the email can be analyzed.</li>
<li>Internal emails may have higher False Positives when using Protecting Users with impersonation registry.</li>
</ul>
<h2 id="automated-post-delivery">Automated Post Delivery</h2>
<p>Cloudflare offers automated workflows based on continuous analysis and submissions. These features enable Cloudflare to move messages using the API <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move</a> policy after delivery. This is best paired with the phish submissions or third-party user submissions.</p>
<h3 id="submission-handling">Submission Handling</h3>
<p>Cloudflare prioritizes Administrator Submissions for false positives and negatives through the Cloudflare dashboard. This approach enables faster review times and helps Cloudflare proactively identify and correct issues that may affect multiple users improving the overall product experience. It is recommended that administrators review user submissions, identify all related messages, and submit as verified false positive/false negatives via the Cloudflare dashboard. These submissions will be reviewed and used to improve Machine Learning Models, Detections, and Engines in the future.</p>
<h2 id="summary">Summary</h2>
<p>To summarize, Email security offers three core deployment models: API, BCC/Journaling, and Inline (or MX). Inline is the preferred deployment model as it filters and remediates malicious messages before they reach the user inbox, thereby removing dwell time risk and allowing for features like URL Rewriting and message modification.</p>
<p>API and BCC/Journaling models are post-delivery solutions, integrating directly with platforms like Microsoft 365 or Google Workspace to inspect and <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move</a> emails after they have landed in the user mailbox. While these post-delivery methods are easier to deploy and require no mail flow changes, they face limitations such as API throttling risks and the inability to modify message content (like subjects or body text).</p>
<p>Finally, the mixed deployment combines the benefits of Inline for external email protection (critical for systems like CRM or ticketing that ingest email) with BCC/Journaling for internal email evaluation.</p>
