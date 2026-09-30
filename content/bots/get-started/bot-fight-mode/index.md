---
cp9:
  canonical: https://developers.cloudflare.com/bots/get-started/bot-fight-mode/
  description: Turn on Bot Fight Mode to challenge requests matching bot patterns on Free plans.
  full_title: Get started with Bot Fight Mode · Cloudflare bot solutions docs
  head_html: <title>Get started with Bot Fight Mode · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn on Bot Fight Mode to challenge requests matching bot patterns on Free plans."><link rel="canonical" href="https://developers.cloudflare.com/bots/get-started/bot-fight-mode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/get-started/bot-fight-mode/index.md"><meta property="og:title" content="Get started with Bot Fight Mode · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn on Bot Fight Mode to challenge requests matching bot patterns on Free plans."><meta property="og:url" content="https://developers.cloudflare.com/bots/get-started/bot-fight-mode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/get-started/bot-fight-mode/#page","headline":"Get started with Bot Fight Mode \u00b7 Cloudflare bot solutions docs","description":"Turn on Bot Fight Mode to challenge requests matching bot patterns on Free plans.","url":"https://developers.cloudflare.com/bots/get-started/bot-fight-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/get-started/bot-fight-mode/
  schema: 1
---
<p>Bot Fight Mode is a simple, free product that helps detect and mitigate bot traffic on your domain. When enabled, the product:</p>
<ul>
<li>Identifies traffic matching patterns of known bots</li>
<li>Issues computationally expensive challenges that force the requesting client to perform CPU-intensive calculations, increasing the cost for bots to send automated requests</li>
<li>Notifies <a href="https://cloudflare.com/bandwidth-alliance/">Bandwidth Alliance</a> partners (if applicable) to disable bots</li>
</ul>
<h2 id="considerations">Considerations</h2>
<p>Bot Fight Mode and Super Bot Fight Mode use the same underlying technology that powers our <a href="https://www.cloudflare.com/products/bot-management/">Bot Management</a> product. Specifically, these products:</p>
<ul>
<li>Protect entire domains without endpoint restrictions</li>
<li>Cannot be customized, adjusted, or reconfigured via WAF custom rules</li>
</ul>
<p>Although these products are designed to fight malicious actors on the Internet, they may challenge API or mobile app traffic. For more granular control, upgrade to <a href="/bots/plans/bm-subscription/">Bot Management for Enterprise</a>.</p>
<h2 id="interaction-with-other-app-security-features">Interaction with other app security features</h2>
<p>If you are using several app security features like custom rules, Managed Rules, and Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
<hr />
<h2 id="enable-bot-fight-mode">Enable Bot Fight Mode</h2>
<p>To start using Bot Fight Mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3506.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3505.md")
</aside>
<hr />
<h2 id="disable-bot-fight-mode">Disable Bot Fight Mode</h2>
<p>If you find that <strong>Bot Fight Mode</strong> is causing problems with your application traffic, you may want to disable it.</p>
<p>To disable Bot Fight Mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3507.md")
</div>
<hr />
<h2 id="block-ai-bots">Block AI bots</h2>
<p>Refer to <a href="/bots/additional-configurations/block-ai-bots/">Block AI bots</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3504.md")
</aside>
<hr />
<h2 id="visibility">Visibility</h2>
<p>You can see bot-related actions by going to <strong>Security</strong> &gt; <strong>Analytics</strong> and selecting the <strong>Events</strong> tab. Any requests challenged by this product will be labeled <strong>Bot Fight Mode</strong> in the <strong>Service</strong> field. This allows you to observe, analyze, and follow trends in your bot traffic over time.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<h3 id="rules">Rules</h3>
<p>You cannot bypass or skip Bot Fight Mode using WAF custom rules or Page Rules. This is because Bot Fight Mode does not run on the <a href="/ruleset-engine/">Ruleset Engine</a> — it operates in a separate evaluation pipeline where <em>Skip</em>, <em>Bypass</em>, and <em>Allow</em> actions have no effect.</p>
<p>If you need to create exceptions for specific traffic (for example, your own API clients or monitoring tools), use <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> instead. Super Bot Fight Mode runs on the Ruleset Engine and supports Skip rules.</p>
<p>Bot Fight Mode can still trigger if you have <a href="/waf/tools/ip-access-rules/">IP Access rules</a>, but it will not trigger if an IP Access rule matches the request first.</p>
<h3 id="javascript-detections">JavaScript Detections</h3>
<p>For Bot Fight Mode customers, <a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a> is automatically enabled and cannot be disabled.</p>
<p>If you have a <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span>, you need to take additional steps to implement JavaScript Detections:</p>
<ul>
<li>Ensure that anything under <code>/cdn-cgi/challenge-platform/</code> is allowed. Your CSP should allow scripts served from your origin domain (<code>script-src self</code>).</li>
<li>For <code>nonce</code> script tags:
<ul>
<li>
<p>If your CSP uses a <code>nonce</code> for script tags, Cloudflare will add these nonces to the scripts it injects by parsing your CSP response header.</p>
</li>
<li>
<p>If your CSP does not use <code>nonce</code> for script tags and <strong>JavaScript Detections</strong> is enabled, you may see a console error such as <code>Refused to execute inline script because it violates the following Content Security Policy directive: &quot;script-src 'self'&quot;. Either the 'unsafe-inline' keyword, a hash ('sha256-b123b8a70+4jEj+d6gWI9U6IilUJIrlnRJbRR/uQl2Jc='), or a nonce ('nonce-...') is required to enable inline execution.</code> We highly discourage the use of <code>unsafe-inline</code> and instead recommend the use CSP <code>nonces</code> in script tags which we parse and support in our CDN.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3503.md")
</aside>
