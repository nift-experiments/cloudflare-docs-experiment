---
cp9:
  canonical: https://developers.cloudflare.com/containers/configuration/environment-variables/
  description: Runtime and user-defined environment variables available inside Container instances.
  full_title: Environment Variables · Cloudflare Containers docs
  head_html: <title>Environment Variables · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Runtime and user-defined environment variables available inside Container instances."><link rel="canonical" href="https://developers.cloudflare.com/containers/configuration/environment-variables/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/configuration/environment-variables/index.md"><meta property="og:title" content="Environment Variables · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Runtime and user-defined environment variables available inside Container instances."><meta property="og:url" content="https://developers.cloudflare.com/containers/configuration/environment-variables/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/configuration/environment-variables/#page","headline":"Environment Variables \u00b7 Cloudflare Containers docs","description":"Runtime and user-defined environment variables available inside Container instances.","url":"https://developers.cloudflare.com/containers/configuration/environment-variables/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/configuration/environment-variables/
  schema: 1
---
<h2 id="runtime-environment-variables">Runtime environment variables</h2>
<p>The container runtime automatically sets the following variables:</p>
<ul>
<li><code>CLOUDFLARE_APPLICATION_ID</code> - the ID of the Containers application</li>
<li><code>CLOUDFLARE_COUNTRY_A2</code> - the <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2 code</a> of a country the container is placed in</li>
<li><code>CLOUDFLARE_LOCATION</code> - a name of a location the container is placed in</li>
<li><code>CLOUDFLARE_REGION</code> - a region name</li>
<li><code>CLOUDFLARE_DURABLE_OBJECT_ID</code> - the ID of the Durable Object instance that the container is bound to. You can use this to identify particular container instances on the dashboard.</li>
</ul>
<h2 id="user-defined-environment-variables">User-defined environment variables</h2>
<p>You can set environment variables when defining a Container in your Worker, or when starting a container instance.</p>
<p>For example:</p>
<pre tabindex="0"><code class="language-javascript">class MyContainer extends Container {&#10;	defaultPort = 4000;&#10;	envVars = {&#10;		MY_CUSTOM_VAR: &quot;value&quot;,&#10;		ANOTHER_VAR: &quot;another_value&quot;,&#10;	};&#10;}&#10;</code></pre>
<p>More details about defining environment variables and secrets can be found in <a href="/containers/examples/env-vars-and-secrets">this example</a>.</p>
