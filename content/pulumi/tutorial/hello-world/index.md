---
cp9:
  canonical: https://developers.cloudflare.com/pulumi/tutorial/hello-world/
  description: In this tutorial, you will follow step-by-step instructions to deploy a Hello World application using Cloudflare Workers and Pulumi infrastructure as code (IaC).
  full_title: Deploy a Worker · Pulumi docs
  head_html: <title>Deploy a Worker · Pulumi docs</title><meta name="generator" content="Nift"><meta name="description" content="In this tutorial, you will follow step-by-step instructions to deploy a Hello World application using Cloudflare Workers and Pulumi infrastructure as code (IaC)."><link rel="canonical" href="https://developers.cloudflare.com/pulumi/tutorial/hello-world/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pulumi/tutorial/hello-world/index.md"><meta property="og:title" content="Deploy a Worker · Pulumi docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="In this tutorial, you will follow step-by-step instructions to deploy a Hello World application using Cloudflare Workers and Pulumi infrastructure as code (IaC)."><meta property="og:url" content="https://developers.cloudflare.com/pulumi/tutorial/hello-world/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pulumi"><meta name="algolia_product_filter" content="Pulumi"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="JavaScript,TypeScript,Python,Go,Java,.NET,YAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pulumi/tutorial/hello-world/#page","headline":"Deploy a Worker \u00b7 Pulumi docs","description":"In this tutorial, you will follow step-by-step instructions to deploy a Hello World application using Cloudflare Workers and Pulumi infrastructure as code (IaC).","url":"https://developers.cloudflare.com/pulumi/tutorial/hello-world/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","TypeScript","Python","Go","Java",".NET","YAML"]}</script>
  markdown: true
  noindex: false
  route: /pulumi/tutorial/hello-world/
  schema: 1
