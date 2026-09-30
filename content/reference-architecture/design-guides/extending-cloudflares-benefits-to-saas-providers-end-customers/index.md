---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/design-guides/extending-cloudflares-benefits-to-saas-providers-end-customers/
  description: Learn how to use Cloudflare to extend performance, security, and data localization to your end users.
  full_title: Extend Cloudflare's benefits to SaaS providers' end-customers · Cloudflare Reference Architecture docs
  head_html: <title>Extend Cloudflare&#x27;s benefits to SaaS providers&#x27; end-customers · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Cloudflare to extend performance, security, and data localization to your end users."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/design-guides/extending-cloudflares-benefits-to-saas-providers-end-customers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/design-guides/extending-cloudflares-benefits-to-saas-providers-end-customers/index.md"><meta property="og:title" content="Extend Cloudflare&#x27;s benefits to SaaS providers&#x27; end-customers · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Cloudflare to extend performance, security, and data localization to your end users."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/design-guides/extending-cloudflares-benefits-to-saas-providers-end-customers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Design guide"><meta name="algolia_content_type" content="Design guide"><meta name="pcx_additional_products" content="Cloudflare Tunnel,Cloudflare for SaaS,Load Balancing,Data Localization Suite"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/reference-architecture/design-guides/extending-cloudflares-benefits-to-saas-providers-end-customers/#page","headline":"Extend Cloudflare's benefits to SaaS providers' end-customers \u00b7 Cloudflare Reference Architecture docs","description":"Learn how to use Cloudflare to extend performance, security, and data localization to your end users.","url":"https://developers.cloudflare.com/reference-architecture/design-guides/extending-cloudflares-benefits-to-saas-providers-end-customers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/design-guides/extending-cloudflares-benefits-to-saas-providers-end-customers/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>A key aspect of developing a Software-as-a-service (SaaS) application is ensuring its security against the wide array of potential attacks it faces on the Internet. Cloudflare's network and security services can be used to protect your customers using your SaaS application, off-loading the risk to a vendor with experience in <a href="https://radar.cloudflare.com/reports/ddos">protecting applications</a>.</p>
