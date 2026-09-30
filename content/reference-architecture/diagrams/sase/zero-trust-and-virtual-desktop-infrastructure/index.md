---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/sase/zero-trust-and-virtual-desktop-infrastructure/
  description: This document provides a reference and guidance for using Cloudflare's Zero Trust services. It offers a vast improvement over remote access to web applications with greater security.
  full_title: Zero Trust and Virtual Desktop Infrastructure · Cloudflare Reference Architecture docs
  head_html: <title>Zero Trust and Virtual Desktop Infrastructure · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="This document provides a reference and guidance for using Cloudflare&#x27;s Zero Trust services. It offers a vast improvement over remote access to web applications with greater security."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/sase/zero-trust-and-virtual-desktop-infrastructure/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/sase/zero-trust-and-virtual-desktop-infrastructure/index.md"><meta property="og:title" content="Zero Trust and Virtual Desktop Infrastructure · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This document provides a reference and guidance for using Cloudflare&#x27;s Zero Trust services. It offers a vast improvement over remote access to web applications with greater security."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/sase/zero-trust-and-virtual-desktop-infrastructure/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="Access,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/sase/zero-trust-and-virtual-desktop-infrastructure/#page","headline":"Zero Trust and Virtual Desktop Infrastructure \u00b7 Cloudflare Reference Architecture docs","description":"This document provides a reference and guidance for using Cloudflare's Zero Trust services. It offers a vast improvement over remote access to web applications with greater security.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/sase/zero-trust-and-virtual-desktop-infrastructure/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/sase/zero-trust-and-virtual-desktop-infrastructure/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Virtual Desktop Infrastructure (VDI) is old, costly, and clunky for a number of reasons including poor user experience, high upfront investments, ongoing operational costs, and many others of which you can read about in detail <a href="https://blog.cloudflare.com/decommissioning-virtual-desktop/">here</a>. We recognize and empathize with the challenges many organizations face that result in continued reliance on this approach. This reference architecture describes how Cloudflare's Zero Trust solution can help organizations secure their virtual desktop infrastructure (VDI) and in most cases offload it entirely. Many organizations use expensive and poor performing VDI only to provide a secure web browser to their remote users. In these cases, Cloudflare can help offload the use of VDI entirely for web-based applications or SaaS apps.</p>
