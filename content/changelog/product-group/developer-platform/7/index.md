<h1 id="changelog">Changelog</h1>

<h2 id="deprecating-sandbox-sdk-features"><a href="/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/">Deprecating Sandbox SDK features</a></h2>
<p><em>2026-06-09</em></p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-06-09-deprecating-sandbox-sdk-features-sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h4>
@markup("md", "content/.markup/bodies/17752.md")</aside>
<p>Today we are announcing the deprecation of several features from the Sandbox SDK. The SDK has grown and matured substantially since it first launched. As agent workflows have developed, we have shipped many new features and experiments so developers can easily integrate secure, isolated code execution into their workflows.</p>
<p>We want the SDK to continue providing a stable foundation for agentic workflows while we iterate quickly on the codebase. These deprecated features have either been superseded by newer capabilities or seen low adoption. Do not build new work on them. Migrate using the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>, or move to the <a href="/sandbox/1-0-preview/">Sandbox SDK 1.0 preview</a> when you can.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-http-and-websocket-transports">HTTP and WebSocket transports</h4>
<p>In April 2026, we released the new RPC transport and deprecated the WebSocket transport. This setting governs how the sandbox container talks to the Workers ecosystem. The RPC transport removes the limitations of both the HTTP and WebSocket transports. As of this announcement, RPC is the recommended default. HTTP and WebSocket transports are deprecated and will not ship in future Sandbox SDK majors.</p>
<p>To migrate, update the <code>SANDBOX_TRANSPORT</code> variable to <code>rpc</code> or set the <code>transport</code> option when calling <code>getSandbox()</code>. For more information, refer to the <a href="/sandbox/configuration/transport/">transport configuration documentation</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-desktop">Desktop</h4>
<p>The desktop feature ran a full Linux desktop inside the sandbox (display server, desktop environment, and VNC/noVNC) so agents and apps could drive a GUI with screenshots, mouse, and keyboard — the same <em>computer-use</em> shape other sandbox products expose for UI automation. Adoption stayed low, and we removed it in <code>0.10.2</code>. If you need that capability again, you can build it on top of the sandbox with <a href="/sandbox/1-0-preview/extensions/">extensions</a> rather than a built-in <code>sandbox.desktop</code> API.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-expose-ports">Expose ports</h4>
<p>We recently released support for Cloudflare Tunnel in the Sandbox SDK. This provides a robust API for exposing services running in your sandbox to the public internet. It fixes issues many were facing with local development and deployment to <code>workers.dev</code> domains. To migrate from <code>exposePort()</code> to tunnels, refer to the <a href="/sandbox/api/tunnels/">tunnels API documentation</a> and the <a href="/sandbox/guides/expose-services/">expose services guide</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-default-sessions">Default sessions</h4>
<p>By default, the <code>exec()</code> method in the Sandbox SDK maintains a default session across all calls, so a <code>cd</code> in one call is honored in the next. This convenience helped developers writing <code>exec</code> statements by hand, but confused agents and caused hard-to-trace bugs. As of <code>0.10.3</code>, we have introduced the <a href="/sandbox/configuration/sandbox-options/"><code>enableDefaultSession</code></a> flag on the <code>getSandbox()</code> interface to turn this off. Default sessions as a concept — and the flag — will be removed in an upcoming release.</p>
<p>We recommend setting <code>enableDefaultSession: false</code> today and using the <a href="/sandbox/api/sessions/"><code>sandbox.createSession()</code> API</a> when you need the previous behavior.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-other-changes">Other changes</h4>
<p>We are also consolidating all APIs that buffer data to support streaming by default. This includes <a href="/sandbox/api/files/"><code>readFile</code>, <code>writeFile</code></a>, and <a href="/sandbox/api/commands/"><code>exec</code></a>. The stream equivalents will be removed.</p>
<p>We are exploring moving non-core features like the <a href="/sandbox/guides/code-execution/">code interpreter</a>, <a href="/sandbox/api/terminal/">terminal</a>, and <a href="/sandbox/guides/git-workflows/">git APIs</a> into helpers. These features will retain their existing APIs, so migration should be simple.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-next-steps">Next steps</h4>
<p>If you use any of these features on the <strong>current stable</strong> package, refer to the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>. Coding agents can use the <strong><code>sandbox-stable</code></strong> skill for stable-package work and that guide for cleanup (<a href="/agent-setup/">Agent setup</a> · <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a>).</p>
<p>If you are moving to <strong>Sandbox SDK 1.0</strong> (<code>@next</code>), use the <a href="/sandbox/1-0-preview/">1.0 preview</a> and <a href="/sandbox/1-0-preview/migrate/">Migrate</a> guides instead — or the <strong><code>sandbox-migrate-to-next</code></strong> skill after installing Cloudflare Skills. New projects should prefer <strong><code>sandbox-next</code></strong> on <code>@next</code>.</p>
<p>For any questions, ask in the <a href="https://discord.gg/cloudflaredev">Cloudflare Developers Discord</a>.</p>


