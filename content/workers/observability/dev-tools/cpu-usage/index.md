<p>If a Worker spends too much time performing CPU-intensive tasks, responses may be slow or the Worker might
fail to startup due to <a href="/workers/platform/limits/#worker-startup-time">time limits</a>.</p>
<p>Profiling in DevTools can help you identify and fix code that uses too much CPU.</p>
<p>Measuring execution time of specific functions in production can be difficult because Workers
<a href="/workers/reference/security-model/#step-1-disallow-timers-and-multi-threading">only increment timers on I/O</a>
for security purposes. However, measuring CPU execution times is possible in local development with DevTools.</p>
<p>When using DevTools to monitor CPU usage, it may be difficult to replicate specific behavior you are
seeing in production. To mimic production behavior, make sure the requests you send to the local Worker
are similar to requests in production. This might mean sending a large volume of requests, making requests
to specific routes, or using production-like data via <a href="/workers/local-development/#remote-bindings">remote bindings</a>.</p>
<h2 id="taking-a-profile">Taking a profile</h2>
<p>To generate a CPU profile:</p>
<ul>
<li>Run <code>wrangler dev</code> to start your Worker</li>
<li>Press the <code>D</code> key from your terminal to open DevTools</li>
<li>Select the &quot;Profiler&quot; tab</li>
<li>Select <code>Start</code> to begin recording CPU usage</li>
<li>Send requests to your Worker from a new tab</li>
<li>Select <code>Stop</code></li>
</ul>
<p>You now have a CPU profile.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17060.md")
</aside>
<h2 id="an-example-profile">An Example Profile</h2>
<p>Let's look at an example to learn how to read a CPU profile. Imagine you have the following Worker:</p>
<pre><code class="language-js">const addNumbers = (body) =&gt; {&#10;	for (let i = 0; i &lt; 5000; ++i) {&#10;		body = body + &quot; &quot; + i;&#10;	}&#10;	return body;&#10;};&#10;&#10;const moreAddition = (body) =&gt; {&#10;	for (let i = 5001; i &lt; 15000; ++i) {&#10;		body = body + &quot; &quot; + i;&#10;	}&#10;	return body;&#10;};&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		let body = &quot;Hello Profiler! - &quot;;&#10;		body = addNumbers(body);&#10;		body = moreAddition(body);&#10;		return new Response(body);&#10;	},&#10;};&#10;</code></pre>
<p>You want to find which part of the code causes slow response times. How do you use DevTool profiling to identify the
CPU-heavy code and fix the issue?</p>
<p>First, as mentioned above, you open DevTools by pressing the <code>D</code> key after running <code>wrangler dev</code>. Then, you
navigate to the &quot;Profiler&quot; tab and take a profile by pressing <code>Start</code> and sending a request.</p>
<p><img src="/assets/upstream/images/workers/observability/profile.png" alt="CPU Profile" /></p>
<p>The top chart in this image shows a timeline of the profile, and you can use it to zoom in on a specific request.</p>
<p>The chart below shows the CPU time used for operations run during the request. In this screenshot, you can see
&quot;fetch&quot; time at the top and the subscomponents of fetch beneath, including the two functions <code>addNumbers</code> and
<code>moreAdditions</code>. By hovering over each box, you get more information, and by clicking the box, you navigate
to the function's source code.</p>
<p>Using this graph, you can answer the question of &quot;what is taking CPU time?&quot;. The <code>addNumbers</code> function has
a very small box, representing 0.3ms of CPU time. The <code>moreAdditions</code> box is larger, representing 2.2ms of CPU time.</p>
<p>Therefore, if you want to make response times faster, you need to optimize <code>moreAdditions</code>.</p>
<p>You can also change the visualization from ‘Chart’ to ‘Heavy (Bottom Up)’ for an alternative view.</p>
<p><img src="/assets/upstream/images/workers/observability/heavy.png" alt="CPU Profile" /></p>
<p>This shows the relative times allocated to each function. At the top of the list, <code>moreAdditions</code> is clearly the
slowest portion of your Worker. You can see that garbage collection also represents a large percentage of time, so
memory optimization could be useful.</p>
<h2 id="additional-resources">Additional Resources</h2>
<p>To learn more about how to use the CPU profiler, see <a href="https://developer.chrome.com/docs/devtools/performance/nodejs#profile">Google's documentation on Profiling the CPU in DevTools</a>.</p>
<p>To learn how to use DevTools to gain insight into memory, see the <a href="/workers/observability/dev-tools/memory-usage/">Memory Usage Documentation</a>.</p>
