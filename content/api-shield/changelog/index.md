---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/changelog/
  description: Track the latest updates and changes to API Shield features.
  full_title: Changelog · Cloudflare API Shield docs
  head_html: <title>Changelog · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Track the latest updates and changes to API Shield features."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/changelog/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/api-shield/changelog/index.xml"><meta property="og:title" content="Changelog · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track the latest updates and changes to API Shield features."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/api-shield/changelog/#page","headline":"Changelog \u00b7 Cloudflare API Shield docs","description":"Track the latest updates and changes to API Shield features.","url":"https://developers.cloudflare.com/api-shield/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/changelog/
  schema: 1
---
<h2 id="2026-08-25">2026-08-25</h2>

<strong>Symmetric key support for JWT validation</strong>

<p>API Shield <a href="/api-shield/security/jwt-validation/">JSON Web Token validation</a> now supports symmetric keys that use the <code>HS256</code>, <code>HS384</code>, and <code>HS512</code> algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.</p>
<p>Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.</p>
<p>Refer to <a href="/api-shield/security/jwt-validation/api/#credentials">Configure JWT validation via the API</a> for supported key formats and credential requirements.</p>


<h2 id="2026-03-23">2026-03-23</h2>

<strong>Web Assets fields now available in GraphQL Analytics API</strong>

<p>Two new fields are now available in the <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code> <a href="/analytics/graphql-api/">GraphQL Analytics API</a> datasets:</p>
<ul>
<li><code>webAssetsOperationId</code> — the ID of the <a href="/api-shield/management-and-monitoring/">saved endpoint</a> that matched the incoming request.</li>
<li><code>webAssetsLabelsManaged</code> — the <a href="/api-shield/management-and-monitoring/endpoint-labels/#managed-labels">managed labels</a> mapped to the matched operation at the time of the request (for example, <code>cf-llm</code>, <code>cf-log-in</code>). At most 10 labels are returned per request.</li>
</ul>
<p>Both fields are empty when no operation matched. <code>webAssetsLabelsManaged</code> is also empty when no managed labels are assigned to the matched operation.</p>
<p>These fields allow you to determine, per request, which Web Assets operation was matched and which managed labels were active. This is useful for troubleshooting downstream security detection verdicts — for example, understanding why <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> did or did not flag a request.</p>
<p>Refer to <a href="/api-shield/management-and-monitoring/endpoint-labels/#analytics">Endpoint labeling service</a> for GraphQL query examples.</p>


<h2 id="2026-03-09">2026-03-09</h2>

<strong>New Vulnerability Scanner for API Shield</strong>

<p>Introducing Cloudflare's Web and API Vulnerability Scanner (Open Beta)</p>
<p>Cloudflare is launching the <a href="https://blog.cloudflare.com/vulnerability-scanner">Open Beta of the <strong>Web and API Vulnerability Scanner</strong></a> for all <a href="/api-shield/">API Shield</a> customers. This new, stateful Dynamic Application Security Testing (DAST) platform helps teams proactively find logic flaws in their APIs.</p>
<p>The initial release focuses on detecting Broken Object Level Authorization (BOLA) vulnerabilities by building API call graphs to simulate attacker and owner contexts, then testing these contexts by sending real HTTP requests to your APIs.</p>
<p>The scanner is now available via the Cloudflare API. To scan, set up your target environment, owner and attacker credentials, and upload your OpenAPI file with response schemas. The scanner will be available in the Cloudflare dashboard in a future release.</p>
<p><strong>Access</strong>: This feature is only available to API Shield subscribers via the Cloudflare API. We hope you will use the API for programmatic integration into your CI/CD pipelines and security dashboards.</p>
<p><strong>Documentation</strong>: Refer to the <a href="/api-shield/security/vulnerability-scanner/">developer documentation</a> to start scanning your endpoints today.</p>


<h2 id="2025-11-25">2025-11-25</h2>

<strong>New Zombie API detection for API Shield</strong>

<p>API Shield now automatically detects zombie endpoints — saved endpoints that have not received traffic for an extended period. When detected, the <code>cf-risk-zombie</code> <a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">risk label</a> is applied.</p>
<p>The scan runs daily alongside existing risk scans. Endpoints are labeled after 32 days without traffic.</p>
<p>Zombie endpoints may indicate deprecated or forgotten API surface area that could pose a security risk. Review these endpoints and consider removing them from Endpoint Management if they are no longer in use. Also consider using a <a href="/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule">fallthrough rule</a> to prevent communication with endpoints removed from Endpoint Management.</p>


