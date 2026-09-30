---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/faq/
  description: Write FAQ pages that answer common questions with short, direct responses and link out to the canonical how-to, tutorial, or glossary.
  full_title: FAQ · Cloudflare Style Guide
  head_html: <title>FAQ · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Write FAQ pages that answer common questions with short, direct responses and link out to the canonical how-to, tutorial, or glossary."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/faq/index.md"><meta property="og:title" content="FAQ · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write FAQ pages that answer common questions with short, direct responses and link out to the canonical how-to, tutorial, or glossary."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/faq/#page","headline":"FAQ \u00b7 Cloudflare Style Guide","description":"Write FAQ pages that answer common questions with short, direct responses and link out to the canonical how-to, tutorial, or glossary.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/content-types/faq/
  schema: 1
---
<p>An FAQ page collects common questions on a topic with short, direct answers, giving a reader a fast path to a single fact and improving the discoverability of the product. The tone is straightforward, educational, and authoritative.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write an FAQ only when a page is genuinely a list of questions with direct answers. If the list grows beyond roughly 10 questions, revisit whether some answers belong elsewhere in the documentation. It is not:</p>
<ul>
<li><strong>A how-to or tutorial.</strong> Procedural questions belong in a how-to or tutorial, whereas an FAQ calls out only a few common ones and links back to them.</li>
<li><strong>A glossary.</strong> Definition questions belong in the glossary, whereas an FAQ repeats only the essential, recurring definitions and links out.</li>
<li><strong>A troubleshooting page.</strong> A troubleshooting page catalogs errors and their fixes, whereas an FAQ surfaces only the most common issues as questions.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: the page title is FAQ. In a large multi-section FAQ, each child page takes the name of its section instead.</li>
<li><strong>Description</strong>: name the product and the key topic areas the questions cover.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Copy this skeleton and adapt it to your topic:</p>
<pre tabindex="0"><code>&#45;--&#10;title: FAQ&#10;description: Answers to common questions about &lt;product&gt;, covering &lt;the key topic areas&gt;.&#10;pcx_content_type: faq&#10;sidebar:&#10;  order: 10&#10;products:&#10;  &#45; product-a&#10;&#45;--&#10;&#10;Open with a short paragraph on the topic and what the reader can expect to find.&#10;&#10;&#35;# &lt;Question written in full from the reader&#x27;s point of view&gt;&#10;&#10;Lead with the direct answer, add one or two sentences of context, and link to the how-to, tutorial, or glossary that answers it in full.&#10;&#10;&#35;# &lt;Next question&gt;&#10;&#10;Answer completely and link out to the source of truth.&#10;</code></pre>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/introductions/#context"><strong>Context</strong></a> opens the page with a short paragraph on the topic and what the reader can expect to find.</li>
<li><a href="/style-guide/documentation-content-strategy/content-types/navigation/"><strong>Navigation</strong></a> lists the sections once an FAQ is large enough to need them, so a reader can jump to the right group.</li>
<li><a href="/style-guide/style-and-grammar/formatting/structure/links/"><strong>Links</strong></a> carry the reader from a called-out question to the how-to, tutorial, or glossary entry that answers it in full.</li>
<li><strong>What does not fit:</strong> long procedures or exhaustive definitions. Keep those in their canonical how-to, tutorial, or glossary and link to them.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre tabindex="0"><code class="language-yaml">pcx_content_type: faq&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="writing-questions-and-answers">Writing questions and answers</h2>
<p>Write each question in full and from the reader's point of view, using the first person. Prefer &quot;Can I use wildcards when creating policies?&quot; over &quot;Can users use wildcards when creating policies?&quot;. Answer completely, and when the question is phrased as yes or no, lead with the direct response before adding context. Prefer &quot;Yes. Cloudflare Access supports several providers simultaneously.&quot; over an answer that omits the leading &quot;Yes&quot;.</p>
<h2 id="question-types">Question types</h2>
<p>Most questions fall into one of five types, each with its own answer shape:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Question shape</th>
<th>How to answer</th>
</tr>
</thead>
<tbody>
<tr>
<td>Yes/No</td>
<td>&quot;Can I...&quot;, &quot;Does the product...&quot;</td>
<td>Lead with Yes or No, then one or two sentences of context</td>
</tr>
<tr>
<td>Procedural</td>
<td>&quot;How do I...&quot;, &quot;How does it work?&quot;</td>
<td>Give a concise answer, then link to the how-to or tutorial that covers it</td>
</tr>
<tr>
<td>Definition</td>
<td>&quot;What is...?&quot;</td>
<td>Give a short, dictionary-style definition, then link to the glossary</td>
</tr>
<tr>
<td>Scenario</td>
<td>&quot;What if...?&quot;</td>
<td>Say whether the product fits in the first sentence, add context, link out</td>
</tr>
<tr>
<td>Troubleshooting</td>
<td>&quot;I see...&quot;, &quot;It does not work when...&quot;</td>
<td>Give the reason, then short actionable steps, then link to deeper docs</td>
</tr>
</tbody>
</table>
<h2 id="structuring-larger-faqs">Structuring larger FAQs</h2>
<ul>
<li><strong>Small pages</strong>, up to about 10 questions, need no sections: a title, a context paragraph, then the questions and answers.</li>
<li><strong>Medium pages</strong> add section headings and a navigation menu that lists them.</li>
<li><strong>Large FAQs</strong>, for product suites such as Cloudflare One, split each section onto its own child page: the main page lists the sections with a one-line context and a button to each child page, and each child page carries its section's questions under breadcrumbs back to the landing page.</li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Full question text.</strong> Write each question with its complete text from the reader's point of view, because an agent matches on the whole question, not a truncated heading.</li>
<li><strong>Direct answers.</strong> Lead with the direct response, Yes or No where the question is yes/no, so a reader or agent gets the fact in the first sentence.</li>
<li><strong>Link to the source of truth.</strong> Point every procedural, definition, or scenario answer to its canonical how-to, tutorial, or glossary entry, because the FAQ is a shortcut, not the authority.</li>
</ul>
