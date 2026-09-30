---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/
  description: First-time setup in Zero Trust.
  full_title: Set up the Cloudflare One Client for your organization · Cloudflare One docs
  head_html: <title>Set up the Cloudflare One Client for your organization · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="First-time setup in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/index.md"><meta property="og:title" content="Set up the Cloudflare One Client for your organization · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="First-time setup in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/#page","headline":"Set up the Cloudflare One Client for your organization \u00b7 Cloudflare One docs","description":"First-time setup in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/
  schema: 1
---
<p>This guide walks you through setting up the Cloudflare One Client (formerly WARP) for your organization for the first time. After completing these steps, your devices will route traffic through Cloudflare's network, where you can apply security policies.</p>
<p>Choose a setup mode based on your needs:</p>
<ul>
<li><a href="#traffic-and-dns-mode-default"><strong>Traffic and DNS mode</strong> (default)</a> — Enables the full suite of security features, including HTTP inspection, identity-based policies, and device posture checks.</li>
<li><a href="#dns-only-mode"><strong>DNS-only mode</strong></a> — Filters only DNS queries. Does not inspect HTTP traffic or enforce device posture checks.</li>
</ul>
<h2 id="traffic-and-dns-mode-default">Traffic and DNS mode (default)</h2>
<p>This mode enables the complete suite of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">device security features</a>.</p>
<h3 id="1-create-a-cloudflare-zero-trust-account"><ol>
<li>Create a Cloudflare Zero Trust account.</li>
</ol></h3>
<p>The <a href="https://dash.cloudflare.com/one/">Cloudflare One dashboard</a> will be your go-to place to check device connectivity data, as well as create Secure Web Gateway and Zero Trust policies for your organization.</p>
<p>As you complete the <a href="/cloudflare-one/setup/">Cloudflare Zero Trust onboarding</a>, you will be asked to create a <span class="nb-glossary-tooltip" title="team name">team name</span> for your organization. You will need the team name when you deploy the Cloudflare One Client on your devices; it will allow your users to connect to your organization's Cloudflare Zero Trust instance.</p>
<h3 id="2-set-up-a-login-method"><ol start="2">
<li>Set up a login method.</li>
</ol></h3>
<p>Configure <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">One-time PIN</a> or connect a <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> in Zero Trust. This is the login method your users will utilize when authenticating to add a new device to your Cloudflare Zero Trust setup.</p>
<h3 id="3-define-device-enrollment-permissions"><ol start="3">
<li>Define device enrollment permissions.</li>
</ol></h3>
<p>Create <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">device enrollment rules</a> to define which users in your organization should be able to connect devices to your organization's Cloudflare Zero Trust setup. As you create your rule, you will be asked to select which login method you would like users to authenticate with.</p>
<h3 id="4-install-the-cloudflare-root-certificate-on-your-devices"><ol start="4">
<li>Install the Cloudflare root certificate on your devices.</li>
</ol></h3>
<p>Advanced security features including HTTP traffic inspection require users to install and trust the <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Cloudflare root certificate</a> on their machine or device. If you are installing certificates manually on all your devices, these steps will need to be performed on each new device that is to be subject to HTTP filtering.</p>
<h3 id="5-download-and-deploy-the-cloudflare-one-client-to-your-devices"><ol start="5">
<li>Download and deploy the Cloudflare One Client to your devices.</li>
</ol></h3>
<p>Choose one of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">different ways</a> to deploy the Cloudflare One Client, depending on what works best for your organization.</p>
<h3 id="6-log-in-to-your-organization-s-cloudflare-zero-trust-instance-from-your-devices"><ol start="6">
<li>Log in to your organization's Cloudflare Zero Trust instance from your devices.</li>
</ol></h3>
<p>Once the Cloudflare One Client is installed on the device, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">log in to your Zero Trust organization</a>. The user is prompted to authenticate with one of your configured login methods. New organizations include the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as the default, so users can sign in with their Cloudflare account credentials. You can also connect a <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> or enable a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN</a>.</p>
<p>Next, build <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway policies</a> to filter DNS, HTTP, and Network traffic on your devices.</p>
<h2 id="dns-only-mode">DNS only mode</h2>
<p>This mode is best suited for organizations that only want to apply DNS filtering to outbound traffic from their company devices. It does not enable advanced HTTP filtering features such as HTTP policies, identity-based policies, device posture checks, or Browser Isolation.</p>
<h3 id="1-create-a-cloudflare-zero-trust-account-1"><ol>
<li>Create a Cloudflare Zero Trust account.</li>
</ol></h3>
<p>Zero Trust will be your go-to place to check device connectivity data, as well as create Secure Web Gateway and Zero Trust policies for your organization.</p>
<p>As you complete the <a href="/cloudflare-one/setup/">Cloudflare Zero Trust onboarding</a>, you will be asked to create a <span class="nb-glossary-tooltip" title="team name">team name</span> for your organization. You will need the team name when you deploy the Cloudflare One Client on your devices; it will allow your users to connect to your organization's Cloudflare Zero Trust instance.</p>
<h3 id="2-set-up-a-login-method-1"><ol start="2">
<li>Set up a login method.</li>
</ol></h3>
<p>Configure <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">One-time PIN</a> or connect a <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> in Zero Trust. This is the login method your users will utilize when authenticating to add a new device to your Cloudflare Zero Trust setup.</p>
<h3 id="3-define-device-enrollment-permissions-1"><ol start="3">
<li>Define device enrollment permissions.</li>
</ol></h3>
<p>Create <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">device enrollment rules</a> to define which users in your organization should be able to connect devices to your organization's Cloudflare Zero Trust setup. As you create your rule, you will be asked to select which login method you would like users to authenticate with.</p>
<h3 id="4-optional-add-a-dns-location-to-gateway"><ol start="4">
<li>(Optional) Add a DNS location to Gateway.</li>
</ol></h3>
<p>By default, the Cloudflare One Client sends DNS queries to Cloudflare using an encrypted protocol called DNS-over-HTTPS (DoH). If you need to apply different DNS policies to different offices or network locations, <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">add a DNS location</a> to Gateway. Gateway will assign a unique <span class="nb-glossary-tooltip" title="DoH subdomain">DoH subdomain</span> to each location, which you provide as a parameter when deploying the Cloudflare One Client to your devices.</p>
<h3 id="5-download-and-deploy-the-cloudflare-one-client-to-your-devices-1"><ol start="5">
<li>Download and deploy the Cloudflare One Client to your devices.</li>
</ol></h3>
<p>Choose one of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">different ways</a> to deploy the Cloudflare One Client, depending on what works best for your organization.</p>
<p>Next, create <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a> to control how DNS queries from your devices get resolved.</p>
