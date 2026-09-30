<p>Use the test harness to send requests through configured routes or target a specific Worker directly. You can also dispatch events like scheduled events.</p>
<h2 id="test-route-dispatch-across-workers">Test route dispatch across Workers</h2>
<p>When a test harness runs multiple Workers, add each Worker to the <code>workers</code> array. The first Worker is the primary Worker. <code>server.fetch()</code> sends relative URLs to the primary Worker and matches absolute URLs against configured routes. If no route matches, it falls back to the primary Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17337.md")
</div>
<h2 id="interact-with-a-specific-worker">Interact with a specific Worker</h2>
<p>Route dispatch tests the application boundary, but some tests might want to target one Worker or trigger other event handlers. Use <code>server.getWorker(name)</code> to bypass route matching and get a handle for that Worker.</p>
<p>You can then use this Worker handle to send requests directly or dispatch other events, such as <code>scheduled()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17338.md")
</div>
<h2 id="assert-logged-behavior">Assert logged behavior</h2>
<p>The test harness captures logs from the Workers runtime. To assert that a Worker logged a specific message, use <code>server.getLogs()</code> to retrieve the log entries.</p>
<p>Captured logs are reset when you call <code>server.reset()</code>. You can also call <code>server.clearLogs()</code> to isolate logs before and after a specific action:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17339.md")
</div>
<h2 id="inspect-and-control-workflow-execution">Inspect and control Workflow execution</h2>
<p>If your Worker starts a Workflow, you can use <code>worker.introspectWorkflow(bindingName)</code> to control new instances and inspect their state.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17340.md")
</div>
<p>If the test already knows the instance ID, you can also introspect that instance directly with <code>worker.introspectWorkflowInstance(bindingName, instanceId)</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17341.md")
</div>
