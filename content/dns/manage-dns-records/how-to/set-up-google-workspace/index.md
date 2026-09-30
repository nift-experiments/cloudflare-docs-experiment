<p>To use your domain with <a href="https://workspace.google.com/">Google Workspace</a>, you must add specific DNS records in Cloudflare. This page explains how to add records for:</p>
<ul>
<li><a href="#verify-domain-ownership">Domain ownership verification</a></li>
<li><a href="#add-mx-records">Gmail delivery (MX records)</a></li>
<li><a href="#add-email-authentication-records">Email authentication (SPF, DKIM, and DMARC)</a></li>
</ul>
<p>It also includes a <a href="#apply-records-to-multiple-domains">tip for applying records across multiple domains</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7818.md")
</aside>
<hr />
<h2 id="verify-domain-ownership">Verify domain ownership</h2>
<p>Google must confirm you control your domain before activating Google Workspace services for it.</p>
<ol>
<li>In <a href="https://admin.google.com">Google Admin console</a>, start the domain setup wizard and copy the TXT verification value Google provides. It looks similar to:</li>
</ol>
<pre><code class="language-txt">google-site-verification=abc123XYZ&#10;</code></pre>
<ol start="2">
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select your account and domain, then go to <strong>DNS</strong> &gt; <strong>Records</strong>.</li>
<li>Select <strong>Add record</strong> and enter:
<ul>
<li><strong>Type</strong>: <code>TXT</code></li>
<li><strong>Name</strong>: <code>@</code> (the root of your domain)</li>
<li><strong>Content</strong>: the verification value copied from Google</li>
<li><strong>Proxy status</strong>: DNS only</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
<li>Return to the Google Admin console and select <strong>Verify</strong>.</li>
</ol>
<p>Google typically verifies within a few minutes, though DNS propagation can take up to 48 hours.</p>
<details class="nb-details"><summary>Google says the domain is already in use</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7819.md")
</div></details>
<details class="nb-details"><summary>TXT record is not visible in external DNS tools</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7820.md")
</div></details>
<hr />
<h2 id="add-mx-records">Add MX records</h2>
<p>MX records direct incoming email for your domain to Google's mail servers. Google Workspace requires five MX records.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>DNS</strong> &gt; <strong>Records</strong>.</li>
<li>If your domain already has MX records pointing to a different mail provider, delete them.</li>
<li>Add each of the records in this table:</li>
</ol>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Mail server</th>
<th>Priority</th>
</tr>
</thead>
<tbody>
<tr>
<td>MX</td>
<td><code>@</code></td>
<td><code>aspmx.l.google.com</code></td>
<td><code>1</code></td>
</tr>
<tr>
<td>MX</td>
<td><code>@</code></td>
<td><code>alt1.aspmx.l.google.com</code></td>
<td><code>5</code></td>
</tr>
<tr>
<td>MX</td>
<td><code>@</code></td>
<td><code>alt2.aspmx.l.google.com</code></td>
<td><code>5</code></td>
</tr>
<tr>
<td>MX</td>
<td><code>@</code></td>
<td><code>alt3.aspmx.l.google.com</code></td>
<td><code>10</code></td>
</tr>
<tr>
<td>MX</td>
<td><code>@</code></td>
<td><code>alt4.aspmx.l.google.com</code></td>
<td><code>10</code></td>
</tr>
</tbody>
</table>
<p>Set <strong>Proxy status</strong> to <strong>DNS only</strong> for each record.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="cloudflare-email-routing-conflict">Cloudflare Email Routing conflict</h3>
@markup("md", "content/.markup/bodies/7817.md")
</aside>
<hr />
<h2 id="add-email-authentication-records">Add email authentication records</h2>
<p>SPF, DKIM, and DMARC records help receiving mail servers verify that messages from your domain are legitimate and protect against spoofing.</p>
<h3 id="spf">SPF</h3>
<p>SPF specifies which mail servers are authorized to send email for your domain.</p>
<ol>
<li>In <strong>DNS</strong> &gt; <strong>Records</strong>, select <strong>Add record</strong> and enter:
<ul>
<li><strong>Type</strong>: <code>TXT</code></li>
<li><strong>Name</strong>: <code>@</code></li>
<li><strong>Content</strong>: <code>v=spf1 include:_spf.google.com ~all</code></li>
<li><strong>Proxy status</strong>: DNS only</li>
</ul>
</li>
<li>If you also send email from other services alongside Google Workspace, add their <code>include:</code> entries to the same record. Do not create a second TXT record starting with <code>v=spf1</code>.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7816.md")
</aside>
<h3 id="dkim">DKIM</h3>
<p>DKIM adds a cryptographic signature to outbound messages so recipients can confirm the messages were not altered in transit.</p>
<ol>
<li>In <a href="https://admin.google.com">Google Admin console</a>, go to <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong> &gt; <strong>Authenticate email</strong>.</li>
<li>Select your domain and choose <strong>Generate new record</strong>. Select a <strong>2048-bit</strong> key length for stronger security.</li>
<li>Copy the TXT record value Google displays. It starts with <code>v=DKIM1; k=rsa; p=...</code>.</li>
<li>In Cloudflare <strong>DNS</strong> &gt; <strong>Records</strong>, add a record:
<ul>
<li><strong>Type</strong>: <code>TXT</code></li>
<li><strong>Name</strong>: the selector Google specifies, typically <code>google._domainkey</code></li>
<li><strong>Content</strong>: the value copied from Google</li>
<li><strong>Proxy status</strong>: DNS only</li>
</ul>
</li>
<li>Return to Google Admin and select <strong>Start authentication</strong>.</li>
</ol>
<p>Allow a few minutes for propagation before Google confirms DKIM is active.</p>
<h3 id="dmarc">DMARC</h3>
<p>DMARC tells receiving servers how to handle messages that fail SPF or DKIM checks and where to send aggregate reports.</p>
<ol>
<li>In <strong>DNS</strong> &gt; <strong>Records</strong>, add a record:
<ul>
<li><strong>Type</strong>: <code>TXT</code></li>
<li><strong>Name</strong>: <code>_dmarc</code></li>
<li><strong>Content</strong>: <code>v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com</code></li>
<li><strong>Proxy status</strong>: DNS only</li>
</ul>
</li>
</ol>
<p>Replace <code>dmarc@yourdomain.com</code> with an address where you want to receive DMARC reports.</p>
<p>Start with <code>p=none</code> (monitoring mode) while you confirm your SPF and DKIM setup is working correctly. Once you have reviewed reports and confirmed that legitimate email is passing authentication, update the policy to <code>p=quarantine</code> or <code>p=reject</code>.</p>
<hr />
<h2 id="apply-records-to-multiple-domains">Apply records to multiple domains</h2>
<p>If you manage many domains with the same Google Workspace account, you can use <a href="/dns/manage-dns-records/how-to/import-and-export/">import and export</a> to apply common records efficiently rather than adding them one by one.</p>
<ol>
<li>Complete the full DNS setup manually on your first domain.</li>
<li>In <strong>DNS</strong> &gt; <strong>Records</strong>, select <strong>Export</strong> to download the zone as a BIND-format file.</li>
<li>Open the exported file and remove records you do not want to replicate — for example, your website A/AAAA records. Keep only the MX, SPF, and DMARC entries.</li>
<li>For each additional domain, go to <strong>DNS</strong> &gt; <strong>Records</strong> &gt; <strong>Import</strong> and upload the edited file.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7815.md")
</aside>
