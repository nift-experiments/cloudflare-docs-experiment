<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 3, 2026</time><h2 id="post-title">Store Wrangler's OAuth credentials in your OS keychain</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/wrangler/">Wrangler</a> can now store the OAuth credentials returned by <code>wrangler login</code> in an <a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">AES-256-GCM</a>-encrypted file, with the encryption key held in your operating system keychain. The default behavior is unchanged — credentials still live in a plaintext TOML file unless you opt in.</p>
<p>To opt in, run:</p>
<pre><code class="language-sh">npx wrangler login --use-keyring&#10;</code></pre>
<p>The choice is persisted across Wrangler invocations. Opt back out with <code>npx wrangler login --no-use-keyring</code>, or override the preference for a single command with the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
<p><code>wrangler whoami</code> now reports where credentials are stored:</p>
<pre><code class="language-sh">🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)&#10;</code></pre>
<p>Per-platform backends:</p>
<ul>
<li><strong>macOS</strong> uses the built-in Keychain via <code>/usr/bin/security</code>.</li>
<li><strong>Linux</strong> uses <a href="https://wiki.gnome.org/Projects/Libsecret">libsecret</a> via the <code>secret-tool</code> CLI from the <code>libsecret-tools</code> package.</li>
<li><strong>Windows</strong> uses Credential Manager via <a href="https://www.npmjs.com/package/@napi-rs/keyring"><code>@napi-rs/keyring</code></a>, installed on-demand the first time you opt in.</li>
</ul>
<p>Refer to <a href="/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</a> for the full details, including the migration behavior on opt-in/opt-out and the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
</div></article></div>
