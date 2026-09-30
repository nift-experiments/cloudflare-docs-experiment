<p>In this tutorial, you will deploy a serverless, real-time chat application that runs using <a href="/durable-objects/">Durable Objects</a>.</p>
<p>This chat application uses a Durable Object to control each chat room. Users connect to the Object using WebSockets. Messages from one user are broadcast to all the other users. The chat history is also stored in durable storage. Real-time messages are relayed directly from one user to others without going through the storage layer.</p>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="clone-the-chat-application-repository">Clone the chat application repository</h2>
<p>Open your terminal and clone the <a href="https://github.com/cloudflare/workers-chat-demo">workers-chat-demo</a> repository:</p>
<pre><code class="language-sh">git clone https://github.com/cloudflare/workers-chat-demo.git&#10;</code></pre>
<h2 id="authenticate-wrangler">Authenticate Wrangler</h2>
<p>After you have cloned the repository, authenticate Wrangler by running:</p>
<pre><code class="language-sh">npx wrangler login&#10;</code></pre>
<h2 id="deploy-your-project">Deploy your project</h2>
<p>When you are ready to deploy your application, run:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your application will be deployed to your <code>*.workers.dev</code> subdomain.</p>
<p>To deploy your application to a custom domain within the Cloudflare dashboard, go to your Worker &gt; <strong>Triggers</strong> &gt; <strong>Add Custom Domain</strong>.</p>
<p>To deploy your application to a custom domain using Wrangler, open your project's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>To configure a route in your Wrangler configuration file, add the following to your environment:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16075.md")
</div>
<p>If you have specified your zone ID in the environment of your Wrangler configuration file, you will not need to write it again in object form.</p>
<p>To configure a subdomain in your Wrangler configuration file, add the following to your environment:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16076.md")
</div>
<p>To test your live application:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker &gt; <strong>Triggers</strong> &gt; <strong>Routes</strong> &gt; Select the <code>edge-chat-demo.&lt;SUBDOMAIN&gt;.workers.dev</code> route.</li>
<li>Enter a name in the <strong>your name</strong> field.</li>
<li>Choose whether to enter a public room or create a private room.</li>
<li>Send the link to other participants. You will be able to view room participants on the right side of the screen.</li>
</ol>
<h2 id="uninstall-your-application">Uninstall your application</h2>
<p>To uninstall your chat application, modify your Wrangler file to remove the <code>durable_objects</code> bindings and add a <code>deleted_classes</code> migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16077.md")
</div>
<p>Then run <code>npx wrangler deploy</code>.</p>
<p>To delete your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Select <strong>Manage Service</strong> &gt; <strong>Delete</strong>. For complete instructions on set up and deletion, refer to the <code>README.md</code> in your cloned repository.</li>
</ol>
<p>By completing this tutorial, you have deployed a real-time chat application with Durable Objects and Cloudflare Workers.</p>
<h2 id="related-resources">Related resources</h2>
<p>Continue building with other Cloudflare Workers tutorials below.</p>
<ul>
<li><a href="/workers/tutorials/build-a-slackbot/">Build a Slackbot</a></li>
<li><a href="/workers/tutorials/github-sms-notifications-using-twilio/">Create SMS notifications for your GitHub repository using Twilio</a></li>
<li><a href="/workers/tutorials/build-a-qr-code-generator/">Build a QR code generator</a></li>
</ul>
