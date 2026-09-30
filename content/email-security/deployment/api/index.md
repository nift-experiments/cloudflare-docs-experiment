<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8509.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8508.md")
</aside>
<p>When you choose an <strong>API deployment</strong> for your <a href="/email-security/deployment/">Email Security (formerly Area 1) setup</a>, email messages only reach Email Security after they have already reached a user's inbox.</p>
<p>Then, through on integrations with your email provider, Email Security can <a href="/email-security/email-configuration/retract-settings/">retract messages</a> based on your organization's policies.</p>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/api-deployment-diagram.png" alt="With API deployment, messages travel through Email Security's email filter after reaching your users." /></p>
<h2 id="benefits">Benefits</h2>
<p>When you choose API deployment, you get the following benefits:</p>
<ul>
<li>Easy protection for complex email architectures, without requiring any change to mailflow operations.</li>
<li>Agentless deployment for Microsoft 365 and Gmail.</li>
<li>The initial email protection measures offered by your current email provider.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>However, API deployment also has the following disadvantages:</p>
<ul>
<li>Email Security is dependent on your email provider's API infrastructure and outages will increase the message dwell time in the inbox.</li>
<li>Email Security requires read and write access to mailboxes.</li>
<li>Requires API support from your email provider (does not typically support on-premise providers).</li>
<li>Your email provider may throttle API requests from Email Security.</li>
<li>Detection rates may be lower if multiple solutions exist.</li>
<li>Messages cannot be modified or quarantined.</li>
<li>Certain URL rewrite schemes cannot be decoded (for example, Mimecast).</li>
</ul>
<h2 id="get-started">Get started</h2>
<p>For help getting started, refer to our <a href="/email-security/deployment/api/setup/">setup guides</a>.</p>
