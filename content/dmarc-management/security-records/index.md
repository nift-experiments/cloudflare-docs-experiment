<p>Without email authentication records, anyone can send email that appears to come from your domain — a technique known as domain spoofing. To prevent this, you add DNS TXT records (text-based entries in your domain's DNS settings) that allow receiving mail servers to verify whether an email actually came from you:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/">Sender Policy Framework (SPF)</a>: Lists the IP addresses and domains authorized to send email on behalf of your domain.</li>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DomainKeys Identified Mail (DKIM)</a>: Authenticates the sender's domain and verifies that email content was not altered in transit, using a cryptographic signature.</li>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">Domain-based Message Authentication Reporting and Conformance (DMARC)</a>: Tells receiving servers what to do when SPF or DKIM checks fail (for example, reject or quarantine the email), and sends you aggregate reports about your email traffic.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1136.md")
</aside>
<h2 id="create-security-records">Create security records</h2>
<p>To set up email security records:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email</strong> &gt; <strong>DMARC Management</strong>.</li>
<li>In <strong>Email record overview</strong>, select <strong>View records</strong>.</li>
<li>Use the available options to set up <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/">SPF</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/">DKIM</a>, and <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/">DMARC records</a>. This page will also list any previous records you might already have in your account.</li>
</ol>
<h2 id="edit-or-delete-records">Edit or delete records</h2>
<p>Refer to <a href="/dns/manage-dns-records/how-to/create-dns-records/">Manage DNS records</a> for more information.</p>