<h2 id="authenticated-smtp-submission-now-available-in-beta"><a href="/changelog/post/2026-06-08-smtp-submission/">Authenticated SMTP submission now available in beta</a></h2>
<p><em>2026-06-08</em></p>
<p>You can now send emails through <strong>Cloudflare Email Service</strong> using authenticated <a href="/email-service/api/send-emails/smtp/">SMTP submission</a> on <code>smtp.mx.cloudflare.net:465</code>. SMTP joins the <a href="/email-service/api/send-emails/rest-api/">REST API</a> and the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a> as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, <code>smtplib</code>, PHPMailer, JavaMail).</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td><code>smtp.mx.cloudflare.net</code></td>
</tr>
<tr>
<td>Port</td>
<td><code>465</code> (implicit TLS)</td>
</tr>
<tr>
<td>AUTH</td>
<td><code>PLAIN</code> or <code>LOGIN</code></td>
</tr>
<tr>
<td>Username</td>
<td><code>api_token</code></td>
</tr>
<tr>
<td>Password</td>
<td>A Cloudflare API token (account-owned or user-owned) with <strong>Email Sending: Edit</strong></td>
</tr>
</tbody>
</table>
<p>Submissions enter the same delivery pipeline as the REST API and Workers binding: identical <a href="/email-service/platform/limits/">limits</a>, automatic DKIM and ARC signing, and shared dashboard logs.</p>
<p>Send your first email with a single command:</p>
<pre><code class="language-sh">curl --ssl-reqd \&#10;  &#45;-url &quot;smtps://smtp.mx.cloudflare.net:465&quot; \&#10;  &#45;-user &quot;api_token:&lt;API_TOKEN&gt;&quot; \&#10;  &#45;-mail-from &quot;welcome@yourdomain.com&quot; \&#10;  &#45;-mail-rcpt &quot;user@example.com&quot; \&#10;  &#45;-upload-file mail.txt&#10;</code></pre>
<p>Refer to the <a href="/email-service/api/send-emails/smtp/">SMTP reference</a> for authentication details, response codes, and language-specific examples.</p>


<h2 id="r2-sql-now-supports-union-intersect-except-and-select-distinct"><a href="/changelog/post/2026-06-05-union-intersect-except-select-distinct/">R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT</a></h2>
<p><em>2026-06-08</em></p>
<p><a href="/r2-sql/">R2 SQL</a> now supports set operations (<code>UNION</code>, <code>INTERSECT</code>, <code>EXCEPT</code>) and <code>SELECT DISTINCT</code>, expanding the range of analytical queries you can run directly on <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<h4 id="2026-06-05-union-intersect-except-select-distinct-set-operations">Set operations</h4>
<p>Combine the results of multiple <code>SELECT</code> statements:</p>
<ul>
<li><strong><code>UNION</code></strong> — returns all rows from both queries, removing duplicates</li>
<li><strong><code>UNION ALL</code></strong> — returns all rows from both queries, including duplicates</li>
<li><strong><code>INTERSECT</code></strong> — returns only rows that appear in both queries</li>
<li><strong><code>EXCEPT</code></strong> — returns rows from the first query that do not appear in the second</li>
</ul>
<pre><code class="language-sql">&#45;- Find zones that had either firewall blocks OR high-risk requests&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;UNION&#10;SELECT zone_id FROM my_namespace.http_requests WHERE risk_score &gt; 0.8&#10;</code></pre>
<pre><code class="language-sql">&#45;- Find zones with both firewall blocks AND high traffic&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;INTERSECT&#10;SELECT zone_id FROM my_namespace.http_requests&#10;GROUP BY zone_id&#10;HAVING COUNT(*) &gt; 10000&#10;</code></pre>
<pre><code class="language-sql">&#45;- Find enterprise zones that have not been compacted&#10;SELECT zone_id FROM my_namespace.zones WHERE plan = &#x27;enterprise&#x27;&#10;EXCEPT&#10;SELECT zone_id FROM my_namespace.compaction_history&#10;</code></pre>
<h4 id="2026-06-05-union-intersect-except-select-distinct-select-distinct">Select distinct</h4>
<p>Eliminate duplicate rows from query results:</p>
<pre><code class="language-sql">SELECT DISTINCT region, department&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 1000&#10;ORDER BY region, department&#10;LIMIT 100&#10;</code></pre>
<p>For large datasets where approximate results are acceptable, <code>approx_distinct()</code> remains a faster alternative for counting unique values.</p>
<p>For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>


