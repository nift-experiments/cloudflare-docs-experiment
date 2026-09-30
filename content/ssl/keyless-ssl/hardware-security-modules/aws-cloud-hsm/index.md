---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/
  description: Learn how to use Keyless SSL with AWS CloudHSM.
  full_title: AWS cloud HSM · Cloudflare SSL/TLS docs
  head_html: <title>AWS cloud HSM · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Keyless SSL with AWS CloudHSM."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/index.md"><meta property="og:title" content="AWS cloud HSM · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Keyless SSL with AWS CloudHSM."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="AWS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/#page","headline":"AWS cloud HSM \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to use Keyless SSL with AWS CloudHSM.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AWS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/14206.md")
</aside>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>Make sure you have:</p>
<ul>
<li>Provisioned an <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html">AWS CloudHSM cluster</a> .</li>
<li>Installed the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-install.html">appropriate software library for PKCS#11</a>.</li>
</ul>
<hr />
<h2 id="1-import-the-public-and-private-key-to-the-hsm"><ol>
<li>Import the public and private key to the HSM</li>
</ol></h2>
<p>Before importing the public key, extract it from the certificate provided by your CA. Place the contents of your private key in <code>privkey.pem</code> and then run the following (replacing certificate.pem with your actual certificate) to populate <code>pubkey.pm</code>.</p>
<pre tabindex="0"><code class="language-txt">keyserver$ openssl x509 -pubkey -noout -in certificate.pem &gt; pubkey.pem&#10;</code></pre>
<p>Log in to the CloudHSM using a previously created <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-users.html#crypto-user">crypto user</a> (CU) account and generate a key encryption key that will be used to import your private key.</p>
<pre tabindex="0"><code class="language-txt">keyserver$ /opt/cloudhsm/bin/key_mgmt_util&#10;Command: loginHSM -u CU -s patrick -p donahue&#10;Command: genSymKey -t 31 -s 16 -sess -l import-wrapping-key&#10;...&#10;Symmetric Key Created.  Key Handle: 658&#10;...&#10;</code></pre>
<p>Referencing the key handle returned above, import the private and public key and then log out of the HSM:</p>
<pre tabindex="0"><code class="language-txt">Command: importPrivateKey -f privkey.pem -l mykey -id 1 -w 658&#10;...&#10;Cfm3WrapHostKey returned: 0x00 : HSM Return: SUCCESS&#10;Cfm3CreateUnwrapTemplate returned: 0x00 : HSM Return: SUCCESS&#10;Cfm3UnWrapKey returned: 0x00 : HSM Return: SUCCESS&#10;...&#10;Private Key Unwrapped.  Key Handle: 658&#10;&#10;&#10;Command: importPubKey -f pubkey.pem -l mykey -id 1&#10;Cfm3CreatePublicKey returned: 0x00 : HSM Return: SUCCESS&#10;...&#10;Public Key Handle: 941&#10;&#10;&#10;Command: logoutHSM&#10;Command: exit&#10;</code></pre>
<hr />
<h2 id="2-modify-the-gokeyless-config-file-and-restart-the-service"><ol start="2">
<li>Modify the gokeyless config file and restart the service</li>
</ol></h2>
<p>Now that the keys are in place, we need to modify the configuration file that the key server will read on startup. Change the <code>object=mykey</code> and <code>pin-value=username:password</code> values to match the key label you provided and CU user you created.</p>
<p>Open <code>/etc/keyless/gokeyless.yaml</code> and immediately after:</p>
<pre tabindex="0"><code class="language-yaml">private_key_stores:&#10;  &#45; dir: /etc/keyless/keys&#10;</code></pre>
<p>add:</p>
<pre tabindex="0"><code class="language-yaml">&#45; uri: pkcs11:token=cavium;object=mykey?module-path=/opt/cloudhsm/lib/libcloudhsm_pkcs11_standard.so&amp;pin-value=patrick:donahue&amp;max-sessions=1&#10;</code></pre>
<p>With the config file saved, restart <code>gokeyless</code> and verify it started successfully.</p>
<pre tabindex="0"><code class="language-sh">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
