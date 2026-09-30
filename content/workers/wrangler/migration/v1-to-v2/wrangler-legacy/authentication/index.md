<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17488.md")
</aside>
<h2 id="background">Background</h2>
<p>In Cloudflare’s system, a user can have multiple accounts and zones. As a result, your user is configured globally on your machine via a single Cloudflare Token. Your account(s) and zone(s) will be configured per project, but will use your Cloudflare Token to authenticate all API calls. A configuration file is created in a <code>.wrangler</code> directory in your computer’s home directory.</p>
<hr />
<h3 id="using-commands">Using commands</h3>
<p>To set up Wrangler to work with your Cloudflare user, use the following commands:</p>
<ul>
<li><code>login</code>: a command that opens a Cloudflare account login page to authorize Wrangler.</li>
<li><code>config</code>: an alternative to <code>login</code> that prompts you to enter your <code>email</code> and <code>api</code> key.</li>
<li><code>whoami</code>: run this command to confirm that your configuration is appropriately set up. When successful, this command will print out your account email and your <code>account_id</code> needed for your project's Wrangler file.</li>
</ul>
<h3 id="using-environment-variables">Using environment variables</h3>
<p>You can also configure your global user with environment variables. This is the preferred method for using Wrangler in CI (continuous integration) environments.</p>
<p>To customize the authentication tokens that Wrangler uses, you may provide the <code>CF_ACCOUNT_ID</code> and <code>CF_API_TOKEN</code> environment variables when running any Wrangler command. The account ID may be obtained from the Cloudflare dashboard in <strong>Overview</strong> and you may <a href="#generate-tokens">create or reuse an existing API token</a>.</p>
<pre><code class="language-sh">CF_ACCOUNT_ID=accountID CF_API_TOKEN=veryLongAPIToken wrangler publish&#10;</code></pre>
<p>Alternatively, you may use the <code>CF_EMAIL</code> and <code>CF_API_KEY</code> environment variable combination instead:</p>
<pre><code class="language-sh">CF_EMAIL=cloudflareEmail CF_API_KEY=veryLongAPI wrangler publish&#10;</code></pre>
<p>You can also specify or override the target Zone ID by defining the <code>CF_ZONE_ID</code> environment variable.</p>
<p>Defining environment variables inline will override the default credentials stored in <code>wrangler config</code> or in your Wrangler file.</p>
<hr />
<h2 id="generate-tokens">Generate Tokens</h2>
<h3 id="api-token">API token</h3>
<ol>
<li>In <strong>Overview</strong>, select <a href="/fundamentals/api/get-started/create-token/"><strong>Get your API token</strong></a>.</li>
<li>After being taken to the <strong>Profile</strong> page, select <strong>Create token</strong>.</li>
<li>Under the <strong>API token templates</strong> section, find the <strong>Edit Cloudflare Workers</strong> template and select <strong>Use template</strong>.</li>
<li>Fill out the rest of the fields and then select <strong>Continue to summary</strong>, where you can select <strong>Create Token</strong> and issue your token for use.</li>
</ol>
<h3 id="global-api-key">Global API Key</h3>
<ol>
<li>In <strong>Overview</strong>, select <strong>Get your API token</strong>.</li>
<li>After being taken to the <strong>Profile</strong> page, scroll to <strong>API Keys</strong>.</li>
<li>Select <strong>View</strong> to copy your <strong>Global API Key</strong>.*</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17487.md")
</aside>
<hr />
<h2 id="use-tokens">Use Tokens</h2>
<p>After getting your token or key, you can set up your default credentials on your local machine by running <code>wrangler config</code>:</p>
<pre><code class="language-sh">wrangler config&#10;</code></pre>
<pre><code class="language-sh">Enter API token:&#10;superlongapitoken&#10;</code></pre>
<p>Use the <code>--api-key</code> flag to instead configure with email and global API key:</p>
<pre><code class="language-sh">wrangler config --api-key&#10;</code></pre>
<pre><code class="language-sh">Enter email:&#10;testuser@example.com&#10;Enter global API key:&#10;superlongapikey&#10;</code></pre>
