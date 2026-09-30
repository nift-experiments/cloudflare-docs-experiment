<p>With Cloudflare Zero Trust, users can connect to non-HTTP applications via a public hostname without installing the Cloudflare One Client. This method requires you to onboard a domain to Cloudflare and install <code>cloudflared</code> on both the server and the user's device.</p>
<p>Users log in to the application by running a <code>cloudflared access</code> command in their terminal. <code>cloudflared</code> will launch a browser window and prompt the user to authenticate with your identity provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4889.md")
</aside>
<p>For examples of how to connect to Access applications with client-side <code>cloudflared</code>, refer to these tutorials:</p>
<ul>
<li><a href="/cloudflare-one/tutorials/cli/">Connect through Access using a CLI</a></li>
<li><a href="/cloudflare-one/tutorials/kubectl/">Connect through Access using kubectl</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/">Connect to SSH with client-side cloudflared</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/#connect-to-rdp-server-with-cloudflared-access">Connect over RDP with cloudflared</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/">Connect over SMB with cloudflared</a></li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/">Connect over arbitrary TCP with cloudflared</a></li>
</ul>
