---
cp9:
  canonical: https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/
  description: Configurable parameters for response header modification rules.
  full_title: API parameter reference · Cloudflare Rules docs
  head_html: <title>API parameter reference · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Configurable parameters for response header modification rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/index.md"><meta property="og:title" content="API parameter reference · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configurable parameters for response header modification rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Headers,Response modification"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/#page","headline":"API parameter reference \u00b7 Cloudflare Rules docs","description":"Configurable parameters for response header modification rules.","url":"https://developers.cloudflare.com/rules/transform/response-header-modification/reference/parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers","Response modification"]}</script>
  markdown: true
  noindex: false
  route: /rules/transform/response-header-modification/reference/parameters/
  schema: 1
---
<p>To set an HTTP response header, overwriting any headers with the same name, use the following parameters in the <code>action_parameters</code> field:</p>
<ul>
<li><strong>operation</strong>: <code>set</code></li>
<li>Include one of the following parameters to define a static or dynamic value:
<ul>
<li><strong>value</strong>: Specifies a static value for the HTTP response header.</li>
<li><strong>expression</strong>: Specifies the expression that defines a value for the HTTP response header.</li>
</ul>
</li>
</ul>
<p>To add an HTTP response header, keeping any existing headers with the same name, use the following parameters in the <code>action_parameters</code> field:</p>
<ul>
<li><strong>operation</strong>: <code>add</code></li>
<li>Include one of the following parameters to define a static or dynamic value:
<ul>
<li><strong>value</strong>: Specifies a static value for the HTTP response header.</li>
<li><strong>expression</strong>: Specifies the expression that defines a value for the HTTP response header.</li>
</ul>
</li>
</ul>
<p>To remove an HTTP response header, set the following parameter in the <code>action_parameters</code> field:</p>
<ul>
<li><strong>operation</strong>: <code>remove</code></li>
</ul>
<h2 id="static-header-value-parameters">Static header value parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to define a static HTTP response header value is the following:</p>
<pre tabindex="0"><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;&lt;set|add&gt;&quot;,&#10;      &quot;value&quot;: &quot;&lt;URI_PATH_VALUE&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="dynamic-header-value-parameters">Dynamic header value parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to define a dynamic HTTP response header value using an expression is the following:</p>
<pre tabindex="0"><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;&lt;set|add&gt;&quot;,&#10;      &quot;expression&quot;: &quot;&lt;EXPRESSION&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13182.md")
</aside>
<h2 id="header-removal-parameters">Header removal parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to remove an HTTP response header is the following:</p>
<pre tabindex="0"><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;remove&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="different-header-modifications-in-the-same-rule">Different header modifications in the same rule</h2>
<p>The same rule can modify different HTTP response headers using different operations. For example, a single rule can set the value of a header and remove a different header. The syntax of such a rule could be the following:</p>
<pre tabindex="0"><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME_1&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;set&quot;,&#10;      &quot;value&quot;: &quot;&lt;HEADER_VALUE_1&gt;&quot;&#10;    },&#10;    &quot;&lt;HEADER_NAME_2&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;remove&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