<h2 id="post-meeting-transcriptions-are-now-generally-available-in-realtimekit"><a href="/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/">Post-meeting transcriptions are now Generally Available in RealtimeKit</a></h2>
<p><em>2026-06-08</em></p>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> lets you build products where people meet over live audio and video — such as HealthTech, EdTech, proctoring, and other real-time platforms — on Cloudflare's <a href="/realtime/sfu/calls-vs-sfus/">global WebRTC infrastructure</a>.</p>
<p><a href="/realtime/realtimekit/ai/transcription/#post-meeting-transcription">Post-meeting transcription</a> is now Generally Available, so completed RealtimeKit meetings can automatically produce full transcript files after they end. Those transcripts can also power <a href="/realtime/realtimekit/ai/summary/">AI-generated summaries</a> for meeting notes, review workflows, and follow-up tasks after the transcript is available.</p>
<p>Post-meeting transcription is a managed service powered by <a href="/workers-ai/">Workers AI</a> using <a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper Large v3 Turbo</a>. RealtimeKit handles transcription processing and can return transcript and summary files through <a href="/realtime/realtimekit/webhooks/">webhooks</a> or the REST API, so you do not need to run your own transcription infrastructure.</p>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-generate-transcripts-and-summaries">Generate transcripts and summaries</h4>
<p>To generate a transcript after a meeting ends, set <code>transcribe_on_end: true</code> when <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a>. To also generate an AI summary automatically after the transcript is available, set <code>summarize_on_end: true</code>:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;title&quot;: &quot;Weekly product review&quot;,&#10;    &quot;transcribe_on_end&quot;: true,&#10;    &quot;summarize_on_end&quot;: true,&#10;    &quot;ai_config&quot;: {&#10;      &quot;transcription&quot;: {&#10;        &quot;language&quot;: &quot;en&quot;&#10;      },&#10;      &quot;summarization&quot;: {&#10;        &quot;word_limit&quot;: 500,&#10;        &quot;text_format&quot;: &quot;markdown&quot;,&#10;        &quot;summary_type&quot;: &quot;team_meeting&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-consume-results">Consume results</h4>
<p>When RealtimeKit finishes processing a meeting, it creates download URLs for the transcript and, if <code>summarize_on_end</code> is set, the summary. You can receive those URLs automatically with <a href="/realtime/realtimekit/webhooks/">webhooks</a>, or fetch them later for a specific session with the <a href="/realtime/realtimekit/ai/summary/#rest-api">REST API</a>.</p>
<p>To receive results as soon as they are ready, configure the <code>meeting.transcript</code> and <code>meeting.summary</code> webhook events:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;name&quot;: &quot;AI results webhook&quot;,&#10;    &quot;url&quot;: &quot;https://example.com/webhook&quot;,&#10;    &quot;events&quot;: [&quot;meeting.transcript&quot;, &quot;meeting.summary&quot;],&#10;    &quot;enabled&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>To fetch results later, call the <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/">transcript</a> or <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/">summary</a> endpoint for the session:</p>
<pre><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Use the <a href="/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/">Generate summary of transcripts for the session</a> API only if <code>summarize_on_end</code> was not set and you want to generate a summary manually after the transcript is available:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Post-meeting transcription supports <a href="/realtime/realtimekit/ai/transcription/#output-formats">CSV, JSON, SRT, and VTT transcript outputs</a>, <a href="/realtime/realtimekit/ai/transcription/#post-meeting-supported-languages">automatic language detection and Whisper language codes</a>. RealtimeKit also supports <a href="/realtime/realtimekit/ai/transcription/#real-time-transcription">real-time transcription</a> with <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> for live captions, in-meeting accessibility, and real-time note-taking.</p>
<p>Learn more in the <a href="/realtime/realtimekit/ai/transcription/">RealtimeKit transcription docs</a> and <a href="/realtime/realtimekit/ai/summary/">summary docs</a>.</p>


<h2 id="rollback-support-now-available-in-workflows"><a href="/changelog/post/2026-06-05-saga-rollbacks/">Rollback support now available in Workflows</a></h2>
<p><em>2026-06-05 15:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> now supports saga-style rollbacks,  allowing you to add compensating logic to each <code>step.do()</code> in case of downstream failures. If the instance fails, the rollback handlers will execute in reverse <code>step-start</code> order.</p>
<p>This is useful for multi-step operations that touch external systems, such as inventory reservations, payment authorization, ticket creation, or infrastructure provisioning. Instead of writing all cleanup logic in a top-level <code>catch</code>, you can keep each compensating action next to the step it undoes.</p>
<p>Rollback handlers support their own retry and timeout configuration, and Workflows now exposes rollback outcomes in instance status responses. Workflows analytics also emits rollback lifecycle events, making it easier to distinguish a forward execution failure from a rollback failure when debugging production workflows.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17832.md")</div>
<p>Refer to <a href="/workflows/build/workers-api/#rollback-options">rollback options</a> to learn more.</p>


<h2 id="control-ai-costs-with-spend-limits"><a href="/changelog/post/2026-06-05-spend-limits/">Control AI costs with spend limits</a></h2>
<p><em>2026-06-05</em></p>
<p>AI Gateway now supports spend limits — cost-based budgets that track cumulative dollar spend and block requests when the budget is exceeded. Unlike rate limiting, which caps the number of requests, spend limits track actual cost based on token usage and model pricing.</p>
<p>You can scope limits by model, provider, or custom metadata dimensions. For example, give each user a $200/day budget, cap total gateway spend at $10,000/day, or limit a specific model to $50/day per user. Each rule uses a configurable time window with fixed or sliding enforcement.</p>
<p>Spend limits work with both <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> and <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a> requests for models with known pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/spend-limits/">Spend limits documentation</a>.</p>


<h2 id="filter-workers-public-internet-traffic-using-gateway-policies"><a href="/changelog/post/2026-06-05-gateway-egress/">Filter Workers' public Internet traffic using Gateway policies</a></h2>
<p><em>2026-06-05</em></p>
<p>Workers using a <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> binding with <code>network_id: &quot;cf1:network&quot;</code> now egress to public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.</p>
<div class="nb-interactive-component" data-cf-component="WorkersVPCEgressDiagram"></div>
<p>What you get by default:</p>
<ul>
<li><strong>Visibility.</strong> Worker egress shows up in Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> logs alongside your other traffic, so you can audit what your Workers are calling and when.</li>
<li><strong>Enforcement.</strong> Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17825.md")</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17826.md")</div>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>. For policy authoring, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway traffic policies</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="pipeline-binding-configuration-field-renamed-to-stream"><a href="/changelog/post/2026-05-27-pipeline-binding-stream-field/">Pipeline binding configuration field renamed to stream</a></h2>
<p><em>2026-06-04</em></p>
<p>The <code>pipeline</code> field inside the <code>pipelines</code> binding configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> has been renamed to <code>stream</code>. The old field is deprecated but still accepted.</p>
<p>Update your configuration to use <code>stream</code> to avoid the deprecation warning.</p>
<p><strong>Before (deprecated):</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17739.md")</div>
<p><strong>After:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17740.md")</div>
<p>No other changes are required. The binding name, TypeScript types, and runtime API (<code>env.MY_PIPELINE.send(...)</code>) remain the same.</p>
<p>For more information on configuring pipeline bindings, refer to <a href="/pipelines/streams/writing-to-streams/#configure-pipeline-binding">Writing to streams</a>.</p>


