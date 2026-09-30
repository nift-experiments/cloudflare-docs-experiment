<p>Advanced mode allows you to develop your Pages Functions with a <code>_worker.js</code> file rather than the <code>/functions</code> directory.</p>
<p>In some cases, Pages Functions' built-in file path based routing and middleware system is not desirable for existing applications. You may have a Worker that is complex and difficult to splice up into Pages' file-based routing system. For these cases, Pages offers the ability to define a <code>_worker.js</code> file in the output directory of your Pages project.</p>
<p>When using a <code>_worker.js</code> file, the entire <code>/functions</code> directory is ignored, including its routing and middleware characteristics. Instead, the <code>_worker.js</code> file is deployed and must be written using the <a href="/workers/runtime-apis/handlers/fetch/">Module Worker syntax</a>. If you have never used Module syntax, refer to the <a href="https://blog.cloudflare.com/workers-javascript-modules/">JavaScript modules blog post</a> to learn more. Using Module syntax enables JavaScript frameworks to generate a Worker as part of the Pages output directory contents.</p>
<h2 id="set-up-a-function">Set up a Function</h2>
<p>In advanced mode, your Function will assume full control of all incoming HTTP requests to your domain. Your Function is required to make or forward requests to your project's static assets. Failure to do so will result in broken or unwanted behavior. Your Function must be written in Module syntax.</p>
<p>After making a <code>_worker.js</code> file in your output directory, add the following code snippet:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11007.md")
</div></div>
<p>In the above code, you have configured your Function to return a response under all requests headed for <code>/api/</code>. Otherwise, your Function will fallback to returning static assets.</p>
<ul>
<li>The <code>env.ASSETS.fetch()</code> function will allow you to return assets on a given request.</li>
<li><code>env</code> is the object that contains your environment variables and bindings.</li>
<li><code>ASSETS</code> is a default Function binding that allows communication between your Function and Pages' asset serving resource.</li>
<li><code>fetch()</code> calls to Pages' asset-serving resource and serves the requested asset.</li>
</ul>
<h2 id="migrate-from-workers">Migrate from Workers</h2>
<p>To migrate an existing Worker to your Pages project, copy your Worker code and paste it into your new <code>_worker.js</code> file. Then handle static assets by adding the following code snippet to <code>_worker.js</code>:</p>
<pre><code class="language-ts">return env.ASSETS.fetch(request);&#10;</code></pre>
<h2 id="deploy-your-function">Deploy your Function</h2>
<p>After you have set up a new Function or migrated your Worker to <code>_worker.js</code>, make sure your <code>_worker.js</code> file is placed in your Pages' project output directory. Deploy your project through your Git integration for advanced mode to take effect.</p>
