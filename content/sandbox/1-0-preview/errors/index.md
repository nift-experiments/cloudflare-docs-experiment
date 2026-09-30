---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/1-0-preview/errors/
  description: Retry and recover from Sandbox SDK 1.0 preview failures when containers start, stop, or interrupt work.
  full_title: Errors and recovery · Cloudflare Sandbox SDK docs
  head_html: <title>Errors and recovery · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Retry and recover from Sandbox SDK 1.0 preview failures when containers start, stop, or interrupt work."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/1-0-preview/errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/1-0-preview/errors/index.md"><meta property="og:title" content="Errors and recovery · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Retry and recover from Sandbox SDK 1.0 preview failures when containers start, stop, or interrupt work."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/1-0-preview/errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/1-0-preview/errors/#page","headline":"Errors and recovery \u00b7 Cloudflare Sandbox SDK docs","description":"Retry and recover from Sandbox SDK 1.0 preview failures when containers start, stop, or interrupt work.","url":"https://developers.cloudflare.com/sandbox/1-0-preview/errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/1-0-preview/errors/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13750.md")
</aside>
<p>Some failures mean the container never started your work. Others mean the work may already have started. Those cases need different recovery.</p>
<p>The same <strong>sandbox ID</strong> can later use a <strong>new container</strong>. Processes, terminals, and local files from the previous container do not return on their own. Refer to <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a> and <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>.</p>
<p>Class catalog: <a href="/sandbox/1-0-preview/api/errors/">Errors API</a>. Symptom table: <a href="/sandbox/1-0-preview/troubleshooting/">Troubleshooting</a>.</p>
<h2 id="before-the-container-starts-the-work">Before the container starts the work</h2>
<p>If the container is not ready, the SDK may throw <code>ContainerUnavailableError</code> (<code>CONTAINER_UNAVAILABLE</code>). The operation did not run inside the container.</p>
<p>That often happens on cold start, after idle stop, or during a deploy.</p>
<p>The error context includes <code>retryable: true</code>, a <code>reason</code> (for example <code>container_starting</code>), and optional <code>retryAfterMs</code>. Back off (use <code>retryAfterMs</code> when present), then try the same kind of work again.</p>
<p>Do not use that same “always retry” rule for failures that occur after the container may already have started the work.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13751.md")
</div>
<h2 id="after-the-container-may-have-started-the-work">After the container may have started the work</h2>
<p>Once the container has accepted an operation, a failure can leave partial results: a process may be running, a file may exist, a backup may have begun.</p>
<h3 id="container-replaced-or-sandbox-ended-during-a-call">Container replaced or sandbox ended during a call</h3>
<p><code>OperationInterruptedError</code> means the container or sandbox changed while the call was already underway. The work may have started.</p>
<p>Use <code>reason</code> and <code>retryable</code> on the error (refer to <a href="/sandbox/1-0-preview/api/errors/">Errors API</a> for fields). If the steps change state, check the sandbox or your own records before running the same steps again.</p>
<h3 id="sdk-lost-contact-during-a-call">SDK lost contact during a call</h3>
<p><code>RPCTransportError</code> means the SDK lost contact with the current container during a call. A later call can succeed against the container again.</p>
<p>That does <strong>not</strong> mean the interrupted call did nothing. Prefer checkpoints and steps that are safe to run twice, or inspect state, before repeating the same work. Diagnostic <code>kind</code> values are listed on the <a href="/sandbox/1-0-preview/api/errors/">Errors API</a>.</p>
<h3 id="stale-process-or-terminal-handles">Stale process or terminal handles</h3>
<p>Process and terminal IDs belong to the <strong>current</strong> container for a sandbox ID. After stop or replace, calls on an old handle throw <code>StaleProcessHandleError</code> or <code>StaleTerminalHandleError</code>. <code>getProcess</code>, <code>getTerminal</code>, <code>listProcesses</code>, and <code>listTerminals</code> do not start a container. They return <code>null</code> or <code>[]</code> when no container is running, or when the ID is unknown in the current container. That is not an exception.</p>
<p>Store the job (command, <code>cwd</code>, <code>env</code>, checkpoint), not only the resource ID. Then start a new <code>exec</code> or <code>createTerminal</code> when the old handle is gone.</p>
<h3 id="local-waits-and-aborts">Local waits and aborts</h3>
<p>Timeouts and <code>AbortSignal</code> on <code>output()</code>, <code>waitForExit()</code>, <code>waitForLog()</code>, <code>waitForPort()</code>, and <code>logs()</code> end <strong>that wait or stream only</strong>. They do not kill the process. Canceling terminal output does not terminate the PTY.</p>
<p>Use <code>process.kill()</code> or <code>terminal.interrupt()</code> / <code>terminal.terminate()</code> when you intend to stop the resource. Typical errors: <code>ProcessWaitTimeoutError</code>, <code>ProcessAbortedError</code>.</p>
<h3 id="invalid-arguments">Invalid arguments</h3>
<p>Invalid <code>cwd</code> or environment variables, a missing executable, or similar request problems fail until you change those values. Do not retry the same invalid request. Typical classes: <code>InvalidProcessCwdError</code>, <code>InvalidProcessEnvironmentError</code>, <code>ProcessSpawnFailedError</code>.</p>
<h3 id="worker-and-container-image-mismatch">Worker and container image mismatch</h3>
<p>Some failures mean the Worker package and container image do not match, the image cannot start, or setup between Worker and container failed.</p>
<table>
<thead>
<tr>
<th>Signal</th>
<th>Response</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RuntimeControlProtocolError</code> (for example <code>unsupported-protocol-version</code>, missing or malformed metadata)</td>
<td>Deploy the Worker package and container image from the same <code>@cloudflare/sandbox@next</code> line. Do not mix preview and stable packages.</td>
</tr>
<tr>
<td>Wrong or missing image, or the container exits before it is ready</td>
<td>Fix <code>wrangler</code>, the image, or the entrypoint. Retrying the same application call will not help.</td>
</tr>
<tr>
<td>Account or location capacity limits</td>
<td>Lower concurrency or raise limits. Refer to <a href="/sandbox/platform/limits/">Platform limits</a>.</td>
</tr>
</tbody>
</table>
<p>Catalog detail: <a href="/sandbox/1-0-preview/api/errors/#worker-and-container-image-mismatch">Worker and container image mismatch</a>.</p>
<p>These are not the same as a slow start (<code>ContainerUnavailableError</code>). Do not use the same backoff-and-retry loop for both.</p>
<h2 id="common-recovery-paths">Common recovery paths</h2>
<h3 id="first-use-or-wake-after-idle">First use or wake after idle</h3>
<p><strong>Error:</strong> <code>ContainerUnavailableError</code></p>
<p>Back off, then run the full unit of work again (for example setup plus <code>exec</code>), not an arbitrary middle step without a checkpoint.</p>
<h3 id="long-job-across-worker-requests">Long job across Worker requests</h3>
<ol>
<li>Persist the job and checkpoint (and a process or terminal ID while it is useful).</li>
<li>On a later request, call <code>getProcess</code> or <code>getTerminal</code> if you still have an ID.</li>
<li>If you get a handle, continue (logs, connect, wait).</li>
<li>If you get <code>null</code> or a stale-handle error, start again from the checkpoint.</li>
<li>If you get <code>ContainerUnavailableError</code>, backoff and continue with a new operation.</li>
</ol>
<h3 id="deploy-or-replace-while-a-call-is-in-flight">Deploy or replace while a call is in flight</h3>
<p><strong>Error:</strong> <code>OperationInterruptedError</code></p>
<p>Read <code>reason</code> and <code>retryable</code>. If the call may have changed something, inspect before repeating it.</p>
<h3 id="lost-contact-during-a-call">Lost contact during a call</h3>
<p><strong>Error:</strong> <code>RPCTransportError</code></p>
<p>Log <code>kind</code> if you need diagnostics. Assume in-flight work may have run. Continue from checkpoints or inspection, then start a new operation if the job still needs it.</p>
<h3 id="you-only-stopped-waiting">You only stopped waiting</h3>
<p><strong>Errors:</strong> <code>ProcessWaitTimeoutError</code>, <code>ProcessAbortedError</code></p>
<p>Either keep observing (<code>getProcess</code> and <code>logs({ since })</code>) or stop the process with <code>kill</code>. Do not assume the process exited because the wait ended.</p>
<h3 id="invalid-arguments-1">Invalid arguments</h3>
<p><strong>Errors:</strong> <code>InvalidProcessCwdError</code>, <code>InvalidProcessEnvironmentError</code>, <code>ProcessSpawnFailedError</code>, and similar</p>
<p>Correct the path, environment, or command (or the files in the image if the binary is missing). Do not retry unchanged values.</p>
<h3 id="worker-and-container-image-mismatch-1">Worker and container image mismatch</h3>
<p><strong>Situation:</strong> After a deploy, calls fail with protocol or setup errors, or the container never becomes usable.</p>
<p><strong>Errors / signals:</strong> <code>RuntimeControlProtocolError</code>; wrong image; container exits before it is ready</p>
<p><strong>Do:</strong> Redeploy the Worker package and container image from the same <code>@cloudflare/sandbox@next</code> line. Confirm the image name and entrypoint.</p>
<p><strong>Do not:</strong> Treat this like a slow container start and only back off.</p>
<h2 id="example">Example</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13752.md")
</div>
<p>Prefer <code>instanceof</code> with classes from <code>@cloudflare/sandbox</code>. Full tables: <a href="/sandbox/1-0-preview/api/errors/">Errors API</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a></li>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a> · <a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a></li>
</ul>
