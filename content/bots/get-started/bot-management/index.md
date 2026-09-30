---
cp9:
  canonical: https://developers.cloudflare.com/bots/get-started/bot-management/
  description: Configure Bot Management for Enterprise to identify and act on automated traffic.
  full_title: Bot Management · Cloudflare bot solutions docs
  head_html: <title>Bot Management · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Bot Management for Enterprise to identify and act on automated traffic."><link rel="canonical" href="https://developers.cloudflare.com/bots/get-started/bot-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/get-started/bot-management/index.md"><meta property="og:title" content="Bot Management · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Bot Management for Enterprise to identify and act on automated traffic."><meta property="og:url" content="https://developers.cloudflare.com/bots/get-started/bot-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/get-started/bot-management/#page","headline":"Bot Management \u00b7 Cloudflare bot solutions docs","description":"Configure Bot Management for Enterprise to identify and act on automated traffic.","url":"https://developers.cloudflare.com/bots/get-started/bot-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/get-started/bot-management/
  schema: 1
---
<p>Bot Management for Enterprise is a paid add-on that provides sophisticated bot protection for your domain. Customers can identify automated traffic, take appropriate action, and view detailed analytics within the dashboard.</p>
<p>This Enterprise product provides the most flexibility to customers by:</p>
<ul>
<li>Generating a <a href="/bots/concepts/bot-score/">bot score</a> of 1-99 for every request. Scores below 30 are commonly associated with bot traffic. This lets you write targeted rules instead of applying blanket actions to all detected bots.</li>
<li>Allowing customers to take action on this score with <a href="/waf/custom-rules/">WAF custom rules</a> or <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>Workers</code></a>. For example, you can challenge low-scoring requests on your login page while allowing them on your public blog.</li>
<li>Allowing customers to view this score in Bot Analytics or Logs, so you can analyze bot traffic patterns and tune your rules over time.</li>
</ul>
<hr />
<h2 id="enable-bot-management-for-enterprise">Enable Bot Management for Enterprise</h2>
<p>Bot Management is automatically enabled for Enterprise zones entitled with the add-on.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3501.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3500.md")
</aside>
<hr />
<h2 id="setup">Setup</h2>
<p>Cloudflare recommends that you deploy the following basic settings and customize them according to the traffic in your zone.</p>
<h3 id="enable-the-latest-machine-learning-version">Enable the latest Machine Learning version</h3>
<p>Cloudflare encourages Enterprise customers to enable auto-updates to its Machine Learning models to get the newest bot detection models as they are released.</p>
<p>To enable auto-updates:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3502.md")
</div>
<h3 id="block-ai-bots">Block AI Bots</h3>
<p>Refer to <a href="/bots/additional-configurations/block-ai-bots/">Block AI bots</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3499.md")
</aside>
<h3 id="deploy-custom-rule-templates">Deploy custom rule templates</h3>
<p>The <strong>Definitely Automated</strong> and <strong>Likely Automated</strong> toggles you configured in the previous step already provide baseline protection against automated traffic.</p>
<p>If you need additional control, such as path-specific protection, custom score thresholds, or combining bot score with other fields, Cloudflare provides <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules?template=bot_traffic">rule templates</a> to get started.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3498.md")
</aside>
<p>These templates use wirefilter expression syntax. In these expressions, <code>eq</code> means equals, <code>le</code> means less than or equal to, <code>ge</code> means greater than or equal to, and <code>not</code> excludes matching traffic.</p>
<ul>
<li><a href="https://dash.cloudflare.com/?to=/:account/:zone:/security/security-rules/custom-rules/create?template=Definitely%20Bots">Definite Bots template</a>: Targets malicious bot traffic while ignoring verified bots and routes delivering static content.</li>
</ul>
<pre tabindex="0"><code class="language-txt">(cf.bot_management.score eq 1 and not cf.bot_management.verified_bot and not cf.bot_management.static_resource)&#10;</code></pre>
<ul>
<li><a href="https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules/custom-rules/create?template=Likely%20Bots">Likely Bots template</a>: Targets traffic likely to be malicious bots while ignoring verified bots and routes with static content. It may contain a small amount of non-bot traffic.</li>
</ul>
<pre tabindex="0"><code class="language-txt">(cf.bot_management.score ge 2 and cf.bot_management.score le 29 and not cf.bot_management.verified_bot and not cf.bot_management.static_resource)&#10;</code></pre>
<ul>
<li>(Optional) <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules/custom-rules/create?template=JavaScript%20Verified%20URLs">JavaScript detections template</a>: You must first enable JavaScript Detections from Security Settings, then set up a <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">managed challenge</a>. Make sure to add a method and URI path. JavaScript detections improves security for URLs that should only expect JavaScript-enabled clients.</li>
</ul>
<pre tabindex="0"><code class="language-txt">(not cf.bot_management.js_detection.passed and http.request.method eq &quot;&quot; and http.request.uri.path in {&quot;&quot;})&#10;</code></pre>
