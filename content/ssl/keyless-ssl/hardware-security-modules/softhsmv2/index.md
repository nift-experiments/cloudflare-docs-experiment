---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/
  description: Learn how to use Keyless SSL with SoftHSMv2.
  full_title: SoftHSMv2 · Cloudflare SSL/TLS docs
  head_html: <title>SoftHSMv2 · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Keyless SSL with SoftHSMv2."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/index.md"><meta property="og:title" content="SoftHSMv2 · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Keyless SSL with SoftHSMv2."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/#page","headline":"SoftHSMv2 \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to use Keyless SSL with SoftHSMv2.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/hardware-security-modules/softhsmv2/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/14200.md")
</aside>
<hr />
<h2 id="1-install-and-configure-softhsmv2"><ol>
<li>Install and configure SoftHSMv2</li>
</ol></h2>
<p>First, we install SoftHSMv2 and configure it to store tokens in the default location <code>/var/lib/softhsm/tokens</code>. We also need to give the <code>softhsm</code> group permission to this directory as this is how the <code>keyless</code> user will access this directory.</p>
<pre tabindex="0"><code class="language-bash">sudo apt-get install -y softhsm2 opensc&#10;&#10;&#35;...&#10;&#10;cat &lt;&lt;EOF | sudo tee /etc/softhsm/softhsm2.conf&#10;directories.tokendir = /var/lib/softhsm/tokens&#10;objectstore.backend = file&#10;log.level = DEBUG&#10;slots.removable = false&#10;EOF&#10;&#10;sudo mkdir /var/lib/softhsm/tokens&#10;sudo chown root:softhsm $_&#10;sudo chmod 0770 /var/lib/softhsm/tokens&#10;sudo usermod -G softhsm keyless&#10;sudo usermod -G softhsm $(whoami)&#10;&#10;echo &#x27;export SOFTHSM2_CONF=/etc/softhsm/softhsm2.conf&#x27; | tee -a ~/.profile&#10;source ~/.profile&#10;</code></pre>
<hr />
<h2 id="2-create-a-token-and-private-keys-and-generate-csrs"><ol start="2">
<li>Create a token and private keys, and generate CSRs</li>
</ol></h2>
<p>Next, we create a token in slot 0 called <code>test-token</code> and secure it with a PIN of <code>1234</code>. In this slot we’ll store the RSA keys for our SSL certificates for <code>keyless-softhsm.example.com</code>.</p>
<pre tabindex="0"><code class="language-sh">sudo -u keyless softhsm2-util --init-token --slot 0 --label test-token --pin 1234 --so-pin 4321&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">The token has been initialized.&#10;</code></pre>
<p>Using cfssl, we generate the <a href="https://github.com/cloudflare/cfssl">private keys and Certificate Signing Requests (CSRs)</a>, the latter of which will be sent to a Certificate Authority (CA) for signing.</p>
<pre tabindex="0"><code class="language-bash">cat &lt;&lt;EOF | tee csr.json&#10;{&#10;    &quot;hosts&quot;: [&#10;        &quot;keyless-softhsm.example.com&quot;&#10;    ],&#10;    &quot;CN&quot;: &quot;keyless-softhsm.example.com&quot;,&#10;    &quot;key&quot;: {&#10;        &quot;algo&quot;: &quot;rsa&quot;,&#10;        &quot;size&quot;: 2048&#10;    },&#10;    &quot;names&quot;: [{&#10;        &quot;C&quot;: &quot;US&quot;,&#10;        &quot;L&quot;: &quot;San Francisco&quot;,&#10;        &quot;O&quot;: &quot;TLS Fun&quot;,&#10;        &quot;OU&quot;: &quot;Technical Operations&quot;,&#10;        &quot;ST&quot;: &quot;California&quot;&#10;    }]&#10;}&#10;EOF&#10;&#10;cfssl genkey csr.json | cfssljson -bare certificate&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">2018/08/12 00:52:22 [INFO] generate received request&#10;2018/08/12 00:52:22 [INFO] received CSR&#10;2018/08/12 00:52:22 [INFO] generating key: rsa-2048&#10;2018/08/12 00:52:22 [INFO] encoded CSR&#10;</code></pre>
<hr />
<h2 id="3-convert-and-import-the-key"><ol start="3">
<li>Convert and import the key</li>
</ol></h2>
<p>Now that the key has been generated, it’s time to load it into the slot we created. Before doing so, we need to convert from PKCS#1 to PKCS#8 format. During import, we specify the token and PIN from token initialization and provide a unique hexadecimal ID and label to the key.</p>
<pre tabindex="0"><code class="language-sh">openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in certificate-key.pem -out certificate-key.p8&#10;sudo chown keyless certificate-key.p8&#10;&#10;sudo -u keyless softhsm2-util --pin 1234 --import ./certificate-key.p8 --token test-token --id a000 --label rsa-privkey&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Found slot 915669571 with matching token label.&#10;The key pair has been imported.&#10;</code></pre>
<p>After importing we ask <code>pkcs11-tool</code> to confirm the objects have been successfully stored in the token.</p>
<pre tabindex="0"><code class="language-bash">sudo -u keyless pkcs11-tool --module /usr/lib/softhsm/libsofthsm2.so -l -p 1234 --token test-token --list-objects&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Public Key Object; RSA 2048 bits&#10;  label:      rsa-privkey&#10;  ID:         a000&#10;  Usage:      verify&#10;Private Key Object; RSA&#10;  label:      rsa-privkey&#10;  ID:         a000&#10;  Usage:      sign&#10;</code></pre>
<hr />
<h2 id="4-modify-your-gokeyless-config-file-and-restart-the-service"><ol start="4">
<li>Modify your gokeyless config file and restart the service</li>
</ol></h2>
<p>With the keys in place, it’s time to build the configuration file that the key server will read on startup. The <code>id</code> refers to the hexadecimal ID you provided to the <code>softhsm2-util</code> import statement; we used <code>a000</code> so it is encoded as <code>%a0%00</code>. The <code>module-path</code> will vary slightly based on the Linux distribution you are using. On Debian it should be <code>/usr/lib/softhsm/libsofthsm2.so</code>.</p>
<p>Open up <code>/etc/keyless/gokeyless.yaml</code> and immediately after</p>
<pre tabindex="0"><code class="language-yaml">private_key_stores:&#10;  &#45; dir: /etc/keyless/keys&#10;</code></pre>
<p>add</p>
<pre tabindex="0"><code class="language-yaml">&#45; uri: pkcs11:token=test-token;id=%a0%00?module-path=/usr/lib/softhsm/libsofthsm2.so&amp;pin-value=1234&amp;max-sessions=1&#10;</code></pre>
<p>Save the config file, restart <code>gokeyless</code>, and verify it started successfully.</p>
<pre tabindex="0"><code class="language-sh">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
