---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/
  description: Understand Cloudflare's SDK lifecycle stages, supported language runtimes, and ecosystem support commitments.
  full_title: SDK ecosystem support policy · Cloudflare Fundamentals docs
  head_html: <title>SDK ecosystem support policy · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand Cloudflare&#x27;s SDK lifecycle stages, supported language runtimes, and ecosystem support commitments."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/index.md"><meta property="og:title" content="SDK ecosystem support policy · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand Cloudflare&#x27;s SDK lifecycle stages, supported language runtimes, and ecosystem support commitments."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/#page","headline":"SDK ecosystem support policy \u00b7 Cloudflare Fundamentals docs","description":"Understand Cloudflare's SDK lifecycle stages, supported language runtimes, and ecosystem support commitments.","url":"https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/sdk-ecosystem-support-policy/
  schema: 1
---
<h2 id="lifecycle">Lifecycle</h2>
<p>Unless otherwise stated in the code repository, Cloudflare only provides active support for the latest major version of a library or tool. The exception to this policy is for critical security fixes, which will be reviewed on a case-by-case basis and take the vulnerability, impact, and mitigation required into consideration.</p>
<p>We provide three primary stages of development: early access, active support, and end of life.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8774.md")
</aside>
<h3 id="early-access">Early access</h3>
<p>During this stage, Cloudflare makes SDK changes available that we are seeking feedback on prior to releasing for general usage. Early access will  often include warning labels or caveats on functionality that is subject to change without notice. In general, early access SDKs are not suitable for production systems unless explicitly mentioned.</p>
<h3 id="active-support">Active support</h3>
<p>During the active support stage, planned changes and support are offered for the library or tool.</p>
<h3 id="end-of-life">End of life</h3>
<p>During the end of life stage, a new major version of the library or tool is released and Cloudflare marks the previous major version as no longer receiving improvements or bug fixes. If you continue to run end of life versions, support will be very limited.</p>
<p><img src="/assets/upstream/images/fundamentals/support-policy.png" alt="All lifecycle stages and their relation to one another" title="All lifecycle stages and their relation to one another" /></p>
<h2 id="previous-or-end-of-life-versions">Previous or end of life versions</h2>
<p>While Cloudflare cannot provide support for all older versions of our libraries or tools, we do not remove those versions so they can continued to be used without direct support.</p>
<h2 id="versioning">Versioning</h2>
<p>The SDK ecosystem follows semantic versioning, which defines versions as follows:</p>
<ul>
<li>MAJOR version when there are backward-incompatible changes made.</li>
<li>MINOR version when functionality is added in a backward compatible-manner.</li>
<li>PATCH version for backward-compatible bug fixes (without any improvements).</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8773.md")
</aside>
<p>Depending on your needs, you should ensure your application's package manager versioning is configured correctly. At a minimum, restrict installation to the current major version of the library or tool you are using to prevent any major version upgrades occurring automatically.</p>
<h2 id="migration">Migration</h2>
<p>Where possible, Cloudflare provides an automated approach to performing major version upgrades to limit the disruption using codemods. Review the library or tool-specific release notes for how to use these migration tools.</p>
<p>Alongside the automatic migration approach, we provide documentation on the changes that have taken place in case you need to make the changes manually.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://semver.org/">Semantic versioning definitions</a></li>
<li><a href="/terraform/">Cloudflare's Terraform documentation</a></li>
</ul>
