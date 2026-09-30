<h2 id="introduction">Introduction</h2>
<p>When building a SaaS application, it is common to create unique hostnames for each customer account (or tenant), for example <code>app.customer.com</code>. It is important to ensure that all communication to this application hostname is done using SSL/TLS and therefore a certificate must be created for your customer's hostname on your application. Certificate management is hard, and often application architects and developers would use a <a href="https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/">multi-domain certificate</a> (MDC), so they can buy and add just one certificate that has hundreds of domains listed. However, this does not scale well when your application reaches thousands and millions of customers.</p>
<p>Also, a customer of your application might wish to have their main website domain hosted directly on your application. So that, for example, <code>www.customer.com</code> is actually delivering content directly from your SaaS application.</p>
<p>Many SaaS applications have caching and security solutions, such as Cloudflare, in front of their applications and as such need to onboard these hostnames. This is often done using a &quot;Zone&quot; model, where inside Cloudflare, or another vendor such as AWS Cloudfront, a &quot;Zone&quot; is created for <code>app.customer.com</code>. This means that, as each new customer is onboarded, a new &quot;Zone&quot; must be created - this might be manageable in the tens and hundreds of customers but, when you get to thousands and millions, management of all these zones and their configurations is hard.</p>
<p>Cloudflare for Platforms extends far beyond this traditional model of most edge providers, by managing traffic across many hostnames and domains in one &quot;Zone&quot;. You can now manage <code>www.customer1.com</code> and <code>www.customer2.net</code>, and millions more hostnames, through the same configuration while also customizing features as needed.</p>
<p>This document provides a reference and guidance for using Cloudflare for Platforms. The document is split into three main sections.</p>
<ul>
<li>Overview of the SaaS model and the common challenges Cloudflare for Platforms solves</li>
<li>SSL certificate issuance in a SaaS model</li>
<li>Customizing the experience for each of your clients</li>
</ul>
<h3 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h3>
<p>This reference architecture is designed for SaaS application owners, engineers, or architects who want to learn how to make their application more scalable and secure through Cloudflare.</p>
<p>To build a stronger baseline understanding of Cloudflare, we recommend the following resources:</p>
<ul>
<li>What is Cloudflare? | <a href="https://www.cloudflare.com/what-is-cloudflare/">Website</a> (5 minute read) or <a href="https://www.youtube.com/watch?v=XHvmX3FhTwU">video</a> (2 minutes)</li>
<li><a href="/ruleset-engine/">Cloudflare Ruleset Engine</a> - We will discuss integrations with the ruleset engine. Familiarity with that feature will be helpful.</li>
<li><a href="/workers/">Cloudflare Workers</a> - We will also discuss integrations with Cloudflare Workers, our serverless application platform. A basic familiarity with this platform will be helpful.</li>
</ul>
<p>Those who read this reference architecture will learn:</p>
<ul>
<li>How Cloudflare's unique offering can solve key challenges for SaaS applications</li>
<li>How to customize the Cloudflare experience for each of your end customers</li>
<li>Tools to integrate serverless applications, for each of your clients, through Workers for Platforms</li>
</ul>
<h2 id="why-cloudflare-for-platforms">Why Cloudflare for Platforms?</h2>
<h3 id="the-saas-model">The SaaS model</h3>
<p>Software as a Service (SaaS) has been a key innovation of the cloud computing era. On premises managed legacy enterprise software - such as accounting, HR, and CRMs - required dedicated attention from IT personnel to establish a platform (whether dedicated hardware, VMs, or cloud instances) for each application in the enterprise. The SaaS model allows providers, like Shopify and Salesforce, to extend their own platform to their customers instead. Now, the customer does not have to provision hardware or consider any other infrastructure concerns; instead, they subscribe to access to the SaaS platform which is always up to date, secure and available.</p>
<h3 id="third-party-hostname-challenges">Third party hostname challenges</h3>
<p>For many SaaS applications, it is important to provide a service under the client's own domain. Their domain is important for branding, security, and organization; and many clients have heavily invested in the right <code>.com</code> to represent their business. Many clients with domains linked to their brand will push back against deploying their applications on the provider's domain.</p>
<p>This is especially true for customer-facing applications like an e-commerce solution. You would want to expose this as <code>shop.example.com</code>, not <code>example.shop.com</code>. To secure traffic to the SaaS application, the provider (&quot;shop&quot;) needs a certificate for their customer, <code>example.com</code>.</p>
<p><img src="/assets/upstream/images/reference-architecture/leveraging-cloudflare-for-your-saas-applications/figure1.svg" alt="Figure 1: eCommerce flow through a SaaS platform." title="Figure 1: eCommerce flow through a SaaS platform." /></p>
<p>This is a challenge for SaaS solutions, as certificate issuance is tightly controlled through the <a href="/ssl/edge-certificates/changing-dcv-method/dcv-flow/">DCV Validation process</a>. The owner of a domain needs to authorize any certificates, and traditional methods of validation are driven by the domain owner and deliver the certificate only to them.</p>
<p><img src="/assets/upstream/images/reference-architecture/leveraging-cloudflare-for-your-saas-applications/figure2.svg" alt="Figure 2: Certificates cannot be automatically renewed on legacy platforms. They will expire and break traffic without manual action." title="Figure 2: Certificates cannot be automatically renewed on legacy platforms. They will expire and break traffic without manual action." /></p>
<p>This poses a dilemma: the SaaS model offers clear advantages but introduces a new challenge of its own. A novel solution would let providers and end customers both get the most out of the SaaS model.</p>
<h2 id="issuing-ssl-certificates-through-cloudflare-for-platforms">Issuing SSL certificates through Cloudflare for Platforms</h2>
<h3 id="manage-certificates-for-any-hostname-on-the-internet">Manage certificates for any hostname on the Internet</h3>
<p>Cloudflare for SaaS provides a unique solution to these common challenges for SaaS providers. By leveraging Cloudflare's position as a low-latency, global network, we can transparently manage certificate issuance for end clients while also providing several other benefits to a SaaS platform.</p>
<h3 id="secure-and-powerful-validation-modes">Secure and powerful validation modes</h3>
<p>Cloudflare has a unique ability to manage the Domain Control Validation (DCV) process in a SaaS scenario. In a traditional model, certificate issuers ask domain owners to place a <a href="/ssl/edge-certificates/changing-dcv-method/dcv-flow/#dcv-tokens">particular token</a> (either a DNS TXT record or a small text file) at their origin in order to validate that they are authorized for that domain. This has to be done repeatedly at certificate renewal, which has become more common with recent security improvements.</p>
<p><img src="/assets/upstream/images/reference-architecture/leveraging-cloudflare-for-your-saas-applications/figure3.svg" alt="Figure 3: The DCV process." title="Figure 3: The DCV process." /></p>
<p>Since Cloudflare's network can easily sit in between the client and the SaaS provider, we can automatically respond with the correct DCV token on behalf of any domain that points traffic to the SaaS provider on Cloudflare.</p>
<p><img src="/assets/upstream/images/reference-architecture/leveraging-cloudflare-for-your-saas-applications/figure4.svg" alt="Figure 4: Certificates automatically renew on Cloudflare-enabled platforms." title="Figure 4: Certificates automatically renew on Cloudflare-enabled platforms." /></p>
<p>Instead of repeatedly performing a complex process at every certificate renewal, the client performs a much simpler process only once.</p>
<h2 id="customize-your-customers-cloudflare-experience">Customize your customers Cloudflare experience</h2>
<h2 id="managed-features-in-cloudflare-for-platforms">Managed features in Cloudflare for platforms</h2>
<p>Cloudflare for Platforms gives you much more than just SSL certificate management. We give you built-in features to control security and performance capabilities, at scale, for each of your clients. Cloudflare's security features, such as <a href="/ddos-protection/">DDoS</a>, <a href="/waf/">WAF</a>, <a href="/bots/">Bot Management</a>, and <a href="/waf/rate-limiting-rules/">Rate Limiting</a> are seamlessly extended to clients on your platform. Security posture can be customized within <a href="/waf/managed-rules/">Managed Rules</a> for individual customers, to exempt good traffic or tighten security. On the <a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/">performance</a> side, <a href="/cache/">Cache</a>, <a href="/argo-smart-routing/">Argo Smart Routing</a>, and HTTP/2 features like <a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas/">Early Hints</a> provide scalable and customizable behavior for all of your customers. Customizable cache rules lets you drive high hit rates across all of your customers.</p>
<p>If you need even more flexibility than our rules provide, to give individual behavior to thousands or millions of customers, <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">Custom Metadata</a> allows complete per-client flexibility. By setting tags like <code>WAF: On</code> or <code>Performance: Premium</code> for each customer, you can customize their security and performance feature set. We have built features like <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">WAF for SaaS</a> which interface with this metadata directly; as well as an API within our Workers serverless environment to use them within custom code.</p>
<h2 id="scalable-serverless-applications-with-workers-for-platforms">Scalable serverless applications with Workers for Platforms</h2>
<p>If you need more customization than even metadata can provide, or are running a service where your customers write or generate their own application code, <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> lets you deploy a complete serverless application for each of your customers.</p>
<p>We provide several key features such as the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dispatch Worker</a>, which gives you infinite flexibility in deciding which customer application to route to. For example, you can run security checks, then decode an HTTP header telling you the user's ID, and then load the appropriate serverless application for this user's request. <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">Outbound Workers</a> give you additional visibility and control into what Internet resources your customer's applications can access, providing a familiar security model in a distributed deployment.</p>
<p>We also provide features for <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/observability/">observability</a>, <a href="/terraform/">configuration</a>, and many other tools needed for a production-grade platform deployment. These are detailed in other <a href="/reference-architecture/">reference architectures</a> and function the same way for platform cases as for the more standard models described in those guides.</p>
<h2 id="use-cases">Use cases</h2>
<p>Let's review three common use cases where Cloudflare for Platforms can enable providers to seamlessly extend SSL, performance, and security to their end customers.</p>
<h3 id="ssl-issuance-at-scale-for-your-platform">SSL issuance at scale for your platform</h3>
<p>In this common design, Cloudflare enables your platform to issue SSL certificates and provide performance and security features. We will not customize the features for each of your clients, but will provide common capabilities for everyone who uses the platform.</p>
<ol>
<li>Cloudflare secures traffic from your clients to your platform, at global scale, by validating and distributing SSL certificates.</li>
<li>In this design, you will use the same L7 configuration - that is, all of the features that act on your traffic, and run after SSL, for each of your clients.</li>
<li>Just set up a <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Cloudflare for SaaS</a> zone and <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/">order a custom hostname</a> for each client hostname. The system will take you through an easy flow to point each client's traffic to your platform, and order their certificate.
<ol>
<li>You can almost always use our default settings through this process, but bespoke SSL customization is also possible.</li>
<li>Origin traffic routing is also handled through the SSL for SaaS process. Our default configuration is secure for most needs.
<ul>
<li>For highly secure use cases, you can use <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a>, <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a>, or an advanced design with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Tunnels</a>.</li>
</ul>
</li>
</ol>
</li>
</ol>
<p><img src="/assets/upstream/images/reference-architecture/leveraging-cloudflare-for-your-saas-applications/figure5.svg" alt="Figure 5" /></p>
<h3 id="feature-customization-for-your-platform-customers">Feature Customization for your Platform customers</h3>
<p>Here, we are not just provisioning a certificate for each client - we are giving each of them a custom configuration. For example, your Basic tier only gets essential WAF, Advanced tier gets Bot management. You can also run common features across all customers.</p>
<ol>
<li>In addition to securing SSL traffic, use an additional field provided when you add each customer (<a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">Custom Metadata</a>) to tag the correct feature set.</li>
<li>Cloudflare features read the Metadata to customize for each client. <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">WAF features are the key security customization</a>. Provide different levels of security, or even customized WAF rulesets.</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/">On the performance side,</a> you can also add Argo Smart Routing, Cache, and Early Hints to level up the performance for chosen customers.</li>
</ol>
<p><img src="/assets/upstream/images/reference-architecture/leveraging-cloudflare-for-your-saas-applications/figure6.svg" alt="Figure 6" /></p>
<h3 id="serverless-application-platform-for-your-customers">Serverless application platform for your customers</h3>
<p>In the most advanced design, we are customizing a full serverless application in our Workers runtime for each of your customers. Simple Workers perform similar tasks to feature customization. Advanced Workers can run your entire platform on the Cloudflare network.</p>
<ol>
<li>Instead of deploying customized Cloudflare capabilities, each customer has their own &quot;User Worker&quot; JavaScript serverless application containing custom code.</li>
<li>You retain control through Dispatch Workers, which determine which code to run, and Outbound Workers, which restrict the access of customer code.</li>
<li>Use advanced Developer Platform capabilities like D1, Workers KV, and Queues to build your entire business on Cloudflare.</li>
</ol>
<p><img src="/assets/upstream/images/reference-architecture/leveraging-cloudflare-for-your-saas-applications/figure7.svg" alt="Figure 7" /></p>
<h2 id="summary">Summary</h2>
<p>With Cloudflare for SaaS, you will be able to easily solve the common challenges that come with a growing platform business. From SSL certificate issuance, through Security, and on to custom serverless applications, Cloudflare for SaaS lets you scale our entire platform to your customers - at the scale of millions.</p>
<p>You can find further details on all of the features we have discussed here in the following links:</p>
<ul>
<li><a href="/cloudflare-for-platforms/">Cloudflare for Platforms</a></li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">Custom metadata</a></li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></li>
</ul>
