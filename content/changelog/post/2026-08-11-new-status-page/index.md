<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 11, 2026</time><h2 id="post-title">New Cloudflare Status page</h2>
<div class="changelog-badges"><span>support</span></div><div class="changelog-body"><p>The Cloudflare Status page at <a href="https://www.cloudflarestatus.com/">www.cloudflarestatus.com</a> has been rebuilt. It is available at the same address, and every previously documented <a href="https://www.cloudflarestatus.com/api">Status API</a> endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.</p>
<h4 id="notifications-that-fire-even-when-cloudflare-is-down">Notifications that fire even when Cloudflare is down</h4>
<p>The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.</p>
<p>The <strong>Maintenance Notification</strong> and <strong>Incident Alerts</strong> in <a href="/notifications/">Cloudflare Notifications</a> remain supported, and deliver to the destinations already configured on your account.</p>
<h4 id="markdown-for-ai-agents">Markdown for AI agents</h4>
<p>Every page on the status page returns Markdown when requested with an <code>Accept: text/markdown</code> header, so agents can read the current status without parsing HTML:</p>
<pre><code class="language-sh">curl -H &quot;Accept: text/markdown&quot; https://www.cloudflarestatus.com/locations&#10;</code></pre>
<h4 id="separate-feeds-for-incidents-and-maintenance">Separate feeds for incidents and maintenance</h4>
<p>Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:</p>
<pre><code class="language-txt">https://www.cloudflarestatus.com/api/v3/incidents.rss&#10;https://www.cloudflarestatus.com/api/v3/incidents.atom&#10;https://www.cloudflarestatus.com/api/v3/maintenance.rss&#10;https://www.cloudflarestatus.com/api/v3/maintenance.atom&#10;</code></pre>
<p>For more information, refer to <a href="/support/cloudflare-status/">Cloudflare Status</a>.</p>
</div></article></div>
