<p>By default, each Dynamic Worker invocation uses your Workers plan <a href="/workers/platform/limits/#account-plan-limits">limits</a> for CPU time and subrequests. Custom limits allow you to programmatically enforce lower limits on the Dynamic Worker's resource usage.</p>
<p>You can set limits for the maximum CPU time and number of subrequests per invocation. If a Dynamic Worker hits either of these limits, it will immediately throw an exception.</p>
<h2 id="set-custom-limits">Set custom limits</h2>
<p>Custom limits can be specified as part of the worker code:</p>
<pre><code class="language-js">const worker = env.LOADER.get(&quot;my-worker&quot;, async () =&gt; {&#10;  return {&#10;    compatibilityDate: &quot;$today&quot;,&#10;    mainModule: &quot;index.js&quot;,&#10;    modules: { &quot;index.js&quot;: code },&#10;    limits: { cpuMs: 10, subRequests: 5 },&#10;  };&#10;});&#10;</code></pre>
<p>They can also be specified as part of the <code>getEntrypoint()</code> call:</p>
<pre><code class="language-js">// get the worker&#x27;s default entrypoint with custom limits&#10;// if limits were already specified as part of the worker code, the lower of the two limits is used&#10;const entrypoint = worker.getEntrypoint(null, { limits: { cpuMs: 10, subRequests: 5 } });&#10;await entrypoint.fetch(...);&#10;</code></pre>
