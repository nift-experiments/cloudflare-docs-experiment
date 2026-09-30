---
cp9:
  canonical: https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/
  description: Use Cloudflare with vBulletin, Xenforo, and other forums.
  full_title: Using Cloudflare with various forums · Cloudflare Support docs
  head_html: <title>Using Cloudflare with various forums · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare with vBulletin, Xenforo, and other forums."><link rel="canonical" href="https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/index.md"><meta property="og:title" content="Using Cloudflare with various forums · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare with vBulletin, Xenforo, and other forums."><meta property="og:url" content="https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/#page","headline":"Using Cloudflare with various forums \u00b7 Cloudflare Support docs","description":"Use Cloudflare with vBulletin, Xenforo, and other forums.","url":"https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>Many widely used forum platforms are compatible with Cloudflare.</p>
<p>These include:</p>
<ul>
<li><a href="https://community.cloudflare.com/t/using-discourse-with-cloudflare-best-practices/602890">Discourse</a></li>
<li>vBulletin</li>
<li>Xenforo</li>
<li>MyBB</li>
</ul>
<p>If you have a forum using these platforms, you can increase its speed and safety by adding Cloudflare.</p>
<hr />
<h2 id="steps">Steps</h2>
<p><strong>1</strong>. Cloudflare acts as a reverse proxy, meaning that all visitor IP addresses will become Cloudflare-affiliated IP addresses. If you are using services like <strong>Stopforumspan</strong> or blocking registration by IP address, you need to <a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">restore original visitor IPs</a>.</p>
<p><strong>2</strong>. To prevent admin functions from being affected by caching or performance features, create a <a href="/cache/how-to/cache-rules/settings/#bypass-cache">Cache Rule</a> to bypass cache on the admin section of your site.</p>
<p><strong>3</strong>. If you want certain services to access your website (APIs or certain IPs), <a href="/waf/">configure the WAF</a>.</p>
<p><strong>4</strong>. Review your DNS records to make sure all your subdomain records are present. If you cannot find a subdomain, <a href="/dns/manage-dns-records/how-to/create-dns-records/">add the DNS record</a>.</p>
