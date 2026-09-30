<h2 id="introduction">Introduction</h2>
<p>A/B testing, also known as split testing, is a fundamental technique in the realm of web development, allowing teams to iteratively refine and optimize their digital experiences. A/B testing involves comparing two versions of a web page or app feature to determine which one performs better in achieving a predefined goal, such as increasing conversions, engagement, or user satisfaction.</p>
<p>The process typically begins with the creation of two variants: the control (A) and the variant (B). These variants are identical except for the specific element being tested, whether it's a headline, button color, layout, or any other component of the user interface or user experience. For example, a team might test two different call-to-action button colors to see which one generates more clicks.</p>
<p>Once the variants are ready, they are exposed to users in a randomized manner. This randomization ensures that any differences in performance between the variants can be attributed to the changes being tested rather than external factors like user demographics or behavior.</p>
<p>As users interact with the different variants, their actions and behaviors are tracked and analyzed to measure the performance of each variant against the predefined goal. Key metrics such as click-through rates, conversion rates, bounce rates, and engagement metrics are monitored to determine which variant is more effective in achieving the desired outcome.</p>
<p>A/B testing is a powerful tool for continuously optimizing and improving digital experiences, enabling teams to make data-driven decisions based on real user feedback rather than subjective opinions or assumptions. By systematically testing and refining different elements of their websites or applications, organizations can enhance user satisfaction, increase conversions, and ultimately achieve their business objectives in a competitive online landscape.</p>
<p>Cloudflare's low-latency, fully serverless compute platform, <a href="/workers/">Workers</a> offers powerful capabilities to enable A/B testing using a server-side implementation. With the help of <a href="/kv/">Workers KV</a>, this solution can be make highly configurable with ease.</p>
<h2 id="a-b-testing-using-workers">A/B testing using Workers</h2>
<p><img src="/assets/upstream/images/reference-architecture/a-b-testing-workers/a-b-testing-workers.svg" alt="Figure 1: A/B testing using Workers" title="Figure 1: A/B testing using Workers" /></p>
<p>This architecture shows a same-URL A/B testing endpoint. The A/B testing logic and configuration is deployed on the server side, so that clients do not have to implement any changes to make use of A/B testing.</p>
<ol>
<li><strong>Client</strong>: Sends requests to server. This could be through a desktop or mobile browser, or native or mobile app.</li>
<li><strong>Configuration</strong>: Process incoming request using Workers. Read current configuration by reading from <a href="/kv/">KV</a> using the <a href="/kv/api/read-key-value-pairs/"><code>get()</code></a> method. This allows for flexible updates to the A/B services configuration fully decoupled from code-deployment.</li>
<li><strong>Origin requests</strong>: Check for already existing cookies in the request headers. If no cookie for group assignment is set, randomly assign a group. If a cookie is set, extract assigned group from the cookie header. Send request to either the control endpoint (A) or variant endpoints (B) depending on the configuration and the assigned group.</li>
<li><strong>Response</strong>: Return the response from the origin. Additionally, if no cookie was previously set, set a cookie with the respective assigned group for session affinity.</li>
</ol>
<p>For an example with code snippets on how to use Workers and Workers KV to route requests to different origin web servers, refer to Workers KV's example on <a href="/kv/examples/routing-with-workers-kv/">routing across web servers</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/get-started/guide/">Workers: Get started</a></li>
<li><a href="/kv/get-started/">Workers KV: Get started</a></li>
<li><a href="/kv/examples/routing-with-workers-kv/">Workers KV: Route requests to web servers with Workers and Workers KV</a></li>
<li><a href="/workers/examples/ab-testing/">Code Example: A/B testing with same-URL direct access</a></li>
</ul>
