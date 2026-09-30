---
cp9:
  canonical: https://developers.cloudflare.com/version-management/troubleshooting/
  description: Troubleshoot common issues with Version Management, including enablement problems, clone failures, and known limitations.
  full_title: Troubleshooting · Cloudflare Version Management docs
  head_html: <title>Troubleshooting · Cloudflare Version Management docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot common issues with Version Management, including enablement problems, clone failures, and known limitations."><link rel="canonical" href="https://developers.cloudflare.com/version-management/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/version-management/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare Version Management docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot common issues with Version Management, including enablement problems, clone failures, and known limitations."><meta property="og:url" content="https://developers.cloudflare.com/version-management/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Version Management"><meta name="algolia_product_filter" content="Version Management"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Version Management"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/version-management/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare Version Management docs","description":"Troubleshoot common issues with Version Management, including enablement problems, clone failures, and known limitations.","url":"https://developers.cloudflare.com/version-management/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /version-management/troubleshooting/
  schema: 1
---
<p>Use this page to resolve common issues with Version Management. If the steps below do not solve your problem, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> and include the details listed in <a href="#information-for-support">Information for Support</a>.</p>
<h2 id="version-management-is-greyed-out-or-unavailable">Version Management is greyed out or unavailable</h2>
<p>If the Version Management option appears greyed out or is not visible in the Cloudflare dashboard, verify that all <a href="/version-management/#requirements">requirements</a> are met.</p>
<p>Common causes:</p>
<ul>
<li><strong>Your zone is not on an Enterprise plan.</strong> Version Management is only available for Enterprise zones.</li>
<li><strong>Your zone is not in an active state.</strong> Verify that your zone's <a href="/dns/zone-setups/reference/domain-status/">domain status</a> is <strong>Active</strong>.</li>
<li><strong>WAF migration is incomplete.</strong> Your zone must use <a href="/waf/managed-rules/">WAF managed rules</a> and <a href="/waf/custom-rules/">custom rules</a> instead of the deprecated Firewall Rules. If your zone still uses the legacy WAF, contact your account team to complete the migration.</li>
<li><strong>Your user account does not have the required role.</strong> You need a <a href="/fundamentals/manage-members/roles/">Super Administrator or Administrator role</a> to enable Version Management. Zone Versioning roles cannot create new versions.</li>
<li><strong>Your user account does not have an API key.</strong> You must have an API key provisioned. Refer to <a href="/fundamentals/api/get-started/keys/#view-your-global-api-key">view your Global API key</a> for more information.</li>
<li><strong>API Access is disabled for your user account.</strong> Refer to <a href="/fundamentals/api/how-to/control-api-access/">control API Access</a> for more information.</li>
</ul>
<p>If all requirements are met and Version Management is still unavailable, contact your account team.</p>
<h2 id="failed-to-create-or-clone-a-version">Failed to create or clone a version</h2>
<p>Version creation (cloning) can fail for several reasons. When you clone a version, Cloudflare copies the zone configuration from the source version to a new version. If any part of this process encounters an error, the clone will fail.</p>
<h3 id="common-causes">Common causes</h3>
<details class="nb-details"><summary>Unsupported or partially supported product configurations</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/174.md")
</div></details>
<details class="nb-details"><summary>Invalid or conflicting configuration in the source version</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/175.md")
</div></details>
<details class="nb-details"><summary>Version creation is stuck</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/176.md")
</div></details>
<h3 id="what-to-do">What to do</h3>
<ol>
<li>Check the <a href="/version-management/#limitations">Limitations</a> section to confirm the source version does not rely on unsupported configurations.</li>
<li>Review the configuration in the source version for invalid or conflicting rules.</li>
<li>Retry the clone operation.</li>
<li>If the issue persists, contact Cloudflare Support.</li>
</ol>
<h2 id="rules-or-settings-appear-missing-for-some-users">Rules or settings appear missing for some users</h2>
<p>When Version Management is enabled, each version has its own independent set of rules and configurations. If a rule or setting appears to be missing, you or another user may be viewing a different version than the one where the rule was created.</p>
<p>For example, a cache rule created in one version will not appear when viewing another version. The rule may still be active and affecting traffic if its version is promoted to an active environment, but it will not be visible in the dashboard when a different version is selected.</p>
<p>To resolve this:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Version Management</strong>.</li>
<li>Check which version you are currently viewing.</li>
<li>Switch to the version where the rule was created.</li>
<li>If you need the rule in a different version, recreate it in that version or <a href="/version-management/how-to/versions/#create-version">clone the version</a> that contains the rule.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/173.md")
</aside>
<h2 id="worker-routes-disappear-or-behave-unexpectedly">Worker routes disappear or behave unexpectedly</h2>
<p>If a version has a Worker route, the route might disappear when a Worker is deployed using <a href="/workers/wrangler/">Wrangler</a>. Additionally, if two versions have the same custom domains, the Worker might randomly choose between them.</p>
<p>To avoid this:</p>
<ul>
<li>Deploy Workers using Wrangler before creating new versions that reference the same routes.</li>
<li>Avoid configuring the same custom domains across multiple versions.</li>
</ul>
<h2 id="terraform-is-not-supported">Terraform is not supported</h2>
<p><a href="/terraform/">Terraform</a> is not supported by Version Management. If you currently use Terraform to manage your zone configuration, you should choose either Terraform or Version Management — using both simultaneously is not supported.</p>
<h2 id="analytics-discrepancies">Analytics discrepancies</h2>
<p>When Version Management is enabled, analytics data in the Cloudflare dashboard may not reflect traffic splits across environments as expected. Analytics are reported at the zone level and may not break down by individual version or environment.</p>
<p>If you notice data discrepancies in your analytics dashboard after enabling Version Management, verify that you are viewing zone-level analytics rather than expecting per-version breakdowns.</p>
<h2 id="permissions-and-read-only-versions">Permissions and read-only versions</h2>
<details class="nb-details"><summary>Domain-scoped roles do not copy to new versions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/177.md")
</div></details>
<details class="nb-details"><summary>Version appears as read-only</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/178.md")
</div></details>
<h2 id="information-for-support">Information for Support</h2>
<p>When contacting Cloudflare Support about a Version Management issue, include the following details:</p>
<ul>
<li><strong>Account ID</strong> and <strong>Zone ID</strong> (found in the Cloudflare dashboard under <strong>Overview</strong>).</li>
<li><strong>Zone name</strong> (your domain).</li>
<li>The <strong>version number</strong> you were working with when the issue occurred.</li>
<li>The <strong>action you were attempting</strong> (for example, creating a version, cloning, promoting, or comparing).</li>
<li>The <strong>exact error message</strong> displayed, if any.</li>
<li>The <strong>approximate timestamp</strong> (including timezone) of when the issue occurred.</li>
<li><strong>Screenshots</strong> of the error, if available.</li>
</ul>
