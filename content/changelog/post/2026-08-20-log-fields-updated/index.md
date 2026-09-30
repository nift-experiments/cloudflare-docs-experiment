<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 20, 2026</time><h2 id="post-title">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="new-datasets">New datasets</h4>
<ul>
<li><strong>Account Abuse Protection Events</strong>: A new dataset with fields including <code>AuthenticationIdentityProvider</code>, <code>AuthenticationMethod</code>, <code>AuthenticationStatus</code>, <code>BotScore</code>, <code>ClientASN</code>, <code>ClientCity</code>, <code>ClientCountry</code>, <code>ClientIP</code>, <code>Email</code>, <code>EphemeralID</code>, <code>EventSource</code>, <code>EventType</code>, <code>FraudEmailRisk</code>, <code>Host</code>, <code>JA4</code>, <code>RayID</code>, <code>Timestamp</code>, <code>UserAgent</code>, and <code>UserID</code>.</li>
<li><strong>Magic BGP Logs</strong>: A new dataset with fields including <code>Direction</code>, <code>EventData</code>, <code>EventKind</code>, <code>EventTimestamp</code>, <code>TunnelID</code>, and <code>TunnelName</code>.</li>
</ul>
<h4 id="updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>AISecurityCustomTopicCategories</code>, <code>WAFRequestSignatureCategories</code>, and <code>WAFRequestSignatureRefs</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>ExperimentalFeatures</code> and <code>PackageInfo</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>AISecurityCustomTopicCategories</code>, <code>ClientTLSKeyExchangeGroup</code>, <code>WAFRequestSignatureCategories</code>, and <code>WAFRequestSignatureRefs</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div></article></div>
