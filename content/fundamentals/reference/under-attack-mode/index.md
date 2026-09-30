---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/
  description: Turn on Cloudflare Under Attack mode to mitigate layer 7 DDoS attacks by challenging suspicious visitors with an interstitial page.
  full_title: Under Attack mode · Cloudflare Fundamentals docs
  head_html: <title>Under Attack mode · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn on Cloudflare Under Attack mode to mitigate layer 7 DDoS attacks by challenging suspicious visitors with an interstitial page."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/index.md"><meta property="og:title" content="Under Attack mode · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn on Cloudflare Under Attack mode to mitigate layer 7 DDoS attacks by challenging suspicious visitors with an interstitial page."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/#page","headline":"Under Attack mode \u00b7 Cloudflare Fundamentals docs","description":"Turn on Cloudflare Under Attack mode to mitigate layer 7 DDoS attacks by challenging suspicious visitors with an interstitial page.","url":"https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/under-attack-mode/
  schema: 1
---
<p>Cloudflare's Under Attack mode performs additional security checks to help mitigate layer 7 DDoS attacks. Validated users access your website and suspicious traffic is blocked. It is designed to be used as one of the last resorts when a zone is under attack (and will temporarily pause access to your site and impact your site analytics).</p>
<p>When enabled, visitors receive an interstitial page.</p>
<h2 id="turn-on-under-attack-mode">Turn on Under Attack mode</h2>
<p>Under Attack mode is turned off by default for your zone.</p>
<h3 id="globally">Globally</h3>
<p>To put your entire zone in Under Attack mode:</p>
<ol>
<li>In the Cloudflare dashboard, select your account and zone from the <strong>Account home</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the zone overview page, turn on <strong>Under Attack Mode</strong> in the <strong>Quick Actions</strong> sidebar.</li>
</ol>
<h3 id="selectively">Selectively</h3>
<p>To enable Under Attack mode for specific pages or sections of your site, use a <a href="/rules/configuration-rules/">configuration rule</a> to adjust the <strong>Security Level</strong>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/8770.md")
</div>
<p>To turn it on for specific ASNs (hosts/ISPs that own IP addresses), countries, or IP ranges, use <a href="/waf/tools/ip-access-rules/">IP Access Rules</a>.</p>
<hr />
<h2 id="preview-under-attack-mode">Preview Under Attack mode</h2>
<p>To preview what Under Attack mode looks like for your visitors:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configurations</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Custom Pages</strong>.</li>
<li>For <strong>Managed Challenge / I'm Under Attack Mode™</strong>, select <strong>Custom Pages</strong> &gt; <strong>View default</strong>.</li>
</ol>
<p>The <code>Checking your browser before accessing...</code> challenge determines whether to block or allow a visitor within five seconds. After passing the challenge, the visitor does not observe another challenge until the duration configured in <a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Challenge Passage</a>.</p>
<hr />
<h2 id="potential-issues">Potential issues</h2>
<p>Since the Under Attack mode requires your browser to support JavaScript to display and pass the interstitial page, it is expected to observe impact on third party analytics tools.</p>
