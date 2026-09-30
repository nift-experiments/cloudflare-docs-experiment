---
cp9:
  canonical: https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/
  description: Deploy prebuilt assets to Cloudflare Pages using Wrangler in your CI/CD pipeline.
  full_title: Use Direct Upload with continuous integration · Cloudflare Pages docs
  head_html: <title>Use Direct Upload with continuous integration · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy prebuilt assets to Cloudflare Pages using Wrangler in your CI/CD pipeline."><link rel="canonical" href="https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/index.md"><meta property="og:title" content="Use Direct Upload with continuous integration · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy prebuilt assets to Cloudflare Pages using Wrangler in your CI/CD pipeline."><meta property="og:url" content="https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/#page","headline":"Use Direct Upload with continuous integration \u00b7 Cloudflare Pages docs","description":"Deploy prebuilt assets to Cloudflare Pages using Wrangler in your CI/CD pipeline.","url":"https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/how-to/use-direct-upload-with-continuous-integration/
  schema: 1
---
<p>Cloudflare Pages supports directly uploading prebuilt assets, allowing you to use custom build steps for your applications and deploy to Pages with <a href="/workers/wrangler/install-and-update/">Wrangler</a>. This guide will teach you how to deploy your application to Pages, using continuous integration.</p>
<h2 id="deploy-with-wrangler">Deploy with Wrangler</h2>
<p>In your project directory, install <a href="/workers/wrangler/install-and-update/">Wrangler</a> so you can deploy a folder of prebuilt assets by running the following command:</p>
<pre tabindex="0"><code class="language-sh">&#35; Publish created project&#10;$ CLOUDFLARE_ACCOUNT_ID=&lt;ACCOUNT_ID&gt; npx wrangler pages deploy &lt;DIRECTORY&gt; --project-name=&lt;PROJECT_NAME&gt;&#10;</code></pre>
<h2 id="get-credentials-from-cloudflare">Get credentials from Cloudflare</h2>
<h3 id="generate-an-api-token">Generate an API Token</h3>
<p>To generate an API token:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>API Tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create Token**.
3. Under **Custom Token**, select **Get started**.
4. Name your API Token in the **Token name** field.
5. Under **Permissions**, select _Account_, _Cloudflare Pages_ and _Edit_:
6. Select **Continue to summary** > **Create Token**.
<p><img src="/assets/upstream/images/pages/how-to/select-api-token-for-pages.png" alt="Follow the instructions above to create an API token for Cloudflare Pages" /></p>
<p>Now that you have created your API token, you can use it to push your project from continuous integration platforms.</p>
<h3 id="get-project-account-id">Get project account ID</h3>
<p>To find your account ID, go to the <strong>Zone Overview</strong> page in the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>Find your account ID in the <strong>API</strong> section on the right-hand side menu.</p>
<p>If you have not added a zone, add one by selecting <strong>Add</strong> &gt; <strong>Connect a domain</strong>. You can purchase a domain from <a href="/registrar/">Cloudflare's registrar</a>.</p>
<h2 id="use-github-actions">Use GitHub Actions</h2>
<p><a href="https://docs.github.com/en/actions">GitHub Actions</a> is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline when using GitHub. You can create workflows that build and test every pull request to your repository or deploy merged pull requests to production.</p>
<p>After setting up your project, you can set up a GitHub Action to automate your subsequent deployments with Wrangler.</p>
<h3 id="add-cloudflare-credentials-to-github-secrets">Add Cloudflare credentials to GitHub secrets</h3>
<p>In the GitHub Action you have set up, environment variables are needed to push your project up to Cloudflare Pages. To add the values of these environment variables in your project's GitHub repository:</p>
<ol>
<li>Go to your project's repository in GitHub.</li>
<li>Under your repository's name, select <strong>Settings</strong>.</li>
<li>Select <strong>Secrets</strong> &gt; <strong>Actions</strong> &gt; <strong>New repository secret</strong>.</li>
<li>Create one secret and put <strong>CLOUDFLARE_ACCOUNT_ID</strong> as the name with the value being your Cloudflare account ID.</li>
<li>Create another secret and put <strong>CLOUDFLARE_API_TOKEN</strong> as the name with the value being your Cloudflare API token.</li>
</ol>
<p>Add the value of your Cloudflare account ID and Cloudflare API token as <code>CLOUDFLARE_ACCOUNT_ID</code> and <code>CLOUDFLARE_API_TOKEN</code>, respectively. This will ensure that these secrets are secure, and each time your Action runs, it will access these secrets.</p>
<h3 id="set-up-a-workflow">Set up a workflow</h3>
<p>Create a <code>.github/workflows/pages-deployment.yaml</code> file at the root of your project. The <code>.github/workflows/pages-deployment.yaml</code> file will contain the jobs you specify on the request, that is: <code>on: [push]</code> in this case. It can also be on a pull request. For a detailed explanation of GitHub Actions syntax, refer to the <a href="https://docs.github.com/en/actions">official documentation</a>.</p>
<p>In your <code>pages-deployment.yaml</code> file, copy the following content:</p>
<pre tabindex="0"><code class="language-yaml">on: [push]&#10;jobs:&#10;  deploy:&#10;    runs-on: ubuntu-latest&#10;    permissions:&#10;      contents: read&#10;      deployments: write&#10;    name: Deploy to Cloudflare Pages&#10;    steps:&#10;      &#45; name: Checkout&#10;        uses: actions/checkout@v6&#10;      &#35; Run your project&#x27;s build step&#10;      &#35; - name: Build&#10;      &#35;   run: npm install &amp;&amp; npm run build&#10;      &#45; name: Deploy&#10;        uses: cloudflare/wrangler-action@v3&#10;        with:&#10;          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}&#10;          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}&#10;          command: pages deploy YOUR_DIRECTORY_OF_STATIC_ASSETS --project-name=YOUR_PROJECT_NAME&#10;          gitHubToken: ${{ secrets.GITHUB_TOKEN }}&#10;</code></pre>
<p>In the above code block, you have set up an Action that runs when you push code to the repository. Replace <code>YOUR_PROJECT_NAME</code> with your Cloudflare Pages project name and <code>YOUR_DIRECTORY_OF_STATIC_ASSETS</code> with your project's output directory, respectively.</p>
<p>The <code>${{ secrets.GITHUB_TOKEN }}</code> will be automatically provided by GitHub Actions with the <code>contents: read</code> and <code>deployments: write</code> permission. This will enable our Cloudflare Pages action to create a Deployment on your behalf.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10889.md")
</aside>
<h2 id="using-circleci-for-ci-cd">Using CircleCI for CI/CD</h2>
<p><a href="https://circleci.com/">CircleCI</a> is another continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. It can be configured to efficiently run complex pipelines with caching, docker layer caching, and resource classes.</p>
<p>Similar to GitHub Actions, CircleCI can use Wrangler to continuously deploy your projects each time to push to your code.</p>
<h3 id="add-cloudflare-credentials-to-circleci">Add Cloudflare credentials to CircleCI</h3>
<p>After you have generated your Cloudflare API token and found your account ID in the dashboard, you will need to add them to your CircleCI dashboard to use your environment variables in your project.</p>
<p>To add environment variables, in the CircleCI web application:</p>
<ol>
<li>Go to your Pages project &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Projects</strong> in the side menu.</li>
<li>Select the ellipsis (...) button in the project's row. You will see the option to add environment variables.</li>
<li>Select <strong>Environment Variables</strong> &gt; <strong>Add Environment Variable</strong>.</li>
<li>Enter the name and value of the new environment variable, which is your Cloudflare credentials (<code>CLOUDFLARE_ACCOUNT_ID</code> and <code>CLOUDFLARE_API_TOKEN</code>).</li>
</ol>
<p><img src="/assets/upstream/images/pages/how-to/project-settings-env-var-v2.png" alt="Follow the instructions above to add environment variables to your CircleCI settings" /></p>
<h3 id="set-up-a-workflow-1">Set up a workflow</h3>
<p>Create a <code>.circleci/config.yml</code> file at the root of your project. This file contains the jobs that will be executed based on the order of your workflow. In your <code>config.yml</code> file, copy the following content:</p>
<pre tabindex="0"><code class="language-yaml">version: 2.1&#10;jobs:&#10;  Publish-to-Pages:&#10;    docker:&#10;      &#45; image: cimg/node:18.7.0&#10;&#10;    steps:&#10;      &#45; checkout&#10;      &#35; Run your project&#x27;s build step&#10;      &#45; run: npm install &amp;&amp; npm run build&#10;      &#35; Publish with wrangler&#10;      &#45; run: npx wrangler pages deploy dist --project-name=&lt;PROJECT NAME&gt; # Replace dist with the name of your build folder and input your project name&#10;&#10;workflows:&#10;  Publish-to-Pages-workflow:&#10;    jobs:&#10;      &#45; Publish-to-Pages&#10;</code></pre>
<p>Your continuous integration workflow is broken down into jobs when using CircleCI. From the code block above, you can see that you first define a list of jobs that run on each commit. For example, your repository will run on a prebuilt docker image <code>cimg/node:18.7.0</code>. It first checks out the repository with the Node version specified in the image.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10888.md")
</aside>
<p>You can modify the Wrangler command with any <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code> options</a>.</p>
<p>After all the specified steps, define a <code>workflow</code> at the end of your file. You can learn more about creating a custom process with CircleCI from the <a href="https://circleci.com/docs/2.0/concepts/">official documentation</a>.</p>
<h2 id="travis-ci-for-ci-cd">Travis CI for CI/CD</h2>
<p>Travis CI is an open-source continuous integration tool that handles specific tasks, such as pull requests and code pushes for your project workflow. Travis CI can be integrated into your GitHub projects, databases, and other preinstalled services enabled in your build configuration. To use Travis CI, you should have A GitHub, Bitbucket, GitLab or Assembla account.</p>
<h3 id="add-cloudflare-credentials-to-travisci">Add Cloudflare credentials to TravisCI</h3>
<p>In your Travis project, add the Cloudflare credentials you have generated from the Cloudflare dashboard to access them in your <code>travis.yml</code> file. Go to your Travis CI dashboard and select your current project &gt; <strong>More options</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment Variables</strong>.</p>
<p>Set the environment variable's name and value and the branch you want it to be attached to. You can also set the privacy of the value.</p>
<h3 id="setup">Setup</h3>
<p>Go to <a href="https://Travis-ci.com">Travis-ci.com</a> and enable your repository by login in with your preferred provider. This guide uses GitHub. Next, create a <code>.travis.yml</code> file and copy the following into the file:</p>
<pre tabindex="0"><code class="language-yaml">language: node_js&#10;node_js:&#10;  &#45; &quot;18.0.0&quot; # You can specify more versions of Node you want your CI process to support&#10;branches:&#10;  only:&#10;    &#45; travis-ci-test # Specify what branch you want your CI process to run on&#10;install:&#10;  &#45; npm install&#10;&#10;script:&#10;  &#45; npm run build # Switch this out with your build command or remove it if you don&#x27;t have a build step&#10;  &#45; npx wrangler pages deploy dist --project-name=&lt;PROJECT NAME&gt;&#10;&#10;env:&#10;  &#45; CLOUDFLARE_ACCOUNT_ID: { $CLOUDFLARE_ACCOUNT_ID }&#10;  &#45; CLOUDFLARE_API_TOKEN: { $CLOUDFLARE_API_TOKEN }&#10;</code></pre>
<p>This will set the Node.js version to 18. You have also set branches you want your continuous integration to run on. Finally, input your <code>PROJECT NAME</code> in the script section and your CI process should work as expected.</p>
<p>You can also modify the Wrangler command with any <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code> options</a>.</p>
