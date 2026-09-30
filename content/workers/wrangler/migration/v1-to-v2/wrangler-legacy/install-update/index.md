---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/
  description: Install or update Wrangler v1 using npm or Cargo. Now deprecated in favor of the latest Wrangler release.
  full_title: Install / Update · Cloudflare Workers docs
  head_html: <title>Install / Update · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Install or update Wrangler v1 using npm or Cargo. Now deprecated in favor of the latest Wrangler release."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update/index.md"><meta property="og:title" content="Install / Update · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install or update Wrangler v1 using npm or Cargo. Now deprecated in favor of the latest Wrangler release."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/#page","headline":"Install / Update \u00b7 Cloudflare Workers docs","description":"Install or update Wrangler v1 using npm or Cargo. Now deprecated in favor of the latest Wrangler release.","url":"https://developers.cloudflare.com/workers/wrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/migration/v1-to-v2/wrangler-legacy/install-update/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17457.md")
</aside>
<h2 id="install">Install</h2>
<h3 id="install-with-npm">Install with <code>npm</code></h3>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/wrangler -g&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="eaccess-error">EACCESS error</h3>
@markup("md", "content/.markup/bodies/17456.md")
</aside>
<h3 id="install-with-cargo">Install with <code>cargo</code></h3>
<p>Assuming you have Rust’s package manager, <a href="https://github.com/rust-lang/cargo">Cargo</a>, installed, run:</p>
<pre tabindex="0"><code class="language-sh">cargo install wrangler&#10;</code></pre>
<p>Otherwise, to install Cargo, you must first install rustup. On Linux and macOS systems, <code>rustup</code> can be installed as follows:</p>
<pre tabindex="0"><code class="language-sh">curl https://sh.rustup.rs -sSf | sh&#10;</code></pre>
<p>Additional installation methods are available <a href="https://forge.rust-lang.org/other-installation-methods.html">on the Rust site</a>.</p>
<p>Windows users will need to install Perl as a dependency for <code>openssl-sys</code> — <a href="https://www.perl.org/get.html">Strawberry Perl</a> is recommended.</p>
<p>After Cargo is installed, you may now install Wrangler:</p>
<pre tabindex="0"><code class="language-sh">cargo install wrangler&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="customize-openssl">Customize OpenSSL</h3>
@markup("md", "content/.markup/bodies/17455.md")
</aside>
<h3 id="manual-install">Manual install</h3>
<ol>
<li>
<p>Download the binary tarball for your platform from the <a href="https://github.com/cloudflare/wrangler-legacy/releases">releases page</a>. You do not need the <code>wranglerjs-*.tar.gz</code> download – Wrangler will install that for you.</p>
</li>
<li>
<p>Unpack the tarball and place the Wrangler binary somewhere on your <code>PATH</code>, preferably <code>/usr/local/bin</code> for Linux/macOS or <code>Program Files</code> for Windows.</p>
</li>
</ol>
<h2 id="update">Update</h2>
<p>To update <a href="https://github.com/cloudflare/wrangler-legacy">Wrangler</a>, run one of the following:</p>
<h3 id="update-with-npm">Update with <code>npm</code></h3>
<pre tabindex="0"><code class="language-sh">npm update -g @cloudflare/wrangler&#10;</code></pre>
<h3 id="update-with-cargo">Update with <code>cargo</code></h3>
<pre tabindex="0"><code class="language-sh">cargo install wrangler --force&#10;</code></pre>
