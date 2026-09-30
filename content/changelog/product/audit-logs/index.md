<h1 id="changelog">Changelog</h1>

<h2 id="audit-logs-v2-resource-history"><a href="/changelog/post/2026-07-27-audit-logs-v2-resource-history/">Audit Logs v2 — Resource History</a></h2>
<p><em>2026-07-27</em></p>
<p>Audit Logs v2 now includes <strong>Resource History</strong>. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.</p>
<p>Resource History uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_resource_history.png" alt="Resource History in Audit Logs v2" /></p>
<p><strong>Dashboard:</strong></p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>.</li>
<li>Open any audit log entry.</li>
<li>Select the <strong>History</strong> tab to see the full history for that resource.</li>
<li>Select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.</li>
</ol>
<p><strong>API:</strong></p>
<p>Use the History endpoint to retrieve the change history for any audit log entry:</p>
<pre><code class="language-txt">GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history&#10;</code></pre>
<p>The endpoint is also available for organization-scoped audit logs at <code>/organizations/{organization_id}/logs/audit/{id}/history</code>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/#resource-history">Resource History documentation</a>.</p>


<h2 id="audit-logs-v2-organization-level-audit-logs-in-cloudflare-dashboard"><a href="/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/">Audit Logs v2 — Organization-level audit logs in Cloudflare dashboard</a></h2>
<p><em>2026-06-24</em></p>
<p>You can now, as an <a href="/fundamentals/organizations/">Organization</a> Super Administrator, view organization-level <a href="/fundamentals/account/account-security/audit-logs/">audit logs</a> in the Cloudflare dashboard, in addition to the existing <a href="/fundamentals/account/account-security/audit-logs/#organization-activity-logs">API access</a>.</p>
<p>Organization audit logs help you monitor activity across your organization. You can see who performed an action, what changed, when it happened, how it was performed, and whether it succeeded or failed.</p>
<p>You can filter and search logs by actor, action, result, resource, request details, and timestamp. Use these logs to troubleshoot changes, investigate unexpected access, and support security or compliance workflows.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_organization_dashboard.png" alt="Organization audit logs in the Cloudflare dashboard" /></p>
<p>If you are viewing account-level audit logs and the account belongs to an organization where you are an Organization Super Administrator, select <strong>View Organization Audit Logs</strong> to open the parent organization's audit logs.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_view_organization_button.png" alt="View Organization Audit Logs button" /></p>
<p>To get started, go to <strong>Organizations</strong>, select your organization, then go to <strong>Manage Organization</strong> &gt; <strong>Audit Logs</strong>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>


<h2 id="audit-logs-v2-organization-level-support"><a href="/changelog/post/2026-04-23-audit-logs-v2-organization-level/">Audit Logs v2 — Organization-level support</a></h2>
<p><em>2026-04-23</em></p>
<p>Audit Logs v2 now supports organization-level audit logs. Org Admins can retrieve audit events for actions performed at the organization level via the Audit Logs v2 API.</p>
<p>To retrieve organization-level audit logs, use the following endpoint:</p>
<pre><code class="language-bash">GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit&#10;</code></pre>
<p>This release covers user-initiated actions performed through organization-level APIs. Audit logs for system-initiated actions, a dashboard UI, and Logpush support for organizations will be added in future releases.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17692.md")</aside>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>


<h2 id="audit-logs-version-2-general-availability"><a href="/changelog/post/2026-03-10-audit-logs-v2-ga/">Audit logs (version 2) - General Availability</a></h2>
<p><em>2026-03-10</em></p>
<p>Audit Logs v2 is now generally available to all Cloudflare customers.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/auditlogsv2.gif" alt="Audit Logs v2 GA" /></p>
<p>Audit Logs v2 provides a unified and standardized system for tracking and recording all user and system actions across Cloudflare products. Built on Cloudflare's API Shield / OpenAPI gateway, logs are generated automatically without requiring manual instrumentation from individual product teams, ensuring consistency across ~95% of Cloudflare products.</p>
<p><strong>What's available at GA:</strong></p>
<ul>
<li><strong>Standardized logging</strong> — Audit logs follow a consistent format across all Cloudflare products, making it easier to search, filter, and investigate activity.</li>
<li><strong>Expanded product coverage</strong> — ~95% of Cloudflare products covered, up from ~75% in v1.</li>
<li><strong>Granular filtering</strong> — Filter by actor, action type, action result, resource, raw HTTP method, zone, and more. Over 20 filter parameters available via the API.</li>
<li><strong>Enhanced context</strong> — Each log entry includes authentication method, interface (API or dashboard), Cloudflare Ray ID, and actor token details.</li>
<li><strong>18-month retention</strong> — Logs are retained for 18 months. Full history is accessible via the API or Logpush.</li>
</ul>
<p><strong>Access:</strong></p>
<ul>
<li><strong>Dashboard</strong>: Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>. Audit Logs v2 is shown by default.</li>
<li><strong>API</strong>: <code>GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit</code></li>
<li><strong>Logpush</strong>: Available via the <code>audit_logs_v2</code> account-scoped dataset.</li>
</ul>
<p><strong>Important notes:</strong></p>
<ul>
<li>Approximately 30 days of logs from the Beta period (back to ~February 8, 2026) are available at GA. These Beta logs will expire on ~April 9, 2026. Logs generated after GA will be retained for the full 18 months. Older logs remain available in Audit Logs v1.</li>
<li>The UI query window is limited to 90 days for performance reasons. Use the API or Logpush for access to the full 18-month history.</li>
<li><code>GET</code> requests (view actions) and <code>4xx</code> error responses are not logged at GA. <code>GET</code> logging will be selectively re-enabled for sensitive read operations in a future release.</li>
<li>Audit Logs v1 continues to run in parallel. A deprecation timeline will be communicated separately.</li>
<li>Before and after values — the ability to see what a value changed from and to — is a highly requested feature and is on our roadmap for a post-GA release. In the meantime, we recommend using Audit Logs v1 for before and after values. Audit Logs v1 will continue to run in parallel until this feature is available in v2.</li>
</ul>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>


