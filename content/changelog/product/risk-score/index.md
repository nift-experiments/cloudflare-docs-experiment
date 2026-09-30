<h1 id="changelog">Changelog</h1>

<h2 id="user-risk-scoring-for-high-risk-browsing-activity"><a href="/changelog/post/2026-04-08-high-risk-browsing/">User risk scoring for high risk browsing activity</a></h2>
<p><em>2026-04-08</em></p>
<p>Cloudflare One's <strong>User Risk Scoring</strong> now incorporates direct signals from <strong>Gateway DNS traffic patterns</strong>. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.</p>
<h4 id="2026-04-08-high-risk-browsing-why-this-matters">Why this matters</h4>
<p>Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:</p>
<ul>
<li><strong>Security threats</strong>: Domains associated with malware, phishing, or command-and-control (C2) centers.</li>
<li><strong>High-risk content</strong>: Categories such as questionable content or violence that may violate corporate compliance.</li>
</ul>
<p>Even if a Gateway policy is set to <strong>Block</strong> the traffic, the interaction is still captured as a &quot;hit&quot; to ensure the user's risk profile reflects the attempted activity.</p>
<h4 id="2026-04-08-high-risk-browsing-new-risk-behaviors">New risk behaviors</h4>
<p>Two new behaviors are now available in the dashboard:</p>
<ul>
<li><strong>Suspicious Security Domain Visited</strong>: Triggers when a user visits a domain in the security threats or security risk categories.</li>
<li><strong>High risk domain visited</strong>: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.</li>
</ul>
<p>To learn more and get started, refer to the <a href="/cloudflare-one/team-and-resources/users/risk-score/">User Risk Scoring documentation</a>.</p>


<h2 id="support-for-crowdstrike-device-scores-in-user-risk-scoring"><a href="/changelog/post/2026-1-15-crowdstrike-score/">Support for CrowdStrike device scores in User Risk Scoring</a></h2>
<p><em>2026-01-15</em></p>
<p>Cloudflare One has expanded its [User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the [CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).</p>
<p>Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.</p>
<p>New risk behaviors
The following risk scoring behaviors are now available:</p>
<ul>
<li>CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a &quot;Low&quot; score from CrowdStrike.</li>
<li>CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a &quot;Medium&quot; score from CrowdStrike.</li>
</ul>
<p>These scores are derived from [CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.</p>


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



