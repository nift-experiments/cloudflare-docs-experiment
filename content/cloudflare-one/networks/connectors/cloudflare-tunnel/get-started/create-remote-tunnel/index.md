<p>Follow this step-by-step guide to create your first <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/tunnel-useful-terms/#remotely-managed-tunnel">remotely-managed tunnel</a>.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5296.md")
</aside>
<h2 id="1-create-a-tunnel"><ol>
<li>Create a tunnel</li>
</ol></h2>
<div class="video-frame"><img class="video-poster" src="https://pub-d9bf66e086fb4b639107aa52105b49dd.r2.dev/tunnel%204_%20set%20up%20tunnel.png" alt="How to set up Cloudflare Tunnel"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/4b75ad2aa58700602e94b148827687a2/iframe?preload=true&amp;letterboxColor=transparent" title="How to set up Cloudflare Tunnel" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, <code>enterprise-VPC-01</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system, then copy the installation command and run it in a terminal on your origin server.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
</ol>
<p>The next steps depend on whether you want to <a href="#2a-publish-an-application">publish an application to the Internet</a> or <a href="#2b-connect-a-network">connect a private network</a>.</p>
<h2 id="2a-publish-an-application">2a. Publish an application</h2>
<p>Follow these steps to publish an application to the Internet. If you are looking to connect a private resource, skip to the <a href="#2b-connect-a-network">Connect a network</a> section.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/5295.md")
</aside>
<p>After creating your tunnel, add a published application route:</p>
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>, then select your tunnel.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</p>
</li>
<li>
<p>Enter a subdomain and select a <strong>Domain</strong> from the drop-down menu. Specify any subdomain or path information.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5294.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-routing">Path routing</h3>
@markup("md", "content/.markup/bodies/5293.md")
</aside>
<ol start="4">
<li>
<p>In <strong>Service URL</strong>, enter the protocol and address of your application (for example, <code>http://localhost:8000</code>). Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/">supported protocols</a> for available options.</p>
<p>If your origin already serves HTTPS or redirects HTTP to HTTPS, refer to <a href="/tunnel/troubleshooting/https-origins/">Troubleshoot HTTPS origins with Cloudflare Tunnel</a> before choosing the service URL.</p>
</li>
<li>
<p>Select <strong>Add route</strong>.</p>
</li>
</ol>
<p>Anyone on the Internet can now access the application at the specified hostname. To allow or block specific users, <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">create an Access application</a>.</p>
<h2 id="2b-connect-a-network">2b. Connect a network</h2>
<p>To connect a private network through your tunnel, add a CIDR route:</p>
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create route</strong>, then choose <strong>Tunnel CIDR</strong>.</li>
<li>Select the tunnel you just created.</li>
<li>In <strong>Network</strong>, enter the private IP address or CIDR range of your service (for example, <code>10.0.0.1</code> or <code>10.0.0.0/24</code>).</li>
<li>Select <strong>Create route</strong>.</li>
</ol>
<p><code>cloudflared</code> can now route traffic to these destination IPs. To configure Zero Trust policies and connect as a user, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Connect an IP/CIDR</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5292.md")
</aside>
<h2 id="3-view-your-tunnel"><ol start="3">
<li>View your tunnel</li>
</ol></h2>
<p>After saving the tunnel, you will be redirected to the <strong>Networking</strong> &gt; <strong>Tunnels</strong> page. Your tunnel should be listed with a <code>Healthy</code> status. If your tunnel status is <code>Inactive</code>, <code>Down</code>, or <code>Degraded</code>, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">troubleshooting documentation</a> for recommended next steps.</p>
