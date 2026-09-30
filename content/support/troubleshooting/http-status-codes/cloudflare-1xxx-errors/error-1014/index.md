<h2 id="error-1014-cname-cross-user-banned">Error 1014: CNAME Cross-User Banned</h2>
<p>This error indicates that a CNAME record between domains in different Cloudflare accounts is prohibited.</p>
<h3 id="common-cause">Common cause</h3>
<p>By default, Cloudflare prohibits a DNS CNAME record between domains in different Cloudflare accounts. CNAME records are permitted within a domain (<code>www.example.com</code> CNAME to <code>api.example.com</code>) and across zones within the same user account (<code>www.example.com</code> CNAME to <code>www.example.net</code>) or using our <a href="https://www.cloudflare.com/saas/">Cloudflare for SaaS</a> solution.</p>
<p>Another common cause is connecting a custom domain to an R2 bucket, where the domain is an active zone with the <a href="/fundamentals/account/account-security/zone-holds/">zone hold</a> feature enabled or if the zone is banned.</p>
<h3 id="resolution">Resolution</h3>
<ul>
<li>
<p>To allow CNAME record resolution to a domain in a different Cloudflare account, the domain owner of the CNAME target must use <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>.</p>
</li>
<li>
<p>To allow connecting to a R2 bucket with a custom domain, disable the <a href="/fundamentals/account/account-security/zone-holds/">zone hold</a> feature on the custom domain target zone to resolve the 1014 error.</p>
</li>
<li>
<p>To allow connections to an R2 bucket whose zone is banned:</p>
<ul>
<li>First, check whether there is any <a href="/fundamentals/reference/report-abuse/complaint-types/">phishing report</a> for the hostname (and request a review if there is one).</li>
<li>Second, make sure that you have no unpaid invoice(s), as you will not be able to enable any new services until <a href="/billing/manage/pay-invoices-overdue-balances/">any outstanding balance</a> is addressed. If this does not resolve the issue, contact your account team.</li>
</ul>
</li>
</ul>
