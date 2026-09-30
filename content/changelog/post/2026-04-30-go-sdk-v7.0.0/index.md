---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/
  description: New updates and improvements at Cloudflare.
  full_title: Go SDK v7.0.0 Released · Changelog
  head_html: <title>Go SDK v7.0.0 Released · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Go SDK v7.0.0 Released · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/#page","headline":"Go SDK v7.0.0 Released \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-go-sdk-v7.0.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-30-go-sdk-v7.0.0/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 30, 2026</time><h2 id="post-title">Go SDK v7.0.0 Released</h2>
<div class="changelog-badges"><span>sdk</span><span>go-sdk</span></div><div class="changelog-body"><p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-go/compare/v6.10.0...v7.0.0">v6.10.0...v7.0.0</a></p>
<p>This is a major version release that includes breaking changes to three packages: <code>ai_search</code>, <code>email_security</code>, and <code>workers</code>. These changes reflect upstream API specification updates that improve type correctness and consistency.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="breaking-changes">Breaking Changes</h4>
<p>See the <a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">v7.0.0 Migration Guide</a> for before/after code examples and actions needed for each change.</p>
<h4 id="ai-search-searchforagents-metadata-removed">AI Search - SearchForAgents Metadata Removed</h4>
<p>The <code>SearchForAgents</code> nested type has been removed from all instance metadata structs. This field is no longer part of the API specification.</p>
<p><strong>Removed Types:</strong></p>
<ul>
<li><code>InstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>InstanceListResponseMetadataSearchForAgents</code></li>
<li><code>InstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>InstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>InstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceListResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateParamsMetadataSearchForAgents</code></li>
</ul>
<h4 id="email-security-path-parameter-type-changes">Email Security - Path Parameter Type Changes</h4>
<p>Multiple Email Security settings sub-resources have changed their path parameter types from <code>int64</code> to <code>string</code>:</p>
<ul>
<li><code>AllowPolicies</code> (<code>policyID int64</code> -&gt; <code>policyID string</code>)</li>
<li><code>BlockSenders</code> (<code>patternID int64</code> -&gt; <code>patternID string</code>)</li>
<li><code>Domains</code> (<code>domainID int64</code> -&gt; <code>domainID string</code>)</li>
<li><code>ImpersonationRegistry</code> (<code>displayNameID int64</code> -&gt; <code>impersonationRegistryID string</code>)</li>
<li><code>TrustedDomains</code> (<code>trustedDomainID int64</code> -&gt; <code>trustedDomainID string</code>)</li>
</ul>
<h4 id="email-security-investigate-parameter-rename">Email Security - Investigate Parameter Rename</h4>
<p>The <code>Investigate.Get</code>, <code>Investigate.Move.New</code>, and <code>Investigate.Reclassify.New</code> methods now use <code>investigateID</code> instead of <code>postfixID</code> as the path parameter name.</p>
<h4 id="email-security-domains-bulkdelete-method-removed">Email Security - Domains BulkDelete Method Removed</h4>
<p>The <code>SettingDomainService.BulkDelete</code> method and its associated types have been removed:</p>
<ul>
<li><code>SettingDomainBulkDeleteResponse</code></li>
<li><code>SettingDomainBulkDeleteParams</code></li>
</ul>
<h4 id="email-security-trusteddomains-return-type-change">Email Security - TrustedDomains Return Type Change</h4>
<p><code>SettingTrustedDomainService.New</code> now returns <code>*SettingTrustedDomainNewResponse</code> instead of <code>*SettingTrustedDomainNewResponseUnion</code>.</p>
<h4 id="email-security-investigate-move-return-type-change">Email Security - Investigate.Move Return Type Change</h4>
<p><code>InvestigateMoveService.New</code> now returns <code>*pagination.SinglePage[InvestigateMoveNewResponse]</code> instead of <code>*[]InvestigateMoveNewResponse</code>.</p>
<h4 id="workers-observability-telemetry-filter-restructuring">Workers - Observability Telemetry Filter Restructuring</h4>
<p>The observability telemetry filter parameter types have been restructured to support nested filter groups. New discriminated union types replace the previous flat filter arrays:</p>
<ul>
<li><code>ObservabilityTelemetryKeysParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code> (was <code>[]interface\{\}</code>)</li>
<li><code>ObservabilityTelemetryQueryParams.Parameters.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
<li><code>ObservabilityTelemetryValuesParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
</ul>
<p>New types include <code>FiltersObjectFiltersObject</code> (for group filters with <code>FilterCombination</code>) and <code>FiltersWorkersObservabilityFilterLeaf</code> (for leaf filters with typed <code>Operation</code>, <code>Type</code>, and <code>Value</code> fields).</p>
<h4 id="features">Features</h4>
<h4 id="organizations-audit-logs-client-organizations-logs-audit">Organizations - Audit Logs (<code>client.Organizations.Logs.Audit</code>)</h4>
<p><strong>NEW SERVICE:</strong> Query organization audit logs with cursor-based pagination.</p>
<ul>
<li><code>List()</code> - Retrieve audit logs</li>
</ul>
<h4 id="browser-rendering-client-browserrendering">Browser Rendering (<code>client.BrowserRendering</code>)</h4>
<ul>
<li><code>client.BrowserRendering.Devtools.Browser.Targets.Close()</code> - Close a specific browser target (tab, page) by ID</li>
</ul>
<h4 id="queues-client-queues">Queues (<code>client.Queues</code>)</h4>
<ul>
<li><code>client.Queues.GetMetrics()</code> - Retrieve queue metrics for a specific queue</li>
</ul>
<h4 id="ai-search-client-aisearch">AI Search (<code>client.AISearch</code>)</h4>
<ul>
<li>Added <code>WaitForCompletion</code> parameter to <code>NamespaceInstanceItemNewOrUpdateParams</code> and <code>NamespaceInstanceItemSyncParams</code> for synchronous indexing confirmation</li>
</ul>
<h4 id="bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>Magic Transit</strong>: <code>ConnectorService.List</code> parameter name corrected from <code>query</code> to <code>params</code> (non-functional, affects generated documentation only)</li>
</ul>
<h4 id="deprecations">Deprecations</h4>
<p>None in this release.</p>
<h4 id="get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go/releases/tag/v7.0.0">Download Go SDK v7.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/go/">Go SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">Migration Guide</a></li>
</ul>
</div></article></div>
