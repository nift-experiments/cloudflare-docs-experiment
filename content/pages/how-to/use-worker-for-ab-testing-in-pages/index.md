<p>In this guide, you will learn how to use <a href="/pages/functions/">Pages Functions</a> for A/B testing in your Pages projects. A/B testing is a user experience research methodology applied when comparing two or more versions of a web page or application. With A/B testing, you can serve two or more versions of a webpage to users and divide traffic to your site.</p>
<h2 id="overview">Overview</h2>
<p>Configuring different versions of your application for A/B testing will be unique to your specific use case. For all developers, A/B testing setup can be simplified into a few helpful principles.</p>
<p>Depending on the number of application versions you have (this guide uses two), you can assign your users into experimental groups. The experimental groups in this guide are the base route <code>/</code> and the test route <code>/test</code>.</p>
<p>To ensure that a user remains in the group you have given, you will set and store a cookie in the browser and depending on the cookie value you have set, the corresponding route will be served.</p>
<h2 id="set-up-your-pages-function">Set up your Pages Function</h2>
<p>In your project, you can handle the logic for A/B testing using <a href="/pages/functions/">Pages Functions</a>. Pages Functions allows you to handle server logic from within your Pages project.</p>
<p>To begin:</p>
<ol>
<li>Go to your Pages project directory on your local machine.</li>
<li>Create a <code>/functions</code> directory. Your application server logic will live in the <code>/functions</code> directory.</li>
</ol>
<h2 id="add-middleware-logic">Add middleware logic</h2>
<p>Pages Functions have utility functions that can reuse chunks of logic which are executed before and/or after route handlers. These are called <a href="/pages/functions/middleware/">middleware</a>. Following this guide, middleware will allow you to intercept requests to your Pages project before they reach your site.</p>
<p>In your <code>/functions</code> directory, create a <code>_middleware.js</code> file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10887.md")
</aside>
<p>Following the Functions naming convention, the <code>_middleware.js</code> file exports a single async <code>onRequest</code> function that accepts a <code>request</code>, <code>env</code> and <code>next</code> as an argument.</p>
<pre><code class="language-js">const abTest = async ({ request, next, env }) =&gt; {&#10;	/*&#10;  Todo:&#10;  1. Conditional statements to check for the cookie&#10;  2. Assign cookies based on percentage, then serve&#10;  &#42;/&#10;};&#10;&#10;export const onRequest = [abTest];&#10;</code></pre>
<p>To set the cookie, create the <code>cookieName</code> variable and assign any value. Then create the <code>newHomepagePathName</code> variable and assign it <code>/test</code>:</p>
<pre><code class="language-js">const cookieName = &quot;ab-test-cookie&quot;;&#10;const newHomepagePathName = &quot;/test&quot;;&#10;&#10;const abTest = async ({ request, next, env }) =&gt; {&#10;	/*&#10;  Todo:&#10;  1. Conditional statements to check for the cookie&#10;  2. Assign cookie based on percentage then serve&#10;  &#42;/&#10;};&#10;&#10;export const onRequest = [abTest];&#10;</code></pre>
<h2 id="set-up-conditional-logic">Set up conditional logic</h2>
<p>Based on the URL pathname, check that the cookie value is equal to <code>new</code>. If the value is <code>new</code>, then <code>newHomepagePathName</code> will be served.</p>
<pre><code class="language-js">const cookieName = &quot;ab-test-cookie&quot;;&#10;const newHomepagePathName = &quot;/test&quot;;&#10;&#10;const abTest = async ({ request, next, env }) =&gt; {&#10;	/*&#10;  Todo:&#10;  1. Assign cookies based on randomly generated percentage, then serve&#10;  &#42;/&#10;&#10;	const url = new URL(request.url);&#10;	if (url.pathname === &quot;/&quot;) {&#10;		// if cookie ab-test-cookie=new then change the request to go to /test&#10;		// if no cookie set, pass x% of traffic and set a cookie value to &quot;current&quot; or &quot;new&quot;&#10;&#10;		let cookie = request.headers.get(&quot;cookie&quot;);&#10;		// is cookie set?&#10;		if (cookie &amp;&amp; cookie.includes(`${cookieName}=new`)) {&#10;			// Change the request to go to /test (as set in the newHomepagePathName variable)&#10;			url.pathname = newHomepagePathName;&#10;			return env.ASSETS.fetch(url);&#10;		}&#10;	}&#10;};&#10;&#10;export const onRequest = [abTest];&#10;</code></pre>
<p>If the cookie value is not present, you will have to assign one. Generate a percentage (from 0-99) by using: <code>Math.floor(Math.random() * 100)</code>. Your default cookie version is given a value of <code>current</code>.</p>
<p>If the percentage of the number generated is lower than <code>50</code>, you will assign the cookie version to <code>new</code>. Based on the percentage randomly generated, you will set the cookie and serve the assets. After the conditional block, pass the request to <code>next()</code>. This will pass the request to Pages. This will result in 50% of users getting the <code>/test</code> homepage.</p>
<p>The <code>env.ASSETS.fetch()</code> function will allow you to send the user to a modified path which is defined through the <code>url</code> parameter. <code>env</code> is the object that contains your environment variables and bindings. <code>ASSETS</code> is a default Function binding that allows communication between your Function and Pages' asset serving resource. <code>fetch()</code> calls to the Pages asset-serving resource and returns the asset (<code>/test</code> homepage) to your website's visitor.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="binding">Binding</h3>
@markup("md", "content/.markup/bodies/10886.md")
</aside>
<pre><code class="language-js">const cookieName = &quot;ab-test-cookie&quot;;&#10;const newHomepagePathName = &quot;/test&quot;;&#10;&#10;const abTest = async (context) =&gt; {&#10;	const url = new URL(context.request.url);&#10;	// if homepage&#10;	if (url.pathname === &quot;/&quot;) {&#10;		// if cookie ab-test-cookie=new then change the request to go to /test&#10;		// if no cookie set, pass x% of traffic and set a cookie value to &quot;current&quot; or &quot;new&quot;&#10;&#10;		let cookie = request.headers.get(&quot;cookie&quot;);&#10;		// is cookie set?&#10;		if (cookie &amp;&amp; cookie.includes(`${cookieName}=new`)) {&#10;			// pass the request to /test&#10;			url.pathname = newHomepagePathName;&#10;			return context.env.ASSETS.fetch(url);&#10;		} else {&#10;			const percentage = Math.floor(Math.random() * 100);&#10;			let version = &quot;current&quot;; // default version&#10;			// change pathname and version name for 50% of traffic&#10;			if (percentage &lt; 50) {&#10;				url.pathname = newHomepagePathName;&#10;				version = &quot;new&quot;;&#10;			}&#10;			// get the static file from ASSETS, and attach a cookie&#10;			const asset = await context.env.ASSETS.fetch(url);&#10;			let response = new Response(asset.body, asset);&#10;			response.headers.append(&quot;Set-Cookie&quot;, `${cookieName}=${version}; path=/`);&#10;			return response;&#10;		}&#10;	}&#10;	return context.next();&#10;};&#10;&#10;export const onRequest = [abTest];&#10;</code></pre>
<h2 id="deploy-to-cloudflare-pages">Deploy to Cloudflare Pages</h2>
<p>After you have set up your <code>functions/_middleware.js</code> file in your project you are ready to deploy with Pages. Push your project changes to GitHub/GitLab.</p>
<p>After you have deployed your application, review your middleware Function:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project > **Settings** > **Functions** > **Configuration**.
