<p>This page contains terminology specific to locally-managed Cloudflare Tunnels. For general Tunnel terminology, refer to the <a href="/tunnel/get-started/">Get started section</a>.</p>
<h2 id="default-cloudflared-directory">Default <code>cloudflared</code> directory</h2>
<p><code>cloudflared</code> uses a default directory when storing credentials files for your tunnels, as well as the <code>cert.pem</code> file it generates when you run <code>cloudflared login</code>. The default directory is also where <code>cloudflared</code> will look for a <a href="#configuration-file">configuration file</a> if no other file path is specified when running a tunnel.</p>
<table>
<thead>
<tr>
<th>OS</th>
<th>Path to default directory</th>
</tr>
</thead>
<tbody>
<tr>
<td>Windows</td>
<td><code>%USERPROFILE%\.cloudflared</code></td>
</tr>
<tr>
<td>macOS and Unix-like systems</td>
<td><code>~/.cloudflared</code>, <code>/etc/cloudflared</code>, and <code>/usr/local/etc/cloudflared</code>, in this order.</td>
</tr>
</tbody>
</table>
<h2 id="configuration-file">Configuration file</h2>
<p>This is a YAML file that functions as the operating manual for <code>cloudflared</code>. <code>cloudflared</code> will automatically look for the configuration file in the <a href="#default-cloudflared-directory">default <code>cloudflared</code> directory</a>, but you can store your configuration file in any directory. It is recommended to always specify the file path for your configuration file whenever you reference it. By creating a configuration file, you can have fine-grained control over how their instance of <code>cloudflared</code> will operate. This includes operations like what you want <code>cloudflared</code> to do with traffic (for example, proxy websockets to port <code>xxxx</code> or SSH to port <code>yyyy</code>), where <code>cloudflared</code> should search for authorization (credentials file, tunnel token), and what mode it should run in (for example, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/"><code>warp-routing</code></a>). In the absence of a configuration file, cloudflared will proxy outbound traffic through port <code>8080</code>. For more information on how to create, store, and structure a configuration file, refer to the <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">dedicated instructions</a>.</p>
<h2 id="cert-pem">Cert.pem</h2>
<p>This is the certificate file issued by Cloudflare when you run <code>cloudflared tunnel login</code>. This file uses a certificate to authenticate your instance of <code>cloudflared</code> and it is required when you create new tunnels, delete existing tunnels, change DNS records, or configure tunnel routing from cloudflared. This file is not required to perform actions such as running an existing tunnel or managing tunnel routing from the Cloudflare dashboard. Refer to the <a href="/tunnel/features/locally-managed-tunnels/tunnel-permissions/">Tunnel permissions page</a> for more details on when this file is needed.</p>
<p>The <code>cert.pem</code> origin certificate is valid for at least 10 years, and the service token it contains is valid until revoked.</p>
<h2 id="credentials-file">Credentials file</h2>
<p>This file is created when you run <code>cloudflared tunnel create &lt;NAME&gt;</code>. It stores your tunnel's credentials in JSON format, and is unique to each tunnel. This file functions as a token authenticating the tunnel it is associated with. Refer to the <a href="/tunnel/features/locally-managed-tunnels/tunnel-permissions/">Tunnel permissions page</a> for more details on when this file is needed.</p>
<h2 id="ingress-rule">Ingress rule</h2>
<p>Ingress rules let you specify which local services traffic should be proxied to. If a rule does not specify a path, all paths will be matched. <code>cloudflared</code> forwards the full request path to the service without stripping or rewriting it. Ingress rules can be listed in your <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">configuration file</a> or when running <code>cloudflared tunnel ingress</code>.</p>
