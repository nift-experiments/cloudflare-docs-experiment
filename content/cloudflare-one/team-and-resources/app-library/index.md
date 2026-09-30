---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/
  description: Application Library in Zero Trust.
  full_title: Application Library · Cloudflare One docs
  head_html: <title>Application Library · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Application Library in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/index.md"><meta property="og:title" content="Application Library · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Application Library in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/#page","headline":"Application Library \u00b7 Cloudflare One docs","description":"Application Library in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/app-library/
  schema: 1
---
<p>The Application Library allows users to manage their SaaS applications in Cloudflare One by consolidating views across all relevant products: <a href="/cloudflare-one/traffic-policies/">Gateway</a>, <a href="/cloudflare-one/access-controls/policies/">Access</a>, and <a href="/cloudflare-one/integrations/cloud-and-saas/">Cloud Access Security Broker (CASB)</a>. The App Library provides visibility and control for available applications, as well as the ability to view categorized hostnames and manage configuration for Access for SaaS and Gateway policies. For example, you can use the App Library to review how Gateway uses specific hostnames to match against application traffic.</p>
<p>To access the App Library in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Application library</strong>. Each application card will list the number of hostnames associated with the application, the supported Cloudflare One product usage, and the <a href="/cloudflare-one/traffic-policies/application-app-types/#app-types">app type</a>.</p>
<p>The App Library groups <a href="/cloudflare-one/traffic-policies/application-app-types/#do-not-inspect-applications">Do Not Inspect applications</a> within the corresponding application. For example, the App Library will group <em>Google Drive (Do Not Inspect)</em> under <strong>Google Drive</strong>. Traffic that does not match a known application will not be included in the App Library.</p>
<h2 id="view-application-details">View application details</h2>
<p>Select an application card to view details about the application.</p>
<h3 id="overview">Overview</h3>
<p>The <strong>Overview</strong> tab shows details about an application, including:</p>
<ul>
<li>Name</li>
<li>Shadow IT <a href="#review-applications">review status</a></li>
<li>Number of hostnames</li>
<li><a href="/cloudflare-one/traffic-policies/application-app-types/#app-types">App type</a></li>
<li>Supported Cloudflare One applications</li>
<li>Application ID for use with the API and Terraform</li>
</ul>
<h3 id="findings">Findings</h3>
<p>The <strong>Findings</strong> tab shows any connected <a href="/cloudflare-one/integrations/cloud-and-saas/#manage-casb-integrations">CASB integrations</a> for the selected application, as well as instances of any detected <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#posture-findings">posture findings</a> and <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#content-findings">content findings</a> for each integration.</p>
<h3 id="policies">Policies</h3>
<p>The <strong>Policies</strong> tab shows any <a href="/cloudflare-one/traffic-policies/">Gateway</a> and <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS</a> policies related to the selected application.</p>
<h3 id="usage">Usage</h3>
<p>The <strong>Usage</strong> tab shows any logs for <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway traffic requests</a>, <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#authentication-logs">Access authentication events</a>, <a href="/cloudflare-one/insights/analytics/shadow-it-discovery/">Shadow IT Discovery user sessions</a>, and <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#view-prompt-logs">generative AI prompt logs</a> sent to the selected application. This section requires logs to be turned on for each feature.</p>
<p>The Shadow IT Discovery dashboard will provide more details for discovered applications. To access Shadow IT Discovery in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Dashboards</strong>, then select <strong>Shadow IT: SaaS analytics</strong> or <strong>Shadow IT: Private Network analytics</strong>.</p>
<h2 id="review-applications">Review applications</h2>
<p>The App Library synchronizes application review statuses with approval statuses from the <a href="/cloudflare-one/insights/analytics/shadow-it-discovery/">Shadow IT Discovery SaaS analytics</a> dashboard.</p>
<p>To organize applications into their approval status for your organization, you can mark them as <strong>Unreviewed</strong> (default), <strong>In review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong>.</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>API value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Approved</td>
<td><code>approved</code></td>
<td>Applications that have been marked as sanctioned by your organization.</td>
</tr>
<tr>
<td>Unapproved</td>
<td><code>unapproved</code></td>
<td>Applications that have been marked as unsanctioned by your organization.</td>
</tr>
<tr>
<td>In review</td>
<td><code>in review</code></td>
<td>Applications in the process of being reviewed by your organization.</td>
</tr>
<tr>
<td>Unreviewed</td>
<td><code>unreviewed</code></td>
<td>Unknown applications that are neither sanctioned nor being reviewed by your organization at this time.</td>
</tr>
</tbody>
</table>
<p>To set the status of an application:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Applications</strong>.</li>
<li>Locate the card for the application.</li>
<li>In the three-dot menu, select the option to mark your desired status.</li>
</ol>
<p>Once you mark the status of an application, its badge will change. You can filter applications by their status to review each application in the list for your organization. The review status for an application in the App Library and Shadow IT Discovery will update within one hour.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4425.md")
</aside>
<h2 id="application-confidence-scorecards">Application confidence scorecards</h2>
<p>Application confidence scorecards provide automated risk assessment for AI and SaaS applications to help organizations make informed decisions about application approval and security policies. These scores bring scale and automation to the labor- and time-intensive task of evaluating generative AI and SaaS applications.</p>
<p>The scoring system evaluates applications across multiple security, compliance, and operational dimensions to generate two complementary scores: the Application Posture Score and the Generative AI Posture Score. These scores help security teams identify risks in Shadow AI and Shadow IT deployments without manual auditing of every application.</p>
<p>To view an application's confidence scorecard:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Application library</strong></li>
<li>Find the application you would like to review or search it by name.</li>
<li>Review the Application Posture Score and the Generative AI Posture Score which are generated on the application card.</li>
</ol>
<h3 id="scoring-methodology">Scoring methodology</h3>
<h4 id="application-posture-score-5-points">Application Posture Score (5 points)</h4>
<p>The Application Posture Score evaluates SaaS providers across five major categories.</p>
<table>
<thead>
<tr>
<th>Category</th>
<th align="center">Points</th>
<th>Assessment Criteria</th>
<th>Scoring Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security and Privacy Compliance</td>
<td align="center">1.2</td>
<td>Presence of SOC 2 and ISO 27001 certifications, which signal operational maturity and adherence to security frameworks.</td>
<td>Full credit awarded for both certifications; partial credit for one certification; no credit if neither certification is present.</td>
</tr>
<tr>
<td>Data Management Practices</td>
<td align="center">1.0</td>
<td>Data retention windows and whether the provider shares data with third parties.</td>
<td>Shorter retention periods and no third-party data sharing earn the highest marks. Applications with indefinite data retention or extensive data sharing receive lower scores.</td>
</tr>
<tr>
<td>Security Controls</td>
<td align="center">1.0</td>
<td>Support for Multi-Factor Authentication (MFA), Single Sign-On (SSO), TLS 1.3, role-based access controls, and session monitoring capabilities.</td>
<td>These represent table stakes of modern SaaS security. Full credit requires comprehensive support across all controls; partial credit awarded for subset implementation.</td>
</tr>
<tr>
<td>Security Reports and Incident History</td>
<td align="center">1.0</td>
<td>Availability of trust or security pages, active bug bounty programs, incident response transparency, and recent breach history.</td>
<td>Recent material breaches result in full point deduction. Proactive security measures like bug bounty programs and transparent incident reporting increase scores.</td>
</tr>
<tr>
<td>Financial Stability</td>
<td align="center">0.8</td>
<td>Company financial status, funding levels, and operational stability.</td>
<td>Public companies and heavily capitalized providers score highest, while startups with limited funding or companies in financial distress receive lower scores.</td>
</tr>
<tr>
<td>Total Points</td>
<td align="center">5.0</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h4 id="generative-ai-posture-score-5-points">Generative AI Posture Score (5 points)</h4>
<table>
<thead>
<tr>
<th>Category</th>
<th align="center">Points</th>
<th>Assessment Criteria</th>
<th>Scoring Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Compliance</td>
<td align="center">1.0</td>
<td>Presence of ISO 42001 certification for AI management systems.</td>
<td>Full credit for ISO 42001 certification; no credit without this specialized AI governance certification.</td>
</tr>
<tr>
<td>Deployment Security Model</td>
<td align="center">1.0</td>
<td>Whether application access requires authentication and implements rate limiting, or if services are publicly exposed without controls.</td>
<td>Authenticated access with proper rate limiting receives full credit; publicly exposed services without controls receive minimal scoring.</td>
</tr>
<tr>
<td>System Card</td>
<td align="center">1.0</td>
<td>Publication of model or system cards documenting safety evaluations, bias testing, and risk assessments.</td>
<td>Comprehensive system cards with detailed safety and bias documentation receive full credit; incomplete or missing documentation results in score reduction.</td>
</tr>
<tr>
<td>Training Data Governance</td>
<td align="center">2.0</td>
<td>Whether user data is explicitly excluded from model training and availability of opt-in/opt-out controls for training data usage.</td>
<td>Explicit exclusion of user data from training receives maximum points; opt-in/opt-out controls receive partial credit; no controls or guaranteed user data training receives minimal scoring.</td>
</tr>
<tr>
<td><strong>Total Points</strong></td>
<td align="center"><strong>5.0</strong></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="automated-scoring-infrastructure">Automated scoring infrastructure</h3>
<h4 id="web-crawling-and-data-extraction">Web crawling and data extraction</h4>
<p>The scoring system employs automated infrastructure to crawl and analyze public information sources.</p>
<ul>
<li>Data sources: Trust centers, privacy policies, security pages, compliance documents, and vendor documentation.</li>
<li>Extraction process: Large language models parse documents to identify relevant information, with structured extraction methods to resist hallucinations and ensure accuracy.</li>
<li>Validation requirements: Source validation and structured data extraction prevent false positives and ensure reliable scoring.</li>
</ul>
<h4 id="human-oversight-and-quality-assurance">Human oversight and quality assurance</h4>
<p>Automated results are supplemented with manual review to maintain transparency and ensure data integrity.</p>
<ul>
<li>Review process: Every automated score undergoes review and audit by Cloudflare analysts before publication in the Application Library.</li>
<li>Validation methodology: Combination of automated crawling and extraction with human validation ensures comprehensive and trustworthy scoring.</li>
<li>Update frequency: Scores update dynamically as vendors improve security and compliance postures, providing live assessment rather than static reports.</li>
</ul>
<h4 id="report-score-inaccuracies">Report score inaccuracies</h4>
<p>If you believe one of the Application confidence scores is incorrect or have additional evidence that should be considered in the scoring process, contact <code>app-confidence-scores@cloudflare.com</code>. Include relevant documentation or evidence that supports your assessment to help us review and update the score accordingly.</p>
