---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/
  description: Learn how to use Keyless SSL with IBM Cloud HSM.
  full_title: IBM Cloud HSM · Cloudflare SSL/TLS docs
  head_html: <title>IBM Cloud HSM · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Keyless SSL with IBM Cloud HSM."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/index.md"><meta property="og:title" content="IBM Cloud HSM · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Keyless SSL with IBM Cloud HSM."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/#page","headline":"IBM Cloud HSM \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to use Keyless SSL with IBM Cloud HSM.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/
  schema: 1
---
<p>The example below was tested using <a href="https://console.bluemix.net/docs/infrastructure/hardware-security-modules/about.html#about-ibm-cloud-hsm">IBM Cloud HSM 7.0</a>, a FIPS 140-2 Level 3 certified implementation based on the Gemalto SafeNet Luna a750.</p>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>Make sure that you have:</p>
<ul>
<li>Initialized <a href="https://console.bluemix.net/docs/infrastructure/hardware-security-modules/initialize_hsm.html#initializing-the-ibm-cloud-hsm">your device</a></li>
<li>Installed the <a href="https://cpl.thalesgroup.com/node/11350">SafeNet client software</a></li>
</ul>
<hr />
<h2 id="1-create-assign-and-initialize-a-new-partition"><ol>
<li>Create, assign, and initialize a new partition</li>
</ol></h2>
<p>The first step is creating an HSM partition, which can be thought of as an independent logical HSM within your IBM Cloud HSM device.</p>
<pre tabindex="0"><code class="language-txt">vm$ ssh admin@hsm&#10;&#10;[cloudflare-hsm.softlayer.com] lunash:&gt;partition create -partition KeylessSSL&#10;&#10;&#10;          Type &#x27;proceed&#x27; to create the partition, or&#10;          &#x27;quit&#x27; to quit now.&#10;          &gt; proceed&#10;&#x27;partition create&#x27; successful.&#10;&#10;&#10;Command Result : 0 (Success)&#10;</code></pre>
<p>Next, the partition needs to be assigned to the client, in this case your key server.</p>
<pre tabindex="0"><code class="language-bash">[cloudflare-hsm.softlayer.com] lunash:&gt;client assignpartition -client cloudflare-vm.softlayer.com -partition KeylessSSL&#10;&#10;&#10;&#x27;client assignPartition&#x27; successful.&#10;&#10;&#10;Command Result : 0 (Success)&#10;</code></pre>
<p>After the partition has been assigned, run <code>lunacm</code> from your virtual server and initialize the partition.</p>
<pre tabindex="0"><code class="language-txt">vm$ lunacm&#10;LunaCM v7.1.0-379. Copyright (c) 2006-2017 SafeNet.&#10;&#10;    Available HSMs:&#10;&#10;    Slot Id -&gt;              0&#10;    Label -&gt;&#10;    Serial Number -&gt;        XXXXXXXXXXXXX&#10;    Model -&gt;                LunaSA 7.0.0&#10;    Firmware Version -&gt;     7.0.1&#10;    Configuration -&gt;        Luna User Partition With SO (PW) Signing With Cloning Mode&#10;    Slot Description -&gt;     Net Token Slot&#10;&#10;&#10;    Current Slot Id: 0&#10;&#10;lunacm:&gt;partition init -label KeylessSSL -domain cloudflare&#10;&#10;  Enter password for Partition SO: ********&#10;&#10;  Re-enter password for Partition SO: ********&#10;&#10;  You are about to initialize the partition.&#10;  All contents of the partition will be destroyed.&#10;&#10;  Are you sure you wish to continue?&#10;&#10;  Type &#x27;proceed&#x27; to continue, or &#x27;quit&#x27; to quit now -&gt;proceed&#10;&#10;Command Result : No Error&#10;</code></pre>
<hr />
<h2 id="2-generate-rsa-and-ecdsa-key-pairs-and-certificate-signing-requests-csrs"><ol start="2">
<li>Generate RSA and ECDSA key pairs and certificate signing requests (CSRs)</li>
</ol></h2>
<p>Before running the commands below, check with your information security and/or cryptography team to confirm the approved key creation procedures for your organization.</p>
<p>When you perform this operation, you need define the ID field for the newly generated keys. It must be set to a big-endian hexadecimal integer value.</p>
<pre tabindex="0"><code class="language-txt">vm$ cmu generatekeypair -keyType=RSA -modulusBits=2048 -publicExponent=65537 -sign=1 -verify=1 -labelpublic=myrsakey -labelprivate=myrsakey -keygenmech=1  -id=a000&#10;Please enter password for token in slot 0 : ********&#10;&#10;&#35; cmu generatekeypair -keyType=ECDSA -curvetype=3 -sign=1 -verify=1 -labelpublic=myecdsakey -labelprivate=myecdsakey -id=a001&#10;Please enter password for token in slot 0 : ********&#10;&#10;&#35; cmu list&#10;Please enter password for token in slot 0 : ********&#10;handle=61   label=myecdsakey&#10;handle=60   label=myecdsakey&#10;handle=48   label=myrsakey&#10;handle=45   label=myrsakey&#10;</code></pre>
<p>Using the keys created in the previous step, generate CSRs that can be sent to a publicly trusted Certificate Authority (CA) for signing.</p>
<pre tabindex="0"><code class="language-txt">&#35; cmu requestCertificate -c=&quot;US&quot; -o=&quot;Example, Inc.&quot; -cn=&quot;ibm-cloudhsm.example.com&quot; -s=&quot;California&quot; -l=&quot;San Francisco&quot; -publichandle=45 -privatehandle=48 -outputfile=&quot;rsa.csr&quot; -sha256withrsa&#10;Please enter password for token in slot 0 : ********&#10;Using &quot;CKM_SHA256_RSA_PKCS&quot; Mechanism&#10;&#10;&#35; cmu requestCertificate -c=&quot;US&quot; -o=&quot;Example, Inc.&quot; -cn=&quot;ibm-cloudhsm.example.com&quot; -s=&quot;California&quot; -l=&quot;San Francisco&quot; -publichandle=60 -privatehandle=61 -outputfile=&quot;ecdsa.csr&quot; -sha256withecdsa&#10;Please enter password for token in slot 0 : ********&#10;Using &quot;CKM_ECDSA_SHA256&quot; Mechanism&#10;</code></pre>
<hr />
<h2 id="3-obtain-and-upload-signed-certificates-from-your-certificate-authority-ca"><ol start="3">
<li>Obtain and upload signed certificates from your Certificate Authority (CA)</li>
</ol></h2>
<p>Provide the CSRs created in the previous step to your organization's preferred CA, demonstrate control of your domain as requested, and then download the signed SSL certificates. Follow the instructions provided in <a href="/ssl/keyless-ssl/configuration/cloudflare-tunnel/#3-upload-keyless-ssl-certificates">Upload Keyless SSL Certificates</a>.</p>
<hr />
<h2 id="4-modify-your-gokeyless-config-file-and-restart-the-service"><ol start="4">
<li>Modify your gokeyless config file and restart the service</li>
</ol></h2>
<p>Lastly, we need to modify the configuration file that the key server will read on startup. Change the <code>object=mykey</code> and <code>pin-value=username:password</code> values to match the key label you provided and CU user you created.</p>
<p>Open <code>/etc/keyless/gokeyless.yaml</code> and immediately after:</p>
<pre tabindex="0"><code class="language-yaml">private_key_stores:&#10;  &#45; dir: /etc/keyless/keys&#10;</code></pre>
<p>add:</p>
<pre tabindex="0"><code class="language-yaml">&#45; uri: pkcs11:token=KeylessSSL;object=myrsakeyid=a000??module-path=/usr/safenet/lunaclient/lib/libCryptoki2_64.so&amp;pin-value=password&amp;max-sessions=1&#10;&#45; uri: pkcs11:token=KeylessSSL;object=myecdsakeyid=a001??module-path=/usr/safenet/lunaclient/lib/libCryptoki2_64.so&amp;pin-value=password&amp;max-sessions=1&#10;</code></pre>
<p>With the config file saved, restart <code>gokeyless</code> and verify it started successfully.</p>
<pre tabindex="0"><code class="language-sh">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
