---
cp9:
  canonical: https://developers.cloudflare.com/changelog/41/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 41 | Cloudflare Docs
  head_html: <title>Changelog - page 41 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/41/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 41"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/41/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/41/#page","headline":"Changelog - page 41 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/41/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/41/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-06-17">Jun 17, 2025</time><div>
<h2 id="post-2025-06-17-terraform-v5.6.0-provider"><a href="/changelog/post/2025-06-17-terraform-v5.6.0-provider/">Terraform v5.6.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>.
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-17">Jun 17, 2025</time><div>
<h2 id="post-2025-06-17-advanced-routing"><a href="/changelog/post/2025-06-17-advanced-routing/">Control which routes invoke your Worker script for Single Page Applications</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>For those building <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control">Single Page Applications (SPAs) on Workers</a>, you can now explicitly define which routes invoke your Worker script in Wrangler configuration. The <a href="/workers/static-assets/binding/#run_worker_first"><code>run_worker_first</code> config option</a> has now been expanded to accept an array of route patterns, allowing you to more granularly specify when your Worker script runs.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-17">Jun 17, 2025</time><div>
<h2 id="post-2025-06-17-open-next-ssrf"><a href="/changelog/post/2025-06-17-open-next-ssrf/">SSRF vulnerability in @opennextjs/cloudflare proactively mitigated for all Cloudflare customers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Mitigations have been put in place for all existing and future deployments of sites with the Cloudflare adapter for Open Next in response to an identified Server-Side Request Forgery (SSRF) vulnerability in the <code>@opennextjs/cloudflare</code> package.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-16">Jun 16, 2025</time><div>
<h2 id="post-2025-06-16-internal-dns-beta-ui"><a href="/changelog/post/2025-06-16-internal-dns-beta-ui/">Internal DNS (beta) now manageable in the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Participating beta testers can now fully configure <a href="/dns/internal-dns/">Internal DNS</a> directly in the <a href="https://dash.cloudflare.com/?to=/:account/internal-dns">Cloudflare dashboard</a>.</p>
<h4 id="2025-06-16-internal-dns-beta-ui-internal-dns-enables-customers-to">Internal DNS enables customers to:</h4>
<ul>
<li>
<p>Map internal hostnames to private IPs for services, devices, and applications not exposed to the public Internet</p>
</li>
<li>
<p>Resolve internal DNS queries securely through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a></p>
</li>
<li>
<p>Use split-horizon DNS to return different responses based on network context</p>
</li>
<li>
<p>Consolidate internal and public DNS zones within a single management platform</p>
</li>
</ul>
<h4 id="2025-06-16-internal-dns-beta-ui-what-s-new-in-this-release">What’s new in this release:</h4>
<ul>
<li>Beta participants can now create and manage internal zones and views in the Cloudflare dashboard</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/internal-dns-beta-ui.png" alt="Internal DNS UI" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17716.md")</aside>
<p>To learn more and get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-16">Jun 16, 2025</time><div>
<h2 id="post-2025-06-16-waf-release"><a href="/changelog/post/2025-06-16-waf-release/">WAF Release - 2025-06-16</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup highlights multiple critical vulnerabilities across popular web frameworks, plugins, and enterprise platforms. The focus lies on remote code execution (RCE), server-side request forgery (SSRF), and insecure file upload vectors that enable full system compromise or data exfiltration.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Cisco IOS XE (CVE-2025-20188): Critical RCE vulnerability enabling unauthenticated attackers to execute arbitrary commands on network infrastructure devices, risking total router compromise.</li>
<li>Axios (CVE-2024-39338): SSRF flaw impacting server-side request control, allowing attackers to manipulate internal service requests when misconfigured with unsanitized user input.</li>
<li>vBulletin (CVE-2025-48827, CVE-2025-48828): Two high-impact RCE flaws enabling attackers to remotely execute PHP code, compromising forum installations and underlying web servers.</li>
<li>Invision Community (CVE-2025-47916): A critical RCE vulnerability allowing authenticated attackers to run arbitrary code in community platforms, threatening data and lateral movement risk.</li>
<li>CrushFTP (CVE-2025-32102, CVE-2025-32103): SSRF vulnerabilities in upload endpoint processing permit attackers to pivot internal network scans and abuse internal services.</li>
<li>Roundcube (CVE-2025-49113): RCE via email processing enables attackers to execute code upon viewing a crafted email — particularly dangerous for webmail deployments.</li>
<li>WooCommerce WordPress Plugin (CVE-2025-47577): Dangerous file upload vulnerability permits unauthenticated users to upload executable payloads, leading to full WordPress site takeover.</li>
<li>Cross-Site Scripting (XSS) Detection Improvements: Enhanced detection patterns.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities span core systems — from routers to e-commerce to email. RCE in Cisco IOS XE, Roundcube, and vBulletin poses full system compromise. SSRF in Axios and CrushFTP supports internal pivoting, while WooCommerce’s file upload bug opens doors to mass WordPress exploitation.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="233bcf0ce50f400989a7e44a35fefd53">35fefd53</code>
</td>
<td>100783</td>
<td>Cisco IOS XE - Remote Code Execution - CVE:CVE-2025-20188</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9284e3b1586341acb4591bfd8332af5d">8332af5d</code>
</td>
<td>100784</td>
<td>Axios - SSRF - CVE:CVE-2024-39338</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2672b175a25548aa8e0107b12e1648d2">2e1648d2</code>
</td>
<td>100785</td>
<td>
				vBulletin - Remote Code Execution - CVE:CVE-2025-48827,
				CVE:CVE-2025-48828
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b77a19fb053744b49eacdab00edcf1ef">0edcf1ef</code>
</td>
<td>100786</td>
<td>Invision Community - Remote Code Execution - CVE:CVE-2025-47916</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="aec2274743064523a9667248d6f5eb48">d6f5eb48</code>
</td>
<td>100791</td>
<td>CrushFTP - SSRF - CVE:CVE-2025-32102, CVE:CVE-2025-32103</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7b80e1f5575d4d99bb7d56ae30baa18a">30baa18a</code>
</td>
<td>100792</td>
<td>Roundcube - Remote Code Execution - CVE:CVE-2025-49113</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="52d76f9394494b0382c7cb00229ba236">229ba236</code>
</td>
<td>100793</td>
<td>XSS - Ontoggle</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d38e657bd43f4d809c28157dfa338296">fa338296</code>
</td>
<td>100794</td>
<td>
				WordPress WooCommerce Plugin - Dangerous File Upload -
				CVE:CVE-2025-47577
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-16">Jun 16, 2025</time><div>
<h2 id="post-2025-06-16-workers-platform-admin-role"><a href="/changelog/post/2025-06-16-workers-platform-admin-role/">Grant account members read-only access to the Workers Platform</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now grant members of your Cloudflare account read-only access to the Workers
Platform.</p>
<p>The new &quot;Workers Platform (Read-only)&quot; role grants read-only access to all products typically used as part of Cloudflare's Developer Platform, including <a href="/workers/">Workers</a>, <a href="/pages/">Pages</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, Zones, <a href="/analytics/account-and-zone-analytics/zone-analytics/">Zone Analytics</a> and <a href="/rules/">Page Rules</a>. When Cloudflare introduces new products to the Workers platform, we will add additional read-only permissions to this role.</p>
<p>Additionally, the role previously named &quot;Workers Admin&quot; has been renamed to &quot;Workers Platform Admin&quot;. This
change ensures that the name more accurately reflects the permissions granted — this
role has always granted access to more than just
Workers — it grants read and write access to the products mentioned above, and similarly, as new products are added to the Workers platform, we will add additional read and write permissions to this role.</p>
<p>You can review the updated roles in the <a href="/fundamentals/manage-members/roles/">developer docs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-11">Jun 11, 2025</time><div>
<h2 id="post-2025-06-11-nsec3-support"><a href="/changelog/post/2025-06-11-nsec3-support/">NSEC3 support for DNSSEC</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Enterprise customers can now select NSEC3 as method for proof of non-existence on their zones.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>NSEC3 support for live-signed zones</strong> – For both primary and secondary zones that are configured to be live-signed (also known as &quot;on-the-fly signing&quot;), NSEC3 can now be selected as proof of non-existence.</p>
</li>
<li>
<p><strong>NSEC3 support for pre-signed zones</strong> – Secondary zones that are transferred to Cloudflare in a <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec">pre-signed setup</a> now also support NSEC3 as proof of non-existence.</p>
</li>
</ul>
<p>For more information and how to enable NSEC3, refer to the <a href="/dns/dnssec/enable-nsec3/">NSEC3 documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-10">Jun 10, 2025</time><div>
<h2 id="post-2025-06-10-media-transformations-limits-increase"><a href="/changelog/post/2025-06-10-media-transformations-limits-increase/">Increased limits for Media Transformations</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>We have increased the limits for <a href="/stream/transform-videos/">Media Transformations</a>:</p>
<ul>
<li>Input file size limit is now 100MB (was 40MB)</li>
<li>Output video duration limit is now 1 minute (was 30 seconds)</li>
</ul>
<p>Additionally, we have improved caching of the input asset, resulting in fewer
requests to origin storage even when transformation options may differ.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-10">Jun 10, 2025</time><div>
<h2 id="post-2025-06-10-default-env-vars"><a href="/changelog/post/2025-06-10-default-env-vars/">Access git commit sha and branch name as environment variables in Workers Builds</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/ci-cd/builds/">Workers Builds</a> connects your Worker to a <a href="/workers/ci-cd/builds/git-integration/">Git repository</a>, and automates building and deploying your code on each pushed change.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-09">Jun 9, 2025</time><div>
<h2 id="post-2025-06-09-custom-errors-fetch-4xx-5xx-assets"><a href="/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/">More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p><a href="/rules/custom-errors/">Custom Errors</a> can now fetch and store <a href="/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard">assets</a> and <a href="/rules/custom-errors/#error-pages">error pages</a> from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.</li>
<li>These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.</li>
</ul>
<p>This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.</p>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-09">Jun 9, 2025</time><div>
<h2 id="post-2025-06-09-transform-rule-subrequest-matching"><a href="/changelog/post/2025-06-09-transform-rule-subrequest-matching/">Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>You can now use the <a href="/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/"><code>cf.worker.upstream_zone</code></a> field in <a href="/rules/transform/">Transform Rules</a> to control rule execution based on whether a request originates from <a href="/workers/">Workers</a>, including subrequests issued by Workers in other zones.</p>
<p><img src="/assets/upstream/images/changelog/rules/transform-rule-subrequest-matching.png" alt="Match Workers subrequests by upstream zone in Transform Rules" /></p>
<p><strong>What's new:</strong></p>
<ul>
<li><code>cf.worker.upstream_zone</code> is now supported in Transform Rules expressions.</li>
<li>Skip or apply logic conditionally when handling <a href="/workers/platform/limits/#subrequests">Workers subrequests</a>.</li>
</ul>
<p>For example, to add a header when the subrequest comes from another zone:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-06-09-transform-rule-subrequest-matching-example">Example</h3>
@markup("md", "content/.markup/bodies/17746.md")</div>
<p>This gives you more granular control in how you handle incoming requests for your zone.</p>
<p>Learn more in the <a href="/rules/transform/">Transform Rules</a> documentation and <a href="/ruleset-engine/rules-language/fields/reference/">Rules language fields</a> reference.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-09">Jun 9, 2025</time><div>
<h2 id="post-2025-06-09-waf-release"><a href="/changelog/post/2025-06-09-waf-release/">WAF Release - 2025-06-09</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s update spotlights four critical vulnerabilities across CMS platforms, VoIP systems, and enterprise applications. Several flaws enable remote code execution or privilege escalation, posing significant enterprise risks.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>WordPress OttoKit Plugin (CVE-2025-27007): Privilege escalation flaw allows unauthenticated attackers to create or elevate user accounts, compromising WordPress administrative control.</li>
<li>SAP NetWeaver (CVE-2025-42999): Remote Code Execution vulnerability enables attackers to execute arbitrary code on SAP NetWeaver systems, threatening core ERP and business operations.</li>
<li>Fortinet FortiVoice (CVE-2025-32756): Buffer error vulnerability may lead to memory corruption and potential code execution, directly impacting enterprise VoIP infrastructure.</li>
<li>Camaleon CMS (CVE-2024-46986): Remote Code Execution vulnerability allows attackers to gain full control over Camaleon CMS installations, exposing hosted content and underlying servers.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target widely deployed CMS, ERP, and VoIP systems. RCE flaws in SAP NetWeaver and Camaleon CMS allow full takeover of business-critical applications. Privilege escalation in OttoKit exposes WordPress environments to full administrative compromise. FortiVoice buffer handling issues risk destabilizing or fully compromising enterprise telephony systems.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4afd50a3ef1948bba87c4e620debd86e">0debd86e</code>
</td>
<td>100769</td>
<td>
				WordPress OttoKit Plugin - Privilege Escalation - CVE:CVE-2025-27007
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="24134c41c3e940daa973b4b95f57b448">5f57b448</code>
</td>
<td>100770</td>
<td>SAP NetWeaver - Remote Code Execution - CVE:CVE-2025-42999</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4f219ac0be3545a5be5f0bf34df8857a">4df8857a</code>
</td>
<td>100779</td>
<td>Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bc8dfbe8cbac4c039725ec743b840107">3b840107</code>
</td>
<td>100780</td>
<td>Camaleon CMS - Remote Code Execution - CVE:CVE-2024-46986</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-09">Jun 9, 2025</time><div>
<h2 id="post-2025-06-09-workers-integrations-changes"><a href="/changelog/post/2025-06-09-workers-integrations-changes/">Workers native integrations were removed from the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers native integrations were <a href="https://blog.cloudflare.com/announcing-database-integrations/">originally launched in May 2023</a> to connect to popular database and observability providers with your Worker in just a few clicks. We are changing how developers connect Workers to these external services. The <strong>Integrations</strong> tab in the dashboard has been removed in favor of a more direct, command-line-based approach using <a href="/workers/wrangler/commands/general/#secret">Wrangler secrets</a>.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-06">Jun 6, 2025</time><div>
<h2 id="post-2025-06-05-open-next-size"><a href="/changelog/post/2025-06-05-open-next-size/">Performance and size optimization for the Cloudflare adapter for Open Next</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>With the release of the Cloudflare adapter for Open Next v1.0.0 in May 2025, we already had followups plans <a href="https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/#1-0-and-the-road-ahead">to improve performance and size</a>.</p>
<p><code>@opennextjs/cloudflare</code> v1.2 released on June 5, 2025 delivers on these enhancements. By removing <code>babel</code> from the app code and dropping a dependency on <code>@ampproject/toolbox-optimizer</code>, we were able to reduce generated bundle sizes. Additionally, by stopping preloading of all app routes, we were able to improve the cold start time.</p>
<p>This means that users will now see a decrease from 14 to 8MiB (2.3 to 1.6MiB gzipped) in generated bundle size for a Next app created via create-next-app, and typically 100ms faster startup times for their medium-sized apps.</p>
<p>Users only need to update to the latest version of <code>@opennextjs/cloudflare</code> to automatically benefit from these improvements.</p>
<p>Note that we published <a href="https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m">CVE-2005-6087</a> for a SSRF vulnerability in the <code>@opennextjs/cloudflare</code> package.
The vulnerability has been fixed from <code>@opennextjs/cloudflare</code> v1.3.0 onwards. Please update to any version after this one.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-05">Jun 5, 2025</time><div>
<h2 id="post-dashboards-access-report"><a href="/changelog/post/dashboards-access-report/">Cloudflare One Analytics Dashboards and Exportable Access Report</a></h2>
<div class="changelog-badges"><span>access</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/Analytics Dashboards.png" alt="Cloudflare One Analytics Dashboards"></p>
<p>Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A <strong>preview</strong> of the report is shown below, with more to be found in the report:</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-report.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>Both features are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-04">Jun 4, 2025</time><div>
<h2 id="post-2025-06-04-account-load-balancing-ui"><a href="/changelog/post/2025-06-04-account-load-balancing-ui/">New Account-Level Load Balancing UI and Private Load Balancers</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>We've made two large changes to load balancing:</p>
<ul>
<li>Redesigned the user interface, now centralized at the <strong>account level</strong>.</li>
<li>Introduced <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.</li>
</ul>
<p>This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/account-load-balancing-ui.png" alt="Load Balancing UI" /></p>
<p><strong>Key Enhancements:</strong></p>
<ul>
<li>
<p><strong>Account-Level UI Consolidation:</strong></p>
<ul>
<li>
<p><strong>Unified Management:</strong> Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.</p>
</li>
<li>
<p><strong>Improved Efficiency:</strong> This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.</p>
</li>
</ul>
</li>
<li>
<p><strong>Private Network Load Balancing:</strong></p>
<ul>
<li>
<p><strong>Secure Internal Application Access:</strong> Create <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.</p>
</li>
<li>
<p><strong>WARP &amp; Magic WAN Integration:</strong> Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.</p>
</li>
<li>
<p><strong>Enhanced Security for Internal Resources:</strong> Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.</p>
</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/load-balancing/private-load-balancer.png" alt="Private Load Balancers" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-03">Jun 3, 2025</time><div>
<h2 id="post-2025-06-03-aig-openai-compatible-endpoint"><a href="/changelog/post/2025-06-03-aig-openai-compatible-endpoint/">AI Gateway adds OpenAI compatible endpoint</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>Users can now use an <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> in AI Gateway to easily switch between providers, while keeping the exact same request and response formats. We're launching now with the chat completions endpoint, with the embeddings endpoint coming up next.</p>
<p>To get started, use the OpenAI compatible chat completions endpoint URL with your own account id and gateway id and switch between providers by changing the <code>model</code> and <code>apiKey</code> parameters.</p>
<pre tabindex="0"><code class="language-js">import OpenAI from &quot;openai&quot;;&#10;const client = new OpenAI({&#10;	apiKey: &quot;YOUR_PROVIDER_API_KEY&quot;, // Provider API key&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat&quot;,&#10;});&#10;&#10;const response = await client.chat.completions.create({&#10;	model: &quot;google-ai-studio/gemini-2.0-flash&quot;,&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;});&#10;&#10;console.log(response.choices[0].message.content);&#10;</code></pre>
<p>Additionally, the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatible endpoint</a> can be combined with our <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> to add fallbacks across multiple providers. That means AI Gateway will return every response in the same standardized format, no extra parsing logic required!</p>
<p>Learn more in the <a href="/ai-gateway/usage/chat-completion/">OpenAI Compatibility</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-03">Jun 3, 2025</time><div>
<h2 id="post-2025-06-03-shopify-o2o-improvements"><a href="/changelog/post/2025-06-03-shopify-o2o-improvements/">Improved onboarding for Shopify merchants</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Shopify merchants can now onboard to <strong>O2O</strong> automatically, without needing to contact support or community members.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>Automatic enablement</strong> – O2O is available for all mutual Cloudflare and Shopify customers.</p>
</li>
<li>
<p><strong>Branded record display</strong> – Merchants see a Shopify logo in DNS records, complete with helpful tooltips.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/shop-dns-icon-o2o.png" alt="Shopify O2O logo" /></p>
<ul>
<li><strong>Checkout protection</strong> – Workers and Snippets are blocked from running on the checkout path to reduce risk and improve security.</li>
</ul>
<p>For more information, refer to the <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/shopify/">provider guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-03">Jun 3, 2025</time><div>
<h2 id="post-2025-06-03-visualize-your-worker-architecture"><a href="/changelog/post/2025-06-03-visualize-your-worker-architecture/">View an architecture diagram of your Worker directly in the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now visualize, explore and modify your Worker’s architecture directly in the Cloudflare dashboard, making it easier to understand how your application connects to Cloudflare resources like <a href="/d1">D1 databases</a>, <a href="/durable-objects">Durable Objects</a>, <a href="/kv">KV namespaces</a>, and <a href="/workers/runtime-apis/bindings/">more</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/bindings-canvas.png" alt="Bindings canvas" /></p>
<p>With this new view, you can easily:</p>
<ul>
<li>Explore existing bindings in a visual, architecture-style diagram</li>
<li>Add and manage bindings directly from the same interface</li>
<li>Discover the full range of compute, storage, AI, and media resources you can attach to your Workers application.</li>
</ul>
<p>To get started, head to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages">Cloudflare dashboard</a> and open the <strong>Bindings</strong> tab of any Workers application.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-02">Jun 2, 2025</time><div>
<h2 id="post-2025-06-02-user-groups-beta"><a href="/changelog/post/2025-06-02-user-groups-beta/">Cloudflare User Groups &amp; Enhanced Permission Policies are now in Beta</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>We're excited to announce the Public Beta launch of <strong>User Groups for Cloudflare Dashboard</strong> and <strong>System for Cross Domain Identity Management (SCIM) User Groups</strong>, expanding our RBAC capabilities to simplify user and group management at scale.</p>
<p>We've also visually overhauled the <strong>Permission Policies UI</strong> to make defining permissions more intuitive.</p>
<p><strong>What's New</strong></p>
<p><strong>User Groups [BETA]</strong>: <a href="/fundamentals/manage-members/user-groups/">User Groups</a> are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.</p>
<p><strong>SCIM User Groups [BETA]</strong>: Centralize &amp; simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17726.md")</aside>
<p><strong>Revamped Permission Policies UI [BETA]</strong>: As Cloudflare's services have grown, so has the need for precise, role-based access control. We've given the Permission Policies builder a visual overhaul to make it much easier for administrators to find and define the exact permissions they want for specific principals.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-06-02-permissions-policy-ux.png" alt="Updated Permissions Policy UX" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17725.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/user-groups/">Get started with User Groups</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">Explore our SCIM integration guide</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-02">Jun 2, 2025</time><div>
<h2 id="post-2025-06-02-waf-release"><a href="/changelog/post/2025-06-02-waf-release/">WAF Release - 2025-06-02</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup highlights five high-risk vulnerabilities affecting SD-WAN, load balancers, and AI platforms. Several flaws enable unauthenticated remote code execution or authentication bypass.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Versa Concerto SD-WAN (CVE-2025-34026, CVE-2025-34027): Authentication bypass vulnerabilities allow attackers to gain unauthorized access to SD-WAN management interfaces, compromising network segmentation and control.</li>
<li>Kemp LoadMaster (CVE-2024-7591): Remote Code Execution vulnerability enables attackers to execute arbitrary commands, potentially leading to full device compromise within enterprise load balancing environments.</li>
<li>AnythingLLM (CVE-2024-0759): Server-Side Request Forgery (SSRF) flaw allows external attackers to force the LLM backend to make unauthorized internal network requests, potentially exposing sensitive internal resources.</li>
<li>Anyscale Ray (CVE-2023-48022): Remote Code Execution vulnerability affecting distributed AI workloads, allowing attackers to execute arbitrary code on Ray cluster nodes.</li>
<li>Server-Side Request Forgery (SSRF) - Generic &amp; Obfuscated Payloads: Ongoing advancements in SSRF payload techniques observed, including obfuscation and expanded targeting of cloud metadata services and internal IP ranges.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose critical infrastructure across networking, AI platforms, and SaaS integrations. Unauthenticated RCE and auth bypass flaws in Versa Concerto, Kemp LoadMaster, and Anyscale Ray allow full system compromise. AnythingLLM and SSRF payload variants expand attack surfaces into internal cloud resources, sensitive APIs, and metadata services, increasing risk of privilege escalation, data theft, and persistent access.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="752cfb5e6f9c46f0953c742139b52f02">39b52f02</code>
</td>
<td>100764</td>
<td>Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34027</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a01171de18034901b48a5549a34edb97">a34edb97</code>
</td>
<td>100765</td>
<td>Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34026</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="840b35492a7543c18ffe50fc0d99b2db">0d99b2db</code>
</td>
<td>100766</td>
<td>Kemp LoadMaster - Remote Code Execution - CVE:CVE-2024-7591</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="121b7070de3a459dbe80d7ed95aa3a4f">95aa3a4f</code>
</td>
<td>100767</td>
<td>AnythingLLM - SSRF - CVE:CVE-2024-0759</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="215417f989e2485a9c50eca0840a0966">840a0966</code>
</td>
<td>100768</td>
<td>Anyscale Ray - Remote Code Execution - CVE:CVE-2023-48022</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3ed619a17d4141bda3a8c3869d16ee18">9d16ee18</code>
</td>
<td>100781</td>
<td>SSRF - Generic Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7ce73f6a70be49f8944737465c963d9d">5c963d9d</code>
</td>
<td>100782</td>
<td>SSRF - Obfuscated Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-30">May 30, 2025</time><div>
<h2 id="post-2025-05-30-pages-build-image-v3"><a href="/changelog/post/2025-05-30-pages-build-image-v3/">Cloudflare Pages builds now provide Node.js v22 by default</a></h2>
<div class="changelog-badges"><span>pages</span></div><div class="changelog-body"><p>When you use the built-in build system that is part of <a href="/pages/">Cloudflare Pages</a>, the <a href="/pages/configuration/build-image/">Build Image</a> now includes Node.js v22. Previously, Node.js v18 was provided by default, and Node.js v18 is now end-of-life (EOL).</p>
<p>If you are creating a new Pages project, the new V3 build image that includes Node.js v22 will be used by default. If you have an existing Pages project, you can update to the latest build image by navigating to Settings &gt; Build &amp; deployments &gt; Build system version in the Cloudflare dashboard for a specific Pages project.</p>
<p>Note that you can always specify a particular version of Node.js or other built-in dependencies by <a href="/pages/configuration/build-image/#override-default-versions">setting an environment variable</a>.</p>
<p>For more, refer to the <a href="/pages/configuration/build-image">developer docs for Cloudflare Pages builds</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-30">May 30, 2025</time><div>
<h2 id="post-2025-05-30-configuration-rules-webp"><a href="/changelog/post/2025-05-30-configuration-rules-webp/">Fine-tune image optimization — WebP now supported in Configuration Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>You can now enable <a href="/images/polish/activate-polish/">Polish</a> with the <code>webp</code> format directly in <a href="/rules/configuration-rules/">Configuration Rules</a>, allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/images/polish/compression/#webp">WebP</a> is now a supported <a href="/rules/configuration-rules/settings/#polish">value</a> in the <strong>Polish</strong> setting for Configuration Rules.</li>
</ul>
<p>This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.</p>
<p>Learn more in the <a href="/images/polish/">Polish</a> and <a href="/rules/configuration-rules/">Configuration Rules</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-30">May 30, 2025</time><div>
<h2 id="post-2025-05-21-vite-plugin-chrome-devtools"><a href="/changelog/post/2025-05-21-vite-plugin-chrome-devtools/">Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now <a href="https://developers.cloudflare.com/workers/observability/dev-tools/">debug, profile, view logs, and analyze memory usage for your Worker</a> using <a href="https://developer.chrome.com/docs/devtools">Chrome Devtools</a> when your Worker runs locally using the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-05-29">May 29, 2025</time><div>
<h2 id="post-gateway-analytics-v2"><a href="/changelog/post/gateway-analytics-v2/">New Gateway Analytics in the Cloudflare One Dashboard</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Users can now access significant enhancements to Cloudflare Gateway analytics, providing you with unprecedented visibility into your organization's DNS queries, HTTP requests, and Network sessions. These powerful new dashboards enable you to go beyond raw logs and gain actionable insights into how your users are interacting with the Internet and your protected resources.</p>
<p>You can now visualize and explore:</p>
<ul>
<li>Patterns Over Time: Understand trends in traffic volume and blocked requests, helping you identify anomalies and plan for future capacity.</li>
<li>Top Users &amp; Destinations: Quickly pinpoint the most active users, enabling better policy enforcement and resource allocation.</li>
<li>Actions Taken: See a clear breakdown of security actions applied by Gateway policies, such as blocks and allows, offering a comprehensive view of your security posture.</li>
<li>Geographic Regions: Gain insight into the global distribution of your traffic.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-analytics.png" alt="Gateway Analytics" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and go to Analytics in the side navigation bar.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/40/">Previous</a><span>Page 41 of 50</span><a class="pagination-next" rel="next" href="/changelog/42/">Next</a></nav>
</div>
