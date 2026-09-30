<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 9, 2025</time><h2 id="post-title">Select Wrangler environments using the CLOUDFLARE_ENV environment variable</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports using the <code>CLOUDFLARE_ENV</code> <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables">environment variable</a> to select the active <a href="/workers/wrangler/environments/">environment</a> for your Worker commands. This provides a more flexible way to manage environments, especially when working with build tools and CI/CD pipelines.</p>
<h4 id="what-s-new">What's new</h4>
<p><strong>Environment selection via environment variable:</strong></p>
<ul>
<li>Set <code>CLOUDFLARE_ENV</code> to specify which environment to use for Wrangler commands</li>
<li>Works with all Wrangler commands that support the <code>--env</code> flag</li>
<li>The <code>--env</code> command line argument takes precedence over the <code>CLOUDFLARE_ENV</code> environment variable</li>
</ul>
<h4 id="example-usage">Example usage</h4>
<pre><code class="language-bash">&#35; Deploy to the production environment using CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=production wrangler deploy&#10;&#10;&#35; Upload a version to the staging environment&#10;CLOUDFLARE_ENV=staging wrangler versions upload&#10;&#10;&#35; The --env flag takes precedence over CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=dev wrangler deploy --env production&#10;&#35; This will deploy to production, not dev&#10;</code></pre>
<h4 id="use-with-build-tools">Use with build tools</h4>
<p>The <code>CLOUDFLARE_ENV</code> environment variable is particularly useful when working with build tools like Vite. You can set the environment once during the build process, and it will be used for both building and deploying your Worker:</p>
<pre><code class="language-bash">&#35; Set the environment for both build and deploy&#10;CLOUDFLARE_ENV=production npm run build &amp; wrangler deploy&#10;</code></pre>
<p>When using <code>@cloudflare/vite-plugin</code>, the build process generates a <a href="/workers/wrangler/configuration/#generated-wrangler-configuration">&quot;redirected deploy config&quot;</a> that is flattened to only contain the active environment. Wrangler will validate that the environment specified matches the environment used during the build to prevent accidentally deploying a Worker built for one environment to a different environment.</p>
<h4 id="learn-more">Learn more</h4>
<ul>
<li><a href="/workers/wrangler/system-environment-variables/">System environment variables</a></li>
<li><a href="/workers/wrangler/environments/">Environments</a></li>
</ul>
</div></article></div>
