---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/
  description: Manage findings in Cloudflare One.
  full_title: Manage security findings · Cloudflare One docs
  head_html: <title>Manage security findings · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage findings in Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/index.md"><meta property="og:title" content="Manage security findings · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage findings in Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/#page","headline":"Manage security findings \u00b7 Cloudflare One docs","description":"Manage findings in Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/cloud-and-saas-findings/manage-findings/
  schema: 1
---
<p>Findings are security issues detected within SaaS and cloud applications that involve users, data at rest (files stored in your apps), and other configuration settings. With Cloudflare CASB, you can review a comprehensive list of findings in Cloudflare One and take action on the issues found.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>You have added a <a href="/cloudflare-one/integrations/cloud-and-saas/">Cloud and SaaS integration</a>.</li>
<li>Your scan has surfaced at least one security finding.</li>
</ul>
<h2 id="posture-findings">Posture findings</h2>
<p>Posture findings include misconfigurations, unauthorized user activity, and other data security issues.</p>
<p>To view details about the posture findings that CASB found:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</li>
<li>Choose <strong>SaaS</strong> or <strong>Cloud</strong>.</li>
<li>To view details about a finding, select the finding's name</li>
</ol>
<p>Cloud &amp; SaaS findings will display details about your posture finding, including the finding type, <a href="#severity-levels">severity level</a>, number of instances, associated integration, current status, and date detected. For more information on each instance of the finding, select <strong>Manage</strong>.</p>
<p>To manage the finding's visibility, you can update the finding's <a href="#severity-levels">severity level</a> or <a href="#hide-findings">hide the finding</a> from view. You can also <a href="#send-webhook">send a posture finding instance to a webhook</a>. Some findings also provide a remediation guide to resolve the issue.</p>
<h3 id="severity-levels">Severity levels</h3>
<p>Cloudflare CASB labels each finding with one of the following severity levels:</p>
<table>
<thead>
<tr>
<th>Severity level</th>
<th>Urgency</th>
</tr>
</thead>
<tbody>
<tr>
<td>Critical</td>
<td>Suggests the finding is something your team should act on today.</td>
</tr>
<tr>
<td>High</td>
<td>Suggests the finding is something your team should act on this week.</td>
</tr>
<tr>
<td>Medium</td>
<td>Suggests the finding should be reviewed sometime this month.</td>
</tr>
<tr>
<td>Low</td>
<td>Suggests the finding is informational or part of a scheduled review process.</td>
</tr>
</tbody>
</table>
<h4 id="change-the-severity-level">Change the severity level</h4>
<p>You can change the severity level for a finding at any time in case the default assignment does not suit your environment:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</li>
<li>Locate the finding you want to modify and select <strong>Manage</strong>.</li>
<li>In the severity level drop-down menu, choose your desired setting (<em>Critical</em>, <em>High</em>, <em>Medium</em>, or <em>Low</em>).</li>
</ol>
<p>The new severity level will only apply to the posture finding within this specific integration. If you added multiple integrations of the same application, the other integrations will not be impacted by this change.</p>
<h2 id="content-findings">Content findings</h2>
<p>Content findings include instances of potential data exposure as identified by <a href="/cloudflare-one/data-loss-prevention/">DLP</a>.</p>
<p>To view details about the content findings that CASB found:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Content Findings</strong>.</li>
<li>Choose <strong>SaaS</strong> or <strong>Cloud</strong>.</li>
<li>To view details about a finding, select the finding's name.</li>
</ol>
<p>Cloud &amp; SaaS findings will display details about your content finding, including the file name, a link to the file, matching DLP profiles, associated integration, and date detected.</p>
<p>AWS users can configure a <a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/#compute-account">compute account</a> to scan for data security resources within their S3 resources.</p>
<h2 id="view-shared-files">View shared files</h2>
<p>File findings for some integrations (such as <a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/#file-sharing">Microsoft 365</a> and <a href="/cloudflare-one/integrations/cloud-and-saas/box/#file-sharing">Box</a>) may link to an inaccessible file. To access the actual shared file:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4527.md")
</div></div>
<h2 id="hide-findings">Hide findings</h2>
<p>After reviewing your findings, you may decide that certain posture findings are not applicable to your organization. Cloudflare CASB allows you to remove findings or individual instances of findings from your list of active issues. CASB will continue to scan for these issues, but any detections will appear in a separate tab.</p>
<ul>
<li><strong>Ignore a finding</strong> — Moves the entire finding type from <strong>Active</strong> to <strong>Ignored</strong>. New detections of this finding type still appear, but in the <strong>Ignored</strong> tab.</li>
<li><strong>Hide an instance</strong> — Moves a single occurrence from <strong>Active</strong> to <strong>Hidden</strong>. Future occurrences for the same user or file go to the <strong>Hidden</strong> tab automatically.</li>
</ul>
<h3 id="ignore-a-finding">Ignore a finding</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</li>
<li>Locate the active finding you want to hide.</li>
<li>In the three-dot menu, select <strong>Move to ignore</strong>.</li>
</ol>
<p>The finding's status will change from <strong>Active</strong> to <strong>Ignored</strong>. CASB will continue to scan for these findings and report detections. You can change ignored findings back to <strong>Active</strong> with the same process at any time.</p>
<h3 id="hide-an-instance-of-a-finding">Hide an instance of a finding</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</li>
<li>Choose the active finding you want to hide, then select <strong>Manage</strong>.</li>
<li>In <strong>Active</strong>, find the instance you want to hide.</li>
<li>In the three-dot menu, select <strong>Move to hidden</strong>.</li>
</ol>
<p>The instance will be moved from <strong>Active</strong> to <strong>Hidden</strong> within the finding. If the finding occurs again for the same user, CASB will report the new instance quietly in the <strong>Hidden</strong> tab. You can move hidden instances back to the <strong>Active</strong> tab at any time.</p>
<h2 id="send-webhook">Send webhook</h2>
<p>After you configure one or more <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a>, you can send posture finding instances to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.</p>
<p>CASB webhooks currently support posture finding instances only.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</li>
<li>Choose <strong>SaaS</strong> or <strong>Cloud</strong>.</li>
<li>Choose the finding you want to review, then select <strong>Manage</strong>.</li>
<li>In <strong>Active Instances</strong>, select an instance.</li>
<li>In the instance details panel, select <strong>Send webhook</strong>.</li>
<li>Choose the webhook destination or destinations you want to use.</li>
<li>Select <strong>Send webhooks</strong>.</li>
</ol>
<p>Cloudflare queues webhook sends in the background. A success message means that Cloudflare accepted the request for delivery.</p>
<p>To validate a destination before sending a live finding instance, use <strong>Test delivery</strong> from the <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">Webhooks</a> page.</p>
<h2 id="remediate-findings">Remediate findings</h2>
<p>In addition to detecting and surfacing misconfigurations or issues with SaaS and cloud applications, CASB can also remediate findings directly in applications.</p>
<h3 id="configure-remediation-permissions">Configure remediation permissions</h3>
<p>Before you can remediate findings, <a href="/cloudflare-one/integrations/cloud-and-saas/">add a new integration</a> and choose <em>Read-Write mode</em> during setup. Alternatively, you can update an existing integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Choose your integration, then select <strong>Configure</strong>.</li>
<li>In <strong>Integration permissions</strong>, choose <em>Read-Write mode</em>.</li>
<li>Select <strong>Update integration</strong>. CASB will redirect you to your Microsoft 365 configuration.</li>
<li>Sign in to your organization, then select <strong>Accept</strong>.</li>
</ol>
<p>CASB can now remediate supported findings directly.</p>
<h3 id="remediate-a-finding">Remediate a finding</h3>
<p>To remediate a supported finding:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>.</li>
<li>Choose a supported finding type, then select <strong>Manage</strong>.</li>
<li>In <strong>Active Instances</strong>, select an instance.</li>
<li>In <strong>Remediation details</strong>, choose a remediation action to take.</li>
</ol>
<p>CASB will begin remediating the instance.</p>
<h3 id="remediate-inherited-file-permissions">Remediate inherited file permissions</h3>
<p>CASB can remove supported permissions applied directly to a Microsoft 365 or Google Workspace resource. If a file inherits access from a parent folder or Shared Drive, change the permission on that parent resource. Changing the file itself does not remove the inherited access.</p>
<p>CASB does not automatically change permissions on parent resources. Changing a parent permission can affect every downstream file and folder that inherits it.</p>
<h4 id="microsoft-365">Microsoft 365</h4>
<p>CASB may show a separate finding for the parent folder that gives the file its permission. The remediation details may include <strong>Parent Folder Access</strong> links. Open the linked finding to remediate the parent folder separately.</p>
<p>When an inherited permission prevents remediation, CASB displays:</p>
<blockquote>
<p>Resource has inherited permissions. Remediate permissions at the folder or organizational level.</p>
</blockquote>
<h4 id="google-workspace">Google Workspace</h4>
<p>For Google Workspace, CASB does not identify the exact parent resource. Asset details may show the associated Shared Drive, but not the originating folder or permission.</p>
<p>When an inherited permission prevents remediation, CASB displays:</p>
<blockquote>
<p>Resource has inherited permissions from a parent resource. Direct remediation of the parent is not yet supported for Google Workspace.</p>
</blockquote>
<p>For example, a file inherits public access when its parent folder allows <strong>Anyone with the link</strong>. Change the parent folder's <strong>General access</strong> setting to remediate the finding.</p>
<p>A file can also inherit external access from a Shared Drive member. Change the relevant parent permission or Shared Drive membership to remediate the finding.</p>
<p>To remediate an inherited Google Workspace permission:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4528.md")
</div>
<p>CASB updates the finding after it receives updated asset data. The failed child-resource remediation remains in the remediation history.</p>
<h3 id="manage-remediated-findings">Manage remediated findings</h3>
<p>Remediated findings will appear in <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Posture Findings</strong>. The status of the finding will change depending on what action CASB has taken:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pending</td>
<td>CASB has set the finding to be remediated.</td>
</tr>
<tr>
<td>Processing</td>
<td>CASB is currently remediating the finding.</td>
</tr>
<tr>
<td>Validating</td>
<td>CASB successfully completed the remediation and is waiting for confirmation that the finding has been resolved.</td>
</tr>
<tr>
<td>Completed</td>
<td>CASB successfully remediated the finding and validated that the finding has been resolved.</td>
</tr>
<tr>
<td>Failed</td>
<td>CASB unsuccessfully remediated the finding.</td>
</tr>
<tr>
<td>Rejected</td>
<td>CASB does not have the correct permissions to remediate the finding.</td>
</tr>
</tbody>
</table>
<p>CASB may take up to 48 hours to validate a remediation.</p>
<p>If the status is <strong>Completed</strong>, remediation succeeded. If the status is <strong>Failed</strong> or <strong>Rejected</strong>, remediation failed, and you can select the finding to take action again. A <strong>Rejected</strong> status indicates that CASB does not have the correct permissions to remediate the finding.</p>
<p>CASB will log remediation actions in <strong>Logs</strong> &gt; <strong>Admin</strong>. For more information, refer to <a href="/cloudflare-one/insights/logs/">Cloudflare One Logs</a>.</p>
<p>To automatically remediate matching findings without reviewing each one, refer to <a href="/cloudflare-one/cloud-and-saas-findings/policies/">Remediation Policies</a>.</p>
