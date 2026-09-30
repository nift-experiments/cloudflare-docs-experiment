---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/
  description: Hide email addresses from bots while keeping them visible to visitors.
  full_title: Email Address Obfuscation · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Email Address Obfuscation · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Hide email addresses from bots while keeping them visible to visitors."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/index.md"><meta property="og:title" content="Email Address Obfuscation · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Hide email addresses from bots while keeping them visible to visitors."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/#page","headline":"Email Address Obfuscation \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Hide email addresses from bots while keeping them visible to visitors.","url":"https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/scrape-shield/email-address-obfuscation/
  schema: 1
---
<p>By enabling Cloudflare Email Address Obfuscation, email addresses on your web page will be hidden from bots, while keeping them visible to humans. In fact, there are no visible changes to your website for visitors.</p>
<h2 id="background">Background</h2>
<p>Email harvesters and other bots roam the Internet looking for email addresses to add to lists that target recipients for spam. This trend results in an increasing amount of unwanted email.</p>
<p>Web administrators have come up with clever ways to protect against this by writing out email addresses, such as <code>help [at] cloudflare [dot] com</code> or by using embedded images of the email address. However, you lose the convenience of clicking on the email address to automatically send an email. By enabling Cloudflare Email Address Obfuscation, email addresses on your web page will be obfuscated (hidden) from bots, while keeping them visible to humans. In fact, there are no visible changes to your website for visitors.</p>
<h2 id="how-it-works">How it works</h2>
<p>When Email Address Obfuscation is enabled, Cloudflare replaces visible email addresses in your HTML with links like <code>[email protected]</code>. If a visitor sees this obfuscated format, they can click the link to reveal the actual email address. This approach prevents bots from scraping email addresses while keeping them accessible to real users.</p>
<p>Cloudflare injects a small decode script (<code>email-decode.min.js</code>) into the page using the <code>defer</code> attribute. This means the script does not block page rendering. It downloads in parallel with HTML parsing and executes after the document is fully parsed. If you have custom JavaScript that interacts with obfuscated email elements, note that the decode script runs before the <code>DOMContentLoaded</code> event.</p>
<h2 id="change-email-address-obfuscation-setting">Change Email Address Obfuscation setting</h2>
<p>Cloudflare enables email address obfuscation automatically when you sign up.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15709.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15705.md")
</aside>
<h2 id="prevent-cloudflare-from-obfuscating-email">Prevent Cloudflare from obfuscating email</h2>
<p>To prevent Cloudflare from obfuscating specific email addresses, you can:</p>
<ul>
<li>Add the following comment in the page HTML code:</li>
</ul>
<pre tabindex="0"><code class="language-html">&lt;!--email_off--&gt;contact@example.com&lt;!--/email_off--&gt;&#10;</code></pre>
<ul>
<li>Return email addresses in JSON format for AJAX calls, making sure your web server returns a content type of <code>application/json</code>.</li>
<li>Disable the Email Obfuscation feature by creating a <a href="/rules/configuration-rules/">configuration rule</a> to be applied on a specific endpoint.</li>
</ul>
<hr />
<h2 id="troubleshoot-email-obfuscation">Troubleshoot email obfuscation</h2>
<p>To prevent unexpected website behavior, email addresses are not obfuscated when they appear in:</p>
<ul>
<li>Any HTML tag attribute, except for the <code>href</code> attribute of the <code>a</code> tag.</li>
<li>Other HTML tags:
<ul>
<li><code>&lt;script&gt;&lt;/script&gt;</code></li>
<li><code>&lt;noscript&gt;&lt;/noscript&gt;</code></li>
<li><code>&lt;textarea&gt;&lt;/textarea&gt;</code></li>
<li><code>&lt;xmp&gt;&lt;/xmp&gt;</code></li>
<li><code>&lt;head&gt;&lt;/head&gt;</code></li>
</ul>
</li>
<li>Any page that does not have a MIME type of <code>text/html</code> or <code>application/xhtml+xml</code>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15704.md")
</aside>