<h2 id="new-workers-bulk-secrets-api-endpoint"><a href="/changelog/post/2026-06-03-bulk-secrets-api/">New Workers bulk secrets API endpoint</a></h2>
<p><em>2026-06-03</em></p>
<p>You can now create, update, or delete multiple secrets for your Worker in a single request using the <a href="/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/">bulk secrets endpoint</a>.</p>
<ul>
<li>Include a secret with a value to create or update.</li>
<li>Set a secret to <code>null</code> to delete.</li>
<li>Secrets not included in the request are left unchanged.</li>
</ul>
<p>The following example creates <code>API_KEY</code>, updates the already existing <code>DB_PASSWORD</code>, and deletes <code>OLD_SECRET</code>:</p>
<pre><code class="language-json">{&#10;  &quot;secrets&quot;: {&#10;    &quot;API_KEY&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;API_KEY&quot;, &quot;text&quot;: &quot;my-api-key&quot; },&#10;    &quot;DB_PASSWORD&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;DB_PASSWORD&quot;, &quot;text&quot;: &quot;my-db-password&quot; },&#10;    &quot;OLD_SECRET&quot;: null&#10;  }&#10;}&#10;</code></pre>
<p>You can do the same from the command line using <a href="/workers/wrangler/commands/workers/#secret-bulk"><code>wrangler secret bulk</code></a>:</p>
<pre><code class="language-sh">npx wrangler secret bulk &lt; secrets.json&#10;</code></pre>
<p>To delete a key, set its value to <code>null</code> in the JSON file. Deletion is not supported with <code>.env</code> files.</p>
<p>Each request supports up to <strong>100 total operations</strong> (creates, updates, and deletes combined).</p>


<h2 id="store-wrangler-s-oauth-credentials-in-your-os-keychain"><a href="/changelog/post/2026-06-03-wrangler-keyring-credential-storage/">Store Wrangler's OAuth credentials in your OS keychain</a></h2>
<p><em>2026-06-03</em></p>
<p><a href="/workers/wrangler/">Wrangler</a> can now store the OAuth credentials returned by <code>wrangler login</code> in an <a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">AES-256-GCM</a>-encrypted file, with the encryption key held in your operating system keychain. The default behavior is unchanged — credentials still live in a plaintext TOML file unless you opt in.</p>
<p>To opt in, run:</p>
<pre><code class="language-sh">npx wrangler login --use-keyring&#10;</code></pre>
<p>The choice is persisted across Wrangler invocations. Opt back out with <code>npx wrangler login --no-use-keyring</code>, or override the preference for a single command with the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
<p><code>wrangler whoami</code> now reports where credentials are stored:</p>
<pre><code class="language-sh">🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)&#10;</code></pre>
<p>Per-platform backends:</p>
<ul>
<li><strong>macOS</strong> uses the built-in Keychain via <code>/usr/bin/security</code>.</li>
<li><strong>Linux</strong> uses <a href="https://wiki.gnome.org/Projects/Libsecret">libsecret</a> via the <code>secret-tool</code> CLI from the <code>libsecret-tools</code> package.</li>
<li><strong>Windows</strong> uses Credential Manager via <a href="https://www.npmjs.com/package/@napi-rs/keyring"><code>@napi-rs/keyring</code></a>, installed on-demand the first time you opt in.</li>
</ul>
<p>Refer to <a href="/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</a> for the full details, including the migration behavior on opt-in/opt-out and the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>


