<h2 id="domain-status">Domain status</h2>
<p>When your domain is registered with Cloudflare, you can review your domain status in <strong>Overview</strong>.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>From <strong>Overview</strong>, scroll down to <strong>Domain Registration</strong> to review the current expiration date.</li>
<li>Select <strong>Manage domain</strong> to review the Auto-Renew status for your domain.</li>
</ol>
<h2 id="billing-information">Billing information</h2>
<p>Domain registrations will not appear in the <strong>Active Subscriptions</strong> section of the dashboard, as Registrar is not subscription based. To check information related to your domain billing:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage Domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the domain you want to check and select <strong>Manage</strong>.</li>
<li>Refer to <strong>Registration</strong> for information regarding your domain fees. From here, you can also opt to <a href="/registrar/account-options/renew-domains/">renew or extend</a> your domain registration.</li>
</ol>
<h2 id="edit-whois-records">Edit WHOIS records</h2>
<p>Cloudflare redacts WHOIS information from your domain by default. However, we do store the authentic WHOIS record for your domain. You may edit the WHOIS contact data for any domain. To do that:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage Domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the domain you want to edit and select <strong>Manage</strong> &gt; <strong>Contacts</strong>.</li>
<li>Select <strong>Edit</strong> in any of the contacts you previously set up. This allows you to update the contact information for the selected domain only. It will not update the contact information for other domains within the account.</li>
</ol>
<p>Refer to <a href="/registrar/account-options/domain-contact-updates/">Registrant contact updates</a> for more information.</p>
<h2 id="edit-default-contact-information">Edit Default Contact information</h2>
<p>The first time you transfer or register a new domain, a Cloudflare Registrar creates a Default Contact with information that can be used for future transfers and registrations. The contact data may be updated at any time in the dashboard. Updating the Default Contact data will not update the contact information for any domains already in the account. This Default Contact data is only used to prepopulate contact information for new registrations and transfers.</p>
<p>It is important that you keep this information accurate and up-to-date. Refer to <a href="/registrar/account-options/domain-contact-updates/">Registrant contact updates</a> for important information about this topic, and to learn how to update this information.</p>
<h2 id="delete-a-domain-registration">Delete a domain registration</h2>
<p>Domains using Cloudflare Registrar will be deleted automatically after expiration if they have not been renewed. The exact timing varies, refer to <a href="/registrar/faq/#what-happens-when-a-domain-expires">What happens when a domain expires?</a> for more details.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deletion-is-irreversible">Deletion is irreversible</h3>
@markup("md", "content/.markup/bodies/12764.md")
</aside>
<p>There may be instances where users may wish to delete a domain prior to expiration. In most cases a domain may be deleted prior to expiration by following these steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Manage Domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Under the <strong>Configuration</strong> tab on the Manage page you will find a <strong>Delete</strong> button.</li>
<li>If the domain is deletable the button will be active.  The button will be disabled if your domain cannot be deleted and you should refer to the Registrar <a href="/registrar/faq/#why-am-i-unable-to-delete-my-registrar-domain">FAQ</a>.</li>
<li>Once you click the Delete button, you will be presented with a confirmation window. If you proceed, an email will be sent to all users with the Super Admin role in the account. The email contains a deletion authorization token that must be entered into the window which appears to confirm and complete the deletion.</li>
</ol>
<p>Once all steps are completed, the domain will then be scheduled for deletion. To understand more about the timelines and potential reasons why a domain cannot be deleted, refer to the Registrar <a href="/registrar/faq/#domain-deletions">FAQ</a>.</p>
