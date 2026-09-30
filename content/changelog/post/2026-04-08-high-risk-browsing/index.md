<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 8, 2026</time><h2 id="post-title">User risk scoring for high risk browsing activity</h2>
<div class="changelog-badges"><span>risk-score</span></div><div class="changelog-body"><p>Cloudflare One's <strong>User Risk Scoring</strong> now incorporates direct signals from <strong>Gateway DNS traffic patterns</strong>. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.</p>
<h4 id="why-this-matters">Why this matters</h4>
<p>Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:</p>
<ul>
<li><strong>Security threats</strong>: Domains associated with malware, phishing, or command-and-control (C2) centers.</li>
<li><strong>High-risk content</strong>: Categories such as questionable content or violence that may violate corporate compliance.</li>
</ul>
<p>Even if a Gateway policy is set to <strong>Block</strong> the traffic, the interaction is still captured as a &quot;hit&quot; to ensure the user's risk profile reflects the attempted activity.</p>
<h4 id="new-risk-behaviors">New risk behaviors</h4>
<p>Two new behaviors are now available in the dashboard:</p>
<ul>
<li><strong>Suspicious Security Domain Visited</strong>: Triggers when a user visits a domain in the security threats or security risk categories.</li>
<li><strong>High risk domain visited</strong>: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.</li>
</ul>
<p>To learn more and get started, refer to the <a href="/cloudflare-one/team-and-resources/users/risk-score/">User Risk Scoring documentation</a>.</p>
</div></article></div>
