<h2 id="introduction">Introduction</h2>
<p>Data at rest refers to data that is stored in a fixed location, such as on a local hard drive, on-premises server, or cloud storage. Many businesses today are using SaaS platforms that store a lot of business data in structured forms (like databases) and unstructured forms (files like documents, images, spreadsheets). The security of the actual storage of the data, such as encryption and reliable backups, is usually abstracted from your control. But the SaaS applications allow you to manage user accounts, define what data they have access to, and also provide an ability to share access to data.</p>
<p>While Cloudflare mostly secures data in transit as it travels over our network, we also have the ability to connect to your SaaS applications and use our DLP profiles to examine data at rest that might not be adequately secured and then provide recommendations for you to take action.</p>
<h2 id="protecting-data-with-cloudflare-casb">Protecting data with Cloudflare CASB</h2>
<p>Cloudflare's API-driven <a href="/cloudflare-one/integrations/cloud-and-saas/">Cloud Access Security Broker</a> (CASB) works by integrating with SaaS APIs and discovering both unstructured data at rest (documents, spreadsheets, and so on) and also examining general configuration of the application and user accounts to ensure data access controls are correctly configured.</p>
<p><a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">DLP profiles</a> are used to discover if files stored in your SaaS application contain sensitive data. Matches are then compared with access controls and findings are generated, such as findings to alert you to a spreadsheet that contains credit card information that is accessible by anyone on the Internet.</p>
<p>When Cloudflare CASB is combined with Cloudflare's <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a> service, which inspects all the traffic going to and from a SaaS application, customers can achieve comprehensive visibility into both data in transit and data at rest for SaaS applications.</p>
<p><img src="/assets/upstream/images/reference-architecture/securing-data-at-rest/securing-data-at-rest-fig1.svg" alt="Figure 1: Overall solution of user access controls to, and the discovery of, sensitive data." title="Figure 1: Overall solution of user access controls to, and the discovery of, sensitive data." /></p>
<h2 id="securing-user-access-to-data-at-rest">Securing user access to data at rest</h2>
<ol>
<li>
<p>Cloudflare authenticates users attempting to access SaaS applications, whether they are initiating the request from managed or unmanaged endpoints.</p>
<ol>
<li>For managed endpoints, we recommend deploying our <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">device agent</a> to maximize visibility and control of all traffic between the end user’s device and the resources being requested.</li>
<li>For unmanaged endpoints, we have <a href="/reference-architecture/diagrams/sase/sase-clientless-access-private-dns/">client-less solutions</a> which all you to still have visibility over and inspection into the data accessed by users.</li>
</ol>
</li>
<li>
<p>Cloudflare's <a href="/cloudflare-one/access-controls/policies/">Zero Trust Network Access</a> (ZTNA) service can integrate directly with your <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">SaaS applications</a> using standard protocols (e.g. SAML or OIDC) to become the initial enforcement point for user access. Access calls your <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> (IdP) of choice and uses additional security signals about your users and devices to make policy decisions.</p>
</li>
<li>
<p>As an extension of what was covered in Securing data in use, Cloudflare <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a> (RBI) can also be used with <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a>, so that even remote clientless user’s traffic can arrive at the requested SaaS application from predictable and consistent IP addresses.</p>
</li>
</ol>
<h2 id="discovering-and-protecting-the-data-at-rest">Discovering and protecting the data at rest</h2>
<ol start="4">
<li>
<p>In addition to what we covered in Securing data in transit, Cloudflare Data Loss Prevention (DLP) can be used to discover files that reside in your SaaS applications that contain sensitive data. CASB will scan every shared and/or publicly accessible file in the SaaS app for sensitive text that matches the DLP profile and alert you with recommended actions to take.</p>
</li>
<li>
<p>To complement the dedicated egress IP option mentioned above, SaaS providers enable the ability to restrict access to your organization's resources by only permitting access when traffic is sourced from specific IP addresses.</p>
</li>
<li>
<p>When you integrate a third-party SaaS application with Cloudflare CASB, CASB makes routine, out-of-band API calls that analyze the associated metadata of your configurations, users, files, and other SaaS ‘objects’. Security issues, or ‘Findings’, are then detected based on whether the metadata indicates any insecure or potentially hazardous configurations exist within the integrated SaaS applications. This can include application misconfigurations, exposed and/or sensitive data, and users accounts with poor security.</p>
</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/reference-architecture/diagrams/security/securing-data-in-transit/">Securing data in transit</a></li>
<li><a href="/reference-architecture/diagrams/security/securing-data-in-use/">Securing data in use</a></li>
</ul>
