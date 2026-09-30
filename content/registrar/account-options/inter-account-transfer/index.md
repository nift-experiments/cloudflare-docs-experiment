<p>Cloudflare supports the move (transfer) of domain registrations between Cloudflare accounts when the source and target account both confirm the move. The move will result in the loss of all configurations and settings for the domain in the source account.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/12760.md")
</aside>
<p>Before proceeding, please be aware of the following:</p>
<ul>
<li>WHOIS contact information will be moved as is.</li>
<li>No other configuration will be moved.</li>
<li>After successful move, the registration will be transfer-locked for 30 days.</li>
<li>The target account will become responsible for domain renewals going forward.</li>
</ul>
<h2 id="1-prepare-for-the-move"><ol>
<li>Prepare for the move</li>
</ol></h2>
<p>Before you request the move, you will need to do the following:</p>
<ul>
<li>Obtain the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> of the new account.</li>
<li>Add the domain as a website to the new account and select a plan.</li>
<li><a href="/dns/dnssec/#disable-dnssec">Disable DNSSEC</a> for the domain and ensure it is set up and ready in the new dashboard account you intend to move it to.</li>
</ul>
<p>The following pre-conditions must be met before the domain can be moved:</p>
<ul>
<li>The domain must have been registered more than 10 days ago.</li>
<li>The domain must be added to the new account as a website and a plan must be selected.</li>
<li>The domain must not be administratively locked, such as being locked due to a dispute or court order.</li>
<li>The domain must not have any of the following registry statuses: <code>pendingDelete</code>, <code>redemptionPeriod</code>, or <code>pendingTransfer</code>.</li>
<li>The registrant email address must be verified.</li>
<li>A pending Change of Registrant request cannot be present. If there is a pending request, it should be completed before initiating the move request.</li>
<li>DNSSEC must be turned off. It can be re-enabled on the new zone once the move completes.</li>
<li>If the current zone is locked, the lock must be released.</li>
</ul>
<h2 id="2-submit-the-move-request"><ol start="2">
<li>Submit the move request</li>
</ol></h2>
<p>You can now submit the move request under the <strong>Configuration</strong> tab of the <strong>Manage Domain</strong> page. Begin the submission process by selecting the <strong>Start</strong> button and follow the instructions.</p>
<p><strong>Important</strong>: Review the pre-conditions described above. If those conditions have not been met, the domain move will not be completed.</p>
<p>Once the move request has been submitted, the gaining account will receive an email notifying them of the request and will provide instructions for how to approve the request.</p>
<p>The gaining account must log into their account and go to <strong>Manage Domains</strong> (under Domain Registration). A message will appear at the top of the page stating that there are domains requiring action to be taken.</p>
<p>Select <strong>View Actions</strong> to display the domains with a pending move along and choose to accept or reject the request. Action must be taken within five days of the request.</p>
<p>If no action is taken within the five days, the request will be automatically canceled.</p>
