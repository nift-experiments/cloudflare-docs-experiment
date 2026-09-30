---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/configuration/
  description: Understand the different settings associated with your build.
  full_title: Configuration · Cloudflare Workers docs
  head_html: <title>Configuration · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand the different settings associated with your build."><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/configuration/index.md"><meta property="og:title" content="Configuration · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the different settings associated with your build."><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#page","headline":"Configuration \u00b7 Cloudflare Workers docs","description":"Understand the different settings associated with your build.","url":"https://developers.cloudflare.com/workers/ci-cd/builds/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/configuration/
  schema: 1
---
<p>When connecting your Git repository to your Worker, you can customize the configurations needed to build and deploy your Worker.</p>
<h2 id="how-workers-builds-works">How Workers Builds works</h2>
<p>When a commit is pushed to your connected repository, Workers Builds runs a two-step process:</p>
<ol>
<li><strong>Build command</strong> <em>(optional)</em> - Compiles your project (for example, <code>npm run build</code> for frameworks like Next.js or Astro)</li>
<li><strong>Deploy command</strong> - Deploys your Worker to Cloudflare (defaults to <code>npx wrangler deploy</code>)</li>
</ol>
<p>For preview builds (commits to branches other than your production branch), the deploy command is replaced with a <strong>preview deploy command</strong> (defaults to <code>npx wrangler versions upload</code>), which creates a preview version without promoting it to production.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-that-use-containers">Workers that use Containers</h3>
@markup("md", "content/.markup/bodies/16774.md")
</aside>
<h2 id="build-settings">Build settings</h2>
<p>Build settings can be found by navigating to <strong>Settings</strong> &gt; <strong>Build</strong> within your Worker.</p>
<p>Note that when you update and save build settings, the updated settings will be applied to your <em>next</em> build. When you <em>retry</em> a build, the build configurations that exist when the build is retried will be applied.</p>
<h3 id="overview">Overview</h3>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Git account</strong></td>
<td>Select the Git account you would like to use. After the initial connection, you can continue to use this Git account for future projects.</td>
</tr>
<tr>
<td><strong>Git repository</strong></td>
<td>Choose the Git repository you would like to connect your Worker to.</td>
</tr>
<tr>
<td><strong>Git branch</strong></td>
<td>Select the branch you would like Cloudflare to listen to for new commits. This will be defaulted to <code>main</code>.</td>
</tr>
<tr>
<td><strong>Build command</strong> <em>(Optional)</em></td>
<td>Set a build command if your project requires a build step (e.g. <code>npm run build</code>). This is necessary, for example, when using a <a href="/workers/ci-cd/builds/configuration/#framework-support">front-end framework</a> such as Next.js or Remix.</td>
</tr>
<tr>
<td><strong><a href="/workers/ci-cd/builds/configuration/#deploy-command">Deploy command</a></strong></td>
<td>The deploy command lets you set the <a href="/workers/wrangler/commands/general/#deploy">specific Wrangler command</a> used to deploy your Worker. Your deploy command will default to <code>npx wrangler deploy</code> but you may customize this command. Workers Builds will use the Wrangler version set in your <code>package.json</code>.</td>
</tr>
<tr>
<td><strong><a href="/workers/ci-cd/builds/configuration/#non-production-branch-deploy-command">Non-production branch deploy command</a></strong></td>
<td>Set a command to run when executing <a href="/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds">a build for commit on a non-production branch</a>. This will default to <code>npx wrangler versions upload</code> but you may customize this command. Workers Builds will use the Wrangler version set in your <code>package.json</code>.</td>
</tr>
<tr>
<td><strong>Root directory</strong> <em>(Optional)</em></td>
<td>Specify the path to your project. The root directory defines where the build command will be run and can be helpful in <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepos</a> to isolate a specific project within the repository for builds.</td>
</tr>
<tr>
<td><strong><a href="/workers/ci-cd/builds/configuration/#api-token">API token</a></strong> <em>(Optional)</em></td>
<td>The API token is used to authenticate your build request and authorize the upload and deployment of your Worker to Cloudflare. By default, Cloudflare will automatically generate an API token for your account when using Workers Builds, and continue to use this API token for all subsequent builds. Alternatively, you can <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/authentication/#generate-tokens">create your own API token</a>, or select one that you already own.</td>
</tr>
<tr>
<td><strong>Build variables and secrets</strong> <em>(Optional)</em></td>
<td>Add environment variables and secrets accessible only to your build. Build variables will not be accessible at runtime. If you would like to configure runtime variables you can do so in <strong>Settings</strong> &gt; <strong>Variables &amp; Secrets</strong></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16773.md")
</aside>
<h3 id="deploy-command">Deploy command</h3>
<p>You can run your deploy command using the package manager of your choice.</p>
<p>If you have added a Wrangler deploy command as a script in your <code>package.json</code>, then you can run it by setting it as your deploy command. For example, <code>npm run deploy</code>.</p>
<p>Examples of other deploy commands you can set include:</p>
<table>
<thead>
<tr>
<th>Example Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>npx wrangler deploy --assets ./public/</code></td>
<td>Deploy your Worker along with static assets from the specified directory. Alternatively, you can use the <a href="/workers/static-assets/binding/">assets binding</a>.</td>
</tr>
<tr>
<td><code>npx wrangler deploy --env staging</code></td>
<td>If you have a <a href="/workers/ci-cd/builds/advanced-setups/#wrangler-environments">Wrangler environment</a> Worker, you should set your deploy command with the environment flag. For more details, see <a href="/workers/ci-cd/builds/advanced-setups/#wrangler-environments">Advanced Setups</a>.</td>
</tr>
<tr>
<td><code>npx wrangler deploy --containers-rollout=immediate</code></td>
<td><a href="/containers/">Containers</a> rollout mode for this deploy. Refer to <a href="/containers/configuration/rollouts/">Rollouts</a>.</td>
</tr>
<tr>
<td><code>npx wrangler deploy --containers-rollout=none</code></td>
<td>Deploy the Worker only. Skip container image build/push and instance rollout.</td>
</tr>
</tbody>
</table>
<h3 id="non-production-branch-deploy-command">Non-production branch deploy command</h3>
<p>The non-production branch deploy command is only applicable when you have enabled <a href="/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds">non-production branch builds</a>.</p>
<p>It defaults to <code>npx wrangler versions upload</code>, producing a <a href="/workers/versions-and-deployments/preview-urls/">preview URL</a>. Like the build and deploy commands, it can be customized to instead run anything.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16772.md")
</aside>
<p>Examples of other non-production branch deploy commands you can set include:</p>
<table>
<thead>
<tr>
<th>Example Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>yarn exec wrangler versions upload</code></td>
<td>You can customize the package manager used to run Wrangler.</td>
</tr>
<tr>
<td><code>npx wrangler versions upload --env staging</code></td>
<td>If you have a <a href="/workers/ci-cd/builds/advanced-setups/#wrangler-environments">Wrangler environment</a> Worker, you should set your non-production branch deploy command with the environment flag. For more details, see <a href="/workers/ci-cd/builds/advanced-setups/#wrangler-environments">Advanced Setups</a>.</td>
</tr>
</tbody>
</table>
<h3 id="automatic-configuration-for-new-projects">Automatic configuration for new projects</h3>
<p>If your repository does not have a Wrangler configuration file, the deploy command (<code>wrangler deploy</code>) will trigger <a href="/workers/framework-guides/automatic-configuration/">automatic project configuration</a>. This detects your framework, creates the necessary configuration, and opens a <a href="/workers/ci-cd/builds/automatic-prs/">pull request</a> for you to review. Once you merge the PR, your project is configured and future builds will deploy normally.</p>
<h3 id="api-token">API token</h3>
<p>The API token in Workers Builds defines the access granted to Workers Builds for interacting with your account's resources. Currently, only user tokens are supported, with account-owned token support coming soon.</p>
<p>When you select <strong>Create new token</strong>, a new API token will be created automatically with the following permissions:</p>
<ul>
<li><strong>Account:</strong> Account Settings (read), Workers Scripts (edit), Workers KV Storage (edit), Workers R2 Storage (edit)</li>
<li><strong>Zone:</strong> Workers Routes (edit) for all zones on the account</li>
<li><strong>User:</strong> User Details (read), Memberships (read)</li>
</ul>
<p>You can configure the permissions of this API token by navigating to <strong>My Profile</strong> &gt; <strong>API Tokens</strong> for user tokens.</p>
<p>It is recommended to consistently use the same API token across all uploads and deployments of your Worker to maintain consistent access permissions.</p>
<h2 id="framework-support">Framework support</h2>
<p><a href="/workers/static-assets/">Static assets</a> and <a href="/workers/framework-guides/">frameworks</a> are now supported in Cloudflare Workers. Learn to set up Workers projects and the commands for each framework in the framework guides:</p>
<ul class="directory-listing"><li><a href="/workers/framework-guides/automatic-configuration/">Deploy an existing project</a></li><li><a href="/workers/framework-guides/web-apps/react/">React + Vite</a></li><li><a href="/workers/framework-guides/web-apps/">Web applications</a></li><li><a href="/workers/framework-guides/web-apps/astro/">Astro</a></li><li><a href="/workers/framework-guides/mobile-apps/">Mobile applications</a></li><li><a href="/workers/framework-guides/apis/">APIs</a></li><li><a href="/workers/framework-guides/web-apps/react-router/">React Router (formerly Remix)</a></li><li><a href="/workers/framework-guides/ai-and-agents/">AI &amp; agents</a></li><li><a href="/workers/framework-guides/web-apps/nextjs/">Next.js</a></li><li><a href="/workers/framework-guides/web-apps/opennext/">OpenNext adapter</a></li><li><a href="/workers/framework-guides/web-apps/vue/">Vue</a></li><li><a href="/workers/framework-guides/web-apps/redwoodsdk/">RedwoodSDK</a></li><li><a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a></li><li><a href="/workers/framework-guides/web-apps/microfrontends/">Microfrontends</a></li><li><a href="/workers/framework-guides/web-apps/sveltekit/">SvelteKit</a></li><li><a href="/workers/framework-guides/web-apps/vike/">Vike</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/">More guides...</a></li><li><a href="/agents/">Agents SDK</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/analog/">Analog</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/angular/">Angular</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/docusaurus/">Docusaurus</a></li><li><a href="https://docs.expo.dev/eas/hosting/reference/worker-runtime/">Expo</a></li><li><a href="/workers/languages/python/packages/fastapi/">FastAPI</a></li><li><a href="/workers/languages/python/packages/flask/">Flask</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/gatsby/">Gatsby</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/hono/">Hono</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/hono/">Hono</a></li><li><a href="/workers/languages/python/packages/langchain/">LangChain</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/nuxt/">Nuxt</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/qwik/">Qwik</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/solid/">Solid</a></li><li><a href="/workers/framework-guides/web-apps/more-web-frameworks/waku/">Waku</a></li></ul>
<h2 id="environment-variables">Environment variables</h2>
<p>You can provide custom environment variables to your build.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16778.md")
</div></div>
<h3 id="default-variables">Default variables</h3>
<p>The following system environment variables are injected by default (but can be overridden):</p>
<table>
<thead>
<tr>
<th>Environment Variable</th>
<th>Injected value</th>
<th>Example use-case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CI</code></td>
<td><code>true</code></td>
<td>Changing build behaviour when run on CI versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI</code></td>
<td><code>1</code></td>
<td>Changing build behaviour when run on Workers Builds versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI_BUILD_UUID</code></td>
<td><code>&lt;build-uuid-of-current-build&gt;</code></td>
<td>Passing the Build UUID along to custom workflows</td>
</tr>
<tr>
<td><code>WORKERS_CI_COMMIT_SHA</code></td>
<td><code>&lt;sha1-hash-of-current-commit&gt;</code></td>
<td>Passing current commit ID to error reporting, for example, Sentry</td>
</tr>
<tr>
<td><code>WORKERS_CI_BRANCH</code></td>
<td><code>&lt;branch-name-from-push-event</code></td>
<td>Customizing build based on branch, for example, disabling debug logging on <code>production</code></td>
</tr>
</tbody>
</table>
