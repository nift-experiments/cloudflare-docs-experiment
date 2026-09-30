---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/
  description: Learn how to configure your Enterprise zone with Salesforce Commerce Cloud.
  full_title: Salesforce Commerce Cloud · Cloudflare for Platforms docs
  head_html: <title>Salesforce Commerce Cloud · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to configure your Enterprise zone with Salesforce Commerce Cloud."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/index.md"><meta property="og:title" content="Salesforce Commerce Cloud · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to configure your Enterprise zone with Salesforce Commerce Cloud."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><meta name="pcx_tags" content="Salesforce"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/#page","headline":"Salesforce Commerce Cloud \u00b7 Cloudflare for Platforms docs","description":"Learn how to configure your Enterprise zone with Salesforce Commerce Cloud.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Salesforce"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/
  schema: 1
---
<p>Cloudflare partners with Salesforce Commerce Cloud to provide Salesforce Commerce Cloud customers’ websites with Cloudflare’s performance and security benefits.</p>
<p>If you use Salesforce Commerce Cloud and also have a Cloudflare plan, you can use your own Cloudflare zone to proxy web traffic to your zone first, then Salesforce Commerce Cloud's (the SaaS Provider) zone second. This configuration option is called <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a>.</p>
<h2 id="benefits">Benefits</h2>
<p>O2O's benefits include applying your own Cloudflare zone's services and settings — such as <a href="/waf/">WAF</a>, <a href="/bots/plans/bm-subscription/">Bot Management</a>, <a href="/waiting-room/">Waiting Room</a>, and more — on the traffic destined for your Salesforce Commerce Cloud environment.</p>
<h2 id="how-it-works">How it works</h2>
<p>For additional detail about how traffic routes when O2O is enabled, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">How O2O works</a>.</p>
<h2 id="enable">Enable</h2>
<p>To enable O2O requires the following:</p>
<ol>
<li>You must configure your SFCC environment as an &quot;SFCC Proxy Zone&quot;. If you currently have an &quot;SFCC Legacy Zone&quot;, you cannot enable O2O.
<ul>
<li>For more details on the different types of SFCC configurations, refer to the <a href="https://help.salesforce.com/s/articleView?id=cc.b2c_ecdn_proxy_zone_faq.htm&amp;type=5">Salesforce FAQ on SFCC Proxy Zones</a>.</li>
<li>For instructions on how to migrate your SFCC environment to an &quot;SFCC Proxy Zone&quot;, refer to the <a href="https://help.salesforce.com/s/articleView?id=cc.b2c_migrate_legacy_zone_to_proxy_zone.htm&amp;type=5">SFCC Legacy Zone to SFCC Proxy Zone migration guide</a>.</li>
</ul>
</li>
<li>Your own Cloudflare zone on an Enterprise plan.</li>
</ol>
<p>If you meet the above requirements, O2O can then be enabled per hostname. To enable O2O for a specific hostname within your Cloudflare zone, <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create</a> a Proxied CNAME DNS record with a target of the CNAME provided by SFCC Business Manager, which is the dashboard used by SFCC customers to configure their storefront environment.</p>
<p>The CNAME provided by SFCC Business Manager will resemble <code>commcloud.prod-abcd-example-com.cc-ecdn.net</code> and contains 3 distinct parts. For each hostname routing traffic to SFCC, be sure to update each part of the example CNAME to match your SFCC environment:</p>
<ol>
<li><strong>Environment</strong>: <code>prod</code> should be changed to <code>prod</code> or <code>dev</code> or <code>stg</code>.</li>
<li><strong>Realm</strong>: <code>abcd</code> should be changed to the Realm ID assigned to you by SFCC.</li>
<li><strong>Domain Name</strong>: <code>example-com</code> should be changed to match your domain name in a hyphenated format.</li>
</ol>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Target</th>
<th>Proxy status</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CNAME</code></td>
<td><code>&lt;YOUR_HOSTNAME&gt;</code></td>
<td><code>commcloud.prod-abcd-example-com.cc-ecdn.net</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<p>For O2O to be configured properly, make sure your Proxied DNS record targets your SFCC CNAME <strong>directly</strong>. Do not indirectly target the SFCC CNAME by targeting another Proxied DNS record in your Cloudflare zone which targets the SFCC CNAME.</p>
<details class="nb-details"><summary>Correct configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4124.md")
</div></details>
<details class="nb-details"><summary>Incorrect configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4125.md")
</div></details>
<h2 id="product-compatibility">Product compatibility</h2>
<p>When a hostname within your Cloudflare zone has O2O enabled, you assume additional responsibility for the traffic on that hostname because you can now configure various Cloudflare products to affect that traffic. Some of the Cloudflare products compatible with O2O are:</p>
<ul>
<li><a href="/cache/">Caching</a></li>
<li><a href="/workers/">Workers</a></li>
<li><a href="/rules/">Rules</a></li>
</ul>
<p>For a full list of compatible products and potential limitations, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/">Product compatibility</a>.</p>
<h2 id="zone-hold">Zone hold</h2>
<p>If your own Cloudflare zone is on the Enterprise plan, you have access to the <a href="/fundamentals/account/account-security/zone-holds/">zone hold feature</a>, which is a toggle that prevents your domain name from being created as a zone in a different Cloudflare account. Additionally, if the zone hold is enabled, it prevents the activation of custom hostnames onboarded to Salesforce Commerce Cloud. Salesforce Commerce Cloud would receive the following error message for your custom hostname: <code>The hostname is associated with a held zone. Please contact the owner of this domain to have the hold removed.</code></p>
<p>To successfully activate the custom hostname on Salesforce Commerce Cloud, the owner of the zone needs to <a href="/fundamentals/account/account-security/zone-holds/#release-zone-holds">temporarily release the hold</a>. If you are only onboarding a subdomain as a custom hostname to Salesforce Commerce Cloud, only the subfeature titled <strong>Also prevent Subdomains</strong> needs to be temporarily disabled.</p>
<p>Once the zone hold is temporarily disabled, follow Salesforce Commerce Cloud's instructions to refresh the custom hostname and it should activate.</p>
<h2 id="additional-support">Additional support</h2>
<p>If you are a Salesforce Commerce Cloud customer and have set up your own Cloudflare zone with O2O enabled on specific hostnames, contact your Cloudflare Account Team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> for help resolving issues in your own zone.</p>
<p>Cloudflare will consult Salesforce Commerce Cloud if there are technical issues that Cloudflare cannot resolve.</p>
<h3 id="resolving-ssl-errors-using-cloudflare-managed-certificates">Resolving SSL errors using Cloudflare Managed Certificates</h3>
<p>If you encounter SSL errors when attempting to activate a Cloudflare Managed Certificate, verify if you have a <code>CAA</code> record on your domain name with command <code>dig +short example.com CAA</code>.</p>
<p>If you do have a <code>CAA</code> record, verify that it permits SSL certificates to be issued by the <a href="/ssl/reference/certificate-authorities/">certificate authorities supported by Cloudflare</a>.</p>
<h3 id="best-practice-zone-level-configuration">Best practice Zone-level configuration</h3>
<ol>
<li>Set <strong>Minimum TLS version</strong> to <strong>TLS 1.2</strong>
<ol>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page, scroll down to find <strong>Minimum TLS Version</strong>, and set it to <em>TLS 1.2</em>. This setting applies to every Proxied DNS record in your Zone.</li>
</ol>
</li>
<li>Match the <strong>Security Level</strong> set in <strong>SFCC Business Manager</strong>
<ol>
<li><em>Option 1: Zone-level</em> - Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/settings"><strong>Settings</strong></a> page under Security, find <strong>Security Level</strong> and set <strong>Security Level</strong> to match what is configured in <strong>SFCC Business Manager</strong>. This setting applies to every Proxied DNS record in your Cloudflare zone.</li>
<li><em>Option 2: Per Proxied DNS record</em> - If the <strong>Security Level</strong> differs between the Proxied DNS records targeting your SFCC environment and other Proxied DNS records in your Cloudflare zone, use a <strong>Configuration Rule</strong> to set the <strong>Security Level</strong> specifically for the Proxied DNS records targeting your SFCC environment. For example:
<ol>
<li>Create a new <strong>Configuration Rule</strong> on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview"><strong>Rules Overview</strong></a> page by selecting <strong>Create rule</strong> next to <strong>Configuration Rules</strong>:
<ol>
<li><strong>Rule name:</strong> <code>Match Security Level on SFCC hostnames</code></li>
<li><strong>Field:</strong> <em>Hostname</em></li>
<li><strong>Operator:</strong> <em>is in</em> (this will match against multiple hostnames specified in the <strong>Value</strong> field)</li>
<li><strong>Value:</strong> <code>www.example.com</code> <code>dev.example.com</code></li>
<li>Scroll down to <strong>Security Level</strong> and click <strong>+ Add</strong>
<ol>
<li><strong>Select Security Level:</strong> <em>Medium</em> (this should match the <strong>Security Level</strong> set in <strong>SFCC Business Manager</strong>)</li>
</ol>
</li>
<li>Scroll to the bottom of the page and click <strong>Deploy</strong></li>
</ol>
</li>
</ol>
</li>
</ol>
</li>
<li>Disable <strong>Browser Integrity Check</strong>
<ol>
<li><em>Option 1: Zone-level</em> - Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/settings"><strong>Settings</strong></a> page under Security, find <strong>Browser Integrity Check</strong> and toggle it off to disable it. This setting applies to every Proxied DNS record in your Cloudflare zone.</li>
<li><em>Option 2: Per Proxied DNS record</em> - If you want to keep <strong>Browser Integrity Check</strong> enabled for other Proxied DNS records in your Cloudflare zone but want to disable it on Proxied DNS records targeting your SFCC environment, keep the Zone-level <strong>Browser Integrity Check</strong> feature enabled and use a <strong>Configuration Rule</strong> to disable <strong>Browser Integrity Check</strong> specifically for the hostnames targeting your SFCC environment. For example:
<ol>
<li>Create a new <strong>Configuration Rule</strong> on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview"><strong>Rules Overview</strong></a> page by selecting <strong>Create rule</strong> next to <strong>Configuration Rules</strong>:
<ol>
<li><strong>Rule name:</strong> <code>Disable Browser Integrity Check on SFCC hostnames</code></li>
<li><strong>Field:</strong> <em>Hostname</em></li>
<li><strong>Operator:</strong> <em>is in</em> (this will match against multiple hostnames specified in the <strong>Value</strong> field)</li>
<li><strong>Value:</strong> <code>www.example.com</code> <code>dev.example.com</code></li>
<li>Scroll down to <strong>Browser Integrity Check</strong> and click the <strong>+ Add</strong> button:
<ol>
<li>Set the toggle to <strong>Off</strong> (a grey X will be displayed)</li>
</ol>
</li>
<li>Scroll to the bottom of the page and click <strong>Deploy</strong></li>
</ol>
</li>
</ol>
</li>
</ol>
</li>
<li>Bypass <strong>Cache</strong> on Proxied DNS records targeting your SFCC environment
<ol>
<li>Your SFCC environment, also called a <strong>Realm</strong>, will contain one to many SFCC Proxy Zones, which is where caching will always occur. In the corresponding SFCC Proxy Zone for your domain, SFCC performs their own cache optimization, so it is recommended to bypass the cache on the Proxied DNS records in your Cloudflare zone which target your SFCC environment to prevent a &quot;double caching&quot; scenario. This can be accomplished with a <strong>Cache Rule</strong>.</li>
<li>If the <strong>Cache Rule</strong> is not created, caching will occur in both your Cloudflare zone and your corresponding SFCC Proxy Zone, which can cause issues if and when the cache is invalidated or purged in your SFCC environment.
<ol>
<li>Additional information on caching in your SFCC environment can be found in <a href="https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/b2c-content-cache.html">SFCC's Content Cache Documentation</a></li>
</ol>
</li>
<li>Create a new <strong>Cache Rule</strong> on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview"><strong>Rules Overview</strong></a> page by selecting <strong>Create rule</strong> next to <strong>Cache Rules</strong>:
<ol>
<li><strong>Rule name:</strong> <code>Bypass cache on SFCC hostnames</code></li>
<li><strong>Field:</strong> <em>Hostname</em></li>
<li><strong>Operator:</strong> <em>is in</em> (this will match against multiple hostnames specified in the <strong>Value</strong> field)</li>
<li><strong>Value:</strong> <code>www.example.com</code> <code>dev.example.com</code></li>
<li><strong>Cache eligibility:</strong> Select <strong>Bypass cache</strong>.</li>
<li>Scroll to the bottom of the page and select <strong>Deploy</strong>.</li>
</ol>
</li>
</ol>
</li>
<li><em>Optional</em> - Upload your Custom Certificate from <strong>SFCC Business Manager</strong> to your Cloudflare zone:
<ol>
<li>The Custom Certificate you uploaded via <strong>SFCC Business Manager</strong> or <strong>SFCC CDN-API</strong>, which exists within your corresponding SFCC Proxy Zone, will terminate TLS connections for your SFCC storefront hostnames. Because of that, it is optional if you want to upload the same Custom Certificate to your own Cloudflare zone. Doing so will allow Cloudflare users with specific roles in your Cloudflare account to receive expiration notifications for your Custom Certificates. Please read <a href="/ssl/edge-certificates/custom-certificates/renewing/#renew-custom-certificates">renew custom certificates</a> for further details.</li>
<li>Additionally, since you now have your own Cloudflare zone, you have access to Cloudflare's various edge certificate products which means you could have more than one certificate covering the same SANs. In that scenario, a certificate priority process occurs to determine which certificate to serve at the Cloudflare edge. If you find your SFCC storefront hostnames are presenting a different certificate compared to what you uploaded via <strong>SFCC Business Manager</strong> or <strong>SFCC CDN-API</strong>, the certificate priority process is likely the reason. Please read <a href="/ssl/reference/certificate-and-hostname-priority/#certificate-deployment">certificate priority</a> for further details.</li>
</ol>
</li>
</ol>
