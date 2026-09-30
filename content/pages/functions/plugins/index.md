---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/plugins/
  description: Extend Pages Functions with distributable Plugins that include built-in routing and functionality.
  full_title: Pages Plugins · Cloudflare Pages docs
  head_html: <title>Pages Plugins · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Extend Pages Functions with distributable Plugins that include built-in routing and functionality."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/plugins/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/plugins/index.md"><meta property="og:title" content="Pages Plugins · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Extend Pages Functions with distributable Plugins that include built-in routing and functionality."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/plugins/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/plugins/#page","headline":"Pages Plugins \u00b7 Cloudflare Pages docs","description":"Extend Pages Functions with distributable Plugins that include built-in routing and functionality.","url":"https://developers.cloudflare.com/pages/functions/plugins/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/plugins/
  schema: 1
---
<p>Cloudflare maintains a number of official Pages Plugins for you to use in your Pages projects:</p>
<ul class="directory-listing"><li><a href="/pages/functions/plugins/cloudflare-access/">Cloudflare Access</a></li><li><a href="/pages/functions/plugins/google-chat/">Google Chat</a></li><li><a href="/pages/functions/plugins/graphql/">GraphQL</a></li><li><a href="/pages/functions/plugins/hcaptcha/">hCaptcha</a></li><li><a href="/pages/functions/plugins/honeycomb/">Honeycomb</a></li><li><a href="/pages/functions/plugins/sentry/">Sentry</a></li><li><a href="/pages/functions/plugins/static-forms/">Static Forms</a></li><li><a href="/pages/functions/plugins/stytch/">Stytch</a></li><li><a href="/pages/functions/plugins/turnstile/">Turnstile</a></li><li><a href="/pages/functions/plugins/community-plugins/">Community Plugins</a></li><li><a href="/pages/functions/plugins/vercel-og/">vercel/og</a></li></ul>
<hr />
<h2 id="author-a-pages-plugin">Author a Pages Plugin</h2>
<p>A Pages Plugin is a Pages Functions distributable which includes built-in routing and functionality. Developers can include a Plugin as a part of their Pages project wherever they chose, and can pass it some configuration options. The full power of Functions is available to Plugins, including middleware, parameterized routes, and static assets.</p>
<p>For example, a Pages Plugin could:</p>
<ul>
<li>Intercept HTML pages and inject in a third-party script.</li>
<li>Proxy a third-party service's API.</li>
<li>Validate authorization headers.</li>
<li>Provide a full admin web app experience.</li>
<li>Store data in KV or Durable Objects.</li>
<li>Server-side render (SSR) webpages with data from a CMS.</li>
<li>Report errors and track performance.</li>
</ul>
<p>A Pages Plugin is essentially a library that developers can use to augment their existing Pages project with a deep integration to Functions.</p>
<h2 id="use-a-pages-plugin">Use a Pages Plugin</h2>
<p>Developers can enhance their projects by mounting a Pages Plugin at a route of their application. Plugins will provide instructions of where they should typically be mounted (for example, an admin interface might be mounted at <code>functions/admin/[[path]].ts</code>, and an error logger might be mounted at <code>functions/_middleware.ts</code>). Additionally, each Plugin may take some configuration (for example, with an API token).</p>
<hr />
<h2 id="static-form-example">Static form example</h2>
<p>In this example, you will build a Pages Plugin and then include it in a project.</p>
<p>The first Plugin should:</p>
<ul>
<li>intercept HTML forms.</li>
<li>store the form submission in <a href="/kv/api/">KV</a>.</li>
<li>respond to submissions with a developer's custom response.</li>
</ul>
<h3 id="1-create-a-new-pages-plugin"><ol>
<li>Create a new Pages Plugin</li>
</ol></h3>
<p>Create a <code>package.json</code> with the following:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;name&quot;: &quot;@cloudflare/static-form-interceptor&quot;,&#10;	&quot;main&quot;: &quot;dist/index.js&quot;,&#10;	&quot;types&quot;: &quot;index.d.ts&quot;,&#10;	&quot;files&quot;: [&quot;dist&quot;, &quot;index.d.ts&quot;, &quot;tsconfig.json&quot;],&#10;	&quot;scripts&quot;: {&#10;		&quot;build&quot;: &quot;npx wrangler pages functions build --plugin --outdir=dist&quot;,&#10;		&quot;prepare&quot;: &quot;npm run build&quot;&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11090.md")
</aside>
<p>In our example, <code>dist/index.js</code> will be the entrypoint to your Plugin. This is a generated file built by Wrangler with the <code>npm run build</code> command. Add the <code>dist/</code> directory to your <code>.gitignore</code>.</p>
<p>Next, create a <code>functions</code> directory and start coding your Plugin. The <code>functions</code> folder will be mounted at some route by the developer, so consider how you want to structure your files. Generally:</p>
<ul>
<li>if you want your Plugin to run on a single route of the developer's choice (for example, <code>/foo</code>), create a <code>functions/index.ts</code> file.</li>
<li>if you want your Plugin to be mounted and serve all requests beyond a certain path (for example, <code>/admin/login</code> and <code>/admin/dashboard</code>), create a <code>functions/[[path]].ts</code> file.</li>
<li>if you want your Plugin to intercept requests but fallback on either other Functions or the project's static assets, create a <code>functions/_middleware.ts</code> file.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="do-not-include-the-mounted-path-in-your-plugin">Do not include the mounted path in your Plugin</h3>
@markup("md", "content/.markup/bodies/11089.md")
</aside>
<p>You are free to use as many different files as you need. The structure of a Plugin is exactly the same as Functions in a Pages project today, except that the handlers receive a new property of their parameter object, <code>pluginArgs</code>. This property is the initialization parameter that a developer passes when mounting a Plugin. You can use this to receive API tokens, KV/Durable Object namespaces, or anything else that your Plugin needs to work.</p>
<p>Returning to your static form example, if you want to intercept requests and override the behavior of an HTML form, you need to create a <code>functions/_middleware.ts</code>. Developers could then mount your Plugin on a single route, or on their entire project.</p>
<pre tabindex="0"><code class="language-typescript">class FormHandler {&#10;	element(element) {&#10;		const name = element.getAttribute(&quot;data-static-form-name&quot;);&#10;		element.setAttribute(&quot;method&quot;, &quot;POST&quot;);&#10;		element.removeAttribute(&quot;action&quot;);&#10;		element.append(&#10;			`&lt;input type=&quot;hidden&quot; name=&quot;static-form-name&quot; value=&quot;${name}&quot; /&gt;`,&#10;			{ html: true },&#10;		);&#10;	}&#10;}&#10;&#10;export const onRequestGet = async (context) =&gt; {&#10;	// We first get the original response from the project&#10;	const response = await context.next();&#10;&#10;	// Then, using HTMLRewriter, we transform `form` elements with a `data-static-form-name` attribute, to tell them to POST to the current page&#10;	return new HTMLRewriter()&#10;		.on(&quot;form[data-static-form-name]&quot;, new FormHandler())&#10;		.transform(response);&#10;};&#10;&#10;export const onRequestPost = async (context) =&gt; {&#10;	// Parse the form&#10;	const formData = await context.request.formData();&#10;	const name = formData.get(&quot;static-form-name&quot;);&#10;	const entries = Object.fromEntries(&#10;		[...formData.entries()].filter(([name]) =&gt; name !== &quot;static-form-name&quot;),&#10;	);&#10;&#10;	// Get the arguments given to the Plugin by the developer&#10;	const { kv, respondWith } = context.pluginArgs;&#10;&#10;	// Store form data in KV under key `form-name:YYYY-MM-DDTHH:MM:SSZ`&#10;	const key = `${name}:${new Date().toISOString()}`;&#10;	context.waitUntil(kv.put(name, JSON.stringify(entries)));&#10;&#10;	// Respond with whatever the developer wants&#10;	const response = await respondWith({ formData });&#10;	return response;&#10;};&#10;</code></pre>
<h3 id="2-type-your-pages-plugin"><ol start="2">
<li>Type your Pages Plugin</li>
</ol></h3>
<p>To create a good developer experience, you should consider adding TypeScript typings to your Plugin. This allows developers to use their IDE features for autocompletion, and also ensure that they include all the parameters you are expecting.</p>
<p>In the <code>index.d.ts</code>, export a function which takes your <code>pluginArgs</code> and returns a <code>PagesFunction</code>. For your static form example, you take two properties, <code>kv</code>, a KV namespace, and <code>respondWith</code>, a function which takes an object with a <code>formData</code> property (<code>FormData</code>) and returns a <code>Promise</code> of a <code>Response</code>:</p>
<pre tabindex="0"><code class="language-typescript">export type PluginArgs = {&#10;	kv: KVNamespace;&#10;	respondWith: (args: { formData: FormData }) =&gt; Promise&lt;Response&gt;;&#10;};&#10;&#10;export default function (args: PluginArgs): PagesFunction;&#10;</code></pre>
<h3 id="3-test-your-pages-plugin"><ol start="3">
<li>Test your Pages Plugin</li>
</ol></h3>
<p>We are still working on creating a great testing experience for Pages Plugins authors. Please be patient with us until all those pieces come together. In the meantime, you can create an example project and include your Plugin manually for testing.</p>
<h3 id="4-publish-your-pages-plugin"><ol start="4">
<li>Publish your Pages Plugin</li>
</ol></h3>
<p>You can distribute your Plugin however you choose. Popular options include publishing on <a href="https://www.npmjs.com/">npm</a>, showcasing it in the #what-i-built or #pages-discussions channels in our <a href="https://discord.com/invite/cloudflaredev">Developer Discord</a>, and open-sourcing on <a href="https://github.com/">GitHub</a>.</p>
<p>Make sure you are including the generated <code>dist/</code> directory, your typings <code>index.d.ts</code>, as well as a <code>README.md</code> with instructions on how developers can use your Plugin.</p>
<hr />
<h3 id="5-install-your-pages-plugin"><ol start="5">
<li>Install your Pages Plugin</li>
</ol></h3>
<p>If you want to include a Pages Plugin in your application, you need to first install that Plugin to your project.</p>
<p>If you are not yet using <code>npm</code> in your project, run <code>npm init</code> to create a <code>package.json</code> file. The Plugin's <code>README.md</code> will typically include an installation command (for example, <code>npm install --save @cloudflare/static-form-interceptor</code>).</p>
<h3 id="6-mount-your-pages-plugin"><ol start="6">
<li>Mount your Pages Plugin</li>
</ol></h3>
<p>The <code>README.md</code> of the Plugin will likely include instructions for how to mount the Plugin in your application. You will need to:</p>
<ol>
<li>Create a <code>functions</code> directory, if you do not already have one.</li>
<li>Decide where you want this Plugin to run and create a corresponding file in the <code>functions</code> directory.</li>
<li>Import the Plugin and export an <code>onRequest</code> method in this file, initializing the Plugin with any arguments it requires.</li>
</ol>
<p>In the static form example, the Plugin you have created already was created as a middleware. This means it can run on either a single route, or across your entire project. If you had a single contact form on your website at <code>/contact</code>, you could create a <code>functions/contact.ts</code> file to intercept just that route. You could also create a <code>functions/_middleware.ts</code> file to intercept all other routes and any other future forms you might create. As the developer, you can choose where this Plugin can run.</p>
<p>A Plugin's default export is a function which takes the same context parameter that a normal Pages Functions handler is given.</p>
<pre tabindex="0"><code class="language-typescript">import staticFormInterceptorPlugin from &quot;@cloudflare/static-form-interceptor&quot;;&#10;&#10;export const onRequest = (context) =&gt; {&#10;	return staticFormInterceptorPlugin({&#10;		kv: context.env.FORM_KV,&#10;		respondWith: async ({ formData }) =&gt; {&#10;			// Could call email/notification service here&#10;			const name = formData.get(&quot;name&quot;);&#10;			return new Response(`Thank you for your submission, ${name}!`);&#10;		},&#10;	})(context);&#10;};&#10;</code></pre>
<h3 id="7-test-your-pages-plugin"><ol start="7">
<li>Test your Pages Plugin</li>
</ol></h3>
<p>You can use <code>wrangler pages dev</code> to test a Pages project, including any Plugins you have installed. Remember to include any KV bindings and environment variables that the Plugin is expecting.</p>
<p>With your Plugin mounted on the <code>/contact</code> route, a corresponding HTML file might look like this:</p>
<pre tabindex="0"><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;body&gt;&#10;		&lt;h1&gt;Contact us&lt;/h1&gt;&#10;		&lt;!-- Include the `data-static-form-name` attribute to name the submission --&gt;&#10;		&lt;form data-static-form-name=&quot;contact&quot;&gt;&#10;			&lt;label&gt;&#10;				&lt;span&gt;Name&lt;/span&gt;&#10;				&lt;input type=&quot;text&quot; autocomplete=&quot;name&quot; name=&quot;name&quot; /&gt;&#10;			&lt;/label&gt;&#10;			&lt;label&gt;&#10;				&lt;span&gt;Message&lt;/span&gt;&#10;				&lt;textarea name=&quot;message&quot;&gt;&lt;/textarea&gt;&#10;			&lt;/label&gt;&#10;		&lt;/form&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>Your plugin should pick up the <code>data-static-form-name=&quot;contact&quot;</code> attribute, set the <code>method=&quot;POST&quot;</code>, inject in an <code>&lt;input type=&quot;hidden&quot; name=&quot;static-form-name&quot; value=&quot;contact&quot; /&gt;</code> element, and capture <code>POST</code> submissions.</p>
<h3 id="8-deploy-your-pages-project"><ol start="8">
<li>Deploy your Pages project</li>
</ol></h3>
<p>Make sure the new Plugin has been added to your <code>package.json</code> and that everything works locally as you would expect. You can then <code>git commit</code> and <code>git push</code> to trigger a Cloudflare Pages deployment.</p>
<p>If you experience any problems with any one Plugin, file an issue on that Plugin's bug tracker.</p>
<p>If you experience any problems with Plugins in general, we would appreciate your feedback in the #pages-discussions channel in <a href="https://discord.com/invite/cloudflaredev">Discord</a>! We are excited to see what you build with Plugins and welcome any feedback about the authoring or developer experience. Let us know in the Discord channel if there is anything you need to make Plugins even more powerful.</p>
<hr />
<h2 id="chain-your-plugin">Chain your Plugin</h2>
<p>Finally, as with Pages Functions generally, it is possible to chain together Plugins in order to combine together different features. Middleware defined higher up in the filesystem will run before other handlers, and individual files can chain together Functions in an array like so:</p>
<pre tabindex="0"><code class="language-typescript">import sentryPlugin from &quot;@cloudflare/pages-plugin-sentry&quot;;&#10;import cloudflareAccessPlugin from &quot;@cloudflare/pages-plugin-cloudflare-access&quot;;&#10;import adminDashboardPlugin from &quot;@cloudflare/a-fictional-admin-plugin&quot;;&#10;&#10;export const onRequest = [&#10;	// Initialize a Sentry Plugin to capture any errors&#10;	sentryPlugin({ dsn: &quot;https://sentry.io/welcome/xyz&quot; }),&#10;&#10;	// Initialize a Cloudflare Access Plugin to ensure only administrators can access this protected route&#10;	cloudflareAccessPlugin({&#10;		domain: &quot;https://test.cloudflareaccess.com&quot;,&#10;		aud: &quot;4714c1358e65fe4b408ad6d432a5f878f08194bdb4752441fd56faefa9b2b6f2&quot;,&#10;	}),&#10;&#10;	// Populate the Sentry plugin with additional information about the current user&#10;	(context) =&gt; {&#10;		const email =&#10;			context.data.cloudflareAccessJWT.payload?.email || &quot;service user&quot;;&#10;&#10;		context.data.sentry.setUser({ email });&#10;&#10;		return next();&#10;	},&#10;&#10;	// Finally, serve the admin dashboard plugin, knowing that errors will be captured and that every incoming request has been authenticated&#10;	adminDashboardPlugin(),&#10;];&#10;</code></pre>
