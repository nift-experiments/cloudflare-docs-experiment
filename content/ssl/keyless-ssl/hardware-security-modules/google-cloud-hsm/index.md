---
cp9:
  canonical: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/
  description: Learn how to use Keyless SSL with Google Cloud HSM.
  full_title: Google Cloud HSM · Cloudflare SSL/TLS docs
  head_html: <title>Google Cloud HSM · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Keyless SSL with Google Cloud HSM."><link rel="canonical" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/index.md"><meta property="og:title" content="Google Cloud HSM · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Keyless SSL with Google Cloud HSM."><meta property="og:url" content="https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="GCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/#page","headline":"Google Cloud HSM \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to use Keyless SSL with Google Cloud HSM.","url":"https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GCP"]}</script>
  markdown: true
  noindex: false
  route: /ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/
  schema: 1
---
<p>This tutorial uses <a href="https://cloud.google.com/kms/docs/hsm">Google Cloud HSM</a> — a FIPS 140-2 Level 3 certified implementation.</p>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>Make sure that you have:</p>
<ul>
<li>Set up your <a href="https://cloud.google.com/kms/docs/quickstart#before-you-begin">Google Cloud project</a></li>
</ul>
<hr />
<h2 id="1-create-a-key-ring"><ol>
<li>Create a key ring</li>
</ol></h2>
<p>To set up the Google Cloud HSM, <a href="https://cloud.google.com/kms/docs/hsm#kms-create-key-hsm-web">create a key ring</a> and indicate its location.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/14202.md")
</aside>
<hr />
<h2 id="2-create-a-key"><ol start="2">
<li>Create a key</li>
</ol></h2>
<p>Create a key, including the following information:</p>
<table>
<thead>
<tr>
<th width="25%">Field</th>
<th width="25%">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key ring</td>
<td>
				The key ring you created in <b>Step 2</b>
</td>
</tr>
<tr>
<td>Protection level</td>
<td>HSM</td>
</tr>
<tr>
<td>Purpose</td>
<td>Asymmetric Encrypt</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="3-import-the-private-key"><ol start="3">
<li>Import the private key</li>
</ol></h2>
<p>After creating a key ring and key, <a href="https://cloud.google.com/kms/docs/importing-a-key">import the private key</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note:</h3>
@markup("md", "content/.markup/bodies/14201.md")
</aside>
<hr />
<h2 id="4-modify-your-gokeyless-config-file-and-restart-the-service"><ol start="4">
<li>Modify your gokeyless config file and restart the service</li>
</ol></h2>
<p>Once you’ve imported the key, copy the <strong>Resource name</strong> from the UI. Then, add this value to the <code>gokeyless</code> YAML file under <code>private_key_stores</code>.</p>
<p>With the config file saved, restart <code>gokeyless</code> and verify it started successfully.</p>
<pre tabindex="0"><code class="language-sh">sudo systemctl restart gokeyless.service&#10;sudo systemctl status gokeyless.service -l&#10;</code></pre>
