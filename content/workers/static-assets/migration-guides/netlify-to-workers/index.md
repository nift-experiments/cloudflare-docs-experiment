<p>In this tutorial, you will learn how to migrate your Netlify application to Cloudflare Workers.</p>
<p>You should already have an existing project deployed on Netlify that you would like to host on Cloudflare Workers. Netlify specific features are not supported by Cloudflare Workers. Review the <a href="/workers/static-assets/migration-guides/migrate-from-pages/#compatibility-matrix">Workers compatibility matrix</a> for more information on what is supported.</p>
<h2 id="frameworks">Frameworks</h2>
<p>Some frameworks like Next.js, Astro with on demand rendering, and others have specific guides for migrating to Cloudflare Workers. Refer to our <a href="/workers/framework-guides/">framework guides</a> for more information. If your framework has a <strong>Deploy an existing project on Workers</strong> guide, follow that guide for specific instructions. Otherwise, continue with the steps below.</p>
<h2 id="find-your-build-command-and-build-directory">Find your build command and build directory</h2>
<p>To move your application to Cloudflare Workers, you will need to know your build command and build directory. Cloudflare Workers will use this information to build and deploy your application. We will cover how to find these values in the Netlify Dashboard below.</p>
<p>In your Netlify Dashboard, find the project you want to migrate to Workers. Go to the <strong>Project configuration</strong> menu for your specific project, then go into the <strong>Build &amp; deploy</strong> menu item. You will find a <strong>Build settings</strong> card that includes the <strong>Build command</strong> and <strong>Publish directory</strong> fields. Save these for deploying to Cloudflare Workers. In the below image, the <strong>Build Command</strong> is <code>npm run build</code>, and the <strong>Output Directory</strong> is <code>.next</code>.</p>
<p><img src="/assets/upstream/images/workers/migrations/netlify-build-command.png" alt="Finding the Build Command and publish Directory fields" /></p>
<h2 id="create-a-wrangler-file">Create a wrangler file</h2>
<p>In the root of your project, create a <code>wrangler.jsonc</code> or <code>wrangler.toml</code> file (<code>wrangler.jsonc</code> is recommended). What goes in the file depends on what type of application you are deploying: an application powered by <a href="/workers/static-assets/routing/static-site-generation/">Static Site Generation (SSG)</a>, or a <a href="/workers/static-assets/routing/single-page-application/">Single Page Application (SPA)</a>.</p>
<p>For each case, be sure to update the <code>&lt;your-project-name&gt;</code> value with the name of your project and <code>&lt;your-build-directory&gt;</code> value with the build directory from Netlify.</p>
<p>For a <strong>static site</strong>, you will need to add the following to your wrangler file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17288.md")
</div>
<p>For a <strong>Single Page Application</strong>, you will need to add the following to your Wrangler configuration file, which includes the <code>not_found_handling</code> field.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17289.md")
</div>
<p>Some frameworks provide specific guides for migrating to Cloudflare Workers. Please refer to our <a href="/workers/framework-guides/">framework guides</a> for more information. If your framework includes a “Deploy an existing project on Workers” guide, follow it for detailed instructions.</p>
<h2 id="create-a-new-workers-project">Create a new Workers project</h2>
<p>Your application has the proper configuration to be built and deployed to Cloudflare Workers.</p>
<p>The <a href="/workers/ci-cd/builds/#connect-a-new-worker">Connect a new Worker</a> guide will instruct you how to connect your GitHub project to Cloudflare Workers. In the configuration step, ensure your build command is the same as the command you found on Netlify. Also, the deploy command should be the default <code>npx wrangler deploy</code>.</p>
<h2 id="add-a-custom-domain">Add a custom domain</h2>
<p>Workers Custom Domains only supports domains that are configured as zones on your account. A zone refers to a domain (such as example.com) that Cloudflare manages for you, including its DNS and traffic.</p>
<p>Follow these instructions for <a href="/workers/configuration/routing/custom-domains/#add-a-custom-domain">adding a custom domain to your Workers project</a>. You will also find additional information on creating a zone for your domain.</p>
<h2 id="delete-your-netlify-app">Delete your Netlify app</h2>
<p>Once your custom domain is set up and sending requests to Cloudflare Workers, you can safely delete your Netlify application.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For additional migration instructions, review the <a href="/workers/static-assets/migration-guides/migrate-from-pages/">Cloudflare Pages to Workers migration guide</a>. While not Netlify specific, it does cover some additional steps that may be helpful.</p>
