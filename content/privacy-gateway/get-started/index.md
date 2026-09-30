---
cp9:
  canonical: https://developers.cloudflare.com/privacy-gateway/get-started/
  description: Set up Privacy Gateway by configuring your server, client, and relay connection using the OHTTP standard.
  full_title: Get started · Cloudflare Privacy Gateway docs
  head_html: <title>Get started · Cloudflare Privacy Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Privacy Gateway by configuring your server, client, and relay connection using the OHTTP standard."><link rel="canonical" href="https://developers.cloudflare.com/privacy-gateway/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-gateway/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Privacy Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Privacy Gateway by configuring your server, client, and relay connection using the OHTTP standard."><meta property="og:url" content="https://developers.cloudflare.com/privacy-gateway/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Gateway"><meta name="algolia_product_filter" content="Privacy Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Privacy Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-gateway/get-started/#page","headline":"Get started \u00b7 Cloudflare Privacy Gateway docs","description":"Set up Privacy Gateway by configuring your server, client, and relay connection using the OHTTP standard.","url":"https://developers.cloudflare.com/privacy-gateway/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-gateway/get-started/
  schema: 1
---
<p>Privacy Gateway implementation consists of three main parts:</p>
<ol>
<li>Application Gateway Server/backend configuration (operated by you).</li>
<li>Client configuration (operated by you).</li>
<li>Connection to a Privacy Gateway Relay Server (operated by Cloudflare).</li>
</ol>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>Privacy Gateway is currently in closed beta. If you are interested, <a href="https://www.cloudflare.com/lp/privacy-edge/">contact us</a>.</p>
<hr />
<h2 id="step-1-configure-your-server">Step 1 - Configure your server</h2>
<p>As a customer of the Privacy Gateway, you also need to add server support for OHTTP by implementing an application gateway server. The application gateway is responsible for decrypting incoming requests, forwarding the inner requests to their destination, and encrypting the corresponding response back to the client.</p>
<p>The <a href="#resources">server implementation</a> will handle incoming requests and produce responses, and it will also advertise its public key configuration for clients to access. The public key configuration is generated securely and made available via an API. Refer to the <a href="https://github.com/cloudflare/privacy-gateway-server-go#readme">README</a> for details about configuration.</p>
<p>Applications can also implement this functionality themselves. Details about <a href="https://datatracker.ietf.org/doc/html/draft-ietf-ohai-ohttp-05#section-3">public key configuration</a>, HTTP message <a href="https://datatracker.ietf.org/doc/html/draft-ietf-ohai-ohttp-05#section-4">encryption and decryption</a>, and <a href="https://datatracker.ietf.org/doc/html/draft-ietf-ohai-ohttp-05#section-5">server-specific details</a> can be found in the OHTTP specification.</p>
<h3 id="resources">Resources</h3>
<p>Use the following resources for help with server configuration:</p>
<ul>
<li><strong>Go</strong>:
<ul>
<li><a href="https://github.com/cloudflare/privacy-gateway-server-go">Sample gateway server</a></li>
<li><a href="https://github.com/chris-wood/ohttp-go">Gateway library</a></li>
</ul>
</li>
<li><strong>Rust</strong>: <a href="https://github.com/martinthomson/ohttp/tree/main/ohttp-server">Gateway library</a></li>
<li><strong>JavaScript / TypeScript</strong>: <a href="https://github.com/chris-wood/ohttp-js">Gateway library</a></li>
</ul>
<hr />
<h2 id="step-2-configure-your-client">Step 2 - Configure your client</h2>
<p>As a customer of the Privacy Gateway, you need to set up client-side support for the gateway. Clients are responsible for encrypting requests, sending them to the Cloudflare Privacy Gateway, and then decrypting the corresponding responses.</p>
<p>Additionally, app developers need to <a href="#resources-1">configure the client</a> to fetch or otherwise discover the gateway’s public key configuration. How this is done depends on how the gateway makes its public key configuration available. If you need help with this configuration, <a href="https://www.cloudflare.com/lp/privacy-edge/">contact us</a>.</p>
<h3 id="resources-1">Resources</h3>
<p>Use the following resources for help with client configuration:</p>
<ul>
<li><strong>Objective C</strong>: <a href="https://github.com/cloudflare/privacy-gateway-client-demo">Sample application</a></li>
<li><strong>Rust</strong>: <a href="https://github.com/martinthomson/ohttp/tree/main/ohttp-client">Client library</a></li>
<li><strong>JavaScript / TypeScript</strong>: <a href="https://github.com/chris-wood/ohttp-js">Client library</a></li>
</ul>
<hr />
<h2 id="step-3-review-your-application">Step 3 - Review your application</h2>
<p>After you have configured your client and server, review your application to make sure you are only sending intended data to Cloudflare and the application backend. In particular, application data should not contain anything unique to an end-user, as this would invalidate the benefits that OHTTP provides.</p>
<ul>
<li>Applications should scrub identifying user data from requests forwarded through the Privacy Gateway. This includes, for example, names, email addresses, phone numbers, etc.</li>
<li>Applications should encourage users to disable crash reporting when using Privacy Gateway. Crash reports can contain sensitive user information and data, including email addresses.</li>
<li>Where possible, application data should be encrypted on the client device with a key known only to the client. For example, iOS generally has good support for <a href="https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys">client-side encryption (and key synchronization via the KeyChain)</a>. Android likely has similar features available.</li>
</ul>
<hr />
<h2 id="step-4-relay-requests-through-cloudflare">Step 4 - Relay requests through Cloudflare</h2>
<p>Before sending any requests, you need to first set up your account with Cloudflare. That requires <a href="https://www.cloudflare.com/lp/privacy-edge/">contacting us</a> and providing the URL of your application gateway server.</p>
<p>Then, make sure you are forwarding requests to a mutually agreed URL with the following conventions.</p>
<pre tabindex="0"><code class="language-txt">https://privacy-relay.cloudflare.com/&lt;GATEWAY_SERVER_NAME&gt;&#10;</code></pre>
