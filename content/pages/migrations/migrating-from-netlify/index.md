<p>In this tutorial, you will learn how to migrate your Netlify application to Cloudflare Pages.</p>
<h2 id="finding-your-build-command-and-build-directory">Finding your build command and build directory</h2>
<p>To move your application to Cloudflare Pages, find your build command and build directory. Cloudflare Pages will use this information to build and deploy your application.</p>
<p>In your Netlify Dashboard, find the project that you want to deploy. It should be configured to deploy from a GitHub repository.</p>
<p><img src="/assets/upstream/images/pages/migrations/netlify-deploy-1.png" alt="Selecting a site in the Netlify Dashboard" /></p>
<p>Inside of your site dashboard, select <strong>Site Settings</strong>, and then <strong>Build &amp; Deploy</strong>.</p>
<p><img src="/assets/upstream/images/pages/migrations/netlify-deploy-2.png" alt="Selecting Site Settings in site dashboard" /></p>
<p><img src="/assets/upstream//images/pages/migrations/netlify-deploy-3.png" alt="Selecting Build and Deploy in sidebar" /></p>
<p>In the <strong>Build &amp; Deploy</strong> tab, find the <strong>Build settings</strong> panel, which will have the <strong>Build command</strong> and <strong>Publish directory</strong> fields. Save these for deploying to Cloudflare Pages. In the below image, <strong>Build command</strong> is <code>yarn build</code>, and <strong>Publish directory</strong> is <code>build/</code>.</p>
<p><img src="/assets/upstream/images/pages/migrations/netlify-deploy-4.png" alt="Finding the Build command and Publish directory fields" /></p>
<h2 id="migrating-redirects-and-headers">Migrating redirects and headers</h2>
<p>If your site includes a <code>_redirects</code> file in your publish directory, you can use the same file in Cloudflare Pages and your redirects will execute successfully. If your redirects are in your <code>netlify.toml</code> file, you will need to add them to the <code>_redirects</code> folder. Cloudflare Pages currently offers limited <a href="/pages/configuration/redirects/">supports for advanced redirects</a>. In the case where you have over 2000 static and/or 100 dynamic redirects rules, it is recommended to use <a href="/rules/url-forwarding/bulk-redirects/create-dashboard/">Bulk Redirects</a>.</p>
<p>Your header files can also be moved into a <code>_headers</code> folder in your publish directory. It is important to note that custom headers defined in the <code>_headers</code> file are not currently applied to responses from functions, even if the function route matches the URL pattern. To learn more about how to <a href="/pages/configuration/headers/">handle headers, refer to Headers</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10882.md")
</aside>
<h2 id="forms">Forms</h2>
<p>In your form component, remove the <code>data-netlify = &quot;true&quot;</code> attribute or the Netlify attribute from the <code>&lt;form&gt;</code> tag. You can now put your form logic as a Pages Function and collect the entries to a database or an Airtable. Refer to the <a href="/pages/tutorials/forms/">handling form submissions with Pages Functions</a> tutorial for more information.</p>
<h2 id="serverless-functions">Serverless functions</h2>
<p>Netlify functions and Pages Functions share the same filesystem convention using a <code>functions</code> directory in the base of your project to handle your serverless functions. However, the syntax and how the functions are deployed differs. Pages Functions run on Cloudflare Workers, which by default operate on the Cloudflare global network, and do not require any additional code or configuration for deployment.</p>
<p>Cloudflare Pages Functions also provides middleware that can handle any logic you need to run before and/or after your function route handler.</p>
<h3 id="functions-syntax">Functions syntax</h3>
<p>Netlify functions export an async event handler that accepts an event and a context as arguments. In the case of Pages Functions, you will have to export a single <code>onRequest</code> function that accepts a <code>context</code> object. The <code>context</code> object contains all the information for the request such as <code>request</code>, <code>env</code>, <code>params</code>, and returns a new Response. Learn more about <a href="/pages/functions/get-started/">writing your first function</a></p>
<p>Hello World with Netlify functions:</p>
<pre><code class="language-js">exports.handler = async function (event, context) {&#10;	return {&#10;		statusCode: 200,&#10;		body: JSON.stringify({ message: &quot;Hello World&quot; }),&#10;	};&#10;};&#10;</code></pre>
<p>Hello World with Pages Functions:</p>
<pre><code class="language-js">export async function onRequestPost(request) {&#10;	return new Response(`Hello world`);&#10;}&#10;</code></pre>
<h2 id="other-netlify-configurations">Other Netlify configurations</h2>
<p>Your <code>netlify.toml</code> file might have other configurations that are supported by Pages, such as, preview deployment, specifying publish directory, and plugins. You can delete the file after migrating your configurations.</p>
<h2 id="access-management">Access management</h2>
<p>You can migrate your access management to <a href="/cloudflare-one/">Cloudflare Zero Trust</a> which allows you to manage user authentication for your applications, event logging and requests.</p>
<h2 id="creating-a-new-pages-project">Creating a new Pages project</h2>
<p>Once you have found your build directory and build command, you can move your project to Cloudflare Pages.</p>
<p>The <a href="/pages/get-started/">Get started guide</a> will instruct you how to add your GitHub project to Cloudflare Pages.</p>
<p>If you choose to use a custom domain for your Pages, you can set it to the same custom domain as your currently deployed Netlify application. To assign a custom domain to your Pages project, refer to <a href="/pages/configuration/custom-domains/">Custom Domains</a>.</p>
<h2 id="cleaning-up-your-old-application-and-assigning-the-domain">Cleaning up your old application and assigning the domain</h2>
<p>In the Cloudflare dashboard, go to the <strong>DNS Records</strong> page.</p>
<div class="nb-dash-button"></div>
<p>Review that you have updated the CNAME record for your domain from Netlify to Cloudflare Pages. With your DNS record updated, requests will go to your Pages application.</p>
<p>In <strong>DNS</strong>, your record's <strong>Content</strong> should be your <code>&lt;SUBDOMAIN&gt;.pages.dev</code> subdomain.</p>
<p>With the above steps completed, you have successfully migrated your Netlify project to Cloudflare Pages.</p>
