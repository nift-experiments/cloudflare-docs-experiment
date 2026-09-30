---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/configuration/public-dns/
  description: Deploy Keyless SSL with public DNS resolution.
  full_title: Public DNS setup - Keyless SSL · Cloudflare SSL/TLS docs
  head_html: <title>Public DNS setup - Keyless SSL · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Keyless SSL with public DNS resolution."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/configuration/public-dns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/configuration/public-dns/index.md"><meta property="og:title" content="Public DNS setup - Keyless SSL · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Keyless SSL with public DNS resolution."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/configuration/public-dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/configuration/public-dns/#page","headline":"Public DNS setup - Keyless SSL \u00b7 Cloudflare SSL/TLS docs","description":"Deploy Keyless SSL with public DNS resolution.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/configuration/public-dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/configuration/public-dns/
  schema: 1
---
<p>If you cannot use a <a href="/ssl/keyless-ssl/configuration/cloudflare-tunnel/">Cloudflare Tunnel setup</a>, you can also create a public DNS record for your key server.</p>
<p>This setup option is not ideal as the DNS record cannot be <a href="/dns/proxy-status/">proxied</a> and - as a result - will expose the origin IP address of your key server.</p>
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
<h2 id="1-create-public-dns-record"><ol>
<li>Create public DNS record</li>
</ol></h2>
<ol>
<li>Open a Terminal and run <code>openssl rand -hex 24</code> to generate a long, random hostname such as <code>11aa40b4a5db06d4889e48e2f738950ddfa50b7349d09b5f.example.com</code>.</li>
<li>Add this record via your DNS provider’s interface as an <strong>A</strong> or <strong>AAAA</strong> record pointing to the IP address of your Keyless SSL server.</li>
<li>Use this hostname as the server hostname during initialization of your Keyless SSL server.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14213.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14212.md")
</aside>
<hr />
<h2 id="certificates-used-in-keyless-ssl">Certificates used in Keyless SSL</h2>
<p>Keyless SSL involves <strong>two different certificates</strong>. Confusing them is the most common setup error.</p>
<table>
<thead>
<tr>
<th>Certificate</th>
<th>What it is</th>
<th>SAN should contain</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Edge (Keyless SSL) certificate</strong></td>
<td>The public certificate Cloudflare serves for your site.</td>
<td>Your site hostnames only (for example, <code>www.example.com</code>)</td>
</tr>
<tr>
<td><strong>Key server authentication certificate</strong></td>
<td>The certificate your key server uses to prove itself to Cloudflare.</td>
<td>The key server hostname only</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14211.md")
</aside>
<hr />
<h2 id="2-upload-keyless-ssl-certificates"><ol start="2">
<li>Upload Keyless SSL Certificates</li>
</ol></h2>
<p>Before your key servers can be configured, you must next upload the corresponding SSL certificates to Cloudflare’s edge. During TLS termination, Cloudflare will present these certificates to connecting browsers and then (for non-resumed sessions) communicate with the specified key server to complete the handshake.</p>
<p>Upload certificates to Cloudflare with only SANs that you wish to use with Cloudflare Keyless SSL. All Keyless SSL hostnames must be <a href="/dns/proxy-status/">proxied</a>.</p>
<p>You will have to upload each certificate used with Keyless SSL.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14216.md")
</div></div>
<hr />
<h2 id="3-set-up-and-activate-key-server"><ol start="3">
<li>Set up and activate key server</li>
</ol></h2>
<p>Finally, you need to install the key server on your infrastructure, populate it with the SSL keys of the certificates you wish to use to terminate TLS at Cloudflare’s edge, and activate the key server so it can be mutually authenticated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14210.md")
</aside>
<h3 id="install">Install</h3>
<p>These steps are also at the <a href="https://pkg.cloudflare.com/">Cloudflare package repository</a>.</p>
<h4 id="debian-ubuntu-packages">Debian/Ubuntu packages</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14223.md")
</div></div>
<h4 id="rhel-centos-amazon-linux-packages">RHEL/CentOS/Amazon Linux packages</h4>
<p>Gokeyless uses CGO for PKCS#11/HSM support, which creates glibc dependencies. Use the repository that matches your distribution.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14228.md")
</div></div>
<h3 id="configure">Configure</h3>
<p>Add your Cloudflare account details to the configuration file located at <code>/etc/keyless/gokeyless.yaml</code>:</p>
<ol>
<li>
<p>Set the hostname of the key server, for example, <code>11aa40b4a5db06d4889e48e2f.example.com</code>. This is also the value you entered when you uploaded your keyless certificate and is the hostname of your key server that holds the key for this certificate.</p>
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
@markup("md", "content/.markup/bodies/14209.md")
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
@markup("md", "content/.markup/bodies/14208.md")
</aside>
<p>If this command fails, try troubleshooting by <a href="/ssl/keyless-ssl/troubleshooting/">checking the logs</a>.</p>
<h3 id="allow-incoming-connections-from-cloudflare">Allow incoming connections from Cloudflare</h3>
<p>During TLS handshakes, Cloudflare's keyless client will initiate connections to the key server hostname or IP address you specify during certificate upload. By default, the keyless client will use a destination TCP port of 2407, but this can be changed during certificate upload or by editing the certificate details after upload.</p>
<p>Create WAF custom rules that allow your key server to accept connections from only Cloudflare. You can get Cloudflare's IPv4 and IPv6 addresses via the <a href="/api/resources/ips/methods/list/">IP details API endpoint</a>.</p>
