---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/
  description: Client certificate in Zero Trust.
  full_title: Client certificate · Cloudflare One docs
  head_html: <title>Client certificate · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Client certificate in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/index.md"><meta property="og:title" content="Client certificate · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Client certificate in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture,mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/#page","headline":"Client certificate \u00b7 Cloudflare One docs","description":"Client certificate in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture","mTLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/
  schema: 1
---
<p>The Client Certificate device posture attribute checks if the device has a valid client certificate signed by a trusted certificate. The trusted certificate is uploaded to Cloudflare and specified as part of the posture check rule. The client certificate posture check can be used in Gateway and Access policies to ensure that the user is connecting from a managed device.</p>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5923.md")
</div></details>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A CA that issues client certificates for your devices. The Cloudflare One Client does not evaluate the certificate trust chain; this needs to be the issuing certificate.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="upload-the-signing-certificate-that-issued-the-client-certificate">Upload the signing certificate that issued the client certificate</h3>
@markup("md", "content/.markup/bodies/5922.md")
</aside>
<ul>
<li>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device.</li>
<li>A client certificate is <a href="#configure-the-client-certificate-check">installed and trusted</a> on the device.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5921.md")
</aside>
<h2 id="configure-the-client-certificate-check">Configure the client certificate check</h2>
<ol>
<li></li>
</ol>
<p>Use the <a href="/api/resources/mtls_certificates/methods/create/">Upload mTLS certificate endpoint</a> to upload the certificate and private key to Cloudflare. The certificate must be a signing certificate, formatted as a single string with <code>\n</code> replacing the line breaks. The private key is only required if you are using this custom certificate for Gateway HTTPS inspection.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/mtls_certificates \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;example_ca_cert&quot;,&#10;  &quot;certificates&quot;: &quot;-----BEGIN CERTIFICATE-----\nXXXXX\n-----END CERTIFICATE-----&quot;,&#10;  &quot;private_key&quot;: &quot;-----BEGIN PRIVATE KEY-----\nXXXXX\n-----END PRIVATE KEY-----&quot;,&#10;  &quot;ca&quot;: true&#10;}&#x27;</code></pre>
<p>The response will return a UUID for the certificate. For example:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;2458ce5a-0c35-4c7f-82c7-8e9487d3ff60&quot;,&#10;    &quot;name&quot;: &quot;example_ca_cert&quot;,&#10;    &quot;issuer&quot;: &quot;O=Example Inc.,L=California,ST=San Francisco,C=US&quot;,&#10;    &quot;signature&quot;: &quot;SHA256WithRSA&quot;,&#10;    ...&#10;  }&#10;}&#10;</code></pre>
<ol start="2">
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>Client certificate</strong>.</p>
</li>
<li>
<p>You will be prompted for the following information:</p>
<ol>
<li><strong>Name</strong>: Enter a unique name for this device posture check.</li>
<li><strong>Operating system</strong>: Select your operating system.</li>
<li><strong>OS locations</strong>: Specify the location(s) where the client certificate is installed.
<details class="nb-details"><summary>Windows</summary><div class="nb-details-body">
</li>
</ol>
</li>
</ol>
@markup("md", "content/.markup/bodies/5924.md")
</div></details>
      <details class="nb-details"><summary>macOS</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5925.md")
</div></details>
      <details class="nb-details"><summary>Linux</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5926.md")
</div></details>
   4. **Certificate ID**: Enter the UUID of the signing certificate.
   5. **Common name**: (Optional) To check for a Common Name (CN) on the client certificate, enter a string with optional `${serial_number}` and `${hostname}` variables (for example, `${serial_number}_mycompany`). The Cloudflare One Client will search for an exact, case-insensitive match. If you do not specify a common name, the Cloudflare One Client will ignore the common name field on the certificate.
   6. **Check for Extended Key Usage**: (Optional) Check whether the client certificate has one or more attributes set. Supported values are **Client authentication** (`1.3.6.1.5.5.7.3.2`) and/or **Email** (`1.3.6.1.5.5.7.3.4`).
   7. **Check for private key**: (Recommended) When enabled, WARP checks that the device has a private key associated with the client certificate.
   8. **Subject Alternative Name**: (Optional) To check for a Subject Alternative Name (SAN) on the client certificate, enter a string with optional `${serial_number}` and `${hostname}` variables (for example, `${serial_number}_mycompany`). The Cloudflare One Client will search for an exact, case-insensitive match. You can add multiple SANs to the posture check — a certificate only needs to match one SAN for the check to pass.
<ol start="6">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the client certificate check is returning the expected results.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>You can use the following commands to check if a client certificate is properly installed and trusted on the device.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5930.md")
</div></div>
<p>For the posture check to pass, a certificate must appear in the output that validates against the uploaded signing certificate.</p>
