<ul>
<li><a href="/queues/">Queues Reference</a></li>
</ul>
<h2 id="producers">Producers</h2>
<p>Specify Queue producers to add to your environment as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	queueProducers: { MY_QUEUE: &quot;my-queue&quot; },&#10;	queueProducers: [&quot;MY_QUEUE&quot;], // If binding and queue names are the same&#10;});&#10;</code></pre>
<h2 id="consumers">Consumers</h2>
<p>Specify Workers to consume messages from your Queues as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	queueConsumers: {&#10;		&quot;my-queue&quot;: {&#10;			maxBatchSize: 5, // default: 5&#10;			maxBatchTimeout: 1 /* second(s) */, // default: 1&#10;			maxRetries: 2, // default: 2&#10;			deadLetterQueue: &quot;my-dead-letter-queue&quot;, // default: none&#10;		},&#10;	},&#10;	queueConsumers: [&quot;my-queue&quot;], // If using default consumer options&#10;});&#10;</code></pre>
<h2 id="manipulating-outside-workers">Manipulating Outside Workers</h2>
<p>For testing, it can be valuable to interact with Queues outside a Worker. You can do this by using the <code>workers</code> option to run multiple Workers in the same instance:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	workers: [&#10;		{&#10;			name: &quot;a&quot;,&#10;			modules: true,&#10;			script: `&#10;			export default {&#10;				async fetch(request, env, ctx) {&#10;					await env.QUEUE.send(await request.text());&#10;				}&#10;			}&#10;			`,&#10;			queueProducers: { QUEUE: &quot;my-queue&quot; },&#10;		},&#10;		{&#10;			name: &quot;b&quot;,&#10;			modules: true,&#10;			script: `&#10;			export default {&#10;				async queue(batch, env, ctx) {&#10;					console.log(batch);&#10;				}&#10;			}&#10;			`,&#10;			queueConsumers: { &quot;my-queue&quot;: { maxBatchTimeout: 1 } },&#10;		},&#10;	],&#10;});&#10;&#10;const queue = await mf.getQueueProducer(&quot;QUEUE&quot;, &quot;a&quot;); // Get from worker &quot;a&quot;&#10;await queue.send(&quot;message&quot;); // Logs &quot;message&quot; 1 second later&#10;</code></pre>
