---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/actions/
  description: Server-side Think tools with idempotency, human approvals, authorization, and reply attachments.
  full_title: Actions · Cloudflare Agents docs
  head_html: <title>Actions · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Server-side Think tools with idempotency, human approvals, authorization, and reply attachments."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/actions/index.md"><meta property="og:title" content="Actions · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Server-side Think tools with idempotency, human approvals, authorization, and reply attachments."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/actions/#page","headline":"Actions \u00b7 Cloudflare Agents docs","description":"Server-side Think tools with idempotency, human approvals, authorization, and reply attachments.","url":"https://developers.cloudflare.com/agents/harnesses/think/actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/actions/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="experimental">Experimental</h3>
@markup("md", "content/.markup/bodies/2180.md")
</aside>
<p>Actions are server-side tools with batteries included. Where a plain AI SDK <code>tool()</code> is just a description, a schema, and an <code>execute</code> function, an <code>action()</code> adds the things that are tedious and dangerous to get right by hand for a tool that has real side effects:</p>
<ul>
<li><strong>Idempotency</strong> — a durable ledger replays a settled result by a stable key instead of re-running the side effect on a recovery retry.</li>
<li><strong>Approvals</strong> — gate a call behind a human, either inline (the turn waits) or durably (the turn parks and resumes later, even from a dashboard with no live socket).</li>
<li><strong>Authorization</strong> — declare the permissions a call requires and grant them per-turn.</li>
<li><strong>Reply attachments</strong> — record advisory delivery metadata (a drafted email, a card, a voice note) without changing what the model sees.</li>
</ul>
<p>Actions compile into Think tools, so the model calls them exactly like any other tool. Return them from <code>getActions()</code>; Think merges them into the tool set alongside <code>getTools()</code>, workspace tools, extensions, and MCP tools.</p>
<h2 id="define-an-action">Define an action</h2>
<p>Use the <code>action()</code> descriptor factory and return a map of actions from <code>getActions()</code>. The map key is the tool name the model sees (unless you set <code>name</code>). The <code>execute</code> input type is inferred from <code>inputSchema</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2181.md")
</div>
<p>The <code>execute</code> callback receives the validated input and an <code>ActionContext</code>:</p>
<pre tabindex="0"><code class="language-ts">type ActionContext = {&#10;	agent: Think;&#10;	env: Cloudflare.Env;&#10;	requestId: string;&#10;	toolCallId: string;&#10;	messages: ReadonlyArray&lt;ModelMessage&gt;;&#10;	signal: AbortSignal; // aborts on turn cancel or after `timeoutMs`&#10;	attachReply(attachment: ReplyAttachment): void;&#10;};&#10;</code></pre>
<p>The action output is normalized to JSON and truncated before it is shown to the model (long outputs are capped). Anything thrown from <code>execute</code> becomes a structured <code>{ error: { name, message } }</code> tool result rather than crashing the turn. Each action has a default timeout of 30 seconds; override it per action with <code>timeoutMs</code>.</p>
<h3 id="actions-versus-plain-tools">Actions versus plain tools</h3>
<p>A plain <code>tool()</code> from <code>getTools()</code> still works and is the right choice for a read-only or trivial tool. Reach for <code>action()</code> when a tool has side effects you must not run twice, needs human approval, or needs declarative authorization — the ledger, approval descriptors, default timeout, and structured error mapping only apply to actions.</p>
<h2 id="idempotency-and-the-action-ledger">Idempotency and the action ledger</h2>
<p>When an action declares an <code>idempotencyKey</code>, Think records the settled result in a durable ledger keyed by <code>action:&lt;name&gt;:&lt;key&gt;</code>. If the same key is seen again — on a recovery retry, a reconnect, or a duplicate inbound event — Think returns the stored result <strong>without</strong> re-running <code>execute</code>, so the side effect happens at most once on the happy path.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2182.md")
</div>
<p><code>idempotencyKey</code> is a string, or a function <code>({ input, ctx }) =&gt; string</code>. Choose a key that survives recovery retries — an order id, an inbound event id — and not a value that changes per attempt. An action with no <code>idempotencyKey</code> falls back to a per-<code>toolCallId</code> key, which only deduplicates within the same tool call, not across retries.</p>
<h3 id="pending-rows-and-the-retry-lease">Pending rows and the retry lease</h3>
<p>A ledger row is written as <code>pending</code> before <code>execute</code> runs and flipped to <code>settled</code> on success (a thrown or timed-out <code>execute</code> deletes the row so the call can be retried cleanly). If the isolate dies mid-execute, the row is left <code>pending</code>. By default such a stale row is reclaimed and the action re-run once the row is older than <code>actionLedgerPendingRetryLeaseMs</code> (default 5 minutes) — <strong>but only for actions that declare an explicit <code>idempotencyKey</code></strong>, since that key is your assertion that re-running the keyed side effect is safe. A fresh pending row (or one without an explicit key) instead returns an <code>ActionPendingError</code> result so the model does not blindly retry an unknown state. Set <code>actionLedgerPendingRetryLeaseMs = false</code> to disable reclaim entirely and always surface <code>ActionPendingError</code> for a stale row.</p>
<h2 id="approvals">Approvals</h2>
<p>Gate an action behind a human with <code>approval</code>. There are two mechanisms, selected by <code>kind</code>.</p>
<h3 id="approval-gated-the-turn-waits">Approval-gated (the turn waits)</h3>
<p>The default when you set <code>approval</code> without a <code>kind</code>. The action compiles to a tool with the AI SDK <code>needsApproval</code> flag: the stream pauses with an <code>approval-requested</code> part, the client approves or rejects, and the turn continues inline. <code>execute</code> runs only after approval.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2183.md")
</div>
<p><code>approval</code> is a boolean or a predicate <code>({ input, ctx }) =&gt; boolean</code>, so you can require approval only for risky inputs. <code>approvalSummary</code> and <code>approvalRisk</code> (<code>&quot;low&quot; | &quot;medium&quot; | &quot;high&quot;</code>) populate the approval descriptor your UI renders.</p>
<h3 id="durable-pause-the-turn-parks-and-resumes-later">Durable-pause (the turn parks and resumes later)</h3>
<p>Set <code>kind: &quot;durable-pause&quot;</code> when approval may take minutes or days and you do not want to hold a connection open. The action parks into a durable store and the turn ends; <code>execute</code> does not run yet. Resume later — from anywhere, including a dashboard with no live WebSocket — with <code>approveExecution()</code> or <code>rejectExecution()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2184.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2185.md")
</div>
<p><code>approveExecution()</code> runs <code>execute</code> once and auto-continues the turn even if no client is connected; <code>rejectExecution()</code> resolves the action without running it. <code>pendingApprovals()</code> merges parked actions and paused <a href="/agents/tools/codemode/">Codemode</a> executions, so a single approval UI can drive both. (<code>durable-pause</code> requires an <code>approval</code> policy — an action that would never park is rejected at definition time.)</p>
<p>Both approval-gated and durable-pause parts carry a stable <code>ActionApprovalDescriptor</code> (<code>{ requestId, toolCallId, action, summary, input, permissions, risk, kind }</code>) so your UI has everything it needs to render the prompt.</p>
<h2 id="authorization">Authorization</h2>
<p>Declare the permissions an action requires with <code>permissions</code>, then grant them per turn. By default every turn is fully authorized, so authorization is opt-in.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2186.md")
</div>
<p>Override <code>authorizeTurn()</code> to decide, once per turn, which permissions are granted. Returning a list narrows the grant; any action requiring a permission outside the set is denied with a structured <code>ActionAuthorizationError</code> (the model never calls <code>execute</code>):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2187.md")
</div>
<p><code>authorizeTurn()</code> returns <code>true</code> (full grant), <code>false</code> (deny all), or <code>{ allowed, reason?, grantedPermissions? }</code>. For per-call logic, override <code>authorizeAction(ctx)</code> instead — it receives the action name, kind, input, and required and granted permissions.</p>
<h2 id="reply-attachments">Reply attachments</h2>
<p>An action can record advisory delivery metadata for the turn — a drafted email, a card, a voice note — with <code>ctx.attachReply()</code>. Attachments never change the tool output the model sees; they ride alongside the response for your delivery layer to render.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2188.md")
</div>
<p>Read the attachments after the turn from the <code>onChatResponse()</code> hook, or from the <code>replyAttachments(requestId?)</code> getter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2189.md")
</div>
<p>Attachments are JSON-normalized and deep-copied on read, capped per turn, and discarded if the <code>execute</code> that recorded them fails. A ledger replay does not re-fire attachments (the side effect already happened), and <code>attachReply()</code> is a no-op when called from a <code>permissions</code>, <code>approval</code>, or <code>idempotencyKey</code> callback — record attachments from <code>execute</code>.</p>
<p>A built-in <code>ReplyAttachment</code> covers <code>email_draft</code>, <code>card</code>, and <code>voice_note</code>; any <code>{ type: string; ... }</code> shape is allowed for custom delivery. Override <a href="/agents/harnesses/think/channels/#deliver-out-of-band"><code>renderAttachment()</code></a> to turn an attachment into a channel notice.</p>
<h2 id="reference">Reference</h2>
<h3 id="action-config"><code>action(config)</code></h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>description</code></td>
<td><code>string</code></td>
<td>Yes</td>
<td>—</td>
<td>Tool description shown to the model.</td>
</tr>
<tr>
<td><code>inputSchema</code></td>
<td><code>FlexibleSchema</code> (Zod, Valibot or AI SDK <code>jsonSchema</code>)</td>
<td>Yes</td>
<td>—</td>
<td>Validates and types the <code>execute</code> input.</td>
</tr>
<tr>
<td><code>execute</code></td>
<td><code>(input, ctx) =&gt; Output | Promise&lt;Output&gt;</code></td>
<td>Yes</td>
<td>—</td>
<td>The action body. Receives validated input and an <code>ActionContext</code>.</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>No</td>
<td>map key</td>
<td>Overrides the tool name.</td>
</tr>
<tr>
<td><code>idempotencyKey</code></td>
<td><code>string | ({ input, ctx }) =&gt; string</code></td>
<td>No</td>
<td>per tool call</td>
<td>Stable key for ledger replay. Use a domain identifier.</td>
</tr>
<tr>
<td><code>permissions</code></td>
<td><code>readonly string[] | ({ input, ctx }) =&gt; readonly string[]</code></td>
<td>No</td>
<td>none</td>
<td>Permissions this call requires (see Authorization).</td>
</tr>
<tr>
<td><code>approval</code></td>
<td><code>boolean | ({ input, ctx }) =&gt; boolean</code></td>
<td>No</td>
<td>none</td>
<td>Gate the call behind a human.</td>
</tr>
<tr>
<td><code>approvalSummary</code></td>
<td><code>string</code></td>
<td>No</td>
<td><code>description</code></td>
<td>Human-readable summary in the approval descriptor.</td>
</tr>
<tr>
<td><code>approvalRisk</code></td>
<td><code>&quot;low&quot; | &quot;medium&quot; | &quot;high&quot;</code></td>
<td>No</td>
<td>—</td>
<td>Risk hint in the approval descriptor.</td>
</tr>
<tr>
<td><code>kind</code></td>
<td><code>&quot;server&quot; | &quot;approval-gated&quot; | &quot;durable-pause&quot;</code></td>
<td>No</td>
<td>inferred</td>
<td><code>approval-gated</code> when <code>approval</code> is set, else <code>server</code>; set <code>durable-pause</code> explicitly.</td>
</tr>
<tr>
<td><code>timeoutMs</code></td>
<td><code>number</code></td>
<td>No</td>
<td><code>30000</code></td>
<td>Per-action execution timeout (also drives <code>ctx.signal</code>).</td>
</tr>
</tbody>
</table>
<h3 id="hooks-and-methods-on-the-agent">Hooks and methods on the agent</h3>
<table>
<thead>
<tr>
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>getActions()</code></td>
<td>Return the action descriptors to compile into tools.</td>
</tr>
<tr>
<td><code>authorizeTurn(ctx)</code></td>
<td>Decide granted permissions once per turn. Defaults to full grant.</td>
</tr>
<tr>
<td><code>authorizeAction(ctx)</code></td>
<td>Decide authorization per action call. Defaults to checking <code>authorizeTurn</code> grants.</td>
</tr>
<tr>
<td><code>pendingApprovals(executionId?)</code></td>
<td>List parked actions and paused Codemode executions awaiting approval.</td>
</tr>
<tr>
<td><code>approveExecution(executionId)</code></td>
<td>Approve a parked execution; runs <code>execute</code> and auto-continues the turn.</td>
</tr>
<tr>
<td><code>rejectExecution(executionId, reason?)</code></td>
<td>Reject a parked execution without running it.</td>
</tr>
<tr>
<td><code>replyAttachments(requestId?)</code></td>
<td>Read the advisory attachments recorded during a turn.</td>
</tr>
<tr>
<td><code>actionLedgerPendingRetryLeaseMs</code></td>
<td>Stale-pending reclaim window (default <code>300000</code>; <code>false</code> to disable).</td>
</tr>
</tbody>
</table>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/harnesses/think/tools/">Tools</a> — workspace tools, code execution, and extensions.</li>
<li><a href="/agents/concepts/agentic-patterns/human-in-the-loop/">Human in the loop</a> — the approval flow end to end.</li>
<li><a href="/agents/harnesses/think/channels/">Channels</a> — deliver attachments and out-of-band notices.</li>
</ul>
