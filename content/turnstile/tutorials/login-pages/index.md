<p>This tutorial will guide you through integrating Cloudflare Turnstile to protect your web forms, such as login, signup, or contact forms. Learn how to implement the Turnstile widget on the client side and verify the Turnstile token via the Siteverify API on the server side.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>You must have a Cloudflare account.</li>
<li>You must have a web application with a form you want to protect.</li>
<li>You must have basic knowledge of HTML and your server-side language of choice, such as Node.js or Python.</li>
</ul>
<h2 id="get-your-turnstile-sitekey-and-secret-key">Get Your Turnstile sitekey and secret key</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14981.md")
</div>
<h2 id="add-the-turnstile-widget-to-your-html-form">Add the Turnstile widget to your HTML form</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14982.md")
</div>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;UTF-8&quot; /&gt;&#10;		&lt;title&gt;Contact Form&lt;/title&gt;&#10;		&lt;script&#10;			src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot;&#10;			async&#10;			defer&#10;		&gt;&lt;/script&gt;&#10;		&lt;script&gt;&#10;			function enableSubmit() {&#10;				document.getElementById(&quot;submit-button&quot;).disabled = false;&#10;			}&#10;		&lt;/script&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;form id=&quot;contact-form&quot; action=&quot;/submit&quot; method=&quot;POST&quot;&gt;&#10;			&lt;input type=&quot;text&quot; name=&quot;name&quot; placeholder=&quot;Name&quot; required /&gt;&#10;			&lt;input type=&quot;email&quot; name=&quot;email&quot; placeholder=&quot;Email&quot; required /&gt;&#10;			&lt;textarea name=&quot;message&quot; placeholder=&quot;Message&quot; required&gt;&lt;/textarea&gt;&#10;&#10;			&lt;!-- Turnstile widget --&gt;&#10;			&lt;div&#10;				class=&quot;cf-turnstile&quot;&#10;				data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&#10;				data-callback=&quot;enableSubmit&quot;&#10;			&gt;&lt;/div&gt;&#10;&#10;			&lt;button type=&quot;submit&quot; id=&quot;submit-button&quot; disabled&gt;Submit&lt;/button&gt;&#10;		&lt;/form&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="verify-the-turnstile-token-on-the-server-side">Verify the Turnstile token on the server side</h2>
<p>You will need to verify the Turnstile token sent from the client side. Below is an example in Node.js.</p>
<pre><code class="language-js">const express = require(&quot;express&quot;);&#10;const axios = require(&quot;axios&quot;);&#10;const bodyParser = require(&quot;body-parser&quot;);&#10;const app = express();&#10;&#10;app.use(bodyParser.urlencoded({ extended: true }));&#10;&#10;app.post(&quot;/submit&quot;, async (req, res) =&gt; {&#10;	const turnstileToken = req.body[&quot;cf-turnstile-response&quot;];&#10;	const secretKey = &quot;your-secret-key&quot;;&#10;&#10;	try {&#10;		const response = await axios.post(&#10;			&quot;https://challenges.cloudflare.com/turnstile/v0/siteverify&quot;,&#10;			null,&#10;			{&#10;				params: {&#10;					secret: secretKey,&#10;					response: turnstileToken,&#10;				},&#10;			},&#10;		);&#10;&#10;		if (response.data.success) {&#10;			// Token is valid, proceed with form submission&#10;			const name = req.body.name;&#10;			const email = req.body.email;&#10;			const message = req.body.message;&#10;			// Your form processing logic here&#10;			res.send(&quot;Form submission successful&quot;);&#10;		} else {&#10;			res.status(400).send(&quot;Turnstile verification failed&quot;);&#10;		}&#10;	} catch (error) {&#10;		res.status(500).send(&quot;Error verifying Turnstile token&quot;);&#10;	}&#10;});&#10;&#10;app.listen(3000, () =&gt; {&#10;	console.log(&quot;Server is running on port 3000&quot;);&#10;});&#10;</code></pre>
<h2 id="important-considerations">Important considerations</h2>
<p>It is crucial to handle the verification of the Turnstile token correctly. This section covers some key points to keep in mind.</p>
<h3 id="verify-the-token-after-form-input">Verify the token after form input</h3>
<ul>
<li>Ensure that you verify the Turnstile token after the user has filled out the form and selected <strong>submit</strong>.</li>
<li>If you verify the token before the user inputs their data, a malicious actor could potentially bypass the protection by manipulating the form submission after obtaining a valid token.</li>
</ul>
<h3 id="proper-flow-implementation">Proper flow implementation</h3>
<ul>
<li>When the user submits the form, send both the form data and the Turnstile token to your server.</li>
<li>On the server side, verify the Turnstile token first.</li>
<li>Based on the verification response, decide whether to proceed with processing the form data.</li>
</ul>
