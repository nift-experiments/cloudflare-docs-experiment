---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/
  description: REST API and TypeScript SDK examples for deploying Workers programmatically.
  full_title: API examples · Cloudflare for Platforms docs
  head_html: <title>API examples · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="REST API and TypeScript SDK examples for deploying Workers programmatically."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/index.md"><meta property="og:title" content="API examples · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="REST API and TypeScript SDK examples for deploying Workers programmatically."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare for Platforms"><meta name="pcx_tags" content="REST API,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/#page","headline":"API examples \u00b7 Cloudflare for Platforms docs","description":"REST API and TypeScript SDK examples for deploying Workers programmatically.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/
  schema: 1
---
<p>The following examples show how to use Cloudflare's REST API and TypeScript SDK to deploy and manage Workers programmatically.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before using these examples, you need:</p>
<ul>
<li>Your <strong>Account ID</strong> - Found in the Cloudflare dashboard URL or API settings</li>
<li>A <strong>dispatch namespace</strong> - Created via the <a href="/cloudflare-for-platforms/workers-for-platforms/get-started/">dashboard</a></li>
<li>An <strong>API token</strong> with Workers permissions - Create one at <a href="https://dash.cloudflare.com/profile/api-tokens">API Tokens</a></li>
</ul>
<p>For SDK examples, install the Cloudflare SDK:</p>
<pre tabindex="0"><code class="language-sh">npm install cloudflare&#10;</code></pre>
<h3 id="deploy-a-user-worker">Deploy a user Worker</h3>
<p>Upload a Worker script to your dispatch namespace. This is the primary operation your platform performs when customers deploy code.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="deployMethod"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4192.md")
</div></div>
<h3 id="deploy-with-bindings-and-tags">Deploy with bindings and tags</h3>
<p>Use <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">bindings</a> to give each user Worker its own resources like a KV store or database. Use <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/tags/">tags</a> to organize Workers by customer ID, project ID, or plan type for bulk operations.</p>
<p>The following example shows how to deploy a Worker with its own KV namespace and tags attached:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="deployMethod"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4195.md")
</div></div>
<p>For more information, refer to <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">Bindings</a> and <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/tags/">Tags</a>.</p>
<h3 id="deploy-a-worker-with-static-assets">Deploy a Worker with static assets</h3>
<p>Deploy a Worker that serves static files (HTML, CSS, JavaScript, images). This is a three-step process:</p>
<ol>
<li>Create an upload session with a manifest of files</li>
<li>Upload the asset files</li>
<li>Deploy the Worker with the assets binding</li>
</ol>
<p>For more details on static assets configuration and options, refer to <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/">Static assets</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="deployMethod"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4198.md")
</div></div>
<h3 id="list-workers-in-a-namespace">List Workers in a namespace</h3>
<p>Retrieve all user Workers deployed to a namespace.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="deployMethod"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4201.md")
</div></div>
<h3 id="delete-workers-by-tag">Delete Workers by tag</h3>
<p>Delete all Workers matching a tag filter. This is useful when a customer deletes their account and you need to remove all their Workers at once.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="deployMethod"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4204.md")
</div></div>
<h3 id="delete-a-single-worker">Delete a single Worker</h3>
<p>Delete a specific Worker by name.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="deployMethod"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4207.md")
</div></div>