<h2 id="2025-11-12">2025-11-12</h2>

<strong>New BOLA Vulnerability Detection for API Shield</strong>

<p>Now, API Shield automatically searches for and highlights <strong>Broken Object Level Authorization (BOLA) attacks</strong> on managed API endpoints. API Shield will highlight both BOLA enumeration attacks and BOLA pollution attacks, telling you what was attacked, by who, and for how long.</p>
<p>You can find these attacks three different ways: Security Overview, Endpoint details, or Security Analytics. If these attacks are not found on your managed API endpoints, there will not be an overview card or security analytics suspicious activity card.</p>
<p>On the Security Overview card, select the suggestion &gt; <strong>View details</strong> to review the top attacked API endpoints, endpoint details, and the attack summary:
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-card.png" alt="BOLA attack Overview card" />
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-drawer.png" alt="BOLA attack Overview drawer" /></p>
<p>From the endpoint details, you can select <strong>View attack</strong> to find details about the BOLA attacker’s sessions.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-endpoint-attack.png" alt="BOLA attack endpoint details" /></p>
<p>From here, select <strong>View in Analytics</strong> to observe attacker traffic over time for the last seven days.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-analytics-drawer.png" alt="BOLA attack analytics drawer" /></p>
<p>Your search will filter to traffic on that endpoint in the last seven days, along with the malicious session IDs found in the attack. Session IDs are hashed for privacy and will not be found in your origin logs. Refer to IP and JA4 fingerprint to cross-reference behavior at the origin.</p>
<p>At any time, you can also start your investigation into attack traffic from Security Analytics by selecting the suspicious activity card.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-suspicious-card.png" alt="Suspicious Activity card" /></p>
<p>We urge you to take all of this client information to your developer team to research the attacker behavior and ensure any broken authorization policies in your API are fixed at the source in your application, preventing further abuse.</p>
<p>In addition, this release marks the end of the beta period for these scans. All Enterprise customers with API Shield subscriptions will see these new attacks if found on their zone.</p>


<h2 id="2025-03-18">2025-03-18</h2>

<strong>New API Posture Management for API Shield</strong>

<p>Now, API Shield <strong>automatically</strong> labels your API inventory with API-specific risks so that you can track and manage risks to your APIs.</p>
<p>View these risks in <a href="/api-shield/management-and-monitoring/">Endpoint Management</a> by label:</p>
<p><img src="/assets/upstream/images/changelog/api-shield/endpoint-management-label.png" alt="A list of endpoint management labels" /></p>
<p>...or in <a href="/security/security-insights/">Security Center Insights</a>:</p>
<p><img src="/assets/upstream/images/changelog/api-shield/posture-management-insight.png" alt="An example security center insight" /></p>
<p>API Shield will scan for risks on your API inventory daily. Here are the new risks we're scanning for and automatically labelling:</p>
<ul>
<li><strong>cf-risk-sensitive</strong>: applied if the customer is subscribed to the <a href="/waf/managed-rules/reference/sensitive-data-detection/">sensitive data detection ruleset</a> and the WAF detects sensitive data returned on an endpoint in the last seven days.</li>
<li><strong>cf-risk-missing-auth</strong>: applied if the customer has configured a session ID and no successful requests to the endpoint contain the session ID.</li>
<li><strong>cf-risk-mixed-auth</strong>: applied if the customer has configured a session ID and some successful requests to the endpoint contain the session ID while some lack the session ID.</li>
<li><strong>cf-risk-missing-schema</strong>: added when a learned schema is available for an endpoint that has no active schema.</li>
<li><strong>cf-risk-error-anomaly</strong>: added when an endpoint experiences a recent increase in response errors over the last 24 hours.</li>
<li><strong>cf-risk-latency-anomaly</strong>: added when an endpoint experiences a recent increase in response latency over the last 24 hours.</li>
<li><strong>cf-risk-size-anomaly</strong>: added when an endpoint experiences a spike in response body size over the last 24 hours.</li>
</ul>
<p>In addition, API Shield has two new 'beta' scans for <strong>Broken Object Level Authorization (BOLA) attacks</strong>. If you're in the beta, you will see the following two labels when API Shield suspects an endpoint is suffering from a BOLA vulnerability:</p>
<ul>
<li><strong>cf-risk-bola-enumeration</strong>: added when an endpoint experiences successful responses with drastic differences in the number of unique elements requested by different user sessions.</li>
<li><strong>cf-risk-bola-pollution</strong>: added when an endpoint experiences successful responses where parameters are found in multiple places in the request.</li>
</ul>
<p>We are currently accepting more customers into our beta. Contact your account team if you are interested in BOLA attack detection for your API.</p>
<p>Refer to the <a href="https://blog.cloudflare.com/cloudflare-security-posture-management/">blog post</a> for more information about Cloudflare's expanded posture management capabilities.</p>


