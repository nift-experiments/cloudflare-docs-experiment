---
cp9:
  canonical: https://developers.cloudflare.com/version-management/how-to/compare-versions/
  description: View differences between configuration versions.
  full_title: Compare versions · Cloudflare Version Management docs
  head_html: <title>Compare versions · Cloudflare Version Management docs</title><meta name="generator" content="Nift"><meta name="description" content="View differences between configuration versions."><link rel="canonical" href="https://developers.cloudflare.com/version-management/how-to/compare-versions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/version-management/how-to/compare-versions/index.md"><meta property="og:title" content="Compare versions · Cloudflare Version Management docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View differences between configuration versions."><meta property="og:url" content="https://developers.cloudflare.com/version-management/how-to/compare-versions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Version Management"><meta name="algolia_product_filter" content="Version Management"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Version Management"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/version-management/how-to/compare-versions/#page","headline":"Compare versions \u00b7 Cloudflare Version Management docs","description":"View differences between configuration versions.","url":"https://developers.cloudflare.com/version-management/how-to/compare-versions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /version-management/how-to/compare-versions/
  schema: 1
---
<p>Quickly view differences between versions to make sure your configurations are correct before <a href="/version-management/how-to/environments/#change-environment-version">promoting a version</a> to a new environment.</p>
<p>A common use case would be to compare the versions in staging and production to verify the changes before promoting the staging version to production.</p>
<p>To compare versions:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and zone.</li>
<li>Go to <strong>Version Management</strong> &gt; <strong>Comparisons</strong>.</li>
<li>Select two different versions.</li>
<li>Select <strong>Compare</strong>.</li>
</ol>
<p>After a few seconds, the page will update automatically with a comparison on a per-product basis. The lower numbered version will always be presented on the left and the top will show you which environments the versions are assigned to so that you can ensure you are comparing the right versions.</p>
<p><img src="/assets/upstream/images/version-management/compare-versions.png" alt="View changes side-by-side between versions" /></p>
<p>Changes will be highlighted for new additions and removals for that service. Based on the comparison, you can then decide if more changes are necessary or if that new version is ready to be rolled out.</p>
