---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/tanium/
  description: Tanium (legacy) in Zero Trust.
  full_title: Integrate Tanium with Access · Cloudflare One docs
  head_html: <title>Integrate Tanium with Access · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Tanium (legacy) in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/tanium/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/tanium/index.md"><meta property="og:title" content="Integrate Tanium with Access · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Tanium (legacy) in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/tanium/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/tanium/#page","headline":"Integrate Tanium with Access \u00b7 Cloudflare One docs","description":"Tanium (legacy) in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/tanium/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/tanium/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5908.md")
</aside>
<p>Cloudflare Access can use endpoint data from <a href="https://www.tanium.com/">Tanium™</a> to determine if a request should be allowed to reach a protected resource. When users attempt to connect to a resource protected by Access with a Tanium rule, Cloudflare Access will validate the user's identity, and the browser will connect to the Tanium agent before making a decision to grant access.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="gateway-policy-limitation">Gateway policy limitation</h3>
@markup("md", "content/.markup/bodies/5907.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Tanium Core Platform version 7.2 or later</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/access-integrations/">Access integrations</a>.</p>
<h2 id="integrate-tanium-with-cloudflare-access">Integrate Tanium with Cloudflare Access</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5906.md")
</aside>
<ol>
<li>
<p>Configure your Tanium deployment using the <a href="https://docs.tanium.com/endpoint_identity/endpoint_identity/userguide.html">step-by-step documentation</a> provided. You will need the public key to integrate your Tanium deployment with Cloudflare Access.</p>
</li>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>Tanium</strong> from the list of providers.</p>
</li>
<li>
<p>Enter any <strong>Name</strong> for the integration.</p>
</li>
<li>
<p>For <strong>Port</strong>, enter <code>17472</code>.</p>
<p>This is the default port used by the Tanium endpoints to communicate inbound and outbound with Cloudflare Access. You may need to modify it to reflect your organization's deployment.</p>
</li>
<li>
<p>Input the public certificate generated in Step 1.</p>
<p>Adding the certificate allows Cloudflare to validate that the response from the Tanium agent is valid.</p>
</li>
</ol>
<p>You can now build <a href="/cloudflare-one/access-controls/policies/">Access policies</a> that check <a href="#tanium-endpoint-signals">device posture signals</a> from the Tanium endpoint.</p>
<h2 id="example-access-policy">Example Access policy</h2>
<p>This example will only grant access to users who are part of your team's email domain and running the Tanium agent.</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Include</td>
<td>Emails Ending in</td>
<td><code>@team.com</code></td>
</tr>
<tr>
<td></td>
<td>Require</td>
<td>Device Posture - Tanium</td>
<td><code>Managed</code></td>
</tr>
</tbody>
</table>
<p>The Tanium rule will require that the device connecting is managed in your Tanium deployment and has checked into the Tanium server in the last 7 days.</p>
<h2 id="tanium-endpoint-signals">Tanium endpoint signals</h2>
<table>
<thead>
<tr>
<th>Signal</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Managed</td>
<td>Boolean</td>
<td>Validates that the device is managed in your organization's Tanium account.</td>
</tr>
</tbody>
</table>
