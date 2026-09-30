<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8521.md")
</aside>
<p>To set up Email security (formerly Area 1) for Gmail:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</li>
<li>Select the question mark, where you will be able to find your BCC address.</li>
<li>Once you found your address, select <strong>Settings</strong> (the gear icon), then select <strong>New Domain</strong>.</li>
<li>Fill in the information needed to add your domain:</li>
</ol>
<ul>
<li><strong>Domain</strong>: Enter the domain you want to set up BCC from Google.</li>
<li><strong>Configured As</strong>: Select Hops, enter <code>2</code>.</li>
<li><strong>Forwarding To</strong>: Enter <code>google.com</code>.</li>
<li><strong>Outbound TLS</strong>: Select <strong>Forward all messages over TLS</strong>.</li>
<li><strong>Quarantine policy</strong>: Ensure no policy is selected.</li>
</ul>
<ol start="5">
<li>Select <strong>Publish Domain</strong>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have found your BCC address and added your domain, continue with <a href="/email-security/deployment/api/setup/gsuite-bcc-setup/bcc-rules-to-area1/">Add BCC rules</a> to add BCC rules to Email security.</p>
