---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/19/
  description: '2025-06-20'
  full_title: Developer platform changelog - page 19 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 19 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-06-20"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/19/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 19"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-06-20"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/19/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/19/#page","headline":"Developer platform changelog - page 19 | Cloudflare Docs","description":"2025-06-20","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/19/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/19/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="increased-blob-size-limits-in-workers-analytics-engine"><a href="/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/">Increased blob size limits in Workers Analytics Engine</a></h2>
<p><em>2025-06-20</em></p>
<p>We’ve increased the total allowed size of <a href="/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker"><code>blob</code></a> fields on data points written to <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> from <strong>5 KB to 16 KB</strong>.</p>
<p>This change gives you more flexibility when logging rich observability data — such as base64-encoded payloads, AI inference traces, or custom metadata — without hitting request size limits.</p>
<p>You can find full details on limits for queries, filters, payloads, and more <a href="/analytics/analytics-engine/limits/">here in the Workers Analytics Engine limits documentation</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17779.md")</div>


<h2 id="view-custom-metadata-in-responses-and-guide-ai-search-with-context-in-autorag"><a href="/changelog/post/2025-06-19-autorag-custom-metadata-and-context/">View custom metadata in responses and guide AI-search with context in AutoRAG</a></h2>
<p><em>2025-06-19</em></p>
<p>In <a href="/ai-search/">AutoRAG</a>, you can now view your object's custom metadata in the response from <a href="/ai-search/api/search/workers-binding/"><code>/search</code></a> and <a href="/ai-search/api/search/workers-binding/"><code>/ai-search</code></a>, and optionally add a <code>context</code> field in the custom metadata of an object to provide additional guidance for AI-generated answers.</p>
<p>You can add <a href="/r2/api/workers/workers-api-reference/#r2putoptions">custom metadata</a> to an object when uploading it to your R2 bucket.</p>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-object-s-custom-metadata-in-search-responses">Object's custom metadata in search responses</h4>
<p>When you run a search, AutoRAG now returns any custom metadata associated with the object. This metadata appears in the response inside <code>attributes</code> then <code>file</code> , and can be used for downstream processing.</p>
<p>For example, the <code>attributes</code> section of your search response may look like:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;attributes&quot;: {&#10;		&quot;timestamp&quot;: 1750001460000,&#10;		&quot;folder&quot;: &quot;docs/&quot;,&#10;		&quot;filename&quot;: &quot;launch-checklist.md&quot;,&#10;		&quot;file&quot;: {&#10;			&quot;url&quot;: &quot;https://wiki.company.com/docs/launch-checklist&quot;,&#10;			&quot;context&quot;: &quot;A checklist for internal launch readiness, including legal, engineering, and marketing steps.&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-add-a-context-field-to-guide-llm-answers">Add a <code>context</code> field to guide LLM answers</h4>
<p>When you include a custom metadata field named <code>context</code>, AutoRAG attaches that value to each chunk of the file. When you run an <code>/ai-search</code> query, this <code>context</code> is passed to the LLM and can be used as additional input when generating an answer.</p>
<p>We recommend using the <code>context</code> field to describe supplemental information you want the LLM to consider, such as a summary of the document or a source URL. If you have several different metadata attributes, you can join them together however you choose within the <code>context</code> string.</p>
<p>For example:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;context&quot;: &quot;summary: &#x27;Checklist for internal product launch readiness, including legal, engineering, and marketing steps.&#x27;; url: &#x27;https://wiki.company.com/docs/launch-checklist&#x27;&quot;&#10;}&#10;</code></pre>
<p>This gives you more control over how your content is interpreted, without requiring you to modify the original contents of the file.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="filter-your-autorag-search-by-file-name"><a href="/changelog/post/2025-06-19-autorag-filename-filter/">Filter your AutoRAG search by file name</a></h2>
<p><em>2025-06-19</em></p>
<p>In <a href="/ai-search/">AutoRAG</a>, you can now <a href="/ai-search/configuration/indexing/metadata/">filter</a> by an object's file name using the <code>filename</code> attribute, giving you more control over which files are searched for a given query.</p>
<p>This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.</p>
<p>For example, your search query may look like:</p>
<pre tabindex="0"><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;what is the project deadline?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;filename&quot;,&#10;		value: &quot;project-alpha-roadmap.md&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>


<h2 id="automate-worker-deployments-with-a-simplified-sdk-and-more-reliable-terraform-provider"><a href="/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/">Automate Worker deployments with a simplified SDK and more reliable Terraform provider</a></h2>
<p><em>2025-06-19</em></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-simplified-worker-deployments-with-our-sdks">Simplified Worker Deployments with our SDKs</h4>
<p>We've simplified the programmatic deployment of Workers via our <a href="/fundamentals/api/reference/sdks/">Cloudflare SDKs</a>. This update abstracts away the low-level complexities of the <code>multipart/form-data</code> upload process, allowing you to focus on your code while we handle the deployment mechanics.</p>
<p>This new interface is available in:</p>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (4.4.1)</li>
<li><a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (4.3.1)</li>
</ul>
<p>For complete examples, see our guide on <a href="/workers/platform/infrastructure-as-code">programmatic Worker deployments</a>.</p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-the-old-way-manual-api-calls">The Old way: Manual API calls</h4>
<p>Previously, deploying a Worker programmatically required manually constructing a <code>multipart/form-data</code> HTTP request, packaging your code and a separate <code>metadata.json</code> file. This was more complicated and verbose, and prone to formatting errors.</p>
<p>For example, here's how you would upload a Worker script previously with cURL:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/workers/scripts/my-hello-world-script \&#10;  &#45;X PUT \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;F &#x27;metadata={&#10;        &quot;main_module&quot;: &quot;my-hello-world-script.mjs&quot;,&#10;        &quot;bindings&quot;: [&#10;          {&#10;            &quot;type&quot;: &quot;plain_text&quot;,&#10;            &quot;name&quot;: &quot;MESSAGE&quot;,&#10;            &quot;text&quot;: &quot;Hello World!&quot;&#10;          }&#10;        ],&#10;        &quot;compatibility_date&quot;: &quot;$today&quot;&#10;      };type=application/json&#x27; \&#10;  &#45;F &#x27;my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module&#x27; &lt;&lt;EOF&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(env.MESSAGE, { status: 200 });&#10;  }&#10;};&#10;EOF&#10;</code></pre>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-after-sdk-interface">After: SDK interface</h4>
<p>With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.</p>
<p>This approach allows you to specify metadata like <code>main_module</code>, <code>bindings</code>, and <code>compatibility_date</code> as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.</p>
<p>Here's how you can now programmatically deploy a Worker via the <a href="https://github.com/cloudflare/cloudflare-typescript"><code>cloudflare-typescript</code> SDK</a></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17777.md")</div>
<p>View the complete example here: <a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts">https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts</a></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-terraform-provider-improvements">Terraform provider improvements</h4>
<p>We've also made several fixes and enhancements to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform provider</a>:</p>
<ul>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource in Terraform, which previously was producing a diff even when there were no changes. Now, your <code>terraform plan</code> outputs will be cleaner and more reliable.</li>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace"><code>cloudflare_workers_for_platforms_dispatch_namespace</code></a>, where the provider would attempt to recreate the namespace on a <code>terraform apply</code>. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.</li>
<li>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route"><code>cloudflare_workers_route</code></a> resource now allows for the <code>script</code> property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes <a href="/workers/configuration/routing/routes">docs</a>). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.</li>
<li>Using <code>primary_location_hint</code> in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database"><code>cloudflare_d1_database</code></a> resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.</li>
</ul>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-api-improvements">API improvements</h4>
<p>We've also properly documented the <a href="/api/resources/workers/subresources/scripts/subresources/script_and_version_settings">Workers Script And Version Settings</a> in our public OpenAPI spec and SDKs.</p>


<h2 id="remote-bindings-public-beta-connect-to-remote-resources-d1-kv-r2-etc-during-local-development"><a href="/changelog/post/2025-06-18-remote-bindings-beta/">Remote bindings public beta - Connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<p><em>2025-06-18</em></p>
<p>Today <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">we announced the public beta</a> of <a href="/workers/local-development/#remote-bindings">remote bindings</a> for local development. With remote bindings, you can now connect to deployed resources like <a href="/r2/">R2 buckets</a> and <a href="/d1/">D1 databases</a> while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.</p>
<h4 id="2025-06-18-remote-bindings-beta-example-configuration">Example configuration</h4>
<p>To enable remote mode, add <code>&quot;experimental_remote&quot; : true</code> to each binding that you want to rely on a remote resource running on Cloudflare:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17778.md")</div>
<p>When remote bindings are configured, your Worker <strong>still executes locally</strong>, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.</p>
<p><strong>You can try out remote bindings for local development today with:</strong></p>
<ul>
<li><a href="/workers/local-development/#remote-bindings">Wrangler v4.20.3</a>: Use the <code>wrangler dev --x-remote-bindings</code> command.</li>
<li>The <a href="/workers/local-development/#remote-bindings">Cloudflare Vite Plugin</a>: Refer to the documentation for how to enable in your Vite config.</li>
<li>The <a href="/workers/local-development/#remote-bindings">Cloudflare Vitest Plugin</a>: Refer to the documentation for how to enable in your Vitest config.</li>
</ul>
<p><strong>Have feedback?</strong>
Join the discussion in our <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">beta announcement</a> to share feedback or report any issues.</p>


<h2 id="terraform-v5-6-0-now-available"><a href="/changelog/post/2025-06-17-terraform-v5.6.0-provider/">Terraform v5.6.0 now available</a></h2>
<p><em>2025-06-17</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>.
Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since
launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a>
reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address
these issues across the company, and have released the v5.6.0 release which includes a number of bug fixes. Please keep an
eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-changes">Changes</h4>
<ul>
<li>Broad fixes across resources with recurring diffs, including, but not limited to:
<ul>
<li><code>cloudflare_zero_trust_access_identity_provider</code>
<ul>
<li><code>cloudflare_zone</code></li>
</ul>
</li>
</ul>
</li>
<li><code>cloudflare_page_rules</code> runtime panic when setting <code>cache_level</code> to <code>cache_ttl_by_status</code></li>
<li>Failure to serialize requests in <code>cloudflare_zero_trust_tunnel_cloudflared_config</code></li>
<li>Undocumented field 'priority' on <code>zone_lockdown</code> resource</li>
<li>Missing importability for <code>cloudflare_zero_trust_device_default_profile_local_domain_fallback</code> and <code>cloudflare_account_subscription</code></li>
<li>New resources:
<ul>
<li><code>cloudflare_schema_validation_operation_settings</code></li>
<li><code>cloudflare_schema_validation_schemas</code></li>
<li><code>cloudflare_schema_validation_settings</code></li>
<li><code>cloudflare_zero_trust_device_settings</code></li>
</ul>
</li>
<li>Other bug fixes</li>
</ul>
<p>For a more detailed look at all of the changes, see the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.6.0">changelog</a> in GitHub.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-issues-closed">Issues Closed</h4>
- [#5098: 500 Server Error on updating 'zero_trust_tunnel_cloudflared_virtual_network' Terraform resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5098)
- [#5148: cloudflare_user_agent_blocking_rule doesn’t actually support user agents](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5148)
- [#5472: cloudflare_zone showing changes in plan after following upgrade steps](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5472)
- [#5508: cloudflare_zero_trust_tunnel_cloudflared_config failed to serialize http request](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5508)
- [#5509: cloudflare_zone: Problematic Terraform behaviour with paused zones](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5509)
- [#5520: Resource 'cloudflare_magic_wan_static_route' is not working](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5520)
- [#5524: Optional fields cause crash in cloudflare_zero_trust_tunnel_cloudflared(s) when left null](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5524)
- [#5526: Provider v5 migration issue: no import method for cloudflare_zero_trust_device_default_profile_local_domain_fallback](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5526)
- [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5561: cloudflare_zero_trust_tunnel_cloudflared: cannot rotate tunnel secret](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5561)
- [#5569: cloudflare_zero_trust_device_custom_profile_local_domain_fallback not allowing multiple DNS Server entries](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5569)
- [#5577: Panic modifying page_rule resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5577)
- [#5653: cloudflare_zone_setting resource schema confusion in 5.5.0: value vs enabled](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5653)
<p>If you have an unaddressed issue with the provider, we encourage you to check the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already
exist for what you are experiencing.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the
<a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have
provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which
use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our
<a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="control-which-routes-invoke-your-worker-script-for-single-page-applications"><a href="/changelog/post/2025-06-17-advanced-routing/">Control which routes invoke your Worker script for Single Page Applications</a></h2>
<p><em>2025-06-17</em></p>
<p>For those building <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control">Single Page Applications (SPAs) on Workers</a>, you can now explicitly define which routes invoke your Worker script in Wrangler configuration. The <a href="/workers/static-assets/binding/#run_worker_first"><code>run_worker_first</code> config option</a> has now been expanded to accept an array of route patterns, allowing you to more granularly specify when your Worker script runs.</p>
<p><strong>Configuration example:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17776.md")</div>
<p>This new routing control was done in partnership with our community and customers who provided great feedback on <a href="https://github.com/cloudflare/workers-sdk/discussions/9143">our public proposal</a>. Thank you to everyone who brought forward use-cases and feedback on the design!</p>
<h4 id="2025-06-17-advanced-routing-prerequisites">Prerequisites</h4>
<p>To use advanced routing control with <code>run_worker_first</code>, you'll need:</p>
<ul>
<li><a href="/workers/wrangler/install-and-update/">Wrangler</a> v4.20.0 and above</li>
<li><a href="/workers/vite-plugin/get-started/">Cloudflare Vite plugin</a> v1.7.0 and above</li>
</ul>


<h2 id="ssrf-vulnerability-in-opennextjs-cloudflare-proactively-mitigated-for-all-cloudflare-customers"><a href="/changelog/post/2025-06-17-open-next-ssrf/">SSRF vulnerability in @opennextjs/cloudflare proactively mitigated for all Cloudflare customers</a></h2>
<p><em>2025-06-17</em></p>
<p>Mitigations have been put in place for all existing and future deployments of sites with the Cloudflare adapter for Open Next in response to an identified Server-Side Request Forgery (SSRF) vulnerability in the <code>@opennextjs/cloudflare</code> package.</p>
<p>The vulnerability stemmed from an unimplemented feature in the Cloudflare adapter for Open Next, which allowed users to proxy arbitrary remote content via the <code>/_next/image</code> endpoint.</p>
<p>This issue allowed attackers to load remote resources from arbitrary hosts under the victim site's domain for any site deployed using the Cloudflare adapter for Open Next. For example: <code>https://victim-site.com/_next/image?url=https://attacker.com</code>. In this example, attacker-controlled content from <code>attacker.com</code> is served through the victim site's domain (<code>victim-site.com</code>), violating the same-origin policy and potentially misleading users or other services.</p>
<p>References: <a href="https://www.cve.org/cverecord?id=CVE-2025-6087">https://www.cve.org/cverecord?id=CVE-2025-6087</a>, <a href="https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m">https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m</a></p>
<h4 id="2025-06-17-open-next-ssrf-impact">Impact</h4>
<ul>
<li>SSRF via unrestricted remote URL loading</li>
<li>Arbitrary remote content loading</li>
<li>Potential internal service exposure or phishing risks through domain abuse</li>
</ul>
<h4 id="2025-06-17-open-next-ssrf-mitigation">Mitigation</h4>
<p>The following mitigations have been put in place:</p>
<p><strong>Server side updates</strong> to Cloudflare's platform to restrict the content loaded via the <code>/_next/image</code> endpoint to images. The update automatically mitigates the issue for all existing and any future sites deployed to Cloudflare using the affected version of the Cloudflare adapter for Open Next</p>
<p><strong>Root cause fix:</strong> Pull request <a href="https://github.com/opennextjs/opennextjs-cloudflare/pull/727">#727</a> to the Cloudflare adapter for Open Next. The patched version of the adapter has been released as <code>@opennextjs/cloudflare@1.3.0</code></p>
<p><strong>Package dependency update:</strong> Pull request <a href="https://github.com/cloudflare/workers-sdk/pull/9608">cloudflare/workers-sdk#9608</a> to create-cloudflare (c3) to use the fixed version of the Cloudflare adapter for Open Next. The patched version of create-cloudflare has been published as <code>create-cloudflare@2.49.3</code>.</p>
<p>In addition to the automatic mitigation deployed on Cloudflare's platform, we encourage affected users to upgrade to <code>@opennext/cloudflare</code> v1.3.0 and use the <a href="https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns"><code>remotePatterns</code></a> filter in Next config if they need to allow-list external urls with images assets.</p>


<h2 id="grant-account-members-read-only-access-to-the-workers-platform"><a href="/changelog/post/2025-06-16-workers-platform-admin-role/">Grant account members read-only access to the Workers Platform</a></h2>
<p><em>2025-06-16</em></p>
<p>You can now grant members of your Cloudflare account read-only access to the Workers
Platform.</p>
<p>The new &quot;Workers Platform (Read-only)&quot; role grants read-only access to all products typically used as part of Cloudflare's Developer Platform, including <a href="/workers/">Workers</a>, <a href="/pages/">Pages</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, Zones, <a href="/analytics/account-and-zone-analytics/zone-analytics/">Zone Analytics</a> and <a href="/rules/">Page Rules</a>. When Cloudflare introduces new products to the Workers platform, we will add additional read-only permissions to this role.</p>
<p>Additionally, the role previously named &quot;Workers Admin&quot; has been renamed to &quot;Workers Platform Admin&quot;. This
change ensures that the name more accurately reflects the permissions granted — this
role has always granted access to more than just
Workers — it grants read and write access to the products mentioned above, and similarly, as new products are added to the Workers platform, we will add additional read and write permissions to this role.</p>
<p>You can review the updated roles in the <a href="/fundamentals/manage-members/roles/">developer docs</a>.</p>


<h2 id="increased-limits-for-media-transformations"><a href="/changelog/post/2025-06-10-media-transformations-limits-increase/">Increased limits for Media Transformations</a></h2>
<p><em>2025-06-10</em></p>
<p>We have increased the limits for <a href="/stream/transform-videos/">Media Transformations</a>:</p>
<ul>
<li>Input file size limit is now 100MB (was 40MB)</li>
<li>Output video duration limit is now 1 minute (was 30 seconds)</li>
</ul>
<p>Additionally, we have improved caching of the input asset, resulting in fewer
requests to origin storage even when transformation options may differ.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<h2 id="access-git-commit-sha-and-branch-name-as-environment-variables-in-workers-builds"><a href="/changelog/post/2025-06-10-default-env-vars/">Access git commit sha and branch name as environment variables in Workers Builds</a></h2>
<p><em>2025-06-10</em></p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> connects your Worker to a <a href="/workers/ci-cd/builds/git-integration/">Git repository</a>, and automates building and deploying your code on each pushed change.</p>
<p>To make CI/CD pipelines even more flexible, Workers Builds now automatically injects <a href="/workers/ci-cd/builds/configuration/#environment-variables">default environment variables</a> into your build process (much like the defaults in <a href="/pages/configuration/build-configuration/#environment-variables">Cloudflare Pages projects</a>). You can use these variables to customize your build process based on the deployment context, such as the branch or commit.</p>
<p>The following environment variables are injected by default:</p>
<table>
<thead>
<tr>
<th>Environment Variable</th>
<th>Injected value</th>
<th>Example use-case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CI</code></td>
<td><code>true</code></td>
<td>Changing build behavior when run on CI versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI</code></td>
<td><code>1</code></td>
<td>Changing build behavior when run on Workers Builds versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI_BUILD_UUID</code></td>
<td><code>&lt;build-uuid-of-current-build&gt;</code></td>
<td>Passing the Build UUID along to custom workflows</td>
</tr>
<tr>
<td><code>WORKERS_CI_COMMIT_SHA</code></td>
<td><code>&lt;sha1-hash-of-current-commit&gt;</code></td>
<td>Passing current commit ID to error reporting, for example, Sentry</td>
</tr>
<tr>
<td><code>WORKERS_CI_BRANCH</code></td>
<td><code>&lt;branch-name-from-push-event</code></td>
<td>Customizing build based on branch, for example, disabling debug logging on <code>production</code></td>
</tr>
</tbody>
</table>
<p>You can override these default values and add your own custom environment variables by navigating to <strong>your Worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment variables</strong>.</p>
<p>Learn more in the <a href="/workers/ci-cd/builds/configuration/#environment-variables">Build configuration documentation</a>.</p>


<h2 id="workers-native-integrations-were-removed-from-the-cloudflare-dashboard"><a href="/changelog/post/2025-06-09-workers-integrations-changes/">Workers native integrations were removed from the Cloudflare dashboard</a></h2>
<p><em>2025-06-09</em></p>
<p>Workers native integrations were <a href="https://blog.cloudflare.com/announcing-database-integrations/">originally launched in May 2023</a> to connect to popular database and observability providers with your Worker in just a few clicks. We are changing how developers connect Workers to these external services. The <strong>Integrations</strong> tab in the dashboard has been removed in favor of a more direct, command-line-based approach using <a href="/workers/wrangler/commands/general/#secret">Wrangler secrets</a>.</p>
<h4 id="2025-06-09-workers-integrations-changes-what-s-changed">What's changed</h4>
<ul>
<li><strong>Integrations tab removed</strong>: The integrations setup flow is no longer available in the Workers dashboard.</li>
<li><strong>Manual secret configuration</strong>: New connections should be configured by adding credentials as secrets to your Workers using <code>npx wrangler secret put</code> commands.</li>
</ul>
<h4 id="2025-06-09-workers-integrations-changes-impact-on-existing-integrations">Impact on existing integrations</h4>
<p><strong>Existing integrations will continue to work without any changes required.</strong> If you have integrations that were previously created through the dashboard, they will remain functional.</p>
<h4 id="2025-06-09-workers-integrations-changes-updating-existing-integrations">Updating existing integrations</h4>
<p>If you'd like to modify your existing integration, you can update the secrets, environment variables, or <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> that were created from the original integration setup.</p>
<ul>
<li><strong>Update secrets</strong>: Use <code>npx wrangler secret put &lt;SECRET_NAME&gt;</code> to update credential values.</li>
<li><strong>Modify environment variables</strong>: Update variables through the dashboard or Wrangler configuration.</li>
<li><strong>Dashboard management</strong>: Access your Worker's settings in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> to modify connections created by our removed native integrations feature.</li>
</ul>
<p>If you have previously set up an observability integration with <a href="https://sentry.io">Sentry</a>, the following environment variables were set and are still modifiable:</p>
<ul>
<li><code>BLOCKED_HEADERS</code>: headers to exclude sending to Sentry</li>
<li><code>EXCEPTION_SAMPLING_RATE</code>: number from 0 - 100, where 0 = no events go through to Sentry, and 100 = all events go through to Sentry</li>
<li><code>STATUS_CODES_TO_SAMPLING_RATES</code>: a map of status codes -- like 400 or with wildcards like 4xx -- to sampling rates described above</li>
</ul>
<h4 id="2025-06-09-workers-integrations-changes-setting-up-new-database-and-observability-connections">Setting up new database and observability connections</h4>
<p>For new connections, refer to our step-by-step guides on connecting to popular database and observability providers including: <a href="/workers/observability/third-party-integrations/sentry">Sentry</a>, <a href="/workers/databases/third-party-integrations/turso/">Turso</a>, <a href="/workers/databases/third-party-integrations/neon/">Neon</a>, <a href="/workers/databases/third-party-integrations/supabase/">Supabase</a>, <a href="/workers/databases/third-party-integrations/planetscale/">PlanetScale</a>, <a href="/workers/databases/third-party-integrations/upstash/">Upstash</a>, <a href="/workers/databases/third-party-integrations/xata/">Xata</a>.</p>


<h2 id="performance-and-size-optimization-for-the-cloudflare-adapter-for-open-next"><a href="/changelog/post/2025-06-05-open-next-size/">Performance and size optimization for the Cloudflare adapter for Open Next</a></h2>
<p><em>2025-06-05T19:00:00+00:00</em></p>
<p>With the release of the Cloudflare adapter for Open Next v1.0.0 in May 2025, we already had followups plans <a href="https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/#1-0-and-the-road-ahead">to improve performance and size</a>.</p>
<p><code>@opennextjs/cloudflare</code> v1.2 released on June 5, 2025 delivers on these enhancements. By removing <code>babel</code> from the app code and dropping a dependency on <code>@ampproject/toolbox-optimizer</code>, we were able to reduce generated bundle sizes. Additionally, by stopping preloading of all app routes, we were able to improve the cold start time.</p>
<p>This means that users will now see a decrease from 14 to 8MiB (2.3 to 1.6MiB gzipped) in generated bundle size for a Next app created via create-next-app, and typically 100ms faster startup times for their medium-sized apps.</p>
<p>Users only need to update to the latest version of <code>@opennextjs/cloudflare</code> to automatically benefit from these improvements.</p>
<p>Note that we published <a href="https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m">CVE-2005-6087</a> for a SSRF vulnerability in the <code>@opennextjs/cloudflare</code> package.
The vulnerability has been fixed from <code>@opennextjs/cloudflare</code> v1.3.0 onwards. Please update to any version after this one.</p>


<h2 id="ai-gateway-adds-openai-compatible-endpoint"><a href="/changelog/post/2025-06-03-aig-openai-compatible-endpoint/">AI Gateway adds OpenAI compatible endpoint</a></h2>
<p><em>2025-06-03</em></p>
<p>Users can now use an <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> in AI Gateway to easily switch between providers, while keeping the exact same request and response formats. We're launching now with the chat completions endpoint, with the embeddings endpoint coming up next.</p>
<p>To get started, use the OpenAI compatible chat completions endpoint URL with your own account id and gateway id and switch between providers by changing the <code>model</code> and <code>apiKey</code> parameters.</p>
<pre tabindex="0"><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;const client = new OpenAI({&#10;	apiKey: &quot;YOUR_PROVIDER_API_KEY&quot;, // Provider API key&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat&quot;,&#10;});&#10;&#10;const response = await client.chat.completions.create({&#10;	model: &quot;google-ai-studio/gemini-2.0-flash&quot;,&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;&#10;console.log(response.choices[0].message.content);&#10;</code></pre>
<p>Additionally, the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> can be combined with our <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> to add fallbacks across multiple providers. That means AI Gateway will return every response in the same standardized format, no extra parsing logic required!</p>
<p>Learn more in the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatibility</a> documentation.</p>


<h2 id="view-an-architecture-diagram-of-your-worker-directly-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-06-03-visualize-your-worker-architecture/">View an architecture diagram of your Worker directly in the Cloudflare dashboard</a></h2>
<p><em>2025-06-03</em></p>
<p>You can now visualize, explore and modify your Worker’s architecture directly in the Cloudflare dashboard, making it easier to understand how your application connects to Cloudflare resources like <a href="/d1">D1 databases</a>, <a href="/durable-objects">Durable Objects</a>, <a href="/kv">KV namespaces</a>, and <a href="/workers/runtime-apis/bindings/">more</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/bindings-canvas.png" alt="Bindings canvas" /></p>
<p>With this new view, you can easily:</p>
<ul>
<li>Explore existing bindings in a visual, architecture-style diagram</li>
<li>Add and manage bindings directly from the same interface</li>
<li>Discover the full range of compute, storage, AI, and media resources you can attach to your Workers application.</li>
</ul>
<p>To get started, head to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages">Cloudflare dashboard</a> and open the <strong>Bindings</strong> tab of any Workers application.</p>


<h2 id="cloudflare-pages-builds-now-provide-node-js-v22-by-default"><a href="/changelog/post/2025-05-30-pages-build-image-v3/">Cloudflare Pages builds now provide Node.js v22 by default</a></h2>
<p><em>2025-05-30T00:00:00+00:00</em></p>
<p>When you use the built-in build system that is part of <a href="/pages/">Cloudflare Pages</a>, the <a href="/pages/configuration/build-image/">Build Image</a> now includes Node.js v22. Previously, Node.js v18 was provided by default, and Node.js v18 is now end-of-life (EOL).</p>
<p>If you are creating a new Pages project, the new V3 build image that includes Node.js v22 will be used by default. If you have an existing Pages project, you can update to the latest build image by navigating to Settings &gt; Build &amp; deployments &gt; Build system version in the Cloudflare dashboard for a specific Pages project.</p>
<p>Note that you can always specify a particular version of Node.js or other built-in dependencies by <a href="/pages/configuration/build-image/#override-default-versions">setting an environment variable</a>.</p>
<p>For more, refer to the <a href="/pages/configuration/build-image">developer docs for Cloudflare Pages builds</a></p>


<h2 id="debug-profile-and-view-logs-for-your-worker-in-chrome-devtools-now-supported-in-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-05-21-vite-plugin-chrome-devtools/">Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin</a></h2>
<p><em>2025-05-30</em></p>
<p>You can now <a href="https://developers.cloudflare.com/workers/observability/dev-tools/">debug, profile, view logs, and analyze memory usage for your Worker</a> using <a href="https://developer.chrome.com/docs/devtools">Chrome Devtools</a> when your Worker runs locally using the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p>Previously, this was only possible if your Worker ran locally using the <a href="https://developers.cloudflare.com/workers/wrangler/">Wrangler CLI</a>, and now you can do all the same things if your Worker uses <a href="https://vite.dev/">Vite</a>.</p>
<p>When you run <code>vite</code>, you'll now see a debug URL in your console:</p>
<pre tabindex="0"><code>  VITE v6.3.5  ready in 461 ms&#10;&#10;  ➜  Local:   http://localhost:5173/&#10;  ➜  Network: use --host to expose&#10;  ➜  Debug:   http://localhost:5173/__debug&#10;  ➜  press h + enter to show help&#10;</code></pre>
<p>Open the URL in Chrome, and an instance of Chrome Devtools will open and connect to your Worker running locally. You can then use Chrome Devtools to debug and introspect performance issues. For example, you can navigate to the Performance tab to understand where CPU time is spent in your Worker:</p>
<p><img src="/assets/upstream/images/workers/observability/profile.png" alt="CPU Profile" /></p>
<p>For more information on how to get the most out of Chrome Devtools, refer to the following docs:</p>
<ul>
<li><a href="/workers/observability/dev-tools/breakpoints/">Debug code by setting breakpoints</a></li>
<li><a href="/workers/observability/dev-tools/cpu-usage/">Profile CPU usage</a></li>
<li><a href="/workers/observability/dev-tools/memory-usage/">Observe memory usage and debug memory leaks</a></li>
</ul>


<h2 id="50-500ms-faster-d1-rest-api-requests"><a href="/changelog/post/2025-05-30-d1-rest-api-latency/">50-500ms Faster D1 REST API Requests</a></h2>
<p><em>2025-05-29</em></p>
<p>Users using Cloudflare's <a href="/api/resources/d1/">REST API</a> to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.</p>
<p>Latency improvements range from 50-500 ms depending on request location and <a href="/d1/configuration/data-location/">database location</a> and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.</p>
<p>D1 query endpoints like <code>/query</code> and <code>/raw</code> have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.</p>


<h2 id="playwright-mcp-server-is-now-compatible-with-browser-rendering"><a href="/changelog/post/2025-05-28-playwright-mcp/">Playwright MCP server is now compatible with Browser Rendering</a></h2>
<p><em>2025-05-28</em></p>
<p>We're excited to share that you can now use the <a href="https://github.com/cloudflare/playwright-mcp">Playwright MCP</a> server with Browser Rendering.</p>
<p>Once you <a href="/browser-run/playwright/playwright-mcp/#deploying">deploy the server</a>, you can use any MCP client with it to interact with Browser Rendering. This allows you to run AI models that can automate browser tasks, such as taking screenshots, filling out forms, or scraping data.</p>
<p><img src="/assets/upstream/images/browser-run/playground-ai-screenshot.png" alt="Access Analytics" /></p>
<p>Playwright MCP is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright-mcp"><code>@cloudflare/playwright-mcp</code></a>. To install it, type:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Deploying the server is then as easy as:</p>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createMcpAgent } from &quot;@cloudflare/playwright-mcp&quot;;&#10;&#10;export const PlaywrightMCP = createMcpAgent(env.BROWSER);&#10;export default PlaywrightMCP.mount(&quot;/sse&quot;);&#10;</code></pre>
<p>Check out the full code at <a href="https://github.com/cloudflare/playwright-mcp">GitHub</a>.</p>
<p>Learn more about Playwright MCP in our <a href="/browser-run/playwright/playwright-mcp/">documentation</a>.</p>


<h2 id="increased-limits-for-cloudflare-for-saas-and-secrets-store-free-and-pay-as-you-go-plans"><a href="/changelog/post/2025-05-19-paygo-updates/">Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans</a></h2>
<p><em>2025-05-27T11:00:00+00:00</em></p>
<p>With upgraded limits to <a href="https://www.cloudflare.com/plans/">all free and paid plans</a>, you can now scale more easily with <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> and <a href="https://developers.cloudflare.com/secrets-store/">Secrets Store</a>.</p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/">limit for custom hostnames</a> on a Cloudflare for SaaS Pay-as-you-go plan has been <strong>raised from 5,000 custom hostnames to 50,000 custom hostnames.</strong></p>
<p>With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">Custom origin server</a> is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.</p>
<p>You can enable custom origin server on a per-custom hostname basis <a href="https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/">via the API</a> or the UI:</p>
<p><img src="/assets/upstream/images/ssl/custom-origin-server.png" alt="Import repo or choose template" /></p>
<p>Currently <a href="https://blog.cloudflare.com/secrets-store-beta/">in beta with a Workers integration</a>, <a href="https://developers.cloudflare.com/secrets-store/">Cloudflare Secrets Store</a> allows you to store, manage, and deploy account level secrets from a secure, centralized platform your <a href="https://developers.cloudflare.com/workers/">Cloudflare Workers</a>. Now, you can create and deploy <strong>100 secrets per account</strong>. Try it out <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a>, with <a href="https://developers.cloudflare.com/secrets-store/integrations/workers/">Wrangler</a>, or <a href="https://developers.cloudflare.com/api/resources/secrets_store/">via the API</a> today.</p>


<h2 id="handle-incoming-request-cancellation-in-workers-with-request-signal"><a href="/changelog/post/2025-05-22-handle-request-cancellation/">Handle incoming request cancellation in Workers with Request.signal</a></h2>
<p><em>2025-05-22</em></p>
<p>In Cloudflare Workers, you can now attach an event listener to <a href="/workers/runtime-apis/request/"><code>Request</code></a> objects, using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request/signal"><code>signal</code> property</a>. This allows you to perform tasks when the request to your Worker is canceled by the client. To use this feature, you must set the <a href="/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests"><code>enable_request_signal</code></a> compatibility flag.</p>
<p>You can use a listener to perform cleanup tasks or write to logs before your Worker's invocation ends. For example, if you run the Worker below, and then abort the request from the client, a log will be written:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17775.md")</div>
<p>For more information see the <a href="/workers/runtime-apis/request"><code>Request</code> documentation</a>.</p>


<h2 id="terraform-v5-5-0-now-available"><a href="/changelog/post/2025-05-19-terraform-v5.5.0-provider/">Terraform v5.5.0 now available</a></h2>
<p><em>2025-05-19</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-changes">Changes</h4>
<ul>
<li>Broad fixes across resources with recurring diffs, including, but not limited to:
<ul>
<li><code>cloudflare_zero_trust_gateway_policy</code></li>
<li><code>cloudflare_zero_trust_access_application</code></li>
<li><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li><code>cloudflare_zone_setting</code></li>
<li><code>cloudflare_ruleset</code></li>
<li><code>cloudflare_page_rule</code></li>
</ul>
</li>
<li>Zone settings can be re-applied without client errors</li>
<li>Page rules conversion errors are fixed</li>
<li>Failure to apply changes to <code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li>Other bug fixes</li>
</ul>
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.5.0">changelog</a> in GitHub.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-issues-closed">Issues Closed</h4>
- [#5304: Importing cloudflare_zero_trust_gateway_policy invalid attribute filter value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
- [#5303: cloudflare_page_rule import does not set values for all of the fields in terraform state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
- [#5178: cloudflare_page_rule Page rule creation with redirect fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
- [#5336: cloudflare_turnstile_wwidget not able to update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
- [#5418: cloudflare_cloud_connector_rules: Provider returned invalid result object after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
- [#5423: cloudflare_zone_setting: "Invalid value for zone setting always_use_https"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="durable-objects-are-now-supported-in-python-workers"><a href="/changelog/post/2025-05-14-python-worker-durable-object/">Durable Objects are now supported in Python Workers</a></h2>
<p><em>2025-05-16</em></p>
<p>You can now create <a href="/durable-objects/">Durable Objects</a> using
<a href="/workers/languages/python/">Python Workers</a>. A Durable Object is a special kind of
Cloudflare Worker which uniquely combines compute with storage, enabling stateful
long-running applications which run close to your users. For more info see
<a href="/durable-objects/concepts/what-are-durable-objects/">here</a>.</p>
<p>You can define a Durable Object in Python in a similar way to JavaScript:</p>
<pre tabindex="0"><code class="language-python">from workers import DurableObject, Response, WorkerEntrypoint&#10;&#10;from urllib.parse import urlparse&#10;&#10;class MyDurableObject(DurableObject):&#10;    def __init__(self, ctx, env):&#10;        self.ctx = ctx&#10;        self.env = env&#10;&#10;    def fetch(self, request):&#10;        result = self.ctx.storage.sql.exec(&quot;SELECT &#x27;Hello, World!&#x27; as greeting&quot;).one()&#10;        return Response(result.greeting)&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        url = urlparse(request.url)&#10;        id = env.MY_DURABLE_OBJECT.idFromName(url.path)&#10;        stub = env.MY_DURABLE_OBJECT.get(id)&#10;        greeting = await stub.fetch(request.url)&#10;        return greeting&#10;</code></pre>
<p>Define the Durable Object in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17773.md")</div>
<p>Then define the storage backend for your Durable Object:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17774.md")</div>
<p>Then test your new Durable Object locally by running <code>wrangler dev</code>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler dev&#10;</code></pre>
<p>Consult the <a href="/durable-objects/">Durable Objects documentation</a> for more details.</p>


<h2 id="hyperdrive-achieves-fedramp-moderate-impact-authorization"><a href="/changelog/post/2025-05-14-hyperdrive-fedramp/">Hyperdrive achieves FedRAMP Moderate-Impact Authorization</a></h2>
<p><em>2025-05-14</em></p>
<p>Hyperdrive has been approved for FedRAMP Authorization and is now available in the <a href="https://marketplace.fedramp.gov/products/FR2000863987">FedRAMP Marketplace</a>.</p>
<p>FedRAMP is a U.S. government program that provides standardized assessment and authorization for cloud products and services. As a result of this product update,
Hyperdrive has been approved as an authorized service to be used by U.S. federal agencies at the Moderate Impact level.</p>
<p>For detailed information regarding FedRAMP and its implications, please refer to the <a href="https://marketplace.fedramp.gov/products/FR2000863987">official FedRAMP documentation for Cloudflare</a>.</p>


<h2 id="introducing-origin-restrictions-for-media-transformations"><a href="/changelog/post/2025-05-14-media-transformations-origin-restrictions/">Introducing Origin Restrictions for Media Transformations</a></h2>
<p><em>2025-05-14</em></p>
<p>We are adding <a href="/stream/transform-videos/sources/">source origin restrictions</a> to
the Media Transformations beta. This allows customers to restrict what sources
can be used to fetch images and video for transformations. This feature is the
same as --- and uses the same settings as ---
<a href="/images/optimization/transformations/sources/">Image Transformations sources</a>.</p>
<p>When transformations is first enabled, the default setting only allows
transformations on images and media from the same website or domain being used to make
the transformation request. In other words, by default, requests to
<code>example.com/cdn-cgi/media</code> can only reference originals on <code>example.com</code>.</p>
<p><img src="/assets/upstream/images/images/allowed-origins.png" alt="Enable allowed origins from the Cloudflare dashboard" /></p>
<p>Adding access to other sources, or allowing any source,
<a href="/images/optimization/transformations/sources/">is easy to do</a>
in the <strong>Transformations</strong> tab under <strong>Stream</strong>. Click each domain enabled for
Transformations and set its sources list to match the needs of your content. The
user making this change will need permission to edit zone settings.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/18/">Previous</a><span>Page 19 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/20/">Next</a></nav>