<p>In other cases, a full virtualized desktop may be necessary for legacy apps, yet organizations still need help securing remote access to their VDI or securing the virtualized desktops themselves once users are interacting with them. This document provides a reference and guidance for using Cloudflare's Zero Trust services and is split into two main sections.</p>
<ul>
<li>Replacing your VDI for secure remote access to web-based applications. Accessing a full blown desktop environment to just use a web browser isn't the best experience for users. Cloudflare offers a vast improvement over remote access to web applications and can do so with greater security.</li>
<li>Securing your VDI desktops...
<ul>
<li>From unauthorized access.</li>
<li>From risky public Internet destinations.</li>
</ul>
</li>
</ul>
<h3 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h3>
<p>This reference architecture is designed for IT or security professionals who are looking at using Cloudflare to replace or secure their Virtual Desktop Infrastructure. To build a stronger baseline understanding of Cloudflare, we recommend the following resources:</p>
<ul>
<li><a href="https://blog.cloudflare.com/decommissioning-virtual-desktop/">Decommissioning your VDI Blog Post</a></li>
<li><a href="/learning-paths/secure-internet-traffic/configure-device-agent/pac-files/#use-cases">Leveraging Cloudflare's Secure Web Gateway with PAC files for VDI</a></li>
</ul>
<h2 id="replacing-your-vdi">Replacing Your VDI</h2>
<p>In today's IT landscape, most applications and services that companies rely on are accessible through a web browser and often delivered by a SaaS provider. In these cases VDI is overkill and an incredibly expensive and burdensome way to provide a secure browser to a remote user. Instead, many organizations are turning to alternatives such as a <a href="https://www.cloudflare.com/zero-trust/products/browser-isolation/">Remote Browser Isolation</a> (RBI) service. These services lower costs and overhead, provide a better user experience and most importantly offer robust security and logging features.</p>
<p><img src="/assets/upstream/images/reference-architecture/zero-trust-and-virtual-desktop-infrastructure/figure1.svg" alt="Figure 1: Remote browser isolation can provide a secure, controlled browser environment for accessing sensitive company applications." title="Figure 1: Remote browser isolation can provide a secure, controlled browser environment for accessing sensitive company applications." /></p>
<p>The diagram above shows the general flow of how user traffic goes from their local browser to Cloudflare's remote browser and then to applications hosted on their infrastructure over a secure tunnel. Figure 2 below shows how users can access applications using remote browser isolation either directly in a browser or, if you require greater privacy and security for the traffic, using our device agent to create a tunnel from the device to Cloudflare. Both methods provide secure access to internal and external resources.</p>
<p><img src="/assets/upstream/images/reference-architecture/zero-trust-and-virtual-desktop-infrastructure/figure2.svg" alt="Figure 2: Two different traffic flow options: clientless RBI &amp; RBI using the device agent." title="Figure 2: Two different traffic flow options: clientless RBI &amp; RBI using the device agent." /></p>
<p><strong>Option 1: Clientless RBI</strong></p>
<ul>
<li>Device agent not required</li>
<li>RBI URL can be protected by an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> with authentication</li>
<li>A simpler way to begin rolling out Cloudflare Zero trust while transitioning away from VDI</li>
<li>A great option for third party contractor access who cannot install software on their device</li>
</ul>
<p><strong>Option 2: RBI via the device agent</strong></p>
<ul>
<li>Provides full security capabilities including device posture checks, split tunneling and the ability to use the Secure Web Gateway service to filter Internet-bound traffic.</li>
<li>More robust end state to transition to once workflows and confidence is built with users and internal teams</li>
<li>Gather end user metrics around user experience, reliability and performance</li>
</ul>
<h2 id="securing-your-vdi">Securing Your VDI</h2>
<h3 id="securing-access-to-your-vdi-using-zero-trust-policies">Securing access to your VDI using Zero Trust policies</h3>
<p>When replacing your VDI is not an option and a fully virtualized desktop is required for legacy applications, Cloudflare's <a href="https://www.cloudflare.com/zero-trust/">SASE platform</a> can still help secure these environments by authorizing the access to them using identity based Zero Trust policies, as well as securing the Internet bound traffic from the devices themselves.</p>
<p><img src="/assets/upstream/images/reference-architecture/zero-trust-and-virtual-desktop-infrastructure/figure3.svg" alt="Figure 3: Using Cloudflare Access ZTNA to secure VDI." title="Figure 3: Using Cloudflare Access ZTNA to secure VDI." /></p>
<p>The diagram above displays a general Zero Trust deployment using best practices for authenticating your remote users to the VDI infrastructure</p>
<ol>
<li>The user device sends traffic to Cloudflare's network over a secure tunnel using the device agent.</li>
<li>Traffic destined to the VDI resources reaches ZTNA policies where it is evaluated for any combination of conditional access criteria, including device posture, identity and traffic context or type.</li>
<li>Traffic that passes the ZTNA policies is allowed to reach the VDI resources where the user can interact with the VDI normally.</li>
</ol>
<p>This model could also benefit from the below options demonstrating how to filter traffic sourced from the VDI hosts as well (refer to below).</p>
<h3 id="securing-traffic-from-your-vdi-using-secure-web-gateway-policies">Securing traffic from your VDI using secure web gateway policies</h3>
<p>Cloudflare's SASE platform is capable of much more than replacing VPNs and bolstering policies towards internal services. It is just as important to protect users from accessing high risk sites on the Internet. Policies in Cloudflare's Secure Web Gateway can be tuned to filter DNS requests or become a sophisticated full forward proxy, inspecting both network and HTTP traffic as it heads towards the open Internet.</p>
<p><img src="/assets/upstream/images/reference-architecture/zero-trust-and-virtual-desktop-infrastructure/figure4.svg" alt="Figure 4: Using Cloudflare's Secure Web Gateway to filter and protect traffic coming from VDI." title="Figure 4: Using Cloudflare's Secure Web Gateway to filter and protect traffic coming from VDI." /></p>
<ol>
<li>
<p><strong>DNS configurations</strong> (Resolver IPs, DoH, DoT) or <strong>PAC files</strong> for <strong>Non-persistent virtual desktop infrastructure (VDI) environments</strong> can be configured within the infrastructure or directly on the VDI hosts</p>
<p>a. DNS configurations allow for DNS policies to be enforced while PAC files allow for all gateway policy types (DNS, Network and HTTP).</p>
</li>
<li>
<p>Traffic is sent from the VDI to the secure web gateway where it is filtered by DNS, network or HTTP policies.</p>
</li>
<li>
<p>Traffic is sent to the Internet if it is allowed past Gateway policies</p>
</li>
</ol>
<h2 id="summary">Summary</h2>
<p>As shown, we have seen several ways to incorporate Cloudflare's Zero Trust services with your existing VDI, either by replacing it completely in favor of Remote Browser Isolation technology or further securing it with our <a href="/cloudflare-one/access-controls/policies/">Access</a> or <a href="/cloudflare-one/traffic-policies/">Gateway</a> services.</p>
<p>For more thorough background, explanation and action steps to a smooth migration be sure to read the following resources:</p>
<ul>
<li><a href="https://blog.cloudflare.com/decommissioning-virtual-desktop/">Decommissioning your VDI Blog Post</a></li>
<li><a href="/learning-paths/secure-internet-traffic/configure-device-agent/pac-files/#use-cases">Leveraging Cloudflare's Secure Web Gateway with PAC files for VDI</a></li>
<li><a href="https://blog.cloudflare.com/browser-isolation-private-network/">Connect to private network services with Browser Isolation</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation">Clientless Web Isolation</a></li>
<li><a href="/learning-paths/secure-internet-traffic/configure-device-agent/pac-files/#use-cases">Determine When to use PAC Files</a></li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/">Agentless DNS Configurations</a></li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC Files for Agentless HTTP Filtering</a></li>
</ul>
<p>As always, if you have any questions on these services, be sure to reach out to your Cloudflare team or contact us to <a href="https://www.cloudflare.com/products/zero-trust/plans/enterprise/">talk to an expert</a>.</p>
