---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/
  description: CORS in Access.
  full_title: CORS · Cloudflare One docs
  head_html: <title>CORS · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="CORS in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/index.md"><meta property="og:title" content="CORS · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="CORS in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="CORS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/#page","headline":"CORS \u00b7 Cloudflare One docs","description":"CORS in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CORS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/
  schema: 1
---
<p>Cross-Origin Resource Sharing (<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS">CORS</a>) is a mechanism that uses HTTP headers to grant a web application running on one origin permission to reach selected resources in a different origin. The web application executes a cross-origin HTTP request when it requests a resource that has a different origin from its own, including domain, protocol, or port.</p>
<p>For a CORS request to reach a site protected by Access, the request must include a valid <code>CF-Authorization</code> cookie. This may require additional configuration depending on the type of request:</p>
<ul>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests">Simple requests</a> are sent directly to the origin, without triggering a preflight request. For configuration instructions, refer to <a href="#allow-simple-requests">Allow simple requests</a>.</p>
</li>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests">Preflighted requests</a> cause the browser to send an OPTIONS request before sending the actual request. The OPTIONS request checks which methods and headers are allowed by the origin. For configuration instructions, refer to <a href="#allow-preflighted-requests">Allow preflighted requests</a>.</p>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4887.md")
</aside>
<h2 id="allow-simple-requests">Allow simple requests</h2>
<p>If you make a simple CORS request to an Access-protected domain and have not yet logged in, the request will return a <code>CORS error</code>. There are two ways you can resolve this error:</p>
<ul>
<li><strong>Option 1</strong> — <a href="#authenticate-manually">Log in and refresh the page</a>.</li>
<li><strong>Option 2</strong> — <a href="#send-authentication-token-with-cloudflare-worker">Create a Cloudflare Worker which automatically sends an authentication token</a>. This method only works if both sites involved in the CORS exchange are behind Access.</li>
</ul>
<h3 id="authenticate-manually">Authenticate manually</h3>
<ol>
<li>Visit the target domain in your browser. You will see the Access login page.</li>
<li>Log in to the target domain. This generates a <code>CF-Authorization</code> cookie.</li>
<li>Refresh the page that made the CORS request. The refresh resends the request with the newly generated cookie.</li>
</ol>
<h2 id="allow-preflighted-requests">Allow preflighted requests</h2>
<p>If you make a preflighted cross-origin request to an Access-protected domain, the OPTIONS request will return a <code>403</code> error. This error occurs regardless of whether you have logged in to the domain. This is because the browser never includes cookies with OPTIONS requests, by design. Cloudflare will therefore block the preflight request, causing the CORS exchange to fail.</p>
<p>There are three ways you can resolve this error:</p>
<ul>
<li><strong>Option 1</strong> — <a href="#bypass-options-requests-to-origin">Bypass OPTIONS requests to origin</a>.</li>
<li><strong>Option 2</strong> — <a href="#configure-response-to-preflight-requests">Configure Cloudflare to respond to the OPTIONS request</a>.</li>
<li><strong>Option 3</strong> — <a href="#send-authentication-token-with-cloudflare-worker">Create a Cloudflare Worker which automatically sends an authentication token</a>. This method only works if both sites involved in the CORS exchange are behind Access.</li>
</ul>
<h3 id="bypass-options-requests-to-origin">Bypass OPTIONS requests to origin</h3>
<p>You can configure Cloudflare to send OPTIONS requests directly to your origin server. To bypass Access for OPTIONS requests:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Locate the origin that will be receiving OPTIONS requests and select <strong>Configure</strong>.</li>
<li>Go to <strong>Advanced settings</strong> &gt; <strong>Cross-Origin Resource Sharing (CORS) settings</strong>.</li>
<li>Turn on <strong>Bypass options requests to origin</strong>. This will remove all existing CORS settings for this application.</li>
</ol>
<p>It is still important to enforce CORS for the Access JWT -- this option should only be used if you have CORS enforcement established in your origin server.</p>
<h3 id="configure-response-to-preflight-requests">Configure response to preflight requests</h3>
<p>You can configure Cloudflare to respond to the OPTIONS request on your behalf. The OPTIONS request never reaches your origin. After the preflight exchange resolves, the browser will then send the main request which does include the authentication cookie (assuming you have logged into the Access-protected domain).</p>
<p>To configure how Cloudflare responds to preflight requests:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Locate the origin that will be receiving OPTIONS requests and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Go to <strong>Advanced settings</strong> &gt; <strong>Cross-Origin Resource Sharing (CORS) settings</strong>.</p>
</li>
<li>
<p>Configure these <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#the_http_response_headers">CORS settings</a> to match the response headers sent by your origin.</p>
<p>For example, if you have configured <code>api.mysite.com</code>to return the following headers:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">headers: {&#10;  &#x27;Access-Control-Allow-Origin&#x27;: &#x27;https://example.com&#x27;,&#10;  &#x27;Access-Control-Allow-Credentials&#x27; : true,&#10;  &#x27;Access-Control-Allow-Methods&#x27;: &#x27;GET, OPTIONS&#x27;,&#10;  &#x27;Access-Control-Allow-Headers&#x27;: &#x27;office&#x27;,&#10;  &#x27;Content-Type&#x27;: &#x27;application/json&#x27;,&#10;}&#10;</code></pre>
<p>then go to <code>api.mysite.com</code> in Access and configure <strong>Access-Control-Allow-Origin</strong>, <strong>Access-Control-Allow-Credentials</strong>, <strong>Access-Control-Allow-Methods</strong>, and <strong>Access-Control-Allow-Headers</strong>.
<img src="/assets/upstream/images/cloudflare-one/policies/CORS-settings.png" alt="Example CORS settings configuration in Cloudflare One" /></p>
<ol start="5">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>(Optional) You can check your configuration by sending an OPTIONS request to the origin with <code>curl</code>. For example,</p>
</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl --head --request OPTIONS https://api.mysite.com \&#10;&#45;-header &#x27;origin: https://example.com&#x27; \&#10;&#45;-header &#x27;access-control-request-method: GET&#x27;&#10;</code></pre>
<p>should return a response similar to:</p>
<pre tabindex="0"><code class="language-txt">HTTP/2 200&#10;date: Tue, 24 May 2022 21:51:21 GMT&#10;vary: Origin, Access-Control-Request-Method, Access-Control-Request-Headers&#10;access-control-allow-origin: https://example.com&#10;access-control-allow-methods: GET&#10;access-control-allow-credentials: true&#10;expect-ct: max-age=604800, report-uri=&quot;https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct&quot;&#10;report-to: {&quot;endpoints&quot;:[{&quot;url&quot;:&quot;https:\/\/a.nel.cloudflare.com\/report\/v3?s=A%2FbOOWJio%2B%2FjuJv5NC%2FE3%2Bo1zBl2UdjzJssw8gJLC4lE1lzIUPQKqJoLRTaVtFd21JK1d4g%2BnlEGNpx0mGtsR6jerNfr2H5mlQdO6u2RdOaJ6n%2F%2BS%2BF9%2Fa12UromVLcHsSA5Y%2Fj72tM%3D&quot;}],&quot;group&quot;:&quot;cf-nel&quot;,&quot;max_age&quot;:604800}&#10;nel: {&quot;success_fraction&quot;:0.01,&quot;report_to&quot;:&quot;cf-nel&quot;,&quot;max_age&quot;:604800}&#10;server: cloudflare&#10;cf-ray: 7109408e6b84efe4-EWR&#10;</code></pre>
<h2 id="send-authentication-token-with-cloudflare-worker">Send authentication token with Cloudflare Worker</h2>
<p>If you have two sites protected by Cloudflare Access, <code>example.com</code> and <code>api.mysite.com</code>, requests made between the two will be subject to CORS checks. Users who log in to <code>example.com</code> will be issued a cookie for <code>example.com</code>. When the user's browser requests <code>api.mysite.com</code>, Cloudflare Access looks for a cookie specific to <code>api.mysite.com</code>. The request will fail if the user has not already logged in to <code>api.mysite.com</code>.</p>
<p>To avoid having to log in twice, you can create a Cloudflare Worker that automatically sends authentication credentials to <code>api.mysite.com</code>.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><a href="/workers/get-started/guide/">Workers account</a></li>
<li><code>wrangler</code> installation</li>
<li><code>example.com</code> and <code>api.mysite.com</code> domains <a href="/cloudflare-one/access-controls/applications/http-apps/">protected by Access</a></li>
</ul>
<h3 id="1-generate-a-service-token"><ol>
<li>Generate a service token</li>
</ol></h3>
<p>Follow <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">these instructions</a> to generate a new Access service token. Copy the <code>Client ID</code> and <code>Client Secret</code> to a safe place, as you will use them in a later step.</p>
<h3 id="2-add-a-service-auth-policy"><ol start="2">
<li>Add a Service Auth policy</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Find your <code>api.mysite.com</code> application and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Select the <strong>Policies</strong> tab.</p>
</li>
<li>
<p>Add the following policy:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td>Service Auth</td>
<td>Include</td>
<td>Service Token</td>
</tr>
</tbody>
</table>
<h3 id="3-create-a-new-worker"><ol start="3">
<li>Create a new Worker</li>
</ol></h3>
<p>Open a terminal and run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- authentication-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- authentication-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare authentication-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare authentication-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest authentication-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest authentication-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This will prompt you to install the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> package and lead you through setup.</p>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your project directory.</p>
<pre tabindex="0"><code class="language-sh">cd authentication-worker&#10;</code></pre>
<p>Open <code>/src/index.js</code> and delete the existing code and paste in the following example:</p>
<pre tabindex="0"><code class="language-js">// The hostname where your API lives&#10;const originalAPIHostname = &quot;api.mysite.com&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		// Change just the host. If the request comes in on example.com/api/name, the new URL is api.mysite.com/api/name&#10;		const url = new URL(request.url);&#10;		url.hostname = originalAPIHostname;&#10;&#10;		// If your API is located on api.mysite.com/anyname (without &quot;api/&quot; in the path),&#10;		// remove the &quot;api/&quot; part of example.com/api/name&#10;&#10;		// url.pathname = url.pathname.substring(4)&#10;&#10;		// Best practice is to always use the original request to construct the new request&#10;		// to clone all the attributes. Applying the URL also requires a constructor&#10;		// since once a Request has been constructed, its URL is immutable.&#10;		const newRequest = new Request(url.toString(), request);&#10;&#10;		newRequest.headers.set(&quot;cf-access-client-id&quot;, env.CF_ACCESS_CLIENT_ID);&#10;		newRequest.headers.set(&quot;cf-access-client-secret&quot;, env.CF_ACCESS_CLIENT_SECRET);&#10;		try {&#10;			const response = await fetch(newRequest);&#10;&#10;			// Copy over the response&#10;			const modifiedResponse = new Response(response.body, response);&#10;&#10;			// Delete the set-cookie from the response so it doesn&#x27;t override existing cookies&#10;			modifiedResponse.headers.delete(&quot;set-cookie&quot;);&#10;&#10;			return modifiedResponse;&#10;		} catch (e) {&#10;			return new Response(JSON.stringify({ error: e.message }), {&#10;				status: 500,&#10;			});&#10;		}&#10;	},&#10;};&#10;</code></pre>
<p>Then, deploy the Worker to your Cloudflare account:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h3 id="4-configure-the-worker"><ol start="4">
<li>Configure the Worker</li>
</ol></h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select your newly created Worker.</p>
</li>
<li>
<p>In the <strong>Triggers</strong> tab, go to <strong>Routes</strong> and add <code>example.com/api/*</code>. The Worker is placed on a subpath of <code>example.com</code> to avoid making a cross-origin request.</p>
</li>
<li>
<p>In the <strong>Settings</strong> tab, select <strong>Variables</strong>.</p>
</li>
<li>
<p>Under <strong>Environment Variables</strong>, add the following <a href="/workers/configuration/environment-variables/#add-environment-variables-via-the-dashboard">secret variables</a>:</p>
<ul>
<li><code>CF_ACCESS_CLIENT_ID</code> = <code>&lt;service token Client ID&gt;</code></li>
<li><code>CF_ACCESS_CLIENT_SECRET</code> = <code>&lt;service token Client Secret&gt;</code></li>
</ul>
</li>
</ol>
<p>The Client ID and Client Secret are copied from your <a href="#1-generate-a-service-token">service token</a>.</p>
<ol start="6">
<li>Enable the <strong>Encrypt</strong> option for each variable and select <strong>Save</strong>.</li>
</ol>
<h3 id="5-update-http-request-urls"><ol start="5">
<li>Update HTTP request URLs</li>
</ol></h3>
<p>Modify your <code>example.com</code> application to send all requests to <code>example.com/api/</code> instead of <code>api.mysite.com</code>.</p>
<p>HTTP requests should now work seamlessly between two different Access-protected domains. When a user logs in to <code>example.com</code>, the browser makes a request to the Worker instead of to <code>api.mysite.com</code>. The Worker adds the Access service token to the request headers and then forwards the request to <code>api.mysite.com</code>. Since the service token matches a Service Auth policy, the user no longer needs to log in to <code>api.mysite.com</code>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>In general, we recommend the following steps when troubleshooting CORS issues:</p>
<ol>
<li>Capture a HAR file with the issue described, as well as the JS console log output recorded simultaneously. This is because the HAR file alone will not give full visibility on the reason behind cross-origin issues.</li>
<li>Ensure that the application has set <code>credentials: 'same-origin'</code> in all fetch or XHR requests.</li>
<li>If you are using the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin">cross-origin setting</a> on script tags, these must be set to &quot;use-credentials&quot;.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="cors-is-failing-on-the-same-domain">CORS is failing on the same domain</h3>
@markup("md", "content/.markup/bodies/4886.md")
</aside>
