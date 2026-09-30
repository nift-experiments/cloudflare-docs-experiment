<p>When you choose an API deployment, email messages only reach Email security after they have already reached a user's inbox.</p>
<p>Then, through an integration with your email provider, Email security can <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move messages</a> based on your organization's policies.</p>
<p><img src="/assets/upstream/email-security/M365_API_Deployment_Graph.png" alt="With API deployment, messages travel through Email security's email filter after reaching your users." /></p>
<h2 id="benefits">Benefits</h2>
<p>When you choose API deployment, you get the following benefits:</p>
<ul>
<li>Easy protection for complex email architectures, without requiring any change to mailflow operations.</li>
<li>Agentless deployment for Microsoft 365.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>However, API deployment also has the following disadvantages:</p>
<ul>
<li>Email security is dependent on Microsoft's Graph API, and outages will increase the message dwell time in the inbox.</li>
<li>Your email provider may throttle API requests from Email security.</li>
<li>Email security requires read and write access to mailboxes.</li>
<li>Requires API support from your email provider (does not typically support on-premise providers).</li>
<li>Detection rates may be lower if multiple solutions exist.</li>
<li>Messages cannot be modified or quarantined.</li>
</ul>
