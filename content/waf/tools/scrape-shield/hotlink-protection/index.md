---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/
  description: Prevent other sites from linking to your hosted images.
  full_title: Hotlink Protection · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Hotlink Protection · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Prevent other sites from linking to your hosted images."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/index.md"><meta property="og:title" content="Hotlink Protection · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Prevent other sites from linking to your hosted images."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/#page","headline":"Hotlink Protection \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Prevent other sites from linking to your hosted images.","url":"https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/scrape-shield/hotlink-protection/
  schema: 1
---
<p>Hotlink Protection prevents your images from being used by other sites, which can reduce the bandwidth consumed by your <a href="https://www.cloudflare.com/learning/cdn/glossary/origin-server/">origin server</a>.</p>
<p>The supported file extensions are <code>gif</code>, <code>ico</code>, <code>jpg</code>, <code>jpeg</code>, and <code>png</code>.</p>
<h2 id="background">Background</h2>
<p>When Cloudflare receives an image request for your site, we check to ensure the request did not originate from visitors on another site. Visitors to your domain will still be able to download and view images.</p>
<p>Technically, this means that Hotlink Protection denies access to requests when the HTTP referer
does not include your website domain name (and is not blank).</p>
<p>Hotlink protection has no impact on crawling, but it will prevent the images from being displayed on sites such as Google images, Pinterest, and Facebook.</p>
<h2 id="enable-hotlink-protection">Enable Hotlink Protection</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15703.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15699.md")
</aside>
<h3 id="saas-providers-using-cloudflare">SaaS providers using Cloudflare</h3>
<p>If you are a SaaS provider using <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>, note that, by default, Hotlink Protection will only allow requests with your zone as referer. To avoid blocking requests from your customers (custom hostnames), consider using <a href="/rules/configuration-rules/settings/#hotlink-protection">Configuration Rules</a> or <a href="/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/">custom rules</a>.</p>
<hr />
<h2 id="allow-hotlinking-to-specific-images">Allow hotlinking to specific images</h2>
<p>You may want certain images to be hotlinked to, whether by external websites (like Google) or certain situations like when using an RSS feed.</p>
<h3 id="configuration-rules">Configuration rules</h3>
<p>To disable Hotlink Protection selectively, create a <a href="/rules/configuration-rules/">configuration rule</a> covering the path of an image folder.</p>
<h3 id="hotlink-ok-directory">hotlink-ok directory</h3>
<p>You can allow certain images to be hotlinked by placing them in a directory named <code>hotlink-ok</code>. The <code>hotlink-ok</code> directory can be placed anywhere on your website.</p>
<p>To allow another website to use <code>logo.png</code> from <code>example.com</code>, put <code>logo.png</code> in a new folder called <code>hotlink-ok</code>.</p>
<p>Some examples of URLs that will not be checked for hotlinking:</p>
<ul>
<li><code>http://example.com/hotlink-ok/pic.jpg</code></li>
<li><code>http://example.com/images/hotlink-ok/pic.jpg</code></li>
<li><code>http://example.com/hotlink-ok/images/pic.jpg</code></li>
<li><code>http://example.com/images/main-site/hotlink-ok/pic.jpg</code></li>
</ul>
