<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 8, 2026</time><h2 id="post-title">Create WAF rules directly from Threat Events saved views</h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Cloudforce One users can now turn <a href="/security-center/cloudforce-one/#analyze-threat-events">Threat Events indicators</a> into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their <strong>Saved Views</strong>.</p>
<h4 id="why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules.
This new integration bridges the gap between threat discovery and threat mitigation:</p>
<ul>
<li>When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.</li>
<li>Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.</li>
<li>Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.</li>
</ul>
<h4 id="how-to-use-it">How to use it</h4>
<p>You can implement these rules through both the dashboard UI and via the API / Terraform.</p>
<p>Go to <strong>Cloudflare Dashboard</strong> &gt; <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Manage Views</strong>, select your desired view, and select <strong>Create WAF Rule</strong>.</p>
<p>This will automatically pre-populate the <a href="/firewall/cf-dashboard/create-edit-delete-rules/">WAF rule builder</a> with the matching threat event IP indicators.</p>
<p>You can also automate this workflow by utilizing the <a href="/firewall/api/cf-firewall-rules/"><strong>WAF Rule Builder API</strong></a> alongside your <a href="/firewall/api/cf-firewall-rules/">Threat Events saved views endpoints</a>.</p>
</div></article></div>
