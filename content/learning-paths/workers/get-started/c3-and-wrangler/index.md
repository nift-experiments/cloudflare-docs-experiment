<p>Before deploying your first Worker, learn about the CLI tools you will use to build and deploy your Worker project.</p>
<h2 id="cloudflare-dashboard">Cloudflare dashboard</h2>
<p>You can build and develop your Worker on the Cloudflare dashboard, without needing to install and use C3 and Wrangler. Continue to the next page to get started with Workers on the Cloudflare dashboard.</p>
<h2 id="cli">CLI</h2>
<p>The Cloudflare Developer Platform ecosystem has two command-line interfaces (CLI):</p>
<ul>
<li>C3: To create new projects.</li>
<li>Wrangler: To build and deploy your projects.</li>
</ul>
<h2 id="c3">C3</h2>
<p><a href="/pages/get-started/c3/">C3</a> (<code>create-cloudflare</code> CLI) is a command-line tool designed to help you set up and deploy new applications to Cloudflare. In addition to speed, it leverages officially developed templates for Workers and framework-specific setup guides to ensure each new application that you set up follows Cloudflare and any third-party best practices for deployment on the Cloudflare network.</p>
<p>You will use C3 for new project creation.</p>
<h2 id="wrangler">Wrangler</h2>
<p><a href="/workers/wrangler/">Wrangler</a> is a command-line tool for building with Cloudflare developer products.</p>
<p>With Wrangler, you can <a href="/workers/wrangler/commands/general/#dev">develop</a> your Worker locally and remotely, <a href="/workers/wrangler/commands/general/#rollback">roll back</a> to a previous deployment of your Worker, <a href="/workers/wrangler/commands/general/#delete">delete</a> a Worker and its bound Developer Platform resources, and more. Refer to <a href="/workers/wrangler/commands/">Wrangler Commands</a> to view the full reference of Wrangler commands.</p>
<p>When you run C3 to create your project, C3 will install the latest version of Wrangler and you do not need to install Wrangler again. You can <a href="/workers/wrangler/install-and-update/#update-wrangler">update Wrangler</a> to a newer version in your project to access new Wrangler capabilities and features.</p>
<h2 id="source-of-truth">Source of truth</h2>
<p>If you are building your Worker on the Cloudflare dashboard, you will set up your project configuration (such as environment variables, bindings, and routes) through the dashboard. If you are building your project programmatically using C3 and Wrangler, you will rely on a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to configure your Worker.</p>
<p>Cloudflare recommends choosing and using one <a href="/workers/wrangler/configuration/#source-of-truth">source of truth</a>, the dashboard or the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, to avoid errors in your project.</p>
<h2 id="summary">Summary</h2>
<p>By reading this page, you have learned:</p>
<ul>
<li>How to use C3 to create new Workers and Pages projects.</li>
<li>How to use Wrangler to develop, configure, and delete your projects.</li>
</ul>
<p>In the next section, you will learn more about the Cloudflare dashboard before moving on to deploy your first Worker.</p>
