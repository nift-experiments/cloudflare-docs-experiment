<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17457.md")
</aside>
<h2 id="install">Install</h2>
<h3 id="install-with-npm">Install with <code>npm</code></h3>
<pre><code class="language-sh">npm i @cloudflare/wrangler -g&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="eaccess-error">EACCESS error</h3>
@markup("md", "content/.markup/bodies/17456.md")
</aside>
<h3 id="install-with-cargo">Install with <code>cargo</code></h3>
<p>Assuming you have Rust’s package manager, <a href="https://github.com/rust-lang/cargo">Cargo</a>, installed, run:</p>
<pre><code class="language-sh">cargo install wrangler&#10;</code></pre>
<p>Otherwise, to install Cargo, you must first install rustup. On Linux and macOS systems, <code>rustup</code> can be installed as follows:</p>
<pre><code class="language-sh">curl https://sh.rustup.rs -sSf | sh&#10;</code></pre>
<p>Additional installation methods are available <a href="https://forge.rust-lang.org/other-installation-methods.html">on the Rust site</a>.</p>
<p>Windows users will need to install Perl as a dependency for <code>openssl-sys</code> — <a href="https://www.perl.org/get.html">Strawberry Perl</a> is recommended.</p>
<p>After Cargo is installed, you may now install Wrangler:</p>
<pre><code class="language-sh">cargo install wrangler&#10;</code></pre>
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
<pre><code class="language-sh">npm update -g @cloudflare/wrangler&#10;</code></pre>
<h3 id="update-with-cargo">Update with <code>cargo</code></h3>
<pre><code class="language-sh">cargo install wrangler --force&#10;</code></pre>