<h2 id="schedule-workflow-instances-directly-from-your-workflow-binding"><a href="/changelog/post/2026-06-02-cron-workflows/">Schedule Workflow instances directly from your Workflow binding</a></h2>
<p><em>2026-06-02 15:00:00 UTC</em></p>
<p>You can now attach cron schedules directly to a Workflow binding in <code>wrangler.jsonc</code>. Each scheduled run creates a new Workflow instance automatically, so you do not need to define a separate Worker with a <code>scheduled</code> handler just to trigger your Workflow on an interval.</p>
<p>For example, you can configure hourly, every-15-minute, or weekday schedules on the same Workflow:</p>
<pre><code class="language-jsonc">{&#10;	&quot;workflows&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;my-scheduled-workflow&quot;,&#10;			&quot;binding&quot;: &quot;MY_WORKFLOW&quot;,&#10;			&quot;class_name&quot;: &quot;MyScheduledWorkflow&quot;,&#10;			&quot;schedules&quot;: [&quot;0 * * * *&quot;, &quot;*/15 * * * *&quot;, &quot;0 9 * * MON-FRI&quot;],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>Cron workloads get all the same benefits of Workflows with built-in retries, multi-step durable execution, and configurable timeouts of Workflows.</p>
<pre><code class="language-ts">import {&#10;	WorkflowEntrypoint,&#10;	WorkflowEvent,&#10;	WorkflowStep,&#10;} from &quot;cloudflare:workers&quot;;&#10;&#10;// Runs automatically on each cron schedule defined for the MY_WORKFLOW binding in wrangler.jsonc.&#10;export class MyScheduledWorkflow extends WorkflowEntrypoint&lt;Env&gt; {&#10;	async run(event: WorkflowEvent, step: WorkflowStep) {&#10;		const data = await step.do(&quot;fetch source data&quot;, async () =&gt; {&#10;			return await fetchSourceData();&#10;		});&#10;&#10;		// If this step fails, only this step is retried with the custom logic below&#10;		await step.do(&#10;			&quot;process and store results&quot;,&#10;			{&#10;				retries: { limit: 5, delay: &quot;30 seconds&quot;, backoff: &quot;exponential&quot; },&#10;				timeout: &quot;10 minutes&quot;,&#10;			},&#10;			async () =&gt; {&#10;				await processAndStore(data);&#10;			},&#10;		);&#10;	}&#10;}&#10;</code></pre>
<p>This makes it easier to build recurring, scheduled jobs such as database backups, invoice generation, report aggregation, and cleanup tasks without wiring up a separate Cron Trigger entrypoint.</p>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/">Trigger Workflows</a>.</p>


<h2 id="agents-sdk-v0-14-0-agent-skills-messengers-scheduled-tasks-workflows-and-hardened-chat-recovery"><a href="/changelog/post/2026-06-02-agents-sdk-v0.14.0/">Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery</a></h2>
<p><em>2026-06-02</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds four new ways to build with <code>@cloudflare/think</code>: on-demand Agent Skills, chat messengers (starting with Telegram), declarative scheduled tasks, and durable reasoning steps inside Workflows. This release also significantly hardens durable chat recovery, so turns reliably ride through deploys, evictions, and stalled model streams in production.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-agent-skills-experimental">Agent Skills (experimental)</h4>
<p>Give an agent a catalog of on-demand instructions, resources, and scripts. A skill source adds a catalog to the system prompt, and the model activates a skill only when a task matches — so a large library of capabilities does not bloat every prompt.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17667.md")</div>
<p>The <code>agents:skills</code> import bundles a local <code>./skills</code> directory through the Agents Vite plugin (one directory per skill, each with a <code>SKILL.md</code>). Skills can also load from R2 or a manifest. When skills are available, Think exposes <code>activate_skill</code>, <code>read_skill_resource</code>, and an optional <code>run_skill_script</code> tool. Skill loading is resilient: a duplicate or failing source is skipped with a warning instead of breaking the agent.</p>
<p>Agent Skills are <strong>experimental</strong>, and script execution in particular is early. The API may change in a future release. We would love your feedback — tell us what you are building and what is missing in the <a href="https://github.com/cloudflare/agents/discussions">Agents repository</a>.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-messengers">Messengers</h4>
<p>Connect a Think agent directly to a chat platform. Think owns the webhook route, conversation routing, durable reply fiber, and streamed delivery back to the provider. Telegram ships as the first provider.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17668.md")</div>
<p>Each Chat SDK thread maps to its own Think sub-agent by default, so group chats and direct messages do not share memory. Multiple bots, custom conversation routing, and custom providers are all supported.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-scheduled-tasks">Scheduled tasks</h4>
<p>Declare recurring, timezone-aware prompts and handlers with a typed domain-specific language (DSL). Think reconciles the declarations on startup and re-arms the next occurrence after each run, backed by durable idempotent submissions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17669.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-think-workflows">Think Workflows</h4>
<p>Run a model-driven reasoning step inside a Cloudflare Workflow with <code>ThinkWorkflow</code> and <code>step.prompt()</code>, with durable typed structured output, long waits, and approval gates.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17670.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-production-hardening-for-durable-chat-recovery">Production hardening for durable chat recovery</h4>
<p>Durable chat turns have always been designed to survive a mid-turn deploy or Durable Object eviction. This release is a major hardening pass on that machinery for production.</p>
<ul>
<li><strong>Better recovery during deploys.</strong> Turns now ride through continuous deploys and evictions without losing completed work or re-running tools that already ran.</li>
<li><strong>A live &quot;recovering…&quot; signal.</strong> <code>useAgentChat</code> exposes a new <code>isRecovering</code> flag, so a recovering turn shows progress instead of looking frozen. Most UIs render <code>isStreaming || isRecovering</code> as &quot;busy&quot;.</li>
<li><strong>Stalled streams recover.</strong> Set <code>chatStreamStallTimeoutMs</code> to route a hung provider stream into the same recovery path instead of leaving an infinite spinner.</li>
<li><strong>Sub-agents re-attach.</strong> On parent recovery, an in-flight <code>agentTool()</code> child is re-attached to its result rather than abandoned and re-run, so long-running children no longer lose work under deploys.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-mcp-transport-improvements">MCP transport improvements</h4>
<ul>
<li><strong>Resumable streams</strong> — In-flight tool calls over Server-Sent Events (SSE) survive a dropped connection. Clients reconnect with <code>Last-Event-ID</code> and replay anything they missed.</li>
<li><strong>Readable server IDs</strong> — <code>addMcpServer</code> accepts an optional <code>id</code>, so tools surface as readable keys (for example <code>tool_github_create_pull_request</code>) instead of opaque connection IDs.</li>
<li><strong>Better handling of concurrent requests</strong> — Overlapping JSON-RPC requests are now correctly correlated to their responses across the HTTP and RPC transports.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Compaction</strong> — A <code>Session</code>'s <code>tokenCounter</code> now also drives the compaction boundary decision (&quot;what to compress&quot;), not just the fire/no-fire trigger.</li>
<li><strong><code>@cloudflare/worker-bundler</code></strong> — Adds a <code>virtualModules</code> option to <code>createWorker</code> to provide in-memory module source during bundling.</li>
<li><strong>Client-tool continuations</strong> — Parallel tool results now coalesce into a single continuation, immediate resume requests attach to the pending continuation, and server-side <code>needsApproval</code> continuations resume reliably after approval.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>


<h2 id="share-sandbox-previews-through-cloudflare-tunnel"><a href="/changelog/post/2026-05-29-sandbox-named-tunnels/">Share sandbox previews through Cloudflare Tunnel</a></h2>
<p><em>2026-05-29</em></p>
<p><a href="/sandbox/">Sandboxes</a> can expose a service running inside the container on a public preview URL through the <code>sandbox.tunnels</code> namespace. The SDK uses <code>cloudflared</code> inside the sandbox so you can share a running service without configuring <code>exposePort()</code> or a custom domain.</p>
<p>By default, <code>sandbox.tunnels.get(port)</code> creates a <a href="https://try.cloudflare.com/">quick tunnel</a> on a zero-config <code>*.trycloudflare.com</code> URL — no Cloudflare account, DNS record, or custom domain required. This is perfect for quick development and for <code>.workers.dev</code> deployments.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17665.md")</div>
<h4 id="2026-05-29-sandbox-named-tunnels-named-tunnels">Named tunnels</h4>
<p>For more control you can create a named tunnel through <code>sandbox.tunnels.get(port, { name })</code>. A named tunnel binds a hostname (<code>&lt;name&gt;.&lt;your-zone&gt;</code>) backed by a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and a CNAME record on your zone resulting in something like <a href="https://my-app-preview.example.com">https://my-app-preview.example.com</a>.</p>
<p>Unlike quick tunnels, which generate a new random URL each time, a named tunnel produces a persistent URL that survives container restarts. This makes named tunnels suitable for production use cases where you want control over the tunnel and it's origin.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17666.md")</div>
<p>Calling <code>sandbox.destroy()</code> tears down the Cloudflare Tunnel and the associated DNS record alongside the container, so you do not leave dangling tunnels or records behind.</p>
<h4 id="2026-05-29-sandbox-named-tunnels-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For full API details, refer to the <a href="/sandbox/api/tunnels/">Sandbox tunnels reference</a>.</p>


<h2 id="d1-migrations-support-nested-layouts-via-migrations-pattern"><a href="/changelog/post/2026-06-04-migrations-pattern/">D1 migrations support nested layouts via `migrations_pattern`</a></h2>
<p><em>2026-05-29</em></p>
<p>You can now point <code>wrangler d1 migrations apply</code> at a nested migrations layout — such as the one produced by <a href="https://orm.drizzle.team/">Drizzle</a> (<code>migrations/0001_init/migration.sql</code>) — using the new <code>migrations_pattern</code> D1 binding config:</p>
<pre><code class="language-jsonc">{&#10;	&quot;d1_databases&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;DB&quot;,&#10;			&quot;database_name&quot;: &quot;my-database&quot;,&#10;			&quot;database_id&quot;: &quot;&lt;UUID&gt;&quot;,&#10;			&quot;migrations_dir&quot;: &quot;migrations&quot;,&#10;			&quot;migrations_pattern&quot;: &quot;migrations/*/migration.sql&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p><code>migrations_pattern</code> is a glob (relative to your Wrangler config file) used to discover migration files. It defaults to <code>${migrations_dir}/*.sql</code>, so existing projects keep working unchanged. Each migration's name is recorded in the migrations table as a path relative to <code>migrations_dir</code>.</p>
<p>To learn more, visit D1's <a href="/d1/reference/migrations/#nested-migration-layouts">migrations documentation</a>.</p>


<h2 id="cloudflare-s-realtime-websocket-adapter-now-auto-reconnects-and-buffers-webrtc-media"><a href="/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/">Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media</a></h2>
<p><em>2026-05-29</em></p>
<p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC Selective Forwarding Unit that runs on Cloudflare's global network</a>, so you can route live audio, video, and data between WebRTC clients around the world without managing SFU infrastructure or regions.</p>
<p>When you use the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> to stream WebRTC media to a WebSocket endpoint, the adapter now auto-reconnects and buffers audio and video after brief endpoint disconnects or restarts.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-streaming-webrtc-media-to-websocket-endpoints">Streaming WebRTC media to WebSocket endpoints</h4>
<p>Many teams also use Realtime SFU as the media layer for backend applications, such as transcription, recording, note-taking, and agentic media-processing services. These systems often need to consume live WebRTC audio or video from the SFU in backend infrastructure, including <a href="/durable-objects/">Durable Objects</a>, <a href="/workers/">Workers</a>, <a href="/containers/">Containers</a>, or external services, without running a WebRTC client themselves.</p>
<p>The <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> bridges that gap by streaming WebRTC media from the SFU to a standard WebSocket endpoint as application-consumable payloads: <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-formats">PCM audio frames and JPEG video frames</a>.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-what-changed">What changed</h4>
<p>When you use the WebSocket adapter in <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#stream-mode-egress">Stream mode (egress)</a> to send live audio or video from the SFU to your own WebSocket endpoint, the SFU now <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">automatically reconnects</a> after brief endpoint disconnects or restarts. This is especially helpful for long-running media pipelines where the WebSocket endpoint may briefly restart while a recording, transcription, or live analysis job is still in progress.</p>
<p>Previously, a brief disconnect from your WebSocket endpoint could close the adapter and require your application to recreate it before media could resume. Now, the SFU retries the same endpoint for up to 5 seconds with no API change required. If the endpoint comes back within that window, audio and video delivery resumes automatically.</p>
<p>The reconnect behavior also includes <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-buffering-during-reconnect">live-first media buffering</a>, so brief interruptions reduce media loss without replaying stale video.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-reconnect-behavior">Reconnect behavior</h4>
<p>During reconnect:</p>
<ul>
<li>Audio uses a short bounded backlog to reduce audible loss. If the interruption lasts longer than the backlog can cover, older audio may be dropped.</li>
<li>Video resumes from the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#video-jpeg">latest available JPEG frame</a> instead of replaying stale frames.</li>
<li>Recovery is best effort and does not guarantee gapless or exactly-once delivery.</li>
</ul>
<p>If the endpoint remains unavailable after the 5-second reconnect window, the adapter closes and must be recreated.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-learn-more">Learn more</h4>
<ul>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a></li>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">Automatic reconnection for streaming</a></li>
<li><a href="/realtime/sfu/get-started/">Get started with Realtime SFU</a></li>
<li><a href="/realtime/sfu/example-architecture/">Realtime SFU example architecture</a></li>
<li><a href="/realtime/sfu/calls-vs-sfus/">Realtime vs Regular SFUs</a></li>
<li><a href="https://realtime-sfu.dev-demos.workers.dev/">Global SFU Network Visualization</a></li>
</ul>


<h2 id="use-browser-run-quick-actions-directly-from-workers"><a href="/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/">Use Browser Run Quick Actions directly from Workers</a></h2>
<p><em>2026-05-28</em></p>
<p>You can now call <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a> directly from a <a href="/workers/">Cloudflare Worker</a> using the <code>quickAction()</code> method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.</p>
<p>With the <code>quickAction()</code> method you can:</p>
<ul>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">Capture screenshots</a> from URLs or HTML</li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">Generate PDFs</a> with custom styling, headers, and footers</li>
<li><a href="/browser-run/quick-actions/content-endpoint/">Extract HTML content</a> from fully rendered pages</li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">Convert pages to Markdown</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">Extract structured JSON</a> using AI</li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">Scrape elements</a> with CSS selectors</li>
<li><a href="/browser-run/quick-actions/links-endpoint/">Get all links</a> from a page</li>
<li><a href="/browser-run/quick-actions/snapshot/">Capture snapshots</a> (HTML + screenshot in one request)</li>
</ul>
<p>To get started, add a browser binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17694.md")</div>
<p>Then call any Quick Action directly from your Worker. For example, to capture a screenshot:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17695.md")</div>
<p>The <code>quickAction()</code> method requires a compatibility date of <code>2026-03-24</code> or later.</p>
<p>For setup instructions and the full list of available actions, refer to <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a>.</p>


<h2 id="wrangler-supports-ssh-proxycommand-for-containers"><a href="/changelog/post/2026-05-28-ssh-proxy-command/">Wrangler supports SSH ProxyCommand for Containers</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/workers/wrangler/">Wrangler</a> supports using <code>wrangler containers ssh</code> as an OpenSSH <code>ProxyCommand</code> for <a href="/containers/">Containers</a>. This lets your local SSH client connect to a running Container through Wrangler.</p>
<pre><code class="language-sh">ssh -o ProxyCommand=&quot;wrangler containers ssh %h&quot; cloudchamber@&lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>When standard input and output are piped, Wrangler forwards data to the SSH server in the Container. You can also pass <code>--stdio</code> to force this mode.</p>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>


<h2 id="send-emails-with-named-recipient-addresses"><a href="/changelog/post/2026-05-28-named-email-recipients/">Send emails with named recipient addresses</a></h2>
<p><em>2026-05-28</em></p>
<p>You can now send emails with display names on recipient addresses in addition to the existing <code>from</code> support. Pass an object with <code>email</code> and an optional <code>name</code> field for <code>to</code>, <code>cc</code>, <code>bcc</code>, <code>replyTo</code>, or <code>from</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17723.md")</div>
<p>Plain strings remain fully supported for backward compatibility, and you can mix strings and named objects in the same array.</p>
<p>Refer to the <a href="/email-service/api/send-emails/workers-api/">Workers API</a> and <a href="/email-service/api/send-emails/rest-api/">REST API</a> documentation for full request examples.</p>


<h2 id="pipelines-pricing-announced"><a href="/changelog/post/2026-05-11-pipelines-pricing-announced/">Pipelines pricing announced</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/pipelines/">Cloudflare Pipelines</a> is a streaming data platform that ingests events, transforms them with SQL, and writes to <a href="/r2/">R2</a> as JSON, Parquet, or <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables. Pipelines now has published pricing based on two usage dimensions: the volume of data processed by SQL transforms and the volume of data delivered to sinks. Ingress into a Pipeline stream is free.</p>
<p><strong>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for Pipelines usage.</strong></p>
<p>Pipelines pricing model is designed to charge per GB based on what you use:</p>
<ul>
<li><strong>Streams (ingress)</strong>: Free, regardless of volume.</li>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks</strong>: $0.03 / GB for JSON, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Free plans include 1 GB / month for each dimension. Workers Paid plans include 50 GB / month.</p>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>


<h2 id="r2-data-catalog-pricing-announced"><a href="/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/">R2 Data Catalog pricing announced</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into R2 buckets, queryable by any Iceberg-compatible engine such as Spark, Snowflake, and DuckDB. R2 Data Catalog now has published pricing for catalog operations and table compaction, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>.</p>
<p>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 Data Catalog usage.</p>
<p>Pricing is based on two dimensions:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when automatic compaction is turned on for a table.</li>
</ul>
<p>Both dimensions include a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>


<h2 id="r2-data-catalog-gets-a-dedicated-dashboard-experience"><a href="/changelog/post/2026-05-28-r2-data-catalog-dashboard/">R2 Data Catalog gets a dedicated dashboard experience</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into your R2 bucket. It exposes a standard Iceberg REST catalog interface so you can connect query engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>, and <a href="/r2-sql/">R2 SQL</a> to your data in R2.</p>
<p>R2 Data Catalog now has a dedicated section in the Cloudflare dashboard, replacing the previous settings panel embedded in R2 bucket configuration. The new experience includes:</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-dashboard.png" alt="R2 Data Catalog dashboard overview" /></p>
<ul>
<li><strong>Catalog overview</strong> — View all your catalogs in one place with catalog request counts, bucket sizes, and table maintenance status at a glance.</li>
<li><strong>Guided setup wizard</strong> — Create a catalog in three steps: choose or create an R2 bucket, configure table maintenance (compaction and snapshot expiration), and review. The wizard creates the bucket and generates a service credential automatically.</li>
<li><strong>Settings management</strong> — A dedicated settings page for each catalog with sections for general configuration, table maintenance, service credentials, and disabling the catalog. You can now enable and configure <a href="/r2-data-catalog/table-maintenance/">snapshot expiration</a> directly from the dashboard.</li>
<li><strong>Built-in metrics</strong> — Five charts on each catalog's metrics tab: bytes compacted, files compacted, catalog requests, storage size, and snapshots expired.</li>
</ul>
<p>To get started, go to <strong>R2 Data Catalog</strong> in the Cloudflare dashboard or refer to the <a href="/r2-data-catalog/get-started/">getting started guide</a> and <a href="/r2-data-catalog/manage-catalogs/">manage catalogs documentation</a>.</p>


<h2 id="r2-sql-pricing-announced"><a href="/changelog/post/2026-05-11-r2-sql-pricing-announced/">R2 SQL pricing announced</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/r2-sql/">R2 SQL</a> is a serverless, distributed query engine that runs SQL against <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL now has published pricing based on a single dimension: the volume of compressed data scanned to execute your queries. At $2.50 / TB ($0.0025 / GB), R2 SQL is priced at half the cost of AWS Athena and less than half of Google BigQuery on-demand.</p>
<p>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 SQL usage.</p>
<p>Data scanned is measured on compressed bytes read from R2 object storage. This matches what you see in your R2 bucket — if a Parquet file is 100 MB on disk, scanning that file bills for 100 MB. Each query has a minimum billing increment of 10 MB.</p>
<p>All plans include 10 GB of data scanned per month. Standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply separately.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-sql/platform/pricing/">R2 SQL pricing</a>.</p>


<h2 id="record-specific-participant-audio-tracks-in-realtimekit"><a href="/changelog/post/2026-05-28-realtimekit-track-recording/">Record specific participant audio tracks in RealtimeKit</a></h2>
<p><em>2026-05-28</em></p>
<p>You can now record specific participant audio tracks in RealtimeKit with <a href="/realtime/realtimekit/recording-guide/track-recording/">track recording</a>. Track recording creates separate WebM files for each participant instead of a single composite recording, which is useful for post-processing, transcription, and regulated or content-sensitive workflows.</p>
<p>To record specific participants, pass <code>user_ids</code> when starting a track recording:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/track \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;  &quot;user_ids&quot;: [&quot;user-123&quot;, &quot;user-456&quot;]&#10;}&#x27;&#10;</code></pre>
<p>To pass <code>user_ids</code> for selective track recording, use the following minimum SDK versions:</p>
<ul>
<li>Web Core: <code>@cloudflare/realtimekit</code> version <code>1.4.0</code> or later</li>
<li>Web UI Kit: <code>@cloudflare/realtimekit-ui</code>, <code>@cloudflare/realtimekit-react-ui</code>, or <code>@cloudflare/realtimekit-angular-ui</code> version <code>1.1.2</code> or later</li>
<li>Android Core or iOS Core: version <code>2.0.0</code> or later</li>
<li>Android UI Kit or iOS UI Kit: version <code>1.1.0</code> or later</li>
</ul>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> provides SDKs and UI components so that you can build your own meeting experience on Cloudflare's <a href="/realtime/#realtime-sfu">global WebRTC infrastructure</a>. Teams today build products ranging from telehealth to education on RealtimeKit for global audiences. You can get started today with our <a href="/realtime/realtimekit/quickstart/">Quickstart</a> or take a look at our <a href="https://github.com/cloudflare/meet">Cloudflare Meet repo</a> as a reference.</p>


<h2 id="transformation-flows-in-images"><a href="/changelog/post/2026-05-27-transformation-flows/">Transformation flows in Images</a></h2>
<p><em>2026-05-27</em></p>
<p><img src="/assets/upstream/images/images/custom-flow.png" alt="Custom flow configuration panel" /></p>
<p>Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.</p>
<p>There are two modes for transformation flows:</p>
<ul>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-provider-flow">Provider flows</a></strong> — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.</li>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-custom-flow">Custom flows</a></strong> — Define your own conditions and actions for use cases like automatic format conversion, <a href="/images/optimization/make-responsive-images/#using-widthauto">responsive sizing</a> with <code>width=auto</code>, or directory-based optimization.</li>
</ul>
<p>To get started, go to <strong>Images</strong> &gt; <strong>Transformations</strong> &gt; <strong>Automation</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>.</p>
<p>Learn more about <a href="/images/optimization/transformations/flows/">transformation flows</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/6/">Previous</a><span>Page 7 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/8/">Next</a></nav>
