<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 18, 2025</time><h2 id="post-title">New API Posture Management for API Shield</h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>Now, API Shield <strong>automatically</strong> labels your API inventory with API-specific risks so that you can track and manage risks to your APIs.</p>
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
</div></article></div>
