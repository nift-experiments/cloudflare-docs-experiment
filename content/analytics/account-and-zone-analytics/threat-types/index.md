---
cp9:
  canonical: https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/
  description: Review threat categories blocked by Cloudflare.
  full_title: Threat types · Cloudflare Analytics docs
  head_html: <title>Threat types · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Review threat categories blocked by Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/index.md"><meta property="og:title" content="Threat types · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review threat categories blocked by Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/#page","headline":"Threat types \u00b7 Cloudflare Analytics docs","description":"Review threat categories blocked by Cloudflare.","url":"https://developers.cloudflare.com/analytics/account-and-zone-analytics/threat-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/account-and-zone-analytics/threat-types/
  schema: 1
---
<p>Cloudflare classifies the threats that it blocks or challenges. To help you understand more about your site’s traffic, the 'Type of Threats Mitigated' metric on the analytics page measures threats blocked or challenged by the following categories:</p>
<h2 id="bad-browser">Bad browser</h2>
<p>The source of the request was not legitimate or the request itself was malicious. Users would receive a <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/">1010 error page</a> in their browser.</p>
<p>Cloudflare's <a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a> looks for common HTTP headers abused most commonly by spammers and denies them access to your page. It will also challenge visitors that do not have a user agent or a non standard user agent (also commonly used by bots, crawlers, or visitors).</p>
<h2 id="blocked-hotlink">Blocked hotlink</h2>
<p><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a> ensures that other sites cannot use your bandwidth by building pages that link to images hosted on your origin server. This feature can be turned on and off by Cloudflare's customers.</p>
<h2 id="human-challenged">Human challenged</h2>
<p>Visitors were presented with an interactive challenge page and failed to pass.</p>
<p><em>Note: An interactive challenge page is a difficult to read word or set of numbers that only a human can translate. If entered incorrectly or not answered in a timely fashion, the request is blocked.</em></p>
<h2 id="browser-challenge">Browser challenge</h2>
<p>A bot gave an invalid answer to the JavaScript challenge (in most cases this will not happen, bots typically do not respond to the challenge at all, so &quot;failed&quot; JavaScript challenges would not get logged).</p>
<p><em>Note: During a JavaScript challenge you will be shown an interstitial page for about five seconds while Cloudflare performs a series of mathematical challenges to make sure it is a legitimate human visitor.</em></p>
<h2 id="bad-ip">Bad IP</h2>
<p>A request that came from an IP address that is not trusted by Cloudflare based on the threat score.</p>
<p>Previously, the threat score was a score from <code>0</code> (zero risk) to <code>100</code> (high risk) classifying the IP reputation of a visitor. Currently, the threat score is always <code>0</code> (zero).</p>
<h2 id="country-block">Country block</h2>
<p>Requests from countries that were blocked based on the <a href="/waf/tools/ip-access-rules/">user configuration</a> set in the WAF.</p>
<h2 id="ip-block-user">IP block (user)</h2>
<p>Requests from specific IP addresses that were blocked based on the <a href="/waf/tools/ip-access-rules/">user configuration</a> set in the WAF.</p>
<h2 id="ip-range-block-16">IP range block (/16)</h2>
<p>A /16 IP range that was blocked based on the <a href="/waf/tools/ip-access-rules/">user configuration</a> set in the WAF.</p>
<h2 id="ip-range-block-24">IP range block (/24)</h2>
<p>A /24 IP range that was blocked based on the <a href="/waf/tools/ip-access-rules/">user configuration</a> set in the WAF.</p>
<h2 id="new-challenge-user">New Challenge (user)</h2>
<p><a href="/cloudflare-challenges/">Challenge</a> based on user configurations set for visitor's IP in either WAF managed rules or custom rules, configured in <strong>Security</strong> &gt; <strong>WAF</strong>.</p>
<h2 id="challenge-error">Challenge error</h2>
<p>Requests made by a bot that failed to pass the challenge.</p>
<p><em>Note: An interactive challenge page is a difficult to read word or set of numbers that only a human can translate. If entered incorrectly or not answered in a timely fashion, the request is blocked.</em></p>
<h2 id="bot-request">Bot Request</h2>
<p>Request that came from a bot.</p>
<h2 id="unclassified">Unclassified</h2>
<p>Unclassified threats comprises a number of automatic blocks that are not related to the Browser Integrity Challenge (Bad Browser). These threats usually relate to Hotlink Protection, and other actions that happen on Cloudflare's global network based on the composition of the request (and not its content).</p>
<p>Unclassified means a number of conditions under which we group common threats related to Hotlink Protection as well as specific requests that are blocked at Cloudflare's global network before reaching your servers.</p>
