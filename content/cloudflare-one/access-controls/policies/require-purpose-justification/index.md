<p>Cloudflare Access allows security and IT teams to present users with a purpose justification screen directly after they log in to an Access application. This allows organizations to audit not only for who is accessing their resources, but also for why they are requesting access.</p>
<p>The purpose justification screen will show for any new sessions of an application. For example, if an Access application has a session time of eight hours, a user will see the purpose justification screen once every eight hours.</p>
<p>Configuring a purpose justification screen is done as part of configuring an Access policy.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Choose an application and select <strong>Configure</strong>.</li>
<li>Go to <strong>Policies</strong>.</li>
<li>Choose an <strong>Allow</strong> policy and select <strong>Configure</strong>.</li>
<li>Under <strong>Additional settings</strong>, turn on <strong>Purpose justification</strong>.</li>
<li>(Optional) Set a custom purpose justification message. This will appear on the purpose justification screen and will be visible to the user.</li>
<li>Save the policy.</li>
</ol>
<p>Users who match this policy will see the following screen:</p>
<p><img src="/assets/upstream/images/cloudflare-one/policies/purpose-justification.png" alt="Finalized purpose justification screen displaying custom message." /></p>
