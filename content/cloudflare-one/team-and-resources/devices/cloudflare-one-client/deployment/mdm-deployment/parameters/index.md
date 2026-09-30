---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/
  description: Explore parameters for deploying the Cloudflare One Client via MDM, including organization setup and device registration for Zero Trust.
  full_title: Parameters · Cloudflare One docs
  head_html: <title>Parameters · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore parameters for deploying the Cloudflare One Client via MDM, including organization setup and device registration for Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/index.md"><meta property="og:title" content="Parameters · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore parameters for deploying the Cloudflare One Client via MDM, including organization setup and device registration for Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="XML,Post-quantum"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#page","headline":"Parameters \u00b7 Cloudflare One docs","description":"Explore parameters for deploying the Cloudflare One Client via MDM, including organization setup and device registration for Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["XML","Post-quantum"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/
  schema: 1
---
<p>Each Cloudflare One Client (formerly WARP) supports the following set of parameters as part of their deployment, regardless of the deployment mechanism.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6360.md")
</aside>
<h2 id="required-for-full-cloudflare-zero-trust-features">Required for full Cloudflare Zero Trust features</h2>
<p>For the majority of Cloudflare Zero Trust features to work, you need to specify a team name. Examples of Cloudflare Zero Trust features which depend on the team name are <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>, <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a>, and <a href="/cloudflare-one/reusable-components/posture-checks/">device posture</a>.</p>
<h3 id="organization"><code>organization</code></h3>
<p>Instructs the client to register the device with your organization. Registration requires authentication via an <a href="/cloudflare-one/integrations/identity-providers/">IdP</a> or <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service Auth</a>.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> Your <span class="nb-glossary-tooltip" title="team name">team name</span>.</p>
<h2 id="required-for-dns-only-policy-enforcement">Required for DNS-only policy enforcement</h2>
<p>This field is used to enforce DNS policies when deploying the client in DoH-only mode.</p>
<h3 id="gateway-unique-id"><code>gateway_unique_id</code></h3>
<p>Instructs the client to direct all DNS queries to a specific <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">Gateway DNS location</a>. This value is only necessary if deploying without a <a href="#organization">team name</a> or in an organization with multiple DNS locations. If you do not supply a DoH subdomain, we will automatically use the default Gateway DNS location for your organization.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> Your <span class="nb-glossary-tooltip" title="DoH subdomain">DoH subdomain</span>.</p>
<h2 id="organization-parameters">Organization parameters</h2>
<p>You can use the following parameters to configure a specific Zero Trust organization.</p>
<h3 id="allow-managed-deployments"><code>allow_managed_deployments</code></h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6363.md")
</div></details>
<p>Local kill switch for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">client version assignments</a> pushed from the Cloudflare dashboard. Use this parameter to opt a device out of dashboard-managed version changes regardless of what is configured in the dashboard.</p>
<p>By default, the device applies any assignment the dashboard sends. If no assignment targets the device, the parameter has no effect.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>true</code> — (default) The device applies client version assignments configured for it in the Cloudflare dashboard. If no assignment targets the device, this setting has no effect.</li>
<li><code>false</code> — The device ignores client version assignments and stays on its current installed version, regardless of what is configured in the dashboard.</li>
</ul>
<h3 id="auth-client-id"><code>auth_client_id</code></h3>
<p>Enrolls the device in your Zero Trust organization using a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#create-a-service-token">service token</a>.
Requires the <code>auth_client_secret</code> parameter.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> Client ID of the service token.</p>
<p>Example configuration:</p>
<pre tabindex="0"><code class="language-xml">&lt;key&gt;auth_client_id&lt;/key&gt;&#10;&lt;string&gt;88bf3b6d86161464f6509f7219099e57.access&lt;/string&gt;&#10;&lt;key&gt;auth_client_secret&lt;/key&gt;&#10;&lt;string&gt;bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5&lt;/string&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6359.md")
</aside>
<h3 id="auth-client-secret"><code>auth_client_secret</code></h3>
<p>Enrolls the device in your Zero Trust organization using a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#create-a-service-token">service token</a>.
Requires the <code>auth_client_id</code> parameter.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> Client Secret of the service token.</p>
<h3 id="auto-connect"><code>auto_connect</code></h3>
<p>If switch has been turned off by user, the client will automatically turn itself back on after the specified number of minutes. We recommend keeping this set to a very low value — usually just enough time for a user to log in to hotel or airport Wi-Fi. If any value is specified for <code>auto_connect</code> the default state of the Cloudflare One Client will always be Connected (for example, after the initial install or a reboot).</p>
<p><strong>Value Type:</strong> <code>integer</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>0</code> — Allow the switch to stay in the off position indefinitely until the user turns it back on.</li>
<li><code>1</code> to <code>1440</code> — Turn switch back on automatically after the specified number of minutes.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6358.md")
</aside>
<h3 id="display-name"><code>display_name</code></h3>
<p>Identifies a Zero Trust organization in the Cloudflare One Client GUI when the client is deployed with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">multiple organizations</a>. Required if the <code>organization</code> parameter is specified within a <a href="#configs"><code>configs</code> array</a>.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> Organization nickname shown to users in the Cloudflare One Client GUI (for example, <code>Test environment</code>).</p>
<h3 id="enable-netbt"><code>enable_netbt</code></h3>
<p>NetBIOS over TCP/IP (NetBT) is a legacy feature in Windows primarily used for name resolution in some <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#when-to-enable-netbt">rare scenarios</a>. The Cloudflare One Client disables NetBT on the tunnel interface by default for security reasons. If your organization still relies on legacy applications that require NetBT, you can override the default behavior and enable NetBT.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — (default) Disables NetBT on the Cloudflare One Client tunnel interface.</li>
<li><code>true</code> — Enables NetBT on the Cloudflare One Client tunnel interface.</li>
</ul>
<h3 id="enable-pmtud"><code>enable_pmtud</code></h3>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/">Path MTU Discovery (PMTUD)</a> allows the Cloudflare One Client to discover the largest packet size that can be sent over the current network and optimize connection performance.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — (default) Disables PMTUD.</li>
<li><code>true</code> — Enables PMTUD on the Cloudflare One Client tunnel interface.</li>
</ul>
<h3 id="enable-post-quantum"><code>enable_post_quantum</code></h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6364.md")
</div></details>
<p>The Cloudflare One Client uses <a href="/ssl/post-quantum-cryptography/">post-quantum cryptography</a> to secure connections from the device to Cloudflare's network. Post-quantum cryptography requires the <a href="#warp_tunnel_protocol">MASQUE protocol</a> and is enabled by default on all devices using MASQUE.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — Disables post-quantum key agreement.</li>
<li><code>true</code> — Enables post-quantum key agreement for all traffic through the WARP tunnel.</li>
</ul>
<h3 id="environment"><code>environment</code></h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6365.md")
</div></details>
<p>Configures the Cloudflare One Client to connect to Cloudflare's FedRAMP High authorized environment.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>normal</code> — (default) The Cloudflare One Client connects to the standard API endpoints, IPs, and domains (like <code>&lt;ACCOUNT_ID&gt;.cloudflare-gateway.com</code>) and forwards traffic to Cloudflare data centers worldwide.</li>
<li><code>fedramp_high</code> — The Cloudflare One Client connects to FedRAMP-specific API endpoints, IPs, and domains (like <code>&lt;ACCOUNT_ID&gt;.fed.cloudflare-gateway.com</code>). Traffic is forwarded to FedRAMP High compliant data centers for processing. To configure the FedRAMP High environment, you must allow the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">FedRAMP-specific endpoints, IPs, and domains</a> through your firewall.</li>
</ul>
<p>When using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">multiple configurations</a> for the same organization, all configurations must specify the same <code>environment</code> value. A single organization cannot operate in both the normal and FedRAMP High environments.</p>
<p>In version 2026.5.0 and above, use <a href="#organization_configs"><code>organization_configs</code></a> to set <code>environment</code> once per organization rather than repeating it in every config entry:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization_configs&lt;/key&gt;&#10;  &lt;dict&gt;&#10;    &lt;key&gt;mycompany-gov&lt;/key&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;environment&lt;/key&gt;&#10;      &lt;string&gt;fedramp_high&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/dict&gt;&#10;  &lt;key&gt;configs&lt;/key&gt;&#10;  &lt;array&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;mycompany-gov&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Production&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;mycompany-gov&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Staging&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;test-org&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Test&lt;/string&gt;&#10;      &lt;key&gt;environment&lt;/key&gt;&#10;      &lt;string&gt;normal&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>In earlier versions, each configuration for that organization must include <code>environment</code> explicitly:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;configs&lt;/key&gt;&#10;  &lt;array&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;mycompany-gov&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Production&lt;/string&gt;&#10;      &lt;key&gt;environment&lt;/key&gt;&#10;      &lt;string&gt;fedramp_high&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;mycompany-gov&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Staging&lt;/string&gt;&#10;      &lt;key&gt;environment&lt;/key&gt;&#10;      &lt;string&gt;fedramp_high&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;test-org&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Test&lt;/string&gt;&#10;      &lt;key&gt;environment&lt;/key&gt;&#10;      &lt;string&gt;normal&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<h3 id="external-emergency-signal-fingerprint"><code>external_emergency_signal_fingerprint</code></h3>
<p>The SHA-256 fingerprint that the Cloudflare One Client will use to validate the <a href="#external_emergency_signal_url"><code>external_emergency_signal_url</code></a> HTTPS endpoint. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">External Emergency Disconnect</a> for details on how to extract this fingerprint.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> SHA-256 fingerprint of the HTTPS server certificate (for example, <code>DD4F4806C57A5BBAF1AA5B080F0541DA75DB468D0A1FE731310149500CCD8662</code>)</p>
<h3 id="external-emergency-signal-interval"><code>external_emergency_signal_interval</code></h3>
<p>How often the Cloudflare One Client will poll <a href="#external_emergency_signal_url"><code>external_emergency_signal_url</code></a> for an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">External Emergency Disconnect</a> signal.</p>
<p><strong>Value Type:</strong> <code>integer</code></p>
<p><strong>Value:</strong> Polling frequency in seconds (minimum <code>30</code>, default <code>300</code>)</p>
<h3 id="external-emergency-signal-url"><code>external_emergency_signal_url</code></h3>
<p>The HTTPS endpoint that the Cloudflare One Client will poll for an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">External Emergency Disconnect</a> signal.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> <code>https://192.0.2.1:3333/status/disconnect</code></p>
<p>The URL must use <code>https://</code> and use an IPv4 or IPv6 address as host (not a domain).</p>
<h3 id="hardware-backed-registration"><code>hardware_backed_registration</code></h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6366.md")
</div></details>
<p>Binds the registration to a non-exportable key stored in device hardware (Secure Enclave or TPM 2.0) and authenticates API requests with mTLS. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a>.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — (default) The Cloudflare One Client stores its API token in the device keystore.</li>
<li><code>true</code> — The Cloudflare One Client generates a hardware-backed key during registration and uses mTLS for subsequent API calls.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6357.md")
</aside>
<h3 id="local-emergency-signal-enabled"><code>local_emergency_signal_enabled</code></h3>
<p>Enables <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-local-emergency-disconnect">Local Emergency Disconnect</a>. When enabled, the Cloudflare One Client monitors a fixed-path JSON file on the device for an emergency disconnect signal.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — (default) Local signal file monitoring is disabled.</li>
<li><code>true</code> — The client monitors the local signal file for emergency disconnect.</li>
</ul>
<h3 id="onboarding"><code>onboarding</code></h3>
<p>Controls the visibility of the onboarding screens that ask the user to review the privacy policy during an application's first launch.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — Screens hidden.</li>
<li><code>true</code> — (default) Screens visible.</li>
</ul>
<h3 id="override-api-endpoint"><code>override_api_endpoint</code></h3>
<p>Overrides the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#client-orchestration-api">IP address</a> used by the Cloudflare One Client to communicate with the client orchestration API. If you set this parameter, be sure to update your organization's firewall to ensure the new IP is allowed through.</p>
<p>This functionality is intended for use with a Cloudflare China local network partner or any other third-party network partner that can maintain the integrity of network traffic. Most IT admins should not set this setting as it will redirect all API traffic to a new IP.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> <code>1.2.3.4</code> — Redirect all client orchestration API calls to <code>1.2.3.4</code>.</p>
<p>The string must be a valid IPv4 or IPv6 address, otherwise the Cloudflare One Client will fail to parse the entire MDM file.</p>
<h3 id="override-doh-endpoint"><code>override_doh_endpoint</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6356.md")
</aside>
<p>Overrides the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#doh-ip">IP address</a> used by the Cloudflare One Client to resolve DNS queries via DNS over HTTPS (DoH). If you set this parameter, be sure to update your organization's firewall to ensure the new IP is allowed through.</p>
<p>This functionality is intended for use with a Cloudflare China local network partner or any other third-party network partner that can maintain the integrity of network traffic. Most IT admins should not set this setting as it will redirect all DoH traffic to a new IP.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> <code>1.2.3.4</code> — Redirect all DNS over HTTPS lookups to <code>1.2.3.4</code>.</p>
<p>The string must be a valid IPv4 or IPv6 address, otherwise the Cloudflare One Client will fail to parse the entire MDM file.</p>
<h3 id="override-warp-endpoint"><code>override_warp_endpoint</code></h3>
<p>Overrides the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#warp-ingress-ip">IP address and UDP port</a> used by the Cloudflare One Client to send traffic to Cloudflare's edge. If you set this parameter, be sure to update your organization's firewall to ensure the new IP is allowed through.</p>
<p>This functionality is intended for use with a Cloudflare China local network partner or any other third-party network partner that can maintain the integrity of network traffic. Most IT admins should not set this setting as it will redirect all Cloudflare One Client traffic to a new IP.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> <code>203.0.113.0:500</code> — Redirect all Cloudflare One Client traffic to <code>203.0.113.0</code> on port <code>500</code>.</p>
<p>The string must be a valid IPv4 or IPv6 socket address (containing the IP address and port number), otherwise the Cloudflare One Client will fail to parse the entire MDM file.</p>
<h3 id="service-mode"><code>service_mode</code></h3>
<p>Allows you to choose the operational mode of the client.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>warp</code> — (default) <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default">Traffic and DNS mode</a>.</li>
<li><code>1dot1</code> — <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">DNS only mode</a>.</li>
<li><code>proxy</code> — <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Local proxy mode</a>. Use the <code>proxy_port</code> parameter to specify the localhost SOCKS proxy port (between <code>0</code>-<code>66535</code>). For example,</li>
</ul>
<pre tabindex="0"><code class="language-xml">&lt;key&gt;service_mode&lt;/key&gt;&#10;&lt;string&gt;proxy&lt;/string&gt;&#10;&lt;key&gt;proxy_port&lt;/key&gt;&#10;&lt;integer&gt;44444&lt;/integer&gt;&#10;</code></pre>
<ul>
<li><code>postureonly</code> — <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#posture-only-mode">Posture only mode</a>.</li>
<li><code>tunnelonly</code> - <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode">Traffic only mode</a>.</li>
</ul>
<h3 id="support-url"><code>support_url</code></h3>
<p>When the Cloudflare One Client is deployed via MDM, the in-app <strong>Send Feedback</strong> button is disabled by default. This parameter allows you to re-enable the button and direct feedback towards your organization.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>https://&lt;support.example.com&gt;</code> — Use an <code>https://</code> link to open your company's internal help site.</li>
<li><code>mailto:&lt;yoursupport@example.com&gt;</code> — Use a <code>mailto:</code> link to open your default mail client.</li>
</ul>
<h3 id="switch-locked"><code>switch_locked</code></h3>
<p>Allows the user to turn off the client switch and disconnect the Cloudflare One Client.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — (default) The user is able to turn the switch on/off at their discretion. When the switch is off, the user will not have the ability to reach sites protected by Access that leverage certain device posture checks.</li>
<li><code>true</code> — The user is prevented from turning off the switch. The Cloudflare One Client will automatically start in the connected state.</li>
</ul>
<p>On new deployments, you must also include the <code>auto_connect</code> parameter with at least a value of <code>0</code>. This will prevent clients from being deployed in the off state without a way for users to manually enable them.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6355.md")
</aside>
<h3 id="unique-client-id"><code>unique_client_id</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6354.md")
</aside>
<p>Assigns a unique identifier to the device for the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/device-uuid">device UUID posture check</a>.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong> UUID for the device (for example, <code>496c6124-db89-4735-bc4e-7f759109a6f1</code>).</p>
<h3 id="use-in-app-webview"><code>use_in_app_webview</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6353.md")
</aside>
<p>Uses an in-app WebView for Zero Trust authentication instead of the default system browser. This setting is required when Always-on VPN with Lockdown mode is enabled.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — (default) Uses the default system browser for Zero Trust authentication.</li>
<li><code>true</code> — Uses an in-app WebView for Zero Trust authentication.</li>
</ul>
<h3 id="warp-tunnel-protocol"><code>warp_tunnel_protocol</code></h3>
<p>Configures the protocol used to route IP traffic from the device to Cloudflare Gateway. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">Device tunnel protocol</a>.</p>
<p><strong>Value Type:</strong> <code>string</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>masque</code> — (default) <a href="https://datatracker.ietf.org/wg/masque/about/">MASQUE</a> protocol</li>
<li><code>wireguard</code> — <a href="https://www.wireguard.com/">WireGuard</a> protocol</li>
</ul>
<h2 id="top-level-parameters">Top-level parameters</h2>
<p>Top-level parameters determine how the Cloudflare One Client manages device registrations.</p>
<h3 id="configs"><code>configs</code></h3>
<p>Allows a user to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch between Zero Trust organizations</a> in the Cloudflare One Client GUI. The <code>configs</code> array is also required when using another <a href="#top-level-parameters">top-level parameter</a> such as <code>multi_user</code> or <code>pre_login</code>, even if only one organization is specified.</p>
<p><strong>Value Type:</strong> <code>array</code></p>
<p><strong>Value:</strong> An array containing one or more Zero Trust organizations.</p>
<h3 id="multi-user"><code>multi_user</code></h3>
<p>Enables multiple user registrations on a Windows device.</p>
<p><strong>Value Type:</strong> <code>boolean</code></p>
<p><strong>Value:</strong></p>
<ul>
<li><code>false</code> — (default) Only one Cloudflare One Client registration is stored per device. After a user logs in to the Cloudflare One Client, their settings and identity will apply to all traffic from the device.</li>
<li><code>true</code> — Each Windows user has their own Cloudflare One Client registration. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">Multiple users on a Windows device</a>.</li>
</ul>
<h3 id="organization-configs"><code>organization_configs</code></h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6367.md")
</div></details>
<p>Defines organization-wide settings that apply to all <a href="#configs"><code>configs</code></a> entries for a given organization, overriding any conflicting values set within individual config entries.</p>
<p><strong>Value Type:</strong> <code>dict</code></p>
<p><strong>Value:</strong> A dict where each key is an organization name (team name) and each value is a dict of organization-wide settings.</p>
<p>Supported settings:</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>environment</code></td>
<td>Overrides the <a href="#environment"><code>environment</code></a> value for all configs belonging to this organization.</td>
</tr>
<tr>
<td><code>hardware_backed_registration</code></td>
<td>Overrides the <a href="#hardware_backed_registration"><code>hardware_backed_registration</code></a> value for all configs belonging to this organization.</td>
</tr>
</tbody>
</table>
<p>Use <code>organization_configs</code> when you have multiple configurations for the same organization and want to enforce a single <code>environment</code> value across all of them. Any <code>environment</code> value set inside an individual <code>configs</code> entry for that organization will be overridden by the value specified in <code>organization_configs</code>.</p>
<p>Example configuration where <code>test-org</code> has two configs (Production and Staging), both enforced to use <code>fedramp_high</code> via <code>organization_configs</code>:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization_configs&lt;/key&gt;&#10;  &lt;dict&gt;&#10;    &lt;key&gt;test-org&lt;/key&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;environment&lt;/key&gt;&#10;      &lt;string&gt;fedramp_high&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/dict&gt;&#10;  &lt;key&gt;configs&lt;/key&gt;&#10;  &lt;array&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;test-org&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Production&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;    &lt;dict&gt;&#10;      &lt;key&gt;organization&lt;/key&gt;&#10;      &lt;string&gt;test-org&lt;/string&gt;&#10;      &lt;key&gt;display_name&lt;/key&gt;&#10;      &lt;string&gt;Staging&lt;/string&gt;&#10;    &lt;/dict&gt;&#10;  &lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<h3 id="pre-login"><code>pre_login</code></h3>
<p>Allows the Cloudflare One Client to connect with a service token before a user completes the initial Windows login. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-prelogin/">Connect the Cloudflare One Client before Windows login</a>.</p>
<h2 id="per-app-vpn-parameters-android">Per-app VPN parameters (Android)</h2>
<p><a href="https://support.google.com/work/android/answer/9213914?hl=en">Per-app VPN</a> parameters allow you to choose the Android apps that can send traffic through the WARP tunnel. Admins can configure these parameters via any MDM tool that supports deploying an Android app to managed devices or work profiles.</p>
<h3 id="app-identifier"><code>app_identifier</code></h3>
<p>An application package name/bundle identifier which uniquely identifies the app on the Google Play Store. This application will be tunneled through the Cloudflare One Client service.</p>
<p><strong>Value Type</strong>: <code>string</code></p>
<p><strong>Value</strong>: The app identifier can be found in the ID query parameter of the specific app's Play Store URL. For example: in the case of <code>https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent</code>, the app identifier for the Cloudflare One Agent app is <code>com.cloudflare.cloudflareoneagent</code>.</p>
<h3 id="is-browser"><code>is_browser</code></h3>
<p>An optional property. <code>is_browser</code> will help the Cloudflare One Agent application decide which browser to open instead of the default browser for specific features such as re-authentication and Gateway block notifications. If needed, admins should explicitly indicate that a given <code>tunneled_app</code> is a browser, rather than relying on automatic browser detection.</p>
<p><strong>Value Type</strong>: <code>boolean</code></p>
<p><strong>Value</strong>: If the value is <code>true</code>, identifies the application defined in <code>app_identifier</code> as a browser. The default value is <code>false</code> and <code>is_browser</code> is an optional property.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Traffic and DNS mode is supported in client version 2025.2.664.0 and below. In version 2025.4.589.1 and above, this parameter does not apply to Traffic and DNS mode because all DoH traffic goes inside of the WARP tunnel.</li></ol></section>
