---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/
  description: Search a shared knowledge base and a tenant-specific one in a single query, and identify which instance each result came from.
  full_title: Search across multiple instances · Cloudflare AI Search docs
  head_html: <title>Search across multiple instances · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Search a shared knowledge base and a tenant-specific one in a single query, and identify which instance each result came from."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/index.md"><meta property="og:title" content="Search across multiple instances · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Search a shared knowledge base and a tenant-specific one in a single query, and identify which instance each result came from."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/#page","headline":"Search across multiple instances \u00b7 Cloudflare AI Search docs","description":"Search a shared knowledge base and a tenant-specific one in a single query, and identify which instance each result came from.","url":"https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/how-to/search-multiple-sources/
  schema: 1
---
<p>AI Search can query several instances in one request, merge the results, and tag each result with the instance it came from. This guide uses that to search two knowledge bases together: a shared <strong>general</strong> knowledge base that every user can search, plus a <strong>tenant-specific</strong> knowledge base that holds one customer's private content. A single query returns relevant content from both.</p>
<p>Keeping each tenant's content in its own instance is the recommended way to isolate tenants (refer to <a href="/ai-search/how-to/per-tenant-search/">Multi-tenant search isolation</a>). Searching across instances then lets you combine a tenant's instance with shared content at query time, so you do not have to copy the shared content into every tenant's instance.</p>
<p><strong>What you will build:</strong> A Worker that searches a shared <code>general-knowledge</code> instance and a per-tenant instance together, then groups the results by their source.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3006.md")
</div></details>
<p>The instances you search across must belong to the same <a href="/ai-search/concepts/namespaces/">namespace</a>. This guide creates them for you.</p>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>multi-source-search</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- multi-source-search</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- multi-source-search" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare multi-source-search</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare multi-source-search" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest multi-source-search</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest multi-source-search" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre tabindex="0"><code class="language-sh">cd multi-source-search&#10;</code></pre>
<h2 id="2-configure-wrangler"><ol start="2">
<li>Configure Wrangler</li>
</ol></h2>
<p>Add an <a href="/ai-search/concepts/namespaces/">AI Search namespace binding</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. Searching across instances is a method on the namespace binding, so a single binding can reach every instance in the namespace.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3007.md")
</div>
<p>The <code>remote</code> option lets <code>wrangler dev</code> proxy requests to your deployed instances, since AI Search does not run locally.</p>
<h2 id="3-add-the-worker-code"><ol start="3">
<li>Add the Worker code</li>
</ol></h2>
<p>Update <code>src/index.ts</code>. This Worker identifies the tenant from a request header, then searches the shared instance and that tenant's instance in one call. Each returned chunk carries an <code>instance_id</code>, so the Worker can group results by source.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3008.md")
</div>
<p><code>env.AI_SEARCH.search()</code> is the namespace-level search. It differs from <code>env.AI_SEARCH.get(id).search()</code>, which searches a single instance. Passing <code>instance_ids</code> fans the query out across those instances and returns one merged, ranked list of chunks. Because every chunk includes an <code>instance_id</code>, you always know whether a result came from the shared instance or the tenant's instance.</p>
<p>If one instance fails, for example because the ID does not exist, the others still return, and the failure is reported in <code>errors</code> instead of throwing. This makes a missing tenant instance a partial result rather than a hard error.</p>
<h2 id="4-run-it"><ol start="4">
<li>Run it</li>
</ol></h2>
<p>Start a local development server:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Send a request with a tenant header and a query. The first request takes a moment because it creates and seeds the instances:</p>
<pre tabindex="0"><code class="language-sh">curl &quot;http://localhost:8787/?q=support+hours+and+my+plan&quot; -H &quot;x-tenant-id: acme&quot;&#10;</code></pre>
<p>The response separates results from the shared instance and the tenant instance:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;query&quot;: &quot;support hours and my plan&quot;,&#10;	&quot;general&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;support-hours.md&quot;,&#10;			&quot;text&quot;: &quot;# Support hours\nSupport is available...&quot;&#10;		}&#10;	],&#10;	&quot;tenant&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;plan.md&quot;,&#10;			&quot;text&quot;: &quot;# Your plan\nThis account is on the Enterprise plan...&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>When every instance succeeds, the response has no <code>errors</code> field. If an instance fails, an <code>errors</code> array lists the failures while the other instances' results are still returned.</p>
<h2 id="5-generate-an-answer-over-both-instances"><ol start="5">
<li>Generate an answer over both instances</li>
</ol></h2>
<p>To return a single written answer grounded in both instances instead of raw chunks, use <code>chatCompletions</code> with the same <code>instance_ids</code>. It retrieves from every listed instance, then generates one response from the combined context:</p>
<pre tabindex="0"><code class="language-ts">const completion = await env.AI_SEARCH.chatCompletions({&#10;	query,&#10;	ai_search_options: {&#10;		instance_ids: [GENERAL_INSTANCE, tenantInstance(tenantId)],&#10;	},&#10;});&#10;&#10;// The generated answer, grounded in both the shared and tenant content.&#10;const answer = completion.choices[0]?.message.content;&#10;</code></pre>
<p>The response also includes the retrieved <code>chunks</code> (each tagged with its <code>instance_id</code>) so you can cite sources, and an <code>errors</code> array for any instance that failed.</p>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<p>Log in with your Cloudflare account, then deploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-multi-tenant-search-isolation-ai-search-how-to-per-tenant-search"><a href="/ai-search/how-to/per-tenant-search/">Multi-tenant search isolation</a></h3><p>Give each tenant its own instance, or share one instance with metadata filtering.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-namespaces-ai-search-concepts-namespaces"><a href="/ai-search/concepts/namespaces/">Namespaces</a></h3><p>How instances are grouped, and how the namespace binding addresses them.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-search-workers-binding-ai-search-api-search-workers-binding"><a href="/ai-search/api/search/workers-binding/">Search Workers binding</a></h3><p>Full reference for single-instance and multi-instance search and chat.</p></div>
