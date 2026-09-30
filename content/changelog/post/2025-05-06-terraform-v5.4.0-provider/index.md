<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 6, 2025</time><h2 id="post-title">Terraform v5.4.0 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="changes">Changes</h4>
<ul>
<li>
<p>Removes the <code>worker_platforms_script_secret</code> resource from the provider (see <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret">migration guide</a> for alternatives—applicable to both Workers and Workers for Platforms)</p>
</li>
<li>
<p>Removes duplicated fields in <code>cloudflare_cloud_connector_rules</code> resource</p>
</li>
<li>
<p>Fixes <code>cloudflare_workers_route</code> id issues <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134">#5134</a> <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501">#5501</a></p>
</li>
<li>
<p>Fixes issue around refreshing resources that have unsupported response types</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre><code>  &lt;li&gt;`cloudflare_certificate_pack`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_registrar_domain`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_download`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_webhook`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_user`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_kv`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_script`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixes <code>cloudflare_workers_kv</code> state refresh issues</p>
</li>
<li>
<p>Fixes issues around configurability of nested properties without computed values for the following resources</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre><code>  &lt;li&gt;`cloudflare_account`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_dns_settings`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_api_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_cloud_connector_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_custom_ssl`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_d1_database`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_dns_record`&lt;/li&gt;&#10;  &lt;li&gt;`email_security_trusted_domains`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_hyperdrive_config`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_keyless_certificate`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_list_item`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_load_balancer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_logpush_dataset_job`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_network_monitoring_configuration`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_lan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_wan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_wan_static_route`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_notification_policy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_pages_project`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue_consumer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_cors`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_event_notification`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lifecycle`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lock`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_sippy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_ruleset`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippet_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippets`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_spectrum_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_deployment`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_group`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixed defaults that made <code>cloudflare_workers_script</code> fail when using Assets</p>
</li>
<li>
<p>Fixed Workers Logpush setting in <code>cloudflare_workers_script</code> mistakenly being readonly</p>
</li>
<li>
<p>Fixed <code>cloudflare_pages_project</code> broken when using &quot;source&quot;</p>
</li>
</ul>
<p>The detailed <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0">changelog</a> is available on GitHub.</p>
<h4 id="upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>, or by opening a <a href="https://www.support.cloudflare.com/s/?language=en_US">support ticket</a>.</p>
<h4 id="for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div></article></div>
