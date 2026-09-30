---
cp9:
  canonical: https://developers.cloudflare.com/workflows/build/visualizer/
  description: View a visual diagram of your Workflow steps, conditionals, and parallel logic in the Cloudflare dashboard.
  full_title: Visualize Workflows · Cloudflare Workflows docs
  head_html: <title>Visualize Workflows · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="View a visual diagram of your Workflow steps, conditionals, and parallel logic in the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/workflows/build/visualizer/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/build/visualizer/index.md"><meta property="og:title" content="Visualize Workflows · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View a visual diagram of your Workflow steps, conditionals, and parallel logic in the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/workflows/build/visualizer/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/build/visualizer/#page","headline":"Visualize Workflows \u00b7 Cloudflare Workflows docs","description":"View a visual diagram of your Workflow steps, conditionals, and parallel logic in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/workflows/build/visualizer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/build/visualizer/
  schema: 1
---
<p>View a visual representation of your parsed Workflow code as a diagram on the Cloudflare dashboard.</p>
<p>The diagram illustrates your sequenced &amp; parallel steps, conditionals, loops, and nested logic. To see the Workflow at a high level, view the diagram with loops and conditionals collapsed, or expand for a more detailed view.</p>
<p><img src="/assets/upstream/images/changelog/workflows/2026-02-03-workflows-diagram.png" alt="Example diagram" /></p>
<p>Workflow diagrams are currently in beta for all Typescript and Javascript Workers. View your Workflows in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a> to see their diagrams.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17544.md")
</aside>
<h2 id="node-types">Node types</h2>
<p>The diagrams consist of the following node types:</p>
<table>
<thead>
<tr>
<th>Node type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>StepSleep</code></td>
<td>Pauses Workflow execution for a specified duration.</td>
</tr>
<tr>
<td><code>StepDo</code></td>
<td>Represents a named, retriable step that wraps a unit of work.</td>
</tr>
<tr>
<td><code>StepWaitForEvent</code></td>
<td>Suspends execution until an external event is received.</td>
</tr>
<tr>
<td><code>StepSleepUntil</code></td>
<td>Pauses Workflow execution until a specific date and time.</td>
</tr>
<tr>
<td><code>LoopNode</code></td>
<td>Represents a loop construct (<code>for</code>, <code>while</code>, etc.) that repeats a block of logic.</td>
</tr>
<tr>
<td><code>ParallelNode</code></td>
<td>Groups steps that execute concurrently, such as those inside <code>Promise.all()</code>.</td>
</tr>
<tr>
<td><code>TryNode</code></td>
<td>Represents a <code>try...catch</code> block that handles errors within a Workflow.</td>
</tr>
<tr>
<td><code>BlockNode</code></td>
<td>Groups a sequence of steps into a logical block for display purposes.</td>
</tr>
<tr>
<td><code>IfNode</code></td>
<td>Represents a conditional branch based on an <code>if/else</code> expression.</td>
</tr>
<tr>
<td><code>SwitchNode</code></td>
<td>Represents a <code>switch</code> statement that routes execution across multiple cases.</td>
</tr>
<tr>
<td><code>StartNode</code></td>
<td>Marks the entry point of the Workflow or a function definition.</td>
</tr>
<tr>
<td><code>FunctionCall</code></td>
<td>Represents a call to a named function within the Workflow code.</td>
</tr>
<tr>
<td><code>FunctionDef</code></td>
<td>Represents the definition of a function used within the Workflow.</td>
</tr>
<tr>
<td><code>BreakNode</code></td>
<td>Represents a <code>break</code> statement that exits a loop early.</td>
</tr>
</tbody>
</table>
<h2 id="execution-order">Execution order</h2>
<p>Each node has a <code>starts</code> and <code>resolves</code> field that tracks execution order. These indices indicate when a promise began executing and when it ended, relative to the first promise that started without an immediate conclusion. This corresponds to vertical positioning in the diagram (i.e. all steps with <code>starts: 1</code> will appear inline).</p>
<p>When parsing, unawaited promises or <code>Promise.all()</code> calls are assigned an entry number stored in the <code>starts</code> field. When an <code>await</code> is encountered for that promise, the entry number is incremented and saved as the exit number in the <code>resolves</code> field. This allows the diagram to determine which promises run concurrently and when each will complete relative to the others.</p>
<p>If steps are awaited at the point of declaration, <code>starts</code> and <code>resolves</code> will be undefined, and the Workflow executes in the order the steps appear to the runtime.</p>