<h2 id="audit-logs-version-2-logpush-beta-release"><a href="/changelog/post/2025-08-22-audit-logs-v2-logpush/">Audit logs (version 2) - Logpush Beta Release</a></h2>
<p><em>2025-08-22</em></p>
<p><a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/">Audit Logs v2 dataset</a> is now available via Logpush.</p>
<p>This expands on earlier releases of Audit Logs v2 in the <a href="/changelog/2025-03-27-automatic-audit-logs-beta-release/">API</a> and <a href="/changelog/2025-07-29-audit-logs-v2-ui-beta/">Dashboard UI</a>.</p>
<p>We recommend creating a new Logpush job for the Audit Logs v2 dataset.</p>
<p>Timelines for General Availability (GA) of Audit Logs v2 and the retirement of Audit Logs v1 will be shared in upcoming updates.</p>
<p>For more details on Audit Logs v2, refer to the <a href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>


<h2 id="audit-logs-version-2-ui-beta-release"><a href="/changelog/post/2025-07-29-audit-logs-v2-ui-beta/">Audit logs (version 2) - UI Beta Release</a></h2>
<p><em>2025-07-29</em></p>
<p>The Audit Logs v2 UI is now available to all Cloudflare customers in Beta. This release builds on the public <a href="/changelog/product/audit-logs/">Beta of the Audit Logs v2 API</a> and introduces a redesigned user interface with powerful new capabilities to make it easier to investigate account activity.</p>
<p><strong>Enabling the new UI</strong></p>
<p>To try the new user interface, go to <strong>Manage Account &gt; Audit Logs</strong>. The previous version of Audit Logs remains available and can be re-enabled at any time using the <strong>Switch back to old Audit Logs</strong> link in the banner at the top of the page.</p>
<p><strong>New Features:</strong></p>
<ul>
<li><strong>Advanced Filtering</strong>: Filter logs by actor, resource, method, and more for faster insights.</li>
<li><strong>On-hover filter controls</strong>: Easily include or exclude values in queries by hovering over fields within a log entry.</li>
<li><strong>Detailed Log Sidebar</strong>: View rich context for each log entry without leaving the main view.</li>
<li><strong>JSON Log View</strong>: Inspect the raw log data in a structured JSON format.</li>
<li><strong>Custom Time Ranges</strong>: Define your own time windows to view historical activity.</li>
<li><strong>Infinite Scroll</strong>: Seamlessly browse logs without clicking through pages.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_filters.png" alt="Audit Logs v2 new UI" /></p>
<p>For more details on Audit Logs v2, see the <a href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
<p><strong>Known issues</strong></p>
<ul>
<li>A small number of audit logs may currently be unavailable in Audit Logs v2. In some cases, certain fields such as actor information may be missing in certain audit logs. We are actively working to improve coverage and completeness for General Availability.</li>
<li>Export to CSV is not supported in the new UI.</li>
</ul>
<p>We are actively refining the Audit Logs v2 experience and welcome your feedback. You can share overall feedback by clicking the thumbs up or thumbs down icons at the top of the page, or provide feedback on specific audit log entries using the thumbs icons next to each audit log line or by filling out our <a href="https://docs.google.com/forms/d/e/1FAIpQLSfXGkJpOG1jUPEh-flJy9B13icmcdBhveFwe-X0EzQjJQnQfQ/viewform?usp=sharing">feedback form</a>.</p>


<h2 id="audit-logs-version-2-beta-release"><a href="/changelog/post/2025-03-27-automatic-audit-logs-beta-release/">Audit logs (version 2) - Beta Release</a></h2>
<p><em>2025-03-27</em></p>
<p>The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.</p>
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



