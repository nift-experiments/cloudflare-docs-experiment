<p>In this tutorial, you will learn how to migrate an existing Firebase application to Cloudflare Pages. You should already have an existing project deployed on Firebase that you would like to host on Cloudflare Pages.</p>
<h2 id="finding-your-build-command-and-build-directory">Finding your build command and build directory</h2>
<p>To move your application to Cloudflare Pages, you will need to find your build command and build directory.</p>
<p>You will use these to tell Cloudflare Pages how to deploy your project. If you have been deploying manually from your local machine using the <code>firebase</code> command-line tool, the <code>firebase.json</code> configuration file should include a <code>public</code> key that will be your build directory:</p>
<pre><code class="language-json">{&#10;	&quot;public&quot;: &quot;public&quot;&#10;}&#10;</code></pre>
<p>Firebase Hosting does not ask for your build command, so if you are running a standard JavaScript set up, you will probably be using <code>npm build</code> or a command specific to the framework or tool you are using (for example, <code>ng build</code>).</p>
<p>After you have found your build directory and build command, you can move your project to Cloudflare Pages.</p>
<h2 id="creating-a-new-pages-project">Creating a new Pages project</h2>
<p>If you have not pushed your static site to GitHub before, you should do so before continuing. This will also give you access to features like automatic deployments, and <a href="/pages/configuration/preview-deployments/">deployment previews</a>.</p>
<p>You can create a new repository by visiting <a href="https://repo.new">repo.new</a> and following the instructions to push your project up to GitHub.</p>
<p>Use the <a href="/pages/get-started/">Get started guide</a> to add your project to Cloudflare Pages, using the <strong>build command</strong> and <strong>build directory</strong> that you saved earlier.</p>
<h2 id="cleaning-up-your-old-application-and-assigning-the-domain">Cleaning up your old application and assigning the domain</h2>
<p>Once you have deployed your application, go to the Firebase dashboard and remove your old Firebase project. In your Cloudflare DNS settings for your domain, make sure to update the CNAME record for your domain from Firebase to Cloudflare Pages.</p>
<p>By completing this guide, you have successfully migrated your Firebase project to Cloudflare Pages.</p>
