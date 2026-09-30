<p>This guide describes how to configure detection settings to mitigate impersonation risks while ensuring legitimate delivery.</p>
<p>Once you configure the <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a> to mitigate spoof detections, you can add emails in the impersonation registry as secondary email. Refer to <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/#edit-users">Edit users</a> to learn how to add a secondary email address.</p>
<p>For impersonation events that are caused by systems, Cloudflare recommends that you configure an <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policy</a> to mitigate delivery disruptions.</p>
<p>To maintain a higher security posture, allow policies should be defined with the narrowest possible scope. Start with specific expressions or email addresses that will target the actual sender or system. If the system is sending from a variety of addresses, you can create an expression that is wider while keeping the expression specific.  In some situations, it is better to have multiple specific entries than a more generic policy that allows a whole domain.</p>
<h2 id="policy-selection-criteria">Policy selection criteria</h2>
<p>When you configure an <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policy</a>, you can choose how Email security handles messages that match your criteria.</p>
<p>Allow policies are suitable for services that may spoof people's names.</p>
<p>Use <strong>Accept sender</strong> with <strong>Sender verification (recommended)</strong> turned on for systematic traffic. For example, a file shared through Google Drive will create a notification using the name of the user that is sharing the document. However, the underlying email address used will be a Google system address.</p>
<p>Use <strong>Trusted Sender</strong> for emails that do not require phishing inspections. This will exempt messages from any phishing analysis, including links analysis.</p>
<p>Example use cases:</p>
<ul>
<li>Temporary rules (to avoid over-detection)</li>
<li>Phishing simulations</li>
<li>Applications that send one time links for verification</li>
</ul>
<h2 id="best-practices-for-configuration">Best practices for configuration</h2>
<ul>
<li>Prioritize static IPs: Use known and owned, static IP addresses for relay servers. Avoid <a href="https://docs.cloud.google.com/vpc/docs/ip-addresses#ephemeral_and_static_ip_addresses">ephemeral IP addresses</a> as their transient nature can lead to policy degradation.</li>
<li>Enforce Sender Verification: Always have <strong>Sender Verification (Recommended)</strong> enabled in the Cloudflare dashboard. It validates the originating system's email authentication records (namely <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/">SPF</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/">DKIM</a>, and <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>) against the domain to ensure authenticity.</li>
<li>Handle unsanctioned traffic: Unsanctioned traffic is traffic which has not been approved within an organization. This is also known as <a href="https://www.cloudflare.com/en-gb/learning/access-management/what-is-shadow-it/">Shadow IT</a>. If an unsanctioned system generates spam or spoofed content, <a href="/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/">configure a text add-on</a> to append a tag to the subject line and automatically <a href="/cloudflare-one/email-security/settings/auto-moves/">move</a> the message to the junk folder.</li>
</ul>
