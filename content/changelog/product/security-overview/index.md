---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/security-overview/
  description: '2026-04-20'
  full_title: security-overview changelog | Cloudflare Docs
  head_html: <title>security-overview changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-20"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/security-overview/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="security-overview changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-20"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/security-overview/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/security-overview/#page","headline":"security-overview changelog | Cloudflare Docs","description":"2026-04-20","url":"https://developers.cloudflare.com/changelog/product/security-overview/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/security-overview/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="archive-and-audit-security-action-items"><a href="/changelog/post/2026-04-27-archive-and-audit-security-action-items/">Archive and audit security action items</a></h2>
<p><em>2026-04-20</em></p>
<h4 id="2026-04-27-archive-and-audit-security-action-items-archive-and-audit-security-action-items">Archive and audit security action items</h4>
<p>Introducing enhanced archiving capabilities for security action items within the Security Overview dashboard. This update allows security teams to maintain a cleaner workspace by removing resolved, accepted, or irrelevant items from their active list while maintaining a clear paper trail for compliance.</p>
<hr />
<h4 id="2026-04-27-archive-and-audit-security-action-items-why-this-matters">Why this matters</h4>
<p>Managing a high volume of security insights can be overwhelming. Previously, users lacked a structured way to dismiss items without losing the context of why they were ignored.</p>
<p>With these new archiving options—<strong>False Positive</strong>, <strong>Accept Risk</strong>, and <strong>Other</strong>—you can now suppress items indefinitely with required rationale text for risk-based decisions. This ensures that your team remains focused on critical, actionable vulnerabilities while preserving institutional knowledge for audits.</p>
<h4 id="2026-04-27-archive-and-audit-security-action-items-key-features">Key features</h4>
<ul>
<li><strong>Structured Archiving:</strong> Choose from specific categories to define why an action item is being moved.</li>
<li><strong>Required Rationale:</strong> For &quot;Accept Risk&quot; and &quot;Other&quot; categories, users must provide documentation, ensuring accountability for security decisions.</li>
<li><strong>Audit Log Transparency:</strong> New API endpoints allow you to programmatically retrieve the history of status changes and rationale for any insight at the account or zone level.</li>
<li><strong>Reversible Actions:</strong> Any archived item can be moved back to the active list at any time if the security context changes.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17753.md")</aside>
<hr />
<h4 id="2026-04-27-archive-and-audit-security-action-items-example-retrieve-audit-logs-via-api">Example: Retrieve audit logs via API</h4>
<p>To review the history and rationale of a specific archived issue at the account level, you can use the following API command:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){account_id}/insights/{insight_id}/audit-log&quot; \&#10;     &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot;&#10;</code></pre>


<h2 id="new-security-overview-ui"><a href="/changelog/post/2026-03-17-new-security-overview-ui/">New Security Overview UI</a></h2>
<p><em>2026-03-17</em></p>
<p>The Security Overview has been updated to provide Application Security customers with more actionable insights and a clearer view of their security posture.</p>
<p>Key improvements include:</p>
<ul>
<li><strong>Criticality for all Insights</strong>: Every insight now includes a criticality rating, allowing you to prioritize the most impactful security action items first.</li>
<li><strong>Detection Tools Section</strong>: A new section displays the security detection tools available to you, indicating which are currently enabled and which can be activated to strengthen your defenses.</li>
<li><strong>Industry Peer Comparison</strong> (Enterprise customers): A new module from Security Reports benchmarks your security posture against industry peers, highlighting relative strengths and areas for improvement.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-overview/overview-ui.png" alt="New Security Overview UI" /></p>
<p>For more information, refer to <a href="/security/overview/">Security Overview</a>.</p>



