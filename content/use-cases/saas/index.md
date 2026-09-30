<p>Build multi-tenant platforms with custom domains, isolated compute, and per-customer configuration. Cloudflare SSL for SaaS provisions and renews SSL certificates for every customer hostname. Workers for Platforms runs customer code in isolated V8 environments. D1, KV, and R2 provide per-tenant data storage. Workers Analytics Engine and Logpush track usage for billing and compliance.</p>
<ul class="directory-listing"><li><a href="/use-cases/saas/custom-domains/">Customer domains with SSL for SaaS</a></li><li><a href="/use-cases/saas/code-deployment/">Enable customer code deployment</a></li><li><a href="/use-cases/saas/data-isolation/">Store and isolate customer data</a></li><li><a href="/use-cases/saas/protect-platform/">Protect your platform</a></li><li><a href="/use-cases/saas/usage-analytics/">Observe customer usage and billing</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="custom-domains-with-ssl">Custom domains with SSL</h3>
<p>Allow customers to use their own domains with automatic certificate management:</p>
<ul>
<li><strong>SSL for SaaS</strong> provisions and renews certificates for every custom hostname</li>
<li><strong>Cloudflare for Platforms</strong> routes customer domains to your platform with per-tenant configuration</li>
</ul>
<h3 id="multi-tenant-compute">Multi-tenant compute</h3>
<p>Let customers deploy their own code on your platform:</p>
<ul>
<li><strong>Workers for Platforms</strong> runs customer code in isolated V8 environments</li>
<li><strong>Dispatch namespaces</strong> route requests to the correct tenant Worker based on hostname or path</li>
<li><strong>SSL for SaaS</strong> handles custom domains for each tenant</li>
</ul>
<h3 id="full-multi-tenant-platform">Full multi-tenant platform</h3>
<p>Combine custom domains, tenant compute, and isolated storage:</p>
<ul>
<li><strong>SSL for SaaS</strong> manages customer hostnames and certificates</li>
<li><strong>Workers for Platforms</strong> runs per-tenant application logic</li>
<li><strong>D1</strong> or <strong>KV</strong> stores per-tenant data with database-level or key-prefix isolation</li>
<li><strong>R2</strong> stores per-tenant files and assets</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> for your platform (for example, <code>yourplatform.com</code>). SSL for SaaS uses this as the provider domain against which customer custom hostnames are issued. Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/enable/">Enable Cloudflare for SaaS</a>.</li>
<li>A <a href="/workers/platform/pricing/">Workers Paid plan</a> for Workers for Platforms. Dispatch namespaces, which route requests to customer-specific Workers, are not available on the free tier.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) and <a href="/workers/wrangler/install-and-update/">Wrangler</a> installed.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> for your platform. This is your domain, not your customers' domains. SSL for SaaS issues customer custom hostnames against this provider domain. Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/enable/">Enable Cloudflare for SaaS</a>.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) and <a href="/workers/wrangler/install-and-update/">Wrangler</a> if you plan to add Workers for Platforms or manage bindings programmatically.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15224.md")
</div>
