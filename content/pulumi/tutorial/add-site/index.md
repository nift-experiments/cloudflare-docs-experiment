---
cp9:
  canonical: https://developers.cloudflare.com/pulumi/tutorial/add-site/
  description: This tutorial uses Pulumi infrastructure as code (IaC) to familiarize yourself with the resource management lifecycle.
  full_title: Add a site · Pulumi docs
  head_html: <title>Add a site · Pulumi docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial uses Pulumi infrastructure as code (IaC) to familiarize yourself with the resource management lifecycle."><link rel="canonical" href="https://developers.cloudflare.com/pulumi/tutorial/add-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pulumi/tutorial/add-site/index.md"><meta property="og:title" content="Add a site · Pulumi docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial uses Pulumi infrastructure as code (IaC) to familiarize yourself with the resource management lifecycle."><meta property="og:url" content="https://developers.cloudflare.com/pulumi/tutorial/add-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pulumi"><meta name="algolia_product_filter" content="Pulumi"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pulumi"><meta name="pcx_tags" content="JavaScript,TypeScript,Python,Go,Java,.NET,YAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pulumi/tutorial/add-site/#page","headline":"Add a site \u00b7 Pulumi docs","description":"This tutorial uses Pulumi infrastructure as code (IaC) to familiarize yourself with the resource management lifecycle.","url":"https://developers.cloudflare.com/pulumi/tutorial/add-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","TypeScript","Python","Go","Java",".NET","YAML"]}</script>
  markdown: true
  noindex: false
  route: /pulumi/tutorial/add-site/
  schema: 1
