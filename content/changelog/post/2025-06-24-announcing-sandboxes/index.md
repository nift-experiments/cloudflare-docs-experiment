---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/
  description: New updates and improvements at Cloudflare.
  full_title: Run AI-generated code on-demand with Code Sandboxes (new) · Changelog
  head_html: <title>Run AI-generated code on-demand with Code Sandboxes (new) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Run AI-generated code on-demand with Code Sandboxes (new) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/#page","headline":"Run AI-generated code on-demand with Code Sandboxes (new) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-06-24-announcing-sandboxes/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 25, 2025</time><h2 id="post-title">Run AI-generated code on-demand with Code Sandboxes (new)</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span><span>workflows</span></div><div class="changelog-body"><p>AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing <a href="https://www.npmjs.com/package/@cloudflare/sandbox">Sandboxes</a>, which let your Worker run actual processes in a secure, container-based environment.</p>
<pre tabindex="0"><code class="language-ts">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;		return sandbox.exec(&quot;ls&quot;, [&quot;-la&quot;]);&#10;	},&#10;};&#10;</code></pre>
<h4 id="methods">Methods</h4>
<ul>
<li><code>exec(command: string, args: string[], options?: { stream?: boolean })</code>:Execute a command in the sandbox.</li>
<li><code>gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })</code>: Checkout a git repository in the sandbox.</li>
<li><code>mkdir(path: string, options: { recursive?: boolean; stream?: boolean })</code>: Create a directory in the sandbox.</li>
<li><code>writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })</code>: Write content to a file in the sandbox.</li>
<li><code>readFile(path: string, options: { encoding?: string; stream?: boolean })</code>: Read content from a file in the sandbox.</li>
<li><code>deleteFile(path: string, options?: { stream?: boolean })</code>: Delete a file from the sandbox.</li>
<li><code>renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })</code>: Rename a file in the sandbox.</li>
<li><code>moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })</code>: Move a file from one location to another in the sandbox.</li>
<li><code>ping()</code>: Ping the sandbox.</li>
</ul>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
<p>You can try it today from your Worker, with just a few lines of code. Let us know what you build.</p>
</div></article></div>
