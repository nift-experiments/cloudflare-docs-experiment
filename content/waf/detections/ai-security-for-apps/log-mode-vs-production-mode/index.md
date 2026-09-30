---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/
  description: Differences between log mode and production mode for AI security detections.
  full_title: Log mode versus production mode · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Log mode versus production mode · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Differences between log mode and production mode for AI security detections."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/index.md"><meta property="og:title" content="Log mode versus production mode · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Differences between log mode and production mode for AI security detections."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/#page","headline":"Log mode versus production mode \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Differences between log mode and production mode for AI security detections.","url":"https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /waf/detections/ai-security-for-apps/log-mode-vs-production-mode/
  schema: 1
---
<p>AI Security for Apps can operate in two distinct modes. Understanding the trade-offs between them helps you choose the right approach for your stage of deployment.</p>
<h2 id="comparison">Comparison</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Production mode</th>
<th>Log mode</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>How it works</strong></td>
<td>You write WAF <a href="/waf/custom-rules/">custom rules</a> using AI Security for Apps detection fields</td>
<td>You enable the AI Security Log Mode Ruleset with pre-built rules</td>
</tr>
<tr>
<td><strong>Prompt logging</strong></td>
<td>No — only request metadata is logged</td>
<td>Yes — the full request body is logged (encrypted via <a href="/waf/managed-rules/payload-logging/">payload logging</a>)</td>
</tr>
<tr>
<td><strong>Response logging</strong></td>
<td>No — use <a href="/ai-gateway/">AI Gateway</a> if response visibility is required</td>
<td>No — same limitation</td>
</tr>
<tr>
<td><strong>Policy flexibility</strong></td>
<td>Full — combine injection scores, PII categories, bot scores, custom topics, and more</td>
<td>Limited — three fixed rules (PII detected, unsafe topic detected, prompt injection detected) with no score-based or subcategory logic</td>
</tr>
<tr>
<td><strong>Blocking behavior</strong></td>
<td>Customizable — issue custom responses including custom JSON</td>
<td>Default WAF block page only</td>
</tr>
<tr>
<td><strong>Best for</strong></td>
<td>Production traffic with granular control</td>
<td>Evaluation and testing — correlate prompts with detection results to tune thresholds</td>
</tr>
</tbody>
</table>
<h2 id="production-mode">Production mode</h2>
<p>Production mode is the standard operating mode. You enable AI Security for Apps and create <a href="/waf/custom-rules/">custom rules</a> using the <a href="/waf/detections/ai-security-for-apps/fields/">detection fields</a> it populates. This gives you full control over:</p>
<ul>
<li><strong>Which detections trigger an action.</strong> For example, block only when <code>cf.llm.prompt.injection_score</code> is below 30, rather than blocking any detection.</li>
<li><strong>Which PII categories matter.</strong> For example, block <code>CREDIT_CARD</code> but only log <code>EMAIL_ADDRESS</code>.</li>
<li><strong>Combining signals.</strong> For example, block when both PII is detected and the bot score is low.</li>
<li><strong>Custom responses.</strong> Return a JSON error message to your application instead of the default WAF block page.</li>
</ul>
<p>Example production rule expression:<br/>
<code>(cf.llm.prompt.injection_score lt 30 and cf.bot_management.score lt 20)</code></p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="limitation">Limitation</h3>
@markup("md", "content/.markup/bodies/15568.md")
</aside>
<h2 id="log-mode">Log mode</h2>
<p>Log mode uses the AI Security Log Mode Ruleset — a pre-built ruleset that logs the full request body alongside detection results. This mode is designed for evaluation and tuning rather than production enforcement.</p>
<p>In log mode:</p>
<ul>
<li>The managed ruleset fires on three broad conditions: PII detected, unsafe topic detected, and prompt injection detected.</li>
<li>The entire request body is logged using <a href="/waf/managed-rules/payload-logging/">payload logging</a> (encrypted — you must configure a key pair to decrypt payloads).</li>
<li>You can correlate specific prompts with their detection scores to understand how the model classifies your traffic.</li>
</ul>
<p><strong>When to use log mode:</strong></p>
<ul>
<li>During initial deployment, to understand what AI Security for Apps detects on your traffic before enforcing actions.</li>
<li>When tuning score thresholds — review logged prompts alongside their scores to determine appropriate thresholds.</li>
<li>When validating that <a href="/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics">custom topic</a> definitions are working as expected.</li>
</ul>
<h3 id="enable-log-mode">Enable log mode</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15572.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15567.md")
</aside>
<h2 id="recommended-workflow">Recommended workflow</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15573.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15566.md")
</aside>