---
<p>In this tutorial, you will follow step-by-step instructions to deploy a Hello World application using Cloudflare Workers and Pulumi infrastructure as code (IaC) to familiarize yourself with the resource management lifecycle. In particular, you will create a Worker, a Route, and a DNS Record to access the application before cleaning up all the resources.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11151.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Ensure you have:</p>
<ul>
<li>A Cloudflare account and API Token with permission to edit the resources in this tutorial. If you need to, sign up for a <a href="https://www.cloudflare.com/sign-up">Cloudflare account</a> before continuing. Your token must have the following:
<ul>
<li><code>Account-Workers Scripts-Edit</code> permission</li>
<li><code>Zone-Workers Route-Edit</code> permission</li>
<li><code>Zone-DNS-Edit</code> permission</li>
</ul>
</li>
<li>A Pulumi Cloud account. You can sign up for an <a href="https://app.pulumi.com/signup">always-free individual tier</a>.</li>
<li>The <a href="/pulumi/installing/">Pulumi CLI</a> is installed on your machine.</li>
<li>A <a href="https://github.com/pulumi/pulumi?tab=readme-ov-file#languages">Pulumi-supported programming language</a> configured. (TypeScript, JavaScript, Python, Go, .NET, Java, or use YAML)</li>
<li>A Cloudflare-managed domain. Complete the <a href="/pulumi/tutorial/add-site/">Add a site tutorial</a> to bring your existing domain under Cloudflare.</li>
</ul>
<h2 id="1-initialize-your-project"><ol>
<li>Initialize your project</li>
</ol></h2>
<p>A Pulumi project is a collection of files in a dedicated folder that describes the infrastructure you want to create. The Pulumi project folder is identified by the required <code>Pulumi.yaml</code> file. You will use the Pulumi CLI to create and configure a new project.</p>
<h3 id="a-create-a-directory">a. Create a directory</h3>
<p>Use a new and empty directory for this tutorial.</p>
<pre tabindex="0"><code class="language-sh">mkdir serverless-cloudflare&#10;cd serverless-cloudflare&#10;</code></pre>
<h3 id="b-login-to-pulumi-cloud">b. Login to Pulumi Cloud</h3>
<p><a href="https://www.pulumi.com/product/pulumi-cloud/">Pulumi Cloud</a> is a hosted service that provides a secure and scalable platform for managing your infrastructure as code. You will use it to store your Pulumi backend configurations.</p>
<p>At the prompt, press Enter to log into your Pulumi Cloud account via the browser. Alternatively, you may provide a <a href="https://www.pulumi.com/docs/pulumi-cloud/access-management/access-tokens/">Pulumi Cloud access token</a>.</p>
<pre tabindex="0"><code class="language-sh">pulumi login&#10;</code></pre>
<h3 id="c-create-a-new-program">c. Create a new program</h3>
<p>A Pulumi program is code written in a <a href="https://github.com/pulumi/pulumi?tab=readme-ov-file#languages">supported programming language</a> that defines infrastructure resources.</p>
<p>To create a program, select your language of choice and run the <code>pulumi</code> command:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11159.md")
</div></div>
<h3 id="d-create-a-stack">d. Create a stack</h3>
<p>A Pulumi <a href="https://www.pulumi.com/docs/concepts/stack/">stack</a> is an instance of a Pulumi program. Stacks are independently configurable and may represent different environments (development, staging, production) or feature branches. For this tutorial, you'll use the <code>dev</code> stack.</p>
<p>To instantiate your <code>dev</code> stack, run:</p>
<pre tabindex="0"><code class="language-sh">pulumi up --yes&#10;&#35; wait a few seconds for the stack to be instantiated.&#10;</code></pre>
<p>You have not defined any resources at this point, so you'll have an empty stack.</p>
<h3 id="e-save-your-application-settings">e. Save your application settings</h3>
<p>In this step, you will store your application settings in a Pulumi <a href="https://www.pulumi.com/docs/esc/environments/">ESC Environment</a>, a YAML file containing configurations and secrets. These can be accessed in several ways, including a Pulumi program. All ESC Environments securely reside in your Pulumi Cloud account and can be fully managed via the Pulumi CLI. For this tutorial, you will store the following values:</p>
<ul>
<li>Your Cloudflare <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</li>
<li>A valid Cloudflare API <a href="/fundamentals/api/get-started/create-token/">token</a>.</li>
<li>A domain. For instance, <code>example.com</code>.</li>
</ul>
<pre tabindex="0"><code class="language-sh">&#35; Give your new ESC Environment a name&#10;E=hello-world/dev-env&#10;&#10;&#35; Initialize the new ESC Environment&#10;pulumi config env init --env $E --yes&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Creating environment hello-world/dev-env for stack dev...&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Replace abc123 with your Cloudflare account ID&#10;pulumi env set $E --plaintext pulumiConfig.accountId abc123&#10;&#10;&#35; Replace API_TOKEN with your Cloudflare API token&#10;pulumi env set $E --secret pulumiConfig.cloudflare:apiToken API_TOKEN&#10;&#10;&#35; Replace example.com with your domain&#10;pulumi env set $E --plaintext pulumiConfig.domain example.com&#10;</code></pre>
<h3 id="f-install-the-cloudflare-package">f. Install the Cloudflare package</h3>
<p>You need to install the Cloudflare package for your language of choice in order to define Cloudflare resources in your Pulumi program.</p>
<p>Install the Cloudflare package by running the following command:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11167.md")
</div></div>
<h2 id="2-define-cloudflare-resources-in-code"><ol start="2">
<li>Define Cloudflare resources in code</li>
</ol></h2>
<p>With the Cloudflare package installed, you can now define any <a href="https://www.pulumi.com/registry/packages/cloudflare/">supported Cloudflare resource</a> in your Pulumi program. Next, define a Worker, a Route, and a DNS Record.</p>
<h3 id="a-add-a-workers-script">a. Add a Workers script</h3>
<p>The <a href="https://www.pulumi.com/registry/packages/cloudflare/api-docs/workersscript/">Workers Script resource</a> represents a Cloudflare Worker that can be deployed to the Cloudflare network.</p>
<p>Replace the contents of your entrypoint file with the following:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11175.md")
</div></div>
<h3 id="b-add-a-route">b. Add a Route</h3>
<p>You will now add a <a href="https://www.pulumi.com/registry/packages/cloudflare/api-docs/workersroute/">Workers Route resource</a> to your Pulumi program so the Workers script can have an endpoint and be active. To properly configure the Route, you will also look up the zone ID for your domain.</p>
<p>Add the following code snippet to your entrypoint file <strong>after</strong> the Worker script resource:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11183.md")
</div></div>
<h3 id="c-add-a-dns-record">c. Add a DNS Record</h3>
<p>You will now add a DNS <a href="https://www.pulumi.com/registry/packages/cloudflare/api-docs/record/">Record resource</a> to resolve the previously configured Route. In the next step, you'll also output the Route URL so it can be easily accessed.</p>
<p>Add the following code snippet to your entrypoint file <strong>after</strong> the Route resource:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11191.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11150.md")
</aside>
<h3 id="d-optional-verify-your-code">d. (Optional) Verify your code</h3>
<p>Confirm all your changes match the full solution below:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11199.md")
</div></div>
<h2 id="3-deploy-your-application"><ol start="3">
<li>Deploy your application</li>
</ol></h2>
<p>Now that you have defined all the Cloudflare resources, you can deploy the Hello World application to your Cloudflare account using the Pulumi CLI.</p>
<p>To deploy the changes, run:</p>
<pre tabindex="0"><code class="language-sh">pulumi up --yes&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">wait for the dev stack to become ready&#10;</code></pre>
<h2 id="4-test-the-worker"><ol start="4">
<li>Test the Worker</li>
</ol></h2>
<p>You incrementally added Cloudflare resources to run and access your Hello World application. You can test your application by curling the <code>url</code> output from the Pulumi stack.</p>
<pre tabindex="0"><code class="language-sh">curl $(pulumi stack output url)&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Hello, World!&#10;</code></pre>
<h2 id="5-clean-up"><ol start="5">
<li>Clean up</li>
</ol></h2>
<p>In this last step, you will clean up the resources and stack used throughout the tutorial.</p>
<h3 id="a-delete-the-cloudflare-resources">a. Delete the Cloudflare resources</h3>
<pre tabindex="0"><code class="language-sh">pulumi destroy&#10;</code></pre>
<h3 id="b-remove-the-pulumi-stack">b. Remove the Pulumi stack</h3>
<pre tabindex="0"><code class="language-sh">pulumi stack rm dev&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Visit the <a href="https://www.pulumi.com/docs/reference/pkg/cloudflare/">Cloudflare package documentation</a> to explore other resources you can define with Pulumi and Cloudflare.</p>
