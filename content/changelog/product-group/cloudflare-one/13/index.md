<h1 id="changelog">Changelog</h1>

<h2 id="increased-transparency-for-phishing-email-submissions"><a href="/changelog/post/2024-12-19-reclassification-tab/">Increased transparency for phishing email submissions</a></h2>
<p><em>2024-12-19</em></p>
<p>You now have more transparency about team and user submissions for phishing emails through a <strong>Reclassification</strong> tab in the Zero Trust dashboard.</p>
<p>Reclassifications happen when users or admins <a href="/cloudflare-one/email-security/settings/phish-submissions/">submit a phish</a> to Email security. Cloudflare reviews and - in some cases - reclassifies these emails based on improvements to our machine learning models.</p>
<p>This new tab increases your visibility into this process, allowing you to view what submissions you have made and what the outcomes of those submissions are.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassifications-tab.png" alt="Use the Reclassification area to review submitted phishing emails" /></p>


<h2 id="troubleshoot-tunnels-with-diagnostic-logs"><a href="/changelog/post/2024-12-19-diagnostic-logs/">Troubleshoot tunnels with diagnostic logs</a></h2>
<p><em>2024-12-19</em></p>
<p>The latest <code>cloudflared</code> build <a href="https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2">2024.12.2</a> introduces the ability to collect all the diagnostic logs needed to troubleshoot a <code>cloudflared</code> instance.</p>
<p>A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine and outputs it to a <code>cloudflared-diag</code> file.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</p>


<h2 id="establish-bgp-peering-over-direct-cni-circuits"><a href="/changelog/post/2024-12-17-bgp-support-cni/">Establish BGP peering over Direct CNI circuits</a></h2>
<p><em>2024-12-17</em></p>
<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Magic WAN BGP peering</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Magic Transit BGP peering</a> to learn more about this feature and how to set it up.</p>


<h2 id="generate-customized-terraform-files-for-building-cloud-network-on-ramps"><a href="/changelog/post/2024-12-05-cloud-onramp-terraform/">Generate customized terraform files for building cloud network on-ramps</a></h2>
<p><em>2024-12-05</em></p>
<p>You can now generate customized terraform files for building cloud network on-ramps to <a href="/cloudflare-wan/">Magic WAN</a>.</p>
<p><a href="/multi-cloud-networking/">Magic Cloud</a> can scan and discover existing network resources and generate the required terraform files to automate cloud resource deployment using their existing infrastructure-as-code workflows for cloud automation.</p>
<p>You might want to do this to:</p>
<ul>
<li>Review the proposed configuration for an on-ramp before deploying it with Cloudflare.</li>
<li>Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.</li>
</ul>
<p>For more details, refer to <a href="/multi-cloud-networking/cloud-on-ramps/#set-up-with-terraform">Set up with Terraform</a>.</p>


<h2 id="find-security-misconfigurations-in-your-aws-cloud-environment"><a href="/changelog/post/2024-11-22-cloud-data-extraction-aws/">Find security misconfigurations in your AWS cloud environment</a></h2>
<p><em>2024-11-22</em></p>
<p>You can now use CASB to find security misconfigurations in your AWS cloud environment using <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a>.</p>
<p>You can also <a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/#compute-account">connect your AWS compute account</a> to extract and scan your S3 buckets for sensitive data while avoiding egress fees. CASB will scan any objects that exist in the bucket at the time of configuration.</p>
<p>To connect a compute account to your AWS integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find and select your AWS integration.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to connect a new compute account.</li>
<li>Select <strong>Refresh</strong>.</li>
</ol>


<h2 id="improved-non-english-keyboard-support"><a href="/changelog/post/2024-11-21-non-english-keyboard/">Improved non-English keyboard support</a></h2>
<p><em>2024-11-21</em></p>
<p>You can now type in languages that use diacritics (like á or ç) and character-based scripts (such as Chinese, Japanese, and Korean) directly within the remote browser. The isolated browser now properly recognizes non-English keyboard input, eliminating the need to copy and paste content from a local browser or device.</p>


<h2 id="use-logpush-for-email-security-user-actions"><a href="/changelog/post/2024-11-07-logpush-user-actions/">Use Logpush for Email security user actions</a></h2>
<p><em>2024-11-07T23:22:49+00:00</em></p>
<p>You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.</p>
<p>When creating a new Logpush job, remember to select <strong>Audit logs</strong> as the dataset and filter by:</p>
<ul>
<li><strong>Field</strong>: <code>&quot;ResourceType&quot;</code></li>
<li><strong>Operator</strong>: <code>&quot;starts with&quot;</code></li>
<li><strong>Value</strong>: <code>&quot;email_security&quot;</code>.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-User-Actions.png" alt="Logpush-user-actions" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs">Enable user action logs</a>.</p>
<p>This feature is available across all Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="search-for-custom-rules-using-rule-name-and-or-id"><a href="/changelog/post/2024-10-02-custom-rule-search/">Search for custom rules using rule name and/or ID</a></h2>
<p><em>2024-10-02</em></p>
<p>The Magic Firewall dashboard now allows you to search custom rules using the rule name and/or ID.</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Network Analytics</strong>.</li>
<li>Select <strong>Magic Firewall</strong>.</li>
<li>Add a filter for <strong>Rule ID</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/cloudflare-network-firewall/search-with-rule-id.png" alt="Search for firewall rules with rule IDs" /></p>
<p>Additionally, the rule ID URL link has been added to Network Analytics.</p>


<h2 id="eliminate-long-lived-credentials-and-enhance-ssh-security-with-cloudflare-access-for-infrastructure"><a href="/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/">Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure</a></h2>
<p><em>2024-10-01</em></p>
<p>Organizations can now eliminate long-lived credentials from their SSH setup and enable strong multi-factor authentication for SSH access, similar to other Access applications, all while generating access and command logs.</p>
<p>SSH with <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> uses short-lived SSH certificates from Cloudflare, eliminating SSH key management and reducing the security risks associated with lost or stolen keys. It also leverages a common deployment model for Cloudflare One customers: <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/">WARP-to-Tunnel</a>.</p>
<p>SSH with Access for Infrastructure enables you to:</p>
<ul>
<li><strong>Author fine-grained policy</strong> to control who may access your SSH servers, including specific ports, protocols, and SSH users.</li>
<li><strong>Monitor infrastructure access</strong> with Access and SSH command logs, supporting regulatory compliance and providing visibility in case of security breach.</li>
<li><strong>Preserve your end users' workflows.</strong> SSH with Access for Infrastructure supports native SSH clients and does not require any modifications to users’ SSH configs.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/infrastructure-app.png" alt="Example of an infrastructure Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Access for Infrastructure</a>.</p>


<h2 id="exchange-user-risk-scores-with-okta"><a href="/changelog/post/2024-06-17-okta-risk-exchange/">Exchange user risk scores with Okta</a></h2>
<p><em>2024-06-17</em></p>
<p>Beyond the controls in <a href="/cloudflare-one/">Zero Trust</a>, you can now <a href="/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta">exchange user risk scores</a> with Okta to inform SSO-level policies.</p>
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


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/12/">Previous</a><span>Page 13 of 13</span></nav>
