<p>Email security works through a system of domain-based routing, where Cloudflare receives and evaluates incoming email from a domain.</p>
<h2 id="create-a-domain">Create a domain</h2>
<p>To create a new domain in Email security:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</p>
</li>
<li>
<p>Select <strong>New Domain</strong>.</p>
</li>
<li>
<p>Enter the following information:</p>
<ul>
<li><strong>Domain</strong>: The domain name receiving email traffic.</li>
<li><strong>Configured As</strong>: Choose <strong>MX Records</strong> or specify a number of <strong>Hops</strong> (depending on your email architecture).</li>
<li><strong>Forwarding To</strong>: Enter the hostname of your email provider.</li>
<li><strong>IP Restrictions</strong> (optional): Restrict incoming traffic to the IP addresses of your mail servers.</li>
<li><strong>Inbound TLS</strong> (only available for non-MX domains): Applies TLS to incoming traffic.</li>
<li><strong>Outbound TLS</strong>: Choose between <strong>Forward all messages over TLS</strong> (recommended) or <strong>Forward all messages using opportunistic TLS</strong>.</li>
<li><strong>Quarantine Policy</strong>: Choose the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
</li>
</ol>
@markup("md", "content/.markup/bodies/8566.md")
</div> you want to send to [Admin quarantine](/email-security/email-configuration/admin-quarantine/).
<ol start="6">
<li>Select <strong>Publish Domain</strong>.</li>
</ol>
<hr />
<h2 id="edit-a-domain">Edit a domain</h2>
<p>To edit an existing domain:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</li>
<li>On a specific domain, select <strong>...</strong> &gt; <strong>Edit</strong>.</li>
<li>Make changes as needed.</li>
<li>Select <strong>Update Domain</strong>.</li>
</ol>
<hr />
<h2 id="delete-a-domain">Delete a domain</h2>
<p>To delete a domain:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</li>
<li>On a specific domain, select <strong>...</strong> &gt; <strong>Delete</strong>.</li>
</ol>
