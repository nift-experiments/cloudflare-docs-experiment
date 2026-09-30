---
cp9:
  canonical: https://developers.cloudflare.com/china-network/concepts/global-acceleration/
  description: Simplify global asset deployment in China with connectivity from CMI, CBC Tech, and JD Cloud.
  full_title: Global Acceleration · Cloudflare China Network docs
  head_html: <title>Global Acceleration · Cloudflare China Network docs</title><meta name="generator" content="Nift"><meta name="description" content="Simplify global asset deployment in China with connectivity from CMI, CBC Tech, and JD Cloud."><link rel="canonical" href="https://developers.cloudflare.com/china-network/concepts/global-acceleration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/china-network/concepts/global-acceleration/index.md"><meta property="og:title" content="Global Acceleration · Cloudflare China Network docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Simplify global asset deployment in China with connectivity from CMI, CBC Tech, and JD Cloud."><meta property="og:url" content="https://developers.cloudflare.com/china-network/concepts/global-acceleration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="China Network"><meta name="algolia_product_filter" content="China Network"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="China Network"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/china-network/concepts/global-acceleration/#page","headline":"Global Acceleration \u00b7 Cloudflare China Network docs","description":"Simplify global asset deployment in China with connectivity from CMI, CBC Tech, and JD Cloud.","url":"https://developers.cloudflare.com/china-network/concepts/global-acceleration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /china-network/concepts/global-acceleration/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3954.md")
</aside>
<p>Organizations that serve content or connect employees in Mainland China face connectivity challenges due to China's network infrastructure and regulatory requirements. Global Acceleration is a suite of connectivity offerings that address these challenges by providing optimized network paths into and out of China. Global Acceleration is provided by Cloudflare's partners including China Mobile International (CMI), CBC Tech, and JD Cloud.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/18457868eb13222051618b0d138e0225/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F2093e8e7-2720-4595-0a4c-5e57ba67bd00%2Fpublic" title="Global Acceleration" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div><details class="nb-details video-chapters"><summary>Chapters</summary><ul><li><button type="button" data-video-time="17"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/18457868eb13222051618b0d138e0225/thumbnails/thumbnail.jpg?fit=crop&amp;time=17s" alt="Introduction"><strong>Introduction</strong><span>17s</span></button></li><li><button type="button" data-video-time="38"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/18457868eb13222051618b0d138e0225/thumbnails/thumbnail.jpg?fit=crop&amp;time=38s" alt="Dynamic content outside of Mainland China"><strong>Dynamic content outside of Mainland China</strong><span>38s</span></button></li><li><button type="button" data-video-time="103"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/18457868eb13222051618b0d138e0225/thumbnails/thumbnail.jpg?fit=crop&amp;time=103s" alt="Access to global services"><strong>Access to global services</strong><span>1m43s</span></button></li><li><button type="button" data-video-time="174"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/18457868eb13222051618b0d138e0225/thumbnails/thumbnail.jpg?fit=crop&amp;time=174s" alt="Private network connectivity"><strong>Private network connectivity</strong><span>2m54s</span></button></li><li><button type="button" data-video-time="223"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/18457868eb13222051618b0d138e0225/thumbnails/thumbnail.jpg?fit=crop&amp;time=223s" alt="Summary"><strong>Summary</strong><span>3m43s</span></button></li></ul></details>
<p>Global Acceleration can support the following scenarios:</p>
<table>
<thead>
<tr>
<th>Service</th>
<th>Scenario</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#cdn-global-acceleration">CDN Global Acceleration</a></td>
<td>Improved performance for dynamic content (API responses, personalized pages) on China Network CDN.</td>
</tr>
<tr>
<td><a href="#cloudflare-one-client-global-acceleration">Cloudflare One Client Global Acceleration</a></td>
<td>Cloudflare One Client used in Mainland China.</td>
</tr>
<tr>
<td><a href="#cloudflare-wan-global-acceleration">Cloudflare WAN Global Acceleration</a></td>
<td>Cloudflare WAN used in Mainland China.</td>
</tr>
<tr>
<td><a href="#icp-services">ICP</a></td>
<td>China Network prerequisite.</td>
</tr>
<tr>
<td><a href="#mlps-services">MLPS</a></td>
<td>China cybersecurity compliance certification.</td>
</tr>
<tr>
<td><a href="#travel-sim">Travel SIM</a></td>
<td>Temporary Cloudflare One Client access for employees traveling to Mainland China.</td>
</tr>
</tbody>
</table>
<h2 id="cdn-global-acceleration">CDN Global Acceleration</h2>
<p>CDN Global Acceleration provides stable and reliable connections for dynamic content — such as API responses and personalized pages — entering and exiting China, improving performance for users within the country.</p>
<h2 id="cloudflare-one-client-global-acceleration">Cloudflare One Client Global Acceleration</h2>
<p>Cloudflare One Client Global Acceleration (formerly WARP Global Acceleration) enables <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> access within China, allowing remote employees to maintain secure and consistent connections.</p>
<h2 id="cloudflare-wan-global-acceleration">Cloudflare WAN Global Acceleration</h2>
<p>Cloudflare WAN Global Acceleration (formerly Magic WAN Global Acceleration) enables <a href="/cloudflare-wan/">Cloudflare WAN</a> access within China, allowing in-office employees to maintain secure and reliable connectivity.</p>
<h2 id="icp-services">ICP services</h2>
<p>The Internet Content Provider (ICP) service simplifies the process of acquiring an <a href="/china-network/concepts/icp/">ICP filing or license</a> for your domains. An ICP is a regulatory requirement for all websites operating in Mainland China.</p>
<h2 id="mlps-services">MLPS services</h2>
<p>The Multi-Level Protection Scheme (MLPS) service add-on streamlines the process of obtaining MLPS Level 3 certification, a China cybersecurity compliance standard required for certain applications handling sensitive data.</p>
<h2 id="travel-sim">Travel SIM</h2>
<p>Travel SIM offers temporary, seamless Cloudflare One Client access for individual employees traveling to China, ensuring uninterrupted connectivity during their visit.</p>
<hr />
<h2 id="general-process">General process</h2>
<h3 id="1-validate-prerequisites"><ol>
<li>Validate prerequisites</li>
</ol></h3>
<p>Ensure that you have a Cloudflare <a href="https://www.cloudflare.com/plans/enterprise/">Enterprise plan</a> and <a href="/china-network/">China Network</a>, if you want CDN Global Acceleration. Cloudflare One Client and Cloudflare WAN entitlements are required for Cloudflare One Client Connection or Cloudflare WAN Global Acceleration.</p>
<h3 id="2-sign-contract"><ol start="2">
<li>Sign contract</li>
</ol></h3>
<p>Contact your Cloudflare account team. They will assist you with contracting with us, or our local China partners, depending on the service.</p>
<h3 id="3-deploy-global-acceleration"><ol start="3">
<li>Deploy Global Acceleration</li>
</ol></h3>
<p>Our local China partners will assist you to deploy Global Acceleration.</p>
