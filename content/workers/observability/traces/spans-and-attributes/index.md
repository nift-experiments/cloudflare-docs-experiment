<p>Cloudflare Workers provides automatic tracing instrumentation <strong>out of the box</strong> - no code changes or SDK are required.</p>
<h2 id="currently-supported-spans-and-attributes">Currently supported spans and attributes</h2>
<h3 id="attributes-available-on-all-spans">Attributes available on all spans</h3>
<ul>
<li><code>cloud.provider</code> - Always set to <code>cloudflare</code></li>
<li><code>cloud.platform</code> - Always set to <code>cloudflare.workers</code></li>
<li><code>faas.name</code> - The name of your Worker</li>
<li><code>faas.invocation_id</code> - A unique identifier for this specific Worker invocation</li>
<li><code>faas.version</code> - The deployed version tag of your Worker</li>
<li><code>faas.invoked_region</code> - The region where the Worker was invoked</li>
<li><code>service.name</code> - The name of your Worker</li>
<li><code>cloudflare.colo</code> - The three-letter IATA airport code of the Cloudflare data center that processed the request (e.g., <code>SFO</code>, <code>LHR</code>)</li>
<li><code>cloudflare.script_name</code> - The name of your Worker</li>
<li><code>cloudflare.script_tags</code> - Tags associated with your Worker deployment</li>
<li><code>cloudflare.script_version.id</code> - The version identifier of your deployed Worker</li>
<li><code>cloudflare.durable_object.id</code> - The Durable Object instance ID, set on root and child spans for Durable Object invocations</li>
<li><code>cloudflare.invocation.sequence.number</code> - A counter added to every emitted span and log that can be used to distinguish which was emitted first when the timestamps are the same</li>
<li><code>telemetry.sdk.language</code> - The programming language used, set to <code>javascript</code></li>
<li><code>telemetry.sdk.name</code> - The telemetry SDK name, set to <code>cloudflare</code></li>
</ul>
<hr />
<h3 id="attributes-available-on-all-root-spans">Attributes available on all root spans</h3>
<ul>
<li><code>faas.trigger</code> - The trigger that your Worker was invoked by (e.g., <code>http</code>, <code>cron</code>, <code>queue</code>, <code>email</code>)</li>
<li><code>cloudflare.ray_id</code> - A <a href="/fundamentals/reference/cloudflare-ray-id/">unique identifier</a> for every request that goes through Cloudflare</li>
<li><code>cloudflare.handler_type</code> - The type of handler that processed the request (e.g., <code>fetch</code>, <code>scheduled</code>, <code>queue</code>, <code>email</code>, <code>alarm</code>)</li>
<li><code>cloudflare.entrypoint</code> - The entrypoint that was invoked in your Worker (e.g. the name of your Durable Object)</li>
<li><code>cloudflare.execution_model</code> - The execution model of the Worker (e.g., <code>stateless</code>, <code>stateful</code> for Durable Objects)</li>
<li><code>cloudflare.outcome</code> - The outcome of the Worker invocation (e.g., <code>ok</code>, <code>exception</code>, <code>exceededCpu</code>, <code>exceededMemory</code>)</li>
<li><code>cloudflare.cpu_time_ms</code> - The CPU time used by the Worker invocation, in milliseconds</li>
<li><code>cloudflare.wall_time_ms</code> - The wall time used by the Worker invocation, in milliseconds</li>
</ul>
<hr />
<h3 id="runtime-api-workers-runtime-apis"><a href="/workers/runtime-apis/">Runtime API</a></h3>
<h4 id="fetch-workers-runtime-apis-handlers-fetch"><a href="/workers/runtime-apis/handlers/fetch/"><code>fetch</code></a></h4>
<ul>
<li><code>network.protocol.name</code></li>
<li><code>network.protocol.version</code></li>
<li><code>url.full</code></li>
<li><code>url.scheme</code></li>
<li><code>url.path</code></li>
<li><code>url.query</code></li>
<li><code>server.port</code></li>
<li><code>server.address</code></li>
<li><code>user_agent.original</code></li>
<li><code>http.request.method</code></li>
<li><code>http.request.header.content-type</code></li>
<li><code>http.request.header.content-length</code></li>
<li><code>http.request.header.accept</code></li>
<li><code>http.request.header.accept-encoding</code></li>
<li><code>http.request.body.size</code></li>
<li><code>http.response.status_code</code></li>
<li><code>http.response.body.size</code></li>
</ul>
<h4 id="cache-put-workers-runtime-apis-cache-put"><a href="/workers/runtime-apis/cache/#put"><code>cache_put</code></a></h4>
<ul>
<li><code>cache.request.url</code></li>
<li><code>cache.request.method</code></li>
<li><code>cache.request.payload.status_code</code></li>
<li><code>cache.request.payload.header.cache_control</code></li>
<li><code>cache.request.payload.header.cache_tag</code></li>
<li><code>cache.request.payload.header.etag</code></li>
<li><code>cache.request.payload.header.expires</code></li>
<li><code>cache.request.payload.header.last_modified</code></li>
<li><code>cache.request.payload.size</code></li>
<li><code>cache.response.success</code></li>
</ul>
<h4 id="cache-match-workers-runtime-apis-cache-match"><a href="/workers/runtime-apis/cache/#match"><code>cache_match</code></a></h4>
<ul>
<li><code>cache.request.ignore_method</code></li>
<li><code>cache.request.url</code></li>
<li><code>cache.request.method</code></li>
<li><code>cache.request.header.range</code></li>
<li><code>cache.request.header.if_modified_since</code></li>
<li><code>cache.request.header.if_none_match</code></li>
<li><code>cache.response.status_code</code></li>
<li><code>cache.response.body.size</code></li>
<li><code>cache.response.cache_status</code></li>
<li><code>cache.response.success</code></li>
</ul>
<h4 id="cache-delete-workers-runtime-apis-cache-delete"><a href="/workers/runtime-apis/cache/#delete"><code>cache_delete</code></a></h4>
<ul>
<li><code>cache.request.ignore_method</code></li>
<li><code>cache.request.url</code></li>
<li><code>cache.request.method</code></li>
<li><code>cache.response.status_code</code></li>
<li><code>cache.response.success</code></li>
</ul>
<hr />
<h3 id="handlers-workers-runtime-apis-handlers"><a href="/workers/runtime-apis/handlers/">Handlers</a></h3>
<h4 id="fetch-handler-workers-runtime-apis-handlers-fetch"><a href="/workers/runtime-apis/handlers/fetch/"><code>Fetch Handler</code></a></h4>
<ul>
<li><code>cloudflare.verified_bot_category</code></li>
<li><code>cloudflare.asn</code></li>
<li><code>cloudflare.response.time_to_first_byte_ms</code></li>
<li><code>geo.timezone</code></li>
<li><code>geo.continent.code</code></li>
<li><code>geo.country.code</code></li>
<li><code>geo.locality.name</code></li>
<li><code>geo.locality.region</code></li>
<li><code>user_agent.original</code></li>
<li><code>user_agent.os.name</code></li>
<li><code>user_agent.os.version</code></li>
<li><code>user_agent.browser.name</code></li>
<li><code>user_agent.browser.major_version</code></li>
<li><code>user_agent.browser.version</code></li>
<li><code>user_agent.engine.name</code></li>
<li><code>user_agent.engine.version</code></li>
<li><code>user_agent.device.type</code></li>
<li><code>user_agent.device.vendor</code></li>
<li><code>user_agent.device.model</code></li>
<li><code>http.request.method</code></li>
<li><code>http.request.header.accept</code></li>
<li><code>http.request.header.accept-encoding</code></li>
<li><code>http.request.header.accept-language</code></li>
<li><code>url.full</code></li>
<li><code>url.path</code></li>
<li><code>network.protocol.name</code></li>
</ul>
<h4 id="scheduled-handler-workers-runtime-apis-handlers-scheduled"><a href="/workers/runtime-apis/handlers/scheduled/"><code>Scheduled Handler</code></a></h4>
<ul>
<li><code>faas.cron</code></li>
<li><code>cloudflare.scheduled_time</code></li>
</ul>
<h4 id="queuehandler-workers-runtime-apis-handlers-queue"><a href="/workers/runtime-apis/handlers/queue/"><code>QueueHandler</code></a></h4>
<ul>
<li><code>cloudflare.queue.name</code></li>
<li><code>cloudflare.queue.batch_size</code></li>
</ul>
<h4 id="rpc-handler-workers-runtime-apis-rpc"><a href="/workers/runtime-apis/rpc/"><code>RPC Handler</code></a></h4>
<ul>
<li><code>jsrpc.method</code></li>
</ul>
<h4 id="email-handler-email-service-api-route-emails-email-handler"><a href="/email-service/api/route-emails/email-handler/"><code>Email Handler</code></a></h4>
<ul>
<li><code>cloudflare.email.from</code></li>
<li><code>cloudflare.email.to</code></li>
<li><code>cloudflare.email.size</code></li>
</ul>
<h4 id="tail-handler-workers-runtime-apis-handlers-tail"><a href="/workers/runtime-apis/handlers/tail/"><code>Tail Handler</code></a></h4>
<ul>
<li><code>cloudflare.trace.count</code></li>
</ul>
<h4 id="alarm-handler-durable-objects-api-alarms-alarm"><a href="/durable-objects/api/alarms/#alarm"><code>Alarm Handler</code></a></h4>
<ul>
<li><code>cloudflare.scheduled_time</code></li>
</ul>
<hr />
<h3 id="rpc-workers-runtime-apis-rpc"><a href="/workers/runtime-apis/rpc/">RPC</a></h3>
<p>Workers tracing emits these spans for RPC calls between Workers and from Workers to Durable Objects.</p>
<h4 id="rpc-session">RPC session</h4>
<p>A caller-side span that covers the lifetime of an RPC session. Calls that reuse the session appear under this span.</p>
<p>This span has no additional RPC-specific attributes.</p>
<h4 id="rpc-invocation">RPC invocation</h4>
<p>A callee-side span that covers an RPC invocation in the target Worker or Durable Object.</p>
<h4 id="rpc-call">RPC call</h4>
<p>A caller-side or callee-side span for an individual method call or property access.</p>
<p>Caller-side and callee-side spans use the execution color of the Worker or Durable Object where they run. The color change marks the execution boundary.</p>
<ul>
<li><code>jsrpc.method</code> - The method name or property path</li>
<li><code>jsrpc.operation</code> - The operation type: <code>call</code> or <code>getProperty</code></li>
<li><code>jsrpc.target_kind</code> - The type of RPC target</li>
<li><code>jsrpc.caller_span_id</code> - On callee-side spans, the corresponding caller-side <code>jsRpcCall</code> span ID</li>
</ul>
<hr />
<h3 id="d1-d1"><a href="/d1/">D1</a></h3>
<h4 id="attributes-available-on-all-d1-spans">Attributes available on all D1 spans</h4>
<ul>
<li><code>db.system.name</code></li>
<li><code>db.operation.name</code></li>
<li><code>db.query.text</code></li>
<li><code>cloudflare.binding.type</code></li>
<li><code>cloudflare.d1.response.size_after</code></li>
<li><code>cloudflare.d1.response.rows_read</code></li>
<li><code>cloudflare.d1.response.rows_written</code></li>
<li><code>cloudflare.d1.response.last_row_id</code></li>
<li><code>cloudflare.d1.response.changed_db</code></li>
<li><code>cloudflare.d1.response.changes</code></li>
<li><code>cloudflare.d1.response.served_by_region</code></li>
<li><code>cloudflare.d1.response.served_by_primary</code></li>
<li><code>cloudflare.d1.response.sql_duration_ms</code></li>
<li><code>cloudflare.d1.response.total_attempts</code></li>
</ul>
<h4 id="d1-batch-d1-worker-api-d1-database-batch"><a href="/d1/worker-api/d1-database/#batch"><code>d1_batch</code></a></h4>
<ul>
<li><code>db.operation.batch.size</code></li>
<li><code>cloudflare.d1.query.bookmark</code></li>
<li><code>cloudflare.d1.response.bookmark</code></li>
</ul>
<h4 id="d1-exec-d1-worker-api-d1-database-exec"><a href="/d1/worker-api/d1-database/#exec"><code>d1_exec</code></a></h4>
<h4 id="d1-first-d1-worker-api-prepared-statements-first"><a href="/d1/worker-api/prepared-statements/#first"><code>d1_first</code></a></h4>
<ul>
<li><code>cloudflare.d1.query.bookmark</code></li>
<li><code>cloudflare.d1.response.bookmark</code></li>
</ul>
<h4 id="d1-run-d1-worker-api-prepared-statements-run"><a href="/d1/worker-api/prepared-statements/#run"><code>d1_run</code></a></h4>
<ul>
<li><code>cloudflare.d1.query.bookmark</code></li>
<li><code>cloudflare.d1.response.bookmark</code></li>
</ul>
<h4 id="d1-all-d1-worker-api-prepared-statements-run"><a href="/d1/worker-api/prepared-statements/#run"><code>d1_all</code></a></h4>
<ul>
<li><code>cloudflare.d1.query.bookmark</code></li>
<li><code>cloudflare.d1.response.bookmark</code></li>
</ul>
<h4 id="d1-raw-d1-worker-api-prepared-statements-raw"><a href="/d1/worker-api/prepared-statements/#raw"><code>d1_raw</code></a></h4>
<ul>
<li><code>cloudflare.d1.query.bookmark</code></li>
<li><code>cloudflare.d1.response.bookmark</code></li>
</ul>
<hr />
<h3 id="browser-run-browser-run"><a href="/browser-run/">Browser Run</a></h3>
<h4 id="browser-rendering-fetch"><code>browser_rendering_fetch</code></h4>
<hr />
<h3 id="workers-kv-kv"><a href="/kv/">Workers KV</a></h3>
<h4 id="attributes-available-on-all-kv-spans">Attributes available on all KV spans</h4>
<ul>
<li><code>db.system.name</code></li>
<li><code>db.operation.name</code></li>
<li><code>cloudflare.binding.name</code></li>
<li><code>cloudflare.binding.type</code></li>
</ul>
<h4 id="kv-get-kv-api-read-key-value-pairs-get-method"><a href="/kv/api/read-key-value-pairs/#get-method"><code>kv_get</code></a></h4>
<ul>
<li><code>cloudflare.kv.query.keys</code></li>
<li><code>cloudflare.kv.query.keys.count</code></li>
<li><code>cloudflare.kv.query.type</code></li>
<li><code>cloudflare.kv.query.cache_ttl</code></li>
<li><code>cloudflare.kv.response.size</code></li>
<li><code>cloudflare.kv.response.returned_rows</code></li>
<li><code>cloudflare.kv.response.metadata</code></li>
<li><code>cloudflare.kv.response.cache_status</code></li>
</ul>
<h4 id="kv-getwithmetadata-kv-api-read-key-value-pairs-getwithmetadata-method"><a href="/kv/api/read-key-value-pairs/#getwithmetadata-method"><code>kv_getWithMetadata</code></a></h4>
<ul>
<li><code>cloudflare.kv.query.keys</code></li>
<li><code>cloudflare.kv.query.keys.count</code></li>
<li><code>cloudflare.kv.query.type</code></li>
<li><code>cloudflare.kv.query.cache_ttl</code></li>
<li><code>cloudflare.kv.response.size</code></li>
<li><code>cloudflare.kv.response.returned_rows</code></li>
<li><code>cloudflare.kv.response.metadata</code></li>
<li><code>cloudflare.kv.response.cache_status</code></li>
</ul>
<h4 id="kv-put-kv-api-write-key-value-pairs-put-method"><a href="/kv/api/write-key-value-pairs/#put-method"><code>kv_put</code></a></h4>
<ul>
<li><code>cloudflare.kv.query.keys</code></li>
<li><code>cloudflare.kv.query.keys.count</code></li>
<li><code>cloudflare.kv.query.value_type</code></li>
<li><code>cloudflare.kv.query.expiration</code></li>
<li><code>cloudflare.kv.query.expiration_ttl</code></li>
<li><code>cloudflare.kv.query.metadata</code></li>
<li><code>cloudflare.kv.query.payload.size</code></li>
</ul>
<h4 id="kv-delete-kv-api-delete-key-value-pairs-delete-method"><a href="/kv/api/delete-key-value-pairs/#delete-method"><code>kv_delete</code></a></h4>
<ul>
<li><code>cloudflare.kv.query.keys</code></li>
<li><code>cloudflare.kv.query.keys.colunt</code></li>
</ul>
<h4 id="kv-list-kv-api-list-keys-list-method"><a href="/kv/api/list-keys/#list-method"><code>kv_list</code></a></h4>
<ul>
<li><code>cloudflare.kv.query.prefix</code></li>
<li><code>cloudflare.kv.query.limit</code></li>
<li><code>cloudflare.kv.query.cursor</code></li>
<li><code>cloudflare.kv.response.size</code></li>
<li><code>cloudflare.kv.response.returned_rows</code></li>
<li><code>cloudflare.kv.response.list_complete</code></li>
<li><code>cloudflare.kv.response.cursor</code></li>
<li><code>cloudflare.kv.response.cache_status</code></li>
<li><code>cloudflare.kv.response.expiration</code></li>
</ul>
<hr />
<h3 id="r2-r2"><a href="/r2/">R2</a></h3>
<h4 id="attributes-available-on-all-r2-spans">Attributes available on all R2 spans</h4>
<ul>
<li><code>cloudflare.binding.type</code></li>
<li><code>cloudflare.binding.name</code></li>
<li><code>cloudflare.r2.bucket</code></li>
<li><code>cloudflare.r2.operation</code></li>
<li><code>cloudflare.r2.response.success</code></li>
<li><code>cloudflare.r2.error.message</code></li>
<li><code>cloudflare.r2.error.code</code></li>
</ul>
<h4 id="r2-head-r2-api-workers-workers-api-reference-bucket-method-definitions"><a href="/r2/api/workers/workers-api-reference/#bucket-method-definitions"><code>r2_head</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.key</code></li>
<li><code>cloudflare.r2.response.etag</code></li>
<li><code>cloudflare.r2.response.size</code></li>
<li><code>cloudflare.r2.response.uploaded</code></li>
<li><code>cloudflare.r2.response.checksum.value</code></li>
<li><code>cloudflare.r2.response.checksum.type</code></li>
<li><code>cloudflare.r2.response.storage_class</code></li>
<li><code>cloudflare.r2.response.ssec_key</code></li>
<li><code>cloudflare.r2.response.content_type</code></li>
<li><code>cloudflare.r2.response.content_encoding</code></li>
<li><code>cloudflare.r2.response.content_disposition</code></li>
<li><code>cloudflare.r2.response.content_language</code></li>
<li><code>cloudflare.r2.response.cache_control</code></li>
<li><code>cloudflare.r2.response.cache_expiry</code></li>
<li><code>cloudflare.r2.response.custom_metadata</code></li>
</ul>
<h4 id="r2-get-r2-api-workers-workers-api-reference-r2getoptions"><a href="/r2/api/workers/workers-api-reference/#r2getoptions"><code>r2_get</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.key</code></li>
<li><code>cloudflare.r2.request.range.offset</code></li>
<li><code>cloudflare.r2.request.range.length</code></li>
<li><code>cloudflare.r2.request.range.suffix</code></li>
<li><code>cloudflare.r2.request.range</code></li>
<li><code>cloudflare.r2.request.ssec_key</code></li>
<li><code>cloudflare.r2.request.only_if.etag_matches</code></li>
<li><code>cloudflare.r2.request.only_if.etag_does_not_match</code></li>
<li><code>cloudflare.r2.request.only_if.uploaded_before</code></li>
<li><code>cloudflare.r2.request.only_if.uploaded_after</code></li>
<li><code>cloudflare.r2.response.etag</code></li>
<li><code>cloudflare.r2.response.size</code></li>
<li><code>cloudflare.r2.response.uploaded</code></li>
<li><code>cloudflare.r2.response.checksum.value</code></li>
<li><code>cloudflare.r2.response.checksum.type</code></li>
<li><code>cloudflare.r2.response.storage_class</code></li>
<li><code>cloudflare.r2.response.ssec_key</code></li>
<li><code>cloudflare.r2.response.content_type</code></li>
<li><code>cloudflare.r2.response.content_encoding</code></li>
<li><code>cloudflare.r2.response.content_disposition</code></li>
<li><code>cloudflare.r2.response.content_language</code></li>
<li><code>cloudflare.r2.response.cache_control</code></li>
<li><code>cloudflare.r2.response.cache_expiry</code></li>
<li><code>cloudflare.r2.response.custom_metadata</code></li>
</ul>
<h4 id="r2-put-r2-api-workers-workers-api-reference-r2putoptions"><a href="/r2/api/workers/workers-api-reference/#r2putoptions"><code>r2_put</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.key</code></li>
<li><code>cloudflare.r2.request.size</code></li>
<li><code>cloudflare.r2.request.checksum.type</code></li>
<li><code>cloudflare.r2.request.checksum.value</code></li>
<li><code>cloudflare.r2.request.custom_metadata</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_type</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_encoding</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_disposition</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_language</code></li>
<li><code>cloudflare.r2.request.http_metadata.cache_control</code></li>
<li><code>cloudflare.r2.request.http_metadata.cache_expiry</code></li>
<li><code>cloudflare.r2.request.storage_class</code></li>
<li><code>cloudflare.r2.request.ssec_key</code></li>
<li><code>cloudflare.r2.request.only_if.etag_matches</code></li>
<li><code>cloudflare.r2.request.only_if.etag_does_not_match</code></li>
<li><code>cloudflare.r2.request.only_if.uploaded_before</code></li>
<li><code>cloudflare.r2.request.only_if.uploaded_after</code></li>
<li><code>cloudflare.r2.response.etag</code></li>
<li><code>cloudflare.r2.response.size</code></li>
<li><code>cloudflare.r2.response.uploaded</code></li>
<li><code>cloudflare.r2.response.checksum.value</code></li>
<li><code>cloudflare.r2.response.checksum.type</code></li>
<li><code>cloudflare.r2.response.storage_class</code></li>
<li><code>cloudflare.r2.response.ssec_key</code></li>
<li><code>cloudflare.r2.response.content_type</code></li>
<li><code>cloudflare.r2.response.content_encoding</code></li>
<li><code>cloudflare.r2.response.content_disposition</code></li>
<li><code>cloudflare.r2.response.content_language</code></li>
<li><code>cloudflare.r2.response.cache_control</code></li>
<li><code>cloudflare.r2.response.cache_expiry</code></li>
<li><code>cloudflare.r2.response.custom_metadata</code></li>
</ul>
<h4 id="r2-list-r2-api-workers-workers-api-reference-r2listoptions"><a href="/r2/api/workers/workers-api-reference/#r2listoptions"><code>r2_list</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.limit</code></li>
<li><code>cloudflare.r2.request.prefix</code></li>
<li><code>cloudflare.r2.request.cursor</code></li>
<li><code>cloudflare.r2.request.delimiter</code></li>
<li><code>cloudflare.r2.request.start_after</code></li>
<li><code>cloudflare.r2.request.include.http_metadata</code></li>
<li><code>cloudflare.r2.request.include.custom_metadata</code></li>
<li><code>cloudflare.r2.response.returned_objects</code></li>
<li><code>cloudflare.r2.response.delimited_prefixes</code></li>
<li><code>cloudflare.r2.response.truncated</code></li>
<li><code>cloudflare.r2.response.cursor</code></li>
</ul>
<h4 id="r2-delete-r2-api-workers-workers-api-reference-bucket-method-definitions"><a href="/r2/api/workers/workers-api-reference/#bucket-method-definitions"><code>r2_delete</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.keys</code></li>
</ul>
<h4 id="r2-createmultipartupload-r2-api-workers-workers-api-reference-r2multipartoptions"><a href="/r2/api/workers/workers-api-reference/#r2multipartoptions"><code>r2_createMultipartUpload</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.key</code></li>
<li><code>cloudflare.r2.request.custom_metadata</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_type</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_encoding</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_disposition</code></li>
<li><code>cloudflare.r2.request.http_metadata.content_language</code></li>
<li><code>cloudflare.r2.request.http_metadata.cache_control</code></li>
<li><code>cloudflare.r2.request.http_metadata.cache_expiry</code></li>
<li><code>cloudflare.r2.request.storage_class</code></li>
<li><code>cloudflare.r2.request.ssec_key</code></li>
<li><code>cloudflare.r2.response.upload_id</code></li>
</ul>
<h4 id="r2-uploadpart-r2-api-workers-workers-multipart-usage"><a href="/r2/api/workers/workers-multipart-usage/"><code>r2_uploadPart</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.key</code></li>
<li><code>cloudflare.r2.request.upload_id</code></li>
<li><code>cloudflare.r2.request.part_number</code></li>
<li><code>cloudflare.r2.request.ssec_key</code></li>
<li><code>cloudflare.r2.request.size</code></li>
<li><code>cloudflare.r2.response.etag</code></li>
</ul>
<h4 id="r2-abortmultipartupload-r2-api-workers-workers-multipart-usage"><a href="/r2/api/workers/workers-multipart-usage/"><code>r2_abortMultipartUpload</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.key</code></li>
<li><code>cloudflare.r2.request.upload_id</code></li>
</ul>
<h4 id="r2-completemultipartupload-r2-api-workers-workers-multipart-usage"><a href="/r2/api/workers/workers-multipart-usage/"><code>r2_completeMultipartUpload</code></a></h4>
<ul>
<li><code>cloudflare.r2.request.key</code></li>
<li><code>cloudflare.r2.request.upload_id</code></li>
<li><code>cloudflare.r2.request.uploaded_parts</code></li>
<li><code>cloudflare.r2.response.etag</code></li>
<li><code>cloudflare.r2.response.size</code></li>
<li><code>cloudflare.r2.response.uploaded</code></li>
<li><code>cloudflare.r2.response.checksum.value</code></li>
<li><code>cloudflare.r2.response.checksum.type</code></li>
<li><code>cloudflare.r2.response.storage_class</code></li>
<li><code>cloudflare.r2.response.ssec_key</code></li>
<li><code>cloudflare.r2.response.content_type</code></li>
<li><code>cloudflare.r2.response.content_encoding</code></li>
<li><code>cloudflare.r2.response.content_disposition</code></li>
<li><code>cloudflare.r2.response.content_language</code></li>
<li><code>cloudflare.r2.response.cache_control</code></li>
<li><code>cloudflare.r2.response.cache_expiry</code></li>
<li><code>cloudflare.r2.response.custom_metadata</code></li>
</ul>
<hr />
<h3 id="durable-object-api-durable-objects"><a href="/durable-objects/">Durable Object API</a></h3>
<h4 id="durable-object-subrequest"><code>durable_object_subrequest</code></h4>
<hr />
<h3 id="durable-object-storage-sql-api-durable-objects-api-sqlite-storage-api"><a href="/durable-objects/api/sqlite-storage-api">Durable Object Storage SQL API</a></h3>
<p>The SQL API allow you to modify the SQLite database embedded within a Durable Object.</p>
<h4 id="durable-object-storage-exec-durable-objects-api-sqlite-storage-api-exec"><a href="/durable-objects/api/sqlite-storage-api/#exec"><code>durable_object_storage_exec</code></a></h4>
<ul>
<li><code>db.system.name</code></li>
<li><code>db.operation.name</code></li>
<li><code>db.query.text</code></li>
<li><code>cloudflare.durable_object.query.bindings</code></li>
<li><code>cloudflare.durable_object.response.rows_read</code></li>
<li><code>cloudflare.durable_object.response.rows_written</code></li>
</ul>
<h4 id="durable-object-storage-getdatabasesize-durable-objects-api-sqlite-storage-api-databasesize"><a href="/durable-objects/api/sqlite-storage-api/#databasesize"><code>durable_object_storage_getDatabaseSize</code></a></h4>
<ul>
<li><code>db.operation.name</code></li>
<li><code>cloudflare.durable_object.response.db_size</code></li>
</ul>
<h4 id="durable-object-storage-kv-get-durable-objects-api-sqlite-storage-api-get"><a href="/durable-objects/api/sqlite-storage-api/#get"><code>durable_object_storage_kv_get</code></a></h4>
<ul>
<li><code>cloudflare.durable_object.kv.query.keys</code></li>
<li><code>cloudflare.durable_object.kv.query.keys.count</code></li>
</ul>
<h4 id="durable-object-storage-kv-put-durable-objects-api-sqlite-storage-api-put"><a href="/durable-objects/api/sqlite-storage-api/#put"><code>durable_object_storage_kv_put</code></a></h4>
<ul>
<li><code>cloudflare.durable_object.kv.query.keys</code></li>
<li><code>cloudflare.durable_object.kv.query.keys.count</code></li>
</ul>
<h4 id="durable-object-storage-kv-delete-durable-objects-api-sqlite-storage-api-delete"><a href="/durable-objects/api/sqlite-storage-api/#delete"><code>durable_object_storage_kv_delete</code></a></h4>
<ul>
<li><code>cloudflare.durable_object.kv.query.keys</code></li>
<li><code>cloudflare.durable_object.kv.query.keys.count</code></li>
<li><code>cloudflare.durable_object.kv.response.deleted_count</code></li>
</ul>
<h4 id="durable-object-storage-kv-list-durable-objects-api-sqlite-storage-api-list"><a href="/durable-objects/api/sqlite-storage-api/#list"><code>durable_object_storage_kv_list</code></a></h4>
<ul>
<li><code>cloudflare.durable_object.kv.query.start</code></li>
<li><code>cloudflare.durable_object.kv.query.startAfter</code></li>
<li><code>cloudflare.durable_object.kv.query.end</code></li>
<li><code>cloudflare.durable_object.kv.query.prefix</code></li>
<li><code>cloudflare.durable_object.kv.query.reverse</code></li>
<li><code>cloudflare.durable_object.kv.query.limit</code></li>
</ul>
<hr />
<h3 id="durable-object-storage-kv-api-durable-objects-api-legacy-kv-storage-api"><a href="/durable-objects/api/legacy-kv-storage-api">Durable Object Storage KV API</a></h3>
<p>The legacy KV-backed API allows you to modify embedded storage within a Durable Object.</p>
<h4 id="durable-object-storage-get-durable-objects-api-legacy-kv-storage-api-do-kv-async-get"><a href="/durable-objects/api/legacy-kv-storage-api/#do-kv-async-get"><code>durable_object_storage_get</code></a></h4>
<h4 id="durable-object-storage-put-durable-objects-api-legacy-kv-storage-api-do-kv-async-put"><a href="/durable-objects/api/legacy-kv-storage-api/#do-kv-async-put"><code>durable_object_storage_put</code></a></h4>
<h4 id="durable-object-storage-delete-durable-objects-api-legacy-kv-storage-api-do-kv-async-delete"><a href="/durable-objects/api/legacy-kv-storage-api/#do-kv-async-delete"><code>durable_object_storage_delete</code></a></h4>
<h4 id="durable-object-storage-list-durable-objects-api-legacy-kv-storage-api-do-kv-async-list"><a href="/durable-objects/api/legacy-kv-storage-api/#do-kv-async-list"><code>durable_object_storage_list</code></a></h4>
<h4 id="durable-object-storage-deleteall-durable-objects-api-legacy-kv-storage-api-deleteall"><a href="/durable-objects/api/legacy-kv-storage-api/#deleteall"><code>durable_object_storage_deleteAll</code></a></h4>
<hr />
<h3 id="durable-object-storage-alarms-api-durable-objects-api-alarms"><a href="/durable-objects/api/alarms/">Durable Object Storage Alarms API</a></h3>
<h4 id="durable-object-alarms-getalarm-durable-objects-api-alarms-getalarm"><a href="/durable-objects/api/alarms/#getalarm"><code>durable_object_alarms_getAlarm</code></a></h4>
<h4 id="durable-object-alarms-setalarm-durable-objects-api-alarms-setalarm"><a href="/durable-objects/api/alarms/#setalarm"><code>durable_object_alarms_setAlarm</code></a></h4>
<h4 id="durable-object-alarms-deletealarm-durable-objects-api-alarms-deletealarm"><a href="/durable-objects/api/alarms/#deletealarm"><code>durable_object_alarms_deleteAlarm</code></a></h4>
<hr />
<h3 id="images-images-optimization-binding"><a href="/images/optimization/binding/">Images</a></h3>
<h3 id="images-output-images-optimization-binding-output"><a href="/images/optimization/binding/#output"><code>images_output</code></a></h3>
<ul>
<li><code>cloudflare.binding.type</code></li>
<li><code>cloudflare.images.options.format</code></li>
<li><code>cloudflare.images.options.quality</code></li>
<li><code>cloudflare.images.options.background</code></li>
<li><code>cloudflare.images.options.anim</code></li>
<li><code>cloudflare.images.options.transforms</code></li>
<li><code>cloudflare.images.error.code</code></li>
</ul>
<h3 id="images-info-images-optimization-binding-info"><a href="/images/optimization/binding/#info"><code>images_info</code></a></h3>
<ul>
<li><code>cloudflare.binding.type</code></li>
<li><code>cloudflare.images.options.encoding</code></li>
<li><code>cloudflare.images.result.format</code></li>
<li><code>cloudflare.images.result.file_size</code></li>
<li><code>cloudflare.images.result.width</code></li>
<li><code>cloudflare.images.result.height</code></li>
<li><code>cloudflare.images.error.code</code></li>
</ul>
<hr />
<h3 id="email-email-service"><a href="/email-service/">Email</a></h3>
<h4 id="reply-email-email-service-api-route-emails-email-handler-reply-to-emails"><a href="/email-service/api/route-emails/email-handler/#reply-to-emails"><code>reply_email</code></a></h4>
<h4 id="forward-email-email-service-api-route-emails-email-handler"><a href="/email-service/api/route-emails/email-handler/"><code>forward_email</code></a></h4>
<h4 id="send-email-email-service-api-send-emails-workers-api"><a href="/email-service/api/send-emails/workers-api/"><code>send_email</code></a></h4>
<hr />
<h3 id="queues-queues"><a href="/queues/">Queues</a></h3>
<h4 id="queue-send-queues-configuration-javascript-apis-queue"><a href="/queues/configuration/javascript-apis/#queue"><code>queue_send</code></a></h4>
<h4 id="queue-sendbatch-queues-configuration-javascript-apis-queue"><a href="/queues/configuration/javascript-apis/#queue"><code>queue_sendBatch</code></a></h4>
<hr />
<h3 id="rate-limiting-workers-runtime-apis-bindings-rate-limit"><a href="/workers/runtime-apis/bindings/rate-limit/"><code>Rate limiting</code></a></h3>
<h4 id="ratelimit-run-workers-runtime-apis-bindings-rate-limit-best-practices"><a href="/workers/runtime-apis/bindings/rate-limit/#best-practices"><code>ratelimit_run</code></a></h4>
<hr />
