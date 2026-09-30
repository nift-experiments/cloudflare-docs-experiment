---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/configuration/dockerfile/
  description: Customize the Sandbox SDK container image with packages, tools, and configurations.
  full_title: Dockerfile reference · Cloudflare Sandbox SDK docs
  head_html: <title>Dockerfile reference · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize the Sandbox SDK container image with packages, tools, and configurations."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/configuration/dockerfile/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/configuration/dockerfile/index.md"><meta property="og:title" content="Dockerfile reference · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize the Sandbox SDK container image with packages, tools, and configurations."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/configuration/dockerfile/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/configuration/dockerfile/#page","headline":"Dockerfile reference \u00b7 Cloudflare Sandbox SDK docs","description":"Customize the Sandbox SDK container image with packages, tools, and configurations.","url":"https://developers.cloudflare.com/sandbox/configuration/dockerfile/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/configuration/dockerfile/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13566.md")
</aside>
<p>Customize the sandbox container image with your own packages, tools, and configurations by extending the base runtime image.</p>
<h2 id="base-images">Base images</h2>
<p>The Sandbox SDK provides multiple Ubuntu-based image variants. Choose the one that fits your use case:</p>
<table>
<thead>
<tr>
<th>Image</th>
<th>Tag suffix</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td>Default</td>
<td>(none)</td>
<td>Lean image for JavaScript/TypeScript workloads</td>
</tr>
<tr>
<td>Python</td>
<td><code>-python</code></td>
<td>Data science, ML, Python code execution</td>
</tr>
<tr>
<td>OpenCode</td>
<td><code>-opencode</code></td>
<td>AI coding agents with OpenCode CLI</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-dockerfile">&#35; Default - lean, no Python&#10;FROM docker.io/cloudflare/sandbox:0.7.0&#10;&#10;&#35; Python - includes Python 3.11 + data science packages&#10;FROM docker.io/cloudflare/sandbox:0.7.0-python&#10;&#10;&#35; OpenCode - includes OpenCode CLI for AI coding&#10;FROM docker.io/cloudflare/sandbox:0.7.0-opencode&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="version-synchronization-required">Version synchronization required</h3>
@markup("md", "content/.markup/bodies/13565.md")
</aside>
<h3 id="default-image">Default image</h3>
<p>The default image is optimized for JavaScript and TypeScript workloads:</p>
<ul>
<li>Ubuntu 22.04 LTS base</li>
<li>Node.js 20 LTS with npm</li>
<li>Bun 1.x (JavaScript/TypeScript runtime)</li>
<li>System utilities: curl, wget, git, jq, zip, unzip, file, procps, ca-certificates</li>
</ul>
<h3 id="python-image">Python image</h3>
<p>The <code>-python</code> variant includes everything in the default image plus:</p>
<ul>
<li>Python 3.11 with pip and venv</li>
<li>Pre-installed packages: matplotlib, numpy, pandas, ipython</li>
</ul>
<h3 id="opencode-image">OpenCode image</h3>
<p>The <code>-opencode</code> variant includes everything in the default image plus:</p>
<ul>
<li><a href="https://opencode.ai">OpenCode CLI</a> for AI-powered coding agents</li>
</ul>
<h2 id="creating-a-custom-image">Creating a custom image</h2>
<p>Create a <code>Dockerfile</code> in your project root:</p>
<pre tabindex="0"><code class="language-dockerfile">FROM docker.io/cloudflare/sandbox:0.7.0-python&#10;&#10;&#35; Install additional Python packages&#10;RUN pip install --no-cache-dir \&#10;    scikit-learn==1.3.0 \&#10;    tensorflow==2.13.0 \&#10;    transformers==4.30.0&#10;&#10;&#35; Install Node.js packages globally&#10;RUN npm install -g typescript ts-node prettier&#10;&#10;&#35; Install system packages&#10;RUN apt-get update &amp;&amp; apt-get install -y \&#10;    postgresql-client \&#10;    redis-tools \&#10;    &amp;&amp; rm -rf /var/lib/apt/lists/*&#10;</code></pre>
<p>Update <code>wrangler.jsonc</code> to reference your Dockerfile:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;containers&quot;: [&#10;		{&#10;			&quot;class_name&quot;: &quot;Sandbox&quot;,&#10;			&quot;image&quot;: &quot;./Dockerfile&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>When you run <code>wrangler dev</code> or <code>wrangler deploy</code>, Wrangler automatically builds your Docker image and pushes it to Cloudflare's container registry. You don't need to manually build or publish images.</p>
<h2 id="using-arbitrary-base-images">Using arbitrary base images</h2>
<p>You can add sandbox capabilities to any Docker image using the standalone binary. This approach lets you use your existing images without depending on the Cloudflare base images:</p>
<pre tabindex="0"><code class="language-dockerfile">FROM your-custom-image:tag&#10;&#10;&#35; Copy the sandbox binary from the official image&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.0 /container-server/sandbox /sandbox&#10;&#10;ENTRYPOINT [&quot;/sandbox&quot;]&#10;</code></pre>
<p>The <code>/sandbox</code> binary starts the HTTP API server that enables SDK communication. You can optionally run your own startup command:</p>
<pre tabindex="0"><code class="language-dockerfile">FROM node:20-slim&#10;&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.0 /container-server/sandbox /sandbox&#10;&#10;&#35; Copy your application&#10;COPY . /app&#10;WORKDIR /app&#10;&#10;ENTRYPOINT [&quot;/sandbox&quot;]&#10;CMD [&quot;node&quot;, &quot;server.js&quot;]&#10;</code></pre>
<p>When using <code>CMD</code>, the sandbox binary runs your command as a child process with proper signal forwarding.</p>
<h2 id="custom-startup-scripts">Custom startup scripts</h2>
<p>For more complex startup sequences, create a custom startup script:</p>
<pre tabindex="0"><code class="language-dockerfile">FROM docker.io/cloudflare/sandbox:0.7.0-python&#10;&#10;COPY my-app.js /workspace/my-app.js&#10;COPY startup.sh /workspace/startup.sh&#10;RUN chmod +x /workspace/startup.sh&#10;&#10;CMD [&quot;/workspace/startup.sh&quot;]&#10;</code></pre>
<p>The base image already sets the correct <code>ENTRYPOINT</code>, so you only need to provide a <code>CMD</code>. The sandbox binary starts the HTTP API server, then spawns your <code>CMD</code> as a child process with proper signal forwarding.</p>
<pre tabindex="0"><code class="language-bash">&#35;!/bin/bash&#10;&#10;&#35; Start your services in the background&#10;node /workspace/my-app.js &amp;&#10;&#10;&#35; Start additional services&#10;redis-server --daemonize yes&#10;until redis-cli ping; do sleep 1; done&#10;&#10;&#35; Keep the script running (the sandbox binary handles the API server)&#10;wait&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="legacy-startup-scripts">Legacy startup scripts</h3>
@markup("md", "content/.markup/bodies/13564.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/containers/guides/image-management/">Image Management</a> - Building and pushing images to Cloudflare's registry</li>
<li><a href="/sandbox/configuration/wrangler/">Wrangler configuration</a> - Using custom images in wrangler.jsonc</li>
<li><a href="https://docs.docker.com/reference/dockerfile/">Docker documentation</a> - Complete Dockerfile syntax</li>
<li><a href="/sandbox/concepts/containers/">Container concepts</a> - Understanding the runtime environment</li>
</ul>
