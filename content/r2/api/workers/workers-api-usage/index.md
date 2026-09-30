<h2 id="1-create-a-new-application-with-c3"><ol>
<li>Create a new application with C3</li>
</ol></h2>
<p>C3 (<code>create-cloudflare-cli</code>) is a command-line tool designed to help you set up and deploy Workers &amp; Pages applications to Cloudflare as fast as possible.</p>
<p>To get started, open a terminal window and run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- r2-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- r2-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare r2-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare r2-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest r2-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest r2-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Then, move into your newly created directory:</p>
<pre><code class="language-sh">cd r2-worker&#10;</code></pre>
<h2 id="2-create-your-bucket"><ol start="2">
<li>Create your bucket</li>
</ol></h2>
<p>Create your bucket by running:</p>
<pre><code class="language-sh">npx wrangler r2 bucket create &lt;YOUR_BUCKET_NAME&gt;&#10;</code></pre>
<p>To check that your bucket was created, run:</p>
<pre><code class="language-sh">npx wrangler r2 bucket list&#10;</code></pre>
<p>After running the <code>list</code> command, you will see all bucket names, including the one you have just created.</p>
<h2 id="3-bind-your-bucket-to-a-worker"><ol start="3">
<li>Bind your bucket to a Worker</li>
</ol></h2>
<p>You will need to bind your bucket to a Worker.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bindings">Bindings</h3>
@markup("md", "content/.markup/bodies/11508.md")
</aside>
<p>To bind your R2 bucket to your Worker, add the following to your Wrangler file. Update the <code>binding</code> property to a valid JavaScript variable identifier and <code>bucket_name</code> to the <code>&lt;YOUR_BUCKET_NAME&gt;</code> you used to create your bucket in <a href="#2-create-your-bucket">step 2</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11509.md")
</div>
<p>For more detailed information on configuring your Worker (for example, if you are using <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdictions</a>), refer to the <a href="/workers/wrangler/configuration/">Wrangler Configuration documentation</a>.</p>
<h2 id="4-access-your-r2-bucket-from-your-worker"><ol start="4">
<li>Access your R2 bucket from your Worker</li>
</ol></h2>
<p>Within your Worker code, your bucket is now available under the <code>MY_BUCKET</code> variable and you can begin interacting with it.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="local-development-mode-in-wrangler">Local Development mode in Wrangler</h3>
@markup("md", "content/.markup/bodies/11507.md")
</aside>
<p>An R2 bucket is able to READ, LIST, WRITE, and DELETE objects. You can see an example of all operations below using the Module Worker syntax. Add the following snippet into your project's <code>index.js</code> file:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11513.md")
</div></div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="prevent-potential-errors-when-accessing-request-body">Prevent potential errors when accessing request.body</h3>
@markup("md", "content/.markup/bodies/11506.md")
</aside>
<h2 id="5-bucket-access-and-privacy"><ol start="5">
<li>Bucket access and privacy</li>
</ol></h2>
<p>With the above code added to your Worker, every incoming request has the ability to interact with your bucket. This means your bucket is publicly exposed and its contents can be accessed and modified by undesired actors.</p>
<p>You must now define authorization logic to determine who can perform what actions to your bucket. This logic lives within your Worker's code, as it is your application's job to determine user privileges. The following is a short list of resources related to access and authorization practices:</p>
<ol>
<li><a href="/workers/examples/basic-auth/">Basic Authentication</a>: Shows how to restrict access using the HTTP Basic schema.</li>
<li><a href="/workers/examples/auth-with-headers/">Using Custom Headers</a>: Allow or deny a request based on a known pre-shared key in a header.</li>
</ol>
<p>Continuing with your newly created bucket and Worker, you will need to protect all bucket operations.</p>
<p>For <code>PUT</code> and <code>DELETE</code> requests, you will make use of a new <code>AUTH_KEY_SECRET</code> environment variable, which you will define later as a Wrangler secret.</p>
<p>For <code>GET</code> requests, you will ensure that only a specific file can be requested. All of this custom logic occurs inside of an <code>authorizeRequest</code> function, with the <code>hasValidHeader</code> function handling the custom header logic. If all validation passes, then the operation is allowed.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11516.md")
</div></div>
<p>For this to work, you need to create a secret via Wrangler:</p>
<pre><code class="language-sh">npx wrangler secret put AUTH_KEY_SECRET&#10;</code></pre>
<p>This command will prompt you to enter a secret in your terminal:</p>
<pre><code class="language-sh">npx wrangler secret put AUTH_KEY_SECRET&#10;</code></pre>
<pre><code class="language-sh">Enter the secret text you&#x27;d like assigned to the variable AUTH_KEY_SECRET on the script named &lt;YOUR_WORKER_NAME&gt;:&#10;&#42;********&#10;🌀  Creating the secret for script name &lt;YOUR_WORKER_NAME&gt;&#10;✨  Success! Uploaded secret AUTH_KEY_SECRET.&#10;</code></pre>
<p>This secret is now available as <code>AUTH_KEY_SECRET</code> on the <code>env</code> parameter in your Worker.</p>
<h2 id="6-deploy-your-worker"><ol start="6">
<li>Deploy your Worker</li>
</ol></h2>
<p>With your Worker and bucket set up, run the <code>npx wrangler deploy</code> <a href="/workers/wrangler/commands/general/#deploy">command</a> to deploy to Cloudflare's global network:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>You can verify your authorization logic is working through the following commands, using your deployed Worker endpoint:</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11505.md")
</aside>
<pre><code class="language-sh">&#35; Attempt to write an object without providing the &quot;X-Custom-Auth-Key&quot; header&#10;curl https://your-worker.dev/cat-pic.jpg -X PUT --data-binary &#x27;test&#x27;&#10;&#35;=&gt; Forbidden&#10;&#35; Expected because header was missing&#10;&#10;&#35; Attempt to write an object with the wrong &quot;X-Custom-Auth-Key&quot; header value&#10;curl https://your-worker.dev/cat-pic.jpg -X PUT --header &quot;X-Custom-Auth-Key: hotdog&quot; --data-binary &#x27;test&#x27;&#10;&#35;=&gt; Forbidden&#10;&#35; Expected because header value did not match the AUTH_KEY_SECRET value&#10;&#10;&#35; Attempt to write an object with the correct &quot;X-Custom-Auth-Key&quot; header value&#10;&#35; Note: Assume that &quot;*********&quot; is the value of your AUTH_KEY_SECRET Wrangler secret&#10;curl https://your-worker.dev/cat-pic.jpg -X PUT --header &quot;X-Custom-Auth-Key: *********&quot; --data-binary &#x27;test&#x27;&#10;&#35;=&gt; Put cat-pic.jpg successfully!&#10;&#10;&#35; Attempt to read object called &quot;foo&quot;&#10;curl https://your-worker.dev/foo&#10;&#35;=&gt; Forbidden&#10;&#35; Expected because &quot;foo&quot; is not in the ALLOW_LIST&#10;&#10;&#35; Attempt to read an object called &quot;cat-pic.jpg&quot;&#10;curl https://your-worker.dev/cat-pic.jpg&#10;&#35;=&gt; test&#10;&#35; Note: This is the value that was successfully PUT above&#10;</code></pre>
<p>By completing this guide, you have successfully installed Wrangler and deployed your R2 bucket to Cloudflare.</p>
<h2 id="related-resources">Related resources</h2>
<ol>
<li><a href="/workers/tutorials/">Workers Tutorials</a></li>
<li><a href="/workers/examples/">Workers Examples</a></li>
</ol>
