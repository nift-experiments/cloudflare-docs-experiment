---
cp9:
  canonical: https://developers.cloudflare.com/pages/get-started/c3/
  description: Use C3 (`create-cloudflare` CLI) to set up and deploy new applications using framework-specific setup guides to ensure each new application follows Cloudflare and any third-party best practices for deployment.
  full_title: Create projects with C3 CLI · Cloudflare Pages docs
  head_html: <title>Create projects with C3 CLI · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Use C3 (`create-cloudflare` CLI) to set up and deploy new applications using framework-specific setup guides to ensure each new application follows Cloudflare and any third-party best practices for deployment."><link rel="canonical" href="https://developers.cloudflare.com/pages/get-started/c3/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/get-started/c3/index.md"><meta property="og:title" content="Create projects with C3 CLI · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use C3 (`create-cloudflare` CLI) to set up and deploy new applications using framework-specific setup guides to ensure each new application follows Cloudflare and any third-party best practices for deployment."><meta property="og:url" content="https://developers.cloudflare.com/pages/get-started/c3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/get-started/c3/#page","headline":"Create projects with C3 CLI \u00b7 Cloudflare Pages docs","description":"Use C3 (create-cloudflare CLI) to set up and deploy new applications using framework-specific setup guides to ensure each new application follows Cloudflare and any third-party best practices for deployment.","url":"https://developers.cloudflare.com/pages/get-started/c3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/get-started/c3/
  schema: 1
