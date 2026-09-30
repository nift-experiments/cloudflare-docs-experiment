<p>To enable clientless access to your applications, you will need to create a Cloudflare Tunnel that publishes applications to a domain on Cloudflare. A published application creates a public DNS record that routes traffic to a specific address, protocol, and port associated with a private application. For example, you can define a public hostname (<code>mywebapp.example.com</code>) to provide access to a web server running on <code>https://localhost:8080</code>. When a user goes to <code>mywebapp.example.com</code> in their browser, their request will first route to a Cloudflare data center where it is inspected against your configured security policies. Cloudflare will then forward validated requests down your tunnel to the web server.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/handshake.jpg" alt="How an HTTP request reaches a private application connected with Cloudflare Tunnel" /></p>
<h2 id="create-a-tunnel">Create a tunnel</h2>
<p>To create a Cloudflare Tunnel:</p>
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
<h2 id="publish-an-application">Publish an application</h2>
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
@markup("md", "content/.markup/bodies/9684.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-routing">Path routing</h3>
@markup("md", "content/.markup/bodies/9683.md")
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
<p>All users on the Internet can now connect to this application via its public hostname. In <a href="/learning-paths/clientless-access/access-application/">Module 4: Secure your applications</a>, we will discuss how to restrict access to authorized users.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9682.md")
</aside>
<h2 id="additional-resources">Additional resources</h2>
<p>For more control over how traffic routes through your tunnel, refer to the following links:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/">DNS records</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/">Load balancer</a></li>
</ul>
