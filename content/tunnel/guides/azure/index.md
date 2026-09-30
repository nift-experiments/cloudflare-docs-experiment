<p>This guide covers how to connect an Azure Virtual Machine to Cloudflare using <code>cloudflared</code> and publish a web application through a Cloudflare Tunnel.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><a href="/fundamentals/manage-domains/add-site/">Add a website to Cloudflare</a></li>
</ul>
<h2 id="1-create-a-virtual-machine"><ol>
<li>Create a Virtual Machine</li>
</ol></h2>
<ol>
<li>
<p>In the Azure portal, go to <strong>Virtual Machines</strong> &gt; <strong>Create</strong> &gt; <strong>Azure virtual machine</strong>.</p>
</li>
<li>
<p>Select a <strong>Resource group</strong> or create a new one.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/azure-1.png" alt="Azure group" /></p>
<ol start="3">
<li>
<p>Enter a name for the VM and select a region. For <strong>Image</strong>, select <em>Ubuntu Server 24.04 LTS</em>. For <strong>Size</strong>, select an appropriate size (for example, <em>Standard_B1s</em>).</p>
</li>
<li>
<p>Under <strong>Administrator account</strong>, select <strong>SSH public key</strong> and enter your key pair.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/azure-2.png" alt="Azure keypair" /></p>
<ol start="5">
<li>Under <strong>Inbound port rules</strong>, allow SSH (<code>22</code>). For testing purposes, also allow HTTP (<code>80</code>) and HTTPS (<code>443</code>).</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/azure-3.png" alt="Azure ports" /></p>
<ol start="6">
<li>
<p>Select <strong>Review + create</strong>, then <strong>Create</strong>.</p>
</li>
<li>
<p>Once the VM is running, copy its <strong>Public IP address</strong> from the VM overview page.</p>
</li>
<li>
<p>SSH into the instance:</p>
</li>
</ol>
<pre><code class="language-sh">ssh -i &quot;your-key.pem&quot; azureuser@&lt;PUBLIC_IP&gt;&#10;</code></pre>
<ol start="9">
<li>
<p>Run <code>sudo su</code> to gain full admin rights to the VM.</p>
</li>
<li>
<p>For testing purposes, you can deploy a basic Apache web server on port <code>80</code>:</p>
</li>
</ol>
<pre><code class="language-bash">apt update&#10;&#10;apt -y install apache2&#10;&#10;cat &lt;&lt;EOF &gt; /var/www/html/index.html&#10;&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;&lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;&lt;/body&gt;&lt;/html&gt;&#10;EOF&#10;</code></pre>
<ol start="11">
<li>To verify that the Apache server is running, open a browser and go to <code>http://&lt;PUBLIC_IP&gt;</code> (make sure to connect over <code>http</code>, not <code>https</code>). You should see the <strong>Hello Cloudflare!</strong> test page.</li>
</ol>
<h2 id="2-create-a-tunnel"><ol start="2">
<li>Create a tunnel</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
<li>Select <strong>Create Tunnel</strong> and enter a name (for example, <code>azure-tunnel</code>).</li>
<li>Select <strong>Create Tunnel</strong>.</li>
<li>Under <strong>Setup Environment</strong>, select <strong>Debian 64-bit</strong>.</li>
<li>Copy the install commands and run them on your Azure VM.</li>
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
<p>To test, open a browser and go to the hostname you configured. You should see the <strong>Hello Cloudflare!</strong> test page.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-private-network-access">Looking for private network access?</h3>
@markup("md", "content/.markup/bodies/14935.md")
</aside>
<h2 id="firewall-configuration">Firewall configuration</h2>
<p>To secure your Azure VM, you can configure your <a href="https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview">Network Security Group (NSG)</a> to deny all inbound traffic and allow only outbound traffic to the <a href="/tunnel/configuration/#required-ports">Cloudflare Tunnel IP addresses</a>. All NSG rules are evaluated by priority; traffic that does not match an allow rule is blocked by the default deny rules. Therefore, you can delete all custom inbound rules and leave only the relevant outbound rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14934.md")
</aside>
<p>After configuring your NSG rules, verify that you can still access the service through Cloudflare Tunnel via its <a href="#3-publish-an-application">public hostname</a>. The service should no longer be accessible from outside Cloudflare Tunnel — for example, direct access to the VM's public IP should no longer work.</p>
