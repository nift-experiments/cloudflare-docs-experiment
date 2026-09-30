---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/
  description: Safe practices for deploying and updating content security rules.
  full_title: Deploy content security rules in production · Client-side security docs
  head_html: <title>Deploy content security rules in production · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Safe practices for deploying and updating content security rules."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/index.md"><meta property="og:title" content="Deploy content security rules in production · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Safe practices for deploying and updating content security rules."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Client-side security"><meta name="pcx_tags" content="CSP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/#page","headline":"Deploy content security rules in production \u00b7 Client-side security docs","description":"Safe practices for deploying and updating content security rules.","url":"https://developers.cloudflare.com/client-side-security/best-practices/deploy-rules-in-production/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CSP"]}</script>
  markdown: true
  noindex: false
  route: /client-side-security/best-practices/deploy-rules-in-production/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4013.md")
</aside>
<p>Follow the practices on this page when deploying or updating <a href="/client-side-security/rules/">content security rules</a> in a production environment. Applying rule changes without a validation period can block legitimate resources and disrupt your application for end users.</p>
<h2 id="update-rules-safely">Update rules safely</h2>
<p>When updating content security rules in production, avoid the following:</p>
<ul>
<li>Do not edit an existing rule directly in production without testing first.</li>
<li>Do not change a rule action from <em>Log</em> to <em>Allow</em> without a validation period.</li>
<li>Do not delete all rules at once.</li>
</ul>
<p>Instead, follow these practices:</p>
<ul>
<li>Test changes in a staging environment before applying them in production.</li>
<li>Use the <em>Log</em> <a href="/client-side-security/rules/#rule-actions">rule action</a> for at least seven days before switching to <em>Allow</em>.</li>
<li>Update one rule at a time.</li>
<li>Monitor <a href="/client-side-security/rules/violations/">rule violations</a> for 24 hours after each change.</li>
<li>Document a rollback procedure before making changes.</li>
</ul>
<h2 id="pre-enforcement-checklist">Pre-enforcement checklist</h2>
<p>Complete the following checklist before switching a content security rule from <em>Log</em> to <em>Allow</em>:</p>
<ul>
<li>The rule was tested in <em>Log</em> mode for a minimum of seven days.</li>
<li>Reviewed all <a href="/client-side-security/rules/violations/">rule violations</a> and confirmed there are no unexpected blocks.</li>
<li>Added all legitimate third-party resources to the rule allowlist.</li>
<li>Tested the application on all major browsers (Chrome, Firefox, Safari, Edge).</li>
<li>Configured <a href="/client-side-security/alerts/">alerts</a> for rule violations.</li>
<li>There is a documented rollback procedure that is ready to execute.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4012.md")
</aside>
<h2 id="rollback-a-rule-change">Rollback a rule change</h2>
<p>If a rule change causes unexpected violations or blocks legitimate resources:</p>
<ol>
<li>Switch the rule action back to <em>Log</em> to stop blocking resources immediately.</li>
<li>Review the <a href="/client-side-security/rules/violations/">rule violations</a> to identify which resources were blocked.</li>
<li>Update the rule to include any missing resources.</li>
<li>Repeat the validation process before switching back to <em>Allow</em> (blocks resources not present in the allowlist).</li>
</ol>
