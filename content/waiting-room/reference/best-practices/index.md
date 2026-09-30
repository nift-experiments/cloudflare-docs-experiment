---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/reference/best-practices/
  description: Best practices for configuring and testing waiting rooms.
  full_title: Best practices · Cloudflare Waiting Room docs
  head_html: <title>Best practices · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="Best practices for configuring and testing waiting rooms."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/reference/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/reference/best-practices/index.md"><meta property="og:title" content="Best practices · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Best practices for configuring and testing waiting rooms."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/reference/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/reference/best-practices/#page","headline":"Best practices \u00b7 Cloudflare Waiting Room docs","description":"Best practices for configuring and testing waiting rooms.","url":"https://developers.cloudflare.com/waiting-room/reference/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/reference/best-practices/
  schema: 1
---
<p>Follow these best practices to avoid potential issues and improve the visitor experience.</p>
<h2 id="total-active-users">Total active users</h2>
<p>When specifying the <strong>Total active users</strong> in your <a href="/waiting-room/reference/configuration-settings/">configuration settings</a>, set the value to <code>75%</code> of your origin's traffic capacity.</p>
<h2 id="page-path">Page path</h2>
<p>When setting the waiting room <strong>Path</strong> in your <a href="/waiting-room/reference/configuration-settings/">configuration settings</a>, pay attention to potential subpaths. Waiting rooms are enabled on all subpaths, meaning you might be sending more traffic to your waiting room than anticipated.</p>
<p>Additionally, if you have multiple waiting rooms, the waiting room with the most specific subpath takes precedence.</p>
<h2 id="update-during-active-queueing">Update during active queueing</h2>
<h3 id="waiting-room-template">Waiting room template</h3>
<p>If you want to provide your users with updated information or expectations when they are queueing, Cloudflare recommends that you update your <a href="/waiting-room/how-to/customize-waiting-room/">waiting room template</a>. All changes will be visible to your users in close to real time.</p>
<h3 id="configuration-settings">Configuration settings</h3>
<p>When users are actively queueing, only make changes to your <a href="/waiting-room/reference/configuration-settings/">configuration settings</a> when necessary. These changes may impact the estimated wait time shown to end users, which might lead to user confusion.</p>
<h3 id="queueing-method">Queueing method</h3>
<p>Though you can change your <a href="/waiting-room/reference/queueing-methods/">queueing method</a>, it may affect users if your waiting room is actively queueing:</p>
<ul>
<li><strong>From FIFO to Random</strong>: Users will no longer be ordered based on their cookie timestamp, which may affect the displayed wait time.</li>
<li><strong>From Random to FIFO</strong>: Users will be ordered based on their cookie timestamp, meaning any new users move to the end of the FIFO queue.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15742.md")
</aside>
<h2 id="waiting-room-and-seo">Waiting Room and SEO</h2>
<p>SEO crawlers may end up in a queue during active queueing. When this happens, your sites search results and SEO may be impacted. To avoid this, you can enable SEO Crawler Bypassing from the Waiting Room dashboard or via API. SEO Crawler Bypassing ensures that trusted SEO Crawlers, verified by Bot Management, are never placed in your waiting rooms. By not being queued, SEO crawlers are always able to crawl your site, which helps maintain your SEO and search results in major search engines.</p>
<p>By enabling this service, you understand that these verified crawlers are completely bypassing your waiting rooms. No waiting room settings or features will apply to this traffic.</p>
