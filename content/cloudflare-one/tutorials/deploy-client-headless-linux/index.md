---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/
  description: This tutorial explains how to deploy the Cloudflare One Client on headless Linux devices using a service token and an installation script.
  full_title: Deploy the Cloudflare One Client on headless Linux machines · Cloudflare One docs
  head_html: <title>Deploy the Cloudflare One Client on headless Linux machines · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to deploy the Cloudflare One Client on headless Linux devices using a service token and an installation script."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/index.md"><meta property="og:title" content="Deploy the Cloudflare One Client on headless Linux machines · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to deploy the Cloudflare One Client on headless Linux devices using a service token and an installation script."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Linux"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/#page","headline":"Deploy the Cloudflare One Client on headless Linux machines \u00b7 Cloudflare One docs","description":"This tutorial explains how to deploy the Cloudflare One Client on headless Linux devices using a service token and an installation script.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/deploy-client-headless-linux/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Linux"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/deploy-client-headless-linux/
  schema: 1
---
<p>This tutorial explains how to deploy the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> on Linux devices using a service token and an installation script. This deployment workflow is designed for headless servers - that is, servers which do not have access to a browser for identity provider logins - and for situations where you want to fully automate the onboarding process. Because devices will not register through an identity provider, <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based policies</a> and logging will be unavailable.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4314.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Cloudflare Zero Trust account</a></li>
<li>Root or <code>sudo</code> access on a supported Linux device</li>
<li>Zero Trust team name</li>
<li>Service token Client ID and Client Secret</li>
</ul>
<h2 id="1-create-a-service-token"><ol>
<li>Create a service token</li>
</ol></h2>
<p>Fully automated deployments rely on a service token to enroll the Cloudflare One Client in your Zero Trust organization. You can use the same token to enroll multiple devices, or generate a unique token per device if they require different <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile settings</a>.</p>
<p>To create a service token:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4320.md")
</div></div>
<h2 id="2-configure-device-enrollment-permissions"><ol start="2">
<li>Configure device enrollment permissions</li>
</ol></h2>
<p>Device enrollment permissions determine the users and devices that can register WARP with your Zero Trust organization.</p>
<p>To allow devices to enroll using a service token:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4321.md")
</div>
<p>To configure service-token enrollment with Terraform, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token">Check for a service token</a>.</p>
<h2 id="3-create-an-installation-script"><ol start="3">
<li>Create an installation script</li>
</ol></h2>
<p>You can use a shell script to automate WARP installation and registration. The following example shows how to deploy the Cloudflare One Client on Ubuntu 24.04.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4323.md")
</div>
<h2 id="4-install-warp"><ol start="4">
<li>Install WARP</li>
</ol></h2>
<p>To install the Cloudflare One Client using the example script:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4324.md")
</div>
<p>The Cloudflare One Client is now deployed with the configuration parameters stored in the root-only <code>/var/lib/cloudflare-warp/mdm.xml</code>. Assuming <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#auto_connect"><code>auto_connect</code></a> is configured, the Cloudflare One Client will automatically connect to your Zero Trust organization.</p>
<p>Verify registration and connection:</p>
<pre tabindex="0"><code class="language-sh">sudo warp-cli --accept-tos registration show&#10;sudo warp-cli --accept-tos status&#10;</code></pre>
<p>Successful enrollment creates a device in <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> with the email <code>non_identity@&lt;team-name&gt;.cloudflareaccess.com</code>. Verify that <code>status</code> reports <code>Connected</code>. A command completion or HTTP redirect alone does not prove registration or connectivity.</p>
<p>The registration and status commands verify enrollment and the connection to Cloudflare. To verify end-to-end traffic, connect to an included destination using the protocol you intend to use. For Cloudflare Mesh, follow <a href="/mesh/guides/connect-client-devices/#2-verify-connectivity">Verify connectivity</a>.</p>
<p>If the client reports <code>Registration Missing due to: Does not exist in API</code>, or the <code>warp-svc</code> logs show an HTTP <code>400</code> enrollment response, enrollment failed. Confirm that the service token policy uses the <em>Service Auth</em> action, the policy is attached to device enrollment permissions, and the MDM team name and token values are correct. After correcting or confirming the configuration, restart the service and repeat both verification commands:</p>
<pre tabindex="0"><code class="language-sh">sudo systemctl restart warp-svc&#10;sudo warp-cli --accept-tos registration show&#10;sudo warp-cli --accept-tos status&#10;</code></pre>
