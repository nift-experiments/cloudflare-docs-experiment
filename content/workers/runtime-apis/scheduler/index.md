<h2 id="background">Background</h2>
<p>The <code>scheduler</code> global provides task scheduling APIs based on the <a href="https://github.com/WICG/scheduling-apis">WICG Scheduling APIs proposal</a>. Workers currently implement the <code>scheduler.wait()</code> method.</p>
<p><code>scheduler.wait()</code> returns a Promise that resolves after a given number of milliseconds. It is an <code>await</code>-able alternative to <code>setTimeout()</code> that does not require a callback.</p>
<p>Like other <a href="/workers/runtime-apis/web-standards/#timers">timers in Workers</a>, <code>scheduler.wait()</code> does not advance during CPU execution when deployed to Cloudflare. This is a <a href="/workers/reference/security-model/#step-1-disallow-timers-and-multi-threading">security measure to mitigate against Spectre attacks</a>. In local development, timers advance regardless of whether I/O occurs.</p>
<h2 id="syntax">Syntax</h2>
<pre><code class="language-js">await scheduler.wait(delay);&#10;await scheduler.wait(delay, options);&#10;</code></pre>
<h2 id="parameters">Parameters</h2>
<ul>
<li>
<p><code>delay</code> number</p>
<ul>
<li>The number of milliseconds to wait before the returned Promise resolves.</li>
</ul>
</li>
<li>
<p><code>options</code> object optional</p>
<ul>
<li>
<p>Optional configuration for the wait operation.</p>
</li>
<li>
<p><code>signal</code> AbortSignal optional</p>
<ul>
<li>An <a href="/workers/runtime-apis/web-standards/#abortcontroller-and-abortsignal"><code>AbortSignal</code></a> that cancels the wait. When the signal is aborted, the returned Promise rejects with an <code>AbortError</code>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="return-value">Return value</h2>
<p>A <code>Promise&lt;void&gt;</code> that resolves after <code>delay</code> milliseconds. If an <code>AbortSignal</code> is provided and aborted before the delay elapses, the Promise rejects with an <code>AbortError</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="basic-delay">Basic delay</h3>
<p>Use <code>scheduler.wait()</code> to pause execution for a specified duration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16130.md")
</div>
<h3 id="retry-with-exponential-backoff">Retry with exponential backoff</h3>
<p>Use <code>scheduler.wait()</code> to implement a delay between retry attempts. This example uses exponential backoff with jitter.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16131.md")
</div>
<h3 id="cancel-with-abortsignal">Cancel with AbortSignal</h3>
<p>Use an <a href="/workers/runtime-apis/web-standards/#abortcontroller-and-abortsignal"><code>AbortController</code></a> to cancel a pending wait.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16132.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/web-standards/#timers">Timers</a> — <code>setTimeout()</code> and <code>setInterval()</code> APIs</li>
<li><a href="/workers/runtime-apis/performance/">Performance and timers</a> — <code>performance.now()</code> and timer security behavior</li>
<li><a href="/workers/runtime-apis/web-standards/#abortcontroller-and-abortsignal">AbortController and AbortSignal</a> — cancel asynchronous operations</li>
<li><a href="https://github.com/WICG/scheduling-apis">WICG Scheduling APIs proposal</a> — the specification this API is based on</li>
</ul>
