---
cp9:
  canonical: https://developers.cloudflare.com/security/overview/
  description: Review your domain's security posture and action items.
  full_title: Security overview · Security dashboard docs
  head_html: <title>Security overview · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="Review your domain&#x27;s security posture and action items."><link rel="canonical" href="https://developers.cloudflare.com/security/overview/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/overview/index.md"><meta property="og:title" content="Security overview · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review your domain&#x27;s security posture and action items."><meta property="og:url" content="https://developers.cloudflare.com/security/overview/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Security dashboard"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/overview/#page","headline":"Security overview \u00b7 Security dashboard docs","description":"Review your domain's security posture and action items.","url":"https://developers.cloudflare.com/security/overview/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security/overview/
  schema: 1
---
<p>Security overview provides an overview of your domain's security posture and allows you to quickly identify security action items that may need your attention.</p>
<p>To access Security overview in the new security dashboard, go to the <strong>Overview</strong> page.</p>
<div class="nb-dash-button"></div>
<p>The Security overview page displays:</p>
<ul>
<li>Security action items</li>
<li>Detection tools</li>
<li>Traffic overview</li>
</ul>
<h2 id="security-action-items">Security action items</h2>
<p><strong>Security action items</strong> shows you insights and recommendations related to misconfigurations, exposed infrastructure, and suspicious activity.</p>
<ul>
<li><strong>Action item types</strong>:
<ul>
<li>Suspicious activity</li>
<li>Security insight</li>
</ul>
</li>
<li><strong>Criticality</strong>: Your action items are ranked by the highest criticality, showing critical first, moderate, and low respectively.</li>
<li><strong>Filters</strong>: You can filter your action items by Criticality, Insight Type, and Security Category.
<ul>
<li>Criticality:
<ul>
<li>Low</li>
<li>Moderate</li>
<li>Critical</li>
</ul>
</li>
<li>Insight Types:
<ul>
<li>Suspicious activity</li>
<li>Exposed infrastructure</li>
<li>Insecure configuration</li>
<li>Configuration suggestion</li>
<li>Compliance Violation</li>
<li>Email Security</li>
<li>Weak Authentication</li>
</ul>
</li>
<li>Security Category:
<ul>
<li>Web application exploits</li>
<li>AI exploits</li>
<li>DDoS attacks</li>
<li>Bot traffic</li>
<li>API abuse</li>
<li>Client-side abuse</li>
<li>Fraud</li>
</ul>
</li>
</ul>
</li>
<li><strong>Review</strong>: Review your security action items for more detailed information and recommended actions to resolve.</li>
<li><strong>Load more</strong>: View the full list of security action items.</li>
</ul>
<h3 id="archive-action-items">Archive action items</h3>
<p>You can archive security action items that you do not want to display in the main list. The following archive options are available:</p>
<ul>
<li><strong>False Positive</strong>: Removes the action item from your active list and suppresses it indefinitely. Rationale text is optional.</li>
<li><strong>Accept Risk</strong>: Removes the action item from your active list and suppresses it indefinitely. Rationale text is required.</li>
<li><strong>Other</strong>: Removes the action item from your active list and suppresses it indefinitely. Rationale text is required.</li>
</ul>
<p>You can move an action item from the archive back to the active list at any time.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="archiving-suspicious-activity">Archiving suspicious activity</h3>
@markup("md", "content/.markup/bodies/360.md")
</aside>
<h3 id="audit-log-api-endpoints">Audit log API endpoints</h3>
<p>To view when an action item’s status was changed and the rationale provided for that change, use the following API commands to retrieve audit logs:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td><code>/api/accounts/{accountID}/insights/audit-log</code></td>
<td>List all audit logs for an account</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/api/accounts/{accountID}/insights/{insightID}/audit-log</code></td>
<td>List audit logs for a specific issue</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/api/accounts/{accountID}/issues/audit-log</code></td>
<td>List all audit logs for account issues</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/api/accounts/{accountID}/issues/{insightID}/audit-log</code></td>
<td>List all audit logs for a specific issue</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/api/accounts/{accountID}/zones/{zoneID}/insights/audit-log</code></td>
<td>List all audit logs for a domain</td>
</tr>
<tr>
<td><code>GET</code></td>
<td><code>/api/accounts/{accountID}/zones/{zoneID}/insights/{insightID}/audit-log</code></td>
<td>List audit logs for a specific issue in a domain</td>
</tr>
</tbody>
</table>
<p>Refer to our <a href="/api/resources/security_center">Security Center API documentation</a> to review the action item audit logs by account, domain, or a specific <code>issue_id</code>.</p>
<h2 id="detection-tools">Detection tools</h2>
<p>Review the available detection tools and what services are currently running to protect your domain against threats.</p>
<h2 id="traffic-overview">Traffic overview</h2>
<p>View the patterns and highlights from your domain's traffic in the past 30 days.</p>
<p>The Cloudflare dashboard displays:</p>
<ul>
<li><strong>Monthly requests</strong>: View the monthly requests and traffic that has been mitigated by Cloudflare.</li>
<li><strong>How you compare to your peers</strong>: For enterprise plans, understand how your security posture compares to others in your industry protected by Cloudflare.</li>
</ul>
