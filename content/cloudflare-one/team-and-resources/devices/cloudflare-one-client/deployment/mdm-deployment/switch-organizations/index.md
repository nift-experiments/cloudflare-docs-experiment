---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/
  description: Switch between Zero Trust organizations in Zero Trust.
  full_title: Switch between Zero Trust organizations · Cloudflare One docs
  head_html: <title>Switch between Zero Trust organizations · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Switch between Zero Trust organizations in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/index.md"><meta property="og:title" content="Switch between Zero Trust organizations · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Switch between Zero Trust organizations in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="XML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/#page","headline":"Switch between Zero Trust organizations \u00b7 Cloudflare One docs","description":"Switch between Zero Trust organizations in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["XML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6338.md")
</div></details>
<p>In the Cloudflare One Client (formerly WARP), users can switch between multiple Zero Trust organizations (or other <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">MDM parameters</a>) that administrators specify in an MDM file. Common use cases include:</p>
<ul>
<li>Allow IT security staff to switch between test and production environments.</li>
<li>Allow Managed Service Providers to support multiple customer accounts.</li>
<li>Allow users to switch between the default Cloudflare One Client ingress IPs and the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#override_warp_endpoint">Cloudflare China ingress IPs</a>.</li>
</ul>
<h2 id="mdm-file-format">MDM file format</h2>
<p>To enable multiple organizations, administrators need to modify their <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">MDM file</a> to take an array of configurations. Each configuration must include a <code>display_name</code> parameter that will be visible to users in the Cloudflare One Client GUI. Because display names are listed in the same order as they appear in the MDM file, we recommend putting the most used configurations at the top of the file. When a user opens the Cloudflare One Client for the first time, they will be prompted to log into the first configuration in the list.</p>
<p>An MDM file supports a maximum of 25 configurations. The following example includes three configurations.</p>
<h3 id="xml">XML</h3>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;	&lt;key&gt;configs&lt;/key&gt;&#10;	&lt;array&gt;&#10;		&lt;dict&gt;&#10;			&lt;key&gt;organization&lt;/key&gt;&#10;			&lt;string&gt;mycompany&lt;/string&gt;&#10;			&lt;key&gt;display_name&lt;/key&gt;&#10;			&lt;string&gt;Production environment&lt;/string&gt;&#10;		&lt;/dict&gt;&#10;		&lt;dict&gt;&#10;			&lt;key&gt;organization&lt;/key&gt;&#10;			&lt;string&gt;mycompany&lt;/string&gt;&#10;			&lt;key&gt;override_api_endpoint&lt;/key&gt;&#10;			&lt;string&gt;203.0.113.0&lt;/string&gt;&#10;			&lt;key&gt;override_doh_endpoint&lt;/key&gt;&#10;			&lt;string&gt;203.0.113.0&lt;/string&gt;&#10;			&lt;key&gt;override_warp_endpoint&lt;/key&gt;&#10;			&lt;string&gt;203.0.113.0:0&lt;/string&gt;&#10;			&lt;key&gt;display_name&lt;/key&gt;&#10;			&lt;string&gt;China employees&lt;/string&gt;&#10;		&lt;/dict&gt;&#10;		&lt;dict&gt;&#10;			&lt;key&gt;organization&lt;/key&gt;&#10;			&lt;string&gt;test-org&lt;/string&gt;&#10;			&lt;key&gt;display_name&lt;/key&gt;&#10;			&lt;string&gt;Test environment&lt;/string&gt;&#10;		&lt;/dict&gt;&#10;	&lt;/array&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<h3 id="plist">plist</h3>
<p><a href="/cloudflare-one/static/mdm/multiple-orgs/com.cloudflare.warp.plist">Download</a> an example <code>.plist</code> file.</p>
<h3 id="mobileconfig">mobileconfig</h3>
<p><a href="/cloudflare-one/static/mdm/multiple-orgs/CloudflareWARP.mobileconfig">Download</a> an example <code>.mobileconfig</code> file.</p>
<h2 id="switch-organizations-in-the-cloudflare-one-client">Switch organizations in the Cloudflare One Client</h2>
<p>To switch to a different organization as a user:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6342.md")
</div></div>
<ol start="3">
<li>Select the configuration that you want to connect to.</li>
<li>If prompted, complete the authentication steps required for the new organization. Your authentication information will be saved and you will be able to switch back and forth between configurations.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6337.md")
</aside>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>When switching organizations or connecting for the first time, keep the following in mind:</p>
<ul>
<li>If this is the first time connecting to an organization, web browsers like Chrome may require a full restart to correctly recognize and trust the organization's root certificate. Cloudflare recommends closing all browser windows after the initial connection. All subsequent switches should not require a restart.</li>
<li>On macOS, ensure the specific CA certificate for the new organization is properly trusted by verifying its status in Keychain Access.</li>
<li>Switching configurations may sometimes momentarily disconnect the Cloudflare One Client. If this occurs, simply re-enable the Cloudflare One Client to restore the connection.</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Logging out is only possible if [Allow device to leave organization](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-device-to-leave-organization) is enabled for your device.</li></ol></section>
