---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/
  description: Install Wrangler v2 and update your Workers project configuration, including wrangler.toml changes.
  full_title: 2. Update to Wrangler v2 · Cloudflare Workers docs
  head_html: <title>2. Update to Wrangler v2 · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Install Wrangler v2 and update your Workers project configuration, including wrangler.toml changes."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/index.md"><meta property="og:title" content="2. Update to Wrangler v2 · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install Wrangler v2 and update your Workers project configuration, including wrangler.toml changes."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/#page","headline":"2. Update to Wrangler v2 \u00b7 Cloudflare Workers docs","description":"Install Wrangler v2 and update your Workers project configuration, including wrangler.toml changes.","url":"https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/update-v1-to-v2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/migration/v1-to-v2/update-v1-to-v2/
  schema: 1
---
<p>This document describes the steps to migrate a project from Wrangler v1 to Wrangler v2. Before updating your Wrangler version, review and complete <a href="/workers/wrangler/migration/v1-to-v2/eject-webpack/">Migrate webpack projects from Wrangler version 1</a> if it applies to your project.</p>
<p>Wrangler v2 ships with new features and improvements that may require some changes to your configuration.</p>
<p>The CLI itself will guide you through the upgrade process.</p>
<div style="position: relative; padding-top: 56.25%;">
<iframe title="Embedded media" src="https://iframe.videodelivery.net/2a60561afea1159f7dd270fd9dce999f?poster=https%3A%2F%2Fcloudflarestream.com%2F2a60561afea1159f7dd270fd9dce999f%2Fthumbnails%2Fthumbnail.jpg%3Ftime%3D%26height%3D600" style="border: none; position: absolute; top: 0; left: 0; height: 100%; width: 100%;" allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;" allowfullscreen="true"></iframe>
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17448.md")
</aside>
<h2 id="update-wrangler-version">Update Wrangler version</h2>
<h3 id="1-uninstall-wrangler-v1"><ol>
<li>Uninstall Wrangler v1</li>
</ol></h3>
<p>If you had previously installed Wrangler v1 globally using npm, you can uninstall it with:</p>
<pre tabindex="0"><code class="language-sh">npm uninstall -g @cloudflare/wrangler&#10;</code></pre>
<p>If you used Cargo to install Wrangler v1, you can uninstall it with:</p>
<pre tabindex="0"><code class="language-sh">cargo uninstall wrangler&#10;</code></pre>
<h3 id="2-install-wrangler"><ol start="2">
<li>Install Wrangler</li>
</ol></h3>
<p>Now, install the latest version of Wrangler.</p>
<pre tabindex="0"><code class="language-sh">npm install -g wrangler&#10;</code></pre>
<h3 id="3-verify-your-install"><ol start="3">
<li>Verify your install</li>
</ol></h3>
<p>To check that you have installed the correct Wrangler version, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler --version&#10;</code></pre>
<h2 id="test-wrangler-v2-on-your-previous-projects">Test Wrangler v2 on your previous projects</h2>
<p>Now you will test that Wrangler v2 can build your Wrangler v1 project. In most cases, it will build just fine. If there are errors, the command line should instruct you with exactly what to change to get it to build.</p>
<p>If you would like to read more on the deprecated <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> fields that cause Wrangler v2 to error, refer to <a href="/workers/wrangler/deprecations/">Deprecations</a>.</p>
<p>Run the <code>wrangler dev</code> command. This will show any warnings or errors that should be addressed.
Note that in most cases, the messages will include actionable instructions on how to resolve the issue.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<ul>
<li>Errors need to be fixed before Wrangler can build your Worker.</li>
<li>In most cases, you will only see warnings.
These do not stop Wrangler from building your Worker, but consider updating the configuration to remove them.</li>
</ul>
<p>Here is an example of some warnings and errors:</p>
<pre tabindex="0"><code class="language-bash"> ⛅️ wrangler 2.x&#10;&#45;------------------------------------------------------&#10;▲ [WARNING] Processing wrangler.toml configuration:&#10;  &#45; 😶 Ignored: &quot;type&quot;:&#10;    Most common features now work out of the box with wrangler, including modules, jsx,&#10;  typescript, etc. If you need anything more, use a custom build.&#10;  &#45; Deprecation: &quot;zone_id&quot;:&#10;    This is unnecessary since we can deduce this from routes directly.&#10;  &#45; Deprecation: &quot;build.upload.format&quot;:&#10;    The format is inferred automatically from the code.&#10;&#10;&#10;✘ [ERROR] Processing wrangler.toml configuration:&#10;  &#45; Expected &quot;route&quot; to be either a string, or an object with shape { pattern, zone_id | zone_name }, but got &quot;&quot;.&#10;</code></pre>
<h2 id="deprecations">Deprecations</h2>
<p>Refer to <a href="/workers/wrangler/deprecations/">Deprecations</a> for more details on what is no longer supported.</p>
