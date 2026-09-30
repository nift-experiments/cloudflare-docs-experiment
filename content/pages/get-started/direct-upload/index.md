---
cp9:
  canonical: https://developers.cloudflare.com/pages/get-started/direct-upload/
  description: Upload your prebuilt assets to Pages and deploy them via the Wrangler CLI or the Cloudflare dashboard.
  full_title: Direct Upload · Cloudflare Pages docs
  head_html: <title>Direct Upload · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload your prebuilt assets to Pages and deploy them via the Wrangler CLI or the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/pages/get-started/direct-upload/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/get-started/direct-upload/index.md"><meta property="og:title" content="Direct Upload · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload your prebuilt assets to Pages and deploy them via the Wrangler CLI or the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/pages/get-started/direct-upload/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/get-started/direct-upload/#page","headline":"Direct Upload \u00b7 Cloudflare Pages docs","description":"Upload your prebuilt assets to Pages and deploy them via the Wrangler CLI or the Cloudflare dashboard.","url":"https://developers.cloudflare.com/pages/get-started/direct-upload/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/get-started/direct-upload/
  schema: 1
---
<p>Direct Upload enables you to upload your prebuilt assets to Pages and deploy them to the Cloudflare global network. You should choose Direct Upload over Git integration if you want to <a href="/pages/how-to/use-direct-upload-with-continuous-integration/">integrate your own build platform</a> or upload from your local computer.</p>
<p>This guide will instruct you how to upload your assets using Wrangler or the drag and drop method.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="you-cannot-switch-to-git-integration-later">You cannot switch to Git integration later</h3>
@markup("md", "content/.markup/bodies/10910.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you deploy your project with Direct Upload, run the appropriate <a href="/pages/configuration/build-configuration/#framework-presets">build command</a> to build your project.</p>
<h2 id="upload-methods">Upload methods</h2>
<p>After you have your prebuilt assets ready, there are two ways to begin uploading:</p>
<ul>
<li><a href="/pages/get-started/direct-upload/#wrangler-cli">Wrangler</a>.</li>
<li><a href="/pages/get-started/direct-upload/#drag-and-drop">Drag and drop</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10909.md")
</aside>
<h2 id="supported-file-types">Supported file types</h2>
<p>Below is the supported file types for each Direct Upload options:</p>
<ul>
<li>Wrangler: A single folder of assets. (Zip files are not supported.)</li>
<li>Drag and drop: A zip file or single folder of assets.</li>
</ul>
<h2 id="wrangler-cli">Wrangler CLI</h2>
<h3 id="set-up-wrangler">Set up Wrangler</h3>
<p>To begin, install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>. Then <a href="/workers/wrangler/install-and-update/">install Wrangler, the Developer Platform CLI</a>.</p>
<h4 id="create-your-project">Create your project</h4>
<p>Log in to Wrangler with the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code> command</a>. Then run the <a href="/workers/wrangler/commands/pages/#pages-project-create"><code>pages project create</code> command</a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages project create&#10;</code></pre>
<p>You will then be prompted to specify the project name. Your project will be served at <code>&lt;PROJECT_NAME&gt;.pages.dev</code> (or your project name plus a few random characters if your project name is already taken). You will also be prompted to specify your production branch.</p>
<p>Subsequent deployments will reuse both of these values (saved in your <code>node_modules/.cache/wrangler</code> folder).</p>
<h4 id="deploy-your-assets">Deploy your assets</h4>
<p>From here, you have created an empty project and can now deploy your assets for your first deployment and for all subsequent deployments in your production environment. To do this, run the <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a> command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages deploy &lt;BUILD_OUTPUT_DIRECTORY&gt;&#10;</code></pre>
<p>Find the appropriate build output directory for your project in <a href="/pages/configuration/build-configuration/#framework-presets">Build directory under Framework presets</a>.</p>
<p>Your production deployment will be available at <code>&lt;PROJECT_NAME&gt;.pages.dev</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10908.md")
</aside>
<p>To deploy assets to a preview environment, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages deploy &lt;OUTPUT_DIRECTORY&gt; --branch=&lt;BRANCH_NAME&gt;&#10;</code></pre>
<p>For every branch you create, a branch alias will be available to you at <code>&lt;BRANCH_NAME&gt;.&lt;PROJECT_NAME&gt;.pages.dev</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10907.md")
</aside>
<p>If you would like to streamline the project creation and asset deployment steps, you can also use the deploy command to both create and deploy assets at the same time. If you execute this command first, you will still be prompted to specify your project name and production branch. These values will still be cached for subsequent deployments as stated above. If the cache already exists and you would like to create a new project, you will need to run the <a href="#create-your-project"><code>create</code> command</a>.</p>
<h4 id="other-useful-commands">Other useful commands</h4>
<p>If you would like to use Wrangler to obtain a list of all available projects for Direct Upload, use <a href="/workers/wrangler/commands/pages/#pages-project-list"><code>pages project list</code></a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages project list&#10;</code></pre>
<p>To get the output as JSON for programmatic use or scripting, use the <code>--json</code> flag:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages project list --json&#10;</code></pre>
<p>If you would like to use Wrangler to obtain a list of all unique preview URLs for a particular project, use <a href="/workers/wrangler/commands/pages/#pages-deployment-list"><code>pages deployment list</code></a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages deployment list&#10;</code></pre>
<p>For step-by-step directions on how to use Wrangler and continuous integration tools like GitHub Actions, Circle CI, and Travis CI together for continuous deployment, refer to <a href="/pages/how-to/use-direct-upload-with-continuous-integration/">Use Direct Upload with continuous integration</a>.</p>
<h2 id="drag-and-drop">Drag and drop</h2>
<h4 id="deploy-your-project-with-drag-and-drop">Deploy your project with drag and drop</h4>
<p>To deploy with drag and drop:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application** > **Get started** > **Drag and drop your files**.
3. Enter your project name in the provided field and drag and drop your assets.
4. Select **Deploy site**.
<p>Your project will be served from <code>&lt;PROJECT_NAME&gt;.pages.dev</code>. Next drag and drop your build output directory into the uploading frame. Once your files have been successfully uploaded, select <strong>Save and Deploy</strong> and continue to your newly deployed project.</p>
<h4 id="create-a-new-deployment">Create a new deployment</h4>
<p>After you have your project created, select <strong>Create a new deployment</strong> to begin a new version of your site. Next, choose whether your new deployment will be made to your production or preview environment. If choosing preview, you can create a new deployment branch or enter an existing one.</p>
<h2 id="troubleshoot">Troubleshoot</h2>
<h3 id="limits">Limits</h3>
<table>
<thead>
<tr>
<th>Upload method</th>
<th>File limit</th>
<th>File size</th>
</tr>
</thead>
<tbody>
<tr>
<td>Wrangler</td>
<td>20,000 files</td>
<td>25 MiB</td>
</tr>
<tr>
<td>Drag and drop</td>
<td>1,000 files</td>
<td>25 MiB</td>
</tr>
</tbody>
</table>
<p>If using the drag and drop method, a red warning symbol will appear next to an asset if too large and thus unsuccessfully uploaded. In this case, you may choose to delete that asset but you cannot replace it. In order to do so, you must reupload the entire project.</p>
<h3 id="production-branch-configuration">Production branch configuration</h3>
<p>If your project is a <a href="/pages/get-started/direct-upload/">Direct Upload</a> project, you will not have the option to configure production branch controls. To update your production branch, you will need to manually call the <a href="/api/resources/pages/subresources/projects/methods/edit/">Update Project</a> endpoint in the API.</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH \&#10;&quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &quot;{\&quot;production_branch\&quot;: \&quot;main\&quot;}&quot;&#10;</code></pre>
<h3 id="functions">Functions</h3>
<p>Drag and drop deployments made from the Cloudflare dashboard do not currently support compiling a <code>functions</code> folder of <a href="/pages/functions/">Pages Functions</a>. To deploy a <code>functions</code> folder, you must use Wrangler. When deploying a project using Wrangler, if a <code>functions</code> folder exists where the command is run, that <code>functions</code> folder will be uploaded with the project.</p>
<p>However, note that a <code>_worker.js</code> file is supported by both Wrangler and drag and drop deployments made from the dashboard.</p>
