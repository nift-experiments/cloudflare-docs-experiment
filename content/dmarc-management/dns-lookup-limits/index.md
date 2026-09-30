<p>An <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/">SPF record</a> lists which servers are authorized to send email for your domain. SPF records can reference other domains and services (for example, using <code>include:</code> or <code>mx</code> mechanisms), and each such reference requires a separate DNS lookup to verify. The <a href="https://www.rfc-editor.org/rfc/rfc7208.html">SPF specification (RFC 7208)</a> limits the total number of these lookups to 10 per SPF check. If your SPF record exceeds this limit, receiving mail servers may treat the SPF check as a permanent error and reject or flag your emails.</p>
<p>To check if your SPF records are compliant with the SPF specification:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email</strong> &gt; <strong>DMARC Management</strong>.</li>
<li>In <strong>Email record overview</strong>, select <strong>View records</strong>.</li>
<li>Find your SPF record, and select the three dots next to it &gt; <strong>Edit</strong>.</li>
<li>DMARC Management will inspect your records and check for the total number of DNS lookups. If the record exceeds the limit, DMARC Management will display a warning. To fix this, remove unnecessary entries in your SPF record. Refer to <a href="/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records">Manage DNS records</a> for more information.</li>
</ol>
