---
cp9:
  canonical: https://developers.cloudflare.com/bots/bot-analytics/
  description: Use Bot Analytics to examine bot traffic patterns on your domain.
  full_title: Cloudflare Bot Analytics · Cloudflare bot solutions docs
  head_html: <title>Cloudflare Bot Analytics · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Bot Analytics to examine bot traffic patterns on your domain."><link rel="canonical" href="https://developers.cloudflare.com/bots/bot-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/bot-analytics/index.md"><meta property="og:title" content="Cloudflare Bot Analytics · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Bot Analytics to examine bot traffic patterns on your domain."><meta property="og:url" content="https://developers.cloudflare.com/bots/bot-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/bots/bot-analytics/#page","headline":"Cloudflare Bot Analytics \u00b7 Cloudflare bot solutions docs","description":"Use Bot Analytics to examine bot traffic patterns on your domain.","url":"https://developers.cloudflare.com/bots/bot-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/bot-analytics/
  schema: 1
---
<h2 id="business-and-enterprise">Business and Enterprise</h2>
<p>Business and Enterprise customers without Bot Management can use <strong>Bot Analytics</strong> to dynamically examine bot traffic. These dashboards offer less functionality than Bot Management for Enterprise but still help you understand bot traffic on your domain.</p>
<h3 id="access">Access</h3>
<p>You can access Bot Analytics by going to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>, and selecting your account and domain.</p>
<p>Go to <strong>Security</strong> &gt; <strong>Analytics</strong> &gt; <strong>Bot analysis</strong>.</p>
<p><img src="/assets/upstream/images/bots/bot-analytics-dashboard-biz.png" alt="View Bot Analytics in the Cloudflare dashboard. For more details, keep reading." /></p>
<h3 id="features">Features</h3>
<p>For a full tour of Bot Analytics, see <a href="https://blog.cloudflare.com/introducing-bot-analytics/">our blog post</a>. At a high level, the tool includes:</p>
<ul>
<li><strong>Requests by traffic type</strong>: View your total domain traffic segmented vertically by traffic type. Keep an eye on <em>automated</em> and <em>likely automated</em> traffic.</li>
<li><strong>Requests by detection source</strong>: Identify the most common detection engines used to score your traffic. Hover over a tooltip to learn more about each engine.</li>
<li><strong>Top requests by attribute</strong>: View more detailed information on specific IP addresses and other characteristics.</li>
</ul>
<p>Bot Analytics shows up to 72 hours of data at a time and can display data up to 30 days old. Bot Analytics displays data in real time in most cases.</p>
<p>Cloudflare uses adaptive bitrate technology to show sampled data — most customers will see a 1-10% sample depending on how much information they are trying to view. Tooltips on the page will display the current sample rate.</p>
<h3 id="common-uses">Common uses</h3>
<p>Business and Enterprise customers without Bot Management can use Bot Analytics to:</p>
<ul>
<li>Understand <span class="nb-glossary-tooltip" title="bot">bot</span> traffic</li>
<li>Study recent attacks to find trends and detailed information</li>
<li>Learn more about Cloudflare’s detection engines with real data</li>
</ul>
<p>For more details and granular control over bot traffic, consider upgrading to <a href="/bots/bot-analytics/#enterprise-bot-management">Bot Management for Enterprise</a>.</p>
<h2 id="enterprise-bot-management">Enterprise Bot Management</h2>
<p>Enterprise customers with Bot Management can use <strong>Bot Analytics</strong> to dynamically examine bot traffic.</p>
<h3 id="access-1">Access</h3>
<p>You can access Bot Analytics by going to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>, and selecting your account and domain.</p>
<p>Go to <strong>Security</strong> &gt; <strong>Analytics</strong> &gt; <strong>Bot analysis</strong>.</p>
<p><img src="/assets/upstream/images/bots/bot-analytics-dashboard-ent.png" alt="View Bot Analytics in the Cloudflare dashboard. For more details, keep reading." /></p>
<h3 id="features-1">Features</h3>
<p>For a full tour of Bot Analytics, see <a href="https://blog.cloudflare.com/introducing-bot-analytics/">our blog post</a>. At a high level, the tool includes:</p>
<ul>
<li><strong>Requests by bot score</strong>: View your total domain traffic and segment it vertically by traffic type. Keep an eye on <em>automated</em> and <em>likely automated</em> traffic.</li>
<li><strong>Bot score distribution</strong>: View the number of requests assigned a bot score 1 through 99.</li>
<li><strong>Bot score source</strong>: Identify the most common detection engines used to score your traffic. Hover over a tooltip to learn more about each engine.</li>
<li><strong>Top requests by attribute</strong>: View more detailed information on specific IP addresses and other characteristics.</li>
</ul>
<p>Bot Analytics shows up to one week of data at a time and can display data up to 30 days old. Bot Analytics displays data in real time in most cases.</p>
<p>Cloudflare uses adaptive bitrate technology to show sampled data — most customers will see a 1-10% sample depending on how much information they are trying to view. Tooltips on the page will display the current sample rate.</p>
<h3 id="common-uses-1">Common uses</h3>
<p>Bot Management customers can use Bot Analytics to:</p>
<ul>
<li>Understand traffic during <a href="/bots/get-started/bot-management/">your onboarding phase</a>.</li>
<li>Tune WAF custom rules to be effective but not overly aggressive.</li>
<li>Study recent attacks to find trends and detailed information.</li>
<li>Learn more about Cloudflare’s detection engines with real data.</li>
</ul>
<h3 id="api">API</h3>
<p>Data from Bot Analytics is also available via the GraphQL API. You can access <span class="nb-glossary-tooltip" title="bot score">bot scores</span>, bot sources, <span class="nb-glossary-tooltip" title="bot tags">bot tags</span>, and bot <em>decisions</em> (<em>automated</em>, <em>likely automated</em>, etc.), and more.</p>
<p>Read the <a href="/analytics/graphql-api/">GraphQL Analytics API documentation</a> for more information about GraphQL and basic querying.</p>
