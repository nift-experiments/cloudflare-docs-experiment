---
cp9:
  canonical: https://developers.cloudflare.com/firewall/cf-firewall-rules/order-priority/
  description: Understand firewall rule evaluation order and priority.
  full_title: Order and priority · Cloudflare Firewall Rules (deprecated) docs
  head_html: <title>Order and priority · Cloudflare Firewall Rules (deprecated) docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand firewall rule evaluation order and priority."><link rel="canonical" href="https://developers.cloudflare.com/firewall/cf-firewall-rules/order-priority/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/firewall/cf-firewall-rules/order-priority/index.md"><meta property="og:title" content="Order and priority · Cloudflare Firewall Rules (deprecated) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand firewall rule evaluation order and priority."><meta property="og:url" content="https://developers.cloudflare.com/firewall/cf-firewall-rules/order-priority/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Firewall Rules (deprecated)"><meta name="algolia_product_filter" content="Firewall Rules (deprecated)"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Firewall Rules (deprecated)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/firewall/cf-firewall-rules/order-priority/#page","headline":"Order and priority \u00b7 Cloudflare Firewall Rules (deprecated) docs","description":"Understand firewall rule evaluation order and priority.","url":"https://developers.cloudflare.com/firewall/cf-firewall-rules/order-priority/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /firewall/cf-firewall-rules/order-priority/
  schema: 1
---
<p>Cloudflare Firewall Rules, now deprecated, is part of a larger evaluation chain for HTTP requests, as illustrated in the diagram below. For example, Firewall Rules only evaluates requests that first clear IP Access rules. If a request is blocked by a rule at any stage in the chain, Cloudflare does not evaluate the request further.</p>
<p><img src="/assets/upstream/images/firewall/firewall-rules-order-and-priority-1.png" alt="Flow chart of request evaluation at Cloudflare for security products that are not powered by the Ruleset Engine" /></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8692.md")
</aside>
<p>By default, Cloudflare evaluates firewall rules in <strong>list order</strong>, where rules are evaluated in the order they appear in the firewall rules list. List ordering is convenient when working with small numbers of rules because you can manage their order by dragging and dropping them into position. However, as the number of rules grows, managing rules in list order becomes difficult. This is where priority order comes into play.</p>
<p>When <strong>priority ordering</strong> is enabled, Cloudflare evaluates firewall rules in order of their <strong>priority number</strong>, starting with the lowest. If a request matches two rules with the same priority, action precedence is used to resolve the tie. In this case, only the action of the rule with the highest precedence is executed, unless that action is <em>Log</em> or <em>Bypass</em> (refer to <a href="/firewall/cf-firewall-rules/actions/#supported-actions">Firewall rules actions</a> for details). Priority ordering makes it a lot easier to manage large numbers of firewall rules, and once the number of rules passes 200, Cloudflare requires it.</p>
<h2 id="managing-rule-evaluation-by-list-order">Managing rule evaluation by list order</h2>
<p>Users with relatively small numbers of firewall rules (no more than 200) will find that list ordering is enabled by default. When list ordering is enabled, the rules list allows you to drag and drop firewall rules into position, as shown below:</p>
<p><img src="/assets/upstream/images/firewall/firewall-rules-order-and-priority-2.gif" alt="Animation of a firewall rule being moved into a new position in the rules list to reorder it" /></p>
<p>Once there are more than 200 total rules, including inactive rules, you must manage evaluation using priority ordering. When you cross this threshold, the firewall rules interface automatically switches to priority ordering.</p>
<h2 id="managing-rule-evaluation-by-priority-order">Managing rule evaluation by priority order</h2>
<p>Although priority ordering is enabled automatically when the number of active and inactive firewall rules exceeds 200, you can manually enable priority ordering at any time from the rules list.</p>
<p>Cloudflare Firewall Rules does not impose default priorities, and you are not required to set a priority for every rule.</p>
<h3 id="enable-priority-ordering">Enable priority ordering</h3>
<p>To manually enable priority ordering:</p>
<ol>
<li>Above the rules list, select <strong>Ordering</strong>.</li>
<li>Select <em>Priority Numbers</em>.</li>
</ol>
<p>Once priority ordering is enabled, you can set a priority number for each firewall rule.</p>
<h3 id="set-rule-priority">Set rule priority</h3>
<p>To set the priority number for a firewall rule:</p>
<ol>
<li>
<p>Locate the desired rule in the rules list and select <strong>Edit</strong> (wrench icon).</p>
</li>
<li>
<p>In the <strong>Edit firewall rule</strong> panel, enter a positive integer value in <strong>Priority</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/firewall/firewall-rules-order-and-priority-4.png" alt="Editing a firewall rule in the dashboard to define its Priority value" /></p>
<ol start="3">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The <strong>Priority</strong> column in the rules list displays the priority value for each rule.</p>
<p><img src="/assets/upstream/images/firewall/firewall-rules-order-and-priority-5.png" alt="When using priority order, the Firewall rules tab displays the priority of each rule (if any) in the first column of the rules list" /></p>
<h2 id="working-with-priority-ordering">Working with priority ordering</h2>
<p>Cloudflare has designed priority ordering to be extremely flexible. This flexibility is particularly useful for managing large rulesets programmatically via the Cloudflare API. Use the Update firewall rules command to set the <code>priority</code> property. Refer to <a href="/api/resources/firewall/subresources/rules/methods/list/">Cloudflare API: Firewall rules</a> for details.</p>
<p>While your priority numbering scheme can be arbitrary, keep the following in mind:</p>
<ul>
<li>
<p><strong>The evaluation sequence starts from the lowest priority number</strong> and goes to the highest.</p>
</li>
<li>
<p><strong>Rules without a priority number are evaluated last</strong>, in order of their action precedence. For example, a rule with the <em>Log</em> action is evaluated before a rule that has the <em>Block</em> action. For more on action precedence, refer to <a href="/firewall/cf-firewall-rules/actions/">Firewall rules actions</a>.</p>
</li>
<li>
<p><strong>Avoid using the number <code>1</code> as a priority</strong> to make rule order modification easier in the future.</p>
</li>
<li>
<p><strong>Consider grouping ranges of priority numbers into categories</strong> that have some meaning for your deployment. Here are some examples:</p>
<ul>
<li>5000-9999: Trusted IP addresses</li>
<li>10000-19999: Blocking rules for bad crawlers</li>
<li>20000-29999: Blocking rules for abusive users/spam</li>
</ul>
</li>
</ul>
