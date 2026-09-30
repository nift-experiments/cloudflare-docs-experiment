---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/
  description: Automatically deploy a root certificate on desktop devices.
  full_title: Install certificate using the Cloudflare One Client · Cloudflare One docs
  head_html: <title>Install certificate using the Cloudflare One Client · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Automatically deploy a root certificate on desktop devices."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/index.md"><meta property="og:title" content="Install certificate using the Cloudflare One Client · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Automatically deploy a root certificate on desktop devices."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/#page","headline":"Install certificate using the Cloudflare One Client \u00b7 Cloudflare One docs","description":"Automatically deploy a root certificate on desktop devices.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6049.md")
</div></details>
<p>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> can automatically install a Cloudflare certificate or <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">custom root certificate</a> on Windows, macOS, and Debian/Ubuntu Linux devices. On mobile devices and Red Hat-based systems, you will need to <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/">install the certificate manually</a>.</p>
<p>The certificate is required if you want to <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">apply HTTP policies to encrypted websites</a>, display custom <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">block pages</a>, and more.</p>
<h2 id="install-a-certificate-using-the-cloudflare-one-client">Install a certificate using the Cloudflare One Client</h2>
<p>To configure the Cloudflare One Client to install a root certificate on your organization's devices:</p>
<ol>
<li>(Optional) <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">Upload</a> a custom root certificate to Cloudflare.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Management</strong>.</li>
<li>Under <strong>Global Cloudflare One Client settings</strong>, turn on <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#install-ca-to-system-certificate-store"><strong>Install CA to system certificate store</strong></a>.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Install</a> the Cloudflare One Client on the device.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Enroll the device</a> in your Zero Trust organization.</li>
<li>(Optional) If the device is running macOS Big Sur or newer, <a href="#manually-trust-the-certificate">manually trust the certificate</a>.</li>
</ol>
<p>The Cloudflare One Client will now download any <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#activate-a-root-certificate">certificates set to <strong>Available</strong></a>. After download, the Cloudflare One Client will add the certificates to the device's system certificate store in <code>installed_certs/&lt;certificate_id&gt;.pem</code> and append the contents to the <code>installed_cert.pem</code> file. If you have any scripts using <code>installed_cert.pem</code>, Cloudflare recommends you set them to use the individual files in the <code>installed_certs/</code> directory instead. <code>installed_certs.pem</code> will be deprecated by 2025-06-31.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6048.md")
</aside>
<p>The Cloudflare One Client does not install certificates to individual applications. You will need to <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/#add-the-certificate-to-applications">manually add certificates</a> to applications that rely on their own certificate store instead of the system certificate store.</p>
<h2 id="access-the-installed-certificate">Access the installed certificate</h2>
<p>After installing the certificate using the Cloudflare One Client, you can verify successful installation by accessing the device's system certificate store.</p>
<h3 id="macos">macOS</h3>
<p>To access the installed certificate in macOS:</p>
<ol>
<li>Open Keychain Access.</li>
<li>In <strong>System Keychains</strong>, go to <strong>System</strong> &gt; <strong>Certificates</strong>.</li>
<li>Open your certificate. The default Cloudflare certificate name is <strong>Gateway CA - Cloudflare Managed G1</strong>.</li>
<li>If the certificate is trusted by all users, Keychain Access will display <strong>This certificate is marked as trusted for all users</strong>.</li>
</ol>
<p>The Cloudflare One Client will also place the certificate in <code>/Library/Application Support/Cloudflare/installed_cert.pem</code> for reference by scripts or tools.</p>
<h4 id="manually-trust-the-certificate">Manually trust the certificate</h4>
<p>macOS Big Sur and newer do not allow the Cloudflare One Client to automatically trust the certificate. To manually trust the certificate:</p>
<ol>
<li>In Keychain Access, <a href="#macos">find and open the certificate</a>.</li>
<li>Open <strong>Trust</strong>.</li>
<li>Set <strong>When using this certificate</strong> to <em>Always Trust</em>.</li>
<li>(Optional) Restart the device to reset connections to Zero Trust.</li>
</ol>
<p>Alternatively, you can configure your mobile device management (MDM) to automatically trust the certificate on all of your organization's devices.</p>
<h3 id="windows">Windows</h3>
<p>To access the installed certificate in Windows:</p>
<ol>
<li>Open the Start menu and select <strong>Run</strong>.</li>
<li>Enter <code>certlm.msc</code>.</li>
<li>Go to <strong>Trusted Root Certification Authority</strong> &gt; <strong>Certificates</strong>. The default Cloudflare certificate name is <strong>Gateway CA - Cloudflare Managed G1</strong>.</li>
</ol>
<p>The Cloudflare One Client will also place the certificate in <code>%PROGRAMDATA%\Cloudflare\installed_cert.pem</code> for reference by scripts or tools.</p>
<h3 id="debian-based-linux-distributions">Debian-based Linux distributions</h3>
<p>On Debian-based Linux distributions, the certificate is stored in <code>/usr/local/share/ca-certificates</code>. The default installed Cloudflare certificate name is <code>managed-warp.pem</code>. The Cloudflare One Client will create a symbolic link named <code>managed-warp.crt</code> to use as its root certificate. If your system is not using <code>managed-warp.crt</code>, run the following commands to update the system store:</p>
<ol>
<li>Update your list of custom CA certificates.</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo update-ca-certificates&#10;</code></pre>
<ol start="2">
<li>Go to the system certificate store.</li>
</ol>
<pre tabindex="0"><code class="language-sh">cd /usr/local/share/ca-certificates&#10;</code></pre>
<ol start="3">
<li>Verify your system has both the <code>managed-warp.pem</code> file and the <code>managed-warp.crt</code> symbolic link. For example:</li>
</ol>
<pre tabindex="0"><code class="language-sh">ls -l&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">lrwxrwxrwx 1 root root   49 Jan  3 21:46 managed-warp.crt -&gt; /usr/local/share/ca-certificates/managed-warp.pem&#10;&#45;rw-r--r-- 1 root root 1139 Jan  3 21:46 managed-warp.pem&#10;</code></pre>
<p>The Cloudflare One Client will also place the certificate in <code>/var/lib/cloudflare-warp/installed_cert.pem</code> for reference by scripts or tools.</p>
<h2 id="uninstall-the-certificate">Uninstall the certificate</h2>
<p>If the certificate was installed by the Cloudflare One Client, it is automatically removed when you turn on another certificate for inspection in Cloudflare One, turn off <strong>Install CA to system certificate store</strong>, or <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/uninstall/">uninstall the Cloudflare One Client</a>. The Cloudflare One Client does not remove certificates that were installed manually (for example, certificates added to third-party applications).</p>
<p>To manually remove the certificate, refer to the instructions supplied by your operating system or the third-party application.</p>
