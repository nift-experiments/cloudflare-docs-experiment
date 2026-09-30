<p>Reach out to your account team at least 30 days prior to the expected traffic surge to schedule a Security Optimization walkthrough with your Customer Solution Engineer.</p>
<p>To learn more about our service offerings, refer to <a href="https://www.cloudflare.com/success-offerings/">Customer Success offerings</a>.</p>
<h2 id="register-your-users">Register your users</h2>
<p>For the security and protection of your account, be sure to register all account users.</p>
<ol>
<li>In the Cloudflare dashboard, go to the  <strong>Manage Account</strong> &gt; <strong>Members</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select more than one Super Administrator to ensure appropriate access when needed.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10277.md")
</aside>
<p>Failure to register account users can create issues with our ticketing system. Unverified users who contact support will be funneled to the self-serve queue rather than the Enterprise queue which can result in long wait times.</p>
<p>We strongly advise against credential-sharing which can jeopardize the trust and safety of your account.</p>
<h2 id="confirm-user-and-domain-administration">Confirm user and domain administration</h2>
<ul>
<li><strong>Multi-User:</strong> Provide role-based permissions to a group of users to better control the administration of your domains. Each user has their own role and limited API key.</li>
<li><strong>Enforce 2FA:</strong> Ensure your entire dashboard is secure by <a href="/fundamentals/user-profiles/2fa/">enforcing 2-factor authentication</a> for your organization.
<ul>
<li>To disable 2FA, submit a support ticket and allow 1-2 business days to validate your request.</li>
</ul>
</li>
<li><strong>Leverage API Access:</strong> Work easily with our system programmatically using our <a href="https://api.cloudflare.com">API</a>.</li>
</ul>
<h2 id="additional-items">Additional items</h2>
<ul>
<li>Check when your <a href="/ssl/edge-certificates/custom-certificates/renewing/">SSL Certificates expire (only custom and origin certificates)</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10276.md")
</aside>
- Review your Operational and Disaster recovery preparedness
    - Enable Load Balancing with smart cache strategies: Use [Cloudflare Load Balancing](/reference-architecture/architectures/load-balancing) to distribute traffic across multiple healthy origins, and increase cache-hit ratios by leveraging [custom cache rules](/cache/performance-review/cache-analytics) and [edge compute](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/) (e.g., Cloudflare Workers) to offload origin traffic during high-demand periods.
    - Configure failover pools and back up DNS with a playbook: Set up [Cloudflare Load Balancer failover pools](/reference-architecture/architectures/load-balancing) to automatically redirect traffic to healthy origins if one fails. Export DNS records for safekeeping and prepare a clear [incident response plan](https://www.cloudflare.com/learning/performance/preventing-downtime) that includes steps for re-routing or recovery.
- Review and update your current users' access
- Check your domain registry validity
