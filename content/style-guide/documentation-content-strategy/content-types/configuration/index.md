---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/
  description: Write configuration pages that show the settings and values for a configuration-intensive feature so readers can copy the right setup.
  full_title: Configuration · Cloudflare Style Guide
  head_html: <title>Configuration · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Write configuration pages that show the settings and values for a configuration-intensive feature so readers can copy the right setup."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/index.md"><meta property="og:title" content="Configuration · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write configuration pages that show the settings and values for a configuration-intensive feature so readers can copy the right setup."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/#page","headline":"Configuration \u00b7 Cloudflare Style Guide","description":"Write configuration pages that show the settings and values for a configuration-intensive feature so readers can copy the right setup.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/content-types/configuration/
  schema: 1
---
<p>A configuration page shows the specific settings, values, and options for a configuration-intensive feature, so a reader can copy the right setup for their use case rather than follow a procedure. Also known as use cases, configurations are reference pages, not instructions. The tone is plain, descriptive, and straightforward.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a configuration when a feature is configuration-intensive, such as rules, and readers mainly need to know which settings and values produce a given outcome. It is not:</p>
<ul>
<li><strong>A how-to.</strong> A how-to walks through the steps to complete a task, whereas a configuration only shows the settings and values for a setup, with no procedural steps.</li>
<li><strong>A tutorial.</strong> A tutorial teaches through a guided project, whereas a configuration is a reference the reader consults for the right values, not a lesson.</li>
<li><strong>A reference.</strong> A reference exhaustively documents every parameter, whereas a configuration curates example setups for common use cases.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: noun-based, naming the feature being configured, because a configuration describes ways to set up a feature rather than guiding the reader toward a goal.</li>
<li><strong>Description</strong>: name the product or feature configured, the use case it serves, and the key settings or values covered.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Copy this skeleton and adapt it to your feature:</p>
<pre tabindex="0"><code>&#45;--&#10;title: &lt;Feature&gt; configuration&#10;description: Configure &lt;product or feature&gt; for &lt;use case&gt;, covering &lt;the key settings and values&gt;.&#10;pcx_content_type: configuration&#10;sidebar:&#10;  order: 10&#10;products:&#10;  &#45; product-a&#10;&#45;--&#10;&#10;Introduce the feature in two or three sentences, frame which configurations the reader will encounter, and link to related documentation.&#10;&#10;&#35;# &lt;Feature area&gt;&#10;&#10;State the outcome this configuration produces, then give the settings and values in a table.&#10;&#10;<table>&#10;&#10;<thead>&#10;<tr>&#10;<th>Setting</th>&#10;<th>Value</th>&#10;<th>Notes</th>&#10;</tr>&#10;</thead>&#10;<tbody>&#10;<tr>&#10;<td>&lt;setting name&gt;</td>&#10;<td>&lt;value to enter or select&gt;</td>&#10;<td>&lt;when to use it&gt;</td>&#10;</tr>&#10;</tbody>&#10;&#10;</table>&#10;</code></pre>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/style-and-grammar/formatting/structure/tables/"><strong>Tables</strong></a> are the signature: a reference table with a 1:1 correspondence between each setting the reader can change and the value to enter or select for a given use case.</li>
<li><a href="/style-guide/documentation-content-strategy/content-types/navigation/"><strong>Navigation</strong></a> helps readers find the right configuration when a feature has many.</li>
<li><strong>What does not fit:</strong> step-by-step procedures. If you find yourself writing instructions, use a <a href="/style-guide/documentation-content-strategy/content-types/how-to/">how-to</a>, <a href="/style-guide/documentation-content-strategy/content-types/tutorial/">tutorial</a>, or <a href="/style-guide/documentation-content-strategy/component-attributes/examples/">example</a> instead.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre tabindex="0"><code class="language-yaml">pcx_content_type: configuration&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="organizing-configurations">Organizing configurations</h2>
<p>Open each configuration with a short context paragraph after the title that introduces the feature, frames which configurations the reader will encounter, and links to related documentation. Group the body by feature, giving each feature its own settings table so the reader can scan to the setup that matches their use case.</p>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Complete setting-value pairs.</strong> Give every table row an explicit setting and the exact value to enter or select, because an agent applies the pair directly with no room to infer.</li>
<li><strong>Use-case framing.</strong> State the outcome each configuration produces in its context, so a reader or agent can match a goal to the right table without reading a procedure.</li>
<li><strong>Instructions point outward.</strong> Link to the how-to, tutorial, or example that carries any steps, because a configuration itself is not executable as a procedure.</li>
</ul>
