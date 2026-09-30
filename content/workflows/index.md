---
cp9:
  canonical: https://developers.cloudflare.com/workflows/
  description: Build durable, multi-step applications on Cloudflare Workers that automatically retry and persist state.
  full_title: Overview · Cloudflare Workflows docs
  head_html: <title>Overview · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Build durable, multi-step applications on Cloudflare Workers that automatically retry and persist state."><link rel="canonical" href="https://developers.cloudflare.com/workflows/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/index.md"><meta property="og:title" content="Overview · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build durable, multi-step applications on Cloudflare Workers that automatically retry and persist state."><meta property="og:url" content="https://developers.cloudflare.com/workflows/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workflows/#page","headline":"Overview \u00b7 Cloudflare Workflows docs","description":"Build durable, multi-step applications on Cloudflare Workers that automatically retry and persist state.","url":"https://developers.cloudflare.com/workflows/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/
  schema: 1
---
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
<pre tabindex="0"><code class="language-ts">export class ImageProcessingWorkflow extends WorkflowEntrypoint {&#10;	async run(event: WorkflowEvent, step: WorkflowStep) {&#10;		const imageData = await step.do(&#x27;fetch image&#x27;, async () =&gt; {&#10;			const object = await this.env.BUCKET.get(event.payload.imageKey);&#10;			return await object.arrayBuffer();&#10;		});&#10;&#10;		const description = await step.do(&#x27;generate description&#x27;, async () =&gt; {&#10;			const imageArray = Array.from(new Uint8Array(imageData));&#10;			return await this.env.AI.run(&#x27;@cf/llava-hf/llava-1.5-7b-hf&#x27;, {&#10;				image: imageArray,&#10;				prompt: &#x27;Describe this image in one sentence&#x27;,&#10;				max_tokens: 50,&#10;			});&#10;		});&#10;&#10;		await step.waitForEvent(&#x27;await approval&#x27;, {&#10;			event: &#x27;approved&#x27;,&#10;			timeout: &#x27;24 hours&#x27;,&#10;		});&#10;&#10;		await step.do(&#x27;publish&#x27;, async () =&gt; {&#10;			await this.env.BUCKET.put(`public/${event.payload.imageKey}`, imageData);&#10;		});&#10;	}&#10;}&#10;</code></pre>
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
