---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/
  description: Reference for the deprecated classic Schema validation feature in API Shield.
  full_title: Configure Classic Schema validation (deprecated) · Cloudflare API Shield docs
  head_html: <title>Configure Classic Schema validation (deprecated) · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for the deprecated classic Schema validation feature in API Shield."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/index.md"><meta property="og:title" content="Configure Classic Schema validation (deprecated) · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for the deprecated classic Schema validation feature in API Shield."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/#page","headline":"Configure Classic Schema validation (deprecated) \u00b7 Cloudflare API Shield docs","description":"Reference for the deprecated classic Schema validation feature in API Shield.","url":"https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/reference/classic-schema-validation/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/3209.md")
</aside>
<p>Use the <strong>API Shield</strong> interface to configure <a href="/api-shield/security/schema-validation/">API Schema validation</a>, which validates requests according to the <span class="nb-glossary-tooltip" title="API schema">API schema</span> you provide.</p>
<p>Before you can configure Schema validation for an API, you must obtain an API Schema file matching our <a href="/api-shield/security/schema-validation/#specifications">specifications</a>.</p>
<p>If you are in the Schema validation 2.0, you can make changes to your settings but you cannot add any new Classic Schema validation schemas.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3208.md")
</aside>
<h2 id="create-an-api-shield-with-schema-validation">Create an API Shield with Schema validation</h2>
<p>To configure Schema validation in the Cloudflare dashboard:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Select <strong>Security</strong> &gt; <strong>API Shield</strong>.</li>
<li>Go to <strong>Schema validation</strong> and select <strong>Add schema</strong>.</li>
<li>Enter a descriptive name for your policy and optionally edit the expression to trigger Schema validation. For example, if your API is available at <code>http://api.example.com/v1</code>, include a check for the <em>Hostname</em> field — equal to <code>api.example.com</code> — and a check for the <em>URI Path</em> field using a regular expression — matching the regex <code>^/v1</code>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/3207.md")
</aside>
5. Select **Next**.
6. Upload your schema file.
7. Select **Save** to validate the content of the schema file and deploy the Schema validation rule. If you get a validation error, ensure that you are using one of the [supported file formats](/api-shield/security/schema-validation/#specifications) and that each endpoint and method pair has a unique operation ID.
<p>After deploying your API Shield rule, Cloudflare displays a summary of all <span class="nb-glossary-tooltip" title="API endpoint">API endpoints</span> organized by their protection level and actions that will occur for non-compliant and unprotected requests.</p>
<ol>
<li>In the <strong>Endpoint action</strong> dropdown, select an action for every request that targets a protected endpoint and fails Schema validation.</li>
<li>In the <strong>Fallthrough action</strong> dropdown, select an action for every request that targets an unprotected endpoint.</li>
<li>Optionally, you can save the endpoints to Endpoint Management at the same time the Schema is saved by selecting <strong>Save new endpoints to <a href="/api-shield/management-and-monitoring/">endpoint management</a></strong>. Endpoints will be saved regardless of whether the Schema is saved as a draft or published live.</li>
<li>Select <strong>Done</strong>.</li>
</ol>
