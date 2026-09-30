---
cp9:
  canonical: https://developers.cloudflare.com/pulumi/tutorial/manage-secrets/
  description: Pulumi ESC (Environments, Secrets, and Configuration) is a secure and robust secrets management solution. The tutorial will walk you through how to develop with Wrangler while following security best practices.
  full_title: Manage secrets with Pulumi ESC · Pulumi docs
  head_html: <title>Manage secrets with Pulumi ESC · Pulumi docs</title><meta name="generator" content="Nift"><meta name="description" content="Pulumi ESC (Environments, Secrets, and Configuration) is a secure and robust secrets management solution. The tutorial will walk you through how to develop with Wrangler while following security best practices."><link rel="canonical" href="https://developers.cloudflare.com/pulumi/tutorial/manage-secrets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pulumi/tutorial/manage-secrets/index.md"><meta property="og:title" content="Manage secrets with Pulumi ESC · Pulumi docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pulumi ESC (Environments, Secrets, and Configuration) is a secure and robust secrets management solution. The tutorial will walk you through how to develop with Wrangler while following security best practices."><meta property="og:url" content="https://developers.cloudflare.com/pulumi/tutorial/manage-secrets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pulumi"><meta name="algolia_product_filter" content="Pulumi"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pulumi"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pulumi/tutorial/manage-secrets/#page","headline":"Manage secrets with Pulumi ESC \u00b7 Pulumi docs","description":"Pulumi ESC (Environments, Secrets, and Configuration) is a secure and robust secrets management solution. The tutorial will walk you through how to develop with Wrangler while following security best practices.","url":"https://developers.cloudflare.com/pulumi/tutorial/manage-secrets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pulumi/tutorial/manage-secrets/
  schema: 1
