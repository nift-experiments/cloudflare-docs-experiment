---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/
  description: Require Gateway in Zero Trust.
  full_title: Require Gateway · Cloudflare One docs
  head_html: <title>Require Gateway · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Require Gateway in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/index.md"><meta property="og:title" content="Require Gateway · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Require Gateway in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/#page","headline":"Require Gateway \u00b7 Cloudflare One docs","description":"Require Gateway in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/
  schema: 1
---
<p>With Require Gateway, you can allow access to your applications only to devices enrolled in your Zero Trust organization. Unlike <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/">Require WARP</a>, which will check for any WARP instance (including the consumer version), Require Gateway will only allow requests coming from devices whose traffic is filtered by your organization's Cloudflare Gateway configuration. This policy is best used when you want to protect company-owned assets by only allowing access to employees.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="1-enable-the-gateway-check"><ol>
<li>Enable the Gateway check</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>Gateway</strong>, then select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="2-add-the-check-to-an-access-application"><ol start="2">
<li>Add the check to an Access application</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Locate the application for which you want to require Gateway. Select <strong>Configure</strong>.</p>
</li>
<li>
<p>In the <strong>Policies</strong> tab, create a new Access policy or edit an existing policy.</p>
</li>
<li>
<p>In the policy builder, add an Include or Require rule which uses the <em>Gateway</em> selector. Save the policy.</p>
</li>
<li>
<p>Save the Access application.</p>
</li>
</ol>
<p>Before granting access to the application, the policy will check that the device is running the Cloudflare One Client and enrolled in your Zero Trust organization.</p>
