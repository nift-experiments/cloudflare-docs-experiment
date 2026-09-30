<p>Below you will find answers to our most commonly asked questions. If you cannot find the answer you are looking for, refer to the <a href="https://community.cloudflare.com/">community page</a> to explore more resources.</p>
<ul>
<li><a href="#domain-management">Domain management</a></li>
<li><a href="#domain-transfers">Domain transfers</a></li>
<li><a href="#domain-registrations">Domain registrations</a></li>
<li><a href="#billing">Billing</a></li>
<li><a href="#domain-restoration">Domain restoration</a></li>
<li><a href="#domain-deletions">Domain deletions</a></li>
</ul>
<hr />
<h2 id="domain-management">Domain management</h2>
<h3 id="can-i-use-my-own-third-party-nameservers">Can I use my own (third-party) nameservers</h3>
<p>No, all domains on Cloudflare Registrar use Cloudflare nameservers, so that we can protect and speed up your content or services.</p>
<p>If you only need a subdomain to be on a different service provider, you can <a href="/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/">delegate a subdomain</a>. Also, if you are on the Business or Enterprise plans, you have the option to set up <a href="/dns/nameservers/custom-nameservers/">custom nameservers</a>, which means you will be using Cloudflare nameservers but with custom-branded nameserver names.</p>
<p>If you still need to use different nameservers, you will have to <a href="/registrar/account-options/transfer-out-from-cloudflare/">move your domain to another Registrar</a>.</p>
<h3 id="why-did-my-domain-stop-resolving-or-show-a-parked-or-suspension-page-and-i-never-got-the-verification-email">Why did my domain stop resolving or show a parked or suspension page, and I never got the verification email</h3>
<p>If you registered your domain through Cloudflare Registrar, ICANN requires you to verify the registrant email address. If that email is unverified or the verification link expired, ICANN requires the registrar to place a hold on the domain and Cloudflare temporarily replaces your nameservers with parking nameservers, which is why the site stops resolving. Once you complete verification, your nameservers are automatically restored.</p>
<p>To fix it, verify your registrant email:</p>
<ol>
<li>Resend the verification email from your <a href="/fundamentals/user-profiles/verify-email-address/">email verification settings</a>.</li>
<li>Check your spam and promotions folders.</li>
<li>Confirm the registrant email on the domain is an address you can actually receive mail at (<strong>Manage Domains</strong> &gt; your domain &gt; <strong>Contacts</strong>). Refer to <a href="/registrar/account-options/domain-contact-updates/">Registrant contact updates</a>.</li>
</ol>
<p>Keep your contact details accurate. ICANN rules allow a domain to be suspended or cancelled if the registrant information is invalid.</p>
<h3 id="how-can-i-update-my-contact-information-and-why-am-i-asked-to-approve-the-change">How can I update my contact information, and why am I asked to approve the change</h3>
<p>You can update both your default contact information and any individual Registrant, Administrator, Technical, or Billing contact for your domain registrations by following <a href="/registrar/account-options/domain-contact-updates/">Registrant contact updates</a>. Details that may be updated include name, email, address, organization, and telephone number.</p>
<p>Most fields update immediately. However, if you change the first name, last name, organization, or email, ICANN treats it as a Change of Registrant: Cloudflare emails an approval link to the registrant and the change only applies once approved. If nobody approves or rejects within seven days, the request auto-cancels. When you change the email, both the old and new addresses must approve.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/460.md")
</aside>
<p>Keeping your contact information accurate matters: ICANN allows a domain to be suspended or cancelled if the registrant information is invalid.</p>
<hr />
<h2 id="domain-transfers">Domain transfers</h2>
<h3 id="how-can-i-see-the-status-of-my-domain-transfer">How can I see the status of my domain transfer</h3>
<p>Once you initiate a domain transfer, your previous registrar has five days to release the domain. In most cases, they will send you an email to confirm you want to transfer. If you actively acknowledge that email (through a link or the registrar's dashboard), they can process it immediately.</p>
<p>To see the progress of your transfer, go to the <strong>Transfer domains</strong> page in the Cloudflare dashboard to see a list of domain transfers that are in progress.</p>
<div class="nb-dash-button"></div>
<p>To accelerate the process, be sure to check with your old registrar how you can approve the transfer out.</p>
<p>Once successful, you will receive an email from Cloudflare and be able to manage the domain in the dashboard under <strong>Overview</strong> of that site.</p>
<h3 id="my-transfer-has-been-pending-for-several-days-is-that-normal">My transfer has been pending for several days. Is that normal</h3>
<p>Some waiting is normal. Your previous registrar has up to five days to release the domain, so the single fastest thing you can do is log in to your old registrar and approve or accelerate the transfer out.</p>
<p>You cannot enter your auth code until the domain is first active on Cloudflare with a <a href="/dns/zone-setups/full-setup/">full setup</a>. If the transfer failed rather than just pending, work through <a href="/registrar/troubleshooting/">Registrar: troubleshoot stalled domain transfers</a>.</p>
<h3 id="why-did-my-transfer-fail">Why did my transfer fail</h3>
<p>Domain transfers sometimes fail. Refer to <a href="/registrar/troubleshooting/">Registrar: troubleshoot stalled domain transfers</a> for more information on what might have happened and how to solve the issue.</p>
<p>If you cannot solve the issue, open a support ticket or contact your account team.</p>
<h3 id="why-am-i-not-allowed-to-transfer-my-domain">Why am I not allowed to transfer my domain</h3>
<p>ICANN prohibits domain transfers within 60 days of a change to the WHOIS data or registrar of a domain. If you modified your contact information, transferred registrars, or registered your domain in the last 60 days, Cloudflare will be unable to process your transfer immediately.</p>
<p>You can leave the domain <strong>In Progress</strong> and Cloudflare will wait until after the 60-day window passes to attempt to process the transfer. For the full list of transfer prerequisites, refer to <a href="/registrar/get-started/transfer-domain-to-cloudflare/">Transfer your domain to Cloudflare</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/459.md")
</aside>
<h3 id="why-am-i-not-able-to-start-a-transfer">Why am I not able to start a transfer</h3>
<p>If you have an <a href="/fundamentals/user-profiles/verify-email-address/">unverified email address</a>, you might experience issues when initiating a domain transfer.</p>
<h3 id="what-happens-if-i-enter-the-wrong-auth-code">What happens if I enter the wrong auth code</h3>
<p>If you enter an incorrect auth code (also referred to as authentication code or authorization code), return to the <strong>Domain Registration</strong> page or the <strong>Overview</strong> for your site. You can use the available input field to reenter your authentication code.</p>
<h3 id="what-happens-to-my-nameservers-when-i-transfer-my-domain-to-cloudflare">What happens to my nameservers when I transfer my domain to Cloudflare</h3>
<p>Cloudflare Registrar only supports transfers of domains that are active on a Cloudflare <a href="/dns/zone-setups/full-setup/">full setup</a>. Domains on Cloudflare use <a href="/dns/nameservers/nameserver-options/#assignment-method">nameservers assigned by Cloudflare</a> to the associated account and those nameservers must remain in place for the domain to be Active.</p>
<h3 id="why-didn-t-my-domain-s-expiration-date-change-after-transferring-it-to-cloudflare">Why didn't my domain's expiration date change after transferring it to Cloudflare</h3>
<p>For most generic TLDs (<code>.com</code>, <code>.net</code>, <code>.org</code>, and similar), a transfer adds one year to your current expiration date. However, some TLDs do not add a year on transfer:</p>
<ul>
<li><strong><code>.uk</code> and <code>.nz</code> domains</strong>: These country-code TLDs do not add an additional year during the transfer process.</li>
<li><strong>Domains at or near the maximum term</strong>: ICANN-governed TLDs cap the registration term at 10 years. If your domain already has 10 years on the term, no additional year can be added. Some country-code TLDs have shorter caps (for example, <code>.co</code> has a 5-year cap), so transfers of those domains may also not add a year.</li>
</ul>
<p>If none of the above apply and your expiration date still did not change, refer to <a href="#my-domains-registration-was-not-extended-by-one-year-after-transferring-to-cloudflare">My domain's registration was not extended by one year after transferring to Cloudflare</a> for the 45-day renewal restriction.</p>
<h3 id="if-i-registered-my-domain-for-10-years-at-another-registrar-will-i-gain-another-year-if-i-transfer-it-to-cloudflare">If I registered my domain for 10 years at another registrar, will I gain another year if I transfer it to Cloudflare</h3>
<p>No. A domain cannot have more than 10 years on the term. If you registered your domain for 10 years, you will get 10 years upon transferring it to Cloudflare.</p>
<h3 id="how-do-i-move-a-domain-from-one-cloudflare-account-to-another">How do I move a domain from one Cloudflare account to another</h3>
<p>You can move a Cloudflare Registrar domain between accounts yourself when both the source and target accounts confirm. For full steps, refer to <a href="/registrar/account-options/inter-account-transfer/">Move a Cloudflare Registrar domain registration between accounts</a>.</p>
<p>Before you start, the domain must meet these conditions:</p>
<ul>
<li>It was registered more than 10 days ago.</li>
<li>The registrant email is verified and there is no pending Change of Registrant request.</li>
<li><a href="/registrar/get-started/enable-dnssec/">DNSSEC</a> is turned off (you can re-enable it after the move).</li>
<li>The domain is not administratively locked and is not in <code>redemptionPeriod</code>, <code>pendingDelete</code>, or <code>pendingTransfer</code>.</li>
<li>You have added the domain as a website to the target account, selected a plan, and have the target account ID ready.</li>
</ul>
<p>Submit the move from the <strong>Configuration</strong> tab of the <strong>Manage Domain</strong> page. The gaining account receives an email and must approve within five days or the request auto-cancels. All configuration and settings in the source account are lost, and the domain is transfer-locked for 30 days after the move.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/458.md")
</aside>
<hr />
<h2 id="domain-registrations">Domain registrations</h2>
<h3 id="i-was-charged-for-a-domain-but-it-is-not-showing-in-the-dashboard-what-happened">I was charged for a domain but it is not showing in the dashboard. What happened</h3>
<p>Domain registrations do not appear in the <strong>Active Subscriptions</strong> section, because Registrar is not subscription-based. Your domains live on the <a href="/registrar/account-options/domain-management/">Domain management</a> page. A new registration usually completes in about 30 seconds and sends a confirmation email.</p>
<p>If you were charged but still do not see the domain:</p>
<ul>
<li>Check which account and email you used at checkout. The domain lands in the Cloudflare account you were logged into, and many people have more than one account. This is the most common cause.</li>
<li>Find the registration confirmation email.</li>
<li>A failed-then-retried checkout can leave a temporary authorization hold (not a completed charge). These typically drop off on their own.</li>
</ul>
<p>If money left your account and the domain still is not in the correct account after a short wait, open a support ticket with the charge details and exact domain name so it can be reconciled.</p>
<h3 id="my-domain-expired-or-a-renewal-failed-can-i-still-get-it-back">My domain expired or a renewal failed. Can I still get it back</h3>
<p>Usually yes, within a window. Cloudflare attempts auto-renew about 30 days before expiration and, if it fails, retries three more times before you must renew manually. A failed renewal is almost always a payment problem, so fix the card or billing profile and manually renew from the <strong>Domain management</strong> page (up to 10 years). Refer to <a href="/registrar/account-options/renew-domains/">Renew domains</a>.</p>
<p>If the domain already expired, refer to <a href="#what-happens-when-a-domain-expires">What happens when a domain expires?</a> for the grace, suspension, redemption, and pending delete lifecycle.</p>
<h3 id="what-happens-when-a-domain-expires">What happens when a domain expires</h3>
<p>In summary, here is what will happen after a domain expires:</p>
<ul>
<li><strong>Day 0</strong>: Expiration Date.</li>
<li><strong>Day 1 - 30</strong>: Grace Period (domain resolves normally).</li>
<li><strong>Day 31 - 40</strong>: Suspension Period (domains resolves to suspension page).</li>
<li><strong>Day 41 - 70</strong>: Redemption Period.</li>
<li><strong>Day 71 - 75</strong>: Pending Delete Period.</li>
</ul>
<p>Cloudflare currently offers a 40-day grace period for most top-level domains (TLDs).</p>
<p>During this period you may renew/extend the domain at any time from within the dashboard but no further auto-renew attempts will be made. For the first 30 days of the grace period, the domain will continue to resolve as normal. On the 30th day after the expiration date, the domain will be suspended and a parked suspension page will be displayed. You may still renew the domain at any time during this suspension period. On the 40th day, the domain will enter the Redemption Period and will no longer resolve to any web page.</p>
<p>The redemption period lasts for 30 days. During this time, it may be possible to restore and renew the domain. A restore fee may apply in addition to the renewal fee. At the end of the 30 day redemption period, the domain will be placed in pending delete status for a period of five days, after which it will be released and made available for re-registration. The domain cannot be restored or renewed during this period.</p>
<p>If the domain is in a state where it can be restored, the Manage Domain page in the Registrar section of the dashboard will display a message indicating the domain is restorable. You will then be able to initiate the restore process directly from the dashboard.</p>
<p>Cloudflare does not guarantee against domain loss in the sense of fully indemnifying you for business losses if you lose your domain. However, mechanisms are in place to alert you of domain expiration and redemption grace periods should your domain expire. You can also elect to set up your domain registration to renew automatically. For an additional layer of control over your domains, refer to <a href="https://www.cloudflare.com/products/registrar/custom-domain-protection/">Domain Protection Service</a>.</p>
<h3 id="my-domain-s-registration-was-not-extended-by-one-year-after-transferring-to-cloudflare">My domain's registration was not extended by one year after transferring to Cloudflare</h3>
<p>Most transfers add one year to your registration. However, if your domain expired, you renewed it to keep it, and then transferred within 45 days of renewal, you will be charged for the transfer but no additional year will actually be added. This is a registry restriction that applies to all registrars, not just Cloudflare.</p>
<p>For example, say <code>example.com</code> expires and you renew it a few days later, extending the registration by one year. You then transfer to Cloudflare about ten days after that renewal. Because the transfer is within 45 days of renewal, the registry does not add an additional year. Your expiration date remains the renewed date.</p>
<p>To avoid this, wait at least 45 days after renewal before transferring.</p>
<p>If this already happened, you have effectively paid twice for the same year. You are entitled to request a refund from your previous registrar.</p>
<hr />
<h2 id="billing">Billing</h2>
<h3 id="how-much-does-cloudflare-registrar-cost">How much does Cloudflare Registrar cost</h3>
<p>Refer to <a href="https://www.cloudflare.com/learning/dns/what-is-cloudflare-registrar/">What is Cloudflare Registrar</a> for more information on pricing.</p>
<h3 id="can-i-get-a-refund-for-a-domain-i-registered-or-renewed-by-mistake">Can I get a refund for a domain I registered or renewed by mistake</h3>
<p>No. Cloudflare Registrar sells domains at cost: you pay the registry and ICANN list price with no markup. Because that money is passed straight to the registry the moment a registration, renewal, or transfer completes, those fees are non-refundable. All renewals are final and Cloudflare will not issue refunds.</p>
<p>If you registered the wrong name, such as a typo or the wrong TLD (<code>.com</code> versus <code>.co</code>), the registration fee has already gone to the registry and cannot be reclaimed. To prevent an unwanted future charge, turn off auto-renew (<strong>Manage Domains</strong> &gt; your domain &gt; <strong>Auto-renew</strong> toggle) at least 30 days before the expiration date and let the domain lapse. Refer to <a href="/registrar/account-options/renew-domains/">Renew domains</a>.</p>
<h3 id="when-will-i-be-billed">When will I be billed</h3>
<p>You will be billed when you input your authorization code and initiate the transfer of your domain to Cloudflare. Currently, Cloudflare Registrar only uses the primary payment method for any associated transaction. Make sure to copy and paste the code to avoid mistakes. The transfer will not initiate if the code is incorrect.</p>
<h3 id="why-was-i-charged-to-transfer-a-domain-or-why-do-i-see-two-charges">Why was I charged to transfer a domain, or why do I see two charges</h3>
<p>A transfer into Cloudflare is not free because most registries require every transfer to include at least one additional year of registration. Cloudflare charges that year at cost, with no markup, and adds it to your current expiration date. Some country-code domains, such as <code>.uk</code> and <code>.nz</code>, have no transfer fee.</p>
<p>Two things people read as double charging that usually are not:</p>
<ul>
<li>A failed-then-retried checkout can leave a temporary authorization hold that drops off. This is not a second charge.</li>
<li>If you renewed at your old registrar and then transferred to Cloudflare within 45 days of that renewal, the registry does not add the extra year even though you paid for the transfer, so you have effectively paid twice for the same year. You are entitled to request a refund from your previous registrar. To avoid this, wait at least 45 days after a renewal before transferring. Refer to <a href="#my-domains-registration-was-not-extended-by-one-year-after-transferring-to-cloudflare">My domain's registration was not extended by one year after transferring to Cloudflare</a>.</li>
</ul>
<h3 id="is-there-a-fee-to-transfer-a-uk-or-nz-domain">Is there a fee to transfer a .UK or .NZ domain</h3>
<p>No, there is no fee to transfer a <code>.uk</code> or <code>.nz</code> domain. Also, an additional year is NOT added during the transfer process. However, if the domain is nearing the expiration date and is set to auto-renew, it may be automatically renewed shortly after the completion of the transfer.</p>
<hr />
<h2 id="domain-restoration">Domain restoration</h2>
<h3 id="which-domains-are-eligible-to-be-restored">Which domains are eligible to be restored</h3>
<p>Domains that are in the Redemption Period and have an EPP status of redemptionPeriod may be restored. For most TLDs this will include domains that are between 40 and 70 days past expiration.</p>
<p><code>.uk</code> domains cannot be restored using the standard redemption process. However, <code>.uk</code> domains can be restored by renewing the domain (no additional restore fee) up until 90 days after expiration.</p>
<h3 id="is-there-a-fee-to-restore-a-domain">Is there a fee to restore a domain</h3>
<p>Yes, in most cases there is a restore fee.</p>
<p>The amount varies depending on the TLD. The restore fee is separate from the renewal fee. You will be presented with both the restore and renewal fees before confirming that you wish to proceed.</p>
<h3 id="will-the-domain-be-renewed-after-the-restore-has-completed">Will the domain be renewed after the restore has completed</h3>
<p>Yes. We will attempt to renew the domain after the restore has been completed. While not common, it is possible for the renewal transaction to fail.</p>
<p>In the event of a failure, we will make several retry attempts. If we are unable to process the renewal after several retries, you will be presented with a message that you should contact support for assistance.</p>
<h3 id="how-long-does-the-restore-process-take">How long does the restore process take</h3>
<p>The entire process can take a few minutes to complete.</p>
<p>There are multiple steps to the restore process, and each step must be completed in a specific sequence. These steps are performed automatically by the system. The UI will continue to poll for an updated status and will provide feedback as each step completes.</p>
<h3 id="what-happens-if-the-domain-renewal-fails">What happens if the domain renewal fails</h3>
<p>The restore and the renewal are two distinct processes that happen sequentially.</p>
<p>In rare cases the domain may be successfully restored but the renewal fails. We will make several attempts to renew the domain. However, should all the renewals fail the customer may attempt to manually renew the domain or contact support so we may investigate the cause of the failure.</p>
<h3 id="can-a-restore-be-reversed-or-refunded">Can a restore be reversed or refunded</h3>
<p>No. Once a restore has been completed it can not be reversed. It may be possible to delete the domain again but there are no refunds.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/457.md")
</aside>
<hr />
<h2 id="domain-deletions">Domain deletions</h2>
<h3 id="why-am-i-unable-to-delete-my-registrar-domain">Why am I unable to delete my Registrar domain</h3>
<p>A domain can only be deleted if all the following conditions are met:</p>
<ul>
<li>The user initiating the action is a Super Admin or Read/Write Administrator.</li>
<li>The domain is not delete locked at the registry with either <code>clientDeleteProhibited</code> or <code>serverDeleteProhibited</code>.</li>
<li>The domain is not already in <code>pendingDelete</code>, <code>redemptionPeriod</code>, or in <code>pendingTransfer</code>.</li>
<li>The domain has not been administratively locked by Cloudflare. This typically occurs for legal reasons such as a UDRP filing or court order, but may also be the result of an abuse or payment investigation.</li>
<li>The domain is NOT a .UK domain. .UK domains currently cannot be deleted at the registry.</li>
</ul>
<p>If any of the above conditions are not met, the domain cannot be deleted.</p>
<h3 id="who-has-permission-to-delete-a-domain-registration">Who has permission to delete a domain registration</h3>
<p>Only Super Admins and Administrators with Read/Write access can initiate the deletion of a domain. Note that only Super Admins will receive the email with the delete token.</p>
<h3 id="will-i-receive-a-refund-for-my-deleted-domain-registration">Will I receive a refund for my deleted domain registration</h3>
<p>No. Refunds will not be issued for costs incurred by a domain registration.</p>
<h3 id="how-do-i-get-the-domain-deletion-token">How do I get the domain deletion token</h3>
<p>The delete token is only sent to the Super Admins of the account. If the user requesting the deletion is not a Super Admin they will need to obtain the delete token from one of the Super Admins of the account.</p>
<h3 id="how-long-is-the-domain-deletion-token-valid-for">How long is the domain deletion token valid for</h3>
<p>The delete token is valid for 30 minutes. After the 30 minutes the code will expire and the user must restart the process.</p>
<h3 id="will-the-domain-be-deleted-immediately-from-my-account">Will the domain be deleted immediately from my account</h3>
<p>If the domain is within 5 days of the initial registration, the domain will be immediately released by the registry and made available for re-registration. In this scenario the domain will be immediately removed from the registrar section of the account. You may need to refresh the page to force an update of the data.</p>
<p>If the domain is more than 5 days old, it will enter the redemption period and will remain in account until the redemption period expires and the registry releases the domain.</p>
