<ul>
<li><a href="/workers/runtime-apis/handlers/scheduled/"><code>ScheduledEvent</code> Reference</a></li>
</ul>
<h2 id="cron-triggers">Cron Triggers</h2>
<p><code>scheduled</code> events are automatically dispatched according to the specified cron
triggers:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	crons: [&quot;15 * * * *&quot;, &quot;45 * * * *&quot;],&#10;});&#10;</code></pre>
<h2 id="http-triggers">HTTP Triggers</h2>
<p>Because waiting for cron triggers is annoying, you can also make HTTP requests
to <code>/cdn-cgi/local/scheduled</code> to trigger <code>scheduled</code> events:</p>
<pre><code class="language-sh">$ curl &quot;http://localhost:8787/cdn-cgi/local/scheduled&quot;&#10;</code></pre>
<p>To simulate different values of <code>scheduledTime</code> and <code>cron</code> in the dispatched
event, use the <code>time</code> and <code>cron</code> query parameters:</p>
<pre><code class="language-sh">$ curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?time=1000&quot;&#10;$ curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<h2 id="dispatching-events">Dispatching Events</h2>
<p>When using the API, the <code>getWorker</code> function can be used to dispatch
<code>scheduled</code> events to your Worker. This can be used for testing responses. It
takes optional <code>scheduledTime</code> and <code>cron</code> parameters, which default to the
current time and the empty string respectively. It will return a promise which
resolves to an array containing data returned by all waited promises:</p>
<pre><code class="language-js">import { Miniflare } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export default {&#10;    async scheduled(controller, env, ctx) {&#10;      const lastScheduledController = controller;&#10;      if (controller.cron === &quot;* * * * *&quot;) controller.noRetry();&#10;    }&#10;  }&#10;  `,&#10;});&#10;&#10;const worker = await mf.getWorker();&#10;&#10;let scheduledResult = await worker.scheduled({&#10;	cron: &quot;* * * * *&quot;,&#10;});&#10;console.log(scheduledResult); // { outcome: &#x27;ok&#x27;, noRetry: true }&#10;&#10;scheduledResult = await worker.scheduled({&#10;	scheduledTime: new Date(1000),&#10;	cron: &quot;30 * * * *&quot;,&#10;});&#10;&#10;console.log(scheduledResult); // { outcome: &#x27;ok&#x27;, noRetry: false }&#10;</code></pre>
