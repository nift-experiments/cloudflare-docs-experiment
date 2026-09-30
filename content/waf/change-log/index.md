---
cp9:
  canonical: https://developers.cloudflare.com/waf/change-log/
  description: Overview of WAF changelog, scheduled changes, and historical updates.
  full_title: Overview of the WAF changelog · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Overview of the WAF changelog · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Overview of WAF changelog, scheduled changes, and historical updates."><link rel="canonical" href="https://developers.cloudflare.com/waf/change-log/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/change-log/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/waf/change-log/index.xml"><meta property="og:title" content="Overview of the WAF changelog · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Overview of WAF changelog, scheduled changes, and historical updates."><meta property="og:url" content="https://developers.cloudflare.com/waf/change-log/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/waf/change-log/#page","headline":"Overview of the WAF changelog \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Overview of WAF changelog, scheduled changes, and historical updates.","url":"https://developers.cloudflare.com/waf/change-log/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/change-log/
  schema: 1
---
<p>The <a href="/waf/change-log/changelog/">WAF changelog</a> provides information about changes to <a href="/waf/managed-rules/">managed rulesets</a> and general updates to WAF protection.</p>
<p><a class="nb-link-button" href="/waf/change-log/changelog/">View changelog</a>
<a class="nb-link-button" href="/waf/change-log/scheduled-changes/">View scheduled changes</a></p>
<div class="nb-r-s-s-button"></div>
<h2 id="changelog-for-managed-rulesets">Changelog for managed rulesets</h2>
<p>Cloudflare regularly releases updates and adds new rules to WAF <a href="/waf/managed-rules/">managed rulesets</a>. Updates improve rule accuracy, reduce false positives, or increase protection in response to changes in the threat landscape.</p>
<h3 id="release-cycle">Release cycle</h3>
<p>New and updated rules follow a seven-day release cycle, typically on Monday or Tuesday (adjusted for public holidays).</p>
<p><strong>Week 1 — Logging only:</strong> Cloudflare deploys new or updated rules in logging-only mode with the <em>Log</em> action. Rules in this mode record matching requests but do not block traffic. Most newly created rules carry both the <code>beta</code> and <code>new</code> tags. Use this period to review your security events for unexpected matches that could be false positives.</p>
<p><strong>Week 2 — Default action:</strong> On the following release day, the rules change from the <em>Log</em> action to their intended default action (shown in the <strong>New Action</strong> column of the changelog table). The <code>beta</code> and <code>new</code> tags are removed.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15398.md")
</aside>
<p>For updates to existing rules, Cloudflare first deploys the updated version as a separate <code>BETA</code> rule (noted in the rule description) with a <code>beta</code> tag, before updating the original rule on the next release cycle.</p>
<h3 id="disabled-rules">Disabled rules</h3>
<p>Cloudflare may also add rules in disabled mode on the same release cycle. These rules make remediation logic available without affecting traffic, and allow Cloudflare to perform impact testing and performance checks. You can activate a disabled rule at any time if you need its protection. Disabled rules do not carry the <code>beta</code> or <code>new</code> tags.</p>
<h3 id="emergency-releases">Emergency releases</h3>
<p>For new vulnerabilities, Cloudflare may release rules outside the regular seven-day cycle. These are emergency releases.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15397.md")
</aside>
<p>If you notice a new or updated rule generating an increased volume of security events, you can disable it or change its action from the default. Once you change a rule to use an action other than the default one, Cloudflare will not be able to override the rule action.</p>
<h2 id="general-updates">General updates</h2>
<p>The <a href="/waf/change-log/changelog/">changelog</a> also includes general updates to WAF protection that are not specific to managed rulesets.</p>
