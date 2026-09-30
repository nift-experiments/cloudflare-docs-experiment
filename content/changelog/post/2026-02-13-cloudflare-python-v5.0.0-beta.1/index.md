<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 13, 2026</time><h2 id="post-title">Cloudflare Python SDK v5.0.0-beta.1 now available</h2>
<div class="changelog-badges"><span>fundamentals</span><span>sdk</span></div><div class="changelog-body"><blockquote>
<p><strong>Disclaimer:</strong> Please note that v5.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0-beta.1">v4.3.1...v5.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions,
which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce
our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>There may be changes that are not captured in this changelog. Feel free to open an issue to report any inaccuracies, and we will make sure it gets into the changelog before the v5.0.0 release.</p>
<p>Most of the breaking changes below are caused by improvements to the accuracy of the base OpenAPI schemas, which
sometimes translates to breaking changes in downstream clients that depend on those schemas.</p>
<p>Please ensure you read through the list of changes below and the migration guide before moving to this version - this
will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="breaking-changes">Breaking Changes</h4>
<p><strong>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/v5-migration-guide.md">v5 Migration Guide</a> for detailed migration instructions.</strong></p>
<ul>
<li><code>abusereports</code></li>
<li><code>acm.totaltls</code></li>
<li><code>apigateway.configurations</code></li>
<li><code>cloudforceone.threatevents</code></li>
<li><code>d1.database</code></li>
<li><code>intel.indicatorfeeds</code></li>
<li><code>logpush.edge</code></li>
<li><code>origintlsclientauth.hostnames</code></li>
<li><code>queues.consumers</code></li>
<li><code>radar.bgp</code></li>
<li><code>rulesets.rules</code></li>
<li><code>schemavalidation.schemas</code></li>
<li><code>snippets</code></li>
<li><code>zerotrust.dlp</code></li>
<li><code>zerotrust.networks</code></li>
</ul>
<h4 id="features">Features</h4>
<h4 id="new-api-resources">New API Resources</h4>
<ul>
<li><code>abusereports</code> - Abuse report management</li>
<li><code>abusereports.mitigations</code> - Abuse report mitigation actions</li>
<li><code>ai.tomarkdown</code> - AI-powered markdown conversion</li>
<li><code>aigateway.dynamicrouting</code> - AI Gateway dynamic routing configuration</li>
<li><code>aigateway.providerconfigs</code> - AI Gateway provider configurations</li>
<li><code>aisearch</code> - AI-powered search functionality</li>
<li><code>aisearch.instances</code> - AI Search instance management</li>
<li><code>aisearch.tokens</code> - AI Search authentication tokens</li>
<li><code>alerting.silences</code> - Alert silence management</li>
<li><code>brandprotection.logomatches</code> - Brand protection logo match detection</li>
<li><code>brandprotection.logos</code> - Brand protection logo management</li>
<li><code>brandprotection.matches</code> - Brand protection match results</li>
<li><code>brandprotection.queries</code> - Brand protection query management</li>
<li><code>cloudforceone.binarystorage</code> - CloudForce One binary storage</li>
<li><code>connectivity.directory</code> - Connectivity directory services</li>
<li><code>d1.database</code> - D1 database management</li>
<li><code>diagnostics.endpointhealthchecks</code> - Endpoint health check diagnostics</li>
<li><code>fraud</code> - Fraud detection and prevention</li>
<li><code>iam.sso</code> - IAM Single Sign-On configuration</li>
<li><code>loadbalancers.monitorgroups</code> - Load balancer monitor groups</li>
<li><code>organizations</code> - Organization management</li>
<li><code>organizations.organizationprofile</code> - Organization profile settings</li>
<li><code>origintlsclientauth.hostnamecertificates</code> - Origin TLS client auth hostname certificates</li>
<li><code>origintlsclientauth.hostnames</code> - Origin TLS client auth hostnames</li>
<li><code>origintlsclientauth.zonecertificates</code> - Origin TLS client auth zone certificates</li>
<li><code>pipelines</code> - Data pipeline management</li>
<li><code>pipelines.sinks</code> - Pipeline sink configurations</li>
<li><code>pipelines.streams</code> - Pipeline stream configurations</li>
<li><code>queues.subscriptions</code> - Queue subscription management</li>
<li><code>r2datacatalog</code> - R2 Data Catalog integration</li>
<li><code>r2datacatalog.credentials</code> - R2 Data Catalog credentials</li>
<li><code>r2datacatalog.maintenanceconfigs</code> - R2 Data Catalog maintenance configurations</li>
<li><code>r2datacatalog.namespaces</code> - R2 Data Catalog namespaces</li>
<li><code>radar.bots</code> - Radar bot analytics</li>
<li><code>radar.ct</code> - Radar certificate transparency data</li>
<li><code>radar.geolocations</code> - Radar geolocation data</li>
<li><code>realtimekit.activesession</code> - Real-time Kit active session management</li>
<li><code>realtimekit.analytics</code> - Real-time Kit analytics</li>
<li><code>realtimekit.apps</code> - Real-time Kit application management</li>
<li><code>realtimekit.livestreams</code> - Real-time Kit live streaming</li>
<li><code>realtimekit.meetings</code> - Real-time Kit meeting management</li>
<li><code>realtimekit.presets</code> - Real-time Kit preset configurations</li>
<li><code>realtimekit.recordings</code> - Real-time Kit recording management</li>
<li><code>realtimekit.sessions</code> - Real-time Kit session management</li>
<li><code>realtimekit.webhooks</code> - Real-time Kit webhook configurations</li>
<li><code>tokenvalidation.configuration</code> - Token validation configuration</li>
<li><code>tokenvalidation.rules</code> - Token validation rules</li>
<li><code>workers.beta</code> - Workers beta features</li>
</ul>
<h4 id="new-endpoints-existing-resources">New Endpoints (Existing Resources)</h4>
<h4 id="acm-totaltls"><code>acm.totaltls</code></h4>
- `edit()`
- `update()`
<h4 id="cloudforceone-threatevents"><code>cloudforceone.threatevents</code></h4>
- `list()`
<h4 id="contentscanning"><code>contentscanning</code></h4>
- `create()`
- `get()`
- `update()`
<h4 id="dns-records"><code>dns.records</code></h4>
- `scan_list()`
- `scan_review()`
- `scan_trigger()`
<h4 id="intel-indicatorfeeds"><code>intel.indicatorfeeds</code></h4>
- `create()`
- `delete()`
- `list()`
<h4 id="leakedcredentialchecks-detections"><code>leakedcredentialchecks.detections</code></h4>
- `get()`
<h4 id="queues-consumers"><code>queues.consumers</code></h4>
- `list()`
<h4 id="radar-ai"><code>radar.ai</code></h4>
- `summary()`
- `timeseries()`
- `timeseries_groups()`
<h4 id="radar-bgp"><code>radar.bgp</code></h4>
- `changes()`
- `snapshot()`
<h4 id="workers-subdomains"><code>workers.subdomains</code></h4>
- `delete()`
<h4 id="zerotrust-networks"><code>zerotrust.networks</code></h4>
- `create()`
- `delete()`
- `edit()`
- `get()`
- `list()`
<h4 id="general-fixes-and-improvements">General Fixes and Improvements</h4>
<h4 id="type-system-compatibility">Type System &amp; Compatibility</h4>
<ul>
<li><strong>Type inference improvements</strong>: Allow Pyright to properly infer TypedDict types within SequenceNotStr</li>
<li><strong>Type completeness</strong>: Add missing types to method arguments and response models</li>
<li><strong>Pydantic compatibility</strong>: Ensure compatibility with Pydantic versions prior to 2.8.0 when using additional fields</li>
</ul>
<h4 id="request-response-handling">Request/Response Handling</h4>
<ul>
<li><strong>Multipart form data</strong>: Correctly handle sending multipart/form-data requests with JSON data</li>
<li><strong>Header handling</strong>: Do not send headers with default values set to omit</li>
<li><strong>GET request headers</strong>: Don't send Content-Type header on GET requests</li>
<li><strong>Response body model accuracy</strong>: Broad improvements to the correctness of models</li>
</ul>
<h4 id="parsing-data-processing">Parsing &amp; Data Processing</h4>
<ul>
<li><strong>Discriminated unions</strong>: Correctly handle nested discriminated unions in response parsing</li>
<li><strong>Extra field types</strong>: Parse extra field types correctly</li>
<li><strong>Empty metadata</strong>: Ignore empty metadata fields during parsing</li>
<li><strong>Singularization rules</strong>: Update resource name singularization rules for better consistency</li>
</ul>
</div></article></div>
