<p>Instead of using the <strong>dashboard editor UI</strong> to define the route graph, you can do it using the REST API. Routes are internally represented using a simple JSON structure:</p>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;&lt;route id&gt;&quot;,&#10;  &quot;name&quot;: &quot;&lt;route name&gt;&quot;,&#10;  &quot;elements&quot;: [&lt;array of elements&gt;]&#10;}&#10;</code></pre>
<h2 id="supported-elements">Supported elements</h2>
<p>Dynamic routing supports several types of elements that you can combine to create sophisticated routing flows. Each element has specific inputs, outputs, and configuration options.</p>
<h3 id="start-element">Start Element</h3>
<p>Marks the beginning of a route. Every route must start with a Start element.</p>
<ul>
<li><strong>Inputs</strong>: None</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>next</code>: Forwards the unchanged request to the next element</li>
</ul>
</li>
</ul>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;start&quot;,&#10;	&quot;outputs&quot;: {&#10;		&quot;next&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="conditional-element-if-else">Conditional Element (If/Else)</h3>
<p>Evaluates a condition based on request parameters and routes the request accordingly.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>true</code>: Forwards request to provided element if condition evaluates to true</li>
<li><code>false</code>: Forwards request to provided element if condition evaluates to false</li>
</ul>
</li>
</ul>
<p><code>conditions</code> supports MongoDB-like operators such as <code>$eq</code>, <code>$ne</code>, <code>$in</code>, <code>$and</code>, and <code>$or</code>.</p>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;conditional&quot;,&#10;	&quot;properties&quot;: {&#10;		&quot;conditions&quot;: {&#10;			&quot;metadata.plan&quot;: { &quot;$eq&quot;: &quot;free&quot; }&#10;		}&#10;	},&#10;	&quot;outputs&quot;: {&#10;		&quot;true&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;false&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="percentage-split">Percentage Split</h3>
<p>Routes requests probabilistically across multiple outputs, useful for A/B testing and gradual rollouts.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>: Up to 5 named percentage outputs
<ul>
<li>Each output key (for example, <code>&quot;10%&quot;</code>) is the probability for that branch, and the keys must sum to 100%</li>
</ul>
</li>
</ul>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;percentage&quot;,&#10;	&quot;outputs&quot;: {&#10;		&quot;10%&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;40%&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;50%&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="rate-budget-limit">Rate/Budget Limit</h3>
<p>Apply limits based on request metadata. Supports both count-based and cost-based limits.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>success</code>: Forwards request to provided element if request is not rate limited</li>
<li><code>fallback</code>: Optional output for rate-limited requests (route terminates if not provided)</li>
</ul>
</li>
</ul>
<p><strong>Properties</strong>:</p>
<ul>
<li><code>limitType</code>: &quot;count&quot; or &quot;cost&quot;</li>
<li><code>key</code>: Request field to use for rate limiting (e.g. &quot;metadata.user_id&quot;)</li>
<li><code>limit</code>: Maximum allowed requests/cost</li>
<li><code>window</code>: Time window in seconds</li>
</ul>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;rate&quot;,&#10;	&quot;properties&quot;: {&#10;		&quot;limitType&quot;: &quot;count&quot;,&#10;		&quot;key&quot;: &quot;metadata.user_id&quot;,&#10;		&quot;limit&quot;: 100,&#10;		&quot;window&quot;: 3600&#10;	},&#10;	&quot;outputs&quot;: {&#10;		&quot;success&quot;: { &quot;elementId&quot;: &quot;node_model_workers_ai&quot; },&#10;		&quot;fallback&quot;: { &quot;elementId&quot;: &quot;node_model_openai_mini&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="model">Model</h3>
<p>Executes inference using a specified model and provider with configurable timeout and retry settings.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>:
<ul>
<li><code>success</code>: Forwards request to provided element if model successfully starts streaming a response</li>
<li><code>fallback</code>: Optional output if model fails after all retries or times out</li>
</ul>
</li>
</ul>
<p><strong>Properties</strong>:</p>
<ul>
<li><code>provider</code>: AI provider (e.g. &quot;openai&quot;, &quot;anthropic&quot;)</li>
<li><code>model</code>: Specific model name</li>
<li><code>timeout</code>: Request timeout in milliseconds</li>
<li><code>retries</code>: Number of retry attempts</li>
</ul>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;model&quot;,&#10;	&quot;properties&quot;: {&#10;		&quot;provider&quot;: &quot;openai&quot;,&#10;		&quot;model&quot;: &quot;gpt-4o-mini&quot;,&#10;		&quot;timeout&quot;: 60000,&#10;		&quot;retries&quot;: 4&#10;	},&#10;	&quot;outputs&quot;: {&#10;		&quot;success&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; },&#10;		&quot;fallback&quot;: { &quot;elementId&quot;: &quot;&lt;id&gt;&quot; }&#10;	}&#10;}&#10;</code></pre>
<h3 id="end-element">End element</h3>
<p>Marks the end of a route. Returns the last successful model response, or an error if no model response was generated.</p>
<ul>
<li><strong>Inputs</strong>: Request</li>
<li><strong>Outputs</strong>: None (provide an empty <code>outputs</code> object)</li>
</ul>
<pre><code class="language-json">{&#10;	&quot;id&quot;: &quot;&lt;id&gt;&quot;,&#10;	&quot;type&quot;: &quot;end&quot;,&#10;	&quot;outputs&quot;: {}&#10;}&#10;</code></pre>
