<p>Cloudflare Pages supports custom package registries, allowing you to include private dependencies in your application. While this walkthrough focuses specifically on <a href="https://www.npmjs.com/">npm</a>, the Node package manager and registry, the same approach can be applied to other registry tools.</p>
<p>You will be adjusting the <a href="/pages/configuration/build-configuration/#environment-variables">environment variables</a> in your Pages project's <strong>Settings</strong>. An existing website can be modified at any time, but new projects can be initialized with these settings, too. Either way, altering the project settings will not be reflected until its next deployment.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10894.md")
</aside>
<h2 id="registry-access-token">Registry Access Token</h2>
<p>Every package registry should have a means of issuing new access tokens. Ideally, you should create a new token specifically for Pages, as you would with any other CI/CD platform.</p>
<p>With npm, you can <a href="https://docs.npmjs.com/creating-and-viewing-access-tokens">create and view tokens through its website</a> or you can use the <code>npm</code> CLI. If you have the CLI set up locally and are authenticated, run the following commands in your terminal:</p>
<pre><code class="language-sh">&#35; Verify the current npm user is correct&#10;npm whoami&#10;&#10;&#35; Create a readonly token&#10;npm token create --read-only&#10;&#35;-&gt; Enter password, if prompted&#10;&#35;-&gt; Enter 2FA code, if configured&#10;</code></pre>
<p>This will produce a read-only token that looks like a UUID string. Save this value for a later step.</p>
<h2 id="private-modules-on-the-npm-registry">Private modules on the npm registry</h2>
<p>The following section applies to users with applications that are only using private modules from the npm registry.</p>
<p>In your Pages project's <strong>Settings</strong> &gt; <strong>Environment variables</strong>, add a new <a href="/pages/configuration/build-configuration/#environment-variables">environment variable</a> named <code>NPM_TOKEN</code> to the <strong>Production</strong> and <strong>Preview</strong> environments and paste the <a href="#registry-access-token">read-only token you created</a> as its value.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10893.md")
</aside>
<p>By default, <code>npm</code> looks for an environment variable named <code>NPM_TOKEN</code> and because you did not define a <a href="#custom-registry-endpoints">custom registry endpoint</a>, the npm registry is assumed. Local development should continue to work as expected, provided that you and your teammates are authenticated with npm accounts (see <code>npm whoami</code> and <code>npm login</code>) that have been granted access to the private package(s).</p>
<h2 id="custom-registry-endpoints">Custom registry endpoints</h2>
<p>When multiple registries are in use, a project will need to define its own root-level <a href="https://docs.npmjs.com/cli/v7/configuring-npm/npmrc"><code>.npmrc</code></a> configuration file. An example <code>.npmrc</code> file may look like this:</p>
<pre><code class="language-ini">@foobar:registry=https://npm.pkg.github.com&#10;//registry.npmjs.org/:_authToken=${TOKEN_FOR_NPM}&#10;//npm.pkg.github.com/:_authToken=${TOKEN_FOR_GITHUB}&#10;</code></pre>
<p>Here, all packages under the <code>@foobar</code> scope are directed towards the GitHub Packages registry. Then the registries are assigned their own access tokens via their respective environment variable names.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10892.md")
</aside>
<p>Your Pages project must then have the matching <a href="/pages/configuration/build-configuration/#environment-variables">environment variables</a> defined for all environments. In our example, that means <code>TOKEN_FOR_NPM</code> must contain <a href="#registry-access-token">the read-only npm token</a> value and <code>TOKEN_FOR_GITHUB</code> must contain its own <a href="https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token#creating-a-token">personal access token</a>.</p>
<h3 id="managing-multiple-environments">Managing multiple environments</h3>
<p>In the event that your local development no longer works with your new <code>.npmrc</code> file, you will need to add some additional changes:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/10895.md")
</div>
