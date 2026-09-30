<p>This tutorial will guide you on how to integrate Cloudflare Turnstile, <a href="/waf/">Web Application Firewall (WAF)</a>, and <a href="/bots/get-started/bot-management/">Bot Management</a> into an existing authentication system. This combination creates a robust defense against various threats, including automated attacks and malicious login attempts.</p>
<h2 id="overview">Overview</h2>
<p>To use WAF and Bot Management, your site must have its DNS pointing through Cloudflare. However, Turnstile can be used independently on any site including those not on Cloudflare's network. This tutorial will cover how to implement all three products, but you can focus on Turnstile if your site is not on Cloudflare's network.</p>
<p>WAF, Bot Management, and Turnstile work well together by operating on different layers of the application:</p>
<ul>
<li>WAF filters malicious traffic based on network signals.</li>
<li>Bot Management analyzes requests to identify and mitigate automated threats.</li>
<li>Turnstile examines client-side and browser signals to distinguish between human users and bots.</li>
</ul>
<p>By combining server-side (WAF and Bot Management) and client-side (Turnstile) security measures, you can combine multiple layers of defense to create a protection system that is difficult for attackers to circumvent.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>You must have a Cloudflare account with access to WAF and Bot Management (if using).</li>
<li>An existing JavaScript/TypeScript-based route handling authentication.</li>
</ul>
<p>This tutorial uses a simple login form written in plain HTML to demonstrate how to integrate Turnstile into your application. In the backend, a stubbed out authentication route, written in TypeScript, will handle the login request. You may replace this with the language of your choice. As long as your language or framework is able to make an external HTTP request to <a href="/api/resources/turnstile/subresources/widgets/methods/create/">Turnstile's API</a>, you can integrate Turnstile into your application.</p>
<h2 id="configure-waf-and-bot-management">Configure WAF and Bot Management</h2>
<p>If your site is on Cloudflare's network and subscribed to an Enterprise plan, you must configure WAF and Bot Management.</p>
<h3 id="issue-challenges-for-potential-bot-traffic">Issue challenges for potential bot traffic</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14983.md")
</div>
<p>This configuration challenges requests with a low bot score, leveraging network signals to identify potential threats before they reach your application. You may customize the score threshold based on your specific use case.</p>
<h2 id="set-up-cloudflare-turnstile">Set up Cloudflare Turnstile</h2>
<p>Turnstile can be used on any site, regardless of whether it is on Cloudflare's network:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14984.md")
</div>
<p>Turnstile adds an extra layer of security by analyzing browser and client-side signals, complementing the server-side checks performed by WAF and Bot Management.</p>
<h3 id="enable-the-option-to-use-the-existing-clearance-cookie">Enable the option to use the existing clearance cookie</h3>
<p>If your site is on Cloudflare, you can enable the option to use the existing <a href="/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile">clearance cookie</a> in Turnstile's settings. This integration allows Turnstile to use the clearance cookie as part of its determination of whether a user should receive a challenge. This integration is optional, but recommended if you already are using WAF and Bot Management.</p>
<h2 id="integrate-turnstile-into-your-application">Integrate Turnstile into your application</h2>
<p>There are two components to implementing Turnstile into your application: the Turnstile widget and the server-side validation logic.</p>
<h3 id="add-the-turnstile-widget-to-your-login-form">Add the Turnstile widget to your login form</h3>
<p>Add the Turnstile widget to your existing login form:</p>
<pre><code class="language-html">&lt;form id=&quot;login-form&quot;&gt;&#10;	&lt;input type=&quot;text&quot; id=&quot;username&quot; placeholder=&quot;Username&quot; required /&gt;&#10;	&lt;input type=&quot;password&quot; id=&quot;password&quot; placeholder=&quot;Password&quot; autocomplete=&quot;off&quot; required /&gt;&#10;	&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&gt;&lt;/div&gt;&#10;	&lt;button type=&quot;submit&quot;&gt;Log in&lt;/button&gt;&#10;&lt;/form&gt;&#10;&#10;&lt;script&#10;	src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot;&#10;	async&#10;	defer&#10;&gt;&lt;/script&gt;&#10;</code></pre>
<p>Replace <code>&lt;YOUR-SITE-KEY&gt;</code> with your actual Turnstile site key.</p>
<h2 id="handle-the-login-request">Handle the login request</h2>
<p>In your existing authentication route, add Turnstile validation:</p>
<pre><code class="language-typescript">async function validateTurnstileToken(&#10;	ip: string,&#10;	token: string,&#10;	secret: string,&#10;): Promise&lt;boolean&gt; {&#10;	const response = await fetch(&#10;		&quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;		{&#10;			method: &quot;POST&quot;,&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;			body: JSON.stringify({ ip, secret, response: token }),&#10;		},&#10;	);&#10;&#10;	const outcome = await response.json();&#10;	return outcome.success;&#10;}&#10;&#10;// Assume that this is a TypeScript route handler.&#10;// You may replace this with a different implementation,&#10;// based on your language or framework&#10;export async function onRequestPost(context) {&#10;	const { request, env } = context;&#10;	const { username, password, token } = await request.json();&#10;&#10;	// Validate Turnstile token&#10;	const secretKey = env.TURNSTILE_SECRET_KEY;&#10;	const ip = request.headers.get(&quot;CF-Connecting-IP&quot;);&#10;	const turnstileValid = await validateTurnstileToken(ip, token, secretKey);&#10;	if (!turnstileValid) {&#10;		// Return back to the login page with an error message&#10;		return Response.redirect(&quot;/login&quot;, 302, {&#10;			headers: {&#10;				Location: &quot;/login?error=invalid-turnstile-token&quot;,&#10;			},&#10;		});&#10;	}&#10;&#10;	// Perform your existing authentication logic here&#10;	const isValidLogin = await checkCredentials(username, password);&#10;&#10;	if (isValidLogin) {&#10;		return new Response(JSON.stringify({ message: &quot;Login successful&quot; }), {&#10;			status: 200,&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;		});&#10;	} else {&#10;		return new Response(JSON.stringify({ error: &quot;Invalid credentials&quot; }), {&#10;			status: 401,&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;		});&#10;	}&#10;}&#10;&#10;async function checkCredentials(&#10;	username: string,&#10;	password: string,&#10;): Promise&lt;boolean&gt; {&#10;	// Your existing credential checking logic&#10;}&#10;</code></pre>
<p>This setup ensures that the Turnstile token is validated on the server-side before proceeding with the login process, adding an extra layer of security based on client-side signals.</p>
<h2 id="testing">Testing</h2>
<p>After deployment, you will want to test your integration. Because your bot score will be low, you will probably not receive a challenge. However, you can add additional rules as needed to force a redirect to the challenge page. Some options to do this are:</p>
<ol>
<li>Add a WAF rule that always forwards your IP address to the challenge page.</li>
<li>Add a WAF rule that checks for the presence of a query parameter, such as <code>?challenge=true</code>.</li>
</ol>
<h2 id="best-practices">Best practices</h2>
<ol>
<li>Always validate the Turnstile token on the server-side before checking credentials.</li>
<li>Use environment variables to store sensitive information like your Turnstile secret key.</li>
<li>Implement proper error handling and logging to monitor for potential security issues.</li>
</ol>
<p>By combining Turnstile with WAF and Bot Management, you can create a system that secures your application at the network layer, while also providing an extra layer of protection using client-side signals. This approach makes it significantly more difficult for malicious actors to automate attacks against your login system.</p>
<h2 id="resources">Resources</h2>
<p>If you are interested in customizing Turnstile, refer to the resources below for more information:</p>
<ul>
<li><a href="/turnstile/get-started/client-side-rendering/">Client-side rendering</a>. Learn how to customize how and when Turnstile renders in your user interface, to better fit your application's needs and user experience.</li>
<li><a href="/turnstile/get-started/server-side-validation/">Server-side validation</a>. Learn how Turnstile's API works, including request parameters, as well as how to handle different types of responses, including error codes.</li>
<li><a href="/turnstile/turnstile-analytics/">Turnstile Analytics</a>. Learn how to view Turnstile's analytics in the Cloudflare dashboard. This includes metrics on the number of challenges issued, as well as the <a href="/cloudflare-challenges/reference/challenge-solve-rate/">challenge solve rate (CSR)</a>.</li>
</ul>
