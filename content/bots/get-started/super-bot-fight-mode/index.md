---
cp9:
  canonical: https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/
  description: Configure Super Bot Fight Mode to challenge or block bots on Pro, Business, and Enterprise plans.
  full_title: Get started with Super Bot Fight Mode · Cloudflare bot solutions docs
  head_html: <title>Get started with Super Bot Fight Mode · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Super Bot Fight Mode to challenge or block bots on Pro, Business, and Enterprise plans."><link rel="canonical" href="https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/index.md"><meta property="og:title" content="Get started with Super Bot Fight Mode · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Super Bot Fight Mode to challenge or block bots on Pro, Business, and Enterprise plans."><meta property="og:url" content="https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/#page","headline":"Get started with Super Bot Fight Mode \u00b7 Cloudflare bot solutions docs","description":"Configure Super Bot Fight Mode to challenge or block bots on Pro, Business, and Enterprise plans.","url":"https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/get-started/super-bot-fight-mode/
  schema: 1
---
<p>Super Bot Fight Mode is included in your Pro, Business, or Enterprise subscription. Compared to <a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a>, Super Bot Fight Mode adds configurable actions per bot category, bot analytics, and the ability to create exceptions using <a href="/waf/custom-rules/">WAF custom rules</a>. When enabled, the product:</p>
<ul>
<li>Identifies traffic matching patterns of known bots</li>
<li>Can challenge or block bots</li>
<li>Offers protection for static resources</li>
<li>Provides limited analytics to help you understand bot traffic</li>
</ul>
<p>Accounts with an Enterprise subscription but not the <a href="/bots/get-started/bot-management/">Bot Management add-on</a> will have Super Bot Fight Mode for Business.</p>
<h2 id="considerations">Considerations</h2>
<p>Bot Fight Mode and Super Bot Fight Mode use the same underlying technology that powers our <a href="https://www.cloudflare.com/products/bot-management/">Bot Management</a> product. Specifically, these products:</p>
<ul>
<li>Protect entire domains without endpoint restrictions</li>
<li>Cannot be customized, adjusted, or reconfigured via WAF custom rules</li>
</ul>
<p>Although these products are designed to fight malicious actors on the Internet, they may challenge API or mobile app traffic. For more granular control, upgrade to <a href="/bots/plans/bm-subscription/">Bot Management for Enterprise</a>.</p>
<h3 id="interaction-with-other-app-security-features">Interaction with other app security features</h3>
<p>If you are using several app security features like custom rules, Managed Rules, and Super Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
<h3 id="configure-exceptions-to-super-bot-fight-mode">Configure exceptions to Super Bot Fight Mode</h3>
<p><a href="/waf/custom-rules/">Custom rules</a> are executed before Super Bot Fight Mode. To configure exceptions to Super Bot Fight Mode, create a custom rule with the <a href="/waf/custom-rules/skip/"><em>Skip</em> action</a>. The <em>Skip</em> action allows the request to bypass the Super Bot Fight Mode phase without terminating the request, enabling it to continue through the rest of the security stack.</p>
<h2 id="enable-super-bot-fight-mode">Enable Super Bot Fight Mode</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3495.md")
</aside>
<p>To start using Super Bot Fight Mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3496.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3494.md")
</aside>
<p>In parts of your site where you want bot traffic, you can use the <a href="/waf/custom-rules/skip/"><em>Skip</em> action</a> in <a href="/waf/custom-rules/">WAF custom rules</a> to specify where Super Bot Fight Mode should not run.</p>
<p>You can use the <a href="/ruleset-engine/rules-language/">Rules language</a> and its <a href="/ruleset-engine/rules-language/operators/">operators</a> and <a href="/ruleset-engine/rules-language/fields/">fields</a> in custom rules to configure a scoped rule for approved automated traffic in Super Bot Fight Mode.</p>
<hr />
<h2 id="disable-super-bot-fight-mode">Disable Super Bot Fight Mode</h2>
<p>If you find that <strong>Super Bot Fight Mode</strong> is causing problems with your application traffic, you may want to disable it.</p>
<p>To disable Super Bot Fight Mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3497.md")
</div>
<p>In parts of your site where you want bot traffic, you can use the <a href="/waf/custom-rules/skip/"><em>Skip</em> action</a> in <a href="/waf/custom-rules/">WAF custom rules</a> to specify where Super Bot Fight Mode should not run.</p>
<p>You can use the <a href="/ruleset-engine/rules-language/">Rules language</a> and its <a href="/ruleset-engine/rules-language/operators/">operators</a> and <a href="/ruleset-engine/rules-language/fields/">fields</a> in custom rules to configure a scoped rule for approved automated traffic in Super Bot Fight Mode.</p>
<hr />
<h2 id="block-ai-bots">Block AI bots</h2>
<p>Refer to <a href="/bots/additional-configurations/block-ai-bots/">Block AI bots</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3493.md")
</aside>
<hr />
<h2 id="analytics">Analytics</h2>
<h3 id="bot-report">Bot Report</h3>
<p>Use the <strong>Bot Report</strong> to monitor bot traffic for the past 24 hours.</p>
<p>To access the <strong>Bot Report</strong>, go to <strong>Security</strong> &gt; <strong>Analytics</strong> &gt; <strong>Bot analysis</strong>. If you see a double-digit percentage of automated traffic, you may want to upgrade to <a href="/bots/plans/bm-subscription/">Bot Management</a> to save money on origin costs and protect your domain from large-scale attacks.</p>
<p><img src="/assets/upstream/images/bots/bot-report-pro.png" alt="Example traffic distribution as part of a bot report" /></p>
<h3 id="security-events">Security events</h3>
<p>You can see bot-related actions by going to <strong>Security</strong> &gt; <strong>Analytics</strong> and selecting the <strong>Events</strong> tab. Any requests challenged by this product will be labeled <strong>Super Bot Fight Mode</strong> in the <strong>Service</strong> field. This allows you to observe, analyze, and follow trends in your bot traffic over time.</p>
<hr />
<h2 id="ruleset-engine">Ruleset Engine</h2>
<p>Super Bot Fight Mode rules run after WAF custom rules in the request evaluation pipeline. Specifically, Super Bot Fight Mode runs during the <code>http_request_sbfm</code> phase of the <a href="/ruleset-engine/about/phases/">Ruleset Engine</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="change-notice-for-super-bot-fight-mode-rulesets">Change notice for Super Bot Fight Mode rulesets</h3>
@markup("md", "content/.markup/bodies/3492.md")
</aside>
