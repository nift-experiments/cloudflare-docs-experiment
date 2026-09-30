---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/
  description: Isolate self-hosted application in Access.
  full_title: Isolate self-hosted application · Cloudflare One docs
  head_html: <title>Isolate self-hosted application · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Isolate self-hosted application in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/index.md"><meta property="og:title" content="Isolate self-hosted application · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Isolate self-hosted application in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/#page","headline":"Isolate self-hosted application \u00b7 Cloudflare One docs","description":"Isolate self-hosted application in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/policies/isolate-application/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4585.md")
</aside>
<p>With Access policies, you can require users to open self-hosted applications in a secure <a href="/cloudflare-one/remote-browser-isolation/">remote browser</a>. Because the remote browser is directly integrated into our Secure Web Gateway platform, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> can be applied to isolated applications without needing to install the Cloudflare One Client. This allows you to distribute internal applications to unmanaged users while retaining control over sensitive data.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Your browser must <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#allow-third-party-cookies-in-the-browser">allow third-party cookies</a> on the application domain.</p>
<h2 id="enable-browser-isolation">Enable Browser Isolation</h2>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</p>
</li>
<li>
<p>Turn on <strong>Allow users to open a remote browser without the device client</strong>.</p>
</li>
<li>
<p>Go to <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Choose a <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a> and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Go to <strong>Policies</strong>.</p>
</li>
<li>
<p>Choose an <a href="/cloudflare-one/access-controls/policies/">Allow policy</a> and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Under <strong>Additional settings</strong>, turn on <strong>Isolate application</strong>.</p>
</li>
<li>
<p>Save the policy.</p>
</li>
</ol>
<p>Browser Isolation is now enabled for users who match this policy. After the user logs into Access, the application will launch in a remote browser. To confirm that the application is isolated, refer to <a href="/cloudflare-one/remote-browser-isolation/setup/#3-check-if-a-web-page-is-isolated">Check if a web page is isolated</a>.</p>
<p>You can optionally add another Allow policy for users on managed devices who do not require isolation.</p>
<h2 id="policies-for-isolated-applications">Policies for isolated applications</h2>
<p>Traffic to the isolated Access application is filtered by your Gateway <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>. Useful policies include:</p>
<ul>
<li><a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a> to allow or block requests based on user identity.</li>
<li><a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention policies</a> to log or block transmission of sensitive data.</li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Isolation policies</a> to disable browser actions such as copy/paste, printing, or file downloads.</li>
</ul>
<p>For example, if your application is hosted on <code>internal.site.com</code>, the following policy blocks users from uploading and downloading credit card numbers within the remote browser:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>internal.site.com</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><code>Financial Information</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="product-compatibility">Product compatibility</h2>
<p>For a list of products that are incompatible with the <strong>Isolate application</strong> feature, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/#product-compatibility">Product Compatibility</a> .</p>
