<p>This guide covers how to connect a Google Cloud Platform (GCP) virtual machine to Cloudflare using <code>cloudflared</code> and publish a web application through a Cloudflare Tunnel.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><a href="https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project">A Google Cloud Project</a></li>
<li><a href="/fundamentals/manage-domains/add-site/">A zone on Cloudflare</a></li>
</ul>
<h2 id="1-create-a-vm-instance"><ol>
<li>Create a VM instance</li>
</ol></h2>
<ol>
<li>
<p>In your <a href="https://console.cloud.google.com/">Google Cloud Console</a>, <a href="https://developers.google.com/workspace/guides/create-project">create a new project</a>.</p>
</li>
<li>
<p>Go to <strong>Compute Engine</strong> &gt; <strong>VM instances</strong>.</p>
</li>
<li>
<p>Select <strong>Create instance</strong>.</p>
</li>
<li>
<p>Name your VM instance. In this example we will name it <code>http-test-server</code>.</p>
</li>
<li>
<p>Choose your desired operating system and specifications. For this example, you can use the following settings:</p>
<ul>
<li><strong>Machine family:</strong> General Purpose</li>
<li><strong>Series:</strong> E2</li>
<li><strong>Machine type:</strong> e2-micro</li>
<li><strong>Boot disk image:</strong> Debian GNU/Linux 12</li>
<li><strong>Firewalls</strong>: Allow HTTP and HTTPS traffic</li>
</ul>
</li>
<li>
<p>Under <strong>Advanced options</strong> &gt; <strong>Management</strong> &gt; <strong>Automation</strong>, add the following startup script. This example deploys a basic Apache web server on port <code>80</code>.</p>
</li>
</ol>
<pre><code class="language-bash">&#35;!/bin/bash&#10;apt update&#10;apt -y install apache2&#10;cat &lt;&lt;EOF &gt; /var/www/html/index.html&#10;&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;&lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;&lt;/body&gt;&lt;/html&gt;&#10;EOF&#10;</code></pre>
<ol start="7">
<li>
<p>Select <strong>Create</strong>.</p>
</li>
<li>
<p>The operating system automatically starts the Apache HTTP server. To verify that the server is running:</p>
<ol>
<li>Copy the <strong>External IP</strong> for the VM instance.</li>
<li>Open a browser and go to <code>http://&lt;EXTERNAL IP&gt;</code>. You should see the <strong>Hello Cloudflare!</strong> test page.</li>
</ol>
</li>
<li>
<p>To login to the VM instance, open the dropdown next to <strong>SSH</strong> and select <em>Open in browser window</em>.</p>
</li>
</ol>
<h2 id="2-create-a-tunnel"><ol start="2">
<li>Create a tunnel</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
<li>Select <strong>Create Tunnel</strong> and enter a name (for example, <code>gcp-tunnel</code>).</li>
<li>Select <strong>Create Tunnel</strong>.</li>
<li>Under <strong>Setup Environment</strong>, select <strong>Debian 64-bit</strong>.</li>
<li>SSH into your VM and run the install commands shown in the dashboard.</li>
<li>Once the tunnel connects, select <strong>Continue</strong>.</li>
</ol>
<h2 id="3-publish-an-application"><ol start="3">
<li>Publish an application</li>
</ol></h2>
<ol>
<li>Under <strong>Routes</strong>, select <strong>Add route</strong> &gt; <strong>Published application</strong>.</li>
<li>Enter a hostname (for example, <code>hellocloudflare.&lt;your-domain&gt;.com</code>).</li>
<li>Under <strong>Service</strong>, enter <code>http://localhost:80</code>.</li>
<li>Select <strong>Add route</strong>.</li>
</ol>
<p>To test, open a browser and go to the hostname you configured.</p>
<p>You can optionally add <a href="/tunnel/integrations/#cloudflare-access">Cloudflare Access</a> to control who can reach the service.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-private-network-access">Looking for private network access?</h3>
@markup("md", "content/.markup/bodies/14933.md")
</aside>
<h2 id="firewall-configuration">Firewall configuration</h2>
<p>To secure your VM instance, you can <a href="https://cloud.google.com/firewall/docs/using-firewalls">configure your VPC firewall rules</a> to deny all ingress traffic and allow only egress traffic to the <a href="/tunnel/configuration/#required-ports">Cloudflare Tunnel IP addresses</a>. Since GCP denies ingress traffic by <a href="https://cloud.google.com/firewall/docs/firewalls#default_firewall_rules">default</a>, you can delete all ingress rules and leave only the relevant egress rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14932.md")
</aside>
<p>After configuring your VPC firewall rules, verify that you can still access the service through Cloudflare Tunnel via its <a href="#3-publish-an-application">public hostname</a>. The service should no longer be accessible from outside Cloudflare Tunnel -- for example, if you go to <code>http://&lt;EXTERNAL IP&gt;</code> the test page should no longer load.</p>
