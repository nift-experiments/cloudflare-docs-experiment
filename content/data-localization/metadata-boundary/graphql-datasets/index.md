---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/metadata-boundary/graphql-datasets/
  description: GraphQL Analytics API fields that respect Customer Metadata Boundary configuration.
  full_title: GraphQL datasets · Cloudflare Data Localization Suite docs
  head_html: <title>GraphQL datasets · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="GraphQL Analytics API fields that respect Customer Metadata Boundary configuration."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/metadata-boundary/graphql-datasets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/metadata-boundary/graphql-datasets/index.md"><meta property="og:title" content="GraphQL datasets · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="GraphQL Analytics API fields that respect Customer Metadata Boundary configuration."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/metadata-boundary/graphql-datasets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Data Localization Suite"><meta name="pcx_tags" content="GraphQL,Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/metadata-boundary/graphql-datasets/#page","headline":"GraphQL datasets \u00b7 Cloudflare Data Localization Suite docs","description":"GraphQL Analytics API fields that respect Customer Metadata Boundary configuration.","url":"https://developers.cloudflare.com/data-localization/metadata-boundary/graphql-datasets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL","Analytics"]}</script>
  markdown: true
  noindex: false
  route: /data-localization/metadata-boundary/graphql-datasets/
  schema: 1
