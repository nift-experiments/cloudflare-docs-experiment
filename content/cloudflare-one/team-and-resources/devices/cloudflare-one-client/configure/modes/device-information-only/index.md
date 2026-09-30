---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/
  description: Enable Posture only mode in Zero Trust.
  full_title: Enable Posture only mode · Cloudflare One docs
  head_html: <title>Enable Posture only mode · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable Posture only mode in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/index.md"><meta property="og:title" content="Enable Posture only mode · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable Posture only mode in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture,mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/#page","headline":"Enable Posture only mode \u00b7 Cloudflare One docs","description":"Enable Posture only mode in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture","mTLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6313.md")
</div></details>
<p>Posture only mode allows you to enforce device posture rules when a user connects to your <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted Access application</a>. This mode relies on a client certificate generated from your account to establish trust between the Access application and the device.</p>
<h2 id="1-turn-on-account-settings"><ol>
<li>Turn on account settings</li>
</ol></h2>
<p>Using the API, enable client certificate provisioning for <a href="/fundamentals/account/find-account-and-zone-ids/">your zone</a>:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/devices/policy/certificates \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<h2 id="2-configure-the-cloudflare-one-client"><ol start="2">
<li>Configure the Cloudflare One Client</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</p>
</li>
<li>
<p>Choose a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> and select <strong>Edit</strong>.</p>
</li>
<li>
<p>For <strong>Service mode</strong>, select <strong>Posture only mode</strong>.</p>
</li>
<li>
<p>Select <strong>Save profile</strong>.</p>
</li>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Enroll your device</a> into your Zero Trust organization.</p>
<p>When enrolled in Posture only mode, the Cloudflare One Client (formerly WARP) will automatically generate a client certificate and install the certificate on the device. This certificate is necessary to confirm the source of outgoing traffic.</p>
</li>
</ol>
<h2 id="3-optional-verify-the-client-certificate"><ol start="3">
<li>(Optional) Verify the client certificate</li>
</ol></h2>
<ol>
<li>To view the client certificates installed on the device:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6320.md")
</div></div>
<pre tabindex="0"><code>    The client certificate name should match the **Device ID** in your Cloudflare One Client **Preferences**.&#10;</code></pre>
<ol start="2">
<li>
<p>To verify the client certificate in your Cloudflare account:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select the zone for which you enabled client certificates.</li>
<li>Go to <strong>SSL/TLS</strong> &gt; <strong>Client Certificates</strong>.</li>
</ol>
<p>The certificate name is the WARP enrollment <strong>Device ID</strong>.
<img src="/assets/upstream/images/cloudflare-one/connections/device-information-only-cert.png" alt="Example client certificate in the Cloudflare dashboard" /></p>
</li>
</ol>
<h2 id="4-enforce-the-client-certificate"><ol start="4">
<li>Enforce the client certificate</li>
</ol></h2>
<p>To block traffic from devices that do not have a valid client certificate:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>SSL/TLS</strong> &gt; <strong>Client Certificates</strong>.</li>
<li>Under <strong>Hosts</strong>, select <strong>Edit</strong> and enter the hostname of your Access application (for example, <code>app.mycompany.com</code>). This enables mTLS authentication for the application.</li>
<li>Select <strong>Create mTLS rule</strong>.</li>
<li>Create a WAF custom rule that checks all requests to your application for a valid client certificate:</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client Certificate</td>
<td>equals</td>
<td>Off</td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Hostname</td>
<td>equals</td>
<td><code>app.mycompany.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
5. Select **Deploy**.
<p>Posture only mode is now enabled on the device. To start enforcing device posture, set up a <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">WARP client check</a> and add a <em>Require</em> device posture rule to your <a href="/cloudflare-one/access-controls/policies/">Access policy</a>. When the device connects to the Access application for the first time, the browser will ask to use the client certificate installed by the Cloudflare One Client.</p>
<div class="nb-width">
@markup("md", "content/.markup/bodies/6321.md")
</div>
<h2 id="limitations">Limitations</h2>
<p>Posture only mode is not compatible with the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-prelogin/">Windows pre-login</a> feature. The user must be logged into Windows because the Cloudflare One Client needs to <a href="#3-optional-verify-the-client-certificate">install a certificate</a> in the user store.</p>
