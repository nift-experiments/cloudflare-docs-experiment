<div class="nb-description">
@markup("md", "content/.markup/bodies/12.md")
</div>
<div class="nb-plan">
<p>Available on Free and Paid plans</p>
</div>
<p>With Workflows, you can build applications that chain together multiple steps, automatically retry failed tasks,
and persist state for minutes, hours, or even weeks - with no infrastructure to manage.</p>
<p>Use Workflows to build reliable AI applications, process data pipelines, manage user lifecycle with automated emails and trial expirations, and implement human-in-the-loop approval systems.</p>
<div class="nb-flex">
@markup("md", "content/.markup/bodies/13.md")
</div>
<h2 id="example">Example</h2>
<p>An image processing workflow that fetches from R2, generates an AI description, waits for approval, then publishes:</p>
<pre><code class="language-ts">export class ImageProcessingWorkflow extends WorkflowEntrypoint {&#10;	async run(event: WorkflowEvent, step: WorkflowStep) {&#10;		const imageData = await step.do(&#x27;fetch image&#x27;, async () =&gt; {&#10;			const object = await this.env.BUCKET.get(event.payload.imageKey);&#10;			return await object.arrayBuffer();&#10;		});&#10;&#10;		const description = await step.do(&#x27;generate description&#x27;, async () =&gt; {&#10;			const imageArray = Array.from(new Uint8Array(imageData));&#10;			return await this.env.AI.run(&#x27;@cf/llava-hf/llava-1.5-7b-hf&#x27;, {&#10;				image: imageArray,&#10;				prompt: &#x27;Describe this image in one sentence&#x27;,&#10;				max_tokens: 50,&#10;			});&#10;		});&#10;&#10;		await step.waitForEvent(&#x27;await approval&#x27;, {&#10;			event: &#x27;approved&#x27;,&#10;			timeout: &#x27;24 hours&#x27;,&#10;		});&#10;&#10;		await step.do(&#x27;publish&#x27;, async () =&gt; {&#10;			await this.env.BUCKET.put(`public/${event.payload.imageKey}`, imageData);&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p><a class="nb-link-button" href="/workflows/get-started/guide/">Get started</a>
<a class="nb-link-button" href="/workflows/examples/">Browse the examples</a></p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/16.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/17.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/18.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/19.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/20.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/21.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/27.md")
</div>
