<p>Cloudflare Access provides visibility and control over who has access to your <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a>. You can allow or block users based on identity, device posture, and other <a href="/cloudflare-one/access-controls/policies/">Access rules</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>You must have an active custom hostname. For setup instructions, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Configuring Cloudflare for SaaS</a>.</li>
<li>You must have a Cloudflare Zero Trust plan in your SaaS provider account. Learn more about <a href="/cloudflare-one/setup/">getting started with Zero Trust</a>.</li>
<li>You can only run Access on custom hostnames if they are managed externally to Cloudflare or in a separate Cloudflare account. If the custom hostname zone is in the same account as the SaaS zone, the Access application will not be applied.</li>
</ul>
<h2 id="setup">Setup</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select your SaaS provider account and go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong>.</li>
<li>Select <strong>Self-hosted and private</strong>.</li>
<li>Select <strong>Add public hostname</strong>.</li>
<li>Select <strong>Switch to custom input</strong>.</li>
<li>In <strong>Hostname</strong>, enter your custom hostname (for example, <code>mycustomhostname.com</code>).</li>
<li>Follow the remaining <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application creation steps</a> to publish the application.</li>
</ol>
