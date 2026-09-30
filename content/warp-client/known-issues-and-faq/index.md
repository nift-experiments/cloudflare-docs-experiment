---
cp9:
  canonical: https://developers.cloudflare.com/warp-client/known-issues-and-faq/
  description: Known issues and answers to common WARP client questions.
  full_title: FAQ · Cloudflare WARP client docs
  head_html: <title>FAQ · Cloudflare WARP client docs</title><meta name="generator" content="Nift"><meta name="description" content="Known issues and answers to common WARP client questions."><link rel="canonical" href="https://developers.cloudflare.com/warp-client/known-issues-and-faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/warp-client/known-issues-and-faq/index.md"><meta property="og:title" content="FAQ · Cloudflare WARP client docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Known issues and answers to common WARP client questions."><meta property="og:url" content="https://developers.cloudflare.com/warp-client/known-issues-and-faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WARP Client"><meta name="algolia_product_filter" content="WARP Client"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="WARP Client"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/warp-client/known-issues-and-faq/#page","headline":"FAQ \u00b7 Cloudflare WARP client docs","description":"Known issues and answers to common WARP client questions.","url":"https://developers.cloudflare.com/warp-client/known-issues-and-faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /warp-client/known-issues-and-faq/
  schema: 1
---
<p>Below you will find answers to our most commonly asked questions regarding the WARP client. If you cannot find the answer you are looking for, refer to the <a href="https://community.cloudflare.com/">community page</a> to explore more resources.</p>
<h2 id="why-am-i-not-connecting-to-a-closer-cloudflare-data-center">Why am I not connecting to a closer Cloudflare data center?</h2>
<p>As our <a href="https://www.cloudflare.com/network/">Network Map</a> shows, we have locations all over the globe. However, in the Advanced Connection stats of our application, you may notice that the server you are connecting to is not necessarily the one physically closest to your location. This can be due to a number of reasons:</p>
<ul>
<li>We work hard to prevent it, but sometimes your nearest server might be having problems. <a href="https://www.cloudflarestatus.com/?_ga=2.155811579.1117044671.1600983837-1079355427.1599074097">Check the system status</a> for more information.</li>
<li>Your Internet provider may choose to route traffic along an alternate path for reasons such as cost savings, reliability, or other infrastructure concerns.</li>
<li>Not all Cloudflare locations are WARP enabled. We are constantly evaluating performance and how users are connecting, bringing more servers online with WARP all the time.</li>
</ul>
<h2 id="does-warp-reveal-my-ip-address-to-websites-i-visit">Does WARP reveal my IP address to websites I visit?</h2>
<p>No. 1.1.1.1 + WARP replaces your original IP address with a Cloudflare IP that consistently and accurately represents your approximate location. This happens regardless of whether the site is on the Cloudflare network or not. Refer to our <a href="https://blog.cloudflare.com/geoexit-improving-warp-user-experience-larger-network/">blog post</a> for more information on this topic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/106.md")
</aside>
<h2 id="why-has-my-throughput-dropped-while-using-warp">Why has my throughput dropped while using WARP?</h2>
<p>Cloudflare WARP is in part powered by <a href="/1.1.1.1/">1.1.1.1</a>, the world's fastest DNS resolver. When visiting sites or going to a new location on the Internet, you should see fast DNS lookups. WARP, however, is built to trade some throughput for enhanced privacy, by encrypting all traffic both to and from your device. While this is not noticeable at most mobile speeds, on desktop systems in countries where high-speed broadband is available, you may notice a drop. We think the tradeoff is worth it and continue to work on improving performance all over the system.</p>
<h2 id="what-about-the-performance-of-the-warp-app">What about the performance of the WARP app?</h2>
<p>Cloudflare WARP and the 1.1.1.1 with WARP applications go through performance testing that includes battery, network and CPU on a regular basis. In addition, both applications are used by millions of users worldwide that help us stay on top of issues across a wide variety of devices, networks, sites and applications.</p>
<h2 id="what-is-the-version-of-net-framework-required-for-the-windows-client">What is the version of .NET Framework required for the Windows client?</h2>
<p>The WARP client for Windows requires .NET Framework version 4.7.2 or later to be installed on your computer.</p>
<h2 id="known-issues">Known issues</h2>
<ul>
<li>
<p>Applications or sites that rely on location information to enforce content licensing agreements (for example, certain games, video streaming, music streaming, or radio streaming) may not function properly. We are working on a product update that will allow these clients to work, by not sending their traffic through WARP.</p>
</li>
<li>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/">Known Limitations</a> for information on devices, software, and configurations that are incompatible with Cloudflare WARP.</p>
</li>
<li>
<p>WARP does not proxy WebRTC traffic. Applications or sites that have access to your microphone or camera, such as for live video calls or online gaming, will bypass WARP. As a result, your IP address will be visible to these websites.</p>
</li>
</ul>
