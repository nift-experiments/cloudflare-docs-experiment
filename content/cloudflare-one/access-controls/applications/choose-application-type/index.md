<p>Cloudflare Access sits in front of your applications and checks every request against your Access policies before letting users through. It supports several application types, each designed for a different use case. Your choice depends on where your application is hosted, how users connect to it, and what level of control you need over sessions and authorization.</p>
<p>Most teams start with self-hosted applications and expand to SaaS applications, infrastructure targets, or a combination over time.</p>
<h2 id="compare-application-types">Compare application types</h2>
<p>The following table summarizes the key differences between each application type. For detailed setup instructions, refer to the section for each type.</p>
<table>
<thead>
<tr>
<th></th>
<th>Self-hosted application</th>
<th>SaaS application</th>
<th>Infrastructure application</th>
<th>Bookmark</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>What it protects</strong></td>
<td>Resources you own and manage: public web apps, private network destinations, and Cloudflare Workers</td>
<td>Third-party SaaS tools your team uses (Salesforce, Atlassian, Workday)</td>
<td>Individual servers and infrastructure targets, reachable over public or private network</td>
<td>External URLs displayed in the App Launcher (not gated by Access authentication)</td>
</tr>
<tr>
<td><strong>Requires Cloudflare One Client</strong></td>
<td>Depends on destination type and <a href="/cloudflare-one/access-controls/policies/">policy requirements</a></td>
<td>No</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td><strong>Clientless access available</strong></td>
<td>Yes (public hostnames, browser isolation, <code>cloudflared access</code> CLI)</td>
<td>Not applicable — users access the SaaS app directly</td>
<td>No</td>
<td>Not applicable</td>
</tr>
<tr>
<td><strong>Authentication and authorization</strong></td>
<td>Access policies with session management and application tokens signed to the application</td>
<td>Access policies with SAML/OIDC assertion</td>
<td>Infrastructure policies with protocol-aware authorization (ports, usernames)</td>
<td>Visibility-only policies for the App Launcher</td>
</tr>
<tr>
<td><strong>Private network routing required</strong></td>
<td>Only for private destinations</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td><strong>Session and token management</strong></td>
<td>Full (application tokens, session duration, forced re-authentication)</td>
<td>Full</td>
<td>Full</td>
<td>None</td>
</tr>
<tr>
<td><strong>Audit logging</strong></td>
<td>Authentication events and per-request Access logs</td>
<td>Authentication events</td>
<td>Authentication events, SSH command logs</td>
<td>App Launcher authentication only</td>
</tr>
<tr>
<td><strong>Use when</strong></td>
<td>Most use cases — web apps, private apps, Zero Trust networking, Workers</td>
<td>Enforcing compliance for SaaS apps, supporting multiple identity providers for SSO</td>
<td>Granular server access control with protocol-level authorization</td>
<td>Organizing links in a single portal</td>
</tr>
</tbody>
</table>
<h2 id="self-hosted-applications">Self-hosted applications</h2>
<p>Self-hosted applications are the most versatile application type and account for the majority of Access deployments. A self-hosted application represents any resource where you control where traffic goes — whether that is a public website on Cloudflare DNS, a non-web service on your private network connected with a Cloudflare Tunnel, or a Worker running on Cloudflare.</p>
<p>Self-hosted applications use the full Access policy engine, including session management, application tokens, forced re-authentication, device posture checks, and identity provider groups.</p>
<h3 id="public-hostname-applications">Public hostname applications</h3>
<p>If your application is already on the public Internet with DNS managed through Cloudflare (or a partial CNAME setup, where your DNS is hosted elsewhere but Cloudflare proxies the traffic), you can place Access in front of it by matching the application's hostname. Cloudflare proxies the request, presents a login page, and only forwards traffic to your origin after the user passes your Access policies.</p>
<p>This is the most common starting point. You do not need to install anything on the user's device — authentication happens entirely in the browser.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Add a self-hosted public application</a>.</p>
<h3 id="private-applications">Private applications</h3>
<p>You can also use self-hosted applications to protect resources on your private network by targeting specific private IPs, hostnames, or CIDR ranges (blocks of IP addresses, for example <code>10.0.0.0/8</code>) with an attached port or port range. This is the primary method for building Zero Trust network access on Cloudflare.</p>
<p>Private network applications require that users route traffic through Cloudflare — typically by running the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on their device. You must also connect your private network to Cloudflare using a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or <a href="/mesh/">Cloudflare Mesh</a>.</p>
<p>With private network applications, you define the same types of Access policies as you do for public applications, but apply them to private destinations. This gives you granular, identity-aware control over who can reach what on your network — replacing broad VPN-level access with per-application or per-service policies. Access policies are reusable, so you can apply the same policy across multiple applications.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Add a self-hosted private application</a>.</p>
<h3 id="protecting-workers">Protecting Workers</h3>
<p>Self-hosted applications can also protect a Cloudflare Worker directly by name, rather than by hostname or IP. When you select a Worker as the destination, you can cover the Worker together with all of its preview deployments, or cover the preview deployments only.</p>
<p>This is the safest and most straightforward way to put authentication in front of a Worker. Instead of configuring individual routes on the Worker and managing authentication at the route level, you link the entire Worker (and optionally its preview deployments) to an Access application. Any request to the Worker on any route passes through Access first.</p>
<p>For Workers-specific setup instructions, refer to <a href="/workers/configuration/cloudflare-access/">Cloudflare Access for Workers</a>.</p>
<h3 id="cli-access-with-cloudflared">CLI access with cloudflared</h3>
<p>Self-hosted applications support client-side <code>cloudflared</code> authentication. Users can install <code>cloudflared</code> on their device and run <code>cloudflared access login &lt;hostname&gt;</code> from the command line to authenticate through your Access policies without the Cloudflare One Client installed. This is useful for SSH sessions, API calls, and other command-line workflows where a browser-based login flow is impractical.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/">cloudflared authentication</a>.</p>
<h2 id="saas-applications">SaaS applications</h2>
<p>SaaS applications are for third-party tools that your organization uses but does not host — services like Salesforce, Atlassian, Slack, or Workday. With a SaaS application, you configure Cloudflare Access as the single sign-on (SSO) provider for the third-party service using SAML or OIDC, the two most common identity federation protocols.</p>
<p>When users sign in to the SaaS application, they are redirected to Cloudflare. Cloudflare redirects to your configured identity provider for authentication, then evaluates your Access policies against the authenticated user. If the user passes both checks, Cloudflare issues a signed credential (a SAML assertion or OIDC token) back to the SaaS application confirming the user's identity.</p>
<h3 id="when-to-use-saas-applications">When to use SaaS applications</h3>
<p>Use a SaaS application when you want to:</p>
<ul>
<li><strong>Enforce consistent Access policies across third-party tools.</strong> Apply the same identity, device posture, and location requirements that you use for your internal applications to external SaaS tools.</li>
<li><strong>Aggregate multiple identity providers.</strong> Cloudflare can federate authentication across multiple identity providers (IdPs), which means you can swap or add identity providers without reconfiguring each SaaS application individually. This is not typically possible with direct SSO integrations.</li>
<li><strong>Apply Cloudflare-specific controls.</strong> Enforce requirements that your SaaS provider cannot check on its own — for example, requiring the Cloudflare One Client or passing a device posture check before granting access to the SaaS tool.</li>
</ul>
<h3 id="limitations">Limitations</h3>
<p>SaaS applications require that the third-party tool supports SAML or OIDC federation. Not all SaaS tools offer this, and some impose restrictions on the number of SSO integrations or the features available through federated authentication. Check your SaaS vendor's documentation for SSO compatibility.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">SaaS applications</a>.</p>
<h2 id="infrastructure-applications">Infrastructure applications</h2>
<p>Infrastructure applications provide protocol-aware access control for servers and infrastructure targets, whether reachable over a public hostname or a private network. Unlike self-hosted applications, which evaluate whether a user can reach a destination, infrastructure applications also control what a user can do after connecting — which usernames they can authenticate as, which ports they can access, and which commands they can run.</p>
<p>Infrastructure applications require the Cloudflare One Client. For targets on your private network, you must also connect the network to Cloudflare through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or <a href="/mesh/">Cloudflare Mesh</a>.</p>
<h3 id="when-to-use-infrastructure-applications">When to use infrastructure applications</h3>
<p>Use an infrastructure application when you need:</p>
<ul>
<li><strong>Protocol-level authorization.</strong> Define policies that grant specific users access to specific ports and usernames on a target server.</li>
<li><strong>Command logging.</strong> All SSH sessions and commands are logged for compliance and auditing. You can export logs to a storage service or SIEM using <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</li>
<li><strong>Short-lived certificates.</strong> Eliminate long-lived SSH keys by authenticating users with certificates that expire quickly. This removes the risk of a stolen or forgotten key granting permanent access to your servers.</li>
</ul>
<p>Infrastructure applications support SSH. You can still use <a href="#self-hosted-applications">self-hosted applications</a> to secure access to servers over other protocols (including SSH), but infrastructure applications are the only way to supplementally control user authorization.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Add an infrastructure application</a>.</p>
<h2 id="bookmarks">Bookmarks</h2>
<p>Bookmarks are not secured by Access. A bookmark is a link to any URL that you want to display in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> alongside your other applications. You can assign Access policies to bookmarks, but those policies only control whether the bookmark tile is visible in the App Launcher — they do not protect the destination URL.</p>
<p>Use bookmarks to give users a single portal where they can find all of the tools they use, including external applications that are not integrated with Cloudflare.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/bookmarks/">Add bookmarks</a>.</p>
<h2 id="private-network-applications-legacy">Private network applications (legacy)</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4686.md")
</aside>
<p>The legacy private network application type creates Gateway Network policies to control access to a private IP address. When you add a legacy private network application, Cloudflare generates two Gateway rules — one Allow rule and one Block rule — because Gateway Network policies are not default-deny (unlike Access policies, which require an explicit Allow rule before any user can reach a protected application).</p>
<p>Legacy private network applications do not support per-session management, application tokens, or the full set of features available in Access policies. This application type is deprecated for new customers and remains available to existing customers.</p>
<p>If you are currently using legacy private network applications, we strongly recommend migrating to <a href="#private-applications">self-hosted private network applications</a> for more comprehensive policy controls and session management.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/">Private network applications (legacy)</a>.</p>
