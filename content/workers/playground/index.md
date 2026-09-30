<aside class="nb-aside note">
<h3 class="nb-aside-title" id="browser-support">Browser support</h3>
@markup("md", "content/.markup/bodies/28.md")
</aside>
<p>The quickest way to experiment with Cloudflare Workers is in the <a href="https://workers.cloudflare.com/playground">Playground</a>. It does not require any setup or authentication. The Playground is a sandbox which gives you an instant way to preview and test a Worker directly in the browser.</p>
<p>The Playground uses the same editor as the authenticated experience. The Playground provides the ability to <a href="#share">share</a> the code you write as well as <a href="#deploy">deploy</a> it instantly to Cloudflare's global network. This way, you can try new things out and deploy them when you are ready.</p>
<p><a class="nb-link-button" href="https://workers.cloudflare.com/playground">Launch the Playground</a></p>
<h2 id="hello-cloudflare-workers">Hello Cloudflare Workers</h2>
<p>When you arrive in the Playground, you will see this default code:</p>
<pre><code class="language-js">import welcome from &quot;welcome.html&quot;;&#10;&#10;/**&#10; &#42; @typedef {Object} Env&#10; &#42;/&#10;&#10;export default {&#10;	/**&#10;	 &#42; @param {Request} request&#10;	 &#42; @param {Env} env&#10;	 &#42; @param {ExecutionContext} ctx&#10;	 &#42; @returns {Response}&#10;	 &#42;/&#10;	fetch(request, env, ctx) {&#10;		console.log(&quot;Hello Cloudflare Workers!&quot;);&#10;&#10;		return new Response(welcome, {&#10;			headers: {&#10;				&quot;content-type&quot;: &quot;text/html&quot;,&#10;			},&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>This is an example of a multi-module Worker that is receiving a <a href="/workers/runtime-apis/request/">request</a>, logging a message to the console, and then returning a <a href="/workers/runtime-apis/response/">response</a> body containing the content from <code>welcome.html</code>.</p>
<p>Refer to the <a href="/workers/runtime-apis/handlers/fetch/">Fetch handler documentation</a> to learn more.</p>
<h2 id="use-the-playground">Use the Playground</h2>
<p>As you edit the default code, the Worker will auto-update such that the preview on the right shows your Worker running just as it would in a browser. If your Worker uses URL paths, you can enter those in the input field on the right to navigate to them. The Playground provides type-checking via JSDoc comments and <a href="https://www.npmjs.com/package/@cloudflare/workers-types"><code>workers-types</code></a>. The Playground also provides pretty error pages in the event of application errors.</p>
<p>To test a raw HTTP request (for example, to test a <code>POST</code> request), go to the <strong>HTTP</strong> tab and select <strong>Send</strong>. You can add and edit headers via this panel, as well as edit the body of a request.</p>
<h2 id="log-viewer">Log viewer</h2>
<p>The Playground and the quick editor in the Workers dashboard include a lightweight log viewer at the bottom of the preview panel. The log viewer displays the output of any calls to <code>console.log</code> made during preview runs.</p>
<p>The log viewer supports the following:</p>
<ul>
<li>Logging primitive values, objects, and arrays.</li>
<li>Clearing the log output between runs.</li>
</ul>
<p>At this time, the log viewer does not support logging class instances or their properties (for example, <code>request.url</code>).</p>
<p>If you need a more complete development experience with full debugging capabilities, you can use <a href="/workers/wrangler/install-and-update/">Wrangler</a> locally. To clone an existing Worker from your dashboard for local development, sign up and use the <a href="/workers/wrangler/commands/general/#init"><code>wrangler init --from-dash</code></a> command once your worker is deployed.</p>
<h2 id="share">Share</h2>
<p>To share what you have created, select <strong>Copy Link</strong> in the top right of the screen. This will copy a unique URL to your clipboard that you can share with anyone. These links do not expire, so you can bookmark your creation and share it at any time. Users that open a shared link will see the Playground with the shared code and preview.</p>
<h2 id="deploy">Deploy</h2>
<p>You can deploy a Worker from the Playground. If you are already logged in, you can review the Worker before deploying. Otherwise, you will be taken through the first-time user onboarding flow before you can review and deploy.</p>
<p>Once deployed, your Worker will get its own unique URL and be available almost instantly on Cloudflare's global network. From here, you can add <a href="/workers/configuration/routing/custom-domains/">Custom Domains</a>, <a href="/workers/platform/storage-options/">storage resources</a>, and more.</p>
