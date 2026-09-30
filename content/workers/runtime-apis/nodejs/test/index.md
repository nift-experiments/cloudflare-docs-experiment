<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17135.md")
</aside>
<h2 id="mocktracker"><code>MockTracker</code></h2>
<p>The <code>MockTracker</code> API in Node.js provides a means of tracking and managing mock objects in a test
environment.</p>
<pre><code class="language-js">import { mock } from &#x27;node:test&#x27;;&#10;&#10;const fn = mock.fn();&#10;fn(1,2,3);  // does nothing... but&#10;&#10;console.log(fn.mock.callCount());  // Records how many times it was called&#10;console.log(fn.mock.calls[0].arguments);  // Records the arguments that were passed each call&#10;</code></pre>
<p>The full <code>MockTracker</code> API is documented in the <a href="https://nodejs.org/docs/latest/api/test.html#class-mocktracker">Node.js documentation for <code>MockTracker</code></a>.</p>
<p>The Workers implementation of <code>MockTracker</code> currently does not include an implementation of the <a href="https://nodejs.org/docs/latest/api/test.html#class-mocktimers">Node.js mock timers API</a>.</p>
