<p>Follow this guide to create a Workers application using the Cloudflare dashboard.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="try-the-playground">Try the Playground</h3>
@markup("md", "content/.markup/bodies/16303.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p><a href="/fundamentals/account/create-account/">Create a Cloudflare account</a>, if you have not already.</p>
<h2 id="setup">Setup</h2>
<p>To get started with a new Workers application:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Create application</strong>. From here, you can:
<ul>
<li>Select from the gallery of production-ready templates</li>
<li>Import an existing Git repository on your own account</li>
<li>Let Cloudflare clone and bootstrap a public repository containing a Workers application.</li>
</ul>
</li>
<li>Once you have connected to your chosen <a href="/workers/ci-cd/builds/git-integration/github-integration/">Git provider</a>, configure your project and select <strong>Deploy</strong>.</li>
<li>Cloudflare will kick off a new build and deployment. Once deployed, preview your Worker at its provided <code>workers.dev</code> subdomain.</li>
</ol>
<h2 id="continue-development">Continue development</h2>
Applications started in the dashboard are set up with Git to help kickstart your development workflow. To continue developing on your repository, you can run:
<pre><code class="language-bash">&#35; clone your repository locally&#10;git clone &lt;git repo URL&gt;&#10;&#10;&#35; make sure you are in the root directory&#10;cd &lt;directory&gt;&#10;</code></pre>
<p>Now, you can preview and test your changes by <a href="/workers/local-development/">running Wrangler in your local development environment</a>. Once you are ready to deploy you can run:</p>
<pre><code class="language-bash">&#35; adds the files to git tracking&#10;git add .&#10;&#10;&#35; commits the changes&#10;git commit -m &quot;your message&quot;&#10;&#10;&#35; push the changes to your Git provider&#10;git push origin main&#10;</code></pre>
<p>To do more:</p>
<ul>
<li>Review our <a href="/workers/examples/">Examples</a> and <a href="/workers/tutorials/">Tutorials</a> for inspiration.</li>
<li>Set up <a href="/workers/runtime-apis/bindings/">bindings</a> to allow your Worker to interact with other resources and unlock new functionality.</li>
<li>Learn how to <a href="/workers/testing/">test and debug</a> your Workers.</li>
<li>Read about <a href="/workers/platform/">Workers limits and pricing</a>.</li>
</ul>
