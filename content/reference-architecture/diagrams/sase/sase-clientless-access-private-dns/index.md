<h2 id="introduction">Introduction</h2>
<p>Using Cloudflare to access private resources - such as applications, servers, and networks that are not exposed directly to the internet - usually involves deploying an (<a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">agent</a>) to devices and then using a server-side agent (<a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">cloudflared</a>, <a href="/mesh/">Cloudflare Mesh</a>), to connect the private network or application to Cloudflare. This document describes an alternative approach which removes the need to deploy software to the user's device, making it easier for allowing third party access such as contractors and partners.</p>
<p>Typically, to provide access to internal resources, you use Cloudflare Zero Trust Network Access <a href="https://www.cloudflare.com/learning/access-management/what-is-ztna/">ZTNA</a> which supports two methods for how the user device accesses a private resource.</p>
<ul>
<li>
<p>A CNAME in public DNS, that resolves to a hostname representing the Cloudflare tunnel which proxies the request to the internal application.</p>
</li>
<li>
<p>An IP address exposed by Cloudflare tunnel, that again, proxies traffic direct to that IP address.</p>
</li>
</ul>
<h2 id="accessing-private-applications">Accessing private applications</h2>
<p>Some organizations don't like the idea of public DNS records which reference internal services, even though the ZTNA services provide strong access security, sometimes just the existence of a service name in public DNS is not desired. Exposing IP addresses directly to users is also a bad idea, they are hard to remember, and IP addresses can change. Unlike accessing a web application via a public DNS record through our proxy, applications exposed via private IP addresses also require the user to install an agent on their device to capture and route the traffic to Cloudflare which in turn routes it to the application. Installing this agent can be a challenge with third parties like partners or contractors.</p>
<p>So how do you allow access to private resources, without creating public DNS records and without requiring the user install software on their device? Cloudflare solved this challenge with <a href="/cloudflare-one/traffic-policies/resolver-policies/">Resolver Policies</a> where internal DNS services can be used. When combined with agentless <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>, it is possible to create Zero Trust access to private web applications with only a modern web browser. Policies to control access to apps are then written in our Secure Web Gateway (SWG) service as <a href="/cloudflare-one/traffic-policies/network-policies/">network firewall</a> policies. This method supports HTTP based applications, although Cloudflare does provide a browser rendering service for SSH and VNC services.</p>
<p>Follow this <a href="/cloudflare-one/tutorials/clientless-access-private-dns/">tutorial</a> for information on how to configure secure access to private web-based resources without having to deploy client agents.</p>
<p><img src="/assets/upstream/images/reference-architecture/sase-clientless-access-private-dns/diagram1.svg" alt="Figure 1: Remote Access Internal Hostname" title="Figure 1: Remote browser connected to private web service using internal hostname" /></p>
<ol>
<li>Users start their access by authenticating to the <a href="https://your_team_domain.cloudflareaccess.com/browser">Cloudflare Browser Isolation</a> service. Note this is a browser running on Cloudflare’s edge network, therefore all requests will by default be handled by Cloudflare. The contents are rendered back to the users’ browser via secure encrypted vector streams that use HTTPS and WebRTC channels.</li>
<li>Once the user has authenticated to the remote browser, they make a request to an internal hostname which is a record in the internal DNS service. e.g. <a href="https://app.company.internal">https://app.company.internal</a></li>
<li>Cloudflare looks up the internal hostname using <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a>, and gets the private IP address from the internal DNS server. This DNS resolution takes place within the Cloudflare network and requires no DNS client changes on the user's device.</li>
<li>Cloudflare evaluates the network firewall policies and verifies if the user has permission to reach the destination addresses.</li>
<li>If the request passes the policy, it is sent via secure <a href="https://blog.cloudflare.com/getting-cloudflare-tunnels-to-connect-to-the-cloudflare-network-with-quic">QUIC</a> tunnels to the Cloudflared connectors which then is reverse proxied to the application servers. All data is transmitted securely through Cloudflare back to the users’ browser via encrypted vector streams.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/tutorials/clientless-access-private-dns/">Tutorial: Access a web application via its private hostname without the Cloudflare One Client</a></li>
</ul>