<p>This design guide illustrates how providers, building and hosting their own product/application offering, can leverage Cloudflare to extend the security, performance, and compliance benefits of Cloudflare's network to their end-customers.</p>
<p>The following diagrams visualize the use of the following services:</p>
<ul>
<li>Data Localization Suite (specifically, <a href="/data-localization/regional-services/">Regional Services</a>)</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a> to securely expose web applications (with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public hostnames</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a>)</li>
<li>Load Balancers to manage traffic and ensure reliability and performance, implementing Global Traffic Management (GTM) and <a href="/load-balancing/private-network/">Private Network Load Balancing</a>.</li>
</ul>
<p>This setup is ideal for SaaS providers who need to ensure minimal downtime, auto-renewal of SSL/TLS certificates, efficiently distribute traffic to healthy endpoints, and regional traffic management for compliance and performance optimization.</p>
<p>This document assumes that the provider's application DNS is registered and managed through Cloudflare as the primary and authoritative DNS provider. You can find details on how to set this up in the <a href="/dns/zone-setups/full-setup/">Cloudflare DNS Zone Setup Guide</a>.</p>
<p>This solution supports subdomains under your own zone while also allowing your customers to use their own domain names (vanity or custom domains) with your services. For example, for each customer you may create the custom hostname <code>mycustomer.myappexample.com</code> but also want to allow them to use their own domain, <code>app.mycustomerexample.com</code> to point to their tenant on your service. Each subdomain (<code>mycustomer.myappexample.com</code>) can be created on the main domain (<code>myappexample.com</code>) through the <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Cloudflare API</a>, allowing you to easily automate the creation of DNS records when your customers create an account on your service.</p>
<h2 id="benefits">Benefits</h2>
<p>Before looking at how Cloudflare can be configured to protect your SaaS application through your custom hostnames, it's worth reviewing the benefits of taking this approach.</p>
<table>
<thead>
<tr>
<th>Benefit</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minimized Downtime</td>
<td>Ensure <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/#minimize-downtime">minimal downtime</a> not only during custom hostname migrations to Cloudflare for SaaS but also throughout the entire lifecycle of the application.</td>
</tr>
<tr>
<td>Security and Performance</td>
<td>Extends Cloudflare's <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">security</a> and <a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/">performance</a> benefits to end-customers through their custom domains.</td>
</tr>
<tr>
<td>Auto-Renewal</td>
<td>Automates the <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/">renewal</a> and management process for custom hostname certificates.</td>
</tr>
<tr>
<td>Apex Proxying</td>
<td>Supports end-customers using <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/#apex-proxying">domain apex</a> (otherwise known as root domain) as custom hostnames. Used where your DNS service doesn't allow <a href="/dns/cname-flattening/">CNAMEs for root domains</a>, instead a <a href="/byoip/address-maps/#static-ips-or-byoip">static IP</a> is used to allow an A record to be used.</td>
</tr>
<tr>
<td>Smart Load Balancing</td>
<td>Use the load balancer as <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">custom origins</a> to steer traffic with <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>. In the context of Cloudflare for SaaS, a custom origin lets you send traffic from one or more custom hostnames to somewhere besides your default proxy fallback origin.</td>
</tr>
<tr>
<td>O2O</td>
<td>For end-customers who already proxy traffic through Cloudflare, <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a> may be required. Generally, it's recommended for those end-customers to <a href="/dns/proxy-status/#dns-only-records">not proxy</a> the hostnames used by the SaaS provider. If O2O functionality is required, please review the <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/">product compatibility</a>.</td>
</tr>
<tr>
<td>Regional Services</td>
<td>Allows <a href="/data-localization/regional-services/">regional traffic management</a> to comply with data localization requirements.</td>
</tr>
</tbody>
</table>
<h2 id="products-included-in-this-guide">Products included in this guide</h2>
<p>The following products are used to deliver this solution.</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a></td>
<td>Extends the security and performance benefits of Cloudflare’s network to your customers through their own custom or vanity domains. This includes <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">Certificate Management</a>, <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">WAF for SaaS</a>, <a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas/">Early Hints for SaaS</a> and <a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/cache-for-saas/">Cache for SaaS</a>.</td>
</tr>
<tr>
<td><a href="/ddos-protection/">DDoS Protection</a></td>
<td>Volumetric attack protection is automatically enabled for <a href="/dns/proxy-status/">proxied</a> hostnames.</td>
</tr>
<tr>
<td><a href="/data-localization/regional-services/">Regional Services</a> (part of the Data Localization Suite)</td>
<td>Restrict inspection of data (processing) to only those data centers within jurisdictional boundaries.</td>
</tr>
<tr>
<td><a href="/load-balancing/">Load Balancer</a></td>
<td>Distributes traffic across your endpoints, which reduces endpoint strain and latency and improves the experience for end users.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a></td>
<td>Secure method to connect to customers' networks and servers without creating holes in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">firewalls</a>. cloudflared is the daemon (software) installed on origin servers to create a secure tunnel from applications back to Cloudflare.</td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-for-saas-examples">Cloudflare for SaaS examples</h2>
<p>The primary objective of using Cloudflare is to ensure that all requests to your application's custom hostname are routed through Cloudflare's security and performance services first to apply security controls and routing or load balancing of traffic. Since the origin server often needs to be publicly accessible, securing the connection between Cloudflare and the origin server is crucial. For comprehensive guidance on securing origin servers, please refer to Cloudflare's documentation: <a href="/fundamentals/security/protect-your-origin-server/">Protect your origin server</a>.</p>
<p>The diagrams below begin by illustrating the simplest approach to achieving this goal, followed by more complex configurations.</p>
<h3 id="standard-fallback-origin-setup">Standard fallback origin setup</h3>
<p>This standard Cloudflare for SaaS setup is the most commonly used and easiest to implement for most providers. Typically, these providers are SaaS companies, which develop and deliver software as a service solutions. This setup requires only a single DNS record to direct requests to Cloudflare, which then proxies the traffic to your application using an A record.</p>
<p><img src="/assets/upstream/images/reference-architecture/extending-cloudflares-benefits-to-saas-providers-end-customers/standard-fallback-origin-setup.svg" alt="Figure 1: Standard fallback origin setup." title="Figure 1: Standard fallback origin setup." /></p>
<ol>
<li>The custom hostname (<code>custom.example.com</code>) is configured as a CNAME record pointing to the fallback origin of the provider. The fallback origin is the server or servers that Cloudflare will route traffic to by default when a request is made to the custom hostname. This DNS record does not need to be managed within Cloudflare; it just needs to point to the Cloudflare-hosted record from the provider (<code>fallback.myappexample.com</code>).</li>
<li>The Fallback Origin is set up as an A record that points to the public IP address of the origin server. Cloudflare will route traffic sent to the custom hostnames to this origin server by default.</li>
</ol>
<p>The origin server receives the details of the custom domain through either the <a href="/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/">host header or SNI</a>. This enables the origin server to determine which application to direct the request to. This method is applicable for both custom hostnames (for example, <code>app.mycustomerexample.com</code>) and vanity domains (for example, <code>customer1.myappexample.com</code>). Since all requests for your application are now routed through the Cloudflare network, you can leverage a range of security and performance services for every request, including:</p>
<ul>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/">Web Application Firewall</a></li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/">Access control policies</a></li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/cache-for-saas/">Caching of application content</a></li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas/">Support browser early hints</a></li>
<li><a href="/images/">Image Transformations</a></li>
<li><a href="/waiting-room/">Waiting Room</a></li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platform</a></li>
</ul>
<p>For implementation details to get started, review the <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">developer documentation</a>.</p>
<h3 id="standard-fallback-origin-setup-with-regional-services">Standard fallback origin setup with regional services</h3>
<p>This approach introduces using Cloudflare's <a href="/data-localization/regional-services/">Regional Services</a> solution to regionalize TLS termination and HTTP processing to confirm with any compliance regulations that dictate your service process data in specific geographic locations. This ensures that traffic destined for the origin server is handled exclusively within the chosen region.</p>
<p><img src="/assets/upstream/images/reference-architecture/extending-cloudflares-benefits-to-saas-providers-end-customers/standard-fallback-origin-setup-regional-services.svg" alt="Figure 2: Standard fallback origin setup with regional services." title="Figure 2: Standard fallback origin setup with regional services." /></p>
<ol>
<li>The custom hostname (<code>custom.example.com</code>) is configured as a CNAME record that points to a regionalized SaaS hostname (<code>eu-customers.myappexample.com</code>). This configuration ensures that all processing, including TLS termination, occurs exclusively within the specified geographic region.</li>
<li>The regionalized SaaS hostname is set up as a CNAME record that directs traffic to the standard <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">Fallback Origin</a> of the SaaS provider (<code>fallback.myappexample.com</code>).</li>
<li>The fallback origin is set up as an A record that points to the public IP address of the origin server. Cloudflare will route traffic sent to the custom hostnames to this origin server by default.</li>
</ol>
<h3 id="cloudflare-tunnel-as-fallback-origin-setup-with-regional-services">Cloudflare Tunnel as fallback origin setup with regional services</h3>
<p>For enhanced security, rather than exposing your application servers directly to the Internet via public IPs, SaaS providers can use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a>. These tunnels connect your network to Cloudflare's nearest data centers, allowing SaaS applications to be accessed through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public hostnames</a>. As a result, Cloudflare becomes the sole entry point for end-customers from the public Internet into your application network.</p>
<p><img src="/assets/upstream/images/reference-architecture/extending-cloudflares-benefits-to-saas-providers-end-customers/cloudflare-tunnel-fallback-origin-setup-regional-services.svg" alt="Figure 3: Cloudflare Tunnel as Fallback Origin Setup with Regional Services." title="Figure 3: Cloudflare Tunnel as Fallback Origin Setup with Regional Services." /></p>
<ol>
<li>The custom hostname (<code>custom.example.com</code>) is configured as a CNAME record that points to a regionalized SaaS hostname (<code>eu-customers.myappexample.com</code>). This configuration ensures that all processing, including TLS termination, occurs exclusively within the specified geographic region.</li>
<li>The regionalized SaaS hostname is set up as a CNAME record that directs traffic to the standard <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">Fallback Origin</a> of the SaaS provider (<code>fallback.myappexample.com</code>).</li>
<li>The fallback origin is a CNAME DNS record that points to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public hostname</a> exposed by Cloudflare Tunnel. This public hostname should be configured to route traffic to your application, for example, <code>localhost:8080</code>.</li>
</ol>
<p>This setup is ideal for SaaS providers that do not need granular load balancing, such as <a href="/load-balancing/understand-basics/traffic-steering/">geo-based traffic steering</a>, across multiple origin servers. It's also well-suited for simple testing and development environments, where <a href="/fundamentals/security/protect-your-origin-server/">protecting your origin server</a> by only allowing requests through the Cloudflare Tunnel is sufficient. However, for distributed applications requiring load balancing at both global and local levels, we recommend using <a href="/load-balancing/">Cloudflare's Load Balancer</a> with global and private network load balancing capabilities.</p>
<h3 id="global-traffic-management-gtm-private-network-load-balancing-as-custom-origin-setup">Global Traffic Management (GTM) &amp; Private Network Load Balancing as custom origin setup</h3>
<p>Cloudflare offers a powerful set of load balancing capabilities. These allow you to reliably steer traffic to different origin servers where your SaaS applications are hosted, whether through public hostnames (as described above) or private IP addresses. This setup helps prevent origin overload by distributing traffic across multiple servers and enhances security by only permitting requests through the Cloudflare Tunnel.</p>
<p><img src="/assets/upstream/images/reference-architecture/extending-cloudflares-benefits-to-saas-providers-end-customers/gtm-ltm-custom-origin-setup.svg" alt="Figure 4: Global Traffic Management (GTM) &amp; Private Network Load Balancing as custom origin setup." title="Figure 4: Global Traffic Management (GTM) &amp; Private Network Load Balancing as custom origin setup." /></p>
<ol>
<li>The custom hostname (<code>custom.example.com</code>) is configured as a CNAME record pointing to a Cloudflare <a href="/data-localization/how-to/load-balancing/">regionalized Load Balancer</a> (<code>eu-lb.myappexample.com</code>). This ensures that all processing, including TLS termination, takes place within a specified geographic region. Additionally, the SaaS provider needs to set up the load balancer as the <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">custom origin</a> for the custom hostname.</li>
<li>The regional load balancer is set up with <a href="/load-balancing/pools/">origin pools</a> to distribute requests across multiple downstream servers. Each pool can be configured to use either <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public hostnames</a> with Global Traffic Management (GTM) or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private network</a> addresses with Private Network Load Balancing. In the diagram above, we utilize both options:
<ul>
<li>Origin pool 1 uses the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/">Cloudflare Tunnel hostname</a> (<code>&lt;UUID&gt;.cfargotunnel.com</code>) as the endpoint or origin server for handling those requests.
When using a public hostname, it is necessary to set the <a href="/load-balancing/additional-options/override-http-host-headers/">HTTP host header value</a> to match the public hostname configured and exposed by the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>. This ensures that the origin server can correctly route the incoming requests.</li>
<li>Origin pool 2 uses the private IP address or private network (that is, <code>10.0.0.5</code>) within the SaaS provider's internal network, where the SaaS application resides. This pool must be configured to operate within the specified <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual network</a> to ensure proper routing of requests.</li>
</ul>
</li>
<li>Cloudflare Tunnel exposes both <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public hostnames</a> with GTM and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a> (private IPs) with Private Network Load Balancing.</li>
</ol>
<p>For enhanced granularity in application serving and scalability, it is generally recommended to use private networks rather than public hostnames. Private networks enable Cloudflare to preserve and accurately pass the host header to the origin server. In contrast, when using public hostnames, providers must configure the <a href="/load-balancing/additional-options/override-http-host-headers/">header value</a> on the load balancer, which is restricted to one public hostname per load balancer endpoint, potentially limiting flexibility.</p>
<p>Be aware of the Zero Trust <a href="/cloudflare-one/account-limits/#cloudflare-tunnel">Tunnel limitations</a>, Cloudflare for SaaS <a href="/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/">connection request details</a>, and the Custom Origin <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/#sni-rewrites">SNI specification</a>. For further information about the Cloudflare Load Balancer, review its <a href="/reference-architecture/architectures/load-balancing/">reference architecture</a>.</p>
<h2 id="automation">Automation</h2>
<p>As a SaaS provider, it is advisable to automate most, if not all, of these processes using <a href="/fundamentals/api/">APIs</a>, <a href="/fundamentals/api/reference/sdks/">SDKs</a>, scripts, <a href="/terraform/">Terraform</a>, or other automation tools.</p>
<p>An example of a high-level migration plan can be <a href="/reference-architecture/static/example-cloudflare-saas-migration-plan.pdf">downloaded here</a>.</p>
<p>It is highly recommended to migrate to Cloudflare for SaaS in phases and address any issues as they arise, particularly with <a href="/ssl/edge-certificates/changing-dcv-method/troubleshooting/">Domain Control Validation (DCV)</a>. Be sure to review the <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/">validation status</a> and relevant <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/">documentation</a> during the process.</p>
<h2 id="summary">Summary</h2>
<p>By leveraging Cloudflare's infrastructure, SaaS providers can deliver secure, reliable, and performance services to their end-customers. This ensures a seamless and secure user experience while meeting compliance requirements, such as regionalization.</p>
<p>Several Cloudflare customers are currently using the Cloudflare for SaaS solution (formerly known as SSL for SaaS). Notable public use cases include:</p>
<ul>
<li><a href="https://www.cloudflare.com/case-studies/shopify/">Shopify</a></li>
<li><a href="https://www.cloudflare.com/case-studies/porsche-informatik/">Porsche Informatik</a></li>
<li><a href="https://www.cloudflare.com/case-studies/divio/">Divio</a></li>
<li><a href="https://www.cloudflare.com/case-studies/mogenius/">mogenius</a></li>
<li><a href="https://www.cloudflare.com/case-studies/quickbutik/">Quickbutik</a></li>
</ul>
<p>Additionally, when migrating to Cloudflare for SaaS, it is crucial to have a runbook and clear public documentation to communicate relevant details to your end-customers. Excellent public examples of this are the <a href="https://help.salesforce.com/s/articleView?id=sf.community_builder_cdn.htm&amp;type=5">Salesforce CDN</a> and <a href="https://help.shopify.com/en/manual/domains/add-a-domain/connecting-domains">Shopify</a> documentation.</p>
