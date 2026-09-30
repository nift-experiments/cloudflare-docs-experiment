---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/
  description: SentinelOne in Zero Trust.
  full_title: SentinelOne - Cloudflare One Client checks · Cloudflare One docs
  head_html: <title>SentinelOne - Cloudflare One Client checks · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="SentinelOne in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/index.md"><meta property="og:title" content="SentinelOne - Cloudflare One Client checks · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="SentinelOne in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture,SentinelOne"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/#page","headline":"SentinelOne - Cloudflare One Client checks \u00b7 Cloudflare One docs","description":"SentinelOne in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture","SentinelOne"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/sentinel-one/
  schema: 1
---
<p>Cloudflare One can check if <a href="https://www.sentinelone.com/">SentinelOne</a> is running on a device to determine if a request should be allowed to reach a protected resource.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>SentinelOne agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="configure-the-sentinelone-check">Configure the SentinelOne check</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>SentinelOne</strong>.</p>
</li>
<li>
<p>You will be prompted for the following information:</p>
<ol>
<li><strong>Name</strong>: Enter a unique name for this device posture check.</li>
<li><strong>Operating system</strong>: Select your operating system. You will need to configure one posture check per operating system.</li>
<li><strong>Application Path</strong>: Enter the full path to the SentinelOne process to be checked (for example, <code>C:\Program Files\SentinelOne\Sentinel Agent 21.7.4.1043\SentinelAgent.exe</code>).</li>
</ol>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5909.md")
</aside>
<ol start="4">
<li><strong>Signing certificate thumbprint (recommended)</strong>: Enter the thumbprint of the publishing certificate used to sign the binary. This proves the binary came from SentinelOne and is the recommended way to validate the process.</li>
<li><strong>SHA-256 (optional)</strong>: Enter a SHA-256 value. This is used to validate the SHA256 signature of the binary and ensures the integrity of the binary file on the device. Note: do not fill out this field unless you strictly control updates to SentinelOne, as this will change between versions.</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the SentinelOne check is returning the expected results.</p>
