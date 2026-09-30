---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/
  description: HTTP filtering in Gateway.
  full_title: Set up HTTP filtering · Cloudflare One docs
  head_html: <title>Set up HTTP filtering · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="HTTP filtering in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/index.md"><meta property="og:title" content="Set up HTTP filtering · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="HTTP filtering in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/#page","headline":"Set up HTTP filtering \u00b7 Cloudflare One docs","description":"HTTP filtering in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/get-started/http/
  schema: 1
---
<p>Secure Web Gateway allows you to inspect HTTP traffic and control which websites users can visit. DNS filtering can only block or allow entire domains (for example, all of <code>dropbox.com</code>). HTTP filtering goes deeper — it inspects full URLs and request content, so you can block a specific page like <code>dropbox.com/shared-folder</code>, scan file uploads for sensitive data, or enforce acceptable use policies based on what users are actually doing on a site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6603.md")
</aside>
<h2 id="1-connect-to-gateway"><ol>
<li>Connect to Gateway</li>
</ol></h2>
<p>HTTP filtering requires three components working together: the Cloudflare One Client routes device traffic through Cloudflare, a root certificate lets Gateway decrypt HTTPS traffic so it can inspect URLs and content, and the Gateway proxy enables Gateway to intercept and evaluate HTTP requests. Without the certificate, Gateway can only see the domain name — not the full URL or request body.</p>
<p>To filter HTTP requests from a device:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Install the Cloudflare root certificate</a> on your device.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Install the Cloudflare One Client</a> on your device.</li>
<li>In the Cloudflare One Client Settings, log in to your organization's <span class="nb-glossary-tooltip" title="team name">Cloudflare One instance</span>.</li>
<li><a href="/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy">Enable the Gateway proxy</a> for TCP. Optionally, enable the UDP proxy to also inspect QUIC traffic on port 443 — this covers HTTP/3, a newer protocol some browsers use by default.</li>
<li>To inspect HTTPS traffic, <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#turn-on-tls-decryption">enable TLS decryption</a>. TLS decryption allows Gateway to read encrypted requests. Without it, Gateway can see that a user visited <code>example.com</code> but not which specific page or what they uploaded.</li>
<li>(Optional) To scan file uploads and downloads for malware, <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">enable anti-virus scanning</a>.</li>
</ol>
<h2 id="2-verify-device-connectivity"><ol start="2">
<li>Verify device connectivity</li>
</ol></h2>
<p>To verify your device is connected to Cloudflare One and traffic is flowing through Gateway:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Under <strong>Log traffic activity</strong>, enable activity logging for all HTTP logs.</li>
<li>On your device, open a browser and go to any website.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>HTTP</strong>.</li>
<li>Make sure HTTP requests from your device appear.</li>
</ol>
<p>After creating your first HTTP policy in the next step, you can test it by visiting a URL that your policy should block and confirming the request is denied.</p>
<h2 id="3-create-your-first-http-policy"><ol start="3">
<li>Create your first HTTP policy</li>
</ol></h2>
<p>An HTTP policy defines which requests to match (for example, uploads to file-sharing sites) and the action to take (for example, block).</p>
<p>To create a new HTTP policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6607.md")
</div></div>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>
<h2 id="4-add-optional-policies"><ol start="4">
<li>Add optional policies</li>
</ol></h2>
<p>Refer to our list of <a href="/cloudflare-one/traffic-policies/http-policies/common-policies">common HTTP policies</a> for other policies you may want to create. Common additions include blocking file downloads by type, isolating risky websites in a <a href="/cloudflare-one/remote-browser-isolation/">remote browser</a>, and adding Do Not Inspect rules for applications that break under TLS decryption (for example, apps that use certificate pinning to enforce their own certificates). Do Not Inspect rules tell Gateway to skip decryption for specific destinations so those applications continue to work.</p>
