---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/cli/
  description: Cloudflare's cloudflared command-line tool allows you to interact with endpoints protected by Cloudflare Access.
  full_title: Connect through Cloudflare Access using a CLI · Cloudflare One docs
  head_html: <title>Connect through Cloudflare Access using a CLI · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare&#x27;s cloudflared command-line tool allows you to interact with endpoints protected by Cloudflare Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/cli/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/cli/index.md"><meta property="og:title" content="Connect through Cloudflare Access using a CLI · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare&#x27;s cloudflared command-line tool allows you to interact with endpoints protected by Cloudflare Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/cli/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="CLI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/cli/#page","headline":"Connect through Cloudflare Access using a CLI \u00b7 Cloudflare One docs","description":"Cloudflare's cloudflared command-line tool allows you to interact with endpoints protected by Cloudflare Access.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/cli/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CLI"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/cli/
  schema: 1
---
<p>Cloudflare's <code>cloudflared</code> command-line tool allows you to interact with endpoints protected by Cloudflare Access. You can use <code>cloudflared</code> to interact with a protected application's API.</p>
<p>These instructions are not meant for configuring a service to run against an API. The token in this example is tailored to user identity and intended only for an end user interacting with an API via a command-line tool.</p>
<p><strong>This walkthrough covers how to:</strong></p>
<ul>
<li>Connect to resources secured by Cloudflare Access from a CLI</li>
</ul>
<p><strong>Time to complete:</strong></p>
<p>30 minutes</p>
<hr />
<h2 id="authenticate-a-session-from-the-command-line">Authenticate a session from the command line</h2>
<p>Once you have <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">installed <code>cloudflared</code></a>, you can use it to retrieve a Cloudflare Access <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a>. This walkthrough uses the domain <code>example.com</code> as a stand-in for a protected API.</p>
<ol>
<li>To generate a token, run the following command:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared access login https://example.com&#10;</code></pre>
<p>With this command, <code>cloudflared</code> launches a browser window containing the same Access login page found when attempting to access a web application.</p>
<ol start="2">
<li>Select your identity provider and log in.</li>
</ol>
<p>If the browser window does not launch, you can use the unique URL that is automatically printed to the command line.</p>
<ol>
<li>Once you have successfully authenticated, the browser returns the token to <code>cloudflared</code> in a cryptographic transfer and stores it.</li>
</ol>
<p>The token is valid for the <a href="/cloudflare-one/access-controls/access-settings/session-management/">session duration</a> configured by the Access administrator.</p>
<h2 id="access-your-api">Access your API</h2>
<p>Once you have retrieved a token, you can access the protected API. The <code>cloudflared</code> command-line tool includes a wrapper for transferring data via <code>curl</code>, which uses URL syntax (for more, see the <a href="https://github.com/curl/curl">curl</a> GitHub project). The wrapper injects the token into the <code>curl</code> request as a query argument named <em>token</em>. You can invoke the wrapper as follows:</p>
<pre tabindex="0"><code class="language-sh">cloudflared access curl http://example.com&#10;</code></pre>
<p>It is possible also to use the <code>put</code> command with <code>cloudflared</code> for any Unix tool to include the token in the request.</p>
<p>Read on for other available commands.</p>
<h2 id="available-commands">Available commands</h2>
<h3 id="login">login</h3>
<p>The <code>login</code> command initiates the login flow for an application behind Access.</p>
<pre tabindex="0"><code class="language-sh">cloudflared access login http://example.com&#10;</code></pre>
<h3 id="curl">curl</h3>
<p>The <code>curl</code> command invokes the client wrapper and includes the token in the request automatically.</p>
<pre tabindex="0"><code class="language-sh">cloudflared access curl http://example.com&#10;</code></pre>
<h3 id="token">token</h3>
<p>The <code>token</code> command retrieves the token scoped to that specific application for use in other command-line tools.</p>
<pre tabindex="0"><code class="language-sh">cloudflared access token -app=http://example.com&#10;</code></pre>
<h2 id="using-the-token-as-an-environment-variable">Using the token as an environment variable</h2>
<p>It is possible to save the token as an environment variable for convenience and concision in scripts that access a protected application.</p>
<p>Set up a token as an environment variable as follows:</p>
<ol>
<li>Run the following command to export the token to the shell environment:</li>
</ol>
<pre tabindex="0"><code class="language-sh">export TOKEN=$(cloudflared access token -app=http://example.com)&#10;</code></pre>
<ol start="2">
<li>Confirm the token was saved with the following:</li>
</ol>
<pre tabindex="0"><code class="language-sh">echo $TOKEN&#10;</code></pre>
<p>Once you have exported the token to your environment, use the variable with the Cloudflare Access request header in the script to access a protected endpoint, as in the following example:</p>
<pre tabindex="0"><code class="language-sh">curl -H &quot;cf-access-token: $TOKEN&quot; https://example.com/rest/api/2/item/foo-123&#10;</code></pre>
