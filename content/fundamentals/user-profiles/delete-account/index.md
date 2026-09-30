<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8740.md")
</aside>
<h2 id="who-can-delete-their-account">Who can delete their account</h2>
<p>If your account uses <a href="/fundamentals/manage-members/dashboard-sso/">Single-Sign On (SSO)</a>, your super administrator may need to delete your account on your behalf.</p>
<p>If your account does not use SSO, you can delete your account on your own.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before Cloudflare can cancel your account and delete your personal information, you will need to follow the process below for each domain associated with your Cloudflare account:</p>
<ul>
<li><a href="/billing/manage/cancel-subscription/">Cancel your subscriptions or add-on services</a></li>
<li><a href="/fundamentals/manage-domains/remove-domain/">Remove your domain from Cloudflare</a></li>
<li><a href="/dns/zone-setups/full-setup/setup/">Remove Cloudflare nameservers at your domain registrar</a></li>
<li><a href="/registrar/account-options/renew-domains#set-up-automatic-renewals">Disable auto-renew for your Registrar domain(s)</a></li>
<li>If you are using a Cloudflare <a href="/dns/zone-setups/partial-setup/">CNAME setup</a>, <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">update your DNS records</a> at your DNS provider to point to your website IPs or hostnames instead of Cloudflare.</li>
<li><a href="/billing/get-started/update-billing-info/#delete-a-payment-method">Delete payment information</a></li>
<li>(<em>Optional</em>) <a href="/billing/manage/invoices/#download-invoice">Download a copy of your invoices</a>. Once deleted, the invoices will no longer be accessible and cannot be re-sent to you.</li>
</ul>
<h2 id="delete-your-cloudflare-account">Delete your Cloudflare account</h2>
<p>When you sign up for Cloudflare, we create a user profile for you and an account named <code>youremail@example.com's account</code>, and your user profile is the admin for the newly create account. Your user profile is where you manage preferences like your password or language, while your account is where you'll manage Cloudflare product configurations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8739.md")
</aside>
<p>When you delete your profile, the account associated with your profile and any accounts where you are the last active member will also be deleted. Deleting your account is permanent. Any accounts where you are the primary owner will also be deleted and any other users on those accounts will be removed.</p>
<p>After you delete your profile, you can use the email address with your profile to create a new account. In most cases, your email should be freed up to be used in a new signup right away.
However, this may not be the same for users who have a lock on their account (for legal purposes).</p>
<p>All domains, subscriptions, and billing information on your account will be removed from Cloudflare.</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>My Profile</strong>.</li>
<li>Select <strong>Delete this user</strong>.</li>
<li>Select <strong>Delete user</strong>.</li>
<li>Follow the prompts to finish deleting your account.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8738.md")
</aside>
