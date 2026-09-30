---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/rules/
  description: Use content security rules to define the resources (scripts) allowed on your applications.
  full_title: Content security rules · Client-side security docs
  head_html: <title>Content security rules · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Use content security rules to define the resources (scripts) allowed on your applications."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/rules/index.md"><meta property="og:title" content="Content security rules · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use content security rules to define the resources (scripts) allowed on your applications."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Client-side security"><meta name="pcx_tags" content="Headers,CSP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/rules/#page","headline":"Content security rules \u00b7 Client-side security docs","description":"Use content security rules to define the resources (scripts) allowed on your applications.","url":"https://developers.cloudflare.com/client-side-security/rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers","CSP"]}</script>
  markdown: true
  noindex: false
  route: /client-side-security/rules/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3965.md")
</aside>
<p>Content security rules (previously known as policies) define which resources your application is allowed to load. They work through <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span> directives that Cloudflare adds to your HTTP responses. There are two types of content security rules:</p>
<ul>
<li><strong>Log rules</strong> report resources that fall outside your allowlist without blocking them.</li>
<li><strong>Allow rules</strong> block any resource not explicitly listed.</li>
</ul>
<p>Create <a href="#rule-actions">allow rules</a> to define an allowlist-based security model. You specify exactly which resources are permitted and everything else is rejected. This approach reduces the attack surface for unwanted third-party scripts in your application.</p>
<p>A content security rule can control both client-side resources monitored by Cloudflare, such as scripts and their connections, and other types of resources. Refer to <a href="/client-side-security/rules/csp-directives/">Supported CSP directives</a> for details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3964.md")
</aside>
<h2 id="rule-actions">Rule actions</h2>
<p>A content security rule can perform one of the following actions:</p>
<ul>
<li><strong>Log</strong>: Cloudflare reports any resources not covered by the rule as <a href="/client-side-security/rules/violations/">rule violations</a> without blocking them. Use this action to validate a new content security rule before deploying it.</li>
<li><strong>Allow</strong>: Cloudflare blocks any resources not explicitly allowed by the rule and logs them as <a href="/client-side-security/rules/violations/">rule violations</a>. Switch to this action after validating a rule with the <em>Log</em> action to avoid blocking essential application resources.</li>
</ul>
<p>For details on the CSP directives Cloudflare creates for each type of rule action, refer to <a href="/client-side-security/how-it-works/#headers-related-to-content-security-rules">How client-side security works</a>. For more information on the CSP directives supported by content security rules, refer to <a href="/client-side-security/rules/csp-directives/">Supported CSP directives</a>.</p>
<h3 id="comparison">Comparison</h3>
<table>
<thead>
<tr>
<th></th>
<th>Log rule</th>
<th>Allow rule</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CSP header</strong></td>
<td><code>content-security-policy-report-only</code></td>
<td><code>content-security-policy</code></td>
</tr>
<tr>
<td><strong>Browser action</strong></td>
<td>Loads all resources</td>
<td>Blocks resources not in your allowlist</td>
</tr>
<tr>
<td><strong>Violations</strong></td>
<td>Reported to Cloudflare without blocking</td>
<td>Logged by Cloudflare after blocking</td>
</tr>
<tr>
<td><strong>Use case</strong></td>
<td>Validate a rule before enforcing it</td>
<td>Enforce a positive security model</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<p>Refer to the following pages for instructions on creating a content security rule:</p>
<ul>
<li><a href="/client-side-security/rules/create-dashboard/">Create a content security rule in the dashboard</a></li>
<li><a href="/client-side-security/reference/api/#create-a-content-security-rule">Client-side security API: Create a content security rule</a></li>
</ul>
<p>Shortly after you configure content security rules, the Cloudflare dashboard will start displaying any <a href="/client-side-security/rules/violations/">violations</a> of those rules.</p>
<p>You can filter client-side security alert notifications according to the content security rules you configured in a zone. These alerts are called <a href="/client-side-security/alerts/#scoped-alerts">scoped alerts</a>.</p>
