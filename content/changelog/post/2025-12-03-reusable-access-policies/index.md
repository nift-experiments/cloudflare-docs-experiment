<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 4, 2025</time><h2 id="post-title">One-click Access protection for Workers now creates reusable Cloudflare Access policies</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers applications now use reusable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policies</a> to reduce duplication and simplify access management across multiple Workers.</p>
<p>Previously, enabling Cloudflare Access on a Worker created per-application policies, unique to each application. Now, we create reusable policies that can be shared across applications:</p>
<ul>
<li>
<p><strong>Preview URLs</strong>: All Workers preview URLs share a single &quot;Cloudflare Workers Preview URLs&quot; policy across your account. This policy is automatically created the first time you enable Access on any preview URL. By sharing a single policy across all preview URLs, you can configure access rules once and have them apply company-wide to all Workers which protect preview URLs. This makes it much easier to manage who can access preview environments without having to update individual policies for each Worker.</p>
</li>
<li>
<p><strong>Production workers.dev URLs</strong>: When enabled, each Worker gets its own reusable policy (named <code>&lt;worker-name&gt; - Production</code>) by default. We recognize production services often have different access requirements and having individual policies here makes it easier to configure service-to-service authentication or protect internal dashboards or applications with specific user groups. Keeping these policies separate gives you the flexibility to configure exactly the right access rules for each production service. When you disable Access on a production Worker, the associated policy is automatically cleaned up if it's not being used by other applications.</p>
</li>
</ul>
<p>This change reduces policy duplication, simplifies cross-company access management for preview environments, and provides the flexibility needed for production services. You can still customize access rules by editing the reusable policies in the Zero Trust dashboard.</p>
<p>To enable Cloudflare Access on your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Workers &amp; Pages</strong>.</li>
<li>Select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, click <strong>Manage Cloudflare Access</strong> to customize the policy.</li>
</ol>
<p>For more information on configuring Cloudflare Access for Workers, refer to the <a href="/workers/configuration/routing/workers-dev/#manage-access-to-workersdev">Workers Access documentation</a>.</p>
</div></article></div>
