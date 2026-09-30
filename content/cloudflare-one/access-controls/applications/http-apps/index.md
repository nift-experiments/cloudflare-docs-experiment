<p>Cloudflare Access allows you to secure your web applications by acting as an identity-aware proxy. Access sits in front of your application and checks each request against your <a href="/cloudflare-one/access-controls/policies/">Access policies</a> before allowing it through. You can use signals from your existing identity providers (IdPs), device posture providers, and <a href="/cloudflare-one/access-controls/policies/#selectors">other selectors</a> to control who can reach the application.</p>
<p><img src="/assets/upstream/images/cloudflare-one/applications/diagram-saas.jpg" alt="Cloudflare Access verifies a user's identity before granting access to your application." /></p>
<p>You can protect the following types of web applications:</p>
<ul>
<li>
<p><a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/"><strong>SaaS applications</strong></a> consist of applications your team relies on that are not hosted by your organization. Examples include Salesforce and Workday. To secure SaaS applications, you must integrate Cloudflare Access with the SaaS application's SSO configuration.</p>
</li>
<li>
<p><strong>Self-hosted applications</strong> consist of internal applications that you host in your own environment. These can be the data center versions of tools like the Atlassian suite or applications created by your own team. Setup requirements for a self-hosted application depend on whether the application is publicly accessible on the Internet or restricted to users on a private network.</p>
<ul>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/"><strong>Public hostname applications</strong></a> are web applications that have public DNS records. Anyone on the Internet can access the application by entering the URL in their browser and authenticating through Cloudflare Access. Securing access to a public website requires a Cloudflare DNS <a href="/dns/zone-setups/full-setup/">full setup</a> or <a href="/dns/zone-setups/partial-setup/">partial CNAME setup</a>.</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/"><strong>Private network applications</strong></a> do not have public DNS records, meaning they are not reachable from the public Internet. To connect using a private IP or private hostname, the user's traffic must route through Cloudflare Gateway. The preferred method is to install the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on the user's device. Alternative options include forwarding traffic from a <a href="/cloudflare-wan/">network location</a>, using <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a>, or <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a>.</li>
</ul>
</li>
<li>
<p><a href="/cloudflare-one/access-controls/ai-controls/"><strong>Model Context Protocol (MCP) servers</strong></a> are web applications that enable generative AI tools to read and write data within your business applications. For example, Salesforce provides an <a href="https://github.com/salesforcecli/mcp">MCP server</a> for developers to interact with resources in their Salesforce tenant using GitHub Copilot or other AI code editors.</p>
</li>
<li>
<p><a href="/fundamentals/manage-members/dashboard-sso/"><strong>Cloudflare Dashboard SSO</strong></a> is a special type of SaaS application that manages SSO settings for the Cloudflare dashboard and has limited permissions for administrator edits.</p>
</li>
</ul>
