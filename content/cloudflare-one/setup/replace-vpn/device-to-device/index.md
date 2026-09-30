<p>Create a secure connection between two devices so they can communicate directly through Cloudflare's network, without needing to be on the same physical network. This is useful when you need to remotely access a specific device, for example connecting to a home computer from a laptop at a coffee shop.</p>
<p>To explore other connection scenarios, refer to <a href="/cloudflare-one/setup/replace-vpn/">Replace your VPN</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> is an app that you install on each device you want to connect. When you enroll a device in your Cloudflare account, it is assigned a <a href="/cloudflare-one/networks/routes/reserved-ips/#device-ips">Mesh IP</a>.</p>
<p>Devices use their Mesh IPs to communicate with each other through Cloudflare's network. This works for most common types of network traffic, including web requests, remote desktop, file sharing, and ping.</p>
<p>Only devices enrolled in your Cloudflare account can reach these addresses, so they are not accessible to anyone outside your organization. No tunnel infrastructure or network configuration is required, and the connection does not disrupt existing traffic on your network.</p>
<p>For more details, refer to <a href="/mesh/guides/connect-client-devices/">Connect client devices</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>Two Linux, Windows, macOS, Android, or iOS devices you want to connect together.</li>
</ul>
<h2 id="step-1-enroll-your-first-device">Step 1: Enroll your first device</h2>
<p>Enrollment permissions control which users can connect devices to your account. In this step, you set an enrollment email and download the Cloudflare One Client. The email you provide becomes the first allowed login for your organization, and anyone with that email address can enroll a device.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add a node</strong>, then follow the wizard. The wizard configures enrollment permissions and Mesh connectivity automatically.</li>
<li>Download the Cloudflare One Client on your first device from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">downloads page</a>.</li>
<li>Open the client, enter your team name, and sign in with your email.</li>
</ol>
<h2 id="step-2-enroll-your-second-device">Step 2: Enroll your second device</h2>
<p>Both devices must be enrolled in your Cloudflare account for the connection to work.</p>
<ol>
<li>Download the Cloudflare One Client on your second device.</li>
<li>Open the client, enter the same team name, and sign in.</li>
<li>The client should show as <strong>Connected</strong> on both devices.</li>
</ol>
<h2 id="step-3-verify-your-connection">Step 3: Verify your connection</h2>
<p>Both devices are now connected through Cloudflare's network using their assigned Mesh IPs.</p>
<p>To view your device's assigned Mesh IP:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Your connected devices appear with their Mesh IPs.</li>
</ol>
<p>To test connectivity, <code>ping</code> the Mesh IP of one device from the other.</p>
<h2 id="recommended-next-steps">Recommended next steps</h2>
<p>After verifying your connection, consider securing your connected devices with policies and access controls:</p>
<ul>
<li><strong>Set up Gateway policies</strong>: By default, all enrolled devices can reach each other over the Mesh IP space. Gateway policies let you scan, filter, and log traffic between your devices. For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>, <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>, and <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</li>
<li><strong>Create an Access application</strong>: Restrict access to specific destinations on enrolled devices with identity-based rules. For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Secure a private IP or hostname</a>.</li>
</ul>
<p>For in-depth guidance on policy design and device posture checks, refer to the <a href="/learning-paths/replace-vpn/concepts/">Replace your VPN learning path</a>.</p>
<h2 id="troubleshoot">Troubleshoot</h2>
<p>If you have issues connecting, try these steps:</p>
<ul>
<li><strong>Windows users</strong>: Windows Firewall blocks device-to-device traffic by default. You may need to add a firewall rule that allows incoming traffic from <code>100.96.0.0/12</code>. For details, refer to <a href="/mesh/guides/connect-client-devices/">Connect client devices</a>.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/">Troubleshoot the Cloudflare One Client</a>: resolve connection and enrollment issues.</li>
</ul>
