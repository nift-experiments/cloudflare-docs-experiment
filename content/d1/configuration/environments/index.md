---
cp9:
  canonical: https://developers.cloudflare.com/d1/configuration/environments/
  description: Configure separate D1 databases for staging and production Wrangler environments.
  full_title: Environments · Cloudflare D1 docs
  head_html: <title>Environments · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure separate D1 databases for staging and production Wrangler environments."><link rel="canonical" href="https://developers.cloudflare.com/d1/configuration/environments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/configuration/environments/index.md"><meta property="og:title" content="Environments · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure separate D1 databases for staging and production Wrangler environments."><meta property="og:url" content="https://developers.cloudflare.com/d1/configuration/environments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/configuration/environments/#page","headline":"Environments \u00b7 Cloudflare D1 docs","description":"Configure separate D1 databases for staging and production Wrangler environments.","url":"https://developers.cloudflare.com/d1/configuration/environments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/configuration/environments/
  schema: 1
---
<p><a href="/workers/wrangler/environments/">Environments</a> are different contexts that your code runs in. Cloudflare Developer Platform allows you to create and manage different environments. Through environments, you can deploy the same project to multiple places under multiple names.</p>
<p>To specify different D1 databases for different environments, use the following syntax in your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7366.md")
</div>
<p>In the code above, the <code>staging</code> environment is using a different database (<code>DATABASE_NAME_1</code>) than the <code>production</code> environment (<code>DATABASE_NAME_2</code>).</p>
<h2 id="anatomy-of-wrangler-file">Anatomy of Wrangler file</h2>
<p>If you need to specify different D1 databases for different environments, your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> may contain bindings that resemble the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7367.md")
</div>
<p>In the above configuration:</p>
<ul>
<li><code>[[env.production.d1_databases]]</code> creates an object <code>production</code> under <code>env</code> with a property <code>d1_databases</code>, where <code>d1_databases</code> is an array of objects, since you can create multiple D1 bindings in case you have more than one database.</li>
<li>Any property below the line in the form <code>&lt;key&gt; = &lt;value&gt;</code> is a property of an object within the <code>d1_databases</code> array.</li>
</ul>
<p>Therefore, the above binding is equivalent to:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;env&quot;: {&#10;    &quot;production&quot;: {&#10;      &quot;d1_databases&quot;: [&#10;        {&#10;          &quot;binding&quot;: &quot;DB&quot;,&#10;          &quot;database_name&quot;: &quot;DATABASE_NAME&quot;,&#10;          &quot;database_id&quot;: &quot;DATABASE_ID&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h3 id="example">Example</h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7368.md")
</div>
<p>The above is equivalent to the following structure in JSON:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;env&quot;: {&#10;    &quot;production&quot;: {&#10;      &quot;d1_databases&quot;: [&#10;        {&#10;          &quot;binding&quot;: &quot;BINDING_NAME_2&quot;,&#10;          &quot;database_id&quot;: &quot;UUID_2&quot;,&#10;          &quot;database_name&quot;: &quot;DATABASE_NAME_2&quot;&#10;        }&#10;      ]&#10;    },&#10;    &quot;staging&quot;: {&#10;      &quot;d1_databases&quot;: [&#10;        {&#10;          &quot;binding&quot;: &quot;BINDING_NAME_1&quot;,&#10;          &quot;database_id&quot;: &quot;UUID_1&quot;,&#10;          &quot;database_name&quot;: &quot;DATABASE_NAME_1&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#10;}&#10;</code></pre>
