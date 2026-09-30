---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/tutorials/persistent-storage/
  description: Mount R2 buckets as local filesystem paths to persist data across sandbox lifecycles.
  full_title: Data persistence with R2 · Cloudflare Sandbox SDK docs
  head_html: <title>Data persistence with R2 · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Mount R2 buckets as local filesystem paths to persist data across sandbox lifecycles."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/tutorials/persistent-storage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/tutorials/persistent-storage/index.md"><meta property="og:title" content="Data persistence with R2 · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Mount R2 buckets as local filesystem paths to persist data across sandbox lifecycles."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/tutorials/persistent-storage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Sandbox SDK,R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/tutorials/persistent-storage/#page","headline":"Data persistence with R2 \u00b7 Cloudflare Sandbox SDK docs","description":"Mount R2 buckets as local filesystem paths to persist data across sandbox lifecycles.","url":"https://developers.cloudflare.com/sandbox/tutorials/persistent-storage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/tutorials/persistent-storage/
  schema: 1
---
<p>Mount object storage buckets as local filesystem paths to persist data across sandbox lifecycles. This tutorial uses Cloudflare R2, but the same approach works with any S3-compatible provider.</p>
<p>This tutorial shows how to persist an external data directory mounted at <code>/data</code>. If you want the working project in <code>/workspace</code> to persist, refer to <a href="/sandbox/guides/backup-restore/">Backup and restore</a>.</p>
<p><strong>Time to complete:</strong> 20 minutes</p>
<h2 id="what-you-ll-build">What you'll build</h2>
<p>A Worker that processes data, stores results in an R2 bucket mounted as a local directory, and demonstrates that data persists even after the sandbox is destroyed and recreated.</p>
<p><strong>Key concepts you'll learn</strong>:</p>
<ul>
<li>Mounting R2 buckets as filesystem paths</li>
<li>Automatic data persistence across sandbox lifecycles</li>
<li>Working with mounted storage using standard file operations</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13306.md")
</div></details>
<p>You'll also need:</p>
<ul>
<li><a href="https://www.docker.com/">Docker</a> running locally</li>
<li>An R2 bucket (create one in the <a href="https://dash.cloudflare.com/?to=/:account/r2">Cloudflare dashboard</a>)</li>
</ul>
<h2 id="1-create-your-project"><ol>
<li>Create your project</li>
</ol></h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- data-pipeline --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- data-pipeline --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare data-pipeline --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare data-pipeline --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest data-pipeline --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest data-pipeline --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div></div>
<pre tabindex="0"><code class="language-sh">cd data-pipeline&#10;</code></pre>
<h2 id="2-configure-r2-binding"><ol start="2">
<li>Configure R2 binding</li>
</ol></h2>
<p>Add an R2 bucket binding to your <code>wrangler.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;name&quot;: &quot;data-pipeline&quot;,&#10;  &quot;compatibility_date&quot;: &quot;2025-11-09&quot;,&#10;  &quot;durable_objects&quot;: {&#10;    &quot;bindings&quot;: [&#10;      { &quot;name&quot;: &quot;Sandbox&quot;, &quot;class_name&quot;: &quot;Sandbox&quot; }&#10;    ]&#10;  },&#10;  &quot;r2_buckets&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;DATA_BUCKET&quot;,&#10;      &quot;bucket_name&quot;: &quot;my-data-bucket&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Replace <code>my-data-bucket</code> with your R2 bucket name. Create the bucket first in the <a href="https://dash.cloudflare.com/?to=/:account/r2">Cloudflare dashboard</a>.</p>
<h2 id="3-build-the-data-processor"><ol start="3">
<li>Build the data processor</li>
</ol></h2>
<p>Replace <code>src/index.ts</code> with code that mounts R2 and processes data:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13307.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="replace-your-account-id">Replace YOUR_ACCOUNT_ID</h3>
@markup("md", "content/.markup/bodies/13305.md")
</aside>
<h2 id="4-deploy-to-production"><ol start="4">
<li>Deploy to production</li>
</ol></h2>
<p><strong>Generate R2 API tokens:</strong></p>
<ol>
<li>Go to <strong>R2</strong> &gt; <strong>Overview</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a></li>
<li>Select <strong>Manage R2 API Tokens</strong></li>
<li>Create a token with <strong>Object Read &amp; Write</strong> permissions</li>
<li>Copy the <strong>Access Key ID</strong> and <strong>Secret Access Key</strong></li>
</ol>
<p><strong>Set up credentials as Worker secrets:</strong></p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put AWS_ACCESS_KEY_ID&#10;&#35; Paste your R2 Access Key ID&#10;&#10;npx wrangler secret put AWS_SECRET_ACCESS_KEY&#10;&#35; Paste your R2 Secret Access Key&#10;</code></pre>
<p>Worker secrets are encrypted and only accessible to your deployed Worker. The SDK automatically detects these credentials when <code>mountBucket()</code> is called.</p>
<p><strong>Deploy your Worker:</strong></p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>After deployment, wrangler outputs your Worker URL (e.g., <code>https://data-pipeline.yourname.workers.dev</code>).</p>
<h2 id="5-test-the-persistence-flow"><ol start="5">
<li>Test the persistence flow</li>
</ol></h2>
<p>Now test against your deployed Worker. Replace <code>YOUR_WORKER_URL</code> with your actual Worker URL:</p>
<pre tabindex="0"><code class="language-sh">&#35; 1. Process data (saves to R2)&#10;curl -X POST https://YOUR_WORKER_URL/process&#10;&#35; Returns: { &quot;message&quot;: &quot;Data processed...&quot;, &quot;result&quot;: { &quot;total&quot;: 144, &quot;average&quot;: 48, ... } }&#10;&#10;&#35; 2. Verify data is accessible&#10;curl https://YOUR_WORKER_URL/results&#10;&#35; Returns the same results from R2&#10;&#10;&#35; 3. Destroy the sandbox&#10;curl -X POST https://YOUR_WORKER_URL/destroy&#10;&#35; Returns: { &quot;message&quot;: &quot;Sandbox destroyed. Data persists in R2!&quot; }&#10;&#10;&#35; 4. Access results again (from new sandbox)&#10;curl https://YOUR_WORKER_URL/results&#10;&#35; Still works! Data persisted across sandbox lifecycle&#10;</code></pre>
<p>The key insight: After destroying the sandbox, the next request creates a new sandbox instance, mounts the same R2 bucket, and finds the data still there.</p>
<h2 id="what-you-learned">What you learned</h2>
<p>In this tutorial, you built a data pipeline that demonstrates filesystem persistence through R2 bucket mounting:</p>
<ul>
<li><strong>Mounting buckets</strong>: Use <code>mountBucket()</code> to make R2 accessible as a local directory</li>
<li><strong>Standard file operations</strong>: Access mounted buckets using familiar filesystem commands (<code>cat</code>, Python <code>open()</code>, etc.)</li>
<li><strong>Automatic persistence</strong>: Data written to mounted directories survives sandbox destruction</li>
<li><strong>Choose the right persistence model</strong>: Use bucket mounts for external storage directories such as <code>/data</code>, and consider backup and restore when you need a persistent workspace under <code>/workspace</code></li>
<li><strong>Credential management</strong>: Configure R2 access using environment variables or explicit credentials</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/sandbox/guides/mount-buckets/">Mount buckets guide</a> - Comprehensive mounting reference</li>
<li><a href="/sandbox/api/storage/">Storage API</a> - Complete API documentation</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> - Credential configuration options</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/r2/">R2 documentation</a> - Learn about Cloudflare R2</li>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> - Long-running data processing</li>
<li><a href="/sandbox/concepts/sandboxes/">Sandboxes concept</a> - Understanding sandbox lifecycle</li>
</ul>
