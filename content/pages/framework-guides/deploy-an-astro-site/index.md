---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/
  description: Deploy an Astro site to Cloudflare Pages.
  full_title: Astro · Cloudflare Pages docs
  head_html: <title>Astro · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy an Astro site to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/index.md"><meta property="og:title" content="Astro · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy an Astro site to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/#page","headline":"Astro \u00b7 Cloudflare Pages docs","description":"Deploy an Astro site to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-an-astro-site/
  schema: 1
---
<p><a href="https://astro.build">Astro</a> is an all-in-one web framework for building fast, content-focused websites. By default, Astro builds websites that have zero JavaScript runtime code.</p>
<p>Refer to the <a href="https://docs.astro.build/">Astro Docs</a> to learn more about Astro or for assistance with an Astro project.</p>
<p>In this guide, you will create a new Astro application and deploy it using Cloudflare Pages.</p>
<h3 id="video-tutorial">Video Tutorial</h3>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/c_IBs1crl4k" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="set-up-a-new-project">Set up a new project</h2>
<p>To use <code>create-cloudflare</code> to create a new Astro project, run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-astro-app --framework=astro --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-astro-app --framework=astro --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-astro-app --framework=astro --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-astro-app --framework=astro --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-astro-app --framework=astro --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-astro-app --framework=astro --platform=pages" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Astro will ask:</p>
<ol>
<li>
<p>Which project type you would like to set up. Your answers will not affect the rest of this tutorial. Select an answer ideal for your project.</p>
</li>
<li>
<p>If you want to initialize a Git repository. We recommend you to select <code>No</code> and follow this guide's <a href="/pages/framework-guides/deploy-an-astro-site/#create-a-github-repository">Git instructions</a> below. If you select <code>Yes</code>, do not follow the below Git instructions precisely but adjust them to your needs.</p>
</li>
</ol>
<p><code>create-cloudflare</code> will then install dependencies, including the <a href="/workers/wrangler/install-and-update/#check-your-wrangler-version">Wrangler</a> CLI and the <code>@astrojs/cloudflare</code> adapter, and ask you setup questions.</p>
<h3 id="astro-configuration">Astro configuration</h3>
<p>You can deploy an Astro Server-side Rendered (SSR) site to Cloudflare Pages using the <a href="https://github.com/withastro/adapters/tree/main/packages/cloudflare#readme"><code>@astrojs/cloudflare</code> adapter</a>. SSR sites render on Pages Functions and allow for dynamic functionality and customizations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11014.md")
</aside>
<p>Add the <a href="https://github.com/withastro/adapters/tree/main/packages/cloudflare#readme"><code>@astrojs/cloudflare</code> adapter</a> to your project's <code>package.json</code> by running:</p>
<pre tabindex="0"><code class="language-sh">npm run astro add cloudflare&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre tabindex="0"><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<h3 id="deploy-via-the-create-cloudflare-cli-c3">Deploy via the <code>create-cloudflare</code> CLI (C3)</h3>
<p>If you use <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code>(C3)</a> to create your new Astro project, C3 will install all dependencies needed for your project and prompt you to deploy your project via the CLI. If you deploy, your site will be live and you will be provided with a deployment URL.</p>
<h3 id="deploy-via-the-cloudflare-dashboard">Deploy via the Cloudflare dashboard</h3>
<p>To deploy your site to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application**.
3. Select the **Pages** tab.
4. Select **Import an existing Git repository**.
5. Select the new GitHub repository that you created and then select **Begin setup**.
6. In the **Set up builds and deployments** section, provide the following information:
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npm run build</code></td></tr><tr><td>Build directory</td><td><code>dist</code></td></tr></tbody></table>
<p>Optionally, you can customize the <strong>Project name</strong> field. It defaults to the GitHub repository's name, but it does not need to match. The <strong>Project name</strong> value is assigned as your <code>*.pages.dev</code> subdomain.</p>
<p>After completing configuration, select <strong>Save and Deploy</strong>.</p>
<p>You will see your first deployment in progress. Pages installs all dependencies and builds the project as specified.</p>
<p>Cloudflare Pages will automatically rebuild your project and deploy it on every new pushed commit.</p>
<p>Additionally, you will have access to <a href="/pages/configuration/preview-deployments/">preview deployments</a>, which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying them to production.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11013.md")
</aside>
<h3 id="local-runtime">Local runtime</h3>
<p>Local runtime support is configured via the <code>platformProxy</code> option:</p>
<pre tabindex="0"><code class="language-js">import { defineConfig } from &quot;astro/config&quot;;&#10;import cloudflare from &quot;@astrojs/cloudflare&quot;;&#10;&#10;export default defineConfig({&#10;	adapter: cloudflare({&#10;		platformProxy: {&#10;			enabled: true,&#10;		},&#10;	}),&#10;});&#10;</code></pre>
<h2 id="use-bindings-in-your-astro-application">Use bindings in your Astro application</h2>
<p>A <a href="/pages/functions/bindings/">binding</a> allows your application to interact with Cloudflare developer products, such as <a href="/kv/concepts/how-kv-works/">KV</a>, <a href="/durable-objects/">Durable Object</a>, <a href="/r2/">R2</a>, and <a href="https://blog.cloudflare.com/introducing-d1/">D1</a>.</p>
<p>Use bindings in Astro components and API routes by using <code>context.locals</code> from <a href="https://docs.astro.build/en/guides/middleware/">Astro Middleware</a> to access the Cloudflare runtime which amongst other fields contains the Cloudflare's environment and consecutively any bindings set for your application.</p>
<p>Refer to the following example of how to access a KV namespace with TypeScript.</p>
<p>First, you need to define Cloudflare runtime and KV type by updating the <code>env.d.ts</code>. Make sure you have generated Cloudflare runtime types by running <a href="/pages/functions/typescript/"><code>wrangler types</code></a>.</p>
<pre tabindex="0"><code class="language-typescript">/// &lt;reference types=&quot;astro/client&quot; /&gt;&#10;&#10;type ENV = {&#10;	// replace `MY_KV` with your KV namespace&#10;	MY_KV: KVNamespace;&#10;};&#10;&#10;// use a default runtime configuration (advanced mode).&#10;type Runtime = import(&quot;@astrojs/cloudflare&quot;).Runtime&lt;ENV&gt;;&#10;declare namespace App {&#10;	interface Locals extends Runtime {}&#10;}&#10;</code></pre>
<p>You can then access your KV from an API endpoint in the following way:</p>
<pre tabindex="0"><code class="language-typescript">import type { APIContext } from &quot;astro&quot;;&#10;&#10;export async function get({ locals }: APIContext) {&#10;	const { MY_KV } = locals.runtime.env;&#10;&#10;	return {&#10;		// ...&#10;	};&#10;}&#10;</code></pre>
<p>Besides endpoints, you can also use bindings directly from your Astro components:</p>
<pre tabindex="0"><code class="language-typescript">&#45;--&#10;const myKV = Astro.locals.runtime.env.MY_KV;&#10;const value = await myKV.get(&quot;key&quot;);&#10;&#45;--&#10;&lt;div&gt;{value}&lt;/div&gt;&#10;</code></pre>
<p>To learn more about the Astro Cloudflare runtime, refer to the <a href="https://docs.astro.build/en/guides/integrations-guide/cloudflare/#access-to-the-cloudflare-runtime">Access to the Cloudflare runtime</a> in the Astro documentation.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Astro site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
