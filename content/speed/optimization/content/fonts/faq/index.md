---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/content/fonts/faq/
  description: Read FAQs about Cloudflare Fonts
  full_title: FAQ · Cloudflare Speed docs
  head_html: <title>FAQ · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Read FAQs about Cloudflare Fonts"><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/content/fonts/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/content/fonts/faq/index.md"><meta property="og:title" content="FAQ · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Read FAQs about Cloudflare Fonts"><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/content/fonts/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/content/fonts/faq/#page","headline":"FAQ \u00b7 Cloudflare Speed docs","description":"Read FAQs about Cloudflare Fonts","url":"https://developers.cloudflare.com/speed/optimization/content/fonts/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/content/fonts/faq/
  schema: 1
---
<p>In the following sections, you can find frequently asked questions about performance, privacy, security, implementation and integration.</p>
<h2 id="performance">Performance</h2>
<h3 id="how-does-cloudflare-fonts-improve-website-performance">How does Cloudflare Fonts improve website performance?</h3>
<p>By serving fonts from your own domain through Cloudflare's optimized infrastructure, Cloudflare Fonts reduces DNS lookups, TLS connection setups and latency. This leads to faster page load times, enhancing the overall performance of your website.</p>
<h2 id="privacy-and-security">Privacy and security</h2>
<h3 id="does-cloudflare-fonts-collect-or-log-user-data">Does Cloudflare Fonts collect or log user data?</h3>
<p>No, Cloudflare Fonts does not collect or log user data during the font delivery process. Cloudflare is committed to a <a href="https://www.cloudflare.com/privacypolicy/">privacy-first</a> approach, ensuring that your users' data remains confidential.</p>
<h2 id="implementation-and-integration">Implementation and integration</h2>
<h3 id="do-i-need-to-host-my-font-files-separately-when-using-cloudflare-fonts">Do I need to host my font files separately when using Cloudflare Fonts?</h3>
<p>No, Cloudflare Fonts simplifies the font delivery process. You do not need to host font files separately. The service works by rewriting the webpage’s HTML. It removes Google Fonts links and replaces them with inline CSS.</p>
<h3 id="are-there-any-code-changes-required-to-use-cloudflare-fonts">Are there any code changes required to use Cloudflare Fonts?</h3>
<p>No, you do not need any code changes to use Cloudflare Fonts.</p>
<h3 id="can-i-see-analytics-of-font-files-served-via-cloudflare-fonts">Can I see analytics of font files served via Cloudflare Fonts?</h3>
<p>Yes, as Cloudflare will be serving these fonts via your zone, analytics will appear within your Cloudflare dashboard. This allows you to analyze requests for font files that you would not have otherwise known about without Cloudflare Fonts.</p>
<h3 id="which-path-are-cloudflare-fonts-requests-made-to">Which path are Cloudflare Fonts requests made to?</h3>
<p>Font requests will be made to your origin with the <code>/cf-fonts/</code> path prefix.</p>
<h3 id="what-other-transformations-are-made">What other transformations are made?</h3>
<p>Cloudflare will strip any preconnect headers for Google Fonts domains from the HTML response body. This will improve performance by removing unnecessary connections.</p>
