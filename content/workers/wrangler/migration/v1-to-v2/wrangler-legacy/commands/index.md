---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/commands/
  description: Reference for all Wrangler v1 CLI commands, including generate, publish, and preview. Now deprecated.
  full_title: Commands - Wrangler v1 (deprecated) · Cloudflare Workers docs
  head_html: <title>Commands - Wrangler v1 (deprecated) · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for all Wrangler v1 CLI commands, including generate, publish, and preview. Now deprecated."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/commands/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/commands/index.md"><meta property="og:title" content="Commands - Wrangler v1 (deprecated) · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for all Wrangler v1 CLI commands, including generate, publish, and preview. Now deprecated."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/commands/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/commands/#page","headline":"Commands - Wrangler v1 (deprecated) \u00b7 Cloudflare Workers docs","description":"Reference for all Wrangler v1 CLI commands, including generate, publish, and preview. Now deprecated.","url":"https://developers.cloudflare.com/workers/wrangler/commands/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/migration/v1-to-v2/wrangler-legacy/commands/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17484.md")
</aside>
<p>Complete list of all commands available for <a href="https://github.com/cloudflare/wrangler-legacy"><code>wrangler</code></a>, the Workers CLI.</p>
<hr />
<h2 id="generate">generate</h2>
<p>Scaffold a Cloudflare Workers project from a public GitHub repository.</p>
<pre tabindex="0"><code class="language-sh">wrangler generate [$NAME] [$TEMPLATE] [--type=$TYPE] [--site]&#10;</code></pre>
<p>Default values indicated by =value.</p>
<ul>
<li>
<p><code>$NAME</code> =worker optional</p>
<ul>
<li>The name of the Workers project. This is both the directory name and <code>name</code> property in the generated <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/">Wrangler configuration</a> file.</li>
</ul>
</li>
<li>
<p><code>$TEMPLATE</code> =<a href="https://github.com/cloudflare/worker-template">https://github.com/cloudflare/worker-template</a> optional</p>
<ul>
<li>The GitHub URL of the <a href="https://github.com/cloudflare/worker-template">repository to use as the template</a> for generating the project.</li>
</ul>
</li>
<li>
<p><code>--type=$TYPE</code> =webpack optional</p>
<ul>
<li>The type of project; one of <code>webpack</code>, <code>javascript</code>, or <code>rust</code>.</li>
</ul>
</li>
<li>
<p><code>--site</code> optional</p>
<ul>
<li>When defined, the default <code>$TEMPLATE</code> value is changed to <a href="https://github.com/cloudflare/workers-sdk/tree/main/templates/worker-sites"><code>cloudflare/workers-sdk/templates/worker-sites</code></a>. This scaffolds a <a href="/workers/configuration/sites/start-from-scratch">Workers Site</a> project.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="init">init</h2>
<p>Create a skeleton <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> in an existing directory. This command can be used as an alternative to <code>generate</code> if you prefer to clone a template repository yourself or you already have a JavaScript project and would like to use Wrangler.</p>
<pre tabindex="0"><code class="language-sh">wrangler init [$NAME] [--type=$TYPE] [--site]&#10;</code></pre>
<p>Default values indicated by =value.</p>
<ul>
<li>
<p><code>$NAME</code> =(Name of working directory) optional</p>
<ul>
<li>The name of the Workers project. This is both the directory name and <code>name</code> property in the generated <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/">Wrangler configuration</a> file.</li>
</ul>
</li>
<li>
<p><code>--type=$TYPE</code> =webpack optional</p>
<ul>
<li>The type of project; one of <code>webpack</code>, <code>javascript</code>, or <code>rust</code>.</li>
</ul>
</li>
<li>
<p><code>--site</code> optional</p>
<ul>
<li>When defined, the default <code>$TEMPLATE</code> value is changed to <a href="https://github.com/cloudflare/workers-sdk/tree/main/templates/worker-sites"><code>cloudflare/workers-sdk/templates/worker-sites</code></a>. This scaffolds a <a href="/workers/configuration/sites/start-from-scratch">Workers Site</a> project.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="build">build</h2>
<p>Build your project (if applicable). This command looks at your Wrangler file and reacts to the <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/#keys"><code>&quot;type&quot;</code> value</a> specified.</p>
<p>When using <code>type = &quot;webpack&quot;</code>, Wrangler will build the Worker using its internal webpack installation. When using <code>type = &quot;javascript&quot;</code> , the <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/#build-1"><code>build.command</code></a>, if defined, will run.</p>
<pre tabindex="0"><code class="language-sh">wrangler build [--env $ENVIRONMENT_NAME]&#10;</code></pre>
<ul>
<li><code>--env</code> optional
<ul>
<li>If defined, Wrangler will load the matching environment's configuration before building. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="login">login</h2>
<p>Authorize Wrangler with your Cloudflare account. This will open a login page in your browser and request your account access permissions. This command is the alternative to <code>wrangler config</code> and it uses OAuth tokens.</p>
<pre tabindex="0"><code class="language-sh">wrangler login [--scopes-list] [--scopes $SCOPES]&#10;</code></pre>
<p>All of the arguments and flags to this command are optional:</p>
<ul>
<li><code>--scopes-list</code> optional
<ul>
<li>List all the available OAuth scopes with descriptions.</li>
</ul>
</li>
<li><code>--scopes $SCOPES</code> optional
<ul>
<li>Allows to choose your set of OAuth scopes. The set of scopes must be entered in a whitespace-separated list,
for example, <code>wrangler login --scopes account:read user:read</code>.</li>
</ul>
</li>
</ul>
<p><code>wrangler login</code> uses all the available scopes by default if no flags are provided.</p>
<hr />
<h2 id="logout">logout</h2>
<p>Remove Wrangler's authorization for accessing your account. This command will invalidate your current OAuth token and delete the configuration file, if present.</p>
<pre tabindex="0"><code class="language-sh">wrangler logout&#10;</code></pre>
<p>This command only invalidates OAuth tokens acquired through the <code>wrangler login</code> command. However, it will try to delete the configuration file regardless of your authorization method.</p>
<p>To delete your API token:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>Overview</strong> &gt; <strong>Get your API token</strong> in the right side menu.</li>
<li>Select the three-dot menu on your Wrangler token and select <strong>Delete</strong>.</li>
</ol>
<hr />
<h2 id="config">config</h2>
<p>Configure Wrangler so that it may acquire a Cloudflare API Token or Global API key, instead of OAuth tokens, in order to access and manage account resources.</p>
<pre tabindex="0"><code class="language-sh">wrangler config [--api-key]&#10;</code></pre>
<ul>
<li><code>--api-key</code> optional
<ul>
<li>To provide your email and global API key instead of a token. (This is not recommended for security reasons.)</li>
</ul>
</li>
</ul>
<p>You can also use environment variables to authenticate, or <code>wrangler login</code> to authorize with OAuth tokens.</p>
<hr />
<h2 id="publish">publish</h2>
<p>Publish your Worker to Cloudflare. Several keys in your Wrangler file determine whether you are publishing to a <code>*.workers.dev</code> subdomain or a custom domain. However, custom domains must be proxied (orange-clouded) through Cloudflare. Refer to the <a href="/workers/configuration/routing/custom-domains/">Get started guide</a> for more information.</p>
<pre tabindex="0"><code class="language-sh">wrangler publish [--env $ENVIRONMENT_NAME]&#10;</code></pre>
<ul>
<li><code>--env</code> optional
<ul>
<li>If defined, Wrangler will load the matching environment's configuration before building and deploying. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
</ul>
<p>To use this command, the following fields are required in your Wrangler file:</p>
<ul>
<li>
<p><code>name</code> string</p>
<ul>
<li>The name of the Workers project. This is both the directory name and <code>name</code> property in the generated <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/">Wrangler configuration</a> file.</li>
</ul>
</li>
<li>
<p><code>type</code> string</p>
<ul>
<li>The type of project; one of <code>webpack</code>, <code>javascript</code>, or <code>rust</code>.</li>
</ul>
</li>
<li>
<p><code>account_id</code> string</p>
<ul>
<li>The Cloudflare account ID. This can be found in the Cloudflare dashboard, for example, <code>account_id = &quot;a655bacaf2b4cad0e2b51c5236a6b974&quot;</code>.</li>
</ul>
</li>
</ul>
<p>You can publish to <a href="https://workers.dev">&lt;your-worker&gt;.&lt;your-subdomain&gt;.workers.dev</a> or to a custom domain.</p>
<p>When you publish changes to an existing Worker script, all new requests will automatically route to the updated version of the Worker without downtime. Any inflight requests will continue running on the previous version until completion. Once all inflight requests have finished complete, the previous Worker version will be purged and will no longer handle requests.</p>
<h3 id="publishing-to-workers-dev">Publishing to workers.dev</h3>
<p>To publish to <a href="https://workers.dev"><code>*.workers.dev</code></a>, you will first need to have a subdomain registered. You can register a subdomain by executing the <a href="#subdomain"><code>wrangler subdomain</code></a> command.</p>
<p>After you have registered a subdomain, add <code>workers_dev</code> to your Wrangler file.</p>
<ul>
<li><code>workers_dev</code> bool
<ul>
<li>When <code>true</code>, indicates that the Worker should be deployed to a <code>*.workers.dev</code> domain.</li>
</ul>
</li>
</ul>
<h3 id="publishing-to-your-own-domain">Publishing to your own domain</h3>
<p>To publish to your own domain, specify these three fields in your Wrangler file.</p>
<ul>
<li>
<p><code>zone_id</code> string</p>
<ul>
<li>The Cloudflare zone ID, for example, <code>zone_id = &quot;b6558acaf2b4cad1f2b51c5236a6b972&quot;</code>, which can be found in the Cloudflare dashboard.</li>
</ul>
</li>
<li>
<p><code>route</code> string</p>
<ul>
<li>The route you would like to publish to, for example, <code>route = &quot;example.com/my-worker/*&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>routes</code> Array</p>
<ul>
<li>The routes you would like to publish to, for example, <code>routes = [&quot;example.com/foo/*&quot;, example.com/bar/*]</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17483.md")
</aside>
<h3 id="publishing-the-same-code-to-multiple-domains">Publishing the same code to multiple domains</h3>
<p>To publish your code to multiple domains, refer to the <a href="/workers/wrangler/environments/">documentation for environments</a>.</p>
<hr />
<h2 id="dev">dev</h2>
<p><code>wrangler dev</code> is a command that establishes a connection between <code>localhost</code> and a global network server that operates your Worker in development. A <code>cloudflared</code> tunnel forwards all requests to the global network server, which continuously updates as your Worker code changes. This allows full access to Workers KV, Durable Objects and other Cloudflare developer platform products. The <code>dev</code> command is a way to test your Worker while developing.</p>
<pre tabindex="0"><code class="language-sh">wrangler dev [--env $ENVIRONMENT_NAME] [--ip &lt;ip&gt;] [--port &lt;port&gt;] [--host &lt;host&gt;] [--local-protocol &lt;http|https&gt;] [--upstream-protocol &lt;http|https&gt;]&#10;</code></pre>
<ul>
<li>
<p><code>--env</code> optional</p>
<ul>
<li>If defined, Wrangler will load the matching environment's configuration. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--ip</code> optional</p>
<ul>
<li>The IP to listen on, defaults to <code>127.0.0.1</code>.</li>
</ul>
</li>
<li>
<p><code>--port</code> optional</p>
<ul>
<li>The port to listen on, defaults to <code>8787</code>.</li>
</ul>
</li>
<li>
<p><code>--host</code> optional</p>
<ul>
<li>The host to forward requests to, defaults to the zone of the project or to <code>tutorial.cloudflareworkers.com</code> if unauthenticated.</li>
</ul>
</li>
<li>
<p><code>--local-protocol</code> optional</p>
<ul>
<li>The protocol to listen to requests on, defaults to <code>http</code>.</li>
</ul>
</li>
<li>
<p><code>--upstream-protocol</code> optional</p>
<ul>
<li>The protocol to forward requests to host on, defaults to <code>https</code>.</li>
</ul>
</li>
</ul>
<p>These arguments can also be set in your Wrangler file. Refer to the <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/#dev"><code>wrangler dev</code> configuration</a> documentation for more information.</p>
<h3 id="usage">Usage</h3>
<p>You should run <code>wrangler dev</code> from your Worker directory. Wrangler will run a local server accepting requests, executing your Worker, and forwarding them to a host. If you want to use another host other than your zone or <code>tutorials.cloudflare.com</code>, you can specify with <code>--host example.com</code>.</p>
<pre tabindex="0"><code class="language-sh">wrangler dev&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">💁  JavaScript project found. Skipping unnecessary build!&#10;💁  watching &quot;./&quot;&#10;👂  Listening on http://127.0.0.1:8787&#10;</code></pre>
<p>With <code>wrangler dev</code> running, you can send HTTP requests to <code>localhost:8787</code> and your Worker should execute as expected. You will also see <code>console.log</code> messages and exceptions appearing in your terminal. If either of these things do not happen, or you think the output is incorrect, <a href="https://github.com/cloudflare/wrangler-legacy">file an issue</a>.</p>
<hr />
<h2 id="tail">tail</h2>
<p>Start a session to livestream logs from a deployed Worker.</p>
<pre tabindex="0"><code class="language-sh">wrangler tail [--format $FORMAT] [--status $STATUS] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>--format $FORMAT</code> json|pretty
<ul>
<li>The format of the log entries.</li>
</ul>
</li>
<li><code>--status $STATUS</code>
<ul>
<li>Filter by invocation status [possible values: <code>ok</code>, <code>error</code>, <code>canceled</code>].</li>
</ul>
</li>
<li><code>--header $HEADER</code>
<ul>
<li>Filter by HTTP header.</li>
</ul>
</li>
<li><code>--method $METHOD</code>
<ul>
<li>Filter by HTTP method.</li>
</ul>
</li>
<li><code>--sampling-rate $RATE</code>
<ul>
<li>Add a percentage of requests to log sampling rate.</li>
</ul>
</li>
<li><code>--search $SEARCH</code>
<ul>
<li>Filter by a text match in <code>console.log</code> messages.</li>
</ul>
</li>
</ul>
<p>After starting <code>wrangler tail</code> in a directory with a project, you will receive a live feed of console and exception logs for each request your Worker receives.</p>
<p>Like all Wrangler commands, run <code>wrangler tail</code> from your Worker’s root directory (the directory with your Wrangler file).</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="legacy-issues-with-existing-cloudflared-configuration">Legacy issues with existing cloudflared configuration</h3>
@markup("md", "content/.markup/bodies/17482.md")
</aside>
<hr />
<h2 id="preview">preview</h2>
<p>Preview your project using the <a href="https://cloudflareworkers.com/">Cloudflare Workers preview service</a>.</p>
<pre tabindex="0"><code class="language-sh">wrangler preview [--watch] [--env $ENVIRONMENT_NAME] [ --url $URL] [$METHOD] [$BODY]&#10;</code></pre>
<p>Default values indicated by =value.</p>
<ul>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, Wrangler will load the matching environment's configuration. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--watch</code> recommended</p>
<ul>
<li>When enabled, any changes to the Worker project will continually update the preview service with the newest version of your project. By default, <code>wrangler preview</code> will only bundle your project a single time.</li>
</ul>
</li>
<li>
<p><code>$METHOD</code> =&quot;GET&quot; optional</p>
<ul>
<li>The type of request to preview your Worker with (<code>GET</code>, <code>POST</code>).</li>
</ul>
</li>
<li>
<p><code>$BODY</code> =&quot;Null&quot; optional</p>
<ul>
<li>The body string to post to your preview Worker request. For example, <code>wrangler preview post hello=hello</code>.</li>
</ul>
</li>
</ul>
<h3 id="kv-namespaces">kv_namespaces</h3>
<p>If you are using <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/#kv_namespaces">kv_namespaces</a> with <code>wrangler preview</code>, you will need to specify a <code>preview_id</code> in your Wrangler file before you can start the session. This is so that you do not accidentally write changes to your production namespace while you are developing. You may make <code>preview_id</code> equal to <code>id</code> if you would like to preview with your production namespace, but you should ensure that you are not writing values to KV that would break your production Worker.</p>
<p>To create a <code>preview_id</code> run:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace create --preview &quot;NAMESPACE&quot;&#10;</code></pre>
<h3 id="previewing-on-windows-subsystem-for-linux-wsl-1-2">Previewing on Windows Subsystem for Linux (WSL 1/2)</h3>
<h4 id="setting-browser-to-your-browser-binary">Setting $BROWSER to your browser binary</h4>
<p>WSL is a Linux environment, so Wrangler attempts to invoke <code>xdg-open</code> to open your browser. To make <code>wrangler preview</code> work with WSL, you should set your <code>$BROWSER</code> to the path of your browser binary:</p>
<pre tabindex="0"><code class="language-sh">export BROWSER=&quot;/mnt/c/tools/firefox.exe&quot;&#10;wrangler preview&#10;</code></pre>
<p>Spaces in filepaths are not common in Linux, and some programs like <code>xdg-open</code> will break on <a href="https://github.com/microsoft/WSL/issues/3632#issuecomment-432821522">paths with spaces</a>. You can work around this by linking the binary to your <code>/usr/local/bin</code>:</p>
<pre tabindex="0"><code class="language-sh">ln -s &quot;/mnt/c/Program Files/Mozilla Firefox/firefox.exe&quot; firefox&#10;export BROWSER=firefox&#10;</code></pre>
<h4 id="setting-browser-to-wsl-open">Setting $BROWSER to <code>wsl-open</code></h4>
<p>Another option is to install <a href="https://github.com/4U6U57/wsl-open#standalone">wsl-open</a> and set the <code>$BROWSER</code> <a href="/workers/configuration/environment-variables/">env variable</a> to <code>wsl-open</code> via <code>wsl-open -w</code>. This ensures that <code>xdg-open</code> uses <code>wsl-open</code> when it attempts to open your browser.</p>
<p>If you are using WSL 2, you will need to install <code>wsl-open</code> following their <a href="https://github.com/4U6U57/wsl-open#standalone">standalone method</a> rather than through <code>npm</code>. This is because their npm package has not yet been updated with WSL 2 support.</p>
<hr />
<h2 id="route"><code>route</code></h2>
<p>List or delete a route associated with a domain:</p>
<pre tabindex="0"><code class="language-sh">wrangler route list [--env $ENVIRONMENT_NAME]&#10;</code></pre>
<p>Default values indicated by =value.</p>
<ul>
<li><code>--env $ENVIRONMENT_NAME</code> optional
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
</ul>
<p>This command will forward the JSON response from the <a href="/api/resources/workers/subresources/routes/methods/list/">List Routes API</a>. Each object within the JSON list will include the route id, route pattern, and the assigned Worker name for the route. Piping this through a tool such as <code>jq</code> will render the output nicely.</p>
<pre tabindex="0"><code class="language-sh">wrangler route delete $ID [--env $ENVIRONMENT_NAME]&#10;</code></pre>
<p>Default values indicated by =value.</p>
<ul>
<li>
<p><code>$ID</code> required</p>
<ul>
<li>The hash of the route ID to delete.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="subdomain">subdomain</h2>
<p>Create or change your <a href="https://workers.dev"><code>*.workers.dev</code></a> subdomain.</p>
<pre tabindex="0"><code class="language-sh">wrangler subdomain &lt;name&gt;&#10;</code></pre>
<hr />
<h2 id="secret">secret</h2>
<p>Interact with your secrets.</p>
<h3 id="put"><code>put</code></h3>
<p>Create or replace a secret.</p>
<pre tabindex="0"><code class="language-sh">wrangler secret put &lt;name&gt; --env ENVIRONMENT_NAME&#10;Enter the secret text you would like assigned to the variable name on the Worker named my-worker-ENVIRONMENT_NAME:&#10;</code></pre>
<p>You will be prompted to input the secret's value. This command can receive piped input, so the following example is also possible:</p>
<pre tabindex="0"><code class="language-sh">echo &quot;-----BEGIN PRIVATE KEY-----\nM...==\n-----END PRIVATE KEY-----\n&quot; | wrangler secret put PRIVATE_KEY&#10;</code></pre>
<ul>
<li>
<p><code>name</code></p>
<ul>
<li>The variable name to be accessible in the script.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
</ul>
<h3 id="delete"><code>delete</code></h3>
<p>Delete a secret from a specific script.</p>
<pre tabindex="0"><code class="language-sh">wrangler secret delete &lt;name&gt; --env ENVIRONMENT_NAME&#10;</code></pre>
<ul>
<li>
<p><code>name</code></p>
<ul>
<li>The variable name to be accessible in the script.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
</ul>
<h3 id="list"><code>list</code></h3>
<p>List all the secret names bound to a specific script.</p>
<pre tabindex="0"><code class="language-sh">wrangler secret list --env ENVIRONMENT_NAME&#10;</code></pre>
<ul>
<li><code>--env $ENVIRONMENT_NAME</code> optional
<ul>
<li>If defined, only the specified environment's secrets will be listed. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="kv">kv</h2>
<p>The <code>kv</code> subcommand allows you to store application data in the Cloudflare network to be accessed from Workers using <a href="https://www.cloudflare.com/products/workers-kv/">Workers KV</a>. KV operations are scoped to your account, so in order to use any of these commands, you:</p>
<ul>
<li>must configure an <code>account_id</code> in your project's Wrangler file.</li>
<li>run all <code>wrangler kv:&lt;command&gt;</code> operations in your terminal from the project's root directory.</li>
</ul>
<h3 id="getting-started">Getting started</h3>
<p>To use Workers KV with your Worker, the first thing you must do is create a KV namespace. This is done with
the <code>kv:namespace</code> subcommand.</p>
<p>The <code>kv:namespace</code> subcommand takes a new binding name as its argument. A Workers KV namespace will be created using a concatenation of your Worker’s name (from your Wrangler file) and the binding name you provide:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace create &quot;MY_KV&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">🌀  Creating namespace with title &quot;my-site-MY_KV&quot;&#10;✨  Success!&#10;Add the following to your configuration file:&#10;kv_namespaces = [&#10;  { binding = &quot;MY_KV&quot;, id = &quot;e29b263ab50e42ce9b637fa8370175e8&quot; }&#10;]&#10;</code></pre>
<p>Successful operations will print a new configuration block that should be copied into your Wrangler file. Add the output to the existing <code>kv_namespaces</code> configuration if already present. You can now access the binding from within a Worker:</p>
<pre tabindex="0"><code class="language-js">let value = await MY_KV.get(&quot;my-key&quot;);&#10;</code></pre>
<p>To write a value to your KV namespace using Wrangler, run the <code>wrangler kv:key put</code> subcommand.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --binding=MY_KV &quot;key&quot; &quot;value&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">✨  Success&#10;</code></pre>
<p>Instead of <code>--binding</code>, you may use <code>--namespace-id</code> to specify which KV namespace should receive the operation:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --namespace-id=e29b263ab50e42ce9b637fa8370175e8 &quot;key&quot; &quot;value&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">✨  Success&#10;</code></pre>
<p>Additionally, KV namespaces can be used with environments. This is useful for when you have code that refers to
a KV binding like <code>MY_KV</code>, and you want to be able to have these bindings point to different namespaces (like
one for staging and one for production).</p>
<p>A Wrangler file with two environments:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17485.md")
</div>
<p>To insert a value into a specific KV namespace, you can use:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --env=staging --binding=MY_MV &quot;key&quot; &quot;value&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">✨  Success&#10;</code></pre>
<p>Since <code>--namespace-id</code> is always unique (unlike binding names), you do not need to specify an <code>--env</code> argument.</p>
<h3 id="concepts">Concepts</h3>
<p>Most <code>kv</code> commands require you to specify a namespace. A namespace can be specified in two ways:</p>
<ol>
<li>With a <code>--binding</code>:</li>
</ol>
<pre tabindex="0"><code class="language-sh">wrangler kv:key get --binding=MY_KV &quot;my key&quot;&#10;</code></pre>
<ul>
<li>This can be combined with <code>--preview</code> flag to interact with a preview namespace instead of a production namespace.</li>
</ul>
<ol start="2">
<li>With a <code>--namespace-id</code>:</li>
</ol>
<pre tabindex="0"><code class="language-sh">wrangler kv:key get --namespace-id=06779da6940b431db6e566b4846d64db &quot;my key&quot;&#10;</code></pre>
<p>Most <code>kv</code> subcommands also allow you to specify an environment with the optional <code>--env</code> flag. This allows you to publish Workers running the same code but with different namespaces. For example, you could use separate staging and production namespaces for KV data in your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17486.md")
</div>
<p>With the Wrangler file above, you can specify <code>--env production</code> when you want to perform a KV action on the namespace <code>MY_KV</code> under <code>env.production</code>. For example, with the Wrangler file above, you can get a value out of a production KV instance with:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key get --binding &quot;MY_KV&quot; --env=production &quot;my key&quot;&#10;</code></pre>
<p>To learn more about environments, refer to <a href="/workers/wrangler/environments/">Environments</a>.</p>
<h3 id="kv-namespace"><code>kv:namespace</code></h3>
<h4 id="create"><code>create</code></h4>
<p>Create a new namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace create $NAME [--env=$ENVIRONMENT_NAME] [--preview]&#10;</code></pre>
<ul>
<li>
<p><code>$NAME</code></p>
<ul>
<li>The name of the new namespace.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--preview</code> optional</p>
<ul>
<li>Interact with a preview namespace (the <code>preview_id</code> value) instead of production.</li>
</ul>
</li>
</ul>
<h5 id="usage-1">Usage</h5>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace create &quot;MY_KV&quot;&#10;🌀  Creating namespace with title &quot;worker-MY_KV&quot;&#10;✨  Add the following to your wrangler.toml:&#10;kv_namespaces = [&#10;  { binding = &quot;MY_KV&quot;, id = &quot;e29b263ab50e42ce9b637fa8370175e8&quot; }&#10;]&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace create &quot;MY_KV&quot; --preview&#10;🌀  Creating namespace with title &quot;my-site-MY_KV_preview&quot;&#10;✨  Success!&#10;Add the following to your wrangler.toml:&#10;kv_namespaces = [&#10;  { binding = &quot;MY_KV&quot;, preview_id = &quot;15137f8edf6c09742227e99b08aaf273&quot; }&#10;]&#10;</code></pre>
<h4 id="list-1"><code>list</code></h4>
<p>List all KV namespaces associated with an account ID.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace list&#10;</code></pre>
<h5 id="usage-2">Usage</h5>
<p>This example passes the Wrangler command through the <code>jq</code> command:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace list | jq &quot;.&quot;&#10;[&#10;  {&#10;    &quot;id&quot;: &quot;06779da6940b431db6e566b4846d64db&quot;,&#10;    &quot;title&quot;: &quot;TEST_NAMESPACE&quot;&#10;  },&#10;  {&#10;    &quot;id&quot;: &quot;32ac1b3c2ed34ed3b397268817dea9ea&quot;,&#10;    &quot;title&quot;: &quot;STATIC_CONTENT&quot;&#10;  }&#10;]&#10;</code></pre>
<h4 id="delete-1"><code>delete</code></h4>
<p>Delete a given namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace delete --binding= [--namespace-id=]&#10;</code></pre>
<ul>
<li>
<p><code>--binding</code> required (if no <code>--namespace-id</code>)</p>
<ul>
<li>The name of the namespace to delete.</li>
</ul>
</li>
<li>
<p><code>--namespace-id</code> required (if no <code>--binding</code>)</p>
<ul>
<li>The ID of the namespace to delete.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--preview</code> optional</p>
<ul>
<li>Interact with a preview namespace instead of production.</li>
</ul>
</li>
</ul>
<h5 id="usage-3">Usage</h5>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace delete --binding=MY_KV&#10;Are you sure you want to delete namespace f7b02e7fc70443149ac906dd81ec1791? [y/n]&#10;yes&#10;🌀  Deleting namespace f7b02e7fc70443149ac906dd81ec1791&#10;✨  Success&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">wrangler kv:namespace delete --binding=MY_KV --preview&#10;Are you sure you want to delete namespace 15137f8edf6c09742227e99b08aaf273? [y/n]&#10;yes&#10;🌀  Deleting namespace 15137f8edf6c09742227e99b08aaf273&#10;✨  Success&#10;</code></pre>
<h3 id="kv-key"><code>kv:key</code></h3>
<h4 id="put-1"><code>put</code></h4>
<p>Write a single key-value pair to a particular namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --binding= [--namespace-id=] $KEY $VALUE&#10;✨  Success&#10;</code></pre>
<ul>
<li>
<p><code>$KEY</code> required</p>
<ul>
<li>The key to write to.</li>
</ul>
</li>
<li>
<p><code>$VALUE</code> required</p>
<ul>
<li>The value to write.</li>
</ul>
</li>
<li>
<p><code>--binding</code> required (if no <code>--namespace-id</code>)</p>
<ul>
<li>The name of the namespace to write to.</li>
</ul>
</li>
<li>
<p><code>--namespace-id</code> required (if no <code>--binding</code>)</p>
<ul>
<li>The ID of the namespace to write to.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--preview</code> optional</p>
<ul>
<li>Interact with a preview namespace instead of production. Pass this to the Wrangler file’s <code>kv_namespaces.preview_id</code> instead of <code>kv_namespaces.id</code>.</li>
</ul>
</li>
<li>
<p><code>--ttl</code> optional</p>
<ul>
<li>The lifetime (in number of seconds) the document should exist before expiring. Must be at least <code>60</code> seconds. This option takes precedence over the <code>expiration</code> option.</li>
</ul>
</li>
<li>
<p><code>--expiration</code> optional</p>
<ul>
<li>The timestamp, in UNIX seconds, indicating when the key-value pair should expire.</li>
</ul>
</li>
<li>
<p><code>--path</code> optional</p>
<ul>
<li>When defined, Wrangler reads the <code>--path</code> file location to upload its contents as KV documents. This is ideal for security-sensitive operations because it avoids saving keys and values into your terminal history.</li>
</ul>
</li>
</ul>
<h5 id="usage-4">Usage</h5>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --binding=MY_KV &quot;key&quot; &quot;value&quot;&#10;✨  Success&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --binding=MY_KV --preview &quot;key&quot; &quot;value&quot;&#10;✨  Success&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --binding=MY_KV &quot;key&quot; &quot;value&quot; --ttl=10000&#10;✨  Success&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">wrangler kv:key put --binding=MY_KV &quot;key&quot; value.txt --path&#10;✨  Success&#10;</code></pre>
<h4 id="list-2"><code>list</code></h4>
<p>Output a list of all keys in a given namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key list --binding= [--namespace-id=] [--prefix] [--env]&#10;</code></pre>
<ul>
<li>
<p><code>--binding</code> required (if no <code>--namespace-id</code>)</p>
<ul>
<li>The name of the namespace to list.</li>
</ul>
</li>
<li>
<p><code>--namespace-id</code> required (if no <code>--binding</code>)</p>
<ul>
<li>The ID of the namespace to list.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--prefix</code> optional</p>
<ul>
<li>A prefix to filter listed keys.</li>
</ul>
</li>
</ul>
<h5 id="usage-5">Usage</h5>
<p>This example passes the Wrangler command through the <code>jq</code> command:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key list --binding=MY_KV --prefix=&quot;public&quot; | jq &quot;.&quot;&#10;[&#10;  {&#10;    &quot;name&quot;: &quot;public_key&quot;&#10;  },&#10;  {&#10;    &quot;name&quot;: &quot;public_key_with_expiration&quot;,&#10;    &quot;expiration&quot;: &quot;2019-09-10T23:18:58Z&quot;&#10;  }&#10;]&#10;</code></pre>
<h4 id="get"><code>get</code></h4>
<p>Read a single value by key from the given namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key get --binding= [--env=] [--preview] [--namespace-id=] &quot;$KEY&quot;&#10;</code></pre>
<ul>
<li>
<p><code>$KEY</code> required</p>
<ul>
<li>The key value to get.</li>
</ul>
</li>
<li>
<p><code>--binding</code> required (if no <code>--namespace-id</code>)</p>
<ul>
<li>The name of the namespace to get from.</li>
</ul>
</li>
<li>
<p><code>--namespace-id</code> required (if no <code>--binding</code>)</p>
<ul>
<li>The ID of the namespace to get from.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the operation will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--preview</code> optional</p>
<ul>
<li>Interact with a preview namespace instead of production. Pass this to use your Wrangler file’s <code>kv_namespaces.preview_id</code> instead of <code>kv_namespaces.id</code></li>
</ul>
</li>
</ul>
<h5 id="usage-6">Usage</h5>
<pre tabindex="0"><code class="language-sh">wrangler kv:key get --binding=MY_KV &quot;key&quot;&#10;value&#10;</code></pre>
<h4 id="delete-2"><code>delete</code></h4>
<p>Removes a single key value pair from the given namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:key delete --binding= [--env=] [--preview] [--namespace-id=] &quot;$KEY&quot;&#10;</code></pre>
<ul>
<li>
<p><code>$KEY</code> required</p>
<ul>
<li>The key value to delete.</li>
</ul>
</li>
<li>
<p><code>--binding</code> required (if no <code>--namespace-id</code>)</p>
<ul>
<li>The name of the namespace to delete from.</li>
</ul>
</li>
<li>
<p><code>--namespace-id</code> required (if no <code>--binding</code>)</p>
<ul>
<li>The id of the namespace to delete from.</li>
</ul>
</li>
<li>
<p><code>--env</code> optional</p>
<ul>
<li>Perform on a specific environment specified as <code>$ENVIRONMENT_NAME</code>.</li>
</ul>
</li>
<li>
<p><code>--preview</code> optional</p>
<ul>
<li>Interact with a preview namespace instead of production. Pass this to use your Wrangler configuration file's <code>kv_namespaces.preview_id</code> instead of <code>kv_namespaces.id</code></li>
</ul>
</li>
</ul>
<h5 id="usage-7">Usage</h5>
<pre tabindex="0"><code class="language-sh">wrangler kv:key delete --binding=MY_KV &quot;key&quot;&#10;Are you sure you want to delete key &quot;key&quot;? [y/n]&#10;yes&#10;🌀  Deleting key &quot;key&quot;&#10;✨  Success&#10;</code></pre>
<h3 id="kv-bulk"><code>kv:bulk</code></h3>
<h4 id="put-2"><code>put</code></h4>
<p>Write a file full of key-value pairs to the given namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:bulk put --binding= [--env=] [--preview] [--namespace-id=] $FILENAME&#10;</code></pre>
<ul>
<li>
<p><code>$FILENAME</code> required</p>
<ul>
<li>The file to write to the namespace</li>
</ul>
</li>
<li>
<p><code>--binding</code> required (if no <code>--namespace-id</code>)</p>
<ul>
<li>The name of the namespace to put to.</li>
</ul>
</li>
<li>
<p><code>--namespace-id</code> required (if no <code>--binding</code>)</p>
<ul>
<li>The id of the namespace to put to.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--preview</code> optional</p>
<ul>
<li>Interact with a preview namespace instead of production. Pass this to use your Wrangler file’s <code>kv_namespaces.preview_id</code> instead of <code>kv_namespaces.id</code></li>
</ul>
</li>
</ul>
<p>This command takes a JSON file as an argument with a list of key-value pairs to upload. An example of JSON input:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;key&quot;: &quot;test_key&quot;,&#10;		&quot;value&quot;: &quot;test_value&quot;,&#10;		&quot;expiration_ttl&quot;: 3600&#10;	}&#10;]&#10;</code></pre>
<p>In order to save JSON data, cast <code>value</code> to a string:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;key&quot;: &quot;test_key&quot;,&#10;		&quot;value&quot;: &quot;{\&quot;name\&quot;: \&quot;test_value\&quot;}&quot;,&#10;		&quot;expiration_ttl&quot;: 3600&#10;	}&#10;]&#10;</code></pre>
<p>The schema below is the full schema for key-value entries uploaded via the bulk API:</p>
<ul>
<li>
<p><code>key</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The key’s name. The name may be 512 bytes maximum. All printable, non-whitespace characters are valid.</li>
</ul>
</li>
<li>
<p><code>value</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The UTF-8 encoded string to be stored, up to 25 MB in length.</li>
</ul>
</li>
<li>
<p><code>expiration</code> int optional</p>
<ul>
<li>The time, measured in number of seconds since the UNIX epoch, at which the key should expire.</li>
</ul>
</li>
<li>
<p><code>expiration_ttl</code> int optional</p>
<ul>
<li>The number of seconds the document should exist before expiring. Must be at least <code>60</code> seconds.</li>
</ul>
</li>
<li>
<p><code>base64</code> bool optional</p>
<ul>
<li>When true, the server will decode the value as base64 before storing it. This is useful for writing values that would otherwise be invalid JSON strings, such as images. Defaults to <code>false</code>.</li>
</ul>
</li>
</ul>
<p>If both <code>expiration</code> and <code>expiration_ttl</code> are specified for a given key, the API will prefer <code>expiration_ttl</code>.</p>
<h5 id="usage-8">Usage</h5>
<pre tabindex="0"><code class="language-sh">wrangler kv:bulk put --binding=MY_KV allthethingsupload.json&#10;🌀  uploading 1 key value pairs&#10;✨  Success&#10;</code></pre>
<h4 id="delete-3"><code>delete</code></h4>
<p>Delete all specified keys within a given namespace.</p>
<pre tabindex="0"><code class="language-sh">wrangler kv:bulk delete --binding= [--env=] [--preview] [--namespace-id=] $FILENAME&#10;</code></pre>
<ul>
<li>
<p><code>$FILENAME</code> required</p>
<ul>
<li>The file with key-value pairs to delete.</li>
</ul>
</li>
<li>
<p><code>--binding</code> required (if no <code>--namespace-id</code>)</p>
<ul>
<li>The name of the namespace to delete from.</li>
</ul>
</li>
<li>
<p><code>--namespace-id</code> required (if no <code>--binding</code>)</p>
<ul>
<li>The ID of the namespace to delete from.</li>
</ul>
</li>
<li>
<p><code>--env $ENVIRONMENT_NAME</code> optional</p>
<ul>
<li>If defined, the changes will only apply to the specified environment. Refer to <a href="/workers/wrangler/environments/">Environments</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--preview</code> optional</p>
<ul>
<li>Interact with a preview namespace instead of production. Pass this to use your Wrangler file’s <code>kv_namespaces.preview_id</code> instead of <code>kv_namespaces.id</code></li>
</ul>
</li>
</ul>
<p>This command takes a JSON file as an argument with a list of key-value pairs to delete. An example of JSON input:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;key&quot;: &quot;test_key&quot;,&#10;		&quot;value&quot;: &quot;&quot;&#10;	}&#10;]&#10;</code></pre>
<ul>
<li>
<p><code>key</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The key’s name. The name may be at most 512 bytes. All printable, non-whitespace characters are valid.</li>
</ul>
</li>
<li>
<p><code>value</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>This field must be specified for deserialization purposes, but is unused because the provided keys are being deleted, not written.</li>
</ul>
</li>
</ul>
<h5 id="usage-9">Usage</h5>
<pre tabindex="0"><code class="language-sh">wrangler kv:bulk delete --binding=MY_KV allthethingsdelete.json&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Are you sure you want to delete all keys in allthethingsdelete.json? [y/n]&#10;y&#10;🌀  deleting 1 key value pairs&#10;✨  Success&#10;</code></pre>
<hr />
<h2 id="environment-variables">Environment variables</h2>
<p>Wrangler supports any <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> keys passed in as environment variables. This works by passing in <code>CF_</code> + any uppercased TOML key. For example:</p>
<p><code>CF_NAME=my-worker CF_ACCOUNT_ID=1234 wrangler dev</code></p>
<hr />
<h2 id="help">--help</h2>
<pre tabindex="0"><code class="language-sh">wrangler --help&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">👷 ✨  wrangler 1.12.3&#10;The Wrangler Team &lt;wrangler@cloudflare.com&gt;&#10;&#10;USAGE:&#10;    wrangler [SUBCOMMAND]&#10;&#10;FLAGS:&#10;    &#45;h, --help       Prints help information&#10;    &#45;V, --version    Prints version information&#10;&#10;SUBCOMMANDS:&#10;    kv:namespace    🗂️  Interact with your Workers KV Namespaces&#10;    kv:key          🔑  Individually manage Workers KV key-value pairs&#10;    kv:bulk         💪  Interact with multiple Workers KV key-value pairs at once&#10;    route           ➡️  List or delete worker routes.&#10;    secret          🤫  Generate a secret that can be referenced in the worker script&#10;    generate        👯  Generate a new worker project&#10;    init            📥  Create a wrangler.toml for an existing project&#10;    build           🦀  Build your worker&#10;    preview         🔬  Preview your code temporarily on cloudflareworkers.com&#10;    dev             👂  Start a local server for developing your worker&#10;    publish         🆙  Publish your worker to the orange cloud&#10;    config          🕵️  Authenticate Wrangler with a Cloudflare API Token or Global API Key&#10;    subdomain       👷  Configure your workers.dev subdomain&#10;    whoami          🕵️  Retrieve your user info and test your auth config&#10;    tail            🦚  Aggregate logs from production worker&#10;    login           🔓  Authorize Wrangler with your Cloudflare username and password&#10;    logout          ⚙️  Remove authorization from Wrangler.&#10;    help            Prints this message or the help of the given subcommand(s)&#10;</code></pre>
