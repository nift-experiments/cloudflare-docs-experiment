---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/
  description: Use the Node.js fs module in Cloudflare Workers to access a virtual file system for reading and writing files.
  full_title: fs · Cloudflare Workers docs
  head_html: <title>fs · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js fs module in Cloudflare Workers to access a virtual file system for reading and writing files."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/index.md"><meta property="og:title" content="fs · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js fs module in Cloudflare Workers to access a virtual file system for reading and writing files."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/#page","headline":"fs \u00b7 Cloudflare Workers docs","description":"Use the Node.js fs module in Cloudflare Workers to access a virtual file system for reading and writing files.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/fs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/fs/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17152.md")
</aside>
<p>You can use <a href="https://nodejs.org/api/fs.html"><code>node:fs</code></a> to access a virtual file
system in Workers.</p>
<p>The <code>node:fs</code> module is available in Workers runtimes that support Node.js
compatibility using the <code>nodejs_compat</code> compatibility flag. Any Worker
running with <code>nodejs_compat</code> enabled and with a compatibility date of
<code>2025-09-01</code> or later will have access to <code>node:fs</code> by default. It is
also possible to enable <code>node:fs</code> on Workers with an earlier compatibility
date using a combination of the <code>nodejs_compat</code> and <code>enable_nodejs_fs_module</code>
flags. To disable <code>node:fs</code> you can set the <code>disable_nodejs_fs_module</code> flag.</p>
<pre tabindex="0"><code class="language-js">import { readFileSync, writeFileSync } from &quot;node:fs&quot;;&#10;&#10;const config = readFileSync(&quot;/bundle/config.txt&quot;, &quot;utf8&quot;);&#10;&#10;writeFileSync(&quot;/tmp/abc.txt&quot;, &quot;Hello, world!&quot;);&#10;</code></pre>
<p>The Workers Virtual File System (VFS) is a memory-based file system that allows
you to read modules included in your Worker bundle as read-only files, access a
directory for writing temporary files, or access common
<a href="https://linux-kernel-labs.github.io/refs/heads/master/labs/device_drivers.html">character devices</a> like
<code>/dev/null</code>, <code>/dev/random</code>, <code>/dev/full</code>, and <code>/dev/zero</code>.</p>
<p>The directory structure initially looks like:</p>
<pre tabindex="0"><code>&#10;/bundle&#10;└── (one file for each module in your Worker bundle)&#10;/tmp&#10;└── (empty, but you can write files, create directories, symlinks, etc)&#10;/dev&#10;├── null&#10;├── random&#10;├── full&#10;└── zero&#10;</code></pre>
<p>The <code>/bundle</code> directory contains the files for all modules included in your
Worker bundle, which you can read using APIs like <code>readFileSync</code> or
<code>read(...)</code>, etc. These are always read-only. Reading from the bundle
can be useful when you need to read a config file or a template.</p>
<pre tabindex="0"><code class="language-js">import { readFileSync } from &quot;node:fs&quot;;&#10;&#10;// The config.txt file would be included in your Worker bundle.&#10;// Refer to the Wrangler documentation for details on how to&#10;// include additional files.&#10;const config = readFileSync(&quot;/bundle/config.txt&quot;, &quot;utf8&quot;);&#10;&#10;export default {&#10;	async fetch(request) {&#10;		return new Response(`Config contents: ${config}`);&#10;	},&#10;};&#10;</code></pre>
<p>The <code>/tmp</code> directory is writable, and you can use it to create temporary files
or directories. You can also create symlinks in this directory. However, the
contents of <code>/tmp</code> are not persistent and are unique to each request. This means
that files created in <code>/tmp</code> within the context of one request will not be
available in other concurrent or subsequent requests.</p>
<pre tabindex="0"><code class="language-js">import { writeFileSync, readFileSync } from &quot;node:fs&quot;;&#10;&#10;export default {&#10;	fetch(request) {&#10;		// The file `/tmp/hello.txt` will only exist for the duration&#10;		// of this request.&#10;		writeFileSync(&quot;/tmp/hello.txt&quot;, &quot;Hello, world!&quot;);&#10;		const contents = readFileSync(&quot;/tmp/hello.txt&quot;, &quot;utf8&quot;);&#10;		return new Response(`File contents: ${contents}`);&#10;	},&#10;};&#10;</code></pre>
<p>The <code>/dev</code> directory contains common character devices:</p>
<ul>
<li><code>/dev/null</code>: A null device that discards all data written to it and returns
EOF on read.</li>
<li><code>/dev/random</code>: A device that provides random bytes on reads and discards all
data written to it. Reading from <code>/dev/random</code> is only permitted when within
the context of a request.</li>
<li><code>/dev/full</code>: A device that always returns EOF on reads and discards all data
written to it.</li>
<li><code>/dev/zero</code>: A device that provides an infinite stream of zero bytes on reads
and discards all data written to it.</li>
</ul>
<p>All operations on the VFS are synchronous. You can use the synchronous,
asynchronous callback, or promise-based APIs provided by the <code>node:fs</code> module
but all operations will be performed synchronously.</p>
<p>Timestamps for files in the VFS are currently always set to the Unix epoch
(<code>1970-01-01T00:00:00Z</code>). This means that operations that rely on timestamps,
like <code>fs.stat</code>, will always return the same timestamp for all files in the VFS.
This is a temporary limitation that will be addressed in a future release.</p>
<p>Since all temporary files are held in memory, the total size of all temporary
files and directories created count towards your Worker’s memory limit. If you
exceed this limit, the Worker instance will be terminated and restarted.</p>
<p>The file system implementation has the following limits:</p>
<ul>
<li>The maximum total length of a file path is 4096 characters, including path
separators. Because paths are handled as file URLs internally, the limit
accounts for percent-encoding of special characters, decoding characters
that do not need encoding before the limit is checked. For example, the
path <code>/tmp/abcde%66/ghi%zz' is 18 characters long because the </code>%66<code>does not need to be percent-encoded and is therefore counted as one character, while the</code>%zz` is an invalid percent-encoding that is counted as 3 characters.</li>
<li>The maximum number of path segments is 48. For example, the path <code>/a/b/c</code> is
3 segments.</li>
<li>The maximum size of an individual file is 128 MB total.</li>
</ul>
<p>The following <code>node:fs</code> APIs are not supported in Workers, or are only partially
supported:</p>
<ul>
<li><code>fs.watch</code> and <code>fs.watchFile</code> operations for watching for file changes.</li>
<li>The <code>fs.globSync()</code> and other glob APIs have not yet been implemented.</li>
<li>The <code>force</code> option in the <code>fs.rm</code> API has not yet been implemented.</li>
<li>Timestamps for files are always set to the Unix epoch (<code>1970-01-01T00:00:00Z</code>).</li>
<li>File permissions and ownership are not supported.</li>
</ul>
<p>The full <code>node:fs</code> API is documented in the <a href="https://nodejs.org/api/fs.html">Node.js documentation for <code>node:fs</code></a>.</p>
