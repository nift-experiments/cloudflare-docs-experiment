---
cp9:
  canonical: https://developers.cloudflare.com/workflows/examples/wait-for-event/
  description: Human-in-the-loop Workflow with waitForEvent API
  full_title: Human-in-the-Loop Image Tagging with waitForEvent · Cloudflare Workflows docs
  head_html: <title>Human-in-the-Loop Image Tagging with waitForEvent · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Human-in-the-loop Workflow with waitForEvent API"><link rel="canonical" href="https://developers.cloudflare.com/workflows/examples/wait-for-event/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/examples/wait-for-event/index.md"><meta property="og:title" content="Human-in-the-Loop Image Tagging with waitForEvent · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Human-in-the-loop Workflow with waitForEvent API"><meta property="og:url" content="https://developers.cloudflare.com/workflows/examples/wait-for-event/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workflows"><meta name="pcx_tags" content="Typescript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/examples/wait-for-event/#page","headline":"Human-in-the-Loop Image Tagging with waitForEvent \u00b7 Cloudflare Workflows docs","description":"Human-in-the-loop Workflow with waitForEvent API","url":"https://developers.cloudflare.com/workflows/examples/wait-for-event/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Typescript"]}</script>
  markdown: true
  noindex: false
  route: /workflows/examples/wait-for-event/
  schema: 1
---
<p class="article-summary">Implement a Cloudflare Workflow that processes user-uploaded images, awaits human approval, and performs AI-based image tagging upon approval.</p>
<p>This example demonstrates how to use the <code>waitForEvent()</code> API in Cloudflare Workflows to introduce a human-in-the-loop step. The Workflow is triggered by an image upload, during which metadata is stored in a D1 database. The Workflow then waits for user approval, and upon approval, it uses Workers AI to generate image tags, which are stored in the database. An accompanying Next.js frontend application facilitates the image upload and approval process.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17522.md")
</aside>
<h2 id="overview-of-the-workflow">Overview of the Workflow</h2>
<p>In this Workflow, we simulate a scenario where an uploaded image requires human approval before AI-based processing. An image is uploaded to R2, then Workflow performs the following steps:</p>
<ol>
<li>Stores image metadata in a D1 database.</li>
<li>Pauses execution using <code>waitForEvent()</code> and waits for an external event sent from the Next.js frontend, indicating approval or rejection.</li>
<li>If approved, the Workflow uses Workers AI to generate image tags and stores the tags in the D1 database.</li>
<li>If rejected, the Workflow ends without further action.</li>
</ol>
<p>This pattern is useful in scenarios where certain operations should not proceed without explicit human consent, adding an extra layer of control and safety.</p>
<h2 id="frontend-integration">Frontend Integration</h2>
<p>This example includes a Next.js frontend application that facilitates the image upload and approval process. The frontend provides an interface for uploading images, reviewing them, and approving or rejecting them. Upon image upload, the application triggers the Cloudflare Workflow, which then manages the subsequent steps, including waiting for user approval and performing AI-based image tagging upon approval.</p>
<p>Refer to the <code>/nextjs-workflow-frontend</code> folder in the <a href="https://github.com/cloudflare/docs-examples/tree/main/workflows/waitForEvent">GitHub repository</a> for the complete frontend implementation and deployment details.</p>
<h2 id="workflow-index-ts">Workflow index.ts</h2>
<p>The <code>index.ts</code> file defines the core logic of the Cloudflare Workflow responsible for handling image uploads, awaiting human approval, and performing AI-based image tagging upon approval. It extends the <code>WorkflowEntrypoint</code> class and implements the <code>run()</code> method.</p>
<p>For the complete implementation of the <code>index.ts</code> file, please refer to the <a href="https://github.com/cloudflare/docs-examples/blob/main/workflows/waitForEvent/workflow/src/index.ts">GitHub repository</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17523.md")
</div>
<h2 id="workflow-wrangler-jsonc">Workflow wrangler.jsonc</h2>
<p>The Workflow configuration is defined in the <code>wrangler.jsonc</code> file. This file includes bindings for the R2 bucket, D1 database, Workers AI, and the Workflow itself. Ensure that all necessary bindings and environment variables are correctly set up to match your Cloudflare account and services.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17524.md")
</div>
<p>For access to the codebase, deployment instructions, and reference architecture, please visit the <a href="https://github.com/cloudflare/docs-examples/tree/main/workflows/waitForEvent">GitHub repository</a>. This resource provides all the necessary tools and information to effectively implement the Workflow and Next.js frontend application.</p>
