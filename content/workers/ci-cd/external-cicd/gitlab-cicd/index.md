<p>You can deploy Workers with <a href="https://docs.gitlab.com/ee/ci/pipelines/index.html">GitLab CI/CD</a>. Here is how you can set up your Gitlab CI/CD pipeline.</p>
<h2 id="1-authentication"><ol>
<li>Authentication</li>
</ol></h2>
<p>When running Wrangler locally, authentication to the Cloudflare API happens via the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> command, which initiates an interactive authentication flow. Since CI/CD environments are non-interactive, Wrangler requires a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> and <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> to authenticate with the Cloudflare API.</p>
<h3 id="cloudflare-account-id">Cloudflare account ID</h3>
<p>To find your Cloudflare account ID, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find account and zone IDs</a>.</p>
<h3 id="api-token">API token</h3>
<p>To create an API token to authenticate Wrangler in your CI job:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Under <strong>Permission policies</strong>, open the <strong>Custom</strong> dropdown and select <strong>Edit Cloudflare Workers</strong>.</li>
<li>Customize your token name.</li>
<li>Scope your token.</li>
</ol>
<p>You will need to choose the account and zone resources that the generated API token will have access to. We recommend scoping these down as much as possible to limit the access of your token. For example, if you have access to three different Cloudflare accounts, you should restrict the generated API token to only the account on which you will be deploying a Worker.</p>
<h2 id="2-set-up-ci"><ol start="2">
<li>Set up CI</li>
</ol></h2>
<p>The method for running Wrangler in your CI/CD environment will depend on the specific setup for your project (whether you use GitHub Actions/Jenkins/GitLab or something else entirely).</p>
<p>To set up your CI:</p>
<ol>
<li>Go to your CI platform and add the following as secrets:</li>
</ol>
<ul>
<li><code>CLOUDFLARE_ACCOUNT_ID</code>: Set to the <a href="#cloudflare-account-id">Cloudflare account ID</a> for the account on which you want to deploy your Worker.</li>
<li><code>CLOUDFLARE_API_TOKEN</code>: Set to the <a href="#api-token">Cloudflare API token you generated</a>.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16763.md")
</aside>
<ol start="2">
<li>Create a workflow that will be responsible for deploying the Worker. This workflow should run <code>wrangler deploy</code>. Review an example <a href="https://docs.github.com/en/actions/using-workflows/about-workflows">GitHub Actions</a> workflow in the following section.</li>
</ol>
<h3 id="gitlab-pipelines">GitLab Pipelines</h3>
<p>Refer to <a href="https://about.gitlab.com/blog/2022/11/21/deploy-remix-with-gitlab-and-cloudflare/">GitLab's blog</a> for an example pipeline. Under the <code>script</code> key, replace <code>npm run deploy</code> with <a href="/workers/wrangler/commands/general/#deploy"><code>npx wrangler deploy</code></a>.</p>
