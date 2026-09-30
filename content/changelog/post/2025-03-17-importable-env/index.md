---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/
  description: New updates and improvements at Cloudflare.
  full_title: Import `env` to access bindings in your Worker's global scope · Changelog
  head_html: <title>Import `env` to access bindings in your Worker&#x27;s global scope · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Import `env` to access bindings in your Worker&#x27;s global scope · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/#page","headline":"Import `env` to access bindings in your Worker's global scope \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-03-17-importable-env/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 17, 2025</time><h2 id="post-title">Import `env` to access bindings in your Worker's global scope</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now access <a href="/workers/runtime-apis/bindings/">bindings</a>
from anywhere in your Worker by importing the <code>env</code> object from <code>cloudflare:workers</code>.</p>
<p>Previously, <code>env</code> could only be accessed during a request. This meant that
bindings could not be used in the top-level context of a Worker.</p>
<p>Now, you can import <code>env</code> and access bindings such as <a href="/workers/configuration/secrets/">secrets</a>
or <a href="/workers/configuration/environment-variables/">environment variables</a> in the
initial setup for your Worker:</p>
<pre tabindex="0"><code class="language-js">import { env } from &quot;cloudflare:workers&quot;;&#10;import ApiClient from &quot;example-api-client&quot;;&#10;&#10;// API_KEY and LOG_LEVEL now usable in top-level scope&#10;const apiClient = ApiClient.new({ apiKey: env.API_KEY });&#10;const LOG_LEVEL = env.LOG_LEVEL || &quot;info&quot;;&#10;&#10;export default {&#10;	fetch(req) {&#10;		// you can use apiClient or LOG_LEVEL, configured before any request is handled&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17767.md")</aside>
<p>Additionally, <code>env</code> was normally accessed as a argument to a Worker's entrypoint handler,
such as <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a>.
This meant that if you needed to access a binding from a deeply nested function,
you had to pass <code>env</code> as an argument through many functions to get it to the
right spot. This could be cumbersome in complex codebases.</p>
<p>Now, you can access the bindings from anywhere in your codebase
without passing <code>env</code> as an argument:</p>
<pre tabindex="0"><code class="language-js">// helpers.js&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;// env is *not* an argument to this function&#10;export async function getValue(key) {&#10;	let prefix = env.KV_PREFIX;&#10;	return await env.KV.get(`${prefix}-${key}`);&#10;}&#10;</code></pre>
<p>For more information, see <a href="/workers/runtime-apis/bindings#how-to-access-env">documentation on accessing <code>env</code></a>.</p>
</div></article></div>
