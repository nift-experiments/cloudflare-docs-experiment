<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 24, 2026</time><h2 id="post-title">Automate migration from Cloudflare's Terraform v4 to v5 provider</h2>
<div class="changelog-badges"><span>terraform</span></div><div class="changelog-body"><p>We're excited to announce <strong>tf-migrate</strong>, a purpose-built CLI tool that simplifies migrating from Cloudflare Terraform Provider v4 to v5.</p>
<h4 id="v5-is-stable-and-ready-for-production">v5 is stable and ready for production</h4>
<p><strong>Terraform Provider v5 is stable and actively receiving updates.</strong>  We encourage all users to migrate to v5 to take advantage of ongoing enhancements and new capabilities.</p>
<p>Cloudflare uses tf-migrate to migrate our own infrastructure — the same tool we're providing to the community — ensuring the best possible migration experience.</p>
<h4 id="what-tf-migrate-does">What tf-migrate does</h4>
<p><strong>tf-migrate</strong> automates the tedious and error-prone parts of the v4 to v5 migration process:</p>
<ul>
<li><strong>Resource type renames</strong> – Automatically updates <code>cloudflare_record</code> → <code>cloudflare_dns_record</code>, <code>cloudflare_access_application</code> → <code>cloudflare_zero_trust_access_application</code>, and 40+ other renamed resources</li>
<li><strong>Attribute transformations</strong> – Updates field names (e.g., <code>value</code> → <code>content</code> for DNS records) and restructures nested blocks</li>
<li><strong>Moved block generation</strong> – Creates Terraform 1.8+ <code>moved</code> blocks to prevent resource replacements and ensure zero-downtime migrations</li>
<li><strong>Cross-file reference updates</strong> – Automatically finds and updates all references to renamed resources across your entire configuration</li>
<li><strong>Dry-run mode</strong> – Preview all changes before applying them to ensure safety</li>
</ul>
<p>Combined with the automatic state upgraders introduced in v5.19+, tf-migrate eliminates the manual work and risk that previously made v5 migrations challenging. Tf-migrate operates directly on the config, and the built-in state upgraders handle the rest.</p>
<h4 id="supported-resources">Supported resources</h4>
<p>Tf-migrate currently supports the most common Terraform resources our customers use. We are actively working to expand coverage, with the most commonly used resources prioritized first.</p>
<p>For the complete list of supported resources and their migration status, refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">v5 Stabilization Tracker</a>. This list is updated regularly as additional resources are stabilized and migration support is added.</p>
<p>Resources not yet supported by tf-migrate will need to be migrated manually using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">version 5 upgrade guide</a>. The upgrade guide provides step-by-step instructions for handling resource renames, attribute changes, and state migrations.</p>
<h4 id="get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/tf-migrate/releases">Download tf-migrate</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration">Version 5 Migration Guide</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Terraform Provider documentation</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">v5 Stabilization Tracker</a></li>
</ul>
<p>We have been releasing Betas over the past month and a half while testing this tool. See the full changelog of those Betas here: <a href="https://github.com/cloudflare/tf-migrate/releases">tf-migrate releases</a>.</p>
</div></article></div>
