---
cp9:
  canonical: https://developers.cloudflare.com/support/third-party-software/others/configure-cloudflare-and-heroku-over-https/
  description: Set up Cloudflare with Heroku for HTTPS traffic.
  full_title: Configure Cloudflare and Heroku over HTTPS · Cloudflare Support docs
  head_html: <title>Configure Cloudflare and Heroku over HTTPS · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Cloudflare with Heroku for HTTPS traffic."><link rel="canonical" href="https://developers.cloudflare.com/support/third-party-software/others/configure-cloudflare-and-heroku-over-https/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/third-party-software/others/configure-cloudflare-and-heroku-over-https/index.md"><meta property="og:title" content="Configure Cloudflare and Heroku over HTTPS · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Cloudflare with Heroku for HTTPS traffic."><meta property="og:url" content="https://developers.cloudflare.com/support/third-party-software/others/configure-cloudflare-and-heroku-over-https/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/third-party-software/others/configure-cloudflare-and-heroku-over-https/#page","headline":"Configure Cloudflare and Heroku over HTTPS \u00b7 Cloudflare Support docs","description":"Set up Cloudflare with Heroku for HTTPS traffic.","url":"https://developers.cloudflare.com/support/third-party-software/others/configure-cloudflare-and-heroku-over-https/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/third-party-software/others/configure-cloudflare-and-heroku-over-https/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>Heroku is a cloud PaaS that supports several pre-configured programming languages. Heroku deals with all your infrastructure so you can focus on your application without having to work at the command line.</p>
<p>This article describes how to configure Heroku with Cloudflare to serve your traffic over HTTPS. For this article, we'll assume that you already have an <a href="/fundamentals/manage-domains/">active domain on Cloudflare</a>, as well as a running Heroku app.</p>
<hr />
<h2 id="step-1-add-a-custom-domain-to-your-heroku-app">Step 1 - Add a custom domain to your Heroku app</h2>
<p>Follow Heroku's instructions: <a href="https://devcenter.heroku.com/articles/custom-domains">Custom Domain Names for Apps</a>.</p>
<hr />
<h2 id="step-2-add-a-subdomain-in-cloudflare-dns">Step 2 - Add a subdomain in Cloudflare DNS</h2>
<p>Below, you will need to add DNS records for a subdomain and the apex domain (also known as &quot;root domain&quot;). Learn how to <a href="/dns/manage-dns-records/how-to/create-dns-records/">Managing DNS records in Cloudflare</a>.</p>
<h3 id="step-2a-add-a-subdomain">Step 2a - Add a subdomain</h3>
<p>In the Cloudflare dashboard, go to the <strong>DNS Records</strong> page.</p>
<div class="nb-dash-button"></div>
<p>Add a 'www' <em>CNAME</em> record that points to the custom domain (also known as <em>DNS target</em>) that you obtained in Step 1 above for your subdomain.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/14687.md")
</div>
<h3 id="step-2b-add-your-root-domain">Step 2b - Add your root domain</h3>
<p>Adding a root or apex domain on Heroku also requires using a CNAME record pointed from your root. You cannot use A records on Heroku because no IP addresses are exposed for Heroku users to use.</p>
<p>Fortunately, Cloudflare offers <a href="/dns/cname-flattening/">CNAME flattening</a> to resolve requests for your root domain.</p>
<p>Add a CNAME record for your root and point it to DNS target you obtained in Step 1 above for your domain.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/14688.md")
</div>
<hr />
<h2 id="step-3-confirm-that-your-domain-is-routed-through-cloudflare">Step 3 - Confirm that your domain is routed through Cloudflare</h2>
<p>The easiest way to confirm that Cloudflare is working for your domain is to issue a cURL command.</p>
<pre tabindex="0"><code class="language-sh">curl -I www.example.com&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">HTTP/1.1 200 OK&#10;Date: Tue, 23 Jan 2018 18:51:30 GMT&#10;Content-Type: text/html; charset=UTF-8&#10;Connection: keep-alive&#10;Cache-Control: public, max-age=0&#10;Last-Modified: Mon, 31 Dec 1979 04:08:00 GMT&#10;X-Powered-By: Express&#10;Server: cloudflare&#10;CF-RAY: 3e1cf1d936f28c52-SFO-DOG&#10;</code></pre>
<p>You can identify Cloudflare-proxied requests by the <em>CF-Ray</em> response header. If either of these two are present, your requests are being proxied by Cloudflare accordingly.</p>
<p>You can repeat the above cURL command for any of the subdomains that you have configured within your DNS settings.</p>
<hr />
<h2 id="step-4-configure-your-domain-for-ssl">Step 4 - Configure your domain for SSL</h2>
<h3 id="step-4a-enable-ssl">Step 4a - Enable SSL</h3>
<p>Cloudflare provides a SANs wildcard certificate with all paid plans, and a SNI wildcard certificate with the Free plan. Full details on SSL <a href="https://www.cloudflare.com/ssl">can be found here</a>.</p>
<p>If you don't know what this means, navigate to the <strong>Overview</strong> tab of the <strong>SSL/TLS</strong> app in your Cloudflare dashboard. Select <em>Flexible</em> mode to serve your site over HTTPS to all public visitors.</p>
<p>Once the certificate status changes to <strong>• Active Certificate</strong>, incoming traffic will be served to your site over HTTPS. Visitors will see HTTPS prefixed to your domain name in the browser bar.</p>
<h3 id="step-4b-force-all-traffic-over-https">Step 4b - Force all traffic over HTTPS</h3>
<p>To ensure all traffic to your site is encrypted, Cloudflare lets you force an automatic HTTPS redirect. To configure this, refer to <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a>.</p>
<p>You can then use a cURL command to verify that all requests are being forced over HTTPS.</p>
<pre tabindex="0"><code class="language-sh">curl -I -L example.com&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">HTTP/1.1 301 Moved Permanently&#10;Date: Tue, 23 Jan 2018 23:17:44 GMT&#10;Connection: keep-alive&#10;Cache-Control: max-age=3600&#10;Expires: Wed, 24 Jan 2018 00:17:44 GMT&#10;Location: https://example.com/&#10;Server: cloudflare&#10;CF-RAY: 3e1e77d5c42b8c52-SFO-DOG&#10;</code></pre>
<p>If SSL was not working for your domain (for example, your SSL certificate has not yet been issued), you would see a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/">525</a> or <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/">526</a> HTTP response after the redirect.</p>
<p>Please note that the issuing of a Universal SSL certificate typically takes up to 24 hours. Our paid SSL certificates issue within 10-15 minutes.</p>
