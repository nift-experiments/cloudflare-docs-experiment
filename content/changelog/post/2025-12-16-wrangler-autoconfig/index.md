<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 16, 2025</time><h2 id="post-title">Configure your framework for Cloudflare automatically</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports automatic configuration for popular web frameworks in experimental mode, making it even easier to deploy to Cloudflare Workers.</p>
<p>Previously, if you wanted to deploy an application using a popular web framework like Next.js or Astro, you had to follow tutorials to set up your application for deployment to Cloudflare Workers. This usually involved creating a Wrangler file, installing adapters, or changing configuration options.</p>
<p>Now <code>wrangler deploy</code> does this for you. Starting with Wrangler 4.55, you can use <code>npx wrangler deploy --x-autoconfig</code> in the directory of any web application using one of the supported frameworks. Wrangler will then proceed to configure and deploy it to your Cloudflare account.</p>
<p>You can also configure your application without deploying it by using the new <code>npx wrangler setup</code> command. This enables you to easily review what changes we are making so your application is ready for Cloudflare Workers.</p>
<p>The following application frameworks are supported starting today:</p>
<ul>
<li>Next.js</li>
<li>Astro</li>
<li>Nuxt</li>
<li>TanStack Start</li>
<li>SolidStart</li>
<li>React Router</li>
<li>SvelteKit</li>
<li>Docusaurus</li>
<li>Qwik</li>
<li>Analog</li>
</ul>
<p>Automatic configuration also supports static sites by detecting the assets directory and build command. From a single index.html file to the output of a generator like Jekyll or Hugo, you can just run <code>npx wrangler deploy --x-autoconfig</code> to upload to Cloudflare.</p>
<p>We're really excited to bring you automatic configuration so you can do more with Workers. Please let us know if you run into challenges using this experimentally. We’ve opened a <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a> and would love to hear your feedback.</p>
</div></article></div>
