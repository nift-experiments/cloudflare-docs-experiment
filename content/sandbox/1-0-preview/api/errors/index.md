---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/1-0-preview/api/errors/
  description: Error classes, codes, and context fields for @cloudflare/sandbox@next.
  full_title: Errors · Cloudflare Sandbox SDK docs
  head_html: <title>Errors · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Error classes, codes, and context fields for @cloudflare/sandbox@next."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/1-0-preview/api/errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/1-0-preview/api/errors/index.md"><meta property="og:title" content="Errors · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Error classes, codes, and context fields for @cloudflare/sandbox@next."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/1-0-preview/api/errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/1-0-preview/api/errors/#page","headline":"Errors \u00b7 Cloudflare Sandbox SDK docs","description":"Error classes, codes, and context fields for @cloudflare/sandbox@next.","url":"https://developers.cloudflare.com/sandbox/1-0-preview/api/errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/1-0-preview/api/errors/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13776.md")
</aside>
<p>Error classes and codes returned by the Sandbox SDK 1.0 preview, with short recommended actions. For full recovery procedures, refer to <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<h2 id="how-errors-are-returned">How errors are returned</h2>
<p>Operations throw exceptions you can catch. Prefer <code>instanceof</code> on classes from <code>@cloudflare/sandbox</code>. Use <code>code</code> and <code>context</code> for metrics and stable field access.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13777.md")
</div>
<h3 id="imports">Imports</h3>
<p>Common lifecycle, process, terminal, and backup errors are available from the package root:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13778.md")
</div>
<p>The full module also exports <code>ErrorCode</code>, <code>SandboxError</code>, <code>createErrorFromResponse</code>, and other domain errors (files, ports, interpreter, mounts, and related context types):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13779.md")
</div>
<p>Platform helpers (not <code>SandboxError</code> subclasses):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13780.md")
</div>
<h3 id="sandboxerror-shape"><code>SandboxError</code> shape</h3>
<p>Most SDK errors extend <code>SandboxError</code>:</p>
<table>
<thead>
<tr>
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>Class name (for example <code>ContainerUnavailableError</code>)</td>
</tr>
<tr>
<td><code>message</code></td>
<td>Human-readable message</td>
</tr>
<tr>
<td><code>code</code></td>
<td>Stable <code>ErrorCode</code> string (for example <code>CONTAINER_UNAVAILABLE</code>)</td>
</tr>
<tr>
<td><code>context</code></td>
<td>Structured fields for the error type</td>
</tr>
<tr>
<td><code>httpStatus</code></td>
<td>Mapped HTTP status when applicable</td>
</tr>
<tr>
<td><code>operation</code></td>
<td>Operation label when provided</td>
</tr>
<tr>
<td><code>suggestion</code></td>
<td>Optional actionable suggestion</td>
</tr>
<tr>
<td><code>timestamp</code></td>
<td>ISO timestamp when provided</td>
</tr>
<tr>
<td><code>toJSON()</code></td>
<td>Serializes the error fields for logs</td>
</tr>
</tbody>
</table>
<p><code>RuntimeIdentityInactiveError</code> extends <code>Error</code> directly (not <code>SandboxError</code>). It means the current container is no longer the active one for this handle or call.</p>
<p>Tables include a <strong>Recommended fix</strong> column. For longer recovery procedures, refer to <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<p>Availability errors and deployment mismatch errors are listed in separate sections. Do not use the same retry loop for both.</p>
<hr />
<h2 id="container-availability-and-interrupted-calls">Container availability and interrupted calls</h2>
<p>These errors come from ordinary start, idle stop, replace, or lost contact while a call is running.</p>
<table>
<thead>
<tr>
<th>Class</th>
<th>Code</th>
<th>Key context</th>
<th>Details</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ContainerUnavailableError</code></td>
<td><code>CONTAINER_UNAVAILABLE</code></td>
<td><code>reason</code>, <code>retryable: true</code>, <code>retryAfterMs?</code></td>
<td>Container not ready before the operation started.</td>
<td>Back off (honor <code>retryAfterMs</code> when set), then try the same kind of work again.</td>
</tr>
<tr>
<td><code>OperationInterruptedError</code></td>
<td><code>OPERATION_INTERRUPTED</code></td>
<td><code>reason</code>, <code>operation</code>, <code>admitted</code>, <code>retryable</code></td>
<td>Container or sandbox changed after the operation may have started.</td>
<td>Read <code>reason</code> and <code>retryable</code>. Check sandbox or app state before repeating work that changes state.</td>
</tr>
<tr>
<td><code>RPCTransportError</code></td>
<td><code>RPC_TRANSPORT_ERROR</code></td>
<td><code>kind</code>, <code>originalMessage</code>, <code>errorName</code>, <code>closeCode?</code></td>
<td>SDK lost contact with the container during a call.</td>
<td>A later call may work. This call may already have changed something.</td>
</tr>
<tr>
<td><code>RuntimeIdentityInactiveError</code></td>
<td>—</td>
<td>—</td>
<td>Current container is no longer active for this call or handle. Plain <code>Error</code>, not <code>SandboxError</code>.</td>
<td>Check whether the resource still exists; if not, start the work again from stored state.</td>
</tr>
</tbody>
</table>
<h3 id="containerunavailableerror-reasons"><code>ContainerUnavailableError</code> reasons</h3>
<p><code>context.reason</code>:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>container_starting</code></td>
<td>Container is still starting</td>
</tr>
<tr>
<td><code>container_unhealthy</code></td>
<td>Container is not healthy</td>
</tr>
<tr>
<td><code>container_replaced</code></td>
<td>Container was replaced</td>
</tr>
<tr>
<td><code>rpc_upgrade_failed</code></td>
<td>Could not establish communication with the container</td>
</tr>
</tbody>
</table>
<h3 id="operationinterruptederror-reasons"><code>OperationInterruptedError</code> reasons</h3>
<p><code>reason</code> / <code>context.reason</code>:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>runtime_replaced</code></td>
<td>Underlying container instance was replaced</td>
</tr>
<tr>
<td><code>container_stopped</code></td>
<td>Container stopped</td>
</tr>
<tr>
<td><code>transport_disposed</code></td>
<td>Communication session was disposed</td>
</tr>
<tr>
<td><code>sandbox_destroyed</code></td>
<td>Sandbox was destroyed</td>
</tr>
<tr>
<td><code>sandbox_lifetime_changed</code></td>
<td>Sandbox lifetime configuration changed</td>
</tr>
<tr>
<td><code>recovery_exhausted</code></td>
<td>Recovery attempts were exhausted</td>
</tr>
<tr>
<td><code>unknown</code></td>
<td>Unclassified interruption</td>
</tr>
</tbody>
</table>
<p>Convenience getters on the error: <code>reason</code>, <code>retryable</code>, and <code>operationName</code>. Other fields such as <code>admitted</code>, <code>operationId</code>, <code>phase</code>, and backup-related metadata are on <code>error.context</code> only (<code>admitted</code> is <code>true | &quot;unknown&quot;</code>).</p>
<h3 id="rpctransporterror-kinds"><code>RPCTransportError</code> kinds</h3>
<p><code>kind</code> / <code>context.kind</code>:</p>
<table>
<thead>
<tr>
<th>Kind</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>peer_closed</code></td>
<td>Peer closed the connection</td>
</tr>
<tr>
<td><code>connection_failed</code></td>
<td>Connection failed</td>
</tr>
<tr>
<td><code>upgrade_failed</code></td>
<td>Connection setup failed</td>
</tr>
<tr>
<td><code>invalid_frame</code></td>
<td>Unexpected frame</td>
</tr>
<tr>
<td><code>protocol_error</code></td>
<td>Frame rejected by the protocol</td>
</tr>
<tr>
<td><code>session_disposed</code></td>
<td>Session disposed</td>
</tr>
<tr>
<td><code>unknown</code></td>
<td>Unclassified failure</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="worker-and-container-image-mismatch">Worker and container image mismatch</h2>
<p>These failures usually mean the Worker package and container image do not match, the image cannot start, or setup metadata does not match what the SDK expects. Fix the deployment. Do not treat them like a slow container start.</p>
<p>Deploy the Worker package and the sandbox container image from the same <code>@cloudflare/sandbox@next</code> line. A preview Worker with a stable image (or the reverse) often fails here.</p>
<table>
<thead>
<tr>
<th>Class</th>
<th>Code</th>
<th>Key context</th>
<th>Details</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RuntimeControlProtocolError</code></td>
<td><code>INTERNAL_ERROR</code></td>
<td><code>reason</code></td>
<td>Worker and container could not complete setup together (metadata or protocol mismatch). The code is the shared <code>INTERNAL_ERROR</code> value — identify this class with <code>instanceof RuntimeControlProtocolError</code> or by pairing <code>code === &quot;INTERNAL_ERROR&quot;</code> with <code>context.reason</code>.</td>
<td>Deploy the Worker package and container image from the same release line. Fix configuration if needed.</td>
</tr>
</tbody>
</table>
<h3 id="runtimecontrolprotocolerror-reasons"><code>RuntimeControlProtocolError</code> reasons</h3>
<p><code>context.reason</code>:</p>
<table>
<thead>
<tr>
<th>Reason</th>
<th>Meaning</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>unsupported-protocol-version</code></td>
<td>Worker and container protocol versions do not match</td>
<td>Worker package and container image are not from the same release</td>
</tr>
<tr>
<td><code>missing-metadata</code></td>
<td>Required setup metadata missing from the container</td>
<td>Bad or incomplete image/build</td>
</tr>
<tr>
<td><code>malformed-metadata</code></td>
<td>Setup metadata could not be parsed</td>
<td>Bad or incomplete image/build</td>
</tr>
<tr>
<td><code>activation-mismatch</code></td>
<td>Activation did not match the expected container</td>
<td>Can appear after container replace; if it keeps happening, check Worker and image pairing</td>
</tr>
</tbody>
</table>
<p>The following permanent problems are related and return the same response:</p>
<table>
<thead>
<tr>
<th>Problem</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>Wrong or missing container image in <code>wrangler</code> / registry</td>
<td>Deploy the Worker package and container image from the same release line. Fix configuration if needed.</td>
</tr>
<tr>
<td>Container exits before it becomes ready</td>
<td>Fix the image or entrypoint and redeploy. Do not only retry the app call.</td>
</tr>
<tr>
<td>Account or location capacity limits</td>
<td>Refer to <a href="#production-capacity-limits">Production capacity limits</a></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="process">Process</h2>
<table>
<thead>
<tr>
<th>Class</th>
<th>Code</th>
<th>Key context</th>
<th>Details</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ProcessNotFoundError</code></td>
<td><code>PROCESS_NOT_FOUND</code></td>
<td><code>processId</code></td>
<td>Unknown process ID in the current container.</td>
<td>Use the correct ID, or start the process again from stored state.</td>
</tr>
<tr>
<td><code>StaleProcessHandleError</code></td>
<td><code>STALE_PROCESS_HANDLE</code></td>
<td><code>processId</code>, <code>pid</code>, <code>operation</code></td>
<td>Handle or ID from a previous container.</td>
<td>Start the work again from stored state. Do not reuse the old handle.</td>
</tr>
<tr>
<td><code>ProcessSpawnFailedError</code></td>
<td><code>PROCESS_SPAWN_FAILED</code></td>
<td><code>processId</code>, <code>command</code>, <code>cwd?</code>, <code>stderr?</code></td>
<td>Process could not start.</td>
<td>Correct the path, environment, command, or other arguments. Do not retry the same invalid request.</td>
</tr>
<tr>
<td><code>InvalidProcessCwdError</code></td>
<td><code>INVALID_PROCESS_CWD</code></td>
<td><code>cwd</code>, <code>reason</code></td>
<td>Invalid working directory.</td>
<td>Correct the path, environment, command, or other arguments. Do not retry the same invalid request.</td>
</tr>
<tr>
<td><code>InvalidProcessEnvironmentError</code></td>
<td><code>INVALID_PROCESS_ENVIRONMENT</code></td>
<td><code>name?</code>, <code>reason</code></td>
<td>Invalid environment overlay.</td>
<td>Correct the path, environment, command, or other arguments. Do not retry the same invalid request.</td>
</tr>
<tr>
<td><code>InvalidProcessCursorError</code></td>
<td><code>INVALID_PROCESS_CURSOR</code></td>
<td><code>processId</code>, <code>cursor?</code>, <code>reason</code></td>
<td>Bad log cursor.</td>
<td>Correct the cursor or other arguments. Do not retry the same invalid value.</td>
</tr>
<tr>
<td><code>ProcessWaitTimeoutError</code></td>
<td><code>PROCESS_WAIT_TIMEOUT</code></td>
<td><code>processId</code>, <code>operation</code>, <code>timeout</code></td>
<td>Local <code>output</code>, <code>waitForExit</code>, or <code>waitForLog</code> timed out.</td>
<td>The wait ended. The process or terminal may still be running.</td>
</tr>
<tr>
<td><code>ProcessAbortedError</code></td>
<td><code>PROCESS_ABORTED</code></td>
<td><code>processId</code>, <code>operation</code></td>
<td>Local <code>AbortSignal</code> ended a wait or stream.</td>
<td>The wait ended. The process or terminal may still be running.</td>
</tr>
<tr>
<td><code>ProcessReadyTimeoutError</code></td>
<td><code>PROCESS_READY_TIMEOUT</code></td>
<td><code>processId</code>, <code>command</code>, <code>condition</code>, <code>timeout</code></td>
<td>Readiness wait timed out.</td>
<td>Check whether the process is still running before starting another.</td>
</tr>
<tr>
<td><code>ProcessExitedBeforeReadyError</code></td>
<td><code>PROCESS_EXITED_BEFORE_READY</code></td>
<td><code>processId</code>, <code>command</code>, <code>condition</code>, <code>exitCode</code></td>
<td>Process exited before readiness.</td>
<td>Correct the command or environment, then start again if needed.</td>
</tr>
<tr>
<td><code>ProcessExitedBeforeLogError</code></td>
<td><code>PROCESS_EXITED_BEFORE_LOG</code></td>
<td><code>processId</code>, <code>pid</code>, <code>exit</code></td>
<td>Process exited before a log match.</td>
<td>Correct the command or environment, then start again if needed.</td>
</tr>
<tr>
<td><code>ProcessError</code></td>
<td><code>PROCESS_ERROR</code></td>
<td><code>processId</code>, <code>pid?</code>, <code>exitCode?</code>, <code>stderr?</code></td>
<td>General process failure.</td>
<td>Check sandbox or app state before repeating work that changes state.</td>
</tr>
</tbody>
</table>
<p><code>getProcess</code> and <code>listProcesses</code> returning <code>null</code> or <code>[]</code> is not an error.</p>
<hr />
<h2 id="terminal">Terminal</h2>
<table>
<thead>
<tr>
<th>Class</th>
<th>Code</th>
<th>Key context</th>
<th>Details</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>TerminalNotFoundError</code></td>
<td><code>TERMINAL_NOT_FOUND</code></td>
<td><code>terminalId</code></td>
<td>Unknown terminal ID in the current container.</td>
<td>Use the correct ID, or start the terminal again from stored state.</td>
</tr>
<tr>
<td><code>StaleTerminalHandleError</code></td>
<td><code>STALE_TERMINAL_HANDLE</code></td>
<td><code>terminalId</code>, <code>operation</code></td>
<td>Handle or ID from a previous container.</td>
<td>Start the work again from stored state. Do not reuse the old handle.</td>
</tr>
<tr>
<td><code>InvalidTerminalCwdError</code></td>
<td><code>INVALID_TERMINAL_CWD</code></td>
<td><code>terminalId</code>, <code>cwd</code>, <code>reason</code></td>
<td>Invalid working directory at create.</td>
<td>Correct the path, environment, command, or other arguments. Do not retry the same invalid request.</td>
</tr>
<tr>
<td><code>InvalidTerminalCursorError</code></td>
<td><code>INVALID_TERMINAL_CURSOR</code></td>
<td><code>terminalId</code>, <code>cursor?</code>, <code>reason</code></td>
<td>Bad output cursor.</td>
<td>Correct the cursor or other arguments. Do not retry the same invalid value.</td>
</tr>
<tr>
<td><code>TerminalControlError</code></td>
<td><code>TERMINAL_CONTROL_ERROR</code></td>
<td><code>terminalId</code>, <code>operation</code>, <code>reason?</code></td>
<td>Interrupt, terminate, resize, or related control failed.</td>
<td>Check sandbox or app state before repeating work that changes state.</td>
</tr>
</tbody>
</table>
<p><code>getTerminal</code> and <code>listTerminals</code> returning <code>null</code> or <code>[]</code> is not an error.</p>
<hr />
<h2 id="backup">Backup</h2>
<table>
<thead>
<tr>
<th>Class</th>
<th>Code</th>
<th>Details</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>BackupCreateError</code></td>
<td><code>BACKUP_CREATE_FAILED</code></td>
<td>Backup create failed.</td>
<td>Check failure details; correct options if they are invalid.</td>
</tr>
<tr>
<td><code>BackupRestoreError</code></td>
<td><code>BACKUP_RESTORE_FAILED</code></td>
<td>Backup restore failed.</td>
<td>Check failure details; correct options if they are invalid.</td>
</tr>
<tr>
<td><code>BackupNotFoundError</code></td>
<td><code>BACKUP_NOT_FOUND</code></td>
<td>Unknown backup ID.</td>
<td>Correct the path, environment, command, or other arguments. Do not retry the same invalid request.</td>
</tr>
<tr>
<td><code>BackupExpiredError</code></td>
<td><code>BACKUP_EXPIRED</code></td>
<td>Backup past validity.</td>
<td>Correct options, or create a new backup.</td>
</tr>
<tr>
<td><code>InvalidBackupConfigError</code></td>
<td><code>INVALID_BACKUP_CONFIG</code></td>
<td>Invalid backup options.</td>
<td>Correct the path, environment, command, or other arguments. Do not retry the same invalid request.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="other-domains">Other domains</h2>
<p>These classes are available from <code>@cloudflare/sandbox/errors</code> (and some mount helpers from the package root). Confirm details against your installed package. Preview-specific guides for every domain are not all published yet.</p>
<table>
<thead>
<tr>
<th>Domain</th>
<th>Examples</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>Filesystem</td>
<td><code>FileNotFoundError</code>, <code>FileExistsError</code>, <code>PermissionDeniedError</code>, <code>FileTooLargeError</code>, <code>FileSystemError</code></td>
<td>Correct the path or handle a missing file.</td>
</tr>
<tr>
<td>Ports / preview</td>
<td><code>PortAlreadyExposedError</code>, <code>PortNotExposedError</code>, <code>InvalidPortError</code>, <code>PortInUseError</code>, <code>ServiceNotRespondingError</code>, <code>CustomDomainRequiredError</code></td>
<td>Correct port options or expose settings.</td>
</tr>
<tr>
<td>Interpreter (extension)</td>
<td><code>InterpreterNotReadyError</code>, <code>ContextNotFoundError</code>, <code>CodeExecutionError</code></td>
<td>If the interpreter is not ready, back off and try again. Otherwise correct the request.</td>
</tr>
<tr>
<td>Mounts</td>
<td><code>BucketMountError</code>, <code>BucketUnmountError</code>, <code>S3FSMountError</code>, <code>MissingCredentialsError</code>, <code>InvalidMountConfigError</code></td>
<td>Correct mount options or credentials.</td>
</tr>
<tr>
<td>Validation</td>
<td><code>ValidationFailedError</code></td>
<td>Correct the path, environment, command, or other arguments. Do not retry the same invalid request.</td>
</tr>
</tbody>
</table>
<p>Other domain classes may exist on <code>@cloudflare/sandbox/errors</code> in your installed package. Confirm against that package before depending on undocumented surfaces.</p>
<p>Mount-related errors are also exported from <code>@cloudflare/sandbox</code> next to the mount APIs.</p>
<hr />
<h2 id="platform-helpers">Platform helpers</h2>
<table>
<thead>
<tr>
<th>Helper</th>
<th>Details</th>
<th>Recommended fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>isPlatformTransientError(error)</code></td>
<td>True for some transient platform signals (for example connection lost, certain Durable Object storage startup resets, or retryable platform errors).</td>
<td>Prefer a new request or operation.</td>
</tr>
<tr>
<td><code>isDurableObjectCodeUpdateReset(error)</code></td>
<td>True when the Durable Object isolate was replaced by a code update or deploy.</td>
<td>Do not keep retrying inside the same request. Let a new request run on the new isolate.</td>
</tr>
</tbody>
</table>
<p>These helpers complement <code>SandboxError</code> subclasses. They do not replace the recovery rules on <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<hr />
<h2 id="production-capacity-limits">Production capacity limits</h2>
<p>In production, the Containers platform may reject work when account or deployment limits are exceeded (for example <code>SURPASSED_BASE_LIMITS</code>, <code>SURPASSED_TOTAL_LIMITS</code>, <code>LOCATION_SURPASSED_BASE_LIMITS</code>). Retrying the same overload does not fix that. Reduce concurrency, raise limits, or fail to an operator path. These limits usually do not appear in local <code>wrangler dev</code>.</p>
<p>Refer to <a href="/sandbox/platform/limits/">Platform limits</a>.</p>
<hr />
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a></li>
<li><a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
</ul>
