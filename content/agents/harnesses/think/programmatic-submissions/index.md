---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/
  description: Durably accept a Think turn with submitMessages() for webhooks and RPC callers, with idempotent retry, status inspection, and cancellation.
  full_title: Programmatic submissions · Cloudflare Agents docs
  head_html: <title>Programmatic submissions · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Durably accept a Think turn with submitMessages() for webhooks and RPC callers, with idempotent retry, status inspection, and cancellation."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/index.md"><meta property="og:title" content="Programmatic submissions · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Durably accept a Think turn with submitMessages() for webhooks and RPC callers, with idempotent retry, status inspection, and cancellation."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/#page","headline":"Programmatic submissions \u00b7 Cloudflare Agents docs","description":"Durably accept a Think turn with submitMessages() for webhooks and RPC callers, with idempotent retry, status inspection, and cancellation.","url":"https://developers.cloudflare.com/agents/harnesses/think/programmatic-submissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/programmatic-submissions/
  schema: 1
---
<p>Durably accept a Think turn and return before inference runs. Use <code>submitMessages()</code> for webhook handlers, RPC callers, and parent Workers that need a fast acknowledgement, safe retry, and later status inspection.</p>
<p>Declarative <a href="/agents/harnesses/think/scheduled-tasks/">scheduled prompt tasks</a> use the same durable submission path under the hood. Use <code>getScheduledTasks()</code> when the trigger is recurring and code-declared; use <code>submitMessages()</code> directly when an external caller or webhook creates one-off work. To wait for the response inline, use <a href="/agents/harnesses/think/sub-agents/#savemessages"><code>saveMessages()</code></a> instead.</p>
<h2 id="submitmessages">submitMessages</h2>
<pre tabindex="0"><code class="language-ts">async submitMessages(&#10;	messages: UIMessage[],&#10;	options?: {&#10;		submissionId?: string;&#10;		idempotencyKey?: string;&#10;		metadata?: Record&lt;string, unknown&gt;;&#10;	},&#10;): Promise&lt;SubmitMessagesResult&gt;&#10;</code></pre>
<p><code>submitMessages()</code> accepts serializable <code>UIMessage[]</code> values. It does not accept the function form supported by <code>saveMessages((messages) =&gt; ...)</code>, because durable submissions persist work before execution and cannot store closures. The array must contain at least one message.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2140.md")
</div>
<h2 id="submission-statuses">Submission statuses</h2>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pending</code></td>
<td>Accepted and waiting for its turn</td>
</tr>
<tr>
<td><code>running</code></td>
<td>Claimed by the agent and executing</td>
</tr>
<tr>
<td><code>completed</code></td>
<td>The Think turn completed successfully</td>
</tr>
<tr>
<td><code>aborted</code></td>
<td>The submission was cancelled</td>
</tr>
<tr>
<td><code>skipped</code></td>
<td>Turn state was reset before the submission ran</td>
</tr>
<tr>
<td><code>error</code></td>
<td>Execution failed or recovery was unsafe</td>
</tr>
</tbody>
</table>
<h2 id="idempotent-retries">Idempotent retries</h2>
<p>Pass an <code>idempotencyKey</code> from your external system. Retrying with the same key returns the existing submission with <code>accepted: false</code> instead of inserting duplicate messages:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2141.md")
</div>
<p>If you pass both <code>submissionId</code> and <code>idempotencyKey</code>, they must identify the same submission. If they point at different existing submissions, <code>submitMessages()</code> throws.</p>
<h2 id="inspect-list-cancel-and-delete">Inspect, list, cancel, and delete</h2>
<p>Use the submission APIs to inspect active work, cancel a durable submission, and clean up terminal records:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2142.md")
</div>
<p>Use <code>cancelSubmission(submissionId)</code> for durable cancellation across Worker and Durable Object RPC boundaries. Use <code>AbortSignal</code> with <code>saveMessages()</code> or <code>continueLastTurn()</code> only when the caller creates the signal inside the Durable Object that runs the turn.</p>
<h2 id="session-behavior">Session behavior</h2>
<p>Think stores accepted submissions in a submission ledger first. It appends submitted messages to the conversation Session only when the submission starts executing. Later accepted submissions are not visible to the model until their own turn starts, which preserves first-in, first-out turn semantics.</p>
<p>If you cancel a submission before its messages have been applied, including one that has been claimed but is still waiting for its turn, those messages are not persisted to the conversation.</p>
<p>If the chat is cleared or turn state is reset before a pending submission runs, the submission is marked <code>skipped</code>.</p>
<h2 id="compared-with-workflows">Compared with Workflows</h2>
<p>Use Workflows for multi-step orchestration, retries per step, long waits, external events, human approvals, or pipelines that may trigger Think as one part of a larger process. Refer to <a href="/agents/harnesses/think/workflows/">Think Workflows</a>.</p>
