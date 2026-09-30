---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/
  description: Connect a sandbox to an Artifacts repo.
  full_title: Sandbox SDK + Artifacts · Cloudflare Artifacts docs
  head_html: <title>Sandbox SDK + Artifacts · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect a sandbox to an Artifacts repo."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/index.md"><meta property="og:title" content="Sandbox SDK + Artifacts · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect a sandbox to an Artifacts repo."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/#page","headline":"Sandbox SDK + Artifacts \u00b7 Cloudflare Artifacts docs","description":"Connect a sandbox to an Artifacts repo.","url":"https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/examples/sandbox-sdk-artifacts/
  schema: 1
---
<p>This example uses the <code>git-repo-per-sandbox</code> Sandbox SDK template and highlights the Artifacts-specific pieces.</p>
<p>Start from the template with <code>create cloudflare</code>, as shown in <a href="/sandbox/tutorials/claude-code/#1-create-your-project">Run Claude Code on a Sandbox</a>. Then adapt the Artifacts flow with the focused snippets below.</p>
<ul>
<li>Creates or reuses a sandbox by ID.</li>
<li>Creates or reuses an Artifacts repo with the same ID.</li>
<li>Passes an authenticated Git remote into the sandbox as <code>ARTIFACTS_GIT_REMOTE</code>.</li>
</ul>
<h2 id="create-your-project">Create your project</h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox" aria-label="Copy to clipboard">Copy</button></div></div>
<pre tabindex="0"><code class="language-sh">cd repo-per-sandbox&#10;</code></pre>
<h2 id="1-create-or-reuse-the-repo"><ol>
<li>Create or reuse the repo</li>
</ol></h2>
<p>The template keeps one Artifacts repo per sandbox ID. Use your own source of truth to decide whether this request should create a new repo or load an existing one.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3313.md")
</div>
<p>The template already knows the repo name, so start with direct lookup instead of scanning <code>list()</code> pages. Avoid broad <code>catch</code> blocks here. They can hide missing-repo, auth, and validation failures behind the same retry message.</p>
<p>If your flow can race with repo creation, handle that retry at the application level after you inspect the thrown error.</p>
<h2 id="2-create-or-reuse-the-sandbox"><ol start="2">
<li>Create or reuse the sandbox</li>
</ol></h2>
<p>Use the same ID for the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3314.md")
</div>
<h2 id="3-pass-the-repo-into-the-sandbox"><ol start="3">
<li>Pass the repo into the sandbox</li>
</ol></h2>
<p>Convert the write token into an authenticated Git remote, then store it as an environment variable inside the sandbox.</p>
<p>Use a short-lived token and pass it into the sandbox only after the sandbox session is authorized to push changes.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3315.md")
</div>
<p>Code running inside the sandbox can then use <code>ARTIFACTS_GIT_REMOTE</code> with <code>git clone</code>, <code>git fetch</code>, <code>git pull</code>, or <code>git push</code>.</p>