---
<p>In this tutorial, you will receive step-by-step instructions on using Pulumi ESC (Environments, Secrets, and Configuration), which is a secure and robust secrets management solution.</p>
<p>The tutorial will walk you through how to develop with Wrangler while following security best practices.</p>
<p>Specifically, you will learn how to manage your <code>CLOUDFLARE_API_TOKEN</code> for logging in to your Cloudflare account, pass ESC-stored secrets to Workers, and programmatically load your <code>.dev.vars</code> file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11149.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Ensure you have:</p>
<ul>
<li>A Cloudflare account. <a href="https://www.cloudflare.com/sign-up">Sign up for a Cloudflare account</a>.</li>
<li>A Pulumi Cloud account. <a href="https://app.pulumi.com/signup">Sign up for a Pulumi Cloud</a>.</li>
<li>The <a href="https://www.pulumi.com/docs/install/esc/">Pulumi ESC CLI</a> installed.</li>
<li>A Wrangler project. To create one, follow the <a href="/workers/get-started/guide/#1-create-a-new-worker-project">Create a New Worker project step</a>.</li>
</ul>
<h2 id="1-set-up-a-new-environment"><ol>
<li>Set up a new Environment</li>
</ol></h2>
<p>A <a href="https://www.pulumi.com/docs/esc/environments/">Pulumi ESC Environment</a>, or Environment, is a YAML file containing configurations and secrets for your application and infrastructure. These can be accessed in several ways, including shell commands. All ESC Environments reside in your Pulumi Cloud account.</p>
<h3 id="a-log-in-to-pulumi-cloud">a. Log in to Pulumi Cloud</h3>
<p>Use the Pulumi ESC CLI to log into your Pulumi Cloud account.</p>
<pre tabindex="0"><code class="language-sh">esc login&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Logged in to pulumi.com as  ....&#10;</code></pre>
<h3 id="b-create-a-new-environment">b. Create a new Environment</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11148.md")
</aside>
<pre tabindex="0"><code class="language-sh">ESC_ENV=wrangler/my-dev-environment&#10;esc env init $ESC_ENV&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Environment created.&#10;</code></pre>
<h2 id="2-log-into-cloudflare"><ol start="2">
<li>Log into Cloudflare</li>
</ol></h2>
<p>Now that the Pulumi ESC Environment has been created, it can be consumed in various ways. For instance, to log into your Cloudflare account without needing to predefine credentials in your shell.</p>
<h3 id="a-add-your-credentials">a. Add your credentials</h3>
<p>By externally and securely storing your <code>CLOUDFLARE_API_TOKEN</code>, you can control access and rotate the token value. We will run <code>wrangler</code> in non-interactive mode, which requires:</p>
<ul>
<li>Your Cloudflare <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a></li>
<li>A valid Cloudflare API <a href="/fundamentals/api/get-started/create-token/">token</a></li>
</ul>
<p>Replace the placeholder <code>123abc</code> with your corresponding values:</p>
<pre tabindex="0"><code class="language-sh">esc env set $ESC_ENV environmentVariables.CLOUDFLARE_ACCOUNT_ID 123abc&#10;esc env set $ESC_ENV environmentVariables.CLOUDFLARE_API_TOKEN  123abc --secret&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11147.md")
</aside>
<h3 id="b-log-out">b. Log out</h3>
<p>Ensure you're not currently logged in to your Cloudflare account.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler logout&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Not logged in, exiting...&#10;</code></pre>
<h3 id="c-log-in">c. Log in</h3>
<p>Pass ESC-stored Cloudflare credentials to Wrangler.</p>
<pre tabindex="0"><code class="language-sh">esc run ${ESC_ENV} npx wrangler whoami&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Getting User settings...&#10;👋 You are logged in with an API Token.&#10;</code></pre>
<p>When you use the <code>esc run</code> command, it opens the Environment and sets the specified Environment variables into a temporary environment. After that, it uses those variables in the context of the <code>wrangler</code> command. This is especially helpful when running <code>wrangler</code> commands in a CI/CD environment but wanting to avoid storing credentials directly in your pipeline.</p>
<h2 id="3-add-worker-secrets"><ol start="3">
<li>Add Worker secrets</li>
</ol></h2>
<p>Pulumi ESC centralizes secrets, and Wrangler can be used to pass them on to Workers and other Cloudflare resources. You will use the <code>wrangler secret put</code> command for this purpose.</p>
<h3 id="a-add-a-secret">a. Add a secret</h3>
<pre tabindex="0"><code class="language-sh">esc env set ${ESC_ENV} environmentVariables.TOP_SECRET &quot;aliens are real&quot; --secret&#10;</code></pre>
<h3 id="b-pass-the-secret-to-your-worker">b. Pass the secret to your Worker</h3>
<pre tabindex="0"><code class="language-sh">esc run -i ${ESC_ENV} -- sh -c &#x27;echo &quot;$TOP_SECRET&quot; | npx wrangler secret put TOP_SECRET&#x27;&#10;</code></pre>
<p>By using an external secrets management solution, commonly used Worker secrets can be stored in a single shared Environment that is accessed by the relevant Workers. You can use shell commands with <code>esc</code> to incorporate scripting and integrate them into deployment pipelines or <code>make</code> commands. Use <code>esc [command] --help</code> for more information about the various commands available in the CLI.</p>
<h2 id="4-load-dev-vars"><ol start="4">
<li>Load <code>.dev.vars</code></li>
</ol></h2>
<p>In this step, you will configure an Environment to load your <code>.dev.vars</code> file programmatically.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11146.md")
</aside>
<p>With a dedicated ESC Environment to store all the <code>.dev.vars</code> secrets, you can use a <code>dotenv</code> export flag.</p>
<h3 id="a-create-an-environment">a. Create an Environment</h3>
<pre tabindex="0"><code class="language-sh">E=wrangler/my-devvars&#10;esc env init $E&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Environment created.&#10;</code></pre>
<h3 id="b-add-a-secret">b. Add a secret</h3>
<pre tabindex="0"><code class="language-sh">esc env set $E environmentVariables.TOP_SECRET  &quot;the moon is made of cheese&quot; --secret&#10;</code></pre>
<h3 id="c-generate-the-dev-vars-file">c. Generate the <code>.dev.vars</code> file</h3>
<pre tabindex="0"><code class="language-sh">esc env open ${E} --format dotenv &gt; .dev.vars&#10;</code></pre>
<p>As <code>.dev.vars</code> files may often contain secrets, they should not be committed to source control. Keeping these secrets externally ensures you can load them to a new development environment without any loss.</p>
<h2 id="next-steps">Next steps</h2>
<p>You have configured Pulumi ESC Environments to load secrets for Wrangler commands, enhancing security during development with Wrangler. The externalized secrets are now reusable across Workers. <a href="https://www.pulumi.com/docs/esc/">Learn more about Pulumi ESC features and integrations</a> or follow the <a href="/pulumi/tutorial/hello-world/">Deploy a Worker with Pulumi</a> tutorial.</p>
