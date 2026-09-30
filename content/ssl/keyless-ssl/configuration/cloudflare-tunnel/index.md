---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/configuration/cloudflare-tunnel/
  description: Deploy Keyless SSL with Cloudflare Tunnel for private connectivity.
  full_title: Cloudflare Tunnel setup - Keyless SSL · Cloudflare SSL/TLS docs
  head_html: <title>Cloudflare Tunnel setup - Keyless SSL · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Keyless SSL with Cloudflare Tunnel for private connectivity."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/configuration/cloudflare-tunnel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/configuration/cloudflare-tunnel/index.md"><meta property="og:title" content="Cloudflare Tunnel setup - Keyless SSL · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Keyless SSL with Cloudflare Tunnel for private connectivity."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/configuration/cloudflare-tunnel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="Integration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/configuration/cloudflare-tunnel/#page","headline":"Cloudflare Tunnel setup - Keyless SSL \u00b7 Cloudflare SSL/TLS docs","description":"Deploy Keyless SSL with Cloudflare Tunnel for private connectivity.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/configuration/cloudflare-tunnel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Integration"]}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/configuration/cloudflare-tunnel/
  schema: 1
---
<p>Through an integration with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>, you can send traffic to a key server through a secure channel and avoid exposing your key server to the public Internet.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<h3 id="supported-platforms">Supported platforms</h3>
<p>Keyless has been tested on <code>amd64</code> and <code>arm</code> architectures. The key server binary will likely run on all architectures that Go supports. Code support may exist for other CPUs too, but these other architectures have not been tested.</p>
<p>In addition to running on bare metal, the key server should run without issue in a virtualized or containerized environment. Care will need to be taken to configure ingress access to the appropriate TCP port and file system access to private keys (if using filesystem storage).</p>
<h3 id="supported-operating-systems">Supported operating systems</h3>
<p>You will need to have a supported operating system (OS) to run Keyless. Supported operating systems include:</p>
<ul>
<li>Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), 24.04 LTS (Noble)</li>
<li>Debian 11 (Bullseye), 12 (Bookworm), 13 (Trixie)</li>
<li>RHEL 8, 9, CentOS 8, and CentOS Stream 9</li>
<li>Amazon Linux 2, 2023</li>
</ul>
<p>We strongly recommend that you use an operating system still supported by the vendor (still receiving security updates) as your key server will have access to your private keys.</p>
<hr />
<h2 id="1-install-cloudflared-on-key-server"><ol>
<li>Install <code>cloudflared</code> on key server</li>
</ol></h2>
<p>First, install <code>cloudflared</code> on your key server.</p>
<p>This process differs depending on whether you are using the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">command line</a> or the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Cloudflare dashboard</a>.</p>
<h2 id="2-create-a-tunnel-and-add-a-route"><ol start="2">
<li>Create a tunnel and add a route</li>
</ol></h2>
<p>Then, create a Cloudflare Tunnel.</p>
<p>This process differs depending on whether you are using the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/create-local-tunnel/">command line</a> or the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Cloudflare dashboard</a>.</p>
<p>During tunnel creation, go to the <strong>CIDR</strong> tab and enter the private IP address of your key server. You can also <a href="/cloudflare-one/networks/routes/add-routes/#add-a-cidr-route">add a CIDR route</a> after creating the tunnel.</p>
<p>After you create the tunnel, use the Cloudflare API to <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/">List tunnel routes</a>, saving the following values for a future step:</p>
<ul>
<li><code>&quot;virtual_network_id&quot;</code></li>
<li><code>&quot;network&quot;</code></li>
</ul>
<h2 id="3-upload-keyless-ssl-certificates"><ol start="3">
<li>Upload Keyless SSL Certificates</li>
</ol></h2>
<p>Before your key servers can be configured, you must next upload the corresponding SSL certificates to Cloudflare’s edge. During TLS termination, Cloudflare will present these certificates to connecting browsers and then (for non-resumed sessions) communicate with the specified key server to complete the handshake.</p>
<p>Upload certificates to Cloudflare with only SANs that you wish to use with Cloudflare Keyless SSL. All Keyless SSL hostnames must be <a href="/dns/proxy-status/">proxied</a>.</p>
<p>You will have to upload each certificate used with Keyless SSL.</p>
<p>To upload a Keyless certificate with the API, send a <a href="/api/resources/keyless_certificates/methods/create/"><code>POST</code></a> request that includes a <code>&quot;tunnel&quot;</code> object.</p>
<pre tabindex="0"><code class="language-json">&quot;tunnel&quot;: {&#10;  &quot;vnet_id&quot;: &quot;&lt;VIRTUAL_NETWORK_ID&gt;&quot;,&#10;  &quot;private_ip&quot;: &quot;&lt;NETWORK&gt;&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14232.md")
</aside>
<h2 id="4-set-up-and-activate-key-server"><ol start="4">
<li>Set up and activate key server</li>
</ol></h2>
<p>Finally, you need to install the key server on your infrastructure, populate it with the SSL keys of the certificates you wish to use to terminate TLS at Cloudflare’s edge, and activate the key server so it can be mutually authenticated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14231.md")
</aside>
<h3 id="install">Install</h3>
<p>These steps are also at the <a href="https://pkg.cloudflare.com/">Cloudflare package repository</a>.</p>
<h4 id="debian-ubuntu-packages">Debian/Ubuntu packages</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14239.md")
</div></div>
<h4 id="rhel-centos-amazon-linux-packages">RHEL/CentOS/Amazon Linux packages</h4>
<p>Gokeyless uses CGO for PKCS#11/HSM support, which creates glibc dependencies. Use the repository that matches your distribution.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14244.md")
</div></div>
<h3 id="configure">Configure</h3>
<p>Add your Cloudflare account details to the configuration file located at <code>/etc/keyless/gokeyless.yaml</code>:</p>
<ol>
<li>
<p>Set the hostname of the key server, for example, <code>keyserver.keyless.example.com</code>. This is also the value you entered when you uploaded your keyless certificate and is the hostname of your key server that holds the key for this certificate.</p>
</li>
<li>
<p>Set the Zone ID (found on <strong>Overview</strong> tab of the Cloudflare dashboard).</p>
</li>
<li>
<p>Set the authentication credential for server certificate enrollment. gokeyless supports two options:</p>
<ul>
<li><strong>API Token (recommended):</strong> <a href="/fundamentals/api/get-started/create-token/">Create an API Token</a> with the <strong>Zone &gt; SSL and Certificates &gt; Edit</strong> permission. Set it in your configuration:</li>
</ul>
</li>
</ol>
<pre tabindex="0"><code class="language-yaml">api_token: &quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code> Or use the environment variable `KEYLESS_API_TOKEN`.&#10;</code></pre>
<ul>
<li><strong>Origin CA API key (deprecated):</strong> <a href="/fundamentals/api/get-started/ca-keys/">Set the Origin CA API key</a>. This option will stop working on September 30, 2026.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="origin-ca-service-keys-are-removed-september-30-2026">Origin CA Service Keys are removed September 30, 2026</h3>
@markup("md", "content/.markup/bodies/14230.md")
</aside>
<h3 id="populate-keys">Populate keys</h3>
<p>Install your private keys in <code>/etc/keyless/keys/</code> and set the user and group to keyless with 400 permissions. Keys must be in PEM or DER format and have an extension of <code>.key</code>:</p>
<pre tabindex="0"><code class="language-sh">ls -l /etc/keyless/keys&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#45;r-------- 1 keyless keyless 1675 Nov 18 16:44 example.com.key&#10;</code></pre>
<p>When running multiple key servers, make sure all required keys are distributed to each key server. Customers typically will either use a configuration management tool such as Salt or Puppet to distribute keys or mount <code>/etc/keyless/keys</code> to a network location accessible only by your key servers. Keys are read on boot into memory, so a network path must be accessible during the gokeyless process start/restart.</p>
<h3 id="activate">Activate</h3>
<p>To activate, restart your keyless instance:</p>
<ul>
<li>systemd: <code>sudo service gokeyless restart</code></li>
<li>upstart/sysvinit: <code>sudo /etc/init.d/gokeyless restart</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14229.md")
</aside>
<p>If this command fails, try troubleshooting by <a href="/ssl/keyless-ssl/troubleshooting/">checking the logs</a>.</p>
