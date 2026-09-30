---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/
  description: New updates and improvements at Cloudflare.
  full_title: Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes · Changelog
  head_html: <title>Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/#page","headline":"Terraform provider improvements\u00a0\u2014\u00a0Python Workers support, smaller plan diffs, and API SDK fixes \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 14, 2025</time><h2 id="post-title">Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The recent <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script">Cloudflare Terraform Provider</a> and SDK releases (such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a>) bring significant improvements to the Workers developer experience. These updates focus on reliability, performance, and adding <a href="/workers/languages/python/">Python Workers</a> support.</p>
<h4 id="terraform-improvements">Terraform Improvements</h4>
<h4 id="fixed-unwarranted-plan-diffs">Fixed Unwarranted Plan Diffs</h4>
<p>Resolved several issues with the <code>cloudflare_workers_script</code> resource that resulted in unwarranted plan diffs, including:</p>
<ul>
<li>Using Durable Objects migrations</li>
<li>Using some bindings such as <code>secret_text</code></li>
<li>Using smart placement</li>
</ul>
<p>A resource should never show a plan diff if there isn't an actual change. This fix reduces unnecessary noise in your Terraform plan and is available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="improved-file-management">Improved File Management</h4>
<p>You can now specify <code>content_file</code> and <code>content_sha256</code> instead of <code>content</code>. This prevents the Workers script content from being stored in the state file which greatly reduces plan diff size and noise. If your workflow synced plans remotely, this should now happen much faster since there is less data to sync. This is available in Cloudflare Terraform Provider 5.7.0.</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;}&#10;</code></pre>
<h4 id="assets-headers-and-redirects-support">Assets Headers and Redirects Support</h4>
<p>Fixed the <code>cloudflare_workers_script</code> resource to properly support headers and redirects for Assets:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;  assets = {&#10;    config = {&#10;      headers = file(&quot;_headers&quot;)&#10;      redirects = file(&quot;_redirects&quot;)&#10;    }&#10;    &#35; Completion jwt from:&#10;    &#35; https://developers.cloudflare.com/api/resources/workers/subresources/assets/subresources/upload/&#10;    jwt = &quot;jwt&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="python-workers-support">Python Workers Support</h4>
<p>Added support for uploading <a href="/workers/languages/python/">Python Workers</a> (beta) in Terraform. You can now deploy Python Workers with:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id       = &quot;123456789&quot;&#10;  script_name      = &quot;my_worker&quot;&#10;  content_file     = &quot;worker.py&quot;&#10;  content_sha256   = filesha256(&quot;worker.py&quot;)&#10;  content_type     = &quot;text/x-python&quot;&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="sdk-enhancements">SDK Enhancements</h4>
<h4 id="improved-file-upload-api">Improved File Upload API</h4>
<p>Fixed an issue where Workers script versions in the SDK did not allow uploading files. This now works, and also has an improved files upload interface:</p>
<pre tabindex="0"><code class="language-js">const scriptContent = `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      return new Response(&#x27;Hello World!&#x27;, { status: 200 });&#10;    }&#10;  };&#10;`;&#10;&#10;client.workers.scripts.versions.create(&#x27;my-worker&#x27;, {&#10;  account_id: &#x27;123456789&#x27;,&#10;  metadata: {&#10;    main_module: &#x27;my-worker.mjs&#x27;,&#10;  },&#10;  files: [&#10;    await toFile(&#10;      Buffer.from(scriptContent),&#10;      &#x27;my-worker.mjs&#x27;,&#10;      {&#10;        type: &quot;application/javascript+module&quot;,&#10;      }&#10;    )&#10;  ]&#10;});&#10;</code></pre>
<p>Will be available in cloudflare-typescript 4.6.0. A similar change will be available in cloudflare-python 4.4.0.</p>
<h4 id="fixed-updating-kv-values">Fixed updating KV values</h4>
<p>Previously when creating a KV value like this:</p>
<pre tabindex="0"><code class="language-js">await cf.kv.namespaces.values.update(&quot;my-kv-namespace&quot;, &quot;key1&quot;, {&#10;  account_id: &quot;123456789&quot;,&#10;  metadata: &quot;my metadata&quot;,&#10;  value: JSON.stringify({&#10;    hello: &quot;world&quot;&#10;  })&#10;});&#10;</code></pre>
<p>...and recalling it in your Worker like this:</p>
<pre tabindex="0"><code class="language-ts">const value = await c.env.KV.get&lt;{hello: string}&gt;(&quot;key1&quot;, &quot;json&quot;);&#10;</code></pre>
<p>You'd get back this: <code>{metadata:'my metadata', value:&quot;{'hello':'world'}&quot;}</code> instead of the correct value of <code>{hello: 'world'}</code></p>
<p>This is fixed in cloudflare-typescript 4.5.0 and will be fixed in cloudflare-python 4.4.0.</p>
</div></article></div>
