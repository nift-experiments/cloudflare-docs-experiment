<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 27, 2025</time><h2 id="post-title">Audit logs (version 2) - Beta Release</h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.</p>
<p>Availability: Audit logs (version 2) is now in Beta, with support limited to <strong>API access</strong>.</p>
<p>Use the following API endpoint to retrieve audit logs:</p>
<pre><code class="language-js">GET https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/logs/audit?since=&lt;date&gt;&amp;before=&lt;date&gt;&#10;</code></pre>
<p>You can access detailed documentation for audit logs (version 2) Beta API release <a href="https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/">here</a>.</p>
<p><strong>Key Improvements in the Beta Release:</strong></p>
<ul>
<li>
<p><strong>Automated &amp; standardized logging</strong>: Logs are now generated automatically using a standardized system, replacing manual, team-dependent logging. This ensures consistency across all Cloudflare services.</p>
</li>
<li>
<p><strong>Expanded product coverage</strong>: Increased audit log coverage from 75% to 95%. Key API endpoints such as <code>/accounts</code>, <code>/zones</code>, and <code>/organizations</code> are now included.</p>
</li>
<li>
<p><strong>Granular filtering</strong>: Logs now follow a uniform format, enabling precise filtering by actions, users, methods, and resources—allowing for faster and more efficient investigations.</p>
</li>
<li>
<p><strong>Enhanced context and traceability</strong>: Each log entry now includes detailed context, such as the authentication method used, the interface (API or Dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for better traceability.</p>
</li>
<li>
<p><strong>Comprehensive activity capture</strong>: Expanded logging to include GET requests and failed attempts, ensuring that all critical activities are recorded.</p>
</li>
</ul>
<p><strong>Known Limitations in Beta</strong></p>
<ul>
<li>Error handling for the API is not implemented.</li>
<li>There may be gaps or missing entries in the available audit logs.</li>
<li>UI is unavailable in this Beta release.</li>
<li>System-level logs and User-Activity logs are not included.</li>
</ul>
<p>Support for these features is coming as part of the GA release later this year. For more details, including a sample audit log, check out our blog post: <a href="https://blog.cloudflare.com/introducing-automatic-audit-logs/">Introducing Automatic Audit Logs</a></p>
</div></article></div>
