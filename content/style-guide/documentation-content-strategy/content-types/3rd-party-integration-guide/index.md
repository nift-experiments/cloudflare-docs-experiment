---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/
  description: Write third-party integration guides that connect an external product with Cloudflare, favoring links to the third party's own maintained documentation.
  full_title: 3rd-party integration guide · Cloudflare Style Guide
  head_html: <title>3rd-party integration guide · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Write third-party integration guides that connect an external product with Cloudflare, favoring links to the third party&#x27;s own maintained documentation."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/index.md"><meta property="og:title" content="3rd-party integration guide · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write third-party integration guides that connect an external product with Cloudflare, favoring links to the third party&#x27;s own maintained documentation."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/#page","headline":"3rd-party integration guide \u00b7 Cloudflare Style Guide","description":"Write third-party integration guides that connect an external product with Cloudflare, favoring links to the third party's own maintained documentation.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/content-types/3rd-party-integration-guide/
  schema: 1
---
<p>A third-party integration guide explains how to use a third-party product with Cloudflare. Because Cloudflare does not control the third party's interface, these guides carry real maintenance risk, so they favor linking to externally maintained documentation over reproducing another product's steps. The tone is instructional and straightforward.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a third-party integration guide when a reader needs to connect one specific external product with Cloudflare, and the integration is worth publishing with an ongoing maintenance commitment. It is not:</p>
<ul>
<li><strong>A how-to.</strong> A how-to documents a task entirely within Cloudflare, whereas an integration guide crosses into a third-party product Cloudflare does not control.</li>
<li><strong>A blog post.</strong> Publish an integration guide only with the expectation of maintenance. If you do not intend to maintain it, write a blog post instead.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: a short verb phrase in the second-person imperative that includes the third-party product name, not a gerund. If the integration is with a Cloudflare technology partner, add the partner component after the title.</li>
<li><strong>Description</strong>: name the third-party product and the Cloudflare product, state what the integration accomplishes, and note the key prerequisites.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Copy this skeleton and adapt it to your integration:</p>
<pre tabindex="0"><code>&#45;--&#10;title: &lt;Verb phrase naming the third-party product&gt;&#10;description: Connect &lt;third-party product&gt; with &lt;Cloudflare product&gt; to &lt;what the integration accomplishes&gt;.&#10;pcx_content_type: integration-guide&#10;sidebar:&#10;  order: 10&#10;products:&#10;  &#45; product-a&#10;&#45;--&#10;&#10;Introduce what the integration accomplishes and any considerations unique to the third party.&#10;&#10;&#35;# Prerequisites&#10;&#10;List what the reader needs on the third-party side before starting.&#10;&#10;&#35;# Set up the integration&#10;&#10;Give the steps that complete the integration, linking to the third party&#x27;s own documentation rather than reproducing its process.&#10;&#10;&#35;# Related links&#10;&#10;Point to the third party&#x27;s maintained documentation and the related Cloudflare product docs.&#10;</code></pre>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/introductions/#context"><strong>Context</strong></a> introduces what the steps accomplish and any considerations unique to the third party.</li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/prerequisites/"><strong>Prerequisites</strong></a> list what the reader needs on the third-party side before starting.</li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/steps-tasks-procedures/"><strong>Steps</strong></a> complete the integration, linking out for basic concepts rather than teaching them.</li>
<li><a href="/style-guide/style-and-grammar/formatting/structure/links/"><strong>Links</strong></a> point to the third party's own documentation, preferred over reproducing its process, and only to reputable sources.</li>
<li><strong>What does not fit:</strong> step-by-step instructions of the third-party product, which are discouraged because they go out of date the moment the third party changes. Screenshots of the third-party product are the most fragile of all, so avoid them and link to the externally maintained source instead.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre tabindex="0"><code class="language-yaml">pcx_content_type: integration-guide&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="maintenance-and-scope">Maintenance and scope</h2>
<p>Publish a third-party integration guide as post-sales, use-phase content, with the expectation that someone will maintain it. External guides cost more to maintain because Cloudflare does not control the third party's interface and does not get the same visibility into changes. If you want to publish something without that maintenance commitment, write a blog post instead. This content appears most often around <a href="/workers/tutorials/">Workers</a>, <a href="/cloudflare-one/integrations/identity-providers/">Zero Trust</a>, and <a href="/analytics/analytics-integrations/">Analytics</a> integrations.</p>
<h2 id="examples">Examples</h2>
<p>Integration handled in the Cloudflare dashboard:</p>
<ul>
<li><a href="/logs/logpush/logpush-job/enable-destinations/sumo-logic/">Enable Logpush to Sumo Logic</a></li>
<li><a href="/cloudflare-one/reusable-components/posture-checks/client-checks/carbon-black/">Device Posture - Carbon Black</a></li>
</ul>
<p>Linking out to external documentation:</p>
<ul>
<li><a href="/workers/tutorials/github-sms-notifications-using-twilio/#sending-a-text-with-twilio">GitHub SMS notifications using Twilio</a></li>
</ul>
<p>Instructions in both the third-party environment and the Cloudflare dashboard, which is discouraged but sometimes acceptable:</p>
<ul>
<li><a href="/cloudflare-one/integrations/identity-providers/entra-id/">IdP integration - Microsoft Entra ID</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jamf/">Managed deployment - Partners - Jamf</a></li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Link, do not reproduce.</strong> Point to the third party's own documentation for its steps, because reproduced instructions and screenshots go stale as soon as the external product changes.</li>
<li><strong>Complete prerequisites.</strong> State exactly what the reader needs on the third-party side before starting, because an agent cannot complete an integration it is not set up to reach.</li>
<li><strong>Name both products.</strong> Name the third-party product and the Cloudflare product in the title and context, so a reader or agent can match the guide to the integration they need.</li>
</ul>
