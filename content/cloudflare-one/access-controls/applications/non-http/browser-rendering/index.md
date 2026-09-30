<p>Cloudflare can render SSH, VNC, and RDP applications in a browser without the need for client software or end-user configuration changes. For SSH and VNC, user email prefixes must match their username on the server. RDP leverages your existing Windows usernames and passwords for authenticating to the Windows server; Cloudflare does not manage any credentials on the Windows server.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Browser rendering is only supported for <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted public applications</a>, not private IPs or hostnames.</li>
<li>You can only render a browser-rendered terminal on domains and subdomains, not on specific paths.</li>
<li></li>
</ul>
<p>Cloudflare does not control the length of an active SSH, VNC, or RDP session. <a href="/cloudflare-one/access-controls/access-settings/session-management/">Application session durations</a> determine the window in which a user can initiate a new connection or refresh an existing one.</p>
<ul>
<li>Cloudflare uses TLS to secure the egress RDP connection to your Windows server. We do not currently validate the chain of trust.</li>
</ul>
<h2 id="turn-on-browser-rendering">Turn on browser rendering</h2>
<h3 id="ssh-and-vnc">SSH and VNC</h3>
<p>To turn on browser rendering for an SSH or VNC application:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Locate the SSH or VNC application you created when <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">connecting the server to Cloudflare</a>. Select <strong>Configure</strong>.</li>
<li>Turn on <strong>Allow access through browser-based RDP, SSH, or VNC sessions</strong>, then select <em>SSH</em> or <em>VNC</em>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4819.md")
</aside>
4. Select **Save**.
<p>When users authenticate and visit the URL of the application, Cloudflare will render a terminal in their browser.</p>
<h3 id="rdp">RDP</h3>
<p>To set up browser-rendering for RDP, refer to our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">browser-based RDP guide</a>.</p>
<h3 id="ssh-key-exchange-algorithms">SSH key exchange algorithms</h3>
<p>Cloudflare's browser-rendered SSH terminal supports the following Key Exchange (KEX) algorithms:</p>
<pre><code>- `curve25519-sha256@libssh.org`&#10;- `curve25519-sha256`&#10;- `ecdh-sha2-nistp256`&#10;- `ecdh-sha2-nistp384`&#10;- `ecdh-sha2-nistp521`&#10;</code></pre>
<p>For browser-rendered SSH connections to work, you may need to update the <code>sshd_config</code> file on your server to accept these algorithms.</p>
