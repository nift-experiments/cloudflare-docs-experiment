---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/guides/aws/
  description: Deploy Cloudflare Tunnel on Amazon Web Services.
  full_title: Deploy cloudflared in AWS · Cloudflare Docs
  head_html: <title>Deploy cloudflared in AWS · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Cloudflare Tunnel on Amazon Web Services."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/guides/aws/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/guides/aws/index.md"><meta property="og:title" content="Deploy cloudflared in AWS · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Cloudflare Tunnel on Amazon Web Services."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/guides/aws/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="AWS,Integration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/guides/aws/#page","headline":"Deploy cloudflared in AWS \u00b7 Cloudflare Docs","description":"Deploy Cloudflare Tunnel on Amazon Web Services.","url":"https://developers.cloudflare.com/tunnel/guides/aws/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AWS","Integration"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/guides/aws/
  schema: 1
---
<p>This guide covers how to connect an Amazon Web Services (AWS) EC2 instance to Cloudflare using <code>cloudflared</code> and publish a web application through a Cloudflare Tunnel.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><a href="/fundamentals/manage-domains/add-site/">Add a website to Cloudflare</a></li>
</ul>
<h2 id="1-create-an-ec2-instance"><ol>
<li>Create an EC2 instance</li>
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
<pre tabindex="0"><code class="language-sh">cd Downloads&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">chmod 400 &quot;YourKeyPair.pem&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">ssh -i &quot;YourKeyPair.pem&quot; ubuntu@ec2-44-202-59-16.compute-1.amazonaws.com&#10;</code></pre>
<ol start="12">
<li>
<p>Run <code>sudo su</code> to gain full admin rights to the instance.</p>
</li>
<li>
<p>For testing purposes, you can deploy a basic Apache web server on port <code>80</code>:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-bash">apt update&#10;&#10;apt -y install apache2&#10;&#10;cat &lt;&lt;EOF &gt; /var/www/html/index.html&#10;&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;&lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;&lt;/body&gt;&lt;/html&gt;&#10;EOF&#10;</code></pre>
<ol start="14">
<li>To verify that the Apache server is running, open a browser and go to <code>http://ec2-44-202-59-16.compute-1.amazonaws.com</code> (make sure to connect over <code>http</code>, not <code>https</code>). You should see the <strong>Hello Cloudflare!</strong> test page.</li>
</ol>
<h2 id="2-create-a-tunnel"><ol start="2">
<li>Create a tunnel</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
<li>Select <strong>Create Tunnel</strong> and enter a name (for example, <code>aws-tunnel</code>).</li>
<li>Select <strong>Create Tunnel</strong>.</li>
<li>Under <strong>Setup Environment</strong>, select <strong>Debian 64-bit</strong>.</li>
<li>Copy the install commands and run them on your EC2 instance.</li>
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
<p>To test, open a browser and go to the hostname you configured. You should see your web server's page.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-private-network-access">Looking for private network access?</h3>
@markup("md", "content/.markup/bodies/14937.md")
</aside>
<h2 id="firewall-configuration">Firewall configuration</h2>
<p>To secure your AWS instance, you can configure your <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html">Security Group rules</a> to deny all inbound traffic and allow only outbound traffic to the <a href="/tunnel/configuration/#required-ports">Cloudflare Tunnel IP addresses</a>. All Security Group rules are Allow rules; traffic that does not match a rule is blocked. Therefore, you can delete all inbound rules and leave only the relevant outbound rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14936.md")
</aside>
<p>After configuring your Security Group rules, verify that you can still access the service through Cloudflare Tunnel via its <a href="#3-publish-an-application">public hostname</a>. The service should no longer be accessible from outside Cloudflare Tunnel -- for example, if you go to <code>http://ec2-44-202-59-16.compute-1.amazonaws.com</code> the test page should no longer load.</p>
