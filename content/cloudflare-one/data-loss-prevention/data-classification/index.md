---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/
  description: Understand how Data Classification works in Cloudflare DLP.
  full_title: Data classification · Cloudflare One docs
  head_html: <title>Data classification · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how Data Classification works in Cloudflare DLP."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/index.md"><meta property="og:title" content="Data classification · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how Data Classification works in Cloudflare DLP."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/#page","headline":"Data classification \u00b7 Cloudflare One docs","description":"Understand how Data Classification works in Cloudflare DLP.","url":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/data-loss-prevention/data-classification/
  schema: 1
---
<p>Data Classification extends Cloudflare DLP with a reusable layer for identifying, organizing, and labeling sensitive content. Instead of building all detection logic directly inside a DLP profile, you can define labels and reusable classification rules, then apply them in custom DLP profiles.</p>
<h2 id="what-is-data-classification">What is Data Classification?</h2>
<p>With Data Classification, you can:</p>
<ul>
<li>Define labels such as sensitivity levels and data tags</li>
<li>Use templates as a starting point for those labels</li>
<li>Build reusable data classes that combine multiple signals into a single classification rule</li>
</ul>
<p>This is useful when you want more than direct inspection. Detection entries help identify sensitive content. Data Classification helps organize and label that content so administrators can identify its severity and apply it consistently across DLP profiles.</p>
<p>Templates provide Cloudflare-managed starting points for sensitivity schemas and data tag groups. When you build from a template, Cloudflare creates a new object in your account that you can edit.</p>
<h2 id="how-data-classification-fits-with-dlp">How Data Classification fits with DLP</h2>
<p>Data Classification works alongside detection entries and DLP profiles.</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>What it does</th>
</tr>
</thead>
<tbody>
<tr>
<td>Detection entries</td>
<td>Detect specific content such as patterns, datasets, document fingerprints, AI prompt topics, and predefined detections.</td>
</tr>
<tr>
<td>Labels</td>
<td>Define sensitivity schemas, sensitivity levels, data tag groups, and data tags used to describe matched content.</td>
</tr>
<tr>
<td>Templates</td>
<td>Provide Cloudflare-managed starting points for sensitivity schemas and data tag groups.</td>
</tr>
<tr>
<td>Data classes</td>
<td>Build reusable classification rules from detection entries, other data classes, sensitivity levels, and data tags.</td>
</tr>
<tr>
<td>DLP profiles</td>
<td>Apply detection and classification logic to DLP scanning and enforcement workflows.</td>
</tr>
</tbody>
</table>
<p>In general, detection entries help identify sensitive content. Data Classification helps organize and label that content so administrators can identify its severity, understand where it exists, and apply it consistently. DLP profiles then apply that logic to scanning and enforcement workflows.</p>
<h2 id="when-to-use-data-classification-vs-dlp-profiles">When to use Data Classification vs DLP profiles</h2>
<p>Use detection entries and DLP profiles when you want direct detection and enforcement. For example, if you want to detect a specific regex, dataset, or predefined detection and immediately use it in a policy, building directly with detection entries may be enough.</p>
<p>Use Data Classification when you want a more reusable and structured model. For example, Data Classification is a better fit when you want to:</p>
<ul>
<li>standardize sensitivity labels across multiple detections</li>
<li>organize related detections into a reusable data class</li>
<li>combine multiple signals into a single classification rule</li>
<li>reuse the same classification logic across multiple DLP profiles</li>
</ul>
<p>In summary, use DLP profiles when you want enforcement. Use Data Classification when you want to organize and label sensitive content in a reusable way before applying that logic in DLP workflows.</p>
<h2 id="next-steps">Next steps</h2>
<p>To get started:</p>
<ul>
<li><a href="/cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/">Configure labels and templates</a> — Create labels and build from Cloudflare-managed templates.</li>
<li><a href="/cloudflare-one/data-loss-prevention/data-classification/build-a-data-class/">Build a data class</a> — Create reusable classification rules and apply them in custom DLP profiles.</li>
<li><a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Configure DLP profiles</a> — Apply detection entries, data classes, and labels in DLP scanning workflows.</li>
</ul>
