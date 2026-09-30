---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/
  description: How Risk score works in Zero Trust.
  full_title: User risk score · Cloudflare One docs
  head_html: <title>User risk score · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Risk score works in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/index.md"><meta property="og:title" content="User risk score · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Risk score works in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Okta,SentinelOne"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#page","headline":"User risk score \u00b7 Cloudflare One docs","description":"How Risk score works in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Okta","SentinelOne"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/users/risk-score/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5955.md")
</aside>
<p>Cloudflare One risk scoring detects user activity and behaviors that could introduce risk to your organization's systems and data. Risk scores add user and entity behavior analytics (UEBA) to the Cloudflare One platform.</p>
<h2 id="user-risk-scoring">User risk scoring</h2>
<p>Cloudflare One assigns a risk score of Low, Medium, or High based on detections of users' activities, posture, and settings. A user's score is equal to the highest-level risk behavior they trigger.</p>
<h3 id="view-a-user-s-risk-score">View a user's risk score</h3>
<p>To view a user's risk score:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Teams &amp; Resources</strong>.</li>
<li>Select <strong>Users</strong>.</li>
<li>Select <strong>Risk score</strong> &gt; <strong>Risk scoring</strong>.</li>
<li>Select a user's name to view their instances of risk behaviors, if any. You can select an instance of a risk behavior to view the log associated with the detection.</li>
</ol>
<p>Users that have had their risk score <a href="#clear-a-users-risk-score">cleared</a> will not appear in the table unless they trigger another risk behavior.</p>
<h3 id="clear-a-user-s-risk-score">Clear a user's risk score</h3>
<p>If required, you can reset risk scores for specific users. Once reset, users will not appear in the associated risk table until they trigger another risk behavior.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Teams &amp; Resources</strong>.</li>
<li>Select <strong>Risk score</strong> &gt; <strong>Risk scoring</strong>.</li>
<li>Select the user you want to clear the risk score for.</li>
<li>In <strong>User risk overview</strong>, select <strong>Reset user risk</strong>.</li>
<li>Select <strong>Confirm</strong>.</li>
</ol>
<h3 id="send-risk-score-to-okta">Send risk score to Okta</h3>
<p>In addition to controls in Cloudflare One, Okta users can send risk scores to Okta to apply SSO-level policies.</p>
<p>First, configure Cloudflare One to send user risk scores to Okta.</p>
<ol>
<li>Set up the <a href="/cloudflare-one/integrations/identity-providers/okta/">Okta SSO integration</a>.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>In <strong>Your identity providers</strong>, locate your Okta integration and select <strong>Edit</strong>.</li>
<li>Turn on <strong>Send risk score to Okta</strong>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.</li>
</ol>
<p>Next, configure Okta to receive your risk scores.</p>
<ol>
<li>On your Okta admin dashboard, go to <strong>Security</strong> &gt; <strong>Device Integrations</strong>.</li>
<li>Go to <strong>Receive shared signals</strong>, then select <strong>Create stream</strong>.</li>
<li>Name your integration. In <strong>Set up integration with</strong>, choose <em>Well-known URL</em>.</li>
<li>In <strong>Well-known URL</strong>, enter the well-known URL value provided by Cloudflare One.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>For more information on configuring user risk score within Okta, refer to the <a href="https://help.okta.com/oie/en-us/content/topics/itp/overview.htm">Okta documentation</a>.</p>
<p>While the Okta integration is turned on, Cloudflare One will send any user risk score updates to Okta, including score increases and resets. Score update events will appear in your <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a>.</p>
<h2 id="predefined-risk-behaviors">Predefined risk behaviors</h2>
<p>By default, all predefined behaviors are disabled. When a behavior is enabled, Cloudflare One will continuously evaluate all users within the organization for the behavior. You can <a href="#change-risk-behavior-risk-levels">change the risk level</a> for predefined behaviors if the default assignment does not suit your environment.</p>
<table>
<thead>
<tr>
<th>Risk behavior</th>
<th>Requirements</th>
<th>Description</th>
<th>Evaluation timing</th>
</tr>
</thead>
<tbody>
<tr>
<td>Impossible travel</td>
<td><a href="/cloudflare-one/access-controls/applications/http-apps/">A configured Access application</a></td>
<td>User has a successful login from two different locations that they could not have traveled between in that period of time. Matches will appear in your <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a>.</td>
<td>Evaluated at each authentication and session-refresh event.</td>
</tr>
<tr>
<td>High number of DLP policies triggered</td>
<td><a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">A configured DLP profile</a></td>
<td>User has created a high number of DLP policy matches within a narrow frame of time. Matches will appear in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</td>
<td>Evaluated per-request in milliseconds.</td>
</tr>
<tr>
<td>SentinelOne threat detected on machine</td>
<td><a href="/cloudflare-one/integrations/service-providers/sentinelone/">SentinelOne service provider integration</a></td>
<td>SentinelOne returns one or more configured <a href="/cloudflare-one/integrations/service-providers/sentinelone/#device-posture-attributes">device posture attributes</a> for a user.</td>
<td>Ingested via service-to-service API. Frequency is administrator-configurable during device posture setup to align with SentinelOne's API rate limits.</td>
</tr>
<tr>
<td>CrowdStrike Low ZTA security score</td>
<td><a href="/cloudflare-one/integrations/service-providers/crowdstrike/">CrowdStrike integration</a></td>
<td>A user's device reports a score between 0-50 for any CrowdStrike Zero Trust Assessment attribute (OS Score, Overall Score, or Sensor Config score). Refer to <a href="/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes">CrowdStrike device posture attributes</a> for more information.</td>
<td>Ingested via service-to-service API. Frequency is administrator-configurable during device posture setup to align with CrowdStrike's API rate limits.</td>
</tr>
<tr>
<td>CrowdStrike Medium ZTA security score</td>
<td><a href="/cloudflare-one/integrations/service-providers/crowdstrike/">CrowdStrike integration</a></td>
<td>A user's device reports a score between 50-79 for any CrowdStrike Zero Trust Assessment attribute (OS Score, Overall Score, or Sensor Config score). Refer to <a href="/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes">CrowdStrike device posture attributes</a> for more information.</td>
<td>Ingested via service-to-service API. Frequency is administrator-configurable during device posture setup to align with CrowdStrike's API rate limits.</td>
</tr>
<tr>
<td>Interaction with Malicious File</td>
<td><a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">Gateway AV scanning</a> or <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">File sandboxing</a></td>
<td>User uploads or downloads a file flagged as malicious by Gateway's AV scanner or file sandboxing. Risk is elevated even if the file is blocked.</td>
<td>Evaluated per-request in milliseconds.</td>
</tr>
<tr>
<td>Suspicious Security Domain Visited</td>
<td><a href="/cloudflare-one/traffic-policies/dns-policies/">Gateway DNS policies</a></td>
<td>User visits a domain categorized as a security risk or security threat. Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">domain categories</a> for the full list. Risk is elevated even if the traffic is blocked.</td>
<td>Evaluated per-request in milliseconds.</td>
</tr>
<tr>
<td>High Risk Domain Visited</td>
<td><a href="/cloudflare-one/traffic-policies/dns-policies/">Gateway DNS policies</a></td>
<td>User visits a domain categorized as questionable content, violence, or CIPA. Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">domain categories</a> for the full list. Risk is elevated even if the traffic is blocked.</td>
<td>Evaluated per-request in milliseconds.</td>
</tr>
</tbody>
</table>
<h2 id="manage-risk-behaviors">Manage risk behaviors</h2>
<p>To toggle risk behaviors, go to <strong>Risk score</strong> &gt; <strong>Risk behaviors</strong>.</p>
<h3 id="enable-risk-behaviors">Enable risk behaviors</h3>
<p>When a specific behavior is enabled, Cloudflare One will continuously monitor all users within the organization for any instances of that behavior.</p>
<p>If a user engages in an enabled risk behavior, their risk level is re-evaluated. Cloudflare One will update their risk score to the highest value between the current risk level and the risk level of the behavior they triggered.</p>
<h3 id="disable-risk-behaviors">Disable risk behaviors</h3>
<p>When a risk behavior is disabled, monitoring for future activity will cease. Previously detected risk behaviors will remain in the logs and associated with a user.</p>
<h3 id="change-risk-behavior-risk-levels">Change risk behavior risk levels</h3>
<p>You can change the risk level for a behavior at any time.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Teams &amp; Resources</strong>.</li>
<li>Go to <strong>Users</strong>.</li>
<li>Select <strong>Risk score</strong> &gt; <strong>Risk behaviors</strong>.</li>
<li>Select the risk behavior you want to modify.</li>
<li>In the drop-down menu, choose your desired risk level.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="use-risk-scores-in-access-policies">Use risk scores in Access policies</h2>
<p>You can use risk scores to control access to applications protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>. This enables adaptive access control that responds to changes in user behavior.</p>
<p>To add a risk score requirement to an Access policy:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong>.</li>
<li>Create a new policy or select an existing policy to edit.</li>
<li>Add a rule with the <em>User Risk Score</em> selector.</li>
<li>For <strong>Value</strong>, select one or more risk levels (Low, Medium, High, or Unscored). The rule matches a user only when their current risk level is one of the selected values.</li>
<li>Save the policy.</li>
</ol>
<h3 id="example-block-high-risk-users">Example: Block high-risk users</h3>
<p>To prevent users with elevated risk scores from accessing sensitive applications, create a policy with the following configuration:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Include</td>
<td>Emails ending in</td>
<td><code>@example.com</code></td>
</tr>
<tr>
<td></td>
<td>Exclude</td>
<td>User risk score</td>
<td><em>High</em></td>
</tr>
</tbody>
</table>
<p>Users with a High risk score will be blocked, while users with Low or Medium scores can access the application.</p>
<p>For more information on Access policies, refer to <a href="/cloudflare-one/access-controls/policies/">Access policies</a>.</p>