---
<p>The <a href="/analytics/graphql-api/">GraphQL Analytics API</a> allows you to programmatically query your Cloudflare analytics data (such as request counts, security events, and performance metrics). When Customer Metadata Boundary (CMB) is enabled, not all analytics data fields are available in every region.</p>
<p>The table below shows a non-exhaustive list of GraphQL Analytics API fields that respect CMB configuration. Fields marked &quot;US and EU&quot; return data regardless of your CMB region. Fields marked &quot;US only&quot; return data only when CMB is set to US — if your CMB is set to EU, queries for these fields will return empty results.</p>
<table>
<thead>
<tr>
<th>Suite/Category</th>
<th>Product</th>
<th>GraphQL Analytics API Field(s) supported in</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application Performance</td>
<td>Caching/CDN</td>
<td>US and EU <br/> <code>httpRequestsAdaptive</code> <br/> <code>httpRequestsAdaptiveGroups</code> <br/> <code>httpRequestsOverviewAdaptiveGroups</code> <br/> <code>httpRequests1mGroups</code> <br/> <code>httpRequests1hGroups</code> <br/> <code>httpRequests1dGroups</code></td>
</tr>
<tr>
<td>Cache Reserve</td>
<td></td>
<td>US and EU <br/> <code>cacheReserveOperationsAdaptiveGroups</code> <br/> <code>cacheReserveRequestsAdaptiveGroups</code> <br/> <code>cacheReserveStorageAdaptiveGroups</code></td>
</tr>
<tr>
<td>DNS</td>
<td></td>
<td>US and EU <br/> <code>dnsAnalyticsAdaptive</code> <br/> <code>dnsAnalyticsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Image Resizing</td>
<td></td>
<td>US only <br/> <code>imageResizingRequests1mGroups</code> <br/> <code>imagesRequestsAdaptiveGroups</code> <br/> <code>imagesUniqueTransformations</code></td>
</tr>
<tr>
<td>Load Balancing</td>
<td></td>
<td>US only <br/> <a href="/load-balancing/reference/load-balancing-analytics/#graphql-analytics"><code>loadBalancingRequestsAdaptive</code></a> <br/> <a href="/load-balancing/reference/load-balancing-analytics/#graphql-analytics"><code>loadBalancingRequestsAdaptiveGroups</code></a> <br/> <code>healthCheckEventsAdaptive</code> <br/> <code>healthCheckEventsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Stream Delivery</td>
<td>Same as Caching/CDN</td>
<td></td>
</tr>
<tr>
<td>Tiered Caching</td>
<td></td>
<td>US and EU <br/> Only the field <code>upperTierColoName</code> part of <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Secondary DNS</td>
<td>Same as DNS</td>
<td></td>
</tr>
<tr>
<td>Waiting Room</td>
<td></td>
<td>US and EU <br/> <a href="/waiting-room/waiting-room-analytics/#graphql-analytics"><code>waitingRoomAnalyticsAdaptive</code></a> <br/> <a href="/waiting-room/waiting-room-analytics/#graphql-analytics"><code>waitingRoomAnalyticsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Web Analytics / Real User Monitoring (RUM)</td>
<td></td>
<td>US only <br/> <code>rumWebVitalsEventsAdaptive</code> <br/> <code>rumWebVitalsEventsAdaptiveGroups</code> <br/> <code>rumPerformanceEventsAdaptiveGroups</code> <br/> <code>rumPageloadEventsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Zaraz</td>
<td></td>
<td>US and EU <br/><code>zarazActionsAdaptiveGroups</code> <br/> <code>zarazTrackAdaptiveGroups</code> <br/> <code>zarazTriggersAdaptiveGroups</code></td>
</tr>
<tr>
<td>Application Security</td>
<td>Advanced Certificate Manager</td>
<td>US and EU <br/> Only the fields <code>clientSSLProtocol</code> and <code>ja3Hash</code> part of <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Advanced DDoS Protection</td>
<td></td>
<td>US and EU <br/> <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><code>dosdAttackAnalyticsGroups</code></a> <br/> <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><code>dosdNetworkAnalyticsAdaptiveGroups</code></a> <br/> <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><code>flowtrackdNetworkAnalyticsAdaptiveGroups</code></a> <br/> <code>advancedTcpProtectionNetworkAnalyticsAdaptiveGroups</code> <br/> <code>advancedDnsProtectionNetworkAnalyticsAdaptiveGroups</code> <br/> <code>programmableFlowProtectionNetworkAnalyticsAdaptiveGroups</code></td>
</tr>
<tr>
<td>API Shield</td>
<td></td>
<td>US and EU <br/> <a href="/api-shield/security/graphql-protection/api/#gather-graphql-statistics"><code>apiGatewayGraphqlQueryAnalyticsGroups</code></a> <br/> <code>apiGatewayMatchedSessionIDsAdaptiveGroups</code> <br/> US only <br/> <code>apiRequestSequencesGroups</code></td>
</tr>
<tr>
<td>Bot Management</td>
<td></td>
<td>US and EU <br/><code>httpRequestsAdaptive</code> <br/> <a href="/analytics/graphql-api/migration-guides/graphql-api-analytics/"><code>httpRequestsAdaptiveGroups</code></a> <br/> <a href="/analytics/graphql-api/tutorials/querying-firewall-events/"><code>firewallEventsAdaptive</code></a> <br/> <a href="https://blog.cloudflare.com/how-we-used-our-new-graphql-api-to-build-firewall-analytics/"><code>firewallEventsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>DNS Firewall</td>
<td>Same as DNS</td>
<td></td>
</tr>
<tr>
<td>DMARC Management</td>
<td></td>
<td>US and EU <br/> <code>dmarcReportsAdaptive</code> <br/> <code>dmarcReportsSourcesAdaptiveGroups</code></td>
</tr>
<tr>
<td>Client-side security (formerly Page Shield)</td>
<td></td>
<td>US and EU <br/> <a href="/client-side-security/rules/violations/#get-rule-violations-via-graphql-api"><code>pageShieldReportsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>SSL</td>
<td></td>
<td>US and EU <br/> Only the fields <code>clientSSLProtocol</code> and <code>ja3Hash</code> part of <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code></td>
</tr>
<tr>
<td>SSL 4 SaaS</td>
<td></td>
<td>US and EU <br/> <a href="/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/#explore-customer-usage">clientRequestHTTPHost</a> <br/> Refer to <a href="/analytics/graphql-api/tutorials/end-customer-analytics/">GraphQL Tutorial on querying HTTP events by hostname</a></td>
</tr>
<tr>
<td>Turnstile</td>
<td></td>
<td>US and EU <br/> <a href="/turnstile/turnstile-analytics/"><code>turnstileAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>WAF/L7 Firewall</td>
<td></td>
<td>US and EU <br/> <a href="/analytics/graphql-api/tutorials/querying-firewall-events/"><code>firewallEventsAdaptive</code></a> <br/> <a href="https://blog.cloudflare.com/how-we-used-our-new-graphql-api-to-build-firewall-analytics/"><code>firewallEventsAdaptiveGroups</code></a> <br/> <code>firewallEventsAdaptiveByTimeGroups</code></td>
</tr>
<tr>
<td>Developer Platform</td>
<td>Cloudflare Images</td>
<td>US only <br/> <code>imagesRequestsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Cloudflare Pages</td>
<td></td>
<td>US only <br/> <code>pagesFunctionsInvocationsAdaptiveGroups</code> <br/></td>
</tr>
<tr>
<td>Durable Objects</td>
<td></td>
<td>US only <br/> <a href="/durable-objects/observability/metrics-and-analytics/"><code>durableObjectsInvocationsAdaptiveGroups</code></a> <br/> <a href="/durable-objects/observability/metrics-and-analytics/"><code>durableObjectsPeriodicGroups</code></a> <br/> <a href="/durable-objects/observability/metrics-and-analytics/"><code>durableObjectsStorageGroups</code></a> <br/> <a href="/durable-objects/observability/metrics-and-analytics/"><code>durableObjectsSubrequestsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Email Routing</td>
<td></td>
<td>US and EU <br/> <code>emailRoutingAdaptive</code> <br/> <code>emailRoutingAdaptiveGroups</code></td>
</tr>
<tr>
<td>R2</td>
<td></td>
<td>US and EU <br/> <code>r2OperationsAdaptiveGroups</code> <br/> <code>r2StorageAdaptiveGroups</code></td>
</tr>
<tr>
<td>Stream</td>
<td></td>
<td>US only <br/> <a href="/stream/getting-analytics/fetching-bulk-analytics/"><code>streamMinutesViewedAdaptiveGroups</code></a> <br/> <a href="/stream/getting-analytics/fetching-bulk-analytics/"><code>videoPlaybackEventsAdaptiveGroups</code></a> <br/> <a href="/stream/getting-analytics/fetching-bulk-analytics/"><code>videoBufferEventsAdaptiveGroups</code></a> <br/> <a href="/stream/getting-analytics/fetching-bulk-analytics/"><code>videoQualityEventsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Workers (deployed on a Zone)</td>
<td></td>
<td>US and EU <br/> <code>workerPlacementAdaptiveGroups</code> <br/> <code>workersAnalyticsEngineAdaptiveGroups</code> <br/> US only <br/> <code>workersZoneInvocationsAdaptiveGroups</code> <br/> <code>workersZoneSubrequestsAdaptiveGroups</code> <br/> <code>workersOverviewRequestsAdaptiveGroups</code> <br/> <code>workersOverviewDataAdaptiveGroups</code> <br/> <a href="/analytics/graphql-api/tutorials/querying-workers-metrics/"><code>workersInvocationsAdaptive</code></a> <br/> <code>workersInvocationsScheduled</code> <br/> <code>workersSubrequestsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Network Services</td>
<td>Network Error Logging (NEL) / Edge Reachability / Last Mile Insights</td>
<td>US only <br/> <code>nelReportsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Cloudflare Network Firewall</td>
<td></td>
<td>US and EU <br/> <a href="/cloudflare-network-firewall/tutorials/graphql-analytics/"><code>magicFirewallSamplesAdaptiveGroups</code></a> <br/> <a href="/cloudflare-network-firewall/tutorials/graphql-analytics/#example-queries-for-cloudflare-network-firewall"><code>magicFirewallNetworkAnalyticsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Network Flow</td>
<td></td>
<td>US only <br/> <a href="/network-flow/tutorials/graphql-analytics/"><code>mnmFlowDataAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Magic Transit</td>
<td></td>
<td>US and EU <br/> <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><code>magicTransitNetworkAnalyticsAdaptiveGroups</code></a> <br/> <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><code>flowtrackdNetworkAnalyticsAdaptiveGroups</code></a> <br/> <code>magicTransitTunnelHealthCheckSLOsAdaptiveGroups</code> <br/><a href="/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-healthcheck-results/"><code>magicTransitTunnelHealthChecksAdaptiveGroups</code></a> <br/> <a href="/magic-transit/analytics/query-bandwidth/"><code>magicTransitTunnelTrafficAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Cloudflare WAN</td>
<td></td>
<td>US and EU <br/> <code>MagicWANConnectorMetricsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Spectrum</td>
<td></td>
<td>US and EU <br/> <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><code>spectrumNetworkAnalyticsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Platform</td>
<td>GraphQL Analytics API</td>
<td>US and EU <br/> <a href="/analytics/graphql-api/features/discovery/introspection/">All GraphQL Analytics API datasets</a></td>
</tr>
<tr>
<td>Logpush</td>
<td></td>
<td>US and EU <br/> <a href="/logs/logpush/alerts-and-analytics/#enable-logpush-health-analytics"><code>logpushHealthAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Zero Trust</td>
<td>Access</td>
<td>US and EU <br/> <a href="/analytics/graphql-api/tutorials/querying-access-login-events/"><code>accessLoginRequestsAdaptiveGroups</code></a></td>
</tr>
<tr>
<td>Browser Isolation</td>
<td></td>
<td>US and EU <br/> Only the field <code>isIsolated</code> part of <code>gatewayL7RequestsAdaptiveGroups</code></td>
</tr>
<tr>
<td>DLP</td>
<td>Part of Gateway HTTP / Gateway L7</td>
<td></td>
</tr>
<tr>
<td>Gateway</td>
<td></td>
<td>US and EU <br/> <code>gatewayL7RequestsAdaptiveGroups</code> <br/> <code>gatewayL4SessionsAdaptiveGroups</code> <br/> <code>gatewayResolverQueriesAdaptiveGroups</code> <br/> <code>gatewayResolverByCategoryAdaptiveGroups</code> <br/> <code>gatewayResolverByRuleExecutionPerformanceAdaptiveGroups</code> <br/> US only <br/> <code>gatewayL4DownstreamSessionsAdaptiveGroups</code> <br/> <code>gatewayL4UpstreamSessionsAdaptiveGroups</code></td>
</tr>
<tr>
<td>WARP</td>
<td></td>
<td>US and EU <br/> <code>warpDeviceAdaptiveGroups</code></td>
</tr>
</tbody>
</table>