---
<p>Cloudflare provides a CLI command for creating new Workers and Pages projects — <code>npm create cloudflare</code>, powered by the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code> package</a>.</p>
<h2 id="create-a-new-application">Create a new application</h2>
<p>Open a terminal window and run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest --platform=pages" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Running this command will prompt you to install the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> package, and then ask you questions about the type of application you wish to create.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10912.md")
</aside>
<h2 id="web-frameworks">Web frameworks</h2>
<p>If you choose the &quot;Framework Starter&quot; option, you will be prompted to choose a framework to use. The following frameworks are currently supported:</p>
<ul>
<li><a href="/pages/framework-guides/deploy-an-angular-site/">Angular</a></li>
<li><a href="/pages/framework-guides/deploy-an-astro-site/">Astro</a></li>
<li><a href="/pages/framework-guides/deploy-a-docusaurus-site/">Docusaurus</a></li>
<li><a href="/pages/framework-guides/deploy-a-gatsby-site/">Gatsby</a></li>
<li><a href="/pages/framework-guides/deploy-a-hono-site/">Hono</a></li>
<li><a href="/pages/framework-guides/nextjs/deploy-a-static-nextjs-site/">Next.js static exports</a></li>
<li><a href="/pages/framework-guides/deploy-a-nuxt-site/">Nuxt</a></li>
<li><a href="/pages/framework-guides/deploy-a-qwik-site/">Qwik</a></li>
<li><a href="/pages/framework-guides/deploy-a-react-site/">React</a></li>
<li><a href="/workers/framework-guides/web-apps/redwoodsdk/">Redwood</a></li>
<li><a href="/pages/framework-guides/deploy-a-remix-site/">Remix</a></li>
<li><a href="/pages/framework-guides/deploy-a-solid-start-site/">SolidStart</a></li>
<li><a href="/pages/framework-guides/deploy-a-svelte-kit-site/">SvelteKit</a></li>
<li><a href="/pages/framework-guides/deploy-a-vue-site/">Vue</a></li>
</ul>
<p>When you use a framework, <code>npm create cloudflare</code> directly uses the framework's own command for generating a new projects, which may prompt additional questions. This ensures that the project you create is up-to-date with the latest version of the framework, and you have all the same options when creating you project via <code>npm create cloudflare</code> that you would if you created your project using the framework's tooling directly.</p>
<h2 id="deploy">Deploy</h2>
<p>Once your project has been configured, you will be asked if you would like to deploy the project to Cloudflare. This is optional.</p>
<p>If you choose to deploy, you will be asked to sign into your Cloudflare account (if you aren't already), and your project will be deployed.</p>
<h2 id="creating-a-new-pages-project-that-is-connected-to-a-git-repository">Creating a new Pages project that is connected to a git repository</h2>
<p>To create a new project using <code>npm create cloudflare</code>, and then connect it to a Git repository on your Github or Gitlab account, take the following steps:</p>
<ol>
<li>Run <code>npm create cloudflare@latest</code>, and choose your desired options</li>
<li>Select <code>no</code> to the prompt, &quot;Do you want to deploy your application?&quot;. This is important — if you select <code>yes</code> and deploy your application from your terminal (<a href="/pages/get-started/direct-upload/">Direct Upload</a>), then it will not be possible to connect this Pages project to a git repository later on. You will have to create a new Cloudflare Pages project.</li>
<li>Create a new git repository, using the application that <code>npm create cloudflare@latest</code> just created for you.</li>
<li>Follow the steps outlined in the <a href="/pages/get-started/git-integration/">Git integration guide</a></li>
</ol>
<h2 id="cli-arguments">CLI Arguments</h2>
<p>C3 collects any required input through a series of interactive prompts. You may also specify your choices via command line arguments, which will skip these prompts. To use C3 in a non-interactive context such as CI, you must specify all required arguments via the command line.</p>
<p>This is the full format of a C3 invocation alongside the possible CLI arguments:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- --platform=pages [&lt;DIRECTORY&gt;] [OPTIONS] [-- &lt;NESTED ARGS...&gt;]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- --platform=pages [&lt;DIRECTORY&gt;] [OPTIONS] [-- &lt;NESTED ARGS...&gt;]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare --platform=pages [&lt;DIRECTORY&gt;] [OPTIONS] [-- &lt;NESTED ARGS...&gt;]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare --platform=pages [&lt;DIRECTORY&gt;] [OPTIONS] [-- &lt;NESTED ARGS...&gt;]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest --platform=pages [&lt;DIRECTORY&gt;] [OPTIONS] [-- &lt;NESTED ARGS...&gt;]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest --platform=pages [&lt;DIRECTORY&gt;] [OPTIONS] [-- &lt;NESTED ARGS...&gt;]" aria-label="Copy to clipboard">Copy</button></div></div>
<ul>
<li>
<p><code>DIRECTORY</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The directory where the application should be created. The name of the application is taken from the directory name.</li>
</ul>
</li>
<li>
<p><code>NESTED ARGS..</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>CLI arguments to pass to eventual third party CLIs C3 might invoke (in the case of full-stack applications).</li>
</ul>
</li>
<li>
<p><code>--category</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>The kind of templates that should be created.</p>
</li>
<li>
<p>The possible values for this option are:</p>
<ul>
<li><code>hello-world</code>: Hello World example</li>
<li><code>web-framework</code>: Framework Starter</li>
<li><code>demo</code>: Application Starter</li>
<li><code>remote-template</code>: Template from a GitHub repo</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>--type</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>The type of application that should be created.</p>
</li>
<li>
<p>The possible values for this option are:</p>
<ul>
<li><code>hello-world</code>: A basic &quot;Hello World&quot; Cloudflare Worker.</li>
<li><code>hello-world-durable-object</code>: A <a href="/durable-objects/">Durable Object</a> and a Worker to communicate with it.</li>
<li><code>common</code>: A Cloudflare Worker which implements a common example of routing/proxying functionalities.</li>
<li><code>scheduled</code>: A scheduled Cloudflare Worker (triggered via <a href="/workers/configuration/cron-triggers/">Cron Triggers</a>).</li>
<li><code>queues</code>: A Cloudflare Worker which is both a consumer and produced of <a href="/queues/">Queues</a>.</li>
<li><code>openapi</code>: A Worker implementing an OpenAPI REST endpoint.</li>
<li><code>pre-existing</code>: Fetch a Worker initialized from the Cloudflare dashboard.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>--framework</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>The type of framework to use to create a web application (when using this option, <code>--type</code> is ignored).</p>
</li>
<li>
<p>The possible values for this option are:</p>
<ul>
<li><code>angular</code></li>
<li><code>astro</code></li>
<li><code>docusaurus</code></li>
<li><code>gatsby</code></li>
<li><code>hono</code></li>
<li><code>next</code></li>
<li><code>nuxt</code></li>
<li><code>qwik</code></li>
<li><code>react</code></li>
<li><code>redwood</code></li>
<li><code>remix</code></li>
<li><code>solid</code></li>
<li><code>svelte</code></li>
<li><code>vue</code></li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>--template</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>Create a new project via an external template hosted in a git repository</p>
</li>
<li>
<p>The value for this option may be specified as any of the following:</p>
<ul>
<li><code>user/repo</code></li>
<li><code>git@github.com:user/repo</code></li>
<li><code>https://github.com/user/repo</code></li>
<li><code>user/repo/some-template</code> (subdirectories)</li>
<li><code>user/repo#canary</code> (branches)</li>
<li><code>user/repo#1234abcd</code> (commit hash)</li>
<li><code>bitbucket:user/repo</code> (BitBucket)</li>
<li><code>gitlab:user/repo</code> (GitLab)</li>
</ul>
<p>See the <code>degit</code> <a href="https://github.com/Rich-Harris/degit">docs</a> for more details.</p>
<p>At a minimum, templates must contain the following:</p>
<ul>
<li><code>package.json</code></li>
<li><a href="/pages/functions/wrangler-configuration/">Wrangler configuration file</a></li>
<li><code>src/</code> containing a worker script referenced from the Wrangler configuration file</li>
</ul>
<p>See the <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare/templates">templates folder</a> of this repo for more examples.</p>
</li>
</ul>
</li>
<li>
<p><code>--deploy</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span></p>
<ul>
<li>Deploy your application after it has been created.</li>
</ul>
</li>
<li>
<p><code>--lang</code> <span class="nb-type">string</span> <span class="nb-metainfo">(default: ts) optional</span></p>
<ul>
<li>
<p>The programming language of the template.</p>
</li>
<li>
<p>The possible values for this option are:</p>
<ul>
<li><code>ts</code></li>
<li><code>js</code></li>
<li><code>python</code></li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>--ts</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span></p>
<ul>
<li>Use TypeScript in your application. Deprecated. Use <code>--lang=ts</code> instead.</li>
</ul>
</li>
<li>
<p><code>--git</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span></p>
<ul>
<li>Initialize a local git repository for your application.</li>
</ul>
</li>
<li>
<p><code>--open</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span></p>
<ul>
<li>Open with your browser the deployed application (this option is ignored if the application is not deployed).</li>
</ul>
</li>
<li>
<p><code>--existing-script</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>The name of an existing Cloudflare Workers script to clone locally. When using this option, <code>--type</code> is coerced to <code>pre-existing</code>.</p>
</li>
<li>
<p>When <code>--existing-script</code> is specified, <code>deploy</code> will be ignored.</p>
</li>
</ul>
</li>
<li>
<p><code>-y</code>, <code>--accept-defaults</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Use all the default C3 options each can also be overridden by specifying it.</li>
</ul>
</li>
<li>
<p><code>--auto-update</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span></p>
<ul>
<li>Automatically uses the latest version of C3.</li>
</ul>
</li>
<li>
<p><code>-v</code>, <code>--version</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Show version number.</li>
</ul>
</li>
<li>
<p><code>-h</code>, <code>--help</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Show a help message.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10911.md")
</aside>
<h2 id="telemetry">Telemetry</h2>
<p>Cloudflare collects anonymous usage data to improve <code>create-cloudflare</code> over time. Read more about this in our <a href="https://github.com/cloudflare/workers-sdk/blob/main/packages/create-cloudflare/telemetry.md">data policy</a>.</p>
<p>You can opt-out if you do not wish to share any information.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- telemetry disable</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- telemetry disable" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare telemetry disable</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare telemetry disable" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest telemetry disable</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest telemetry disable" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Alternatively, you can set an environment variable:</p>
<pre tabindex="0"><code class="language-sh">export CREATE_CLOUDFLARE_TELEMETRY_DISABLED=1&#10;</code></pre>
<p>You can check the status of telemetry collection at any time.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- telemetry status</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- telemetry status" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare telemetry status</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare telemetry status" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest telemetry status</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest telemetry status" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You can always re-enable telemetry collection.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- telemetry enable</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- telemetry enable" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare telemetry enable</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare telemetry enable" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest telemetry enable</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest telemetry enable" aria-label="Copy to clipboard">Copy</button></div></div>
