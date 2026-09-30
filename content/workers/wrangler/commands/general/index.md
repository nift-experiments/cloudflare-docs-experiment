---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/commands/general/
  description: General Wrangler commands for authentication, telemetry, and shell completions.
  full_title: General commands · Cloudflare Workers docs
  head_html: <title>General commands · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="General Wrangler commands for authentication, telemetry, and shell completions."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/commands/general/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/commands/general/index.md"><meta property="og:title" content="General commands · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="General Wrangler commands for authentication, telemetry, and shell completions."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/commands/general/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/commands/general/#page","headline":"General commands \u00b7 Cloudflare Workers docs","description":"General Wrangler commands for authentication, telemetry, and shell completions.","url":"https://developers.cloudflare.com/workers/wrangler/commands/general/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/commands/general/
  schema: 1
---
<p>General Wrangler commands for authentication, telemetry, and shell completions.</p>
<h2 id="docs">docs</h2><p>📚 Open Wrangler's command documentation in your browser</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler docs [SEARCH]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler docs [SEARCH]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler docs [SEARCH]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler docs [SEARCH]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler docs [SEARCH]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler docs [SEARCH]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>search</code> <small>string</small><p>Enter search terms (e.g. the wrangler command) you want to know more about</p>
</li><li><code>--yes</code> <small>boolean</small><p>Takes you to the docs, even if search fails</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h2 id="login"><code>login</code></h2>
<p>Authorize Wrangler with your Cloudflare account using OAuth. Wrangler will attempt to automatically open your web browser to login with your Cloudflare account.</p>
<p>If you prefer to use API tokens for authentication, such as in headless or continuous integration environments, refer to <a href="/workers/ci-cd/">Running Wrangler in CI/CD</a>.</p>
<pre tabindex="0"><code class="language-txt">wrangler login [OPTIONS]&#10;</code></pre>
<ul>
<li><code>--scopes-list</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>List all the available OAuth scopes with descriptions.</li>
</ul>
</li>
<li><code>--scopes</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Allows to choose your set of OAuth scopes. The set of scopes must be entered in a whitespace-separated list,
for example, <code>npx wrangler login --scopes account:read user:read</code>.</li>
</ul>
</li>
<li><code>--browser</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Defaults to <code>true</code>. Automatically opens the OAuth link in your default browser. Use <code>--browser=false</code> to print the link instead of opening it.</li>
</ul>
</li>
<li><code>--callback-host</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Defaults to <code>localhost</code>. Sets the IP or hostname where Wrangler should listen for the OAuth callback. Cannot be combined with <code>--device</code>.</li>
</ul>
</li>
<li><code>--callback-port</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Defaults to <code>8976</code>. Sets the port where Wrangler should listen for the OAuth callback. Cannot be combined with <code>--device</code>.</li>
</ul>
</li>
<li><code>--use-keyring</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Stores the OAuth credentials in your operating system keychain instead of the default plaintext TOML file. Refer to <a href="#storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</a> for details. Use <code>--no-use-keyring</code> to opt back out. The choice is persisted across Wrangler invocations.</li>
</ul>
</li>
<li><code>--device</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Defaults to <code>false</code>. Uses the OAuth 2.0 Device Authorization Grant (<a href="https://www.rfc-editor.org/rfc/rfc8628">RFC 8628</a>) instead of the default <code>localhost</code> callback flow. Refer to <a href="#use-wrangler-login-without-a-local-callback-server">Use <code>wrangler login</code> without a local callback server</a>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17441.md")
</aside>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<p>If Wrangler fails to open a browser, you can copy and paste the URL generated by <code>wrangler login</code> in your terminal into a browser and log in.</p>
<h3 id="use-wrangler-login-on-a-remote-machine">Use <code>wrangler login</code> on a remote machine</h3>
<p>If you are using Wrangler from a remote machine, but run the login flow from your local browser, you will receive the following error message after logging in:<code>This site can't be reached</code>.</p>
<p>To finish the login flow, run <code>wrangler login</code> and go through the login flow in the browser:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;</code></pre>
<pre tabindex="0"><code class="language-sh"> ⛅️ wrangler 2.1.6&#10;&#45;------------------&#10;Attempting to login via OAuth...&#10;Opening a link in your default browser: https://dash.cloudflare.com/oauth2/auth?xyz...&#10;</code></pre>
<p>The browser login flow will redirect you to a <code>localhost</code> URL on your machine.</p>
<p>Leave the login flow active. Open a second terminal session. In that second terminal session, use <code>curl</code> or an equivalent request library on the remote machine to fetch this <code>localhost</code> URL. Copy and paste the <code>localhost</code> URL that was generated during the <code>wrangler login</code> flow and run:</p>
<pre tabindex="0"><code class="language-sh">curl &lt;LOCALHOST_URL&gt;&#10;</code></pre>
<p>To avoid this second terminal session entirely, use <a href="#use-wrangler-login-without-a-local-callback-server"><code>wrangler login --device</code></a>, which does not rely on a <code>localhost</code> callback URL.</p>
<h3 id="use-wrangler-login-in-a-container">Use <code>wrangler login</code> in a container</h3>
<p>The Cloudflare OAuth provider will always redirect to a callback server at <code>localhost:8976</code>. If you are running Wrangler inside a container, this server might not be accessible from your host machine's browser - even after authorizing the connection, your login command will hang.</p>
<p>You must configure your container to map port <code>8976</code> on your host machine to the Wrangler OAuth callback server's port (<code>8976</code> by default).</p>
<p>For example, if you are running Wrangler in a Docker container:</p>
<pre tabindex="0"><code class="language-sh">docker run -p 8976:8976 &lt;your-image&gt;&#10;</code></pre>
<p>And when you run <code>npx wrangler login</code> inside your container, set the callback host to listen on all network interfaces:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --callback-host=0.0.0.0&#10;</code></pre>
<p>Now when the browser redirects to <code>localhost:8976</code>, the request will be forwarded to Wrangler running inside the container on <code>0.0.0.0:8976</code>.</p>
<p>If you need to use a different port inside the container, use <code>--callback-port</code> as well and adjust your port mapping accordingly, for example:</p>
<pre tabindex="0"><code class="language-sh">&#35; When starting your container&#10;docker run -p 8976:9000 &lt;your-image&gt;&#10;&#10;&#35; Inside the container&#10;npx wrangler login --callback-host=0.0.0.0 --callback-port=9000&#10;</code></pre>
<p>If you would rather not map ports at all, use <a href="#use-wrangler-login-without-a-local-callback-server"><code>wrangler login --device</code></a>, which does not start a callback server.</p>
<h3 id="use-wrangler-login-without-a-local-callback-server">Use <code>wrangler login</code> without a local callback server</h3>
<p>The default <code>wrangler login</code> flow needs your browser to be able to reach a temporary local server on <code>localhost:8976</code>. In some environments — remote SSH sessions, containers without forwarded ports, GitHub Codespaces, or otherwise restricted networks — that callback URL is unreachable from the browser, and setting up the workarounds for remote machines and containers may be difficult.</p>
<p>For those cases, pass <code>--device</code> to use the <a href="https://www.rfc-editor.org/rfc/rfc8628">OAuth 2.0 Device Authorization Grant</a> instead. This flow does not start a local callback server. Instead, Wrangler prints a verification URL and a short user code to the terminal, opens the verification URL in your default browser, and polls Cloudflare for an access token while you approve the request.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --device&#10;</code></pre>
<pre tabindex="0"><code class="language-sh"> ⛅️ wrangler 4.119.0&#10;────────────────────&#10;Attempting to login via OAuth Device Authorization Grant...&#10;To authorize Wrangler, please visit:&#10;&#10;  https://dash.cloudflare.com/oauth2/device&#10;&#10;and enter the code:&#10;&#10;  jPqK6Qvs&#10;&#10;You have 5 minutes to approve this request.&#10;&#10;Opening a link in your default browser: https://dash.cloudflare.com/oauth2/device?user_code=jPqK6Qvs&#10;Successfully logged in.&#10;</code></pre>
<p>The URL Wrangler opens in your browser has the user code already filled in, so you only need to confirm the code and approve the request. Wrangler always prints the plain verification URL and the user code as well, so you can approve on a phone or another machine, or enter the code by hand if the browser cannot open.</p>
<p>Wrangler stops polling after 5 minutes, or sooner if Cloudflare sets a shorter expiry on the user code. If the code expires before you approve it, run <code>wrangler login --device</code> again to get a new one.</p>
<p>Pass <code>--browser=false</code> to stop Wrangler from opening the browser for you and copy the verification URL yourself:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --device --browser=false&#10;</code></pre>
<p><code>--callback-host</code> and <code>--callback-port</code> configure the temporary local callback server, which this flow does not use. Wrangler rejects the combination with an error rather than ignoring the flags:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --device --callback-host=0.0.0.0&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">✘ [ERROR] `--callback-host` and `--callback-port` cannot be used with `--device`; the device authorization flow does not use a local callback server.&#10;</code></pre>
<h3 id="storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</h3>
<p>By default, Wrangler stores the OAuth access token and refresh token returned by <code>wrangler login</code> in a plaintext TOML file under the global Wrangler config directory (typically <code>~/.config/.wrangler/config/default.toml</code>). Pass <code>--use-keyring</code> to opt in to a more secure storage path that uses your operating system keychain:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --use-keyring&#10;</code></pre>
<p>When <code>--use-keyring</code> is enabled, Wrangler writes the credentials into an <a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">AES-256-GCM</a>-encrypted file (<code>default.enc</code>, alongside the legacy <code>default.toml</code> location) and stores the 32-byte encryption key in your OS keychain:</p>
<ul>
<li><strong>macOS</strong> uses the built-in <a href="https://support.apple.com/guide/keychain-access/welcome/mac">Keychain</a> via <code>/usr/bin/security</code>.</li>
<li><strong>Linux</strong> uses <a href="https://wiki.gnome.org/Projects/Libsecret">libsecret</a> via the <code>secret-tool</code> CLI from the <code>libsecret-tools</code> package. Wrangler will print a per-distro install hint if <code>secret-tool</code> is not available.</li>
<li><strong>Windows</strong> uses <a href="https://support.microsoft.com/en-us/windows/accessing-credential-manager-1b5c916a-6a16-889f-8581-fc16e8165ac0">Credential Manager</a> via <a href="https://www.npmjs.com/package/@napi-rs/keyring"><code>@napi-rs/keyring</code></a>, which Wrangler installs lazily the first time you opt in (≈1.9 MB one-time download). In non-interactive environments such as CI, install the binding ahead of time with <code>npm install -g @napi-rs/keyring@&lt;version&gt;</code> or stay on the default plaintext path.</li>
</ul>
<p>If a plaintext credentials file exists when you first opt in, Wrangler reads it, encrypts the contents into the new <code>.enc</code> file, and deletes the plaintext file.</p>
<p>The choice is persisted across Wrangler invocations. To verify where credentials are currently stored, run <code>wrangler whoami</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler whoami&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">👋 You are logged in with an OAuth Token, associated with the email user@example.com.&#10;🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)&#10;</code></pre>
<h4 id="opting-out">Opting out</h4>
<p>To opt back out, pass <code>--no-use-keyring</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --no-use-keyring&#10;</code></pre>
<p>Opt-out <strong>deletes</strong> the encrypted file and the keychain entry. Wrangler intentionally does not decrypt the existing credentials onto disk — writing plaintext during opt-out would defeat the at-rest protection you just chose to disable. The subsequent login flow writes fresh credentials into the plaintext TOML file.</p>
<h4 id="per-process-override">Per-process override</h4>
<p>The environment variable <code>CLOUDFLARE_AUTH_USE_KEYRING</code> overrides the persistent preference for a single invocation:</p>
<pre tabindex="0"><code class="language-sh">&#35; Force the keychain backend for this command only&#10;CLOUDFLARE_AUTH_USE_KEYRING=true npx wrangler deploy&#10;&#10;&#35; Force the plaintext file backend for this command only&#10;CLOUDFLARE_AUTH_USE_KEYRING=false npx wrangler deploy&#10;</code></pre>
<p>When the environment variable is set to <code>true</code> and the keychain backend is unavailable (for example, <code>secret-tool</code> is missing on Linux), Wrangler exits with an error rather than silently falling back to the plaintext file. With only the persistent preference set, Wrangler falls back to the plaintext file and prints a one-time warning so a broken keychain never locks you out.</p>
<h4 id="compatibility">Compatibility</h4>
<p>The <code>--use-keyring</code> opt-in does not change how API tokens are resolved: <code>CLOUDFLARE_API_TOKEN</code> and <code>CLOUDFLARE_API_KEY</code>/<code>CLOUDFLARE_EMAIL</code> continue to take priority over any stored OAuth credentials, and the <a href="/workers/ci-cd/">Running Wrangler in CI/CD</a> guidance still applies for non-interactive environments.</p>
<hr />
<h2 id="logout"><code>logout</code></h2>
<p>Remove Wrangler's authorization for accessing your account. This command will invalidate your current OAuth token and delete the stored credentials. When <a href="#storing-oauth-credentials-in-the-os-keychain">keychain storage</a> is active, both the encrypted credentials file and the keychain entry are removed.</p>
<pre tabindex="0"><code class="language-txt">wrangler logout&#10;</code></pre>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<p>If you are using <code>CLOUDFLARE_API_TOKEN</code> instead of OAuth, and you can logout by deleting your API token in the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the three-dot menu on your Wrangler token.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
<hr />
<h2 id="auth"><code>auth</code></h2>
<p>Manage authentication, including named <a href="/workers/wrangler/profiles/">authentication profiles</a> for working across multiple accounts.</p>
<h3 id="auth-token"><code>auth token</code></h3>
<p>Retrieve your current authentication token or credentials for use with other tools and scripts.</p>
<pre tabindex="0"><code class="language-txt">wrangler auth token [OPTIONS]&#10;</code></pre>
<ul>
<li><code>--json</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Return output as JSON with token type information. This also enables retrieving API key/email credentials.</li>
</ul>
</li>
</ul>
<p>The command returns whichever authentication method is currently configured, in the following order of precedence:</p>
<ul>
<li>API token from <code>CLOUDFLARE_API_TOKEN</code> environment variable</li>
<li>API key/email from <code>CLOUDFLARE_API_KEY</code> and <code>CLOUDFLARE_EMAIL</code> environment variables (requires <code>--json</code> flag, since this method uses two values instead of a single token)</li>
<li>OAuth token from <code>wrangler login</code> (automatically refreshed if expired)</li>
</ul>
<p>When using <code>--json</code>, the output includes the token type:</p>
<pre tabindex="0"><code class="language-jsonc">// API token&#10;{ &quot;type&quot;: &quot;api_token&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// OAuth token&#10;{ &quot;type&quot;: &quot;oauth&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// API key/email (only available with --json)&#10;{ &quot;type&quot;: &quot;api_key&quot;, &quot;key&quot;: &quot;...&quot;, &quot;email&quot;: &quot;...&quot; }&#10;</code></pre>
<p>An error is returned if no authentication method is available, or if API key/email is configured without <code>--json</code>.</p>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<h3 id="auth-create">auth create</h3><p>Create or re-authenticate a named auth profile</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler auth create [NAME]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler auth create [NAME]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler auth create [NAME]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler auth create [NAME]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler auth create [NAME]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler auth create [NAME]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>name</code> <small>required, string</small><p>Name for the auth profile</p>
</li><li><code>--browser</code> <small>boolean, default: True</small><p>Automatically open the OAuth link in a browser</p>
</li><li><code>--scopes</code> <small>string</small><p>Pick the set of applicable OAuth scopes when logging in</p>
</li><li><code>--callback-host</code> <small>string, default: localhost</small><p>Use the ip or host address for the temporary login callback server.</p>
</li><li><code>--callback-port</code> <small>number, default: 8976</small><p>Use the port for the temporary login callback server.</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="auth-activate">auth activate</h3><p>Bind a named auth profile to a directory</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler auth activate [NAME] [DIR]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler auth activate [NAME] [DIR]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler auth activate [NAME] [DIR]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler auth activate [NAME] [DIR]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler auth activate [NAME] [DIR]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler auth activate [NAME] [DIR]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>name</code> <small>required, string</small><p>Name of the auth profile to activate</p>
</li><li><code>dir</code> <small>string</small><p>Directory to bind the profile to (defaults to current directory)</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="auth-deactivate">auth deactivate</h3><p>Remove the auth profile binding from a directory</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler auth deactivate [DIR]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler auth deactivate [DIR]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler auth deactivate [DIR]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler auth deactivate [DIR]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler auth deactivate [DIR]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler auth deactivate [DIR]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>dir</code> <small>string</small><p>Directory to unbind (defaults to current directory). Must be the exact directory the profile was bound to.</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="auth-list">auth list</h3><p>List all auth profiles</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler auth list</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler auth list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler auth list</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler auth list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler auth list</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler auth list" aria-label="Copy to clipboard">Copy</button></div></div><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="auth-delete">auth delete</h3><p>Delete a named auth profile</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler auth delete [NAME]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler auth delete [NAME]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler auth delete [NAME]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler auth delete [NAME]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler auth delete [NAME]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler auth delete [NAME]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>name</code> <small>required, string</small><p>Name of the auth profile to delete</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<hr />
<h2 id="whoami">whoami</h2><p>🕵️ Retrieve your user information</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler whoami</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler whoami" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler whoami</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler whoami" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler whoami</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler whoami" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--account</code> <small>string</small><p>Show membership information for the given account (id or name).</p>
</li><li><code>--json</code> <small>boolean, default: False</small><p>Return user information as JSON. Exits with a non-zero status if not authenticated.</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<hr />
<h2 id="telemetry"><code>telemetry</code></h2>
<p>Cloudflare collects anonymous usage data to improve Wrangler. You can learn more about this in our <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler/telemetry.md">data policy</a>.</p>
<p>You can manage sharing of usage data at any time using these commands.</p>
<h3 id="disable"><code>disable</code></h3>
<p>Disable telemetry collection for Wrangler.</p>
<pre tabindex="0"><code class="language-txt">wrangler telemetry disable&#10;</code></pre>
<h3 id="enable"><code>enable</code></h3>
<p>Enable telemetry collection for Wrangler.</p>
<pre tabindex="0"><code class="language-txt">wrangler telemetry enable&#10;</code></pre>
<h3 id="status"><code>status</code></h3>
<p>Check whether telemetry collection is currently enabled. The return result is specific to the directory where you have run the command.</p>
<p>This will resolve the global status set by <code>wrangler telemetry disable / enable</code>, the environment variable <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>WRANGLER_SEND_METRICS</code></a>, and the <a href="/workers/wrangler/configuration/#top-level-only-keys"><code>send_metrics</code></a> key in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<pre tabindex="0"><code class="language-txt">wrangler telemetry status&#10;</code></pre>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="complete"><code>complete</code></h2>
<p>Generate shell completion scripts for Wrangler commands. Shell completions allow you to autocomplete commands, subcommands, and flags by pressing Tab as you type.</p>
<pre tabindex="0"><code class="language-txt">wrangler complete &lt;SHELL&gt;&#10;</code></pre>
<ul>
<li><code>SHELL</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The shell to generate completions for. Supported values: <code>bash</code>, <code>zsh</code>, <code>fish</code>, <code>powershell</code>.</li>
</ul>
</li>
</ul>
<h3 id="setup">Setup</h3>
<p>Generate and add the completion script to your shell configuration file:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17446.md")
</div></div>
<h3 id="usage">Usage</h3>
<p>After setup, press Tab to autocomplete commands, subcommands, and flags:</p>
<pre tabindex="0"><code class="language-sh">wrangler d&lt;TAB&gt;          # completes to &#x27;deploy&#x27;, &#x27;dev&#x27;, &#x27;d1&#x27;, etc.&#10;wrangler kv &lt;TAB&gt;        # shows subcommands: namespace, key, bulk&#10;</code></pre>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
