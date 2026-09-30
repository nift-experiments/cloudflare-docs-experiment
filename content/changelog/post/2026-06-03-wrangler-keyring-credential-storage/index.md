---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/
  description: New updates and improvements at Cloudflare.
  full_title: Store Wrangler's OAuth credentials in your OS keychain · Changelog
  head_html: <title>Store Wrangler&#x27;s OAuth credentials in your OS keychain · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Store Wrangler&#x27;s OAuth credentials in your OS keychain · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/#page","headline":"Store Wrangler's OAuth credentials in your OS keychain \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-wrangler-keyring-credential-storage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-03-wrangler-keyring-credential-storage/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 3, 2026</time><h2 id="post-title">Store Wrangler's OAuth credentials in your OS keychain</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/wrangler/">Wrangler</a> can now store the OAuth credentials returned by <code>wrangler login</code> in an <a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">AES-256-GCM</a>-encrypted file, with the encryption key held in your operating system keychain. The default behavior is unchanged — credentials still live in a plaintext TOML file unless you opt in.</p>
<p>To opt in, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --use-keyring&#10;</code></pre>
<p>The choice is persisted across Wrangler invocations. Opt back out with <code>npx wrangler login --no-use-keyring</code>, or override the preference for a single command with the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
<p><code>wrangler whoami</code> now reports where credentials are stored:</p>
<pre tabindex="0"><code class="language-sh">🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)&#10;</code></pre>
<p>Per-platform backends:</p>
<ul>
<li><strong>macOS</strong> uses the built-in Keychain via <code>/usr/bin/security</code>.</li>
<li><strong>Linux</strong> uses <a href="https://wiki.gnome.org/Projects/Libsecret">libsecret</a> via the <code>secret-tool</code> CLI from the <code>libsecret-tools</code> package.</li>
<li><strong>Windows</strong> uses Credential Manager via <a href="https://www.npmjs.com/package/@napi-rs/keyring"><code>@napi-rs/keyring</code></a>, installed on-demand the first time you opt in.</li>
</ul>
<p>Refer to <a href="/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</a> for the full details, including the migration behavior on opt-in/opt-out and the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
</div></article></div>
