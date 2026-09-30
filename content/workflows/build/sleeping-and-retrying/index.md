<p>This guide details how to sleep a Workflow and/or configure retries for a Workflow step.</p>
<h2 id="sleep-a-workflow">Sleep a Workflow</h2>
<p>You can set a Workflow to sleep as an explicit step, which can be useful when you want a Workflow to wait, schedule work ahead, or pause until an input or other external state is ready.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17556.md")
</aside>
<h3 id="sleep-for-a-relative-period">Sleep for a relative period</h3>
<p>Use <code>step.sleep</code> to have a Workflow sleep for a relative period of time:</p>
<pre><code class="language-ts">await step.sleep(&quot;sleep for a bit&quot;, &quot;1 hour&quot;);&#10;</code></pre>
<p>The second argument to <code>step.sleep</code> accepts both <code>number</code> (milliseconds) or a human-readable format, such as &quot;1 minute&quot; or &quot;26 hours&quot;. The accepted units for <code>step.sleep</code> when used this way are as follows:</p>
<pre><code class="language-ts">| &quot;second&quot;&#10;| &quot;minute&quot;&#10;| &quot;hour&quot;&#10;| &quot;day&quot;&#10;| &quot;week&quot;&#10;| &quot;month&quot;&#10;| &quot;year&quot;&#10;</code></pre>
<h3 id="sleep-until-a-fixed-date">Sleep until a fixed date</h3>
<p>Use <code>step.sleepUntil</code> to have a Workflow sleep to a specific <code>Date</code>: this can be useful when you have a timestamp from another system or want to &quot;schedule&quot; work to occur at a specific time (e.g. Sunday, 9AM UTC).</p>
<pre><code class="language-ts">// sleepUntil accepts a Date object as its second argument&#10;const workflowsLaunchDate = Date.parse(&quot;24 Oct 2024 13:00:00 UTC&quot;);&#10;await step.sleepUntil(&quot;sleep until X times out&quot;, workflowsLaunchDate);&#10;</code></pre>
<p>You can also provide a UNIX timestamp (milliseconds since the UNIX epoch) directly to <code>sleepUntil</code>.</p>
<h2 id="retry-steps">Retry steps</h2>
<p>Each call to <code>step.do</code> in a Workflow accepts an optional <code>StepConfig</code>, which allows you define the retry behaviour for that step.</p>
<p>If you do not provide your own retry configuration, Workflows applies the following defaults:</p>
<pre><code class="language-ts">const defaultConfig: WorkflowStepConfig = {&#10;	retries: {&#10;		limit: 5,&#10;		delay: 10000,&#10;		backoff: &quot;exponential&quot;,&#10;	},&#10;	timeout: &quot;10 minutes&quot;,&#10;};&#10;</code></pre>
<p>When providing your own <code>StepConfig</code>, you can configure:</p>
<ul>
<li>The total number of attempts to make for a step (limited to 10,000 retries per step)</li>
<li>The delay between attempts. Use a fixed duration as a <code>number</code> in milliseconds or a human-readable string, or use a function that returns the next delay.</li>
<li>What backoff algorithm to apply between each attempt: any of <code>constant</code>, <code>linear</code>, or <code>exponential</code></li>
<li>When to timeout (in duration) before considering the step as failed (including during a retry attempt, as the timeout is set per attempt)</li>
</ul>
<p>For example, to limit a step to 10 retries and have it apply an exponential delay (starting at 10 seconds) between each attempt, you would pass the following configuration as an optional object to <code>step.do</code>:</p>
<pre><code class="language-ts">let someState = await step.do(&#10;	&quot;call an API&quot;,&#10;	{&#10;		retries: {&#10;			limit: 10, // The total number of attempts&#10;			delay: &quot;10 seconds&quot;, // Delay between each retry&#10;			backoff: &quot;exponential&quot;, // Any of &quot;constant&quot; | &quot;linear&quot; | &quot;exponential&quot;;&#10;		},&#10;		timeout: &quot;30 minutes&quot;,&#10;	},&#10;	async () =&gt; {&#10;		/* Step code goes here */&#10;	},&#10;);&#10;</code></pre>
<h3 id="set-a-dynamic-retry-delay">Set a dynamic retry delay</h3>
<p>Use a delay function when the next retry delay should depend on the failed attempt or the thrown error. This gives you more control than a fixed delay with <code>constant</code>, <code>linear</code>, or <code>exponential</code> backoff. It is useful for rate limits, downstream provider recovery, and short network failures.</p>
<p>The delay function receives an object with:</p>
<ul>
<li><code>ctx</code> - the current <a href="/workflows/build/step-context/"><code>WorkflowStepContext</code></a>, including <code>ctx.attempt</code>.</li>
<li><code>error</code> - the error that caused the retry.</li>
</ul>
<p>Return a duration string, a number in milliseconds, or a promise that resolves to either value.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17557.md")
</div>
<h2 id="force-a-workflow-instance-to-fail">Force a Workflow instance to fail</h2>
<p>You can also force a Workflow instance to fail and <em>not</em> retry by throwing a <code>NonRetryableError</code> from within the step.</p>
<p>This can be useful when you detect a terminal (permanent) error from an upstream system (such as an authentication failure) or other errors where retrying would not help.</p>
<pre><code class="language-ts">// Import the NonRetryableError definition&#10;import {&#10;	WorkflowEntrypoint,&#10;	WorkflowStep,&#10;	WorkflowEvent,&#10;} from &quot;cloudflare:workers&quot;;&#10;import { NonRetryableError } from &quot;cloudflare:workflows&quot;;&#10;&#10;// In your step code:&#10;export class MyWorkflow extends WorkflowEntrypoint&lt;Env, Params&gt; {&#10;	async run(event: WorkflowEvent&lt;Params&gt;, step: WorkflowStep) {&#10;		await step.do(&quot;some step&quot;, async () =&gt; {&#10;			if (!event.payload.data) {&#10;				throw new NonRetryableError(&#10;					&quot;event.payload.data did not contain the expected payload&quot;,&#10;				);&#10;			}&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>The Workflow instance itself will fail immediately, no further steps will be invoked, and the Workflow will not be retried.</p>
<p>If earlier steps registered rollback handlers, those handlers will still run before the instance settles into its terminal state.</p>
<h2 id="register-rollback-handlers">Register rollback handlers</h2>
<p>You can attach a rollback handler to <code>step.do()</code> to implement saga-style compensation. When the Workflow later fails, Workflows runs registered rollback handlers in reverse <code>step-start</code> order.</p>
<p>A failed step with rollback options can also participate in rollback alongside any completed steps which have a rollback handler registered. For example, if a steps throws a <code>NonRetryableError</code> after registering rollback, its rollback handler runs with <code>output</code> set to <code>undefined</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17558.md")
</div>
<p>Rollback handlers receive:</p>
<ul>
<li><code>error</code> - the error that caused the Workflow to fail.</li>
<li><code>output</code> - the value returned by the forward step, or <code>undefined</code> if the step failed before returning</li>
</ul>
<p>You can use <code>rollbackConfig</code> to control retry behavior for the rollback handler. Throw a <code>NonRetryableError</code> from the rollback handler to stop retrying it immediately.</p>
<h2 id="catch-workflow-errors">Catch Workflow errors</h2>
<p>Any uncaught exceptions that propagate to the top level, or any steps that reach their retry limit, will cause the Workflow to end execution in an <code>Errored</code> state.</p>
<p>If you want to avoid this, you can catch exceptions emitted by a <code>step</code>. This can be useful if you need to trigger clean-up tasks or have conditional logic that triggers additional steps.</p>
<p>To allow the Workflow to continue its execution, surround the intended steps that are allowed to fail with a <code>try...catch</code> block.</p>
<pre><code class="language-ts">...&#10;await step.do(&#x27;task&#x27;, async () =&gt; {&#10;	// work to be done&#10;});&#10;&#10;try {&#10;    await step.do(&#x27;non-retryable-task&#x27;, async () =&gt; {&#10;		// work not to be retried&#10;        throw new NonRetryableError(&#x27;oh no&#x27;);&#10;    });&#10;} catch (e) {&#10;    console.log(`Step failed: ${e.message}`);&#10;    await step.do(&#x27;clean-up-task&#x27;, async () =&gt; {&#10;      // Clean up code here&#10;    });&#10;}&#10;&#10;// the Workflow will not fail and will continue its execution&#10;&#10;await step.do(&#x27;next-task&#x27;, async() =&gt; {&#10;	// more work to be done&#10;});&#10;...&#10;</code></pre>
