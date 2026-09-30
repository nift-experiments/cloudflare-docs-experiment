<div class="nb-description">
@markup("md", "content/.markup/bodies/1467.md")
</div>
<p>Account abuse — bulk account creation and account takeover attacks — can cause financial losses and erode user trust. Fraud detection allows you to detect and mitigate these attacks among your traffic. You can use fraud signals to <a href="/waf/custom-rules/">update or create new rules</a> for suspicious account activity, or pass signals to your origin to integrate into authentication and authorization systems.</p>
<h2 id="availability">Availability</h2>
<p>Account Abuse Protection is available in Early Access for any <a href="/bots/get-started/bot-management">Bot Management Enterprise</a> customer. You can use these features at no additional cost for a limited period until they are generally available.</p>
<p>Contact your Cloudflare account team to request access.</p>
<hr />
<h2 id="concepts">Concepts</h2>
<h3 id="user-id">User ID</h3>
<p>User ID is a cryptographically hashed, per-zone identifier that customers can use in <a href="/waf/analytics/security-analytics/">Security Analytics</a>, <a href="/waf/custom-rules/">Security Rules</a>, and <a href="/rules/transform/managed-transforms/reference/">Managed Transforms</a>. Hashed User IDs are created by encrypting the primary credentials your users provide, converting them into opaque identifiers unique to your zone. This allows traffic analysis while protecting user privacy. With access to hashed User ID, website owners can:</p>
<ul>
<li>Review which users have the most activity on your website.</li>
<li>Find the details on a specific user's characteristics and activity patterns.</li>
<li>Mitigate traffic based on the user, such as blocking a user with historically suspicious activity.</li>
<li>Combine fields to see when accounts are being targeted with leaked credentials.</li>
<li>Manage network patterns or signals associated with specific users.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="data-privacy">Data privacy</h3>
@markup("md", "content/.markup/bodies/1466.md")
</aside>
<p>User ID is an opt-in feature that can be enabled in Security Settings.</p>
<p>To enable, edit, or disable the setting:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1468.md")
</div>
<h3 id="ephemeral-ids">Ephemeral IDs</h3>
<p>Customers using Cloudflare <a href="/turnstile/">Turnstile</a> can utilize ephemeral IDs for Fraud detection.</p>
<p>Refer to <a href="/turnstile/tutorials/fraud-detection-with-ephemeral-ids/">Fraud detection with ephemeral IDs</a> for more information.</p>
<h3 id="account-takeover-detections">Account takeover detections</h3>
<p>Cloudflare Bot Management includes dedicated detection IDs for account takeover attacks.</p>
<p>Refer to <a href="/bots/additional-configurations/detection-ids/account-takeover-detections/">Account takeover detections</a> for more information.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1465.md")
</aside>
<hr />
<h2 id="get-started">Get started</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>Fraud detection requires the following configurations and settings to be enabled to properly identify suspicious behavior.</p>
<h4 id="security-settings">Security Settings</h4>
<ul>
<li>User ID: Cloudflare encrypts or hashes your user IDs to better understand typical user traffic patterns across your applications. Enabling Cloudflare to create hashed user ID mappings to your users will allow you to receive account takeover and bulk account creation detections.</li>
</ul>
<h4 id="eligible-traffic">Eligible traffic</h4>
<p>Cloudflare automatically identifies certain login and sign up traffic on your applications and runs these detections without any additional configurations.</p>
<ul>
<li>Sign-ups: Cloudflare automatically monitors traffic on endpoints that match common sign up endpoints.</li>
<li>Login: Cloudflare automatically monitors traffic on endpoints that match common login endpoints.</li>
</ul>
<p>Verify that your endpoints are properly labeled to ensure Cloudflare can detect and monitor them correctly.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="login-or-sign-up-endpoints">Login or sign up endpoints</h3>
@markup("md", "content/.markup/bodies/1464.md")
</aside>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="enhanced-with-leaked-credential-detections">Enhanced with leaked credential detections</h3>
@markup("md", "content/.markup/bodies/1463.md")
</aside>
<hr />
<h3 id="detections">Detections</h3>
<p>Fraud detections focus on account abuse attacks such as account takeover, bulk account creation, and credential quality. These detections run on all eligible traffic and can be used across <a href="/rules/">Cloudflare Rules</a> to log, challenge, and/or block requests to your sign up and login endpoints.</p>
<h4 id="account-creation">Account creation</h4>
<p>Disposable Email Checks detect when users sign up with throwaway email addresses commonly used for promotion abuse and fake account creation. These disposable email services allow attackers to create thousands of unique accounts without maintaining real infrastructure.</p>
<p>You can use the following binary field as you build rules to enforce security preferences, choosing to block all disposable emails outright, or issue a <a href="/cloudflare-challenges/challenge-types/">challenge</a> to anyone attempting to create an account with a disposable email.</p>
<h4 id="suspicious-emails">Suspicious emails</h4>
<p>Cloudflare analyzes the components of an email used during sign up to help identify suspicious patterns. Refer to <a href="#prerequisites">prerequisites</a> to ensure your traffic is eligible for detections.</p>
<p>Cloudflare does not store email addresses during this analysis. All detections processed without any storage or caching.</p>
<table>
<thead>
<tr>
<th>Detection tag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.fraud_detection.disposable_email</code></td>
<td>Identifies emails with domains that are commonly found in lists of temporary or disposable email services.</td>
</tr>
<tr>
<td><code>cf.fraud.email_risk</code></td>
<td>Analyzes the randomness (entropy) of characters in an email username and top level domain. For example, <code>a8xk2m9p@example.com</code> has high entropy (very random characters), while <code>john.smith@example.com</code> has low entropy (recognizable pattern). <br />High risk emails indicate high entropy, while medium and low risk emails indicate less randomness in the string of characters.</td>
</tr>
</tbody>
</table>
<hr />
<h3 id="mitigations">Mitigations</h3>
<p>The following Fraud detection fields can be used in Security Rules to help identify and mitigate suspicious traffic.</p>
<h4 id="security-rules">Security Rules</h4>
<p>The following fields can be used in new and existing Security Rules.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.fraud_detection.disposable_domain</code></td>
<td>Flags whether a domain for a given email is included in a known list of temporary email providers.</td>
<td><code>True</code> or <code>False</code></td>
</tr>
<tr>
<td><code>cf.fraud.email_risk</code></td>
<td>Measures risk of email based on randomness of characters in the username and domain.</td>
<td><code>Low</code> represents low risk due to reduced randomness and simple emails. <br /><code>Medium</code> represents medium risk based on larger strings with slightly more randomness. <br /><code>High</code> represents high risk based on larger and random character strings. <br /><code>Unknown</code></td>
</tr>
</tbody>
</table>
<h4 id="other-rules">Other rules</h4>
<p>You can use Fraud detection data in Request Header <a href="/rules/transform/managed-transforms/">Transform Rules</a> to pass information down to the origin.</p>
<h4 id="logpush">LogPush</h4>
<p>You can add Fraud detection fields to existing or new <a href="/logs/logpush/">LogPush</a> jobs.</p>
<hr />
<h2 id="analytics">Analytics</h2>
<p>You can find Fraud data and detections in Security Analytics, where you can see top User IDs.</p>
<div class="nb-dash-button"></div>
<p>Fraud fields can be used as filters to identify suspicious patterns in your traffic.</p>
<p>The hashed User ID field within Security Analytics also provides Fraud customers with data that can help review detections and patterns per individual users rather than requests. You can review user level aggregations for IPs and IP counts, event types (login or sign up), locations, devices, and browsers.</p>
<p>A user level profile also provides a quick way to review the latest events associated with a user so that you can identify any anomalies and create a custom rule to log, block, or challenge that user.</p>
