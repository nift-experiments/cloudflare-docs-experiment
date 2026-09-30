---
cp9:
  canonical: https://developers.cloudflare.com/automatic-platform-optimization/troubleshooting/
  description: Resolve common APO issues including plugin detection and stale content.
  full_title: Troubleshooting · Cloudflare Automatic Platform Optimization docs
  head_html: <title>Troubleshooting · Cloudflare Automatic Platform Optimization docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common APO issues including plugin detection and stale content."><link rel="canonical" href="https://developers.cloudflare.com/automatic-platform-optimization/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/automatic-platform-optimization/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare Automatic Platform Optimization docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common APO issues including plugin detection and stale content."><meta property="og:url" content="https://developers.cloudflare.com/automatic-platform-optimization/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Automatic Platform Optimization"><meta name="algolia_product_filter" content="Automatic Platform Optimization"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Automatic Platform Optimization"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/automatic-platform-optimization/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare Automatic Platform Optimization docs","description":"Resolve common APO issues including plugin detection and stale content.","url":"https://developers.cloudflare.com/automatic-platform-optimization/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /automatic-platform-optimization/troubleshooting/
  schema: 1
---
<h2 id="wordpress-plugin-is-undetected-on-cloudflare-dashboard">WordPress plugin is undetected on Cloudflare dashboard</h2>
<p>The WordPress plugin may go undetected on your Cloudflare dashboard for a few reasons.</p>
<ul>
<li>Versions older than 3.8.2 of the WordPress plugin are installed.
<ul>
<li><strong>Solution:</strong> Install version 4.4.0 of the WordPress plugin.</li>
</ul>
</li>
<li>Version 3.8.2 of the plugin is installed but existing cache plugins return stale responses, for example, without <code>cf-edge-cache</code> header.
<ul>
<li><strong>Solution:</strong> Enable APO from the WordPress plugin and purge the cache in the existing cache plugins.</li>
</ul>
</li>
<li>WordPress only runs on a subdomain, but WordPress and the WordPress plugin check against the apex domain.
<ul>
<li><strong>Solution:</strong> For additional information, see <a href="/automatic-platform-optimization/reference/subdomain-subdirectories/">Subdomains and subdirectories</a></li>
</ul>
</li>
</ul>
<p>If your Cloudflare dashboard cannot detect the WordPress plugin after trying the solutions above, ensure you completed all of the steps listed in <a href="/automatic-platform-optimization/get-started/activate-cf-wp-plugin/">Activate the Cloudflare WordPress plugin</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3340.md")
</aside>
<h2 id="wordpress-returns-stale-content">WordPress returns stale content</h2>
<p>If WordPress is returning stale content, <a href="/cache/how-to/purge-cache/">purge the cache</a> when APO is enabled.</p>
