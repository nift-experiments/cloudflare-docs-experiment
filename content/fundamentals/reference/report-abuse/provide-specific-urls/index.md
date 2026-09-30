---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/
  description: Learn how to provide specific asset URLs when submitting an abuse report.
  full_title: Providing specific URLs - Report abuse · Cloudflare Fundamentals docs
  head_html: <title>Providing specific URLs - Report abuse · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to provide specific asset URLs when submitting an abuse report."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/index.md"><meta property="og:title" content="Providing specific URLs - Report abuse · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to provide specific asset URLs when submitting an abuse report."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/#page","headline":"Providing specific URLs - Report abuse \u00b7 Cloudflare Fundamentals docs","description":"Learn how to provide specific asset URLs when submitting an abuse report.","url":"https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/report-abuse/provide-specific-urls/
  schema: 1
---
<p>If you are <a href="https://abuse.cloudflare.com">submitting an abuse report</a> to Cloudflare because our IP address appears in the WHOIS and DNS records for a website, it is very likely that the website is one of millions of websites that use our pass-through security and content distribution network (CDN) services. Because assets on the same website may be hosted by different providers, it is important that you submit the URL for that specific asset to enable appropriate action. This guide will teach you how to identify URLs for specific video or images on a webpage.</p>
<h2 id="get-the-url-for-specific-content">Get the URL for specific content</h2>
<p>To get the URL for a specific piece of content on a webpage:</p>
<ol>
<li>
<p>Open your web browser (Google Chrome, Safari, Firefox, Edge).</p>
</li>
<li>
<p>Go to the web page you want to report.</p>
</li>
<li>
<p>Right click on the content you wish to report (often a video or image).</p>
</li>
<li>
<p>Select <strong>Inspect Element</strong>.</p>
</li>
<li>
<p>In the <strong>DevTools</strong> panel, look for the <strong>src</strong> attribute in the selected the image, video, or iFrame.
<img src="/assets/upstream/images/fundamentals/get-started/identify-url.png" alt="Look for the URL in the src attribute of the video or image" /></p>
</li>
<li>
<p>Copy the URL.</p>
</li>
</ol>
<p>Providing the most specific and helpful URL enables Cloudflare to correctly identify any services it may be providing with respect to that content.</p>
<h2 id="submitting-the-abuse-report">Submitting the abuse report</h2>
<p>Once you have identified the URL for the specific asset, you can <a href="https://abuse.cloudflare.com">submit an abuse report</a> through Cloudflare's online abuse reporting process.</p>
<p>You can learn more about the process, and what you can expect from Cloudflare in response to such abuse reports, from <a href="https://www.cloudflare.com/trust-hub/reporting-abuse/">our abuse policy</a>.</p>
