<p>Consider the following sections on how you can remove domains from Cloudflare. Removing your domain cancels all active subscriptions on that domain, which will not be refunded per our <a href="/billing/understand/billing-policy/">billing policy</a>. If you add this domain back to Cloudflare later, you will need to re-purchase all subscriptions. Removing your domain from Cloudflare does not change your domain registration.</p>
<h2 id="before-removing-your-domain">Before removing your domain</h2>
<p>If you experience website issues, we recommend <a href="/fundamentals/manage-domains/pause-cloudflare/">temporarily pausing Cloudflare</a> to evaluate your website's performance.</p>
<p>If you have an Enterprise plan, you need to <a href="/billing/manage/change-plan/#change-plan-type">change the zone plan</a> to <strong>Free</strong>.</p>
<p>If you need to re-add the domain in a different account, make sure the current settings have been saved. For example, you may <a href="/dns/manage-dns-records/how-to/import-and-export/">Import and export DNS records</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8900.md")
</aside>
<h3 id="actions-outside-of-cloudflare">Actions outside of Cloudflare</h3>
<ul>
<li>
<p>When you remove a domain from Cloudflare, it also prevents your domain from using Cloudflare for DNS resolution. To avoid DNS errors, update your nameservers at your domain registrar to use nameservers not owned by Cloudflare.</p>
<ul>
<li>Refer to <a href="/dns/zone-setups/full-setup/setup/#35-verify-changes">Check if your nameservers are pointing to Cloudflare</a> to confirm that your nameservers no longer point to Cloudflare.</li>
</ul>
</li>
<li>
<p>At your registrar, make sure you do not have a <strong>DS</strong> DNS record. This record enables <a href="/dns/dnssec/">DNSSEC</a> and could prevent your DNS records from being changed.</p>
</li>
</ul>
<h3 id="actions-within-cloudflare">Actions within Cloudflare</h3>
<ul>
<li>
<p><a href="/billing/manage/cancel-subscription/">Cancel active add-on subscriptions</a>.</p>
</li>
<li>
<p><a href="/logs/logpush/examples/example-logpush-curl/#optional---delete-a-job">Delete all the Logpush jobs for that domain</a></p>
</li>
<li>
<p>If you use Cloudflare Registrar:</p>
<ul>
<li>
<p><a href="/registrar/account-options/renew-domains/">Disable domain auto-renewal</a> or <a href="/registrar/account-options/transfer-out-from-cloudflare/">transfer your domain out of Cloudflare</a>.</p>
</li>
<li>
<p>If the domain has already expired, it will be automatically removed from your account. Refer to <a href="/registrar/faq/#what-happens-when-a-domain-expires">What happens when a domain expires?</a></p>
</li>
<li>
<p>If the domain has not yet expired you can likely request deletion. Refer to <a href="/registrar/account-options/domain-management/#delete-a-domain-registration">Delete a domain registration</a></p>
</li>
<li>
<p>If enabled, disable DNSSEC. In your domain dashboard, go to <strong>DNS</strong> &gt; <strong>Settings</strong>. Within <strong>DNSSEC</strong>, select <strong>Disable DNSSEC</strong>. Select <strong>Confirm</strong>.</p>
</li>
</ul>
</li>
</ul>
<h2 id="remove-a-domain-activated-in-cloudflare">Remove a domain activated in Cloudflare</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your domain.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>On the domain <strong>Overview</strong> page, find <strong>Advanced Actions</strong> and then select <strong>Remove from Cloudflare</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8899.md")
</aside>
<ol start="3">
<li>Select <strong>Confirm</strong>.</li>
</ol>
