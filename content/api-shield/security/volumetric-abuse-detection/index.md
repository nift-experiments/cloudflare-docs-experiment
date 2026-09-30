---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/
  description: Set up adaptive, per-session rate limiting for API endpoints with Volumetric Abuse Detection.
  full_title: Volumetric Abuse Detection · Cloudflare API Shield docs
  head_html: <title>Volumetric Abuse Detection · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up adaptive, per-session rate limiting for API endpoints with Volumetric Abuse Detection."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/index.md"><meta property="og:title" content="Volumetric Abuse Detection · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up adaptive, per-session rate limiting for API endpoints with Volumetric Abuse Detection."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/#page","headline":"Volumetric Abuse Detection \u00b7 Cloudflare API Shield docs","description":"Set up adaptive, per-session rate limiting for API endpoints with Volumetric Abuse Detection.","url":"https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/volumetric-abuse-detection/
  schema: 1
---
<p>Cloudflare Volumetric Abuse Detection generates per-endpoint, per-session rate limit recommendations that adjust automatically as your traffic patterns change.</p>
<p>Cloudflare looks for endpoint abuse based on user traffic to individual endpoints.</p>
<p>For example, your API might see different levels of traffic to a <code>/reset-password</code> endpoint than a <code>/login</code> endpoint. Additionally, your <code>/login</code> endpoint might see higher than average traffic after a successful marketing campaign.</p>
<p>These two scenarios speak to the limitations of traditional rate limiting. Not only does traffic vary between endpoints, but it also can vary over time for the same endpoint. Volumetric Abuse Detection solves these problems using unsupervised learning (analyzing traffic patterns without predefined rules) to develop separate baselines for each endpoint and adjust to changes in user behavior over time.</p>
<p>Volumetric Abuse Detection rate limits are generated on a per-session basis rather than per IP address. This reduces false positives when traffic to your API increases, because rate limits track individual sessions rather than shared IP addresses.</p>
<p>Volumetric Abuse Detection rate limits are a way to prevent blatant volumetric abuse while minimizing false positives. If you are trying to prevent abusive bot traffic altogether, refer to Cloudflare's <a href="/bots/">Bot solutions</a>.</p>
<h2 id="process">Process</h2>
<p>Volumetric Abuse Detection analyzes your API's individual session traffic statistics to recommend per-endpoint, per-session rate limits.</p>
<p>To access your endpoints, go to <strong>Security</strong> &gt; <strong>Web Assets</strong> &gt; <strong>Endpoints</strong>.</p>
<p>Recommendations will continue to update if your traffic pattern changes.</p>
<h3 id="requirements">Requirements</h3>
<p>Volumetric Abuse Detection generates rate limit thresholds only after collecting enough traffic data to produce reliable recommendations. If recommendations are missing for a discovered endpoint, the traffic likely failed to meet the necessary criteria.</p>
<p>Thresholds are suggested only for endpoints that satisfy all of the following requirements within the last seven days (or since initial discovery):</p>
<ul>
<li>The endpoint must receive sufficient valid traffic (traffic that meets the <a href="/api-shield/security/api-discovery/#requirements">API Discovery</a> criteria). Intermittent or erratic traffic may prevent suggestions.</li>
<li>The endpoint must be accessed by at least 50 distinct sessions in any 24-hour period during the last seven days.</li>
<li><span class="nb-glossary-tooltip" title="session identifier">Session identifiers</span>, such as an authorization token available as a request header or cookie, must be configured to allow Cloudflare to accurately detect individual sessions and perform the required per-session rate analysis.</li>
</ul>
<p>After adding a session identifier, allow 24 hours for rate limit recommendations to appear on endpoints in the Cloudflare dashboard.</p>
<h3 id="rate-limiting-recommendation-calculation">Rate limiting recommendation calculation</h3>
<p>Select an endpoint row in <strong>Endpoints</strong> to view its rate limit recommendation. The detail view shows the overall recommended value and percentile-based values (p50, p90, p99).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="percentile-values">Percentile values</h3>
@markup("md", "content/.markup/bodies/3189.md")
</aside>
<p>Cloudflare recalculates the recommended value throughout the day based on requests from the last 24 hours. The recommendation may not change if your traffic profile remains consistent.</p>
<p>Cloudflare recommends using the overall rate limit recommendation rather than a single percentile value. The overall recommendation accounts for variation across all your API sessions. Choosing a single percentile value may cause false positives due to a high number of outliers.</p>
<p>In <strong>Endpoints</strong>, you can review the confidence level for each recommendation and how many unique sessions were observed over the last seven days. In general, endpoints with fewer unique sessions and high variability of user behavior will have lower confidence scores.</p>
<p>Implementing low confidence rate limits can still be helpful to prevent API abuse. If the confidence level is low, start your rate limit rule in <code>log</code> mode and observe violations for false positives before switching to <code>block</code>.</p>
<h3 id="create-rate-limits">Create rate limits</h3>
<p>Refer to the <a href="/waf/rate-limiting-rules/create-zone-dashboard/">Rules documentation</a> for more information on how to create an Advanced Rate Limiting rule.</p>
<h2 id="api">API</h2>
<p><a href="/api/resources/api_gateway/subresources/operations/methods/get/">Rate limit recommendations are available via the API</a> if you would like to dynamically update rate limits over time.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/operations/{operation_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="special-cases">Special cases</h2>
<h3 id="rate-limit-by-user-jwt-claim">Rate limit by user (JWT claim)</h3>
<p>You can rate limit requests based on any claim inside of a JSON Web Token (JWT), such as:</p>
<ul>
<li>Registered claims like <code>aud</code> or <code>sub</code></li>
<li>Custom claims like <code>userEmail</code>, including nested custom claims like <code>user.email</code></li>
</ul>
<p>Rate limiting based on JWT claim values will only work on valid JSON Web Tokens. If you do not block invalid JSON Web Tokens on your path, the <a href="/waf/rate-limiting-rules/parameters/#missing-field-versus-empty-value">JWT claims will all be counted and possibly blocked</a> if high traffic is detected in the Point of Presence (PoP).</p>
<p>You must also count the JWT claim that uniquely identifies the user. If you select a claim that is the same for many of your users, their rate limits will all be counted together.</p>
<h3 id="rate-limit-by-user-tier">Rate limit by user tier</h3>
<p>If you offer multiple tiers on your website or application and you want to enforce rate limiting based on the tiers, such as:</p>
<ul>
<li>If <code>&quot;aud&quot;: &quot;free-tier&quot;</code>, rate limit to five requests per minute.</li>
<li>If <code>&quot;aud&quot;: &quot;premium-tier&quot;</code>, rate limit to 50 requests per minute.</li>
</ul>
<p>You can follow the rate limiting rule example below:</p>
<pre tabindex="0"><code class="language-txt">(http.request.method eq &quot;GET&quot; and&#10;http.host eq &quot;&lt;YOUR_DOMAIN&gt;&quot; and&#10;http.request.uri.path matches &quot;&lt;/EXAMPLE_PATH&gt;&quot; and&#10;lookup_json_string(http.request.jwt.claims[&quot;&lt;JWT_TOKEN_CONFIGURATION_ID&gt;&quot;][0], &quot;aud&quot;) eq &quot;free-tier&quot;&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<p>API Shield will always calculate recommendations when session identifiers are configured. To enable session-based rate limits, <a href="/waf/rate-limiting-rules/#availability">subscribe to Advanced Rate Limiting</a>.</p>
<h2 id="availability">Availability</h2>
<p>Volumetric Abuse Detection is only available for Enterprise customers. If you are an Enterprise customer interested in this product, contact your account team.</p>
