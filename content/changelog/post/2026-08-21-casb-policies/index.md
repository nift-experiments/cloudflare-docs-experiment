---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/
  description: New updates and improvements at Cloudflare.
  full_title: Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies · Changelog
  head_html: <title>Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/#page","headline":"Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-21-casb-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-21-casb-policies/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 21, 2026</time><h2 id="post-title">Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies</h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p><a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> is an API-based (agentless) tool that continuously scans your SaaS and cloud applications for security misconfigurations and data exposure. You can now use <strong>CASB remediation policies</strong> to automatically fix a finding or send a webhook the moment CASB detects it, without manual triage.</p>
<h4 id="remediate-microsoft-365-and-google-workspace-findings">Remediate Microsoft 365 and Google Workspace findings</h4>
<p>A policy can perform a first-party remediation action directly against the SaaS integration API. When a policy triggers, Cloudflare revokes the external sharing configuration without human intervention.</p>
<p>Remediation is currently supported for file-sharing findings in Microsoft 365 and Google Workspace. Support for additional finding types and integrations is coming soon. For the full list of supported finding types, refer to <a href="/cloudflare-one/cloud-and-saas-findings/policies/#run-remediations">Run remediations</a> in the CASB remediation policies documentation.</p>
<h4 id="send-webhooks">Send webhooks</h4>
<p>A policy can send posture finding data to Slack, ServiceNow, or any other webhook destination. Webhook actions are supported for all posture finding types across CASB integrations.</p>
<p>A single policy can perform both actions: remediate a finding and send a webhook.</p>
<h4 id="get-started">Get started</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Policies</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Under <strong>Basic information</strong>, enter a <strong>Policy name</strong> and, optionally, a <strong>Description</strong>.</li>
<li>Under <strong>Choose how you want to trigger the policy</strong>, select a <strong>Vendor</strong>, <strong>Integration</strong>, and <strong>Finding type</strong>.</li>
<li>Under <strong>Define what to do with findings that match your trigger</strong>, choose <strong>Run Remediation</strong>, <strong>Send webhooks</strong>, or both.</li>
<li>Under <strong>Status</strong>, turn on <strong>Enable policy</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<h4 id="learn-more">Learn more</h4>
<ul>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/policies/">create and manage CASB remediation policies</a> in Cloudflare One.</li>
<li>Configure <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a> as a policy destination.</li>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">manage findings</a> in Cloudflare One.</li>
</ul>
<p>CASB remediation policies are now available in Cloudflare One.</p>
</div></article></div>
