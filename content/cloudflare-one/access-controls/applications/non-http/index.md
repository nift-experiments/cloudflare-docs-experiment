<p>Cloudflare offers both client-based and clientless ways to grant secure access to non-HTTP applications.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4818.md")
</aside>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/205bdeb4-3e37-4b04-f430-8b5c06a9b300/public" alt="SASE - Secure remote access to your critical infrastructure"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/f13b085ed4d28a9dbb8faf19ae986125/iframe?preload=true&amp;letterboxColor=transparent" title="SASE - Secure remote access to your critical infrastructure" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="cloudflare-one-client">Cloudflare One Client</h2>
<p>Users can connect by installing the Cloudflare One Client on their device and enrolling in your Zero Trust organization. Remote devices connect to your applications as if they were on your private network. By default, all devices enrolled in your organization can access any private route. To restrict access, <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">create a self-hosted application</a> for a private IP range, port range, and/or hostname and build <a href="/cloudflare-one/access-controls/policies/">Access policies</a> or <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway firewall rules</a> that allow or block specific users.</p>
<p>If you would like to define how users access specific infrastructure servers within your network, <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">create an infrastructure application</a> in Access for Infrastructure. Access for Infrastructure provides an additional layer of control and visibility over how users access non-HTTP applications, including:</p>
<ul>
<li>Define fine-grained policies to govern who has access to specific servers and exactly how a user may access that server.</li>
<li>Eliminate SSH keys by using short-lived certificates to authenticate users.</li>
<li>Export SSH command logs to a storage service or SIEM solution using <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</li>
</ul>
<h2 id="clientless-access">Clientless access</h2>
<p>Clientless access methods are suited for organizations that cannot deploy the Cloudflare One Client or need to support third-party contractors where installing a client is not possible. Clientless access requires onboarding a domain to Cloudflare and configuring a public hostname in order to make the server reachable. Command logging is not supported.</p>
<h3 id="browser-rendered-terminal">Browser-rendered terminal</h3>
<p>Cloudflare's <a href="/cloudflare-one/access-controls/applications/non-http/browser-rendering/">browser-based terminal</a> allows users to connect over SSH, RDP, and VNC without any configuration. When users visit the public hostname URL (for example, <code>https://ssh.example.com</code>) and log in with their Access credentials, Cloudflare will render a terminal in their browser. For RDP connections, users must authenticate to the Windows server using their Windows username and password in addition to being authenticated by Cloudflare Access.</p>
<h3 id="client-side-cloudflared">Client-side cloudflared</h3>
<p>Users can log in to the application by installing <code>cloudflared</code> on their device and running a hostname-specific command in their terminal. For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/">cloudflared authentication</a>.</p>
<h2 id="related-resources">Related resources</h2>
<p>To connect to an application over a specific protocol, refer to these tutorials:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">SSH</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/">SMB</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/">RDP</a></li>
</ul>
