<h2 id="debugging">Debugging</h2>
<p><a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> and <a href="/workers/wrangler/commands/general/#tail"><code>wrangler tail</code></a> are both available to help you debug your Durable Objects.</p>
<p><code>wrangler tail</code> displays a live feed of console and exception logs for each request served by your Worker code, including both normal Worker requests and Durable Object requests. After running <code>npx wrangler deploy</code>, you can use <code>wrangler tail</code> in the root directory of your Worker project and visit your Worker URL to see console and error logs in your terminal.</p>
<h2 id="common-errors">Common errors</h2>
<h3 id="no-event-handlers-were-registered-this-script-does-nothing">No event handlers were registered. This script does nothing.</h3>
<p>In your Wrangler file, make sure the <code>dir</code> and <code>main</code> entries point to the correct file containing your Worker code, and that the file extension is <code>.mjs</code> instead of <code>.js</code> if using ES modules syntax.</p>
<h3 id="cannot-apply-delete-class-migration-to-class">Cannot apply <code>--delete-class</code> migration to class.</h3>
<p>When deleting a migration using <code>npx wrangler deploy --delete-class &lt;ClassName&gt;</code>, you may encounter this error: <code>&quot;Cannot apply --delete-class migration to class &lt;ClassName&gt; without also removing the binding that references it&quot;</code>. You should remove the corresponding binding under <code>[durable_objects]</code> in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> before attempting to apply <code>--delete-class</code> again.</p>
<h3 id="durable-object-is-overloaded">Durable Object is overloaded.</h3>
<p>A single instance of a Durable Object cannot do more work than is possible on a single thread. These errors mean the Durable Object has too much work to keep up with incoming requests:</p>
<ul>
<li><code>Error: Durable Object is overloaded. Too many requests queued.</code> The total count of queued requests is too high.</li>
<li><code>Error: Durable Object is overloaded. Too much data queued.</code> The total size of data in queued requests is too high.</li>
<li><code>Error: Durable Object is overloaded. Requests queued for too long.</code> The oldest request has been in the queue too long.</li>
<li><code>Error: Durable Object is overloaded. Too many requests for the same object within a 10 second window.</code> The number of requests for a Durable Object is too high within a short span of time (10 seconds). This error indicates a more extreme level of overload.</li>
</ul>
<p>To solve this error, you can either do less work per request, or send fewer requests. For example, you can split the requests among more instances of the Durable Object.</p>
<p>These errors and others that are due to overload will have an <a href="/durable-objects/best-practices/error-handling"><code>.overloaded</code> property</a> set on their exceptions, which can be used to avoid retrying overloaded operations.</p>
<h3 id="your-account-is-generating-too-much-load-on-durable-objects-please-back-off-and-try-again-later">Your account is generating too much load on Durable Objects. Please back off and try again later.</h3>
<p>There is a limit on how quickly you can create new <a href="/durable-objects/api/stub">stubs</a> for new or existing Durable Objects. Those lookups are usually cached, meaning attempts for the same set of recently accessed Durable Objects should be successful, so catching this error and retrying after a short wait is safe. If possible, also consider spreading those lookups across multiple requests.</p>
<h3 id="durable-object-reset-because-its-code-was-updated">Durable Object reset because its code was updated.</h3>
<p>Reset in error messages refers to in-memory state. Any durable state that has already been successfully persisted via <code>state.storage</code> is not affected.</p>
<p>Refer to <a href="/durable-objects/platform/known-issues/#global-uniqueness">Global Uniqueness</a>.</p>
<h3 id="durable-object-storage-operation-exceeded-timeout-which-caused-object-to-be-reset">Durable Object storage operation exceeded timeout which caused object to be reset.</h3>
<p>To prevent indefinite blocking, there is a limit on how much time storage operations can take. In Durable Objects containing a sufficiently large number of key-value pairs, <code>deleteAll()</code> may hit that time limit and fail. When this happens, note that each <code>deleteAll()</code> call does make progress and that it is safe to retry until it succeeds. Otherwise contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a>.</p>
<h3 id="your-account-is-doing-too-many-concurrent-storage-operations-please-back-off-and-try-again-later">Your account is doing too many concurrent storage operations. Please back off and try again later.</h3>
<p>Besides the suggested approach of backing off, also consider changing your code to use <code>state.storage.get(keys Array&lt;string&gt;)</code> rather than multiple individual <code>state.storage.get(key)</code> calls where possible.</p>
