---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/
  description: New updates and improvements at Cloudflare.
  full_title: Create WAF rules directly from Threat Events saved views · Changelog
  head_html: <title>Create WAF rules directly from Threat Events saved views · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Create WAF rules directly from Threat Events saved views · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/#page","headline":"Create WAF rules directly from Threat Events saved views \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-08-create-waf-rules-from-threat-events/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-08-create-waf-rules-from-threat-events/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 8, 2026</time><h2 id="post-title">Create WAF rules directly from Threat Events saved views</h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Cloudforce One users can now turn <a href="/security-center/cloudforce-one/#analyze-threat-events">Threat Events indicators</a> into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their <strong>Saved Views</strong>.</p>
<h4 id="why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules.
This new integration bridges the gap between threat discovery and threat mitigation:</p>
<ul>
<li>When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.</li>
<li>Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.</li>
<li>Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.</li>
</ul>
<h4 id="how-to-use-it">How to use it</h4>
<p>You can implement these rules through both the dashboard UI and via the API / Terraform.</p>
<p>Go to <strong>Cloudflare Dashboard</strong> &gt; <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Manage Views</strong>, select your desired view, and select <strong>Create WAF Rule</strong>.</p>
<p>This will automatically pre-populate the <a href="/firewall/cf-dashboard/create-edit-delete-rules/">WAF rule builder</a> with the matching threat event IP indicators.</p>
<p>You can also automate this workflow by utilizing the <a href="/firewall/api/cf-firewall-rules/"><strong>WAF Rule Builder API</strong></a> alongside your <a href="/firewall/api/cf-firewall-rules/">Threat Events saved views endpoints</a>.</p>
</div></article></div>
