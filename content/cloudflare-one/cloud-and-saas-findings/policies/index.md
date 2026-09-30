---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/
  description: Automatically remediate findings or send webhooks with CASB policies in Cloudflare One.
  full_title: Remediation Policies · Cloudflare One docs
  head_html: <title>Remediation Policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Automatically remediate findings or send webhooks with CASB policies in Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/index.md"><meta property="og:title" content="Remediation Policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Automatically remediate findings or send webhooks with CASB policies in Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/#page","headline":"Remediation Policies \u00b7 Cloudflare One docs","description":"Automatically remediate findings or send webhooks with CASB policies in Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/cloud-and-saas-findings/policies/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/4523.md")
</aside>
<p>Use CASB policies to automatically remediate a finding or send a webhook as soon as CASB detects it. A policy defines the vendor, the finding type match, and the action Cloudflare should take.</p>
<p>Policies build on <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#remediate-findings">manual remediation</a> and <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a>. Instead of each finding instance needing to be actioned manually, a configured policy automatically triggers action on all newly discovered matching finding instances.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A configured <a href="/cloudflare-one/integrations/cloud-and-saas/">Cloud or SaaS integration</a>.</li>
<li><a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#configure-remediation-permissions">Read-Write permissions</a> on the integration, required for remediation actions.</li>
<li>A <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/#create-a-webhook">configured webhook destination</a>, required for webhook actions.</li>
</ul>
<h2 id="how-policies-work">How policies work</h2>
<p>When CASB detects a finding, it checks whether the finding matches a customer-configured policy. If a policy matches, Cloudflare runs the policy's configured action against that finding instance automatically.</p>
<p>A policy can run a remediation action, send a webhook, or both.</p>
<h2 id="create-a-policy">Create a policy</h2>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Policies</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Under <strong>Basic information</strong>, enter a <strong>Policy name</strong>. Optionally, enter a <strong>Description</strong>.</li>
<li>Under <strong>Choose how you want to trigger the policy</strong>, select a <strong>Vendor</strong>.</li>
<li>Select one or more <strong>Integrations</strong>, or select <strong>Apply to all integrations</strong> to apply the policy to every integration for the vendor.</li>
<li>Select a <strong>Finding type</strong>. Only finding types available for the selected vendor and integrations appear here.</li>
<li>Under <strong>Define what to do with findings that match your trigger</strong>, choose one or both actions:
<ul>
<li><strong>Run Remediation</strong> to have Cloudflare perform a first-party remediation action against the SaaS integration API. This option is only available for select finding types.</li>
<li><strong>Send webhooks</strong> to send a notification to one or more webhook destinations.</li>
</ul>
</li>
<li>Under <strong>Status</strong>, turn on <strong>Enable policy</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>Policies will be in effect for all newly discovered finding instances going forward. New or updated policies are not applied retroactively to existing finding instances.</p>
<p>CASB policies appear in a list showing each policy's name, integration, finding type, webhook, remediation action, status, and the time it last ran.</p>
<h3 id="run-remediations">Run remediations</h3>
<p>Remediation actions perform a first-party fix directly against the integration's API, such as revoking a public file share.</p>
<p>CASB currently supports remediation actions for Microsoft 365 and Google Workspace file and folder finding types. If a finding type does not support remediation, <strong>Run Remediation</strong> displays <strong>No automated remediation available for this finding type</strong> and cannot be enabled.</p>
<details class="nb-details"><summary>Supported findings for remediation</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4524.md")
</div></details>
<p>Remediation requires <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#configure-remediation-permissions">Read-Write permissions</a> on the integration. If the integration only has Read permissions, upgrade the integration before the policy can remediate matching findings.</p>
<p>For more information, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#manage-remediated-findings">Manage remediated findings</a>.</p>
<h3 id="send-webhooks">Send webhooks</h3>
<p>Webhook actions send the finding instance to a previously configured webhook destination. Use this to route findings to systems such as Slack, Microsoft Teams, Jira, ServiceNow, Tines, or a custom HTTPS endpoint.</p>
<p>When a policy sends a webhook, the payload uses the same format as a webhook sent manually from a finding instance. For the payload structure and field descriptions, refer to <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/#payload-format">Payload format</a>.</p>
<h2 id="edit-turn-off-or-delete-a-policy">Edit, turn off, or delete a policy</h2>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Policies</strong>.</li>
<li>Select the policy to update.</li>
<li>Modify the policy's basic information, trigger, or actions.</li>
<li>Select <strong>Save changes</strong>.</li>
</ol>
<p>To turn a policy on or off, use the <strong>Enable policy</strong> toggle under <strong>Status</strong>. A policy's status displays as <strong>Enabled</strong> or <strong>Disabled</strong> in the policy list. A disabled policy stops matching new findings until enabled again.</p>
<p>To delete a policy, open the policy and select <strong>Delete</strong>.</p>
<h2 id="logs">Logs</h2>
<p>Every policy produces two categories of logs, available under <strong>Insights</strong> in Cloudflare One:</p>
<ul>
<li><strong>Admin Activity logs</strong> record changes to a policy definition, including who created, edited, or disabled the policy, and when.</li>
<li><strong>Cloud &amp; SaaS Security policies logs</strong> record the runtime outcome of each policy invocation, including the finding that triggered the policy, the asset acted on, whether the action succeeded or failed, and the error returned by the vendor if it failed (for example, a <code>401 Unauthorized</code> response or a rate limit error).</li>
</ul>
<p>For compliance reporting, the Cloud &amp; SaaS Security policies log ties a specific finding to a specific automated action and timestamp.</p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/">Cloudflare One Logs</a>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Remediation actions in a policy are only available for Microsoft 365 and Google Workspace file and folder finding types.</li>
<li>CASB cannot remove permissions inherited from a parent resource by remediating the affected child. For vendor-specific behavior and manual remediation steps, refer to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#remediate-inherited-file-permissions">Remediate inherited file permissions</a>.</li>
<li>A policy only applies to new instances of a finding type detected after the policy is created.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For help diagnosing issues, refer to <a href="/cloudflare-one/integrations/cloud-and-saas/troubleshooting/casb/">CASB troubleshooting</a>.</p>
