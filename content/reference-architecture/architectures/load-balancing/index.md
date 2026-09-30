---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/
  description: This reference architecture is for organizations looking to deploy both global and local traffic management load balancing solutions. It is designed for IT, web hosting, and network professionals with some responsibility over or familiarity with their organization's existing infrastructure.
  full_title: Load Balancing Reference Architecture · Cloudflare Reference Architecture docs
  head_html: <title>Load Balancing Reference Architecture · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="This reference architecture is for organizations looking to deploy both global and local traffic management load balancing solutions. It is designed for IT, web hosting, and network professionals with some responsibility over or familiarity with their organization&#x27;s existing infrastructure."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/index.md"><meta property="og:title" content="Load Balancing Reference Architecture · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This reference architecture is for organizations looking to deploy both global and local traffic management load balancing solutions. It is designed for IT, web hosting, and network professionals with some responsibility over or familiarity with their organization&#x27;s existing infrastructure."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture"><meta name="algolia_content_type" content="Reference architecture"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/#page","headline":"Load Balancing Reference Architecture \u00b7 Cloudflare Reference Architecture docs","description":"This reference architecture is for organizations looking to deploy both global and local traffic management load balancing solutions. It is designed for IT, web hosting, and network professionals with some responsibility over or familiarity with their organization's existing infrastructure.","url":"https://developers.cloudflare.com/reference-architecture/architectures/load-balancing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/architectures/load-balancing/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Cloudflare Load Balancing is a SaaS offering that allows organizations to host applications for a global user base while vastly reducing concerns of maintenance, failover, resiliency, and scalability. Using Cloudflare Load Balancing allows organizations to address the following challenges:</p>
