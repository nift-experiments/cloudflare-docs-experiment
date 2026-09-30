<p>This guide covers how to connect an Amazon Web Services (AWS) virtual machine to Cloudflare using our lightweight connector, <code>cloudflared</code>.</p>
<p>We will deploy:</p>
<ul>
<li>An EC2 virtual machine that runs a basic HTTP server.</li>
<li>A Cloudflare Tunnel that allows users to connect to the service via either a public hostname or a private IP address.</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5341.md")
</aside>
<h3 id="prerequisites">Prerequisites</h3>
<p>To complete the following procedure, you will need to:</p>
<ul>
<li><a href="/fundamentals/manage-domains/add-site/">Add a website to Cloudflare</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Deploy the Cloudflare One Client</a> on an end-user device</li>
</ul>
<h2 id="1-create-a-vm-instance-in-aws"><ol>
<li>Create a VM instance in AWS</li>
</ol></h2>
<ol>
<li>
<p>From the AWS console, go to <strong>Compute</strong> &gt; <strong>EC2</strong> &gt; <strong>Instances</strong></p>
</li>
<li>
<p>Select <strong>Launch instance</strong>.</p>
</li>
<li>
<p>Name your VM instance. In this example we will name it <code>http-test-server</code>.</p>
</li>
<li>
<p>For *<em>Amazon Machine Image (AMI)</em> choose your desired operating system and specifications. For this example, we will use <em>Ubuntu Server 24.04 LTS (HVM), SSD Volume Type</em>.</p>
</li>
<li>
<p>For <strong>Instance type:</strong>, you can select <em>t2.micro</em> which is available on the free tier.</p>
</li>
<li>
<p>In <strong>Key pair (login)</strong>, create a new key pair to use for SSH. You will need to download the <code>.pem</code> file onto your local machine.</p>
</li>
<li>
<p>In <strong>Network settings</strong>, select <strong>Create security group</strong>.</p>
</li>
<li>
<p>Turn on the following Security Group rules:</p>
<ul>
<li><strong>Allow SSH traffic from <em>My IP</em></strong> to prevent the instance from being publicly accessible.</li>
<li><strong>Allow HTTPS traffic from the internet</strong></li>
<li><strong>Allow HTTP traffic from the internet</strong></li>
</ul>
</li>
<li>
<p>Select <strong>Launch instance</strong>.</p>
</li>
<li>
<p>Once the instance is up and running, go to the <strong>Instances</strong> summary page and copy its <strong>Public IPv4 DNS</strong> hostname (for example, <code>ec2-44-202-59-16.compute-1.amazonaws.com</code>).</p>
</li>
<li>
<p>To log in to the instance over SSH, open a terminal and run the following commands:</p>
</li>
</ol>
<pre><code class="language-sh">cd Downloads&#10;</code></pre>
<pre><code class="language-sh">chmod 400 &quot;YourKeyPair.pem&quot;&#10;</code></pre>
<pre><code class="language-sh">ssh -i &quot;YourKeyPair.pem&quot; ubuntu@ec2-44-202-59-16.compute-1.amazonaws.com&#10;</code></pre>
<ol start="12">
<li>
<p>Run <code>sudo su</code> to gain full admin rights to the instance.</p>
</li>
<li>
<p>For testing purposes, you can deploy a basic Apache web server on port <code>80</code>:</p>
</li>
</ol>
<pre><code class="language-bash">apt update&#10;&#10;apt -y install apache2&#10;&#10;cat &lt;&lt;EOF &gt; /var/www/html/index.html&#10;&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;&lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;&lt;/body&gt;&lt;/html&gt;&#10;EOF&#10;</code></pre>
<ol start="14">
<li>To verify that the Apache server is running, open a browser and go to <code>http://ec2-44-202-59-16.compute-1.amazonaws.com</code> (make sure to connect over <code>http</code>, not <code>https</code>). You should see the <strong>Hello Cloudflare!</strong> test page.</li>
</ol>
<h2 id="2-create-a-cloudflare-tunnel"><ol start="2">
<li>Create a Cloudflare Tunnel</li>
</ol></h2>
<p>Create a Cloudflare Tunnel and run it on the AWS instance.</p>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel (for example, <code>aws-tunnel</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system (select <strong>Debian</strong> for your AWS instance). Copy the installation command and run it on your AWS instance.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
</ol>
<h2 id="3-connect-using-a-public-hostname"><ol start="3">
<li>Connect using a public hostname</li>
</ol></h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">Published applications</a> allow anyone on the Internet to connect to HTTP resources hosted on your virtual private cloud (VPC). To add a published application for your Cloudflare Tunnel:</p>
<ol>
<li>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</li>
<li>Enter a hostname for the application (for example, <code>hellocloudflare.&lt;your-domain&gt;.com</code>).</li>
<li>Under <strong>Service</strong>, enter <code>http://localhost:80</code>.</li>
<li>Select <strong>Add route</strong>.</li>
<li>To test, open a browser and go to <code>http://hellocloudflare.&lt;your-domain&gt;.com</code>. You should see the <strong>Hello Cloudflare!</strong> test page.</li>
</ol>
<p>You can optionally <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">create an Access application</a> to control who can access the service.</p>
<h2 id="4-connect-using-a-private-ip"><ol start="4">
<li>Connect using a private IP</li>
</ol></h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Private network routes</a> allow users to connect to your virtual private cloud (VPC) using the Cloudflare One Client. To add a private network route for your Cloudflare Tunnel:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the <strong>Private IP address</strong> of your AWS instance (for example, <code>172.31.19.0</code>), and select <strong>Create route</strong>. You can expand the IP range later if necessary.</p>
</li>
<li>
<p>In your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#add-a-route">Split Tunnel configuration</a>, make sure the private IP is routing through the Cloudflare One Client. For example, if you are using Split Tunnels in <strong>Exclude</strong> mode, delete <code>172.16.0.0/12</code>. We recommend re-adding the IPs that are not explicitly used by your AWS instance.</p>
<pre><code>To determine which IP addresses to re-add, subtract your AWS instance IPs from &lt;code&gt;172.16.0.0/12&lt;/code&gt;:&#10;</code></pre>
</li>
</ol>
<div class="nb-interactive-component" data-cf-component="SubtractIPCalculator"></div>
<pre><code>    Add the results back to your Split Tunnel Exclude mode list.&#10;</code></pre>
<ol start="4">
<li>
<p>To test on a user device:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Log in to the Cloudflare One Client</a>.</li>
<li>Open a terminal window and connect to the service using its private IP:</li>
</ol>
<pre><code class="language-sh">`curl 172.31.19.0`</code></pre>
</li>
</ol>
<pre><code class="language-txt">&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;&lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;&lt;/body&gt;&lt;/html&gt;&#10;</code></pre>
<p>You can optionally <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#4-recommended-filter-network-traffic-with-gateway">create Gateway network policies</a> to control who can access the AWS instance via its private IP.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5340.md")
</aside>
<h2 id="firewall-configuration">Firewall configuration</h2>
<p>To secure your AWS instance, you can configure your <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html">Security Group rules</a> to deny all inbound traffic and allow only outbound traffic to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#required-for-tunnel-operation">Cloudflare Tunnel IP addresses</a>. All Security Group rules are Allow rules; traffic that does not match a rule is blocked. Therefore, you can delete all inbound rules and leave only the relevant outbound rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5339.md")
</aside>
<p>After configuring your Security Group rules, verify that you can still access the service through Cloudflare Tunnel via its <a href="#3-connect-using-a-public-hostname">public hostname</a> or <a href="#4-connect-using-a-private-ip">private IP</a>. The service should no longer be accessible from outside Cloudflare Tunnel -- for example, if you go to <code>http://ec2-44-202-59-16.compute-1.amazonaws.com</code> the test page should no longer load.</p>
