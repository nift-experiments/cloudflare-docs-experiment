<p>The following methods can be used to configure your Pages Function.</p>
<h2 id="methods">Methods</h2>
<h3 id="onrequests"><code>onRequests</code></h3>
<p>The <code>onRequest</code> method will be called unless a more specific <code>onRequestVerb</code> method is exported. For example, if both <code>onRequest</code> and <code>onRequestGet</code> are exported, only <code>onRequestGet</code> will be called for <code>GET</code> requests.</p>
<ul>
<li>
<p><code>onRequest(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all requests no matter what the request method is, as long as no specific request verb (like one of the methods below) is exported.</li>
</ul>
</li>
<li>
<p><code>onRequestGet(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>GET</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestPost(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>POST</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestPatch(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>PATCH</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestPut(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>PUT</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestDelete(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>DELETE</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestHead(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>HEAD</code> requests.</li>
</ul>
</li>
<li>
<p><code>onRequestOptions(context<a href="#eventcontext">EventContext</a>)</code> Response | Promise&lt;Response&gt;</p>
<ul>
<li>This function will be invoked on all <code>OPTIONS</code> requests.</li>
</ul>
</li>
</ul>
<h3 id="env-assets-fetch"><code>env.ASSETS.fetch()</code></h3>
<p>The <code>env.ASSETS.fetch()</code> function allows you to fetch a static asset from your Pages project.</p>
<p>You can pass a <a href="/workers/runtime-apis/request/">Request object</a>, URL string, or URL object to <code>env.ASSETS.fetch()</code> function. The URL must be to the pretty path, not directly to the asset. For example, if you had the path <code>/users/index.html</code>, you will request <code>/users/</code> instead of <code>/users/index.html</code>. This method call will run the header and redirect rules, modifying the response that is returned.</p>
<h2 id="types">Types</h2>
<h3 id="eventcontext"><code>EventContext</code></h3>
<p>The following are the properties on the <code>context</code> object which are passed through on the <code>onRequest</code> methods:</p>
<ul>
<li>
<p><code>request</code> <a href="/workers/runtime-apis/request/">Request</a></p>
<p>This is the incoming <a href="/workers/runtime-apis/request/">Request</a>.</p>
</li>
<li>
<p><code>functionPath</code> string</p>
<p>This is the path of the request.</p>
</li>
<li>
<p><code>waitUntil(promisePromise&lt;any&gt;)</code> void</p>
<p>Refer to <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code> documentation</a> for more information.</p>
</li>
<li>
<p><code>passThroughOnException()</code> void</p>
<p>Refer to <a href="/workers/runtime-apis/context/#passthroughonexception"><code>passThroughOnException</code> documentation</a> for more information. Note that this will not work on an <a href="/pages/functions/advanced-mode/">advanced mode project</a>.</p>
</li>
<li>
<p><code>next(input?Request | string, init?RequestInit)</code> Promise&lt;Response&gt;</p>
<p>Passes the request through to the next Function or to the asset server if no other Function is available.</p>
</li>
<li>
<p><code>env</code> <a href="#envwithfetch">EnvWithFetch</a></p>
</li>
<li>
<p><code>params</code> Params&lt;P&gt;</p>
<p>Holds the values from <a href="/pages/functions/routing/#dynamic-routes">dynamic routing</a>.</p>
<p>In the following example, you have a dynamic path that is <code>/users/[user].js</code>. When you visit the site on <code>/users/nevi</code> the <code>params</code> object would look like:</p>
</li>
</ul>
<pre><code class="language-js">{&#10;	user: &quot;nevi&quot;;&#10;}&#10;</code></pre>
<p>This allows you fetch the dynamic value from the path:</p>
<pre><code class="language-js">export function onRequest(context) {&#10;	return new Response(`Hello ${context.params.user}`);&#10;}&#10;</code></pre>
<p>Which would return <code>&quot;Hello nevi&quot;</code>.</p>
<ul>
<li><code>data</code> Data</li>
</ul>
<h3 id="envwithfetch"><code>EnvWithFetch</code></h3>
<p>Holds the environment variables, secrets, and bindings for a Function. This also holds the <code>ASSETS</code> binding which is how you can fallback to the asset-serving behavior.</p>
