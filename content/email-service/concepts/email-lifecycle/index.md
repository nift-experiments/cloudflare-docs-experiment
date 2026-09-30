<p class="article-summary">Understand the complete email processing lifecycle from request received through final delivery status with Cloudflare Email Service
</p>
<p>The email lifecycle describes the complete journey of an email through Cloudflare Email Service. Understanding this process helps you optimize your email implementation and troubleshoot delivery issues.</p>
<p>Email Sending and Email Routing follow distinct processing pipelines. The outbound flow covers emails you send through the service; the inbound flow covers emails received on domains configured with Email Routing.</p>
<h2 id="outbound-flow-email-sending">Outbound flow (Email Sending)</h2>
<p>Every email sent through Cloudflare Email Service follows this processing pipeline:</p>
<pre><code class="language-mermaid">flowchart LR&#10;    A[Request Received] --&gt; B[&quot;Rate Limit, Authentication &amp; Suppression Check&quot;] --&gt; E[Delivery Attempt]&#10;    E --&gt; G{Success?}&#10;    G --&gt;|Yes, successfully delivered| F[Final Status &amp; Metrics]&#10;    G --&gt;|No - Soft Bounce| H[Retry with Exponential Backoff]&#10;    G --&gt;|No - Hard Bounce| F&#10;    H --&gt;|Retries remaining| E&#10;    H --&gt;|Max retries exceeded| F&#10;</code></pre>
<h3 id="stage-details">Stage details</h3>
<ol>
<li>
<p><strong>Request received:</strong> The system validates the email format, sender authorization, and message structure. Invalid requests are rejected immediately and do not proceed to the next stage.</p>
</li>
<li>
<p><strong>Rate limit check:</strong> The system checks sending <a href="/email-service/platform/limits/">limits</a> per account, domain, and recipient to prevent abuse. Requests that exceed these limits are temporarily rejected and must be retried later.</p>
</li>
<li>
<p><strong>Authentication and reputation</strong>: The system performs email authentication checks and evaluates sender reputation:</p>
<ul>
<li><strong>SPF (Sender Policy Framework)</strong>: Verifies that the sending IP address is authorized to send emails for the domain by checking DNS TXT records. This prevents domain spoofing and improves deliverability.</li>
<li><strong>DKIM (DomainKeys Identified Mail)</strong>: Validates the email's cryptographic signature to ensure message integrity and authenticate the sender domain. This builds trust with recipient servers.</li>
<li><strong>DMARC (Domain-based Message Authentication)</strong>: Applies domain owner policies for handling emails that fail SPF or DKIM checks, helping prevent phishing and brand impersonation while providing feedback reports.</li>
</ul>
<p>These authentication mechanisms work together to establish sender legitimacy and protect against email fraud. Senders with low reputation scores may experience throttling or delayed processing.</p>
</li>
<li>
<p><strong>Suppression list check:</strong> The system checks each recipient against the Email Sending <a href="/email-service/concepts/suppressions/">suppression list</a> for your account. Suppressed recipients do not reach the delivery stage or count toward your quota.</p>
<p>The per-sending-domain <a href="/email-service/configuration/domains/#drop-suppressed-recipients"><strong>Drop suppressed recipients</strong> setting</a> is off by default. When off, the REST API returns <code>400</code>, the Workers binding throws <code>E_RECIPIENT_SUPPRESSED</code>, and SMTP rejects the message if any recipient is suppressed.</p>
<p>When on, Email Service removes suppressed recipients and processes the remaining recipients. Email Service does not process unsubscribe links, so add unsubscribed recipients manually.</p>
</li>
<li>
<p><strong>Delivery attempt:</strong> The system connects to the recipient's mail server and attempts message delivery via SMTP. When delivery fails, the system applies different retry logic based on the failure type:</p>
<ul>
<li><strong>Soft bounces (4xx responses)</strong>: The system retries delivery using exponential backoff timing</li>
<li><strong>Hard bounces (5xx responses)</strong>: The system marks the email as permanently failed with no retry attempts</li>
</ul>
</li>
<li>
<p><strong>Server response handling:</strong> The system processes SMTP response codes from the recipient server to determine the final email status:</p>
<ul>
<li><strong>2xx codes</strong>: The email was delivered successfully</li>
<li><strong>4xx codes</strong>: Temporary failure occurred and the email will be retried</li>
<li><strong>5xx codes</strong>: Permanent failure occurred and the email cannot be delivered</li>
</ul>
</li>
<li>
<p><strong>Final status and metrics:</strong> Based on the server response, the system assigns emails one of these final statuses:</p>
<ul>
<li><strong>Delivered</strong>: The email was successfully accepted by the recipient server</li>
<li><strong>Delivery failed</strong>: The email permanently failed delivery (hard bounce) or exceeded the maximum retry attempts (soft bounce). This status appears as <code>deliveryFailed</code> when querying the <a href="/email-service/observability/metrics-analytics/">GraphQL Analytics API</a>.</li>
</ul>
</li>
</ol>
<h2 id="inbound-flow-email-routing">Inbound flow (Email Routing)</h2>
<p>Every email received on a domain configured with Email Routing follows this processing pipeline:</p>
<pre><code class="language-mermaid">flowchart LR&#10;    A[SMTP Receipt] --&gt; B[Authentication Check]&#10;    B --&gt; C{Authenticated?}&#10;    C --&gt;|Yes| D[Rule Match]&#10;    C --&gt;|No| R[Reject]&#10;    D --&gt; E{Action?}&#10;    E --&gt;|Send to email| F[ARC Sign &amp; SRS Rewrite]&#10;    E --&gt;|Send to Worker| W[Worker]&#10;    E --&gt;|Drop| X[Drop]&#10;    W --&gt; Y{Worker action?}&#10;    Y --&gt;|forward| F&#10;    Y --&gt;|reply| F&#10;    Y --&gt;|setReject| R&#10;    F --&gt; G[Outbound Delivery]&#10;    G --&gt; H[Final Status &amp; Metrics]&#10;</code></pre>
<h3 id="stage-details-1">Stage details</h3>
<ol>
<li><strong>SMTP receipt:</strong> A sending server connects to a Cloudflare MX server and submits the message over SMTP. Messages larger than the <a href="/email-service/platform/limits/">inbound message size limit</a> are rejected at this stage.</li>
<li><strong>Authentication check:</strong> The system performs <a href="/email-service/concepts/email-authentication/">SPF, DKIM, DMARC, and ARC</a> checks on the incoming message. Mail that fails authentication according to the sender's DMARC policy is rejected. Mail from IP addresses on a Realtime Block List is also rejected at this stage. Refer to <a href="/email-service/reference/postmaster/">Postmaster information</a> for details.</li>
<li><strong>Rule match:</strong> The system matches the recipient address against your configured <a href="/email-service/configuration/email-routing-addresses/">routing rules</a>. If <a href="/email-service/configuration/email-routing-addresses/#subaddressing">subaddressing</a> is enabled, sub-addressed recipients fall back to the base routing rule. If no rule matches and the <a href="/email-service/configuration/email-routing-addresses/#catch-all-rule">catch-all rule</a> is enabled, the catch-all rule applies.</li>
<li><strong>Action:</strong> The system applies the matched rule's action:
<ul>
<li><strong>Send to an email</strong>: The message is forwarded to the verified destination address (stage 5).</li>
<li><strong>Send to a Worker</strong>: The message is passed to your <a href="/email-service/api/route-emails/email-handler/">Worker</a>. The Worker can call <code>forward()</code>, <code>reply()</code>, or <code>setReject()</code>.</li>
<li><strong>Drop</strong>: The message is silently discarded. No further processing occurs.</li>
</ul>
</li>
<li><strong>ARC sign and SRS rewrite:</strong> For forwarded messages, the system adds an ARC seal preserving the original authentication results and rewrites the envelope sender using the <a href="/email-service/reference/postmaster/#sender-rewriting">Sender Rewriting Scheme</a>. This allows SPF to pass at the destination server.</li>
<li><strong>Outbound delivery:</strong> The system connects to the destination mail server and delivers the message. Soft bounces are retried with exponential backoff. Hard bounces are returned to the original sender in-session as upstream SMTP errors. Refer to <a href="/email-service/reference/postmaster/#smtp-errors">Postmaster: SMTP errors</a>.</li>
<li><strong>Final status and metrics:</strong> The final outcome is recorded and available through the <a href="/email-service/observability/logs/">Activity log</a> and the <a href="/email-service/observability/metrics-analytics/">GraphQL Analytics API</a>.</li>
</ol>
