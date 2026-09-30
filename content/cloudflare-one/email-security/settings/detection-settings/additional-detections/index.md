<p>Email security allows you to configure the following additional detections:</p>
<ul>
<li>Domain age</li>
<li>Blank email detection</li>
<li><a href="https://en.wikipedia.org/wiki/Automated_clearing_house">Automated Clearing House (ACH)</a> change from free email detection</li>
<li>HTML attachment email detection</li>
</ul>
<p>To configure additional detections:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>On the <strong>Settings</strong> page, go to <strong>Detection settings</strong> &gt; <strong>Additional detections</strong>, and select <strong>Edit</strong>.</li>
</ol>
<h2 id="configure-domain-age">Configure domain age</h2>
<p>The domain age is the time since the domain has been registered.</p>
<p>Because of the domain age detection, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a> can be used to create an exception to the age detection.</p>
<p>To configure a domain age:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page:
<ul>
<li>Select <strong>Malicious domain age</strong>: Controls the threshold for a malicious disposition. Maximum of 100 days. It is recommended to set the <strong>Malicious domain age</strong> to 7 days.</li>
<li>Select <strong>Suspicious domain age</strong>: Controls the threshold for a suspicious disposition. Maximum of 100 days. It is recommended to set the <strong>Suspicious domain age</strong> between 30 and 45 days.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-blank-email-detection">Configure blank email detection</h2>
<p>Blank email detection detects emails with blank bodies and assigns a default disposition. You can choose between <strong>Malicious</strong> and <strong>Suspicious</strong> as dispositions.</p>
<p>To enable blank email detection:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page, enable <strong>Blank email detection</strong>.</li>
<li>Choose between <strong>Malicious</strong> and <strong>Suspicious</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-ach-change-from-free-email-detection">Configure ACH change from free email detection</h2>
<p><a href="https://en.wikipedia.org/wiki/Automated_clearing_house">Automated Clearing House (ACH)</a> is a banking term related to direct deposits. ACH change from free email detection detects payroll inquiries or change requests from free email domains and assigns a default disposition. You can choose between <strong>Malicious</strong> and <strong>Suspicious</strong> as dispositions.</p>
<p>To enable ACH change from free email detection:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page, enable <strong>ACH change from free email detection</strong>.</li>
<li>Choose between <strong>Malicious</strong> and <strong>Suspicious</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-html-attachment-email-detection">Configure HTML attachment email detection</h2>
<p>HTML attachment email detection detects HTM and HTML attachments in emails and assigns a default disposition.</p>
<p>To enable HTML attachment email detection:</p>
<ol>
<li>On the <strong>Edit additional detections</strong> page, enable <strong>HTML attachment email detection</strong>.</li>
<li>Choose between <strong>Malicious</strong> and <strong>Suspicious</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
