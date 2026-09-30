<p>With Cloudflare Access, you can require that users obtain approval before they can access a specific self-hosted application or SaaS application. The administrator will receive an email notification to approve or deny the request. Unlike a typical Allow policy, the user will have to request access at the end of each session. This allows you to define the users who should have persistent access and those who must request temporary access.</p>
<h2 id="set-up-temporary-authentication">Set up temporary authentication</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Choose a <strong>Self-hosted</strong> or <strong>SaaS</strong> application and select <strong>Configure</strong>.</li>
<li>Choose an <strong>Allow</strong> policy and select <strong>Configure</strong>.</li>
<li>Under <strong>Additional settings</strong>, turn on <a href="/cloudflare-one/access-controls/policies/require-purpose-justification/"><strong>Purpose justification</strong></a>.</li>
<li>Turn on <strong>Temporary authentication</strong>.</li>
<li>Enter the <strong>Email addresses of the approvers</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4575.md")
</aside>
7. Save the policy.
<p>Temporary authentication is now enabled for users who match this policy. You can optionally add a second <strong>Allow</strong> policy for users who should have persistent access. Be sure the policy order is set to allow persistent users through.</p>
<h2 id="temporary-authentication-requests">Temporary authentication requests</h2>
<p>When a user accesses the application, they will be prompted to enter a purpose justification and submit an access request. The request is automatically emailed to approvers. Alternatively, the user can manually present the approval link to approvers.
<img src="/assets/upstream/images/cloudflare-one/policies/temp-auth-request.png" alt="Temporary authentication request page shown to users" /></p>
<p>Approvers will receive a request similar to the example below. The approver can then grant access for a set amount of time, up to a maximum of 24 hours.</p>
<p><img src="/assets/upstream/images/cloudflare-one/policies/temp-auth-approval.png" alt="Temporary authentication approval page shown to administrators" /></p>
