---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/
  description: Create a tunnel to connect private applications.
  full_title: Create a Cloudflare Tunnel · Cloudflare Learning Paths
  head_html: <title>Create a Cloudflare Tunnel · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Create a tunnel to connect private applications."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/index.md"><meta property="og:title" content="Create a Cloudflare Tunnel · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a tunnel to connect private applications."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Access,Cloudflare Tunnel,Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/#page","headline":"Create a Cloudflare Tunnel \u00b7 Cloudflare Learning Paths","description":"Create a tunnel to connect private applications.","url":"https://developers.cloudflare.com/learning-paths/clientless-access/connect-private-applications/create-tunnel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/clientless-access/connect-private-applications/create-tunnel/
  schema: 1
---
<p>To enable clientless access to your applications, you will need to create a Cloudflare Tunnel that publishes applications to a domain on Cloudflare. A published application creates a public DNS record that routes traffic to a specific address, protocol, and port associated with a private application. For example, you can define a public hostname (<code>mywebapp.example.com</code>) to provide access to a web server running on <code>https://localhost:8080</code>. When a user goes to <code>mywebapp.example.com</code> in their browser, their request will first route to a Cloudflare data center where it is inspected against your configured security policies. Cloudflare will then forward validated requests down your tunnel to the web server.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/handshake.jpg" alt="How an HTTP request reaches a private application connected with Cloudflare Tunnel" /></p>
<h2 id="create-a-tunnel">Create a tunnel</h2>
<p>To create a Cloudflare Tunnel:</p>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, <code>enterprise-VPC-01</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system, then copy the installation command and run it in a terminal on your origin server.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
</ol>
<h2 id="publish-an-application">Publish an application</h2>
<p>After creating your tunnel, add a published application route:</p>
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>, then select your tunnel.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</p>
</li>
<li>
<p>Enter a subdomain and select a <strong>Domain</strong> from the drop-down menu. Specify any subdomain or path information.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9684.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-routing">Path routing</h3>
@markup("md", "content/.markup/bodies/9683.md")
</aside>
<ol start="4">
<li>
<p>In <strong>Service URL</strong>, enter the protocol and address of your application (for example, <code>http://localhost:8000</code>). Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/">supported protocols</a> for available options.</p>
<p>If your origin already serves HTTPS or redirects HTTP to HTTPS, refer to <a href="/tunnel/troubleshooting/https-origins/">Troubleshoot HTTPS origins with Cloudflare Tunnel</a> before choosing the service URL.</p>
</li>
<li>
<p>Select <strong>Add route</strong>.</p>
</li>
</ol>
<p>All users on the Internet can now connect to this application via its public hostname. In <a href="/learning-paths/clientless-access/access-application/">Module 4: Secure your applications</a>, we will discuss how to restrict access to authorized users.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9682.md")
</aside>
<h2 id="additional-resources">Additional resources</h2>
<p>For more control over how traffic routes through your tunnel, refer to the following links:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/">DNS records</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/">Load balancer</a></li>
</ul>
