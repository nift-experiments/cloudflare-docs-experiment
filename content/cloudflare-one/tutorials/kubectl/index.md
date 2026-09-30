---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/
  description: Connecting to Cloudflare's network using kubectl. Create a Zero Trust policy for your machine. Create an outbound-only connection between your machine and Cloudflared's network.
  full_title: Connect through Cloudflare Access using kubectl · Cloudflare One docs
  head_html: <title>Connect through Cloudflare Access using kubectl · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connecting to Cloudflare&#x27;s network using kubectl. Create a Zero Trust policy for your machine. Create an outbound-only connection between your machine and Cloudflared&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/index.md"><meta property="og:title" content="Connect through Cloudflare Access using kubectl · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connecting to Cloudflare&#x27;s network using kubectl. Create a Zero Trust policy for your machine. Create an outbound-only connection between your machine and Cloudflared&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Kubernetes,TCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/#page","headline":"Connect through Cloudflare Access using kubectl \u00b7 Cloudflare One docs","description":"Connecting to Cloudflare's network using kubectl. Create a Zero Trust policy for your machine. Create an outbound-only connection between your machine and Cloudflared's network.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Kubernetes","TCP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/kubectl/
  schema: 1
---
<p>You can connect to machines over <code>kubectl</code> using Cloudflare's Zero Trust platform.</p>
<p><strong>This walkthrough covers how to:</strong></p>
<ul>
<li>Build a policy in Cloudflare Access to secure the machine</li>
<li>Connect a machine to Cloudflare's network using kubectl</li>
<li>Connect from a client machine</li>
</ul>
<p><strong>Before you start</strong></p>
<ul>
<li><a href="/fundamentals/manage-domains/add-site/">Add a website to Cloudflare</a></li>
</ul>
<p><strong>Time to complete:</strong></p>
<p>30 minutes</p>
<hr />
<h2 id="create-an-access-policy">Create an Access policy</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong>.</li>
<li>Select <strong>Self-hosted and private</strong>.</li>
<li>Select <strong>Add public hostname</strong> and input a subdomain. This will be the hostname where your application will be available to users.</li>
<li><a href="/cloudflare-one/access-controls/policies/policy-management/">Create a new policy</a> to control who can reach the application, or select existing policies.</li>
<li>Follow the remaining <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application creation steps</a> to publish the application.</li>
</ol>
<h2 id="install-cloudflared">Install <code>cloudflared</code></h2>
<p>Cloudflare Tunnel creates a secure, outbound-only connection between this machine and Cloudflare's network. With an outbound-only model, you can prevent any direct access to this machine and lock down any externally exposed points of ingress. And with that, no open firewall ports.</p>
<p>Cloudflare Tunnel is made possible through a lightweight daemon from Cloudflare called <code>cloudflared</code>. Download and install <code>cloudflared</code> on the DigitalOcean machine by following the instructions listed on the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Downloads</a> page.</p>
<h2 id="authenticate-cloudflared">Authenticate <code>cloudflared</code></h2>
<p>Run the following command to authenticate cloudflared into your Cloudflare account.</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel login&#10;</code></pre>
<p><code>cloudflared</code> will open a browser window and prompt you to log in to your Cloudflare account. If you are working on a machine that does not have a browser, or a browser window does not launch, you can copy the URL from the command-line output and visit the URL in a browser on any machine.</p>
<p>Choose any hostname presented in the list. Cloudflare will issue a certificate scoped to your account. You do not need to pick the specific hostname where you will serve the Tunnel.</p>
<h2 id="create-a-tunnel">Create a Tunnel</h2>
<p>Next, create a tunnel with the command below.</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel create &lt;NAME&gt;&#10;</code></pre>
<p>Replacing <code>&lt;NAME&gt;</code> with a name for the Tunnel. This name can be any value. A single Tunnel can also serve traffic for multiple hostnames to multiple services in your environment, including a mix of connection types like SSH and HTTP.</p>
<p>The command will output an ID for the Tunnel and generate an associated credentials file. At any time you can list the Tunnels in your account with the following command.</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel list&#10;</code></pre>
<h2 id="configure-the-tunnel">Configure the Tunnel</h2>
<p>You can now <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/#4-create-a-configuration-file">configure the tunnel</a> to serve traffic.</p>
<p>Create a <code>YAML</code> file that <code>cloudflared</code> can reach. By default, <code>cloudflared</code> will look for the file in the same folder where <code>cloudflared</code> has been installed.</p>
<pre tabindex="0"><code class="language-sh">vim ~/.cloudflared/config.yml&#10;</code></pre>
<p>Next, configure the Tunnel, replacing the example ID below with the ID of the Tunnel created above. Additionally, replace the hostname in this example with the hostname of the application configured with Cloudflare Access.</p>
<pre tabindex="0"><code class="language-yaml">tunnel: 6ff42ae2-765d-4adf-8112-31c55c1551ef&#10;credentials-file: /root/.cloudflared/6ff42ae2-765d-4adf-8112-31c55c1551ef.json&#10;&#10;ingress:&#10;  &#45; hostname: azure.widgetcorp.tech&#10;    service: tcp://kubernetes.docker.internal:6443&#10;    originRequest:&#10;      proxyType: socks&#10;  &#45; service: http_status:404&#10;  &#35; Catch-all rule, which responds with 404 if traffic doesn&#x27;t match any of&#10;  &#35; the earlier rules&#10;</code></pre>
<h2 id="route-to-the-tunnel">Route to the Tunnel</h2>
<p>You can now create a DNS record that will route traffic to this Tunnel. Multiple DNS records can point to a single Tunnel and will send traffic to the configured service as long as the hostname is defined with an <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/#file-structure-for-public-hostnames">ingress rule</a>.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to the <strong>DNS Records</strong> page for your domain.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Add record</strong>. Choose <code>CNAME</code> as the record type. For <strong>Name</strong>, choose the hostname where you want to create a Tunnel. This should match the hostname of the Access policy.</p>
</li>
<li>
<p>For <strong>Target</strong>, input the ID of your Tunnel followed by <code>.cfargotunnel.com</code>. For example:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">  6ff42ae2-765d-4adf-8112-31c55c1551ef.cfargotunnel.com&#10;</code></pre>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="run-the-tunnel">Run the Tunnel</h2>
<p>You can now run the Tunnel to connect the target service to Cloudflare. Use the following command to run the Tunnel, replacing <code>&lt;NAME&gt;</code> with the name created for your Tunnel.</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel run &lt;NAME&gt;&#10;</code></pre>
<p>We recommend that you run <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/">as a service</a> that is configured to launch on start.</p>
<h2 id="connect-from-a-client-machine">Connect from a client machine</h2>
<p>You can now connect from a client machine using <code>cloudflared</code>.</p>
<p>This example uses a macOS laptop. On macOS, you can install <code>cloudflared</code> with the following command using Homebrew.</p>
<pre tabindex="0"><code class="language-sh">brew install cloudflared&#10;</code></pre>
<p>Run the following command to create a connection from the device to Cloudflare. Any available port can be specified.</p>
<pre tabindex="0"><code class="language-sh">cloudflared access tcp --hostname azure.widgetcorp.tech --url 127.0.0.1:1234&#10;</code></pre>
<p>With this service running, you can run a <code>kubectl</code> command and <code>cloudflared</code> will launch a browser window and prompt the user to authenticate with your SSO provider. Once authenticated, <code>cloudflared</code> will expose the connection to the client machine at the local URL specified in the command.</p>
<p><code>kubeconfig</code> does not support proxy command configurations at this time, though the community has submitted plans to do so. In the interim, users can alias the cluster's API server to save time.</p>
<pre tabindex="0"><code class="language-sh">alias kubeone=&quot;env HTTPS_PROXY=socks5://127.0.0.1:1234 kubectl&quot;&#10;</code></pre>
