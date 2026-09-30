---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/how-we-docs/metadata/
  description: Manage documentation page metadata.
  full_title: Metadata · Cloudflare Style Guide
  head_html: <title>Metadata · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Manage documentation page metadata."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/how-we-docs/metadata/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/how-we-docs/metadata/index.md"><meta property="og:title" content="Metadata · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage documentation page metadata."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/how-we-docs/metadata/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/how-we-docs/metadata/#page","headline":"Metadata \u00b7 Cloudflare Style Guide","description":"Manage documentation page metadata.","url":"https://developers.cloudflare.com/style-guide/how-we-docs/metadata/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/how-we-docs/metadata/
  schema: 1
---
<p>Page-level metadata - content type, associated products, last updated, word count - lets you take a broader, more strategic view of your content.</p>
<p>It helps you answer questions like the following:</p>
<ul>
<li>As a writer:
<ul>
<li>Am I missing something obvious in the content strategy?</li>
<li>What are some pages I should be updating right now?</li>
<li>How does X tutorial compare with all tutorials? Is it getting more traffic than the baseline?</li>
</ul>
</li>
<li>As a manager:
<ul>
<li>Are we over or underinvesting in a specific product area? Or a specific content type?</li>
<li>How does the traffic to this set of products compare to another?</li>
<li>How can I communicate broader trends to my stakeholders?</li>
</ul>
</li>
</ul>
<p>You cannot answer these questions without some level of rollup reporting, which you can only get through metadata.</p>
<h2 id="what-we-track">What we track</h2>
<p>At Cloudflare, we track the following information about different pages:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
<th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Description</strong></td>
<td>A 1-2 sentence summary that populates the <code>&lt;meta name=&quot;description&quot;&gt;</code> tag. Required for all pages with a <code>pcx_content_type</code>.</td>
<td>Refer to <a href="/style-guide/build-the-page/frontmatter/#writing-a-description">frontmatter guidance</a>.</td>
</tr>
<tr>
<td><strong>Product</strong></td>
<td>The top-level subfolder of the page.</td>
<td><code>dns</code>, <code>bots</code></td>
</tr>
<tr>
<td><strong>Product Group</strong></td>
<td>The primary area that each product falls into.</td>
<td><code>Application Performance</code>, <code>Developer Platform</code></td>
</tr>
<tr>
<td><strong>Content type</strong></td>
<td>The primary purpose of the page, which corresponds to our listed <a href="/style-guide/documentation-content-strategy/content-types/">content types</a>.</td>
<td><code>how-to</code>, <code>faq</code></td>
</tr>
<tr>
<td><strong>Last modified</strong></td>
<td>How many days ago was this page last updated?</td>
<td><code>63</code></td>
</tr>
<tr>
<td><strong>Last reviewed</strong> (optional)</td>
<td>How many days ago was this page last reviewed?</td>
<td><code>100</code></td>
</tr>
</tbody>
</table>
<p>Of all of these values, there is a bit of nuance to our <strong>Last reviewed</strong> metadata. <strong>Last reviewed</strong> differs from <strong>Last modified</strong> because a review is more thorough than an update. A review implies that all contents of the page have been vetted for accuracy.</p>
<p>Because of this extra effort, we only track <strong>Last reviewed</strong> for content types that are particularly important to the user journey and require an additional level of maintenance. At the moment, those content types are <a href="/style-guide/documentation-content-strategy/content-types/tutorial/">tutorials</a>.</p>
<hr />
<h2 id="how-we-track">How we track</h2>
<p>We set these values at two different levels, the folder level and the page level.</p>
<h3 id="folder-level-attributes">Folder-level attributes</h3>
<p>We set two values at a folder level, <code>Product</code> and <code>Product Group</code>. We take this approach because we can assume that these values apply every page within that folder.</p>
<p>For example, here's the content from our <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/content/products/dns.yaml">DNS folder</a>.</p>
<pre tabindex="0"><code class="language-yaml">name: DNS&#10;&#10;product:&#10;  title: DNS&#10;  url: /dns/&#10;  group: Application performance&#10;&#10;meta:&#10;  title: Cloudflare DNS docs&#10;  description: Cloudflare DNS provides the fastest, most resilient, and simplest&#10;    managed DNS platform to meet your needs.&#10;  author: &quot;@cloudflare&quot;&#10;&#10;resources:&#10;  community: https://community.cloudflare.com/tags/c/reliability/7/none&#10;  dashboard_link: https://dash.cloudflare.com/?to=/:account/:zone/dns&#10;  learning_center: https://www.cloudflare.com/learning/dns/what-is-dns/&#10;</code></pre>
<h3 id="page-level-attributes">Page-level attributes</h3>
<p>We primarily set page-level attributes through the <a href="/style-guide/build-the-page/frontmatter/custom-properties/">page's frontmatter</a>.</p>
<p>For example, here are the values set for our <a href="/workers/tutorials/build-a-slackbot/">Build a Slackbot tutorial</a>.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;updated: 2024-06-05&#10;difficulty: Beginner&#10;pcx_content_type: tutorial&#10;title: Build a Slackbot&#10;tags:&#10;  &#45; Hono&#10;languages:&#10;  &#45; TypeScript&#10;&#45;--&#10;</code></pre>
<p>However, the <code>last_modified</code> value is pulled automatically from the git history of a file.</p>
<p>At the page-level, the required <code>products</code> frontmatter lists relevant Cloudflare products, separately from the folder-level <code>Product</code> attribute.</p>
<hr />
<h2 id="how-we-use-values">How we use values</h2>
<p>We choose to render all of these values as specific <code>meta</code> properties for each page.</p>
<p>For example, these are the <code>meta</code> properties and values on the <a href="/ai-crawl-control/get-started/">AI Crawl Control - Get Started page</a>.</p>
<pre tabindex="0"><code class="language-html">&lt;meta name=&quot;pcx_content_group&quot; content=&quot;Core platform&quot; &gt;&#10;&lt;meta name=&quot;pcx_product&quot; content=&quot;AI Crawl Control&quot; &gt;&#10;&lt;meta name=&quot;pcx_content_type&quot; content=&quot;get-started&quot; &gt;&#10;&lt;meta name=&quot;pcx_last_modified&quot; content=&quot;7&quot; &gt;&#10;</code></pre>
<p>We render these values using a custom override for our <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/src/components/overrides/Head.astro"><code>Head.astro</code></a> file. If specific values are set, we then add them as meta tags onto the page.</p>
<pre tabindex="0"><code class="language-ts">		if (product.data.product.title) {&#10;			[&quot;pcx_product&quot;, &quot;algolia_product_filter&quot;].map((name) =&gt; {&#10;				metaTags.push({&#10;					name,&#10;					content: product.data.product.title,&#10;				});&#10;			});&#10;		}&#10;</code></pre>
<h3 id="benefits">Benefits</h3>
<p>We get two primary benefits from structuring our content this way.</p>
<p>First, our metadata is easily consumable by anyone who crawls our pages. We started using these values for our Algolia search configuration and internal reporting, but have since expanded to sharing this data with other teams that consume our content for AI systems too.</p>
<p>Additionally, this decisions means that our GitHub repo is always the source of truth. We do not have to keep a spreadsheet or mapping updated elsewhere, the source of truth is always in our repo and - by extension - a lot more likely to be accurate than if we maintained multiple sources of truth.</p>
<hr />
<h2 id="description-and-ai-retrievability">Description and AI retrievability</h2>
<p>The <code>description</code> frontmatter field populates the <code>&lt;meta name=&quot;description&quot;&gt;</code> tag in the HTML head. This is the single most important metadata field for AI retrievability. Search engines, AI crawlers, and <code>llms.txt</code> frontmatter blocks consume this value when deciding whether to cite a page.</p>
<p>Every page with a <code>pcx_content_type</code> must include a <code>description</code>. A strong description names the product, states what the page helps the reader do, and works as a standalone answer snippet when extracted from the page.</p>
<p>For writing guidance and examples, refer to <a href="/style-guide/build-the-page/frontmatter/#writing-a-description">Writing a description</a>.</p>
<p>For more on how we make content available to AI systems, refer to <a href="/style-guide/how-we-docs/ai-consumability/">AI consumability</a>.</p>
<hr />
<h2 id="how-we-ensure-quality">How we ensure quality</h2>
<p>It's difficult to avoid errors with this kind of metadata, specifically because we are relying on freeform text entry in the frontmatter of individual files.</p>
<p>We utilize <a href="https://zod.dev/">Zod schemas</a> heavily in our Astro site, which are defined in <a href="https://github.com/cloudflare/cloudflare-docs/tree/production/src/schemas"><code>src/schemas/</code></a>.</p>
<p>These allow us to provide <a href="https://docs.astro.build/en/reference/experimental-flags/content-intellisense/">Intellisense guidance</a> for contributors using IDEs for local development.</p>
<p><img src="/assets/upstream/images/style-guide/how-we-docs/intellisense.png" alt="Intellisense in action" /></p>
