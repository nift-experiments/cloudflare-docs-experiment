<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 19, 2025</time><h2 id="post-title">Terraform v5.15.0 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.15 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="features">Features</h4>
<ul>
<li><strong>ai_search:</strong> Add AI Search endpoints (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6f02adb420e872457f71f95b49cb527663388915">6f02adb</a>)</li>
<li><strong>certificate_pack:</strong> Ensure proper Terraform resource ID handling for path parameters in API calls (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/081f32acab4ce9a194a7ff51c8e9fcabd349895a">081f32a</a>)</li>
<li><strong>worker_version:</strong> Support <code>startup_time_ms</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/286ab55bea8d5be0faa5a2b5b8b157e4a2214eba">286ab55</a>)</li>
<li><strong>zero_trust_dlp_custom_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_integration_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_predefined_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_gateway_policy:</strong> Support <code>forensic_copy</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
<li><strong>zero_trust_list:</strong> Support additional types (category, location, device) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
</ul>
<h4 id="bug-fixes">Bug fixes</h4>
<ul>
<li><strong>access_rules:</strong> Add validation to prevent state drift. Ideally, we'd use Semantic Equality but since that isn't an option, this will remove a foot-gun. (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/44577911b3cbe45de6279aefa657bdee73c0794d">4457791</a>)</li>
<li><strong>cloudflare_pages_project:</strong> Addressing drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6edffcfcf187fdc9b10b624b9a9b90aed2fb2b2e">6edffcf</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3db318e747423bf10ce587d9149e90edcd8a77b0">3db318e</a>)</li>
<li><strong>cloudflare_worker:</strong> Can be cleanly imported (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/4859b52968bb25570b680df9813f8e07fd50728f">4859b52</a>)</li>
<li><strong>cloudflare_worker:</strong> Ensure clean imports (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5b525bc478a4e2c9c0d4fd659b92cc7f7c18016a">5b525bc</a>)</li>
<li><strong>list_items:</strong> Add validation for IP List items to avoid inconsistent state (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/b6733dc4be909a5ab35895a88e519fc2582ccada">b6733dc</a>)</li>
<li><strong>zero_trust_access_application:</strong> Remove all conditions from sweeper (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3197f1aed61be326d507d9e9e3b795b9f1d18fd7">3197f1a</a>)</li>
<li><strong>spectrum_application:</strong> Map missing fields during spectrum resource import (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6495">#6495</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/ddb4e722b82c735825a549d651a9da219c142efa">ddb4e72</a>)</li>
</ul>
<h4 id="upgrade-to-newer-version">Upgrade to newer version</h4>
We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
</div></article></div>