---
<p>In this tutorial, you will follow step-by-step instructions to bring an existing site to Cloudflare using Pulumi infrastructure as code (IaC) to familiarize yourself with the resource management lifecycle. In particular, you will create a Zone and a DNS record to resolve your newly added site. This tutorial adopts the IaC principle to complete the steps listed in the <a href="/fundamentals/manage-domains/add-site/">Add site tutorial</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11204.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Ensure you have:</p>
<ul>
<li>A Cloudflare account and API Token with permission to edit the resources in this tutorial. If you need to, sign up for a <a href="https://www.cloudflare.com/sign-up">Cloudflare account</a> before continuing. Your token must have:
<ul>
<li><code>Zone-Zone-Edit</code> permission</li>
<li><code>Zone-DNS-Edit</code> permission</li>
<li><code>include-All zones from an account-&lt;your account&gt;</code> zone resource</li>
</ul>
</li>
<li>A Pulumi Cloud account. You can sign up for an <a href="https://app.pulumi.com/signup">always-free individual tier</a>.</li>
<li>The <a href="/pulumi/installing/">Pulumi CLI</a> is installed on your machine.</li>
<li>A <a href="https://github.com/pulumi/pulumi?tab=readme-ov-file#languages">Pulumi-supported programming language</a> is configured. (TypeScript, JavaScript, Python, Go, .NET, Java, or use YAML)</li>
<li>A domain name. You may use <code>example.com</code> to complete the tutorial.</li>
</ul>
<h2 id="1-initialize-your-project"><ol>
<li>Initialize your project</li>
</ol></h2>
<p>A Pulumi project is a collection of files in a dedicated folder that describes the infrastructure you want to create. The Pulumi project folder is identified by the required <code>Pulumi.yaml</code> file. You will use the Pulumi CLI to create and configure a new project.</p>
<h3 id="a-create-a-directory">a. Create a directory</h3>
<p>Use a new and empty directory for this tutorial.</p>
<pre tabindex="0"><code class="language-sh">mkdir addsite-cloudflare&#10;cd addsite-cloudflare&#10;</code></pre>
<h3 id="b-login-to-pulumi-cloud">b. Login to Pulumi Cloud</h3>
<p><a href="https://www.pulumi.com/product/pulumi-cloud/">Pulumi Cloud</a> is a hosted service that provides a secure and scalable platform for managing your infrastructure as code. You will use it to store your Pulumi backend configurations.</p>
<p>At the prompt, press Enter to log into your Pulumi Cloud account via the browser. Alternatively, you may provide a <a href="https://www.pulumi.com/docs/pulumi-cloud/access-management/access-tokens/">Pulumi Cloud access token</a>.</p>
<pre tabindex="0"><code class="language-sh">pulumi login&#10;</code></pre>
<h3 id="c-create-a-new-program">c. Create a new program</h3>
<p>A Pulumi program is code written in a <a href="https://github.com/pulumi/pulumi?tab=readme-ov-file#languages">supported programming language</a> that defines infrastructure resources.</p>
<p>To create a program, select your language of choice and run the <code>pulumi</code> command:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11212.md")
</div></div>
<h3 id="d-create-a-stack">d. Create a stack</h3>
<p>A Pulumi <a href="https://www.pulumi.com/docs/concepts/stack/">stack</a> is an instance of a Pulumi program. Stacks are independently configurable and may represent different environments (development, staging, production) or feature branches. For this tutorial, you'll use the <code>dev</code> stack.</p>
<p>To instantiate your <code>dev</code> stack, run:</p>
<pre tabindex="0"><code class="language-sh">pulumi up --yes&#10;&#35; wait a few seconds for the stack to be instantiated.&#10;</code></pre>
<p>You have not defined any resources at this point, so you'll have an empty stack.</p>
<h3 id="e-save-your-settings">e. Save your settings</h3>
<p>In this step, you will store your settings in a Pulumi <a href="https://www.pulumi.com/docs/esc/environments/">ESC Environment</a>, a YAML file containing configurations and secrets. These can be accessed in several ways, including a Pulumi program. All ESC Environments securely reside in your Pulumi Cloud account and can be fully managed via the Pulumi CLI. For this tutorial, you will store the following values:</p>
<ul>
<li>Your Cloudflare <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</li>
<li>A valid Cloudflare API <a href="/fundamentals/api/get-started/create-token/">token</a>.</li>
<li>A domain. For instance, <code>example.com</code>.</li>
</ul>
<pre tabindex="0"><code class="language-sh">&#35; Define an ESC Environment name&#10;E=cloudflare/my-dev-env&#10;&#10;&#35; Create a new Pulumi ESC Environment&#10;pulumi config env init --env $E --yes&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Creating environment cloudflare/my-dev-env for stack dev...&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Replace abc123 with your Cloudflare Account ID&#10;pulumi env set $E --plaintext pulumiConfig.accountId abc123&#10;&#10;&#35; Replace API_TOKEN with your Cloudflare API Token&#10;pulumi env set $E --secret  pulumiConfig.cloudflare:apiToken API_TOKEN&#10;&#10;&#35; Replace example.com with your registered domain, or leave as is&#10;pulumi env set $E --plaintext pulumiConfig.domain example.com&#10;</code></pre>
<h3 id="f-install-the-cloudflare-package">f. Install the Cloudflare package</h3>
<p>You need to install the Cloudflare package for your language of choice in order to define Cloudflare resources in your Pulumi program.</p>
<p>Install the Cloudflare package by running the following command:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11220.md")
</div></div>
<h2 id="2-define-cloudflare-resources-in-code"><ol start="2">
<li>Define Cloudflare resources in code</li>
</ol></h2>
<p>With the Cloudflare package installed, you can now define any <a href="https://www.pulumi.com/registry/packages/cloudflare/">supported Cloudflare resource</a> in your Pulumi program. You'll define a Zone, and a DNS Record next.</p>
<h3 id="a-add-a-zone">a. Add a Zone</h3>
<p>A domain, or site, is known as a Zone in Cloudflare. In Pulumi, the <a href="https://www.pulumi.com/registry/packages/cloudflare/api-docs/zone/">Zone resource</a> represents a Cloudflare Zone.</p>
<p>Replace the contents of your entrypoint file with the following:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11228.md")
</div></div>
<p>Notice that the code also outputs several properties from the Zone resource, such as the <code>zoneId</code>, <code>nameservers</code>, and <code>status</code>, so that they can easily be accessed in subsequent steps.</p>
<h3 id="b-add-a-dns-record">b. Add a DNS Record</h3>
<p>You will now add a DNS <a href="https://www.pulumi.com/registry/packages/cloudflare/api-docs/record/">Record resource</a> to test previously configured Zone.</p>
<p>Add the following code snippet to your entrypoint file <strong>after</strong> the Zone resource definition:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11236.md")
</div></div>
<h2 id="3-deploy-your-changes"><ol start="3">
<li>Deploy your changes</li>
</ol></h2>
<p>Now that you have defined your resources, you can deploy the changes using the Pulumi CLI so that they are reflected in your Cloudflare account.</p>
<p>To deploy the changes, run:</p>
<pre tabindex="0"><code class="language-sh">pulumi up --yes&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">wait for the dev stack to become ready&#10;</code></pre>
<h2 id="4-configure-your-dns-provider"><ol start="4">
<li>Configure your DNS provider</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11203.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11202.md")
</aside>
<h3 id="a-obtain-your-nameservers">a. Obtain your nameservers</h3>
<p>Once you have added a domain to Cloudflare, that domain will receive two assigned authoritative nameservers.</p>
<p>To retrieve the assigned <code>nameservers</code>, run:</p>
<pre tabindex="0"><code class="language-sh">pulumi stack output&#10;</code></pre>
<h3 id="b-update-your-registrar">b. Update your registrar</h3>
<p>Update the nameservers at your registrar to activate Cloudflare services for your domain. The instructions are registrar-specific. You may be able to find guidance under <a href="/dns/zone-setups/full-setup/setup/#34-update-your-registrar">this consolidated list of common registrars</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11201.md")
</aside>
<h3 id="c-check-your-domain-status">c. Check your domain status</h3>
<p>Once successfully registered, your domain <code>status</code> will change to <code>active</code>.</p>
<pre tabindex="0"><code class="language-sh">pulumi stack output&#10;</code></pre>
<h2 id="5-test-your-site"><ol start="5">
<li>Test your site</li>
</ol></h2>
<p>You will run two <code>nslookup</code> commands against the Cloudflare-assigned nameservers.</p>
<p>To test your site, run:</p>
<pre tabindex="0"><code class="language-sh">DOMAIN=$(pulumi config get domain)&#10;NS1=$(pulumi stack output nameservers | jq &#x27;.[0]&#x27; -r)&#10;NS2=$(pulumi stack output nameservers | jq &#x27;.[1]&#x27; -r)&#10;nslookup $DOMAIN $NS1&#10;nslookup $DOMAIN $NS2&#10;</code></pre>
<p>For .NET, use <code>Nameservers</code> as the Output.</p>
<p>Confirm your response returns the IP address(es) for your site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11200.md")
</aside>
<h2 id="6-clean-up"><ol start="6">
<li>Clean up</li>
</ol></h2>
<p>In this last step, you will remove the resources and stack used throughout the tutorial.</p>
<h3 id="a-delete-the-resources">a. Delete the resources</h3>
<pre tabindex="0"><code class="language-sh">pulumi destroy --yes&#10;</code></pre>
<h3 id="b-remove-the-stack">b. Remove the stack</h3>
<pre tabindex="0"><code class="language-sh">pulumi stack rm dev&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>You have incrementally defined Cloudflare resources needed to add a site to Cloudflare. You declare the resources in your programming language of choice and let Pulumi handle the rest.</p>
<p>To deploy a serverless app with Pulumi, follow the <a href="/pulumi/tutorial/hello-world/">Deploy a Worker tutorial</a>.</p>
