---
cp9:
  canonical: https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/
  description: Integrate Workers development into your existing GitHub Actions workflows.
  full_title: GitHub Actions · Cloudflare Workers docs
  head_html: <title>GitHub Actions · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Workers development into your existing GitHub Actions workflows."><link rel="canonical" href="https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/index.md"><meta property="og:title" content="GitHub Actions · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Workers development into your existing GitHub Actions workflows."><meta property="og:url" content="https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/#page","headline":"GitHub Actions \u00b7 Cloudflare Workers docs","description":"Integrate Workers development into your existing GitHub Actions workflows.","url":"https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/ci-cd/external-cicd/github-actions/
  schema: 1
---
<p>You can deploy Workers with <a href="https://github.com/marketplace/actions/deploy-to-cloudflare-workers-with-wrangler">GitHub Actions</a>. Here is how you can set up your GitHub Actions workflow.</p>
<h2 id="1-authentication"><ol>
<li>Authentication</li>
</ol></h2>
<p>When running Wrangler locally, authentication to the Cloudflare API happens via the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> command, which initiates an interactive authentication flow. Since CI/CD environments are non-interactive, Wrangler requires a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> and <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> to authenticate with the Cloudflare API.</p>
<h3 id="cloudflare-account-id">Cloudflare account ID</h3>
<p>To find your Cloudflare account ID, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find account and zone IDs</a>.</p>
<h3 id="api-token">API token</h3>
<p>To create an API token to authenticate Wrangler in your CI job:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Under <strong>Permission policies</strong>, open the <strong>Custom</strong> dropdown and select <strong>Edit Cloudflare Workers</strong>.</li>
<li>Customize your token name.</li>
<li>Scope your token.</li>
</ol>
<p>You will need to choose the account and zone resources that the generated API token will have access to. We recommend scoping these down as much as possible to limit the access of your token. For example, if you have access to three different Cloudflare accounts, you should restrict the generated API token to only the account on which you will be deploying a Worker.</p>
<h2 id="2-set-up-ci-cd"><ol start="2">
<li>Set up CI/CD</li>
</ol></h2>
<p>The method for running Wrangler in your CI/CD environment will depend on the specific setup for your project (whether you use GitHub Actions/Jenkins/GitLab or something else entirely).</p>
<p>To set up your CI/CD:</p>
<ol>
<li>Go to your CI/CD platform and add the following as secrets:</li>
</ol>
<ul>
<li><code>CLOUDFLARE_ACCOUNT_ID</code>: Set to the <a href="#cloudflare-account-id">Cloudflare account ID</a> for the account on which you want to deploy your Worker.</li>
<li><code>CLOUDFLARE_API_TOKEN</code>: Set to the <a href="#api-token">Cloudflare API token you generated</a>.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16764.md")
</aside>
<ol start="2">
<li>Create a workflow that will be responsible for deploying the Worker. This workflow should run <code>wrangler deploy</code>. Review an example <a href="https://docs.github.com/en/actions/using-workflows/about-workflows">GitHub Actions</a> workflow in the follow section.</li>
</ol>
<h3 id="github-actions">GitHub Actions</h3>
<p>Cloudflare provides <a href="https://github.com/cloudflare/wrangler-action">an official action</a> for deploying Workers. Refer to the following example workflow which deploys your Worker on push to the <code>main</code> branch.</p>
<pre tabindex="0"><code class="language-yaml">name: Deploy Worker&#10;on:&#10;  push:&#10;    branches:&#10;      &#45; main&#10;jobs:&#10;  deploy:&#10;    runs-on: ubuntu-latest&#10;    timeout-minutes: 60&#10;    steps:&#10;      &#45; uses: actions/checkout@v6&#10;      &#45; name: Build &amp; Deploy Worker&#10;        uses: cloudflare/wrangler-action@v3&#10;        with:&#10;          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}&#10;          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}&#10;</code></pre>
