<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 8, 2026</time><h2 id="post-title">Moondream 3.1 now available on Workers AI</h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Partnering with <a href="https://moondream.ai/">Moondream</a> to bring their latest model <a href="/workers-ai/models/moondream3.1-9B-A2B/"><code>@cf/moondream/moondream3.1-9B-A2B</code></a> to Workers AI. Moondream 3.1 is a fast vision language model built on a mixture-of-experts architecture with 9B total parameters and 2B active, delivering frontier-level visual reasoning while retaining fast, cost-efficient inference.</p>
<p>Moondream 3.1 is designed for real-world vision tasks, with a 32K token context window for handling complex queries and structured outputs.</p>
<h4 id="key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Query</strong> — ask open-ended questions about an image, with an optional reasoning parameter</li>
<li><strong>Caption</strong> — generate short, normal, or long descriptions of an image</li>
<li><strong>Point</strong> — return coordinates for objects matching a target phrase</li>
<li><strong>Detect</strong> — return bounding boxes for objects matching a target phrase</li>
</ul>
<h4 id="real-time-vision-at-the-edge">Real-time vision at the edge</h4>
<p>Vision workloads like live camera feeds, robotics, content moderation, and interactive agents need answers in milliseconds, not seconds. Moondream 3.1's small active footprint (2B active parameters) pairs well with Workers AI's serverless, globally distributed inference: requests run close to your users, and streaming responses start returning tokens almost immediately.</p>
<p>In our testing, first tokens streamed back in roughly 20–30 ms, and results were fast across every task. The example end-to-end times below (client-observed median, including network round trip) are for a simple, single-subject image. Actual latency depends heavily on the image and how much detail you ask for.</p>
<table>
<thead>
<tr>
<th>Task</th>
<th>End-to-end (p50)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>query</code></td>
<td>~770 ms</td>
</tr>
<tr>
<td><code>caption</code></td>
<td>~480 ms</td>
</tr>
<tr>
<td><code>point</code></td>
<td>~145 ms</td>
</tr>
<tr>
<td><code>detect</code></td>
<td>~160 ms</td>
</tr>
</tbody>
</table>
<p>At these speeds you can call the model inline while handling a request rather than pushing the work to a background queue or a separate service. That opens up use cases where a slow response breaks the experience: moderating user-uploaded images before they are stored, locating an object in a video frame to drive a live overlay, extracting fields from a document during a form submission, or letting an agent inspect a screenshot and decide its next step within a single turn.</p>
<h4 id="get-started">Get started</h4>
<p>Use Moondream 3.1 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>) or the REST API at <code>/ai/run</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/moondream3.1-9B-A2B/">Moondream 3.1 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div></article></div>
