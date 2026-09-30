---
cp9:
  canonical: https://developers.cloudflare.com/speed/aim/
  description: Measure real-world internet quality metrics for your visitors.
  full_title: Aggregated Internet Measurement · Cloudflare Speed docs
  head_html: <title>Aggregated Internet Measurement · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Measure real-world internet quality metrics for your visitors."><link rel="canonical" href="https://developers.cloudflare.com/speed/aim/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/aim/index.md"><meta property="og:title" content="Aggregated Internet Measurement · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Measure real-world internet quality metrics for your visitors."><meta property="og:url" content="https://developers.cloudflare.com/speed/aim/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/aim/#page","headline":"Aggregated Internet Measurement \u00b7 Cloudflare Speed docs","description":"Measure real-world internet quality metrics for your visitors.","url":"https://developers.cloudflare.com/speed/aim/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/aim/
  schema: 1
---
<p>Aggregated Internet Measurement (AIM) helps you understand your Internet quality to identify scenarios that your Internet connection is good or bad for. Typically, an Internet speed test provides you with upload and download speeds, which may not always provide a holistic view of your Internet quality.</p>
<p>AIM uses a scoring rubric that assigns point values based on speed tests to help you understand how your Internet quality will perform for streaming, gaming, and webchat/real-time communication (RTC).</p>
<h2 id="scoring-rubric">Scoring Rubric</h2>
<p>AIM analyzes the following metrics to generate your score:</p>
<ul>
<li>Latency</li>
<li>Packet Loss</li>
<li>Download</li>
<li>Upload</li>
<li>Loaded Latency</li>
<li>Jitter</li>
</ul>
<p>After the test is run and a point value is assigned to each metric, the points are translated to a network score for streaming, gaming, and webchat/RTC.  These scores will indicate how good your Internet is in each of these scenarios.</p>
<p>The possible network scores are:</p>
<ul>
<li>Bad</li>
<li>Poor</li>
<li>Average</li>
<li>Good</li>
<li>Great</li>
</ul>
<h2 id="improve-your-network-score">Improve your network score</h2>
<p>You have a few options to help improve network scores.</p>
<ul>
<li><strong>Switch to a wired connection.</strong> When possible, switch to a wired connection instead of wireless to avoid performance issues due to radio interference and signal strength.</li>
<li><strong>Move closer to your router.</strong> If you are unable to use a wired connection, try to move closer to your wireless router. Signal strength drops as you move away from your wireless router and a weaker signal means poorer connectivity. Keep in mind that any objects or materials between you and your wireless router can also have a negative impact on signal strength.</li>
<li><strong>Upgrade your router.</strong> Ensure you are using a router capable of handling smarter queueing with hardware that will not fall over under load.</li>
<li><strong>Contact your ISP.</strong> If you’re using a wired connection or have a good connection to your wireless router and are still seeing issues, you may have issues with your Internet connection and should reach out to your ISP.</li>
</ul>
