---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/block-page/
  description: Set up custom Gateway block pages.
  full_title: Gateway block page · Cloudflare Learning Paths
  head_html: <title>Gateway block page · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Set up custom Gateway block pages."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/block-page/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/block-page/index.md"><meta property="og:title" content="Gateway block page · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up custom Gateway block pages."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/block-page/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/block-page/#page","headline":"Gateway block page \u00b7 Cloudflare Learning Paths","description":"Set up custom Gateway block pages.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/build-policies/block-page/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/build-policies/block-page/
  schema: 1
---
<p>With Cloudflare Zero Trust, you can deliver actionable feedback to users when they are blocked by a Gateway policy. Custom block messages can reduce user confusion and decrease your IT ticket load.</p>
<p>There are two different ways to surface block messages:</p>
<ul>
<li><a href="#custom-block-page">Custom block page</a></li>
<li><a href="#cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</a></li>
</ul>
<h2 id="custom-block-page">Custom block page</h2>
<p>You can display a custom block page in the browser when users are blocked by a Gateway DNS or HTTP policy. This is a static page that educates users on why they were blocked and how to contact IT.</p>
<p>The custom block page has a few drawbacks:</p>
<ul>
<li>To display the block page, you must install a <a href="/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/#configure-user-side-certificates">user-side certificate</a> on the end user device.</li>
<li>The block page does not appear when users are blocked by a Gateway network policy.</li>
<li>The custom block page only displays when the user loads a site in a browser. If, for instance, the user is allowed to visit a site but not allowed to upload a file, the file upload would fail silently and the user would not get a block page.</li>
</ul>
<p>To work around these limitations, we recommend using <a href="#cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9991.md")
</aside>
<h3 id="enable-the-block-page-for-dns-policies">Enable the block page for DNS policies</h3>
<p>For DNS policies, you will need to enable the block page on a per-policy basis.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9994.md")
</div></div>
<h3 id="customize-the-block-page">Customize the block page</h3>
<p>You can customize the Cloudflare-hosted block page by making global changes that Gateway will display every time a user reaches your block page. Customizations will apply regardless of the type of policy (DNS or HTTP) that blocks the traffic.</p>
<p>To customize your block page:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9997.md")
</div></div>
<p>Gateway will now display a custom Gateway block page when your users visit a blocked website.</p>
<h2 id="cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9990.md")
</aside>
<p>For more granular user feedback, you can enable Cloudflare One Client block notifications on any Gateway DNS or Network <em>Block</em> policy. Blocked users will receive an operating system notification from the Cloudflare One Client with a custom message you set.</p>
<p>Client notifications provide additional functionality over the <a href="#custom-block-page">custom block page</a>:</p>
<ul>
<li>
<p>Client notifications work with network policies, which means you can surface feedback for all partial actions on user traffic including blocking a specific port, file upload, or protocol.</p>
</li>
<li>
<p>Client notifications allow you to direct users to a unique link per individual policy. For example, you could link users to your organization's acceptable use policy, data protection policy, or any existing IT troubleshooting infrastructure. If no infrastructure for this exists within your organization, you can quickly deploy an HTML site on <a href="/pages/">Cloudflare Pages</a>, put the site behind a <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policy</a>, and provide dynamic feedback based on the identity and device posture values found in the user's <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">Access JWT</a>.</p>
</li>
</ul>
