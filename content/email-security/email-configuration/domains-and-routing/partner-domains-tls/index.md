<p>To add additional TLS requirements for emails coming from certain domains, you can enforce higher levels of SSL/TLS inspection. If TLS is required, mail without TLS from the specified domain will be dropped.</p>
<h2 id="add-a-domain">Add a domain</h2>
<p>To require that email from a specific domain passes SSL/TLS inspection:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>On <strong>Email Configuration</strong>, go to <strong>Domains &amp; Routing</strong> &gt; <strong>Partner Domains TLS</strong>.</li>
<li>Select <strong>New Partner Domain</strong>.</li>
<li>Enter a <strong>Domain</strong> and any <strong>Notes</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="exempt-tls-inspection">Exempt TLS inspection</h2>
<p>If you decide to exempt a domain from TLS inspection - by toggling <strong>Require TLS Inbound</strong> to <strong>Off</strong> - this will not turn off enforcement against legacy standards like SSLv1, SSLv2, and TLSv1, which is generally considered insecure.</p>
