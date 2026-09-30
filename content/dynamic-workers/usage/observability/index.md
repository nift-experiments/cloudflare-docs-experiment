<p>Dynamic Workers support logs with <code>console.log()</code> calls, exceptions, and request metadata captured during execution. To access those logs, you attach a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a>, a callback that runs after the Dynamic Worker finishes that passes along all the logs, exceptions, and metadata it collected.</p>
<p>This guide will show you how to:</p>
<ul>
<li>Store Dynamic Worker logs so you can search, filter, and query them</li>
<li>Collect logs during execution and return them in real time, for development and debugging</li>
</ul>
<h2 id="capture-logs-with-tail-workers">Capture logs with Tail Workers</h2>
<p>To save logs emitted by a Dynamic Worker, you need to capture them and write them somewhere they can be stored. Setting this up requires three steps:</p>
<ol>
<li>Enabling <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> on the loader Worker so that log output is saved.</li>
<li>Defining a Tail Worker that receives logs from the Dynamic Worker and writes them to Workers Logs.</li>
<li>Attaching the Tail Worker to the Dynamic Worker when you create it.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8440.md")
</aside>
<h3 id="enable-workers-logs-on-the-loader-worker">Enable Workers Logs on the loader Worker</h3>
<p>Enable <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> by adding the <code>observability</code> setting to the loader Worker's Wrangler configuration. However, Workers Logs only captures log output from the loader Worker itself. Dynamic Workers are separate, so their <code>console.log()</code> calls are not included automatically. To get Dynamic Worker logs into Workers Logs, you need to define a Tail Worker that receives logs from the Dynamic Worker and writes them into the loader Worker's Workers Logs.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8441.md")
</div>
<h3 id="define-the-tail-worker">Define the Tail Worker</h3>
<p>When a Dynamic Worker runs, the runtime collects all of its <code>console.log()</code> calls, exceptions, and request metadata. By default, those logs are discarded after the Dynamic Worker finishes.</p>
<p>To keep them, you define a Tail Worker on the loader Worker. A Tail Worker is a class with a <code>tail()</code> method. This is where you write the code that decides what happens with the logs. The runtime will call this method after the Dynamic Worker finishes, passing in everything it collected during execution.</p>
<p>Inside <code>tail()</code>, you write each log entry to Workers Logs by calling <code>console.log()</code> with a JSON object. Include a <code>workerId</code> field in each entry so you can tell which Dynamic Worker produced each log and use it to filter and search the logs by Dynamic Worker later on.</p>
<pre><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class DynamicWorkerTail extends WorkerEntrypoint {&#10;	async tail(events) {&#10;		for (const event of events) {&#10;			for (const log of event.logs) {&#10;				console.log({&#10;					source: &quot;dynamic-worker-tail&quot;,&#10;					workerId: this.ctx.props.workerId,&#10;					level: log.level,&#10;					message: log.message,&#10;				});&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The Tail Worker reads <code>workerId</code> from <code>this.ctx.props.workerId</code>. You set this value when you attach the Tail Worker to the Dynamic Worker in the next step.</p>
<p>Since the Tail Worker is defined within the loader Worker, its <code>console.log()</code> output is saved to Workers Logs along with the loader Worker's own logs.</p>
<h3 id="attach-the-tail-worker-to-the-dynamic-worker">Attach the Tail Worker to the Dynamic Worker</h3>
<p>When you create the Dynamic Worker, pass the Tail Worker in the <a href="/dynamic-workers/api-reference/#tails"><code>tails</code></a> array. This tells the runtime: after this Dynamic Worker finishes, send its collected logs to the Tail Worker you defined.</p>
<p>To reference the <code>DynamicWorkerTail</code> class you defined in the previous step, use <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code></a>. <code>ctx</code> is the third parameter in the loader Worker's <code>fetch(request, env, ctx)</code> handler. <code>ctx.exports</code> gives you access to classes that are exported from the loader Worker. Because the Dynamic Worker runs in a separate context and cannot access the class directly, you use <code>ctx.exports.DynamicWorkerTail()</code> to create a reference that the runtime can wire up to the Dynamic Worker.</p>
<p>You also need to tell the Tail Worker which Dynamic Worker it is logging for. Since the Tail Worker runs separately from the loader Worker's <code>fetch()</code> handler, it does not have access to your local variables. To pass it information, use the <a href="/workers/runtime-apis/context/#props"><code>props</code></a> option when you create the instance. <code>props</code> is a plain object of key-value pairs that you set when attaching the Tail Worker and that the Tail Worker can read at <code>this.ctx.props</code> when it runs. In this case, you pass the <code>workerId</code> so the Tail Worker knows which Dynamic Worker produced the logs.</p>
<pre><code class="language-js">const worker = env.LOADER.get(workerId, () =&gt; ({&#10;	mainModule: WORKER_MAIN,&#10;	modules: {&#10;		[WORKER_MAIN]: WORKER_SOURCE,&#10;	},&#10;	tails: [&#10;		ctx.exports.DynamicWorkerTail({&#10;			props: { workerId },&#10;		}),&#10;	],&#10;}));&#10;&#10;return worker.getEntrypoint().fetch(request);&#10;</code></pre>
<h2 id="return-logs-in-real-time">Return logs in real time</h2>
<p>The setup above stores logs for later, but sometimes you need logs right away for real-time development. The challenge is that the Tail Worker and the loader Worker's <code>fetch()</code> handler run separately. The Tail Worker has the logs, but the <code>fetch()</code> handler is the one building the response. You need a shared place where the Tail Worker can write the logs and the <code>fetch()</code> handler can read them.</p>
<p>A <a href="/durable-objects/">Durable Object</a> works well for this. Both the Tail Worker and the <code>fetch()</code> handler can look up the same Durable Object instance by name. The Tail Worker writes logs into it after the Dynamic Worker finishes, and the <code>fetch()</code> handler reads them out and includes them in the response.</p>
<p>The pattern works like this:</p>
<ol>
<li>The <code>fetch()</code> handler creates a log session in a Durable Object before running the Dynamic Worker.</li>
<li>The Dynamic Worker runs and produces logs.</li>
<li>After the Dynamic Worker finishes, the Tail Worker writes the collected logs to the same Durable Object.</li>
<li>The <code>fetch()</code> handler reads the logs from the Durable Object and returns them in the response.</li>
</ol>
<pre><code class="language-js">import { exports } from &quot;cloudflare:workers&quot;;&#10;&#10;// 1. Create a log session before running the Dynamic Worker.&#10;const logSession = exports.LogSession.getByName(workerName);&#10;const logWaiter = await logSession.waitForLogs();&#10;&#10;// 2. Run the Dynamic Worker.&#10;const response = await worker.getEntrypoint().fetch(request);&#10;&#10;// 3. Wait up to 1 second for the Tail Worker to deliver logs.&#10;const logs = await logWaiter.getLogs(1000);&#10;</code></pre>
<p>For a full working implementation, refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground example</a>.</p>
