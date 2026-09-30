---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/
  description: File check in Zero Trust.
  full_title: File check · Cloudflare One docs
  head_html: <title>File check · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="File check in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/index.md"><meta property="og:title" content="File check · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="File check in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Posture"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/#page","headline":"File check \u00b7 Cloudflare One docs","description":"File check in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Posture"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/posture-checks/client-checks/file-check/
  schema: 1
---
<p>The File Check device posture attribute checks for the presence of a file on a device. You can create multiple file checks for each operating system you need to run it on, or if you need to check for multiple files.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="configure-a-file-check">Configure a file check</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>File Check</strong>.</p>
</li>
<li>
<p>You will be prompted for the following information:</p>
<ol>
<li><strong>Name</strong>: Enter a unique name for this device posture check.</li>
<li><strong>Operating system</strong>: Select your operating system.</li>
<li><strong>File Path</strong>: Enter a file path (for example, <code>c:\my folder\myfile.exe</code>).</li>
</ol>
</li>
</ol>
<details class="nb-details" open><summary>Environment variables</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5918.md")
</div></details>
<ol start="4">
<li>
<p><strong>Signing certificate thumbprint (recommended)</strong>: Enter the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/#determine-the-signing-thumbprint">thumbprint</a> of the publishing certificate used to sign the file. Adding this information will enable the check to ensure that the file was signed by the expected software developer.</p>
</li>
<li>
<p><strong>SHA-256 (optional)</strong>: Enter the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/#determine-the-sha-256-value">SHA-256 value</a> of the file. This is used to ensure the integrity of the file on the device.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the file check is returning the expected results.</p>
