---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/builds/build-image/
  description: Understand the build image used in Workers Builds.
  full_title: Build image · Cloudflare Workers docs
  head_html: <title>Build image · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand the build image used in Workers Builds."><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/builds/build-image/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/builds/build-image/index.md"><meta property="og:title" content="Build image · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the build image used in Workers Builds."><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/builds/build-image/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#page","headline":"Build image \u00b7 Cloudflare Workers docs","description":"Understand the build image used in Workers Builds.","url":"https://developers.cloudflare.com/workers/ci-cd/builds/build-image/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/builds/build-image/
  schema: 1
---
<p>Workers Builds uses a build image with support for a variety of languages and tools such as Node.js, Python, PHP, Ruby, and Go.</p>
<h2 id="supported-tooling">Supported Tooling</h2>
<p>Workers Builds supports a variety of runtimes, languages, and tools. Builds will use the default versions listed below unless a custom version is detected or specified. You can <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">override the default versions</a> using environment variables or version files. All versions are available for override.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="default-version-updates">Default version updates</h3>
@markup("md", "content/.markup/bodies/16780.md")
</aside>
<h3 id="runtime">Runtime</h3>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Default version</th>
<th>Environment variable</th>
<th>File</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Go</strong></td>
<td>1.24.3</td>
<td><code>GO_VERSION</code></td>
<td></td>
</tr>
<tr>
<td><strong>Node.js</strong></td>
<td>24.18.0</td>
<td><code>NODE_VERSION</code></td>
<td>.nvmrc, .node-version</td>
</tr>
<tr>
<td><strong>Python</strong></td>
<td>3.13.3</td>
<td><code>PYTHON_VERSION</code></td>
<td>.python-version, runtime.txt</td>
</tr>
<tr>
<td><strong>Ruby</strong></td>
<td>3.4.4</td>
<td><code>RUBY_VERSION</code></td>
<td>.ruby-version</td>
</tr>
</tbody>
</table>
<p>The build image preinstalls Node.js 22.23.2 and 24.18.0.</p>
<h3 id="tools-and-languages">Tools and languages</h3>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Default version</th>
<th>Environment variable</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bun</strong></td>
<td>1.2.15</td>
<td><code>BUN_VERSION</code></td>
</tr>
<tr>
<td><strong>Hugo</strong></td>
<td>extended_0.147.7</td>
<td><code>HUGO_VERSION</code></td>
</tr>
<tr>
<td><strong>npm</strong></td>
<td>10.9.2</td>
<td></td>
</tr>
<tr>
<td><strong>yarn</strong></td>
<td>4.9.1</td>
<td><code>YARN_VERSION</code></td>
</tr>
<tr>
<td><strong>pnpm</strong></td>
<td>10.11.1</td>
<td><code>PNPM_VERSION</code></td>
</tr>
<tr>
<td><strong>pip</strong></td>
<td>25.1.1</td>
<td></td>
</tr>
<tr>
<td><strong>gem</strong></td>
<td>3.6.9</td>
<td></td>
</tr>
<tr>
<td><strong>poetry</strong></td>
<td>2.1.3</td>
<td></td>
</tr>
<tr>
<td><strong>pipx</strong></td>
<td>1.7.1</td>
<td></td>
</tr>
<tr>
<td><strong>bundler</strong></td>
<td>2.6.9</td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="advanced-settings">Advanced Settings</h2>
<h3 id="overriding-default-versions">Overriding Default Versions</h3>
<p>If you need to override a <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">specific version</a> of a language or tool within the image, you can specify it as a <a href="/workers/ci-cd/builds/configuration/#build-settings">build environment variable</a>, or set the relevant file in your source code as shown above.</p>
<p>To set the version using a build environment variables, you can:</p>
<ol>
<li>Find the environment variable name for the language or tool and desired version (e.g. <code>NODE_VERSION = 22</code>)</li>
<li>Add and save the environment variable on the dashboard by going to <strong>Settings</strong> &gt; <strong>Build</strong> &gt; <strong>Build Variables and Secrets</strong> in your Workers project</li>
</ol>
<p>Or, to set the version by adding a file to your project, you can:</p>
<ol>
<li>Find the filename for the language or tool (e.g. <code>.nvmrc</code>)</li>
<li>Add the specified file name to the root directory and set the desired version number as the file's content. For example, if the version number is 22, the file should contain '22'.</li>
</ol>
<h3 id="skip-dependency-install">Skip dependency install</h3>
<p>You can add the following build variable to disable automatic dependency installation and run a custom install command instead.</p>
<table>
<thead>
<tr>
<th>Build variable</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SKIP_DEPENDENCY_INSTALL</code></td>
<td><code>1</code> or <code>true</code></td>
</tr>
</tbody>
</table>
<h2 id="pre-installed-packages">Pre-installed Packages</h2>
<p>In the following table, review the pre-installed packages in the build image. The packages are installed with <code>apt</code>, a package manager for Linux distributions.</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>curl</code></td>
<td><code>libbz2-dev</code></td>
<td><code>libreadline-dev</code></td>
</tr>
<tr>
<td><code>git</code></td>
<td><code>libc++1</code></td>
<td><code>libssl-dev</code></td>
</tr>
<tr>
<td><code>git-lfs</code></td>
<td><code>libdb-dev</code></td>
<td><code>libvips-dev</code></td>
</tr>
<tr>
<td><code>unzip</code></td>
<td><code>libgdbm-dev</code></td>
<td><code>libyaml-dev</code></td>
</tr>
<tr>
<td><code>autoconf</code></td>
<td><code>libgdbm6</code></td>
<td><code>tzdata</code></td>
</tr>
<tr>
<td><code>build-essential</code></td>
<td><code>libgbm1</code></td>
<td><code>wget</code></td>
</tr>
<tr>
<td><code>bzip2</code></td>
<td><code>libgmp-dev</code></td>
<td><code>zlib1g-dev</code></td>
</tr>
<tr>
<td><code>gnupg</code></td>
<td><code>liblzma-dev</code></td>
<td><code>zstd</code></td>
</tr>
<tr>
<td><code>libffi-dev</code></td>
<td><code>libncurses5-dev</code></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="build-environment">Build Environment</h2>
<p>Workers Builds are run in the following environment:</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Build Environment</strong></td>
<td>Ubuntu 24.04</td>
</tr>
<tr>
<td><strong>Architecture</strong></td>
<td>x86_64</td>
</tr>
</tbody>
</table>
<h2 id="build-image-policy">Build Image Policy</h2>
<h3 id="preinstalled-software-updates">Preinstalled Software Updates</h3>
<p>Preinstalled software (languages and tools) will be updated before reaching end-of-life (EOL). These updates apply only if you have not <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">overridden the default version</a>.</p>
<ul>
<li><strong>Minor version updates</strong>: May be updated to the latest available minor version without notice. For tools that do not follow semantic versioning (e.g., Bun or Hugo), updates that may contain breaking changes will receive 3 months’ notice.</li>
<li><strong>Major version updates</strong>: Updated to the next stable long-term support (LTS) version with 3 months’ notice.</li>
</ul>
<p><strong>How you'll be notified (for changes requiring notice):</strong></p>
<ul>
<li><a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a></li>
<li>Dashboard notifications for projects that will receive the update</li>
<li>Email notifications to project owners</li>
</ul>
<p>To maintain a specific version and avoid automatic updates, <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">override the default version</a>.</p>
<h3 id="best-practices">Best Practices</h3>
<p>To avoid unexpected build failures:</p>
<ul>
<li><strong>Monitor announcements</strong> via the <a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a>, dashboard notifications, and email</li>
<li><strong>Pin specific versions</strong> of critical preinstalled software by <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">overriding default versions</a></li>
</ul>
