---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/
  description: Hardware-backed registration binds a Cloudflare One Client registration to a Secure Enclave or TPM key and authenticates API requests with mTLS.
  full_title: Hardware-backed registration · Cloudflare One docs
  head_html: <title>Hardware-backed registration · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Hardware-backed registration binds a Cloudflare One Client registration to a Secure Enclave or TPM key and authenticates API requests with mTLS."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/index.md"><meta property="og:title" content="Hardware-backed registration · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Hardware-backed registration binds a Cloudflare One Client registration to a Secure Enclave or TPM key and authenticates API requests with mTLS."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="mTLS,TPM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/#page","headline":"Hardware-backed registration \u00b7 Cloudflare One docs","description":"Hardware-backed registration binds a Cloudflare One Client registration to a Secure Enclave or TPM key and authenticates API requests with mTLS.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS","TPM"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6374.md")
</div></details>
<p>Hardware-backed registration binds a device registration to a non-exportable private key stored in device hardware. The Cloudflare One Client uses this key to prove that API requests originate from the device that created the registration.</p>
<p>By default, the Cloudflare One Client stores its API token in the device keystore. An attacker who extracts that token can replay it from another device. Hardware-backed registration protects against this token extraction by requiring every API request to be authenticated with a key that never leaves the device hardware.</p>
<p>Before you turn on hardware-backed registration, note the following:</p>
<ul>
<li><strong>Re-registration is required.</strong> Turning the setting on or off invalidates the existing registration and forces affected devices to register again. The Cloudflare One Client does not migrate a registration between hardware-backed and standard registration.</li>
<li><strong>Configure it at the organization layer.</strong> Set <code>hardware_backed_registration</code> in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs"><code>organization_configs</code></a> so the setting applies consistently to every configuration for an organization.</li>
<li><strong>Certificates expire.</strong> The hardware-backed certificate is valid for 90 days. A device that stays offline until the certificate expires — for example, during an extended vacation — must register again.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>When hardware-backed registration is turned on, the Cloudflare One Client performs the following steps during <a href="/cloudflare-one/team-and-resources/devices/device-registration/">device registration</a>:</p>
<ol>
<li>The client generates a non-exportable key pair in a hardware security module on the device.</li>
<li>The client creates a certificate signing request (CSR) for the key and sends it with the registration request.</li>
<li>Cloudflare issues a client certificate for the key and returns it to the client.</li>
<li>The client authenticates all subsequent API requests with <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">mutual TLS (mTLS)</a>, signing the TLS handshake with the hardware-backed key.</li>
</ol>
<p>Cloudflare validates each request against the certificate stored for the registration. Requests that do not present the matching certificate are rejected. Because the private key cannot leave the device, an extracted API token alone is not enough to make valid API requests from another device.</p>
<p>The client renews the certificate automatically before it expires, reusing the existing hardware-backed key so the registration is preserved.</p>
<h2 id="hardware-requirements">Hardware requirements</h2>
<p>Hardware-backed registration uses the security hardware available on each desktop platform:</p>
<table>
<thead>
<tr>
<th>Operating system</th>
<th>Hardware</th>
</tr>
</thead>
<tbody>
<tr>
<td>Windows</td>
<td>TPM 2.0</td>
</tr>
<tr>
<td>macOS</td>
<td>Secure Enclave (T2 or Apple silicon)</td>
</tr>
<tr>
<td>Linux</td>
<td>TPM 2.0</td>
</tr>
</tbody>
</table>
<p>Devices without a supported security module cannot complete a hardware-backed registration.</p>
<h2 id="turn-on-hardware-backed-registration">Turn on hardware-backed registration</h2>
<p>Hardware-backed registration is turned off by default. To turn it on, set the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#hardware_backed_registration"><code>hardware_backed_registration</code></a> parameter to <code>true</code> in the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs"><code>organization_configs</code></a> layer of your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">MDM configuration</a>.</p>
<p>The following example turns on hardware-backed registration for the <code>example-team</code> organization:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization_configs&lt;/key&gt;&#10;  &lt;dict&gt;&#10;    &lt;key&gt;example-team&lt;/key&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;hardware_backed_registration&lt;/key&gt;&#10;      &lt;true/&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/dict&gt;&#10;  &lt;key&gt;configs&lt;/key&gt;&#10;  &lt;array&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;example-team&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Example team&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<p>Hardware-backed registration is available on Windows, macOS, and Linux only. Mobile platforms (iOS, Android, and ChromeOS) are not supported. The feature applies only to Zero Trust registrations that use an <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> or a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>. Consumer registrations are not supported.</p>
