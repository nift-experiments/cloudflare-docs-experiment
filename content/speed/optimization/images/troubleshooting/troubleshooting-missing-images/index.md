---
cp9:
  canonical: https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/
  description: Fix missing or broken images after enabling image optimization.
  full_title: Troubleshoot missing images · Cloudflare Speed docs
  head_html: <title>Troubleshoot missing images · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Fix missing or broken images after enabling image optimization."><link rel="canonical" href="https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/index.md"><meta property="og:title" content="Troubleshoot missing images · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fix missing or broken images after enabling image optimization."><meta property="og:url" content="https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Speed"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/#page","headline":"Troubleshoot missing images \u00b7 Cloudflare Speed docs","description":"Fix missing or broken images after enabling image optimization.","url":"https://developers.cloudflare.com/speed/optimization/images/troubleshooting/troubleshooting-missing-images/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /speed/optimization/images/troubleshooting/troubleshooting-missing-images/
  schema: 1
---
<p>If images are missing from your website, other Cloudflare features may be interfering with those images.</p>
<p>To troubleshoot:</p>
<ol>
<li>
<p>Perform one of the following actions:</p>
<ul>
<li><a href="/cache/how-to/purge-cache">Purge cache</a> for the URL of the missing image file.</li>
<li><a href="/fundamentals/manage-domains/pause-cloudflare/">Temporarily pause Cloudflare</a>.</li>
<li>Disable <a href="/speed/optimization/content/rocket-loader/enable/">Rocket Loader</a>.</li>
</ul>
</li>
<li>
<p>Retest the image load in a private browser tab.</p>
</li>
<li>
<p>If the issue is not fixed, try another of the actions suggested in Step 1.</p>
</li>
</ol>