<ul>
<li>Efficiently handling large volumes of incoming traffic, especially during unexpected surges or spikes.</li>
<li>Ensuring applications and services remain accessible to users.</li>
<li>Maintaining quick response times and optimal performance for all users, especially during high traffic periods.</li>
<li>Adapting to changing traffic demands and ensuring the infrastructure can accommodate growth.</li>
<li>Helping applications and services resist Distributed Denial of Service (DDoS) attacks.</li>
</ul>
<p>Cloudflare Load Balancing is built on Cloudflare’s connectivity cloud, ​​a unified, intelligent platform of programmable cloud-native services that enable secure any-to-any connectivity between all networks (enterprise and Internet), cloud environments, applications, and users. It is one of the largest global networks, with data centers spanning <div class="nb-data-component" data-cf-component="PublicStats"></div> and interconnection with <div class="nb-data-component" data-cf-component="PublicStats"></div>. It also has a greater presence in core Internet exchanges than many other large technology companies.</p>
<p>As a result, Cloudflare operates within ~50 ms of ~95% of the world’s Internet-connected population. And since all Cloudflare services are designed to run across every network location, all requests are routed, inspected, and filtered close to their source, resulting in strong performance and consistent user experiences.</p>
<p>This document describes a reference architecture for organizations looking to deploy both global and local traffic management load balancing solutions.</p>
<h3 id="who-is-this-document-for-and-what-will-you-learn">Who is this document for and what will you learn?</h3>
<p>This reference architecture is designed for IT, web hosting, and network professionals with some responsibility over or familiarity with their organization's existing infrastructure. It is useful to have some experience with networking concepts such as routing, DNS, and IP addressing, as well as basic understanding of load balancer functionality.</p>
<p>To build a stronger baseline understanding of Cloudflare and its load balancing solution, we recommend the following resources:</p>
<ul>
<li>What is Cloudflare? | <a href="https://www.cloudflare.com/what-is-cloudflare/">Website</a> (5 minute read) or <a href="https://youtu.be/XHvmX3FhTwU?feature=shared">video</a> (2 minutes)</li>
</ul>
<ul>
<li>Solution Brief: <a href="https://cf-assets.www.cloudflare.com/slt3lc6tev37/4mn2dtdw7TvSwCUJw8mMf5/f1fa6269f4468c432560b2c9f5ebd38a/Cloudflare_Local_Traffic_Manager_Solution_Brief.pdf">Cloudflare Private Network Load Balancing</a> (5 minute read)</li>
<li>Solution Brief: <a href="https://cf-assets.www.cloudflare.com/slt3lc6tev37/5OWUduF4YBKYADj3zREAX6/5241a81a3fc4ff1db7c9bade14991b23/Cloudflare_Global_Traffic_Manager__GTM__Solution_Brief.pdf">Cloudflare GTM Load Balancing</a> (5 minute read)</li>
<li>Blog: <a href="https://blog.cloudflare.com/elevate-load-balancing-with-private-ips-and-cloudflare-tunnels-a-secure-path-to-efficient-traffic-distribution/">Elevate load balancing with Private IPs and Cloudflare Tunnels: a secure path to efficient traffic distribution</a> (13 minutes)</li>
</ul>
<p>Those who read this reference architecture will learn:</p>
<ul>
<li>How Cloudflare Load Balancing can address both Private Network Load Balancing and global traffic management use cases.</li>
<li>How Cloudflare’s global network enhances the functionality of Cloudflare Load Balancing.</li>
<li>The capabilities of Cloudflare Load Balancers, and how they apply to various use cases.</li>
<li>The structure of Cloudflare Load Balancers and their various configurations.</li>
</ul>
<h2 id="handling-dynamic-workloads-in-modern-applications">Handling dynamic workloads in modern applications</h2>
<h3 id="concepts-and-terminology">Concepts and terminology</h3>
<h4 id="endpoint">Endpoint</h4>
<p>In this document, the term “endpoint” is any service or hardware that intercepts and processes incoming public or private traffic. Since load balancing can be used for more than just web servers, the term endpoint has been chosen to represent all possible types of origins, hostnames, private or public IP addresses, virtual IP addresses (VIPs), servers, and other dedicated hardware boxes. It could be on-premises or hosted in a public or private cloud — and could even be a third-party load balancer.</p>
<h4 id="steering">Steering</h4>
<p>Steering is a load balancer’s main function — the process of handling, sending, and forwarding requests based on a set of policies. These policies generally take many factors into account, including request URL, URL path, HTTP headers, configured weights, priority, and endpoint latency, responsiveness, capacity, and load.</p>
<h4 id="layer-7">Layer 7</h4>
<p><a href="https://www.cloudflare.com/learning/ddos/what-is-layer-7/">Layer 7</a> of the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a>, also known as the application layer, is where protocols such as SSH, FTP, NTP, SMTP, and HTTP(S) reside. When this document refers to layer 7 or layer 7 load balancers, it means HTTP(S)-based services. The Cloudflare layer 7 stack allows Cloudflare to apply services like DDoS protection, Bot Management, WAF, CDN, Load Balancing, and more to a customer's website to improve performance, availability, and security.</p>
<h4 id="layer-4">Layer 4</h4>
<p>Layer 4 of the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a> — also called the transport layer — is responsible for end-to-end communication between two devices. Network services that operate at layer 4 can support a much broader set of services and protocols. Cloudflare’s public layer 4 load balancers are enabled by a product called Spectrum, which works as a layer 4 reverse proxy. In addition to offering load balancing, Spectrum provides protection from <a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">DDoS attacks</a> and can conceal the endpoint IP addresses.</p>
<h4 id="ssl-tls-offloading">SSL/TLS Offloading</h4>
<p>SSL (Secure Sockets Layer) and its successor TLS (Transport Layer Security) are cryptographic protocols used to secure connections over the Internet. SSL and TLS offloading, also known as SSL/TLS termination or SSL/TLS acceleration, is a technique used in load balancers and web servers to handle the SSL/TLS encryption and decryption process without affecting an endpoint’s performance. SSL/TLS offloading improves server performance, simplifies certificate management, and enhances scalability by offloading the resource-intensive encryption and decryption tasks to dedicated devices, helping endpoints remain dedicated to serving content and application logic.</p>
<h3 id="challenges-addressed-by-load-balancers">Challenges addressed by load balancers</h3>
<p>Modern websites, or any applications for that matter, face three main challenges:</p>
<ol>
<li><strong>Performance:</strong> Ensuring that the application responds to users requests and input in a timely manner</li>
<li><strong>Availability:</strong> Maintaining the uptime for the application, so it is always able to respond to user requests</li>
<li><strong>Scalability:</strong> Growing, shrinking, or relocating application resources based on user behavior or demand.</li>
</ol>
<h4 id="performance">Performance</h4>
<p>Application performance can be affected by several factors, but the most common cause of performance issues is the amount of usage or load placed on an endpoint. An endpoint generally has a finite amount of compute resources it can provide. If too many requests arrive at once, or if the type of requests cause increased CPU/memory usage, the endpoint will respond slower or fail to respond at all.</p>
<p>To address these challenges, endpoints can be upgraded with more compute resources. But during idle or low-usage times, the organization ends up paying for underutilized resources. Organizations may also deploy multiple endpoints — but to seamlessly steer traffic between them, a load balancing solution is needed to make this process seamless to the end user.</p>
<p>Figure 1 shows how load might be distributed without a load balancer:</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-1.svg" alt="Endpoint load is not distributed evenly without a load balancer" title="Figure 1: Endpoint performance can suffer without a load balancer" /></p>
<p>Load balancers allow organizations to host several endpoints and portion out traffic between them, ensuring no single endpoint gets overwhelmed. The load balancer handles all incoming requests and forwards them to the appropriate endpoint. The client doesn’t need any knowledge of endpoint availability or load — it just needs to send the request to the load balancer and the load balancer handles the rest. Figure 2 shows how a load balancer can evenly distribute traffic from users across a set of endpoints.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-2.svg" alt="A load balancer helps evenly distribute requests across multiple endpoints" title="Figure 2: Load balancers help distribute load across endpoints" /></p>
<p>Another performance-related issue has to do with the distance between a client and an endpoint. Whether due to the mere fact of traveling farther, or having to make more network hops, a request that travels a longer distance generally has a higher round-trip time (RTT).</p>
<p>RTT becomes important at scale. For example, if a client and endpoint are both located in the United States, it would be reasonable to expect a RTT of 25ms. If the client has 20 requests it needs responses to, the total time required to handle them sequentially (not including compute time) would be 500ms (20 x 25ms). And if the same client connected from the APAC region the RTT might be upwards of 150ms, resulting in an undesirable total loading time of 3000ms (20 x 150ms). (Certainly, request streaming enhancements in HTTP/2 and HTTP/3 might change this math — but in websites with dynamic or interactive content, where a response’s information is used to generate additional requests, the example still holds in general.) Figure 3 illustrates how this happens.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-3.svg" alt="Latency compounds based on the number of requests" title="Figure 3: How latency can compound and affect the total time it takes to load a resource" /></p>
<p>In the same way a load balancer can pass traffic to a less-busy endpoint, it can also pass traffic to a geographically closer endpoint, resulting in a more responsive experience for the client. Specifically, the load balancer performs a lookup of the IP address that sent the request, determines its location, and selects the closest or most region-appropriate endpoint to send it to (this is similar to functionality provided by DNS solutions like GeoDNS).</p>
<h4 id="availability">Availability</h4>
<p>Service availability encompasses both unintentional and intentional downtime of endpoints behind a load balancer. Several factors can contribute to unintentional downtime, including hardware failure, software bugs, network issues, and ISP or other vendor issues. Even for the most advanced organizations, these issues are inevitable.</p>
<p>Load balancers solve these issues by always monitoring the health of endpoints. If an endpoint is slow to respond to a health check, or fails to respond entirely, the endpoint is marked as unhealthy. Several methods exist for monitoring, including basic health tests like ICMP (ping) and TCP connection tests. More advanced health tests can be used like issuing an HTTP GET request and ensuring a specific response code and response body are returned from the endpoint. Once an endpoint is in a degraded state, the load balancer will send fewer or no requests its way in favor of healthier endpoints. As the endpoint becomes operational again and the load balancer is able to receive responses to its health checks, the endpoint is marked as operational and has traffic steered towards it once more.</p>
<p>Intentional downtime comes in a few different forms, including capacity changes, hardware or infrastructure upgrades, and software updates. Load balancers gracefully remove traffic from one or more endpoints to allow for such maintenance.</p>
<h4 id="scale">Scale</h4>
<p>Effective application scaling helps organizations meet customer or user demand and avoid unnecessary billing or charges. During traffic increases, organizations may need to temporarily deploy more endpoints to ensure the service stays performant and available. However, constantly having enough endpoints online to meet your maximum possible traffic could be costly regardless whether the endpoint is located on-premises or via a cloud provider like AWS, GCP, or Azure. Load balancers allow for dynamic increases or decreases in capacity by monitoring requests, connections, and latency to the endpoints.</p>
<p>Another type of scale to consider is geographic scale. As services grow in popularity, endpoint location becomes more important. Users in a different geographic region than an endpoint may have slower response times and receive a lower quality of service than users in the same region. As organizations deploy new endpoints in different regions, they have to decide how they want to distribute their traffic. This challenge has been met by different layers of load balancing called global traffic management (GTM) and Private Network Load Balancing. This document describes both of these in detail in the following section — but in summary, the GTM load balancer handles the initial request (typically via DNS) and then selects and steers traffic to the Private Network Load Balancer that is deployed close to endpoints in the appropriate geographic region.</p>
<h3 id="types-of-traffic-management">Types of traffic management</h3>
<p>As mentioned, load balancing for global applications and services comes in two layers. The first layer is called Global Traffic Management or Manager (GTM), which may also be called Global Server Load Balancing (GSLB). The second layer is called Private Network Load Balancing, which may also be referred to as Server Load Balancing (SLB). This section will define the purpose of these different types of load balancing and how they work together.</p>
<h4 id="global-traffic-manager-global-traffic-management-gtm">Global traffic manager / global traffic management (GTM)</h4>
<p>A Global Traffic Manager is responsible for routing requests, generally from the Internet, to the proper region or data center. Many GTM load balancers operate at the DNS layer, allowing them to:</p>
<ul>
<li>Resolve a DNS request to an IP address based on geographic region or physical location.</li>
<li>Provide the IP of the endpoint or service closest to the client, so it can connect.</li>
</ul>
<p>Figure 4 shows how a GTM load balancer is used to select a data center based on the client location or region.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-4.svg" alt="Global traffic management steers traffic to the proper region or data center" title="Figure 4: Global traffic management load balancer overview" /></p>
<p>Global Traffic Managers can also proxy traffic and perform a variety of inspections, including reading/changing/deleting headers in HTTP requests and modifying URLs based on region or geographic location. GTM functionality is best implemented by cloud-based load balancers (like Cloudflare) since the goal is to steer traffic from anywhere in the world. Hardware load balancers exist in a single physical location, which means the further traffic originates from the load balancer, the slower the end-user experience. A cloud-based load balancer can run in many different geographic locations, helping it provide a performant solution for DNS-only, layer 4, and layer 7 contexts.</p>
<h4 id="private-network-load-balancing">Private Network Load Balancing</h4>
<p>Private Network Load Balancing steers traffic within a data center or geographic location. A Private Network Load Balancer can be responsible for load balancing, SSL/TLS offloading, content switching, and other application delivery functions. Private Network Load Balancing ensures efficient distribution of client requests across multiple endpoints to improve performance and ensure high availability. Private Network Load Balancers are usually placed inside private networks and are used to load balance publicly or privately accessible resources. In Figure 5 below, the GTM load balancer has selected the Europe data center to direct a request to the Europe data center’s Private Network Load Balancer which will then steer it to the appropriate endpoint.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-5.svg" alt="Private Network Load Balancing is responsible for steering to the final endpoint or destination" title="Figure 5: Private Network Load Balancer overview" /></p>
<p>Private Network Load Balancer and their endpoints usually sit behind firewalls. But while endpoints may be protected on private networks, accessibility to the Private Network Load Balancer can be either public or private depending on deployment requirements. A Private Network Load Balancer will monitor total requests, connections, and endpoint health to ensure requests are steered towards endpoints capable of responding in a timely manner.</p>
<h4 id="on-premises-vs-cloud-based-load-balancers">On-premises vs cloud-based load balancers</h4>
<p>There are two main load balancer architectures:</p>
<ul>
<li>On-premises load balancers
<ul>
<li>Typically hardware-based, but also can be virtualized or software-based</li>
<li>Focused on maximum performance</li>
</ul>
</li>
<li>Cloud-based load balancers
<ul>
<li>Software deployed on public cloud infrastructure</li>
<li>Handle requests closer to the originator of the request</li>
</ul>
</li>
</ul>
<p>Each approach has advantages and disadvantages. On-premises load balancers usually exist inside of private networks completely controlled by the organization. These load balancers are collocated with the endpoints they are load balancing, so latency and RTT time should be minimal. The disadvantage of these on-premises load balancers is that they are restricted to a single physical location. Which means traffic from other regions can have long RTT and high latency in responses. Also, adding another data center requires purchasing and deploying all new equipment. On-premises load balancers also typically require cloud-based load balancers for geographic traffic steering to get requests routed by a geographically local or region-appropriate data center. The advantages of cloud-based load balancers is that they can operate in almost any geographic region without concern for rack space, power, cooling, or maintenance and can scale without concern for new chassis, modules, or larger network connections. Cloud-based load balancers do however increase latency and RTT between the load balancer and the endpoints as they are not typically colocated with the endpoints they are steering traffic toward.</p>
<h2 id="cloudflare-load-balancing-architecture-and-design">Cloudflare Load Balancing architecture and design</h2>
<p>Cloudflare has offered cloud-based GTM since 2016 and started adding Private Network Load Balancing capabilities in 2023. This section will review the entire Cloudflare Load Balancing architecture and dive deep into the different configurations and options available. First, however, it's important to understand the benefits that Cloudflare Load Balancers have simply by running on Cloudflare’s global network.</p>
<h3 id="inherent-advantages-in-the-cloudflare-architecture">Inherent advantages in the Cloudflare architecture</h3>
<p>Cloudflare Load Balancing is built on Cloudflare’s connectivity cloud, ​​a unified, intelligent platform of programmable cloud-native services that enable any-to-any connectivity between all networks (enterprise and Internet), cloud environments, applications, and users. It is one of the largest global networks, with data centers spanning <div class="nb-data-component" data-cf-component="PublicStats"></div> and interconnection with <div class="nb-data-component" data-cf-component="PublicStats"></div>. It also has a greater presence in core Internet exchanges than many other large technology companies.</p>
<p>As a result, Cloudflare operates within ~50 ms of ~95% of the world’s Internet-connected population. And since all Cloudflare services are designed to run across every network location, all traffic is connected, inspected, and filtered close to the source for the best performance and consistent user experience.</p>
<p>Cloudflare’s load balancing solution benefits from our use of anycast technology. Anycast allows Cloudflare to announce the IP addresses of our services from every data center worldwide, so traffic is always routed to the Cloudflare data center closest to the source. This means traffic inspection, authentication, and policy enforcement take place close to the end user, leading to consistently high-quality experiences.</p>
<p>Using anycast ensures the Cloudflare network is well balanced. If there is a sudden increase in traffic on the network, the load can be distributed across multiple data centers – which in turn, helps maintain consistent and reliable connectivity for users. Further, Cloudflare’s large network capacity and AI/ML-optimized smart routing also help ensure that performance is constantly optimized.</p>
<p>By contrast, many other SaaS-based load balancing providers use Unicast routing in which a single IP address is associated with a single endpoint and/or data center. In many such architectures, a single IP address is then associated with a specific application, which means requests to access that application may have very different network routing experiences depending on how far that traffic needs to travel. For example, performance may be excellent for employees working in the office next to the application’s endpoints, but poor for remote employees or those working overseas. Unicast also complicates scaling traffic loads — that single service location must ramp up resources when load increases, whereas anycast networks can share traffic across many data centers and geographies.</p>
<p>Figure 6 shows how using the Cloudflare network allows geographically disparate users to connect to their resources as fast as possible.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-6.svg" alt="Cloudflare’s global anycast network ensures that the closest data center is always selected" title="Figure 6: Load balancers hosted on Cloudflare’s global anycast network" /></p>
<p>Figure 6, above, shows other Cloudflare services are also running in each of these data centers since Cloudflare runs every service in every data center so users have a consistent experience everywhere. For example, Cloudflare’s layer 7 load balancer will also be able to take advantage of other services such as DDoS protection, CDN/Cache, Bot Management, or WAF. All of these additional services can help protect your service from unnecessary traffic whether it be malicious requests (blocked by DDoS Protection, Bot Management, or WAF) or requests that can be served via cache rather than a request to endpoint. All of these services can be combined as needed to make a service or offering as protected, resilient, and performant as possible.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-7.svg" alt="Cloudflare Layer 7 features can be used together to further secure a service" title="Figure 7: Some of the processes a HTTP request passes through in the Cloudflare layer 7 stack" /></p>
<p>Cloudflare also has a <a href="https://blog.cloudflare.com/orpheus-saves-internet-requests-while-maintaining-speed/">network optimization service</a> that is constantly running at all data centers to ensure that Cloudflare provides the best path between Cloudflare data centers and also track all the available paths to endpoints. This allows Cloudflare to ensure that endpoints can always be reached and reroute traffic to alternate Cloudflare data centers, if necessary, to reach an endpoint. After the load balancer has made a decision on which endpoint to steer the traffic, the traffic is then forwarded to Cloudflare’s network optimization service to determine the best path to reach the destination. The path can be affected by a feature called Argo Smart Routing which, when enabled, uses timed TCP connections to find the Cloudflare data center with the fastest RTT to the endpoint. Figure 8 shows how Argo Smart Routing can help improve connection time to endpoints.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-8.svg" alt="Argo Smart Routing finds the fastest path between requester and endpoint" title="Figure 8: Argo Smart Routing reduces latency to endpoints" /></p>
<p>Another way traffic flow can be affected is by the use of Cloudflare Tunnels. This document covers Cloudflare Tunnels in depth in the following section. Because Cloudflare Tunnels connect endpoints to specific Cloudflare data centers, traffic destined for those endpoints must traverse those data centers to reach the endpoint. Figure 9 shows how connections to private endpoints connected via Cloudflare Tunnel must pass through the data center where the tunnel terminates.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-9.svg" alt="Requests take different paths depending on whether the endpoint is public or connected over Cloudflare Tunnel" title="Figure 9: Paths to endpoints differ when connecting endpoints via Cloudflare Tunnel" /></p>
<p>Usually, GTM and Private Network Load Balancers are either separate hardware or separate SaaS (GTM) and hardware Private Network Load Balancing components. Cloudflare’s GTM and Private Network Load Balancing capabilities are combined into a single SaaS offering which greatly simplifies configuration and management. There is no need to create a GTM load balancer and steer traffic to more local Private Network Load Balancers. All endpoints can be directly connected to Cloudflare and traffic is steered to the correct region, data center, and endpoint all from a single load balancer configuration. While the concepts of GTM and Private Network Load Balancing features will persist, their implementation in Cloudflare will be done in a way that keeps load balancer configurations as simple and straightforward as possible. Figure 10 illustrates how global traffic can be steered from any geographic region to a specific endpoint as needed.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-10.svg" alt="Combining GTM and Private Network Load Balancing functions into a single load balancer configuration" title="Figure 10: Cloudflare combines the function of GTM and Private Network Load Balancing" /></p>
<h3 id="the-structure-of-a-cloudflare-load-balancer">The structure of a Cloudflare Load Balancer</h3>
<p>A Cloudflare Load Balancer, often referred to as a Virtual IP (VIP), is configured with an entrypoint. Typically, this entrypoint is a DNS record. The load balancer first applies a defined traffic steering algorithm to select an endpoint pool, which is a group of endpoints selected based on function, geographic area, or region. A load balancer configuration can have one or multiple endpoint pools, and each endpoint pool can have one or many endpoints. After selecting an endpoint pool, the load balancer applies an endpoint steering algorithm to the list of endpoints and selects an endpoint to steer the traffic towards. Figure 11 shows the basic steps from client request to endpoint within a Cloudflare Load Balancer.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-11.svg" alt="The steps within a Cloudflare Load Balancer" title="Figure 11: The basic process flow through a Cloudflare Load Balancer" /></p>
<p>The definition of a Cloudflare Load Balancer is divided into three main components:</p>
<ol>
<li>Health monitors: these components are responsible for observing the health of endpoints and categorizing them as healthy or critical (unhealthy).</li>
<li>Endpoint pools: this is where endpoints are defined and where health monitors and endpoint steering are applied.</li>
<li>Load balancers: in this component, lists of endpoint pools and traffic steering policies are applied.</li>
</ol>
<p>The following sections detail the options available and considerations for configuring a Cloudflare Load Balancer, starting with steering, which is utilized in both endpoint pool and load balancer configurations.</p>
<h3 id="steering-types-and-methods">Steering types and methods</h3>
<p>Steering is the core function of a load balancer and steering methods ultimately determine which endpoint is going to be selected when a load balancer is engaged. From the load balancer’s perspective, steering can be applied in two key areas.</p>
<p>The first is called ‘traffic steering’, and it is responsible for determining which endpoint pool will handle incoming requests, typically based on proximity or geographic region of the requester. The concept of traffic steering closely aligns with the idea of global traffic management.</p>
<p>The second area where steering is applied is after a region, data center, or endpoint pool has been selected. At this point, the load balancer needs to select the single endpoint responsible for handling the request or connection, referred to as ‘endpoint steering’. Steering at both of these levels is done by applying steering methods tailored to the specific needs of the customer deploying the load balancer. There are several different algorithms to choose from, but not all algorithms are applicable to both steering types.</p>
<p>Below is an in-depth review of all the steering methods Cloudflare offers. At the end of this section, there is a quick reference table which can be helpful in understanding which algorithms are applicable to which use cases.</p>
<h4 id="traffic-steering">Traffic steering</h4>
<p>Traffic steering selects the group of endpoints, also called an endpoint pool. The most common use of traffic steering is to select the endpoint pool based on the least latent response times, geographic region, or physical location. Traffic steering is closely aligned to global traffic management and serves as the initial step in directing traffic to an endpoint.</p>
<h4 id="endpoint-steering">Endpoint steering</h4>
<p>Endpoint steering is responsible for selecting which endpoint will receive the request or connection. Endpoint steering can randomly select an endpoint, a previously selected endpoint (if session affinity is enabled), or it can be used to select the least utilized, fastest responding, endpoint for a request or connection. Endpoint steering is closely related to Private Network Load Balancing, as it is responsible for selecting the final destination of a request or connection.</p>
<h4 id="weighted-steering">Weighted steering</h4>
<p>Weighted steering takes into account the differences in endpoint pools and endpoints that will be responsible for handling requests from a load balancer. Endpoint weight, which is a required field for every endpoint, is only used when specific steering methods are chosen. Similarly, endpoint pool weight is only needed when specific steering methods are selected. Please see the <a href="#steering-options-overview">steering options overview</a> section for a quick reference for when weights are applied.</p>
<p>Weight influences the randomness of endpoint pool or endpoint selection for a single request or connection within a load balancer. Weight does not consider historical data or current connection information, which means that weight may have variations in distribution over shorter timeframes. However, over longer periods of time and with significant traffic, the distribution will more closely resemble the desired weights applied in configuration. It’s important to note that session affinity will also override weight settings after the initial connection, as session affinity is intended to direct subsequent requests to the same endpoint pool or endpoint. Figure 12 shows a weight example for two endpoint pools with equal capacity and probability of being selected.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-12.svg" alt="A pair of endpoint pools with equal probability of being selected" title="Figure 12: A pair of endpoint pools with equal capacity" /></p>
<p>Specific algorithms, such as Least Outstanding Request Steering, take into account the number of open requests and connections. Weight is used to determine which endpoints or endpoint pools can handle a greater number of open requests or connections. Essentially, weight defines the capacity of endpoints or endpoint pools, regardless of the selected steering method.</p>
<p>Weight is defined as any number between 0.00 and 1.00. It’s important to note that the total weight of the endpoint pools or the endpoints within an endpoint pool do not need to equal 1. Instead, the weights will be added together, and then an individual weight value is divided by that sum to get the probability of that endpoint being selected.</p>
<p>Weight to percentage equation: (endpoint weight) ÷ (sum of all weights in the pool) = (% of traffic to endpoint)</p>
<p>Below are some examples with diagrams to help in understanding how weight is used for distributing traffic. In these examples, it is assumed that the goal is to evenly distribute traffic across all endpoints with the same capacity or compute resources. <a href="#random-steering">Random</a> traffic steering will be used to demonstrate traffic distribution across three endpoint pools.</p>
<p>Example 1:</p>
<ul>
<li>There are three endpoint pools defined, all with a weight of 1</li>
<li>Each endpoint pool has a 33% probability of being selected</li>
</ul>
<p>Example math for weight of 1: (1) ÷ (1 + 1 + 1) = (.3333) (or 33.33%)</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-13.svg" alt="A set of three endpoint pools all with equal probability" title="Figure 13: Three endpoint pools with equal weight" /></p>
<p>In this example, it was simple to apply 1 to all the weight values for each of the endpoint pools. However, it should be noted that any number between 0.01 and 1.00 could have been used as long as the same number was used across all three endpoint pools. For instance, setting all three pools to .1 or even .7 would have resulted in an equal probability that each pool would be selected to receive traffic.</p>
<p>Since the sum of the weights is used to calculate the probability, organizations can use any number of values to make these inputs easier to understand. In the following examples, since each endpoint has the same capacity, a value of .1 weight is assigned to each endpoint, and the sum of these values is used as the weight for the endpoint pool.</p>
<p>Example 2</p>
<ul>
<li>There are three endpoint pools defined</li>
<li>Each endpoint pool has a different number of endpoints, but all endpoints have equal capacity</li>
<li>To evenly distribute load across endpoints, each endpoint pool needs a different probability</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-14.svg" alt="Three endpoint pools with different numbers of endpoints" title="Figure 14: Illustrates how to use weight to balance load across endpoint pools with different capacity" /></p>
<p>Example math for weight of .4 : (.4) ÷ (.4 + .5 + .6) = (.2667) (or 26.67%)</p>
<p>Example math for weight of .5 : (.5) ÷ (.4 + .5 + .6) = (.3333) (or 33.33%)</p>
<p>Example math for weight of .6 : (.6) ÷ (.4 + .5 + .6) = (.4000) (or 40.00%)</p>
<p>It is possible that endpoints do not all have the same capacity. In the following example, one of the endpoint pool’s endpoints has twice the capacity of the endpoints in the other two endpoint pools.</p>
<p>Example 3</p>
<ul>
<li>There are three endpoint pools defined</li>
<li>Endpoint pool 1 has endpoints that have double the capacity compared to those in endpoint pool 2 and endpoint pool 3</li>
<li>The goal is to place double the amount of traffic to endpoint pool 1 per endpoint</li>
<li>Endpoint pool 1 has 4 endpoints but with double capacity, the weight of each endpoint will be valued at .2 for a total of .8 for the endpoint pool</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-15.svg" alt="Three endpoint pools with different numbers of endpoints and endpoints of different capacity" title="Figure 15: Using weight to balance load across endpoint pools with different capacities and endpoints" /></p>
<p>Example math for weight of .8 : (.4) ÷ (.8 + .5 + .6) = (.4211) (or 42.11%)</p>
<p>Example math for weight of .5 : (.5) ÷ (.8 + .5 + .6) = (.2632) (or 26.32%)</p>
<p>Example math for weight of .6 : (.6) ÷ (.8 + .5 + .6) = (.3157) (or 31.57%)</p>
<p>In this final example, since the four endpoints in endpoint pool 1 are double the capacity of other endpoints, the calculation treats endpoint pool 1 as if it essentially has 8 endpoints instead of 4. Therefore, the weight value of .8 instead of .4 as shown in example 2.</p>
<p>These are just three simple examples illustrating how weight can be used to distribute load across endpoint pools or endpoints. The same calculations are used for weights applied to endpoints within an endpoint pool as well. However, the impact of using weights within different steering methods is similar, although with slightly modified calculations, as covered in the sections below.</p>
<p>Weights are most useful when one endpoint pool might have more resources than another endpoint pool or when endpoints within an endpoint pool do not have equal capacity. Weight helps to ensure that all resources are used equally given their capabilities.</p>
<h4 id="steering-methods">Steering methods</h4>
<h5 id="off-failover">Off - failover</h5>
<p>Off - failover is the most basic of traffic steering policies. It uses the order of the endpoint pools as a priority list for selecting which pool to direct traffic towards. If the first pool in the list is healthy and able to receive traffic, that is the pool that will be selected. Since off - failover isn’t available for endpoint steering, another steering method will be used to select an endpoint. Off - failover is commonly used in active/passive failover scenarios where a primary data center or group of endpoints is used to handle traffic, and only under failure conditions, is traffic steered towards a backup endpoint pool.</p>
<h5 id="random-steering">Random steering</h5>
<p>Random steering is available for both traffic steering and endpoint steering. Random spreads traffic across resources based on the weight defined at both the load balancer configuration and within the endpoint pool. The weight values set at the load balancer for each endpoint pool can differ from the weight value set per endpoint within that endpoint pool. For example, within a load balancer configuration, 70% of traffic can be sent to one of two endpoint pools, then within that endpoint pool, the traffic can be evenly distributed across four endpoints. The previous section, <a href="#weighted-steering">weighted steering</a>, provides a detailed explanation of how weight is used and the calculations that determine the selection of an endpoint pool or endpoint.</p>
<h5 id="hash-steering">Hash steering</h5>
<p>Hash steering is an endpoint steering algorithm that uses endpoint weight and the request’s source IP address to select an endpoint. The result is that every request from the same IP address will always steer to the same endpoint. It’s important to note that altering the order of endpoints or adding or removing endpoints from the endpoint pool could result in different outcomes when using the hash algorithm.</p>
<h5 id="geo-steering">Geo steering</h5>
<p>Geo steering is a traffic steering algorithm available to enterprise plan customers that is used to tie endpoint pools to specific countries or geographic regions. This option can be useful for improving performance by steering traffic to endpoints closer to users. It also aids in complying with laws and regulations by steering requests from users in specific regions to resources within the same region or to resources designed to meet specific regulatory requirements.</p>
<h5 id="dynamic-steering">Dynamic steering</h5>
<p>Dynamic steering is a traffic steering algorithm available to enterprise plan customers that creates round trip time (RTT) profiles. RTT values are collected each time a health probe request is made and based on the response from the endpoint to the monitor request. When a request is made, Cloudflare inspects the RTT data and sorts pools by their RTT values. If there is no existing RTT data for your pool in a region or colocation center, Cloudflare directs traffic to the pools in failover order. When enabling dynamic steering the first time for an endpoint pool, allow 10 minutes for the change to take effect as Cloudflare builds an RTT profile for that pool. Dynamic steering doesn’t use geographic boundaries in its decision making process and solely focuses on selecting the lowest RTT endpoint pool.</p>
<h5 id="proximity-steering">Proximity steering</h5>
<p>Proximity steering is a traffic steering algorithm available to enterprise plan customers that steers traffic to the closest physical data center based on where the request originated.</p>
<p>Cloudflare determines the requester’s physical location using the following methods, in this order:</p>
<ol>
<li><a href="https://developers.google.com/speed/public-dns/docs/ecs">EDNS Client Subnet</a> information, if provided in the DNS request</li>
<li>Geolocation information of the resolver used to reach Cloudflare</li>
<li>GPS location of the Cloudflare data center handling the request</li>
</ol>
<p>Proximity steering requires providing GPS coordinates for all endpoint pools, allowing Cloudflare to calculate the closest endpoint pool based on the requesting IP, DNS resolver, or Cloudflare data center.</p>
<h5 id="least-outstanding-requests-steering-lors">Least outstanding requests steering (LORS)</h5>
<p>Least outstanding request steering (LORS) is available to enterprise plan customers and can be used for both traffic and endpoint steering.</p>
<p>LORS uses the number of unanswered HTTP requests to influence steering and is only functional when used with Cloudflare Layer 7 proxied Cloudflare Load Balancers. If LORS is assigned to any other type of load balancer, its behavior will be equivalent to random steering. LORS uses the counts of open requests, along with weight, to create a new transformed weight that is used for the steering decision.</p>
<p>Equation for LORS transformed weight:</p>
<ul>
<li>weight / (count + 1) = transformedWeight</li>
</ul>
<p>Reminder for random weight calculation:</p>
<ul>
<li>weight / (total weight) = probability of being selected</li>
</ul>
<p>Here’s an example of LORS:</p>
<ul>
<li>Pool A has a weight of 0.4</li>
<li>Pool B has a weight of 0.6</li>
<li>Pool A has 3 open requests</li>
<li>Pool B has 0 open requests</li>
<li>Relevant equation
<ul>
<li>weight / (count + 1) = transformedWeight</li>
</ul>
</li>
<li>Pool A's transformed weight: 0.4 / (3 + 1) = 0.1</li>
<li>Pool B's transformed weight: 0.6 / (0 + 1) = 0.6</li>
<li>Relevant equation
<ul>
<li>weight / (total weight) = probability of being selected</li>
</ul>
</li>
<li>Pool A’s probability of being steered toward: 0.1 / (0.1+0.6) = .1429 (14.29%)</li>
<li>Pool B’s probability of being steered toward: 0.6 / (0.1+0.6) = .8571 (85.71%)</li>
</ul>
<p>In this example, the next connection has a 14.29% probability of being steered to Pool A and a 85.71% probability of being steered to Pool B. While it’s likely that traffic will be steered towards Pool B, it is still possible for it to be steered to Pool A. In situations with lighter load conditions, there will be more variation in the steering results, which may not precisely match the configured weights. However, as the load increases, the actual steering results will closely match the configured weights.</p>
<p>When non-L7 proxied load balancers are used with LORS, the open request count information is not available. As a result, the denominator will always be 1. Since dividing any number by 1 doesn’t change the numerator, and in this case, the numerator is the weight, steering decisions will be made solely on weight. This results in the random method described above.</p>
<p>LORS is best used if endpoint pools or endpoints are easily overwhelmed by spikes in concurrent requests. It is well-suited for applications that value endpoint health over factors like latency, geographic alignment, or other metrics. This is especially useful when some or all requests put a heavy load on an endpoint and take a significant amount of time to generate a response.</p>
<h4 id="steering-options-overview">Steering options overview</h4>
<table>
<thead>
<tr>
<th>Steering Method</th>
<th>Traffic Steering</th>
<th>Endpoint Steering</th>
<th>Weight-based</th>
<th>Enterprise-only</th>
</tr>
</thead>
<tbody>
<tr>
<td>Off - Failover</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Random</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>Hash</td>
<td></td>
<td>X</td>
<td>X</td>
<td>X</td>
</tr>
<tr>
<td>Geo</td>
<td>X</td>
<td></td>
<td></td>
<td>X</td>
</tr>
<tr>
<td>Dynamic</td>
<td>X</td>
<td></td>
<td></td>
<td>X</td>
</tr>
<tr>
<td>Proximity</td>
<td>X</td>
<td></td>
<td></td>
<td>X</td>
</tr>
<tr>
<td>Least Outstanding Requests</td>
<td>X</td>
<td>X</td>
<td>X</td>
<td>X</td>
</tr>
</tbody>
</table>
<p>All traffic steering methods marked above as Enterprise-only can also be obtained as a self-service add-on as well. All endpoint steering methods marked as Enterprise-Only require an enterprise plan with Cloudflare.</p>
<h3 id="health-monitors">Health monitors</h3>
<p>A health monitor determines the health of endpoints once they are configured inside an endpoint pool. Health monitors generate probes, which are connection attempts to endpoints. Health monitors use the responses to the probes to record endpoint health. Health monitors serve as templates that include service type, path, and port, and advanced features such as interval, timeout, and protocol specific settings for evaluating endpoint health. The health monitor template is then applied to the endpoint pool, which contains endpoints hosting similar services. Once a health monitor is attached to the endpoint pool, the endpoint address is used as the destination for the health monitor probe. A single health monitor can be used across many endpoint pools, and health monitors are account-level objects, allowing them to be leveraged by multiple zones within the same Cloudflare account.</p>
<p>By default, health monitor probes are sent directly to the endpoint address, bypassing the entire layer 7 stack. This means that actual traffic to the endpoint through the load balancer will receive different treatment than the health monitor probe. Depending on the configuration, this could result in a health monitor reporting an endpoint as healthy, even if actual connections or requests are failing.</p>
<p>The Simulate Zone feature ensures that health monitor probes follow the same path as layer 7 HTTP/HTTPS requests for the given zone, passing through the same Cloudflare software-defined routing for egress to origin. This ensures health monitors take the same path through the Cloudflare network and other layer 7 processes to reach the origin endpoint.</p>
<p>The Simulate Zone feature is required for health monitors when certain features are enabled at the zone level, such as <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a> or <a href="/ssl/client-certificates/byo-ca/">Bring your own CA</a>, where probes would fail if they weren’t being provided with the proper mTLS certificate or authority for authentication with the origin server. Simulate Zone also ensures health monitor probes use the same path provided by <a href="/argo-smart-routing/">Argo Smart Routing</a> and the same <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> when organizations leverage <a href="/smart-shield/get-started/#packages-and-availability">Smart Shield Advanced</a> to restrict the edge IP addresses that Cloudflare uses to reach their endpoints.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-16.png" alt="HTTPS health monitor to monitor the status of an endpoint" title="Figure 16: HTTPS health monitor configuration" /></p>
<p>Health monitor Probes can be configured as the following types:</p>
<ul>
<li>HTTP</li>
<li>HTTPS</li>
<li>TCP</li>
<li>UDP ICMP</li>
<li>ICMP Ping</li>
<li>SMTP</li>
<li>LDAP</li>
</ul>
<p>Once a health monitor is defined, it can be assigned to an endpoint and the probes will be sent to the endpoint at the interval defined. There are two additional settings to note in regards to the health monitor configuration within the endpoint pool. The first is the Health Threshold, which is used to determine how many endpoints within the pool need to be healthy in order to consider the endpoint pool to be healthy or degraded.</p>
<ul>
<li>Endpoint pool in healthy state
<ul>
<li>Contains only healthy endpoints</li>
</ul>
</li>
<li>Endpoint pool in degraded state
<ul>
<li>Contains at least one critical endpoint but remains at or above the health threshold setting</li>
</ul>
</li>
<li>Endpoint pool in critical state
<ul>
<li>Contains healthy endpoints below the health threshold</li>
<li>Not capable of handling traffic; removed from all steering decisions.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-17.svg" alt="Comparison of three endpoint pools with different numbers of healthy endpoints" title="Figure 17: When endpoints pool are considered healthy, degraded, or critical" /></p>
<p>The second setting after defining the health monitor in the endpoint pool is to define which regions the health monitor probes should source from inside the Cloudflare global network. The available selections are listed below:</p>
<ul>
<li>All Regions (Default)</li>
<li>All Data Centers (Enterprise Only)</li>
<li>Western North America</li>
<li>Eastern North America</li>
<li>Western Europe</li>
<li>Eastern Europe</li>
<li>Northern South America</li>
<li>Southern South America</li>
<li>Oceania</li>
<li>Middle East</li>
<li>Northern Africa</li>
<li>Southern Africa</li>
<li>Southern Asia</li>
<li>Southeast Asia</li>
<li>Northeast Asia</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-18.png" alt="Endpoint pool settings to further customize the health monitors" title="Figure 18: Health Threshold and region selection for an endpoint pool configuration" /></p>
<p>With the exception of “All Regions” and “All Data Centers”, health monitor probes will only originate from data centers in the selected region or regions. For locally relevant services, it may not matter whether or not a data center on the other side of the world can reach the endpoints. Therefore, limiting checks to a specific region or a set of regions may make sense. The selection of “All Regions” or “All Data Centers” is intended to be used for globally available services where reaching a set of endpoints could be crucial to the function of the application.</p>
<h3 id="endpoints-and-endpoint-pools">Endpoints and endpoint pools</h3>
<p>Endpoints are the actual servers that handle connections and requests after a load balancer has applied all its policies. Endpoints can be physical servers, virtual machines, or serverless applications. As long as they can handle a request or connection from a user or client, they can be considered an endpoint. There are several different methods of defining and connecting endpoints to Cloudflare and the next section details those methods.</p>
<h4 id="connecting-endpoints-to-cloudflare">Connecting endpoints to Cloudflare</h4>
<p>Cloudflare endpoints can be defined in two ways, by IP address or by hostname. IP addresses are the most straightforward and basic of connection methods, hostnames offer a few options to consider. A hostname can be defined in Cloudflare DNS and it can be proxied or DNS-only (unproxied). Another option, of course, is that the hostname is not in a domain which Cloudflare is an authoritative DNS server for which means Cloudflare will rely on outside DNS servers to resolve that hostname to an IP address. Cloudflare Tunnel can also be used and offers two different options as well. These methods are discussed below in this section.</p>
<h5 id="cloudflare-proxied-dns-ip-and-non-cloudflare-endpoints">Cloudflare proxied, DNS, IP, and non-Cloudflare endpoints</h5>
<p>As mentioned in the “HTTP(S) Load Balancing” section above, load balancing is the very last process run before a request is sent to an endpoint. However, even if an endpoint is proxied via Cloudflare’s edge, after the load balancer, the request is forwarded directly to the endpoint without passing through the layer 7 stack again. This doesn’t mean the endpoint is unprotected or uncached, however. As long as the load balancer itself is proxied then all those protections are provided to the load balancer rather than the endpoints. Any direct communication with the endpoint can still be proxied and treated with Cloudflare’s layer 7 stack, but communication with an endpoint places all the processing in front of the load balancer, not the endpoint. Figure 19 illustrates the difference of where the Cloudflare layer 7 stack is placed in relation to the endpoint(s).</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-19.svg" alt="Load balancing is the last process before dispatching to the endpoint" title="Figure 19: Differences in the Layer 7 paths between load balancer and endpoint" /></p>
<p>There are very few differences from a load balancer perspective when it comes to what type of endpoint is defined as part of an endpoint pool. Once the traffic and endpoint steering policies and the load balancer rules are applied, the Cloudflare Load Balancing service instructs the L7 stack where to forward the incoming request or connection. This request is sent directly to the endpoint. Depending on the type of connection to the endpoint, there may be a different path. Features like Argo Smart Routing or tunnel-connected endpoints that are terminated at different Cloudflare data centers will route traffic differently rather than sending the request out of the Cloudflare edge, over the internet, directly to the endpoint. Regardless of the path, however, load balancing is the last process in the stack and this means that traffic doesn’t receive any additional treatment. So while the connection to endpoint can change the path from Cloudflare to the endpoint, the treatment or processing doesn’t change once an endpoint is selected.</p>
<h5 id="cloudflare-tunnel">Cloudflare Tunnel</h5>
<p>Cloudflare Tunnel is an outbound connection that enables organizations to simplify their firewall configurations, reduce complexity, enhance security, and more easily join their assets to the Cloudflare network. The executable that creates these tunnels is called cloudflared and may be referenced in this document and diagrams that follow.</p>
<p>Cloudflare Tunnel (cloudflared) can be installed directly on the endpoint or any server with IP connectivity to the endpoint. And because the connection to Cloudflare is initiated from where Cloudflare Tunnel was installed to Cloudflare, the only access needed is outbound access to Cloudflare. A single Cloudflare Tunnel can transport traffic to one or many different endpoints in one of two different ways, one which results in the endpoint being publicly accessible and one which keeps the endpoint completely only accessible privately.</p>
<p>Cloudflare Tunnel can be installed on the endpoint itself or on any server with layer 3 (IP) connectivity to the endpoint or endpoints that need to be connected to Cloudflare. The decision to separate cloudflared could be made for many different reasons including but not limited to isolating the endpoint(s) and ensuring their performance, having separate teams that manage network level connectivity and endpoints, or separation for architectural simplicity where servers have segregated roles or responsibilities.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-20.svg" alt="A single cloudflared instance tunnels traffic for multiple endpoints" title="Figure 20: A shared cloudflared deployed on a separate server tunnels traffic for multiple endpoints" /></p>
<p>A single cloudflared instance will create 4 different tunnels, two tunnels in two different Cloudflare data centers. This model ensures high availability and mitigates the risk of individual connection failures. This means in event a single connection, server, or data center goes offline, the endpoints will remain available. Cloudflare Tunnel also allows organizations to deploy additional instances of cloudflared, for availability and failover scenarios. These unique instances are called replicas. Each replica establishes four new connections which serve as additional points of ingress to the endpoint(s). Each of the replicas will point to the same tunnel. This ensures that your network remains up in the event a single host running cloudflared goes down. By design, replicas do not offer any level of traffic steering (random, hash, or round-robin).</p>
<h6 id="public-hostname">Public hostname</h6>
<p>The public endpoint method allows organizations to define a tunnel that points to a specific service or port running on an endpoint. The tunnel can terminate on the endpoint or on any server with IP connectivity to the endpoint. Using this public hostname method requires that each service that will be accessed over the tunnel is defined in the tunnel configuration. When configured, a unique tunnel ID, such as d74b3a46-f3a3-4596-9049-da7e72c876f5, will be created for the IP and port or service for which the tunnel is connecting traffic. This tunnel ID is then created into a unique public hostname in the Cloudflare-owned domain of cfargotunnel.com which results in a DNS A record being created that points directly to that service, that is d74b3a46-f3a3-4596-9049-da7e72c876f5.cfargotunnel.com. While this hostname is public it can only be accessed or utilized by traffic that is sent through the account that owns the Cloudflare Tunnel configuration. No other accounts would be able to access or send traffic directly to this DNS address. A DNS CNAME record created outside of the account that owns the cfargotunnel.com hostname will not be able to send traffic through that specific Cloudflare Tunnel.</p>
<p>When configured via the Dashboard, Cloudflare automatically creates a CNAME record in the DNS zone that refers to the cfargotunnel.com hostname. For example, a CNAME record of myTunnelService.example.com could be created to point the A record of d74b3a46-f3a3-4596-9049-da7e72c876f5.cfargotunnel.com. The main benefit being the ease of use and administration as the CNAME record is much more suggestive about its purpose and belongs to the customer DNS zone.</p>
<p>Another option is to create these tunnels and services on the host running cloudflared. This is called a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/">locally-managed tunnel</a>. When working with locally-managed tunnels, the CNAME entry is not created automatically however, so the organization would have to configure this manually, after the tunnel and service is defined.</p>
<p>From a load balancer perspective, it's very important to understand how these tunnels can be used as an endpoint. An endpoint can only be defined by using the cfargotunnel.com hostname. Using a public CNAME record that points to the cfargotunnel.com address will not work properly and is not supported. This is especially important for endpoint services that don’t operate on ports 80 or 443. Cloudflare Load Balancers default to these two ports to access the services running on the endpoints. If an organization has services running on other ports, they will need to configure a Cloudflare Tunnel with a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/#how-traffic-is-matched">catch-all rule</a> to reach that port. This configuration allows a Cloudflare Load Balancer to reach the service via port 443 while having Cloudflare tunnel proxy the connection to the desired port on the endpoint.</p>
<h6 id="private-ip">Private IP</h6>
<p>The second method is for private subnets. This method allows organizations to define private IP addresses and a subnet mask which will be used to create a private virtual network within the Cloudflare global network. The private subnet method does not allow the definition of a port and as such, once a subnet and mask are defined, the entire subnet can be reached over that tunnel but only to users within the organization that are allowed access via defined Zero Trust policies.</p>
<p>This subnet then gets added to the virtual network inside of Cloudflare where the customer can control how users can access it and which users can access it. This subnet can be defined for any desired subnetting or routing, including using a 32-bit mask (single IP address, i.e., 10.0.0.1/32). The allowed subnet does not need to exist on the host that is running the cloudflared process either. All that is required is layer 3 or IP connectivity between the host running cloudflared and the subnet that is going to be reachable over Cloudflare Tunnel.</p>
<h4 id="endpoint-pool-details">Endpoint pool details</h4>
<p>Within the endpoint pool, there are several configuration options. This section details what these configuration options are and how they alter the behavior of a Cloudflare Load Balancer.</p>
<h5 id="endpoint-steering-1">Endpoint steering</h5>
<p>The first configuration, besides defining a name and description of the endpoint pool, is to determine the endpoint steering method. Endpoint steering is responsible for ultimately selecting the endpoint pool or endpoint that will receive the request or connection attempt (please refer to the <a href="#steering-methods">Steering methods</a> section for a detailed description of each method).</p>
<h5 id="endpoints">Endpoints</h5>
<p>Individual endpoints are defined within endpoint pools, and the endpoint pool allows for one or more endpoints to be defined per pool.</p>
<ul>
<li>The <em>endpoint name</em> is primarily used for reference, reporting, and analytics; it does not affect the function of the load balancer or endpoint pool.</li>
<li>The <em>endpoint address</em>, however, defines a resource that the load balancer can use to handle a request or connection.
<ul>
<li>Endpoints within an endpoint pool must be accessible over port 80 or 443. If the endpoint is not listening on port 80 or 443, then either a proxy service or network port forwarding device needs to be placed in front of the endpoint to map port 80 or 443 to the port that the service is actually listening on.</li>
<li>Another method for mapping ports of endpoints to 80 or 443 is to connect to the endpoint service using <a href="#cloudflare-tunnel">Cloudflare Tunnel</a>, and then use the hostname created through that process as the endpoint address. This will automatically map the intended endpoint port to port 443.</li>
</ul>
</li>
</ul>
<p><em>Endpoint address</em> can be defined in one of the following ways:</p>
<ul>
<li>Publicly routable IP address</li>
<li>Cloudflare-proxied publicly reachable hostname</li>
<li>Publicly reachable non-Cloudflare hostname</li>
<li>Private, non-publicly routable IP address with the selection of a virtual network</li>
</ul>
<h5 id="virtual-networks">Virtual networks</h5>
<p>Using public IPs and hostnames of any type require no additional configuration. In those scenarios, the virtual network should be set to the default value of “<em>none</em>”. The “<em>none</em>” setting signals that these resources will be accessible on the public Internet, routed via Cloudflare’s global edge network.</p>
<p>The use of the <em>virtual network</em> option is reserved for private IP resources. This setting maps to IP subnets that are hosted behind <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/">Cloudflare Tunnel configurations</a>. A virtual network should be selected that has a route to the IP address of the endpoint. To navigate to this setting in the Cloudflare Dashboard, select <em>Networks - Routes</em> from the Zero Trust page.</p>
<h5 id="endpoint-weight">Endpoint weight</h5>
<p><em>Endpoint weight</em> is only used for the random, hash, and least outstanding request steering methods; it must always be defined as part of the endpoint definition. (Please refer to the <a href="#weighted-steering">Weighted Steering</a> section for more information on how weights are used for endpoint selection.)</p>
<h5 id="host-header-modification">Host header modification</h5>
<p>Endpoint pools allow for the host header to be modified before dispatching a request to an endpoint. This configuration only applies to the HTTP(S) layer 7 load balancer (it will be ignored when used with layer 4 load balancers, including private IP and Spectrum).</p>
<p>Within a layer 7 load balancer where requests are HTTP(S)-based, the Host header tells the endpoint which website is being requested, as a single endpoint may host several different web domains. When an endpoint is specifically configured to host a web domain, it may either not respond or send a failure response to a request for a resource, if it does not believe it is hosting the resource requested in the Host header (i.e., if there are mismatched Host headers).</p>
<p>For example:</p>
<ul>
<li>Say a user tries to reach <code>www.example.com</code>. The load balancer will be configured with the hostname of <code>www.example.com</code> to receive all the requests.</li>
<li>Since the endpoints can’t have the same public hostname in DNS, its hostname is <code>endpoint1.example.com</code>.</li>
<li>When the user makes a request to <code>www.example.com,</code> the Host header will be set to <code>www.example.com</code>, as well. The endpoint will need to be configured to respond to Host headers of <code>www.example.com</code>.</li>
<li>In some cases (such as with certain cloud or SaaS applications), however, endpoints aren’t configurable in that manner, so the endpoint may receive a request with an unknown Host header and fail to respond appropriately.</li>
<li>In this example, in the endpoint configuration, setting the Host header for the endpoint to the endpoint address of <code>endpoint1.example.com</code> will replace the Host header of <code>www.example.com</code> with <code>endpoint1.example.com</code>, and will allow the endpoint to properly respond to this request.</li>
</ul>
<p>Figure 21 highlights the potential problem of mismatched Host headers:</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-21.svg" alt="Mismatched Host headers may result in the endpoint rejecting the request" title="Figure 21: How the load balancer can rewrite the Host header to match the endpoint" /></p>
<p>Also, at the endpoint pool, GPS coordinates for the pool (which are used with proximity traffic steering) can be defined. If proximity steering is not being used, then these coordinates are not required (please refer to the <a href="#proximity-steering">Proximity Steering</a>).</p>
<h5 id="load-shedding">Load shedding</h5>
<p><a href="/load-balancing/additional-options/load-shedding/">Load shedding</a> — a real-time response available to administrators to protect against endpoints in a pool that are <a href="/load-balancing/understand-basics/health-details/">becoming unhealthy </a> — is also configured on the endpoint pool.</p>
<p>The load shedding setting is not intended to be enabled unless an administrator is trying to actively protect an endpoint pool from becoming unhealthy. It is activated, for example, when an endpoint that is still responding to requests is experiencing increased CPU or memory usage, increased response times, or occasionally failing to respond at all.</p>
<p>When an endpoint pool’s health begins to degrade, load shedding can help direct some of the existing loads from one endpoint pool to another.</p>
<p>Depending on the health of the endpoint pool, it may be enough to simply shed or redirect new requests and connections away from the endpoint pool. This policy applies to traffic, which is not subject to any session affinity rules since these are new connections that haven’t had an endpoint pool or endpoint selected yet (and, therefore, will not potentially affect the end user experience).</p>
<p>Should an endpoint pool approach critical failure due to load, the next option is to shed additional session affinity traffic. This will start to redirect requests and connections that are bound to endpoint pools through session affinity as well. However, please note that because this process can ultimately change the user’s endpoint, it could impact the end user’s experience. Ultimately, the impact is determined by the application that is being load balanced, and how much connection context is shared between endpoints.</p>
<h5 id="health-monitors-1">Health monitors</h5>
<p>Health monitors are attached to endpoints at the endpoint pool as well as health threshold and the health check region selection. Details of these options can be found in the <a href="#health-monitors">health monitor</a> section.</p>
<h3 id="load-balancers">Load balancers</h3>
<p>Load balancing within Cloudflare combines both GTM and Private Network Load Balancing into a single load balancer configuration. While certain features or terms may align more with GTM or Private Network Load Balancing, for Cloudflare customers, both are combined into a single, easy-to-manage instance.</p>
<p>Depending on their specific use case, organizations can leverage different types of Cloudflare Load Balancers. The following section highlights the main differences between the deployment models, and articulates when each type of load balancer should be implemented.</p>
<p>Figure 22 highlights all the possible combinations of load balancers and endpoints supported by Cloudflare:</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-22-ALT.svg" alt="All the possible combinations of load balancer and endpoint types" title="Figure 22: The combinations of public and private load balancers and endpoints and how they connect" /></p>
<h4 id="deployment-models">Deployment models</h4>
<p>Cloudflare offers three load balancing deployment models, each of which support different use cases, functionality, and privacy requirements.</p>
<ul>
<li><a href="#layer-7-https-load-balancing">Layer 7 HTTP(S) load balancing</a></li>
<li><a href="#dns-only-load-balancing">DNS-only load balancing</a></li>
<li><a href="#spectrum-load-balancing">Spectrum load balancing</a></li>
</ul>
<p>Except for the DNS-only load balancing option described in more detail below, all of the deployment models anchor traffic through the load balancer. This means the user or client creating the request or connection is never aware of the endpoints that are being used to service the request or connection. Endpoint information can certainly be exposed — if desired — through the use of headers, but this is not default behavior for any of these anchored deployment models.</p>
<p>The following explores the four main deployment models (and their differences) in more detail.</p>
<h5 id="layer-7-http-s-load-balancing">Layer 7 HTTP(S) load balancing</h5>
<p>First, the most common model is the <strong>HTTP(S)-based layer 7 proxied load balancer</strong>. These load balancers exist on Cloudflare’s edge and are publicly reachable. Amongst other features, this model supports <a href="/network/websockets/">WebSockets</a>, which are open connections between the client and endpoint allowing for data to be passed back and forth between the two.</p>
<p>Because this same layer 7 security stack also provides WAF, DDoS protection, Bot Management, Zero Trust, and other services, accessing these public load balancers can be restricted to authenticated and authorized users as needed. (Please refer to <a href="#protecting-and-securing-load-balancers">Securing Load Balancers</a> for more information.)</p>
<p>In this layer 7 stack, load balancing can further improve the performance, reliability, and reachability of an organization’s public-facing web assets. The endpoints for these load balancers may be deployed in public cloud, private cloud, on-premises, or any combination thereof within the same load balancer. (Please refer to <a href="#connecting-endpoints-to-cloudflare">Connecting endpoints to Cloudflare</a> for more details about how to connect endpoints to Cloudflare’s edge network).</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-23-ALT.svg" alt="Layer 7 load balancing request flow to two different types of endpoints" title="Figure 23: How Cloudflare’s Layer 7 load balancers can steer traffic to both public and private endpoints" /></p>
<p>As illustrated in Figure 23 above, the load balancing component of the layer 7 stack is the last process run on a request as it moves towards the endpoint. This can have a large positive impact on increasing performance and reducing load on endpoints.</p>
<p>For example, caching can prevent requests from ever reaching the endpoint and can be responded to without ever having to engage the load balancers. Also, WAF, DDoS protection, and Bot Management can eliminate attack traffic altogether — leaving more capacity for legitimate traffic.</p>
<p>Once a request reaches the load balancer process, the request is always sent directly to the endpoint that was selected. This means that even if the endpoint is proxied through Cloudflare, the request will be sent directly to the endpoint and receives no further processing.</p>
<p>For customized treatment after the load balancer selects an endpoint, the load balancer’s Custom Rules are applied. (This is covered in detail in the <a href="#load-balancers">Load balancers</a> section below).</p>
<p><strong>Important notes about Layer 7 HTTP(S) load balancers:</strong></p>
<ul>
<li>Layer 7 HTTP(S) load balancers support both public and private endpoints</li>
<li>Layer 7 HTTP(S) load balancers will only support HTTP(S) and WebSocket traffic</li>
<li>Zero trust policies can be applied to Layer 7 HTTP(S) load balancers</li>
</ul>
<h5 id="dns-only-load-balancing">DNS-only load balancing</h5>
<p>Cloudflare’s DNS-only load balancer is an unproxied load balancer. This means that only the initial DNS request for the resource — not the actual traffic — passes through the Cloudflare edge. Therefore, instead of a DNS request resolving to a Cloudflare IP and then moving through the layer 7 stack as seen earlier in Figure 7, Cloudflare receives a DNS request for a DNS-only load balancer, applies all the appropriate load balancing policies, then returns an IP address to the requesting client to reach out directly.</p>
<p>Because all the traffic between the client and the endpoint will travel directly between the two and not through Cloudflare’s layer 7 stack, any type of IP traffic can be supported by a DNS-only load balancer.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-24.png" alt="The orange cloud icon represents a proxied Layer 7 Cloudflare Load Balancer" title="Figure 24: A proxied load balancer configuration" /></p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-25.png" alt="The gray cloud icon represents an unproxied (DNS-only) load balancer" title="Figure 25: An unproxied (DNS-only) load balancer configuration" /></p>
<p>Even though Cloudflare does not proxy these types of load balancer connections, the health monitor service is still monitoring the health on all the endpoints in the pool. Based on the health or availability of an endpoint, a Cloudflare DNS-only load balancer will either add or remove an applicable endpoint to a DNS response to ensure that traffic is being steered to healthy endpoints.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-26.svg" alt="DNS-only load balancers only use Cloudflare to respond to a DNS request" title="Figure 26: How Cloudflare’s DNS-only load balancer functions" /></p>
<p>After a DNS-only load balancer has selected an endpoint pool via traffic steering, one or many IP addresses may be returned in the DNS response.</p>
<p>The decision to send one or many IP addresses within the DNS response is based on the weight assigned to the endpoints within the selected endpoint pool:</p>
<ul>
<li>If all the weights are equal across all endpoints, all IP addresses of all the endpoints will be returned in DNS response.</li>
<li>If at least one endpoint is specified with a unique weight within the endpoint pool, then only a single IP address will be returned in the DNS response — regardless of the endpoint steering method selected on the endpoint pool.</li>
</ul>
<p>This gives organizations the flexibility to allow applications to be aware of all the endpoints and perform local failover, or to allow Cloudflare to provide a single IP for an application to utilize.</p>
<p>Figure 27 shows how the defined weight within an endpoint pool can affect how a DNS-only load balancer responds.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-27.svg" alt="DNS-only load balancers can respond to DNS requests with one or many IP addresses" title="Figure 27: How weight affects the DNS response from a DNS-only load balancer" /></p>
<p>Please note that DNS-only load balancers have a few limitations compared to proxied load balancers:</p>
<ul>
<li>The load balancer no longer hides the endpoint’s IP address from the client as it is sent back to the client directly.</li>
<li>They do not have the built-in layer 7 stack services mentioned in the previous model; i.e., DNS-only load balancers do not include caching, WAF, DDoS protection, or Zero Trust support.</li>
<li>Session affinity is limited to <code>ip_cookie</code>, which will select an endpoint deterministically and then map that endpoint to the client IP address for all subsequent requests.</li>
<li>Finally, because connections are not proxied through the load balancer for DNS only, certain steering methods will not work either. For example, <a href="#least-outstanding-requests-steering-lors">LORS</a> will not work since Cloudflare will not be aware of the connections to the endpoints. These steering methods will revert to random weighted steering.</li>
</ul>
<p>For more information on additional steering methods, please refer to the <a href="#steering">Steering</a> section.</p>
<p>There are also client and resolver DNS cache considerations when using DNS-only load balancers. The cache life is determined by the DNS server answering the request. The <a href="https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/">Time-to-Live (TTL)</a> value tells a DNS requester how long the response is valid before the client should send a new DNS request to see if the destination has changed. The TTL is calculated in seconds, so — for example — a TTL value of 3600 equates to a TTL of one hour. However, standard DNS TTL values are usually either 12 or 24 hours or 43200 and 86400 respectively.</p>
<p>The TTL of a DNS-only load balancer is set to 30 (seconds). This ensures that as endpoint health changes or endpoints are added or deleted, the DNS-only load balancer is queried more often to provide the most accurate list of available endpoints possible.</p>
<p><strong>Important notes about DNS-only load balancers:</strong></p>
<ul>
<li>DNS-only load balancers support only public endpoints</li>
<li>DNS-only load balancers do not proxy traffic — and — as such, are not involved in the connections to endpoint</li>
<li>DNS-only load balancers only respond to a DNS request with an IP address or set of IP addresses</li>
</ul>
<h5 id="spectrum-load-balancing">Spectrum load balancing</h5>
<p>Cloudflare also offers another ingress method via the <a href="/spectrum/">Spectrum</a> product.</p>
<p>Where the layer 7 stack only supported HTTP(S) and WebSockets, Spectrum offers support for any TCP- or UDP-based protocol. A Cloudflare Load Balancer using Spectrum as an ingress for traffic operates at layer 4, where both TCP and UDP protocols exist. Any service that utilizes TCP or UDP for transport can leverage Spectrum with a Cloudflare Load Balancer including SSH, FTP, NTP, SMTP, and more.</p>
<p>Given the breadth of services and protocols this represents, the treatment provided is more generalized than what is offered with the layer 7 HTTP(S) stack. For example, Cloudflare Spectrum supports features such as TLS/SSL offloading, DDoS protection, IP Access lists, Argo Smart Routing, and session persistence with our layer 4 load balancers.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-28-ALT.svg" alt="Spectrum-based load balancing supports public endpoints" title="Figure 28: Spectrum Layer 4 load balancers support both TCP and UDP protocols" /></p>
<p>Cloudflare layer 4 Spectrum load balancers are publicly accessible. Access to these load balancing resources can be managed using a Spectrum configuration called <em>IP Access Rules,</em> which can be defined as part of a WAF configuration, but are limited to rules created with the “allow” or “block” action for specific IP addresses, subnets, countries, or <a href="https://www.cloudflare.com/learning/security/glossary/what-is-bgp/">Border Gateway Protocol (BGP)</a> Autonomous System Numbers (ASNs).</p>
<p>In addition to being public, Spectrum load balancers are always proxied. The proxy setting shown earlier (Figures 24 and 25) will be ignored when Spectrum is configured as the ingress path for the load balancer. All traffic destined for Spectrum-based load balancers will always pass through the Cloudflare edge.</p>
<p><strong>Important notes about Spectrum load balancers:</strong></p>
<ul>
<li>Spectrum load balancers support both public and private endpoints</li>
<li>Spectrum load balancers are initially created as Layer 7 HTTP(S) load balancers. A Spectrum application is then created with a Load Balancer endpoint type, and the load balancer that has already been created is selected.</li>
<li>Spectrum load balancers are always proxied, regardless of the proxy setting on the load balancer configuration</li>
<li>There is no ability to change the ingress port from the Internet via Spectrum to the endpoint; i.e., if the traffic comes in on port 22 to Spectrum, it will be steered to port 22 on the endpoint</li>
<li>Spectrum load balancers only support session affinity using the hash endpoint steering method</li>
<li>Spectrum load balancers do not support Custom Rules</li>
</ul>
<h5 id="deployment-models-at-a-glance">Deployment models at-a-glance</h5>
<table>
<thead>
<tr>
<th>Load Balancer Model</th>
<th>Public</th>
<th>Proxied</th>
<th>OSI Layer</th>
<th>Traffic Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>Layer 7 HTTP(S)</td>
<td>X</td>
<td>X</td>
<td>7</td>
<td>HTTP(S)</td>
</tr>
<tr>
<td>DNS-Only</td>
<td>X</td>
<td></td>
<td>7 (DNS)</td>
<td>IP-Based</td>
</tr>
<tr>
<td>Spectrum</td>
<td>X</td>
<td>X</td>
<td>4</td>
<td>TCP/UDP</td>
</tr>
</tbody>
</table>
<h4 id="load-balancer-details">Load balancer details</h4>
<h5 id="hostname">Hostname</h5>
<p>The hostname setting is the publicly-reachable hostname for the load balancer. The hostname must be created within the zone for which the load balancer is being created.</p>
<h5 id="proxy-status">Proxy status</h5>
<p>The proxy setting determines whether Cloudflare will proxy traffic for the load balancer or simply provide a DNS reply with the endpoints for the client to directly connect. This is covered in detail in the <a href="#deployment-models">Deployment models</a> section.</p>
<h5 id="session-affinity">Session affinity</h5>
<p>Session affinity, also known as session persistence or sticky sessions, keeps a client connected to the same endpoint for all subsequent requests after the first request or connection. This can be an important feature for applications that don’t share session data — the context of a user’s interaction with a web application — between endpoints. For example, if a new endpoint were selected in the middle of a client session and information about the session (e.g. the contents of a user’s shopping cart) were lost, the user experience for that application would be poor.</p>
<p>Cloudflare offers three methods for enabling session affinity:</p>
<ol>
<li><strong>By Cloudflare cookie only (cookie):</strong> On the first request to a proxied load balancer, a cookie is generated, encoding information of which endpoint the request will be forwarded to. Subsequent requests (by the same client to the same load balancer) will be sent to the endpoint that the cookie encodes for a) the duration of the cookie and b) as long as the endpoint remains healthy. If the cookie has expired or the endpoint is unhealthy, a new endpoint will be calculated and used.</li>
<li><strong>By Cloudflare cookie and Client IP fallback (ip_cookie):</strong> This behaves similar to the cookie method above, except that the cookie is generated based on the client IP address. In this case, requests from the same IP address always get steered towards the same endpoint for a) the duration of the cookie and b) as long as the endpoint remains healthy. If the cookie has expired or the endpoint is unhealthy, a new endpoint will be calculated and used.</li>
<li><strong>By HTTP header (header):</strong> On the first request to a proxied load balancer, a session key is generated based on the configured HTTP headers. Subsequent requests to the load balancer with the same headers will be sent to the same endpoint, for a) the duration of the session or b) as long as the endpoint remains healthy. If the session has been idle for the duration of session affinity time-to-live (TTL) seconds or the endpoint is unhealthy, then a new endpoint will be calculated and used.</li>
</ol>
<p>These three session affinity options only apply to layer 7 HTTP(S) load balancers. Session affinity requires a TTL, which determines how long the load balancer will route subsequent requests to a specific endpoint. The default TTL is 82,800 seconds (23 hours), but it can be set for anywhere from 1,800 seconds (30 minutes) to 604,800 seconds (seven days).</p>
<p>For cookie-based session affinity, the expiration timer is never reset, meaning that the timer is counting down from the start of the session — regardless of the session being idle or active. HTTP header-based session affinity will reset the expiration timer every time there is activity in the session.</p>
<h5 id="endpoint-draining">Endpoint draining</h5>
<p>Endpoint draining is a subfeature of session affinity. It allows for sessions to gracefully expire from an endpoint while not allowing new sessions to be created on that same endpoint. Endpoint draining is useful for maintenance, as it does not require administrators to arbitrarily or abruptly cut off user sessions in order to remove all active sessions from an endpoint.</p>
<p>The endpoint drain TTL is the amount of time that endpoints will be allowed to maintain active sessions before being forcefully terminated. Once the endpoint drain TTL is set, endpoint draining is started by disabling an endpoint (or multiple endpoints) within an endpoint pool. As seen in the below image, administrators can monitor the time remaining on an endpoint draining operation from the load balancer UI.</p>
<p><img src="/assets/upstream/images/reference-architecture/load-balancing-reference-architecture-images/lb-ref-arch-30.png" alt="Endpoint draining in process from web user interface" title="Figure 30: Endpoint draining occurring within a Cloudflare Load Balancer" /></p>
<p>Endpoint draining is only applicable for session affinity because without session affinity, subsequent requests or connections are not guaranteed to be steered to the same endpoint. Thus, disabling an endpoint does not have an impact on user experience.</p>
<h5 id="zero-downtime-failover">Zero-downtime failover</h5>
<p>Zero-downtime failover automatically sends traffic to endpoints within an endpoint pool during transient network issues.
Zero-downtime failover will trigger a single retry only if there is another healthy endpoint in the pool and a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/">521, 522, 523, 525 or 526 error code</a> is occurring. No other error codes will trigger a zero-downtime failover operation.</p>
<p>These response codes are not returned from the endpoint, but from requests made by upstream Cloudflare services to an organization's endpoints.</p>
<p>Zero-downtime failover has three modes of operation:</p>
<ol>
<li><strong>None (Off):</strong> No failover will take place and users may receive error messages or a poor user experience.</li>
<li><strong>Temporary:</strong> Traffic will be sent to other endpoint(s) until the endpoint is available again.</li>
<li><strong>Sticky:</strong> The session affinity cookie is updated and subsequent requests are sent to the new endpoint moving forward as needed. This is not supported when session affinity is using HTTP header mode.</li>
</ol>
<h5 id="adaptive-routing-failover-across-pools">Adaptive routing - failover across pools</h5>
<p><em>Adaptive routing - failover across pools</em> extends the functionality of zero-downtime failover by allowing failover to extend to endpoints in another endpoint pool, rather than only failing over to an endpoint in the <em>same</em> pool.</p>
<h5 id="endpoint-pools">Endpoint pools</h5>
<p>Endpoint pools are configured in a priority order and can be rearranged as needed. This priority order is only considered when using <em>Off - Failover traffic steering;</em> otherwise, endpoint pools will be selected based on the criteria outlined in the <a href="#steering-methods">Steering methods</a> section.</p>
<p>The endpoint pools assigned to a load balancer represent the entire collection of endpoints that could possibly handle requests or connections through the load balancer. An endpoint pool typically contains endpoints that all have the same capabilities and are in the data center or geographic region. All endpoints in a pool should be capable of handling any request directed to an endpoint pool. For more information about endpoint pools, please refer to the <a href="#endpoint-pools">Endpoint pools</a> section.</p>
<h5 id="fallback-pools">Fallback pools</h5>
<p>A fallback pool is the pool of last resort. When all endpoint pools are unavailable or unhealthy, the fallback pool will be used for all requests and connections. While health monitor data is always considered when steering traffic within a load balancer, a fallback pool does not rely on this data and is not subject to it.</p>
<h5 id="health-monitors-2">Health monitors</h5>
<p>Health monitors are usually configured as part of the endpoint pool. Health monitors can be added, changed, or deleted as part of the load balancer configuration. Please see the <a href="#health-monitors">Health monitors</a> section for more information.</p>
<h5 id="traffic-steering-1">Traffic steering</h5>
<p>Traffic steering is the method of steering between endpoint pools. For help understanding which traffic steering method to select, please see the <a href="#steering-types-and-methods">Steering types and methods</a> section.</p>
<h5 id="custom-rules">Custom rules</h5>
<p><a href="/load-balancing/additional-options/load-balancing-rules/">Custom rules</a> allow users to perform actions on requests or connections before the load balancer finishes its decision process. Custom rules are configured with expressions that match certain <a href="/load-balancing/additional-options/load-balancing-rules/reference/">fields</a> in requests or connections. Once the expression is created to match traffic, an <a href="/load-balancing/additional-options/load-balancing-rules/actions/">action</a> is assigned for when a request or connection matches the expression.</p>
<p>Custom rules are a powerful tool for customizing the steering and output from a load balancer before the request or connection is sent to the endpoint. For example, the HTTP method (e.g. GET, PUT, POST) could be matched to ensure that POST messages are sent to a specific endpoint pool dedicated to handling receiving information from clients.</p>
<p>Alternatively, that session affinity TTL could be reset based on a request going to a specific URL path to ensure that the client has enough time to complete the transaction.</p>
<p>It is not possible to document all of the potential combinations of fields that can be matched and actions that can be taken. However, the following resources describe all of the fields and actions that are currently available:</p>
<ul>
<li><a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields and operators</a></li>
<li><a href="/load-balancing/additional-options/load-balancing-rules/actions/">Load Balancing actions</a></li>
</ul>
<p>If the default behavior of a load balancer is not covered in the documents listed above, it is likely that a custom rule can help meet unique use case requirements.</p>
<h3 id="protecting-and-securing-load-balancers">Protecting and securing load balancers</h3>
<h4 id="inherent-security">Inherent security</h4>
<p>All Cloudflare Load Balancer deployment models come with inherent protections. The following section briefly highlights the default security Cloudflare provides, as well as optional protections that can be added in front of Cloudflare Load Balancers:</p>
<ul>
<li>Proxied HTTP layer 7 load balancer (Public)
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/">DDoS protection</a> to protect against attacks</li>
<li>WAF with <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare managed ruleset</a> and <a href="/waf/managed-rules/reference/owasp-core-ruleset/">OWASP ruleset</a> to block known vulnerabilities and exploits</li>
</ul>
</li>
<li>DNS-only load balancer (Public)
<ul>
<li><a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">DNS DDoS protection</a> to ensure a DNS-only load balancer is always available</li>
</ul>
</li>
<li>Spectrum layer 4 load balancer (Public)
<ul>
<li><a href="/spectrum/about/ddos-for-spectrum/">DDoS Protection</a> to protect against layer 4 attacks</li>
</ul>
</li>
</ul>
<h4 id="additional-options">Additional options</h4>
<p>Cloudflare offers additional security layers that can be used in conjunction with load balancing to protect any services — including websites, APIs, HTTP(S)-based services, and more:</p>
<ul>
<li>Proxied HTTP layer 7 load balancer (Public)
<ul>
<li><a href="/bots/">Bot management</a> to control which bots can access resources</li>
<li><a href="/waf/">WAF</a> for creating custom rules for web applications</li>
<li><a href="/client-side-security/">Client-side security</a> for monitoring script usage on web applications</li>
<li><a href="/api-shield/">API Shield</a> for protecting APIs</li>
</ul>
</li>
<li>DNS-only load balancer (Public)
<ul>
<li><a href="/dns/dnssec/">DNSSEC</a> to ensure authenticity of DNS records</li>
</ul>
</li>
<li>Spectrum layer 4 load balancer (Public)
<ul>
<li><a href="/spectrum/reference/configuration-options/#ip-access-rules">IP Access Rules</a> for controlling access to public layer 4 load balancers</li>
</ul>
</li>
</ul>
<h2 id="summary">Summary</h2>
<p>The Cloudflare global anycast network is a powerful platform for load balancing. A load balancing configuration in Cloudflare is accessible in <div class="nb-data-component" data-cf-component="PublicStats"></div> across the world and has virtually unlimited capacity and bandwidth.</p>
<p>These load balancers operate within approximately 50ms of about 95% of the Internet-connected population, including endpoints that allow Cloudflare Load Balancers to perform both GTM and Private Network Load Balancing. Cloudflare now combines these two distinct load balancing concepts into a single load balancer. This helps enable organizations to steer traffic to geographically-relevant data centers, then select the proper endpoint to handle the request.</p>
<p>With Cloudflare Tunnel, endpoints can be located within private networks and still be utilized by Cloudflare Load Balancers. Cloudflare offers public layer 7 load balancers — that supports both HTTP(S) and WebSockets, as well as public layer 4 load balancers that can steer any TCP or UDP traffic. This means that Cloudflare can offer load balancing services to all organizations and users, no matter their location, use cases, or existing configurations.</p>