<h2 id="2025-02-17">2025-02-17</h2>
<p><strong>New automatically applied risk labels</strong></p>
<p>API Shield now automatically labels endpoints with risks due to missing schemas and performance anomalies (spikes in error rates, latency, and body response sizes).</p>
<h2 id="2025-01-16">2025-01-16</h2>
<p><strong>API Authentication Posture</strong></p>
<p>Customers will see per-endpoint authentication details inside <a href="/api-shield/management-and-monitoring/">Endpoints</a> for zones with configured session identifiers.</p>
<h2 id="2024-12-19">2024-12-19</h2>
<p><strong>Automatically applied endpoint risk labels</strong></p>
<p>API Shield now automatically labels endpoints with risks due to authentication status and sensitive data detection.</p>
<h2 id="2024-11-04">2024-11-04</h2>
<p><strong>Endpoint labels</strong></p>
<p>Customers can now organize their endpoints by use case and custom labels using the <a href="/api-shield/management-and-monitoring/endpoint-labels/">Endpoint labeling service</a> for easy reference and future machine learning (ML) model training.</p>
<h2 id="2024-10-18">2024-10-18</h2>
<p><strong>API Shield fields in Custom Rules</strong></p>
<p>Customers can now use API Shield product feature fields in <a href="/waf/custom-rules/">custom rules</a>, referencing features such as <a href="/api-shield/security/jwt-validation/">JWT validation</a>, <a href="/api-shield/get-started/#session-identifiers">session identifiers</a>, and <a href="/api-shield/security/schema-validation/">Schema validation</a>.</p>
<h2 id="2024-09-25">2024-09-25</h2>
<p><strong>Fallthrough rule for Schema validation 2.0</strong></p>
<p>Customers can now enable the <a href="/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule">Fallthrough Action</a> for Schema validation 2.0 to block or log requests that do not match the endpoints listed in schemas protected by Schema validation 2.0.</p>
<h2 id="2024-08-28">2024-08-28</h2>
<p><strong>Increased capacity for Endpoint management and Schema validation</strong></p>
<p>Endpoint management and Schema validation now support up to 10,000 saved and validated API endpoints.</p>
<h2 id="2024-07-08">2024-07-08</h2>
<p><strong>API Discovery's hostname variables</strong></p>
<p>Customers can now see when <a href="/api-shield/security/api-discovery/">API Discovery</a> groups similar subdomains with the same methods and paths, making it easy to discover and manage APIs that share many vanity domains or subdomains.</p>
<h2 id="2024-07-02">2024-07-02</h2>
<p><strong>Route API requests using API Routing</strong></p>
<p>Customers can now route requests to different back-end services through <a href="/api-shield/management-and-monitoring/api-routing/">API Routing</a>, creating a unified front for their APIs distributed across otherwise disparate systems.</p>
<h2 id="2024-05-13">2024-05-13</h2>
<p><strong>Use JWT claims in Advanced Rate Limiting, Transform Rules, and as session IDs</strong></p>
<p>Customers can now use the fields inside <a href="/api-shield/security/jwt-validation/transform-rules/#enhance-transform-rules-with-jwt-claims">JSON Web Tokens (known as claims)</a> as <a href="/api-shield/get-started/#session-identifiers">session identifiers in API Shield</a>, to count values in <a href="/waf/rate-limiting-rules/">Advanced Rate Limiting</a>, and to send on useful information in <a href="/rules/transform/">Transform Rules</a>.</p>
<h2 id="2024-04-30">2024-04-30</h2>
<p><strong>Build sequence mitigation rules via the Cloudflare dashboard</strong></p>
<p>Customers can now build <a href="/api-shield/security/sequence-mitigation/">Sequence mitigation</a> rules with a new user interface inside the API Shield section of the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<h2 id="2024-02-23">2024-02-23</h2>
<p><strong>Endpoint management supports hostname variables</strong></p>
<p>Customers can now save endpoints in <a href="/api-shield/management-and-monitoring/">Endpoint management</a> that contain variables in the hostname. Hostname variables are supported across all product features.</p>


