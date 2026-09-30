---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/
  description: Understand Cloudflare's video delivery policies, resolve Terms of Service redirects, and choose the right paid product for streaming video.
  full_title: Delivering Videos with Cloudflare · Cloudflare Fundamentals docs
  head_html: <title>Delivering Videos with Cloudflare · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand Cloudflare&#x27;s video delivery policies, resolve Terms of Service redirects, and choose the right paid product for streaming video."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/index.md"><meta property="og:title" content="Delivering Videos with Cloudflare · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand Cloudflare&#x27;s video delivery policies, resolve Terms of Service redirects, and choose the right paid product for streaming video."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/#page","headline":"Delivering Videos with Cloudflare \u00b7 Cloudflare Fundamentals docs","description":"Understand Cloudflare's video delivery policies, resolve Terms of Service redirects, and choose the right paid product for streaming video.","url":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/
  schema: 1
---
<h2 id="using-cloudflare-s-services">Using Cloudflare's Services</h2>
<p>Cloudflare launched in 2010 believing everyone deserves a secure, fast, reliable web presence. We did not think you should have to pay more when you came under cyber attack, so we offered free and fixed-rate pricing for websites. That worked because most websites do not consume much bandwidth, and so we could provide our services in an affordable way to everyone. From the beginning, we prohibited streaming video content using our bandwidth. While you could embed a video from another provider, we limited your ability to use our services to deliver video bits from our network to your visitors. This restriction exists because every second of a typical video requires as much bandwidth as loading a full web page.</p>
<p>Over time we recognized that some of our customers wanted to stream video using our network. To accommodate them, we developed our <a href="https://www.cloudflare.com/products/cloudflare-stream/">Stream</a> product. Stream delivers great performance at an affordable rate charged based on how much load you place on our network.</p>
<p>Unfortunately, while most people respect these limitations and understand they exist to ensure high quality of service for all Cloudflare customers, some users attempt to misconfigure our service to stream video in violation of our <a href="https://www.cloudflare.com/service-specific-terms-application-services/#content-delivery-network-free-pro-or-business">service-specific terms</a>. We want to make sure our service is great for everyone, including public service initiatives we run like <a href="https://www.cloudflare.com/galileo/">Project Galileo</a>, <a href="https://www.cloudflare.com/athenian/">The Athenian Project</a>, and <a href="https://www.cloudflare.com/fair-shot/">Project Fair Shot</a>. A handful of people misusing our service limits our ability to run these initiatives.</p>
<p>The following are some recommendations for using Cloudflare's services based on what may have brought you to this page.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cloudflare-tunnel">Cloudflare Tunnel</h3>
@markup("md", "content/.markup/bodies/9006.md")
</aside>
<hr />
<h2 id="i-m-a-website-operator-and-my-content-was-redirected-for-terms-of-service-violations">I'm a website operator and my content was redirected for Terms of Service violations</h2>
<p>If you are on a Free, Pro, or Business Plan and your application appears to be serving videos or a disproportionate amount of large files without using the appropriate paid service as described below, Cloudflare may redirect your content or take other actions to protect quality of service. When this happens, you will receive an email notification regarding Cloudflare's actions and your options.</p>
<h2 id="options-for-web-admins-to-remove-redirects">Options for web admins to remove redirects</h2>
<ul>
<li>
<p><strong>Serve redirected content from a grey-clouded sub-domain</strong></p>
</li>
<li>
<p><strong>Serve redirected content from a paid service as outlined below</strong></p>
</li>
</ul>
<h2 id="delivering-videos-with-cloudflare-using-paid-products">Delivering videos with Cloudflare using paid products</h2>
<p>Cloudflare permits the delivery of video content with specific paid services. If you are interested in serving video content, there are two recommended options.</p>
<h3 id="option-1-cloudflare-stream">Option 1: Cloudflare Stream</h3>
<p><a href="https://www.cloudflare.com/products/cloudflare-stream/">Stream</a> is a video-on-demand platform for building video applications. Stream encodes, stores, and delivers optimized video formatted for different devices and network connections.</p>
<p>To get started with Stream, visit <strong>Stream</strong> from your Dashboard or <a href="https://dash.cloudflare.com/sign-up/stream">sign up</a>. Your Stream videos are not attached to a domain in your Cloudflare account, and you do not need a domain on Cloudflare to use Stream.</p>
<h3 id="option-2-stream-delivery-enterprise-only">Option 2: Stream Delivery (Enterprise only)</h3>
<p><a href="https://www.cloudflare.com/products/stream-delivery/">Stream Delivery</a> offers caching and delivery of video content through Cloudflare data centers around the globe. This CDN feature is only available on the Cloudflare Enterprise Plan. Please <a href="https://www.cloudflare.com/products/stream-delivery/#">contact sales</a> if you'd like to explore this option.</p>
<hr />
<h2 id="getting-information-on-the-content-you-are-delivering">Getting information on the content you are delivering</h2>
<p>If you need more information about the content your zone is serving (for example, content type), you can use the following tools:</p>
<ul>
<li>Cache Analytics users: Open the <strong>Caching tab</strong> on the Dashboard to filter by content type and identify the type of traffic you are transferring.</li>
<li>Users without Cache Analytics: Open the <strong>Analytics tab</strong> on the Dashboard and select the <strong>Performance</strong> section for information about the content you are serving.</li>
</ul>
<p><img src="/assets/upstream/images/support/traffic-types.png" alt="Cache Analytics - Identify type of traffic being transferred" /></p>
<h2 id="still-have-questions-contact-support">Still have questions? Contact support</h2>
<p>If you have additional questions about redirection (e.g. if you believe your content was redirected in error and have supporting evidence), file a <a href="https://dash.cloudflare.com/redirect?account=support">support ticket</a> and include the following information:</p>
<ul>
<li>Name of your domain</li>
<li>Description of the problem</li>
<li>Description of the content you're serving through Cloudflare's network</li>
</ul>
