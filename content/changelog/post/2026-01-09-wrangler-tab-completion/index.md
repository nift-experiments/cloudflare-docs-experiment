<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 9, 2026</time><h2 id="post-title">Shell tab completions for Wrangler CLI</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now includes built-in shell tab completion support, making it faster and easier to navigate commands without memorizing every option. Press Tab as you type to autocomplete commands, subcommands, flags, and even option values like log levels.</p>
<p>Tab completions are supported for Bash, Zsh, Fish, and PowerShell.</p>
<h4 id="setup">Setup</h4>
<p>Generate the completion script for your shell and add it to your configuration file:</p>
<pre><code class="language-sh">&#35; Bash&#10;wrangler complete bash &gt;&gt; ~/.bashrc&#10;&#10;&#35; Zsh&#10;wrangler complete zsh &gt;&gt; ~/.zshrc&#10;&#10;&#35; Fish&#10;wrangler complete fish &gt;&gt; ~/.config/fish/config.fish&#10;&#10;&#35; PowerShell&#10;wrangler complete powershell &gt;&gt; $PROFILE&#10;</code></pre>
<p>After adding the script, restart your terminal or source your configuration file for the changes to take effect. Then you can simply press Tab to see available completions:</p>
<pre><code class="language-sh">wrangler d&lt;TAB&gt;          # completes to &#x27;deploy&#x27;, &#x27;dev&#x27;, &#x27;d1&#x27;, etc.&#10;wrangler kv &lt;TAB&gt;        # shows subcommands: namespace, key, bulk&#10;</code></pre>
<p>Tab completions are dynamically generated from Wrangler's command registry, so they stay up-to-date as new commands and options are added. This feature is powered by <a href="https://github.com/bombshell-dev/tab/"><code>@bomb.sh/tab</code></a>.</p>
<p>See the <a href="/workers/wrangler/commands/general/#complete"><code>wrangler complete</code> documentation</a> for more details.</p>
</div></article></div>
