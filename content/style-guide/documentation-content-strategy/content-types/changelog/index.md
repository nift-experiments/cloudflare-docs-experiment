---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/
  description: Write changelog pages that record notable, dated product changes, the single type for release notes and other product updates.
  full_title: Changelog · Cloudflare Style Guide
  head_html: <title>Changelog · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Write changelog pages that record notable, dated product changes, the single type for release notes and other product updates."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/index.md"><meta property="og:title" content="Changelog · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write changelog pages that record notable, dated product changes, the single type for release notes and other product updates."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/#page","headline":"Changelog \u00b7 Cloudflare Style Guide","description":"Write changelog pages that record notable, dated product changes, the single type for release notes and other product updates.","url":"https://developers.cloudflare.com/style-guide/documentation-content-strategy/content-types/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/documentation-content-strategy/content-types/changelog/
  schema: 1
---
<p>A changelog logs notable, dated changes to a product. The tone is instructional and straightforward.</p>
<p>This page covers how to write one. For the published updates themselves, refer to <a href="/changelog/">Changelog</a>.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a changelog when you need to record notable, dated changes to a product as an ongoing feed. It is not:</p>
<ul>
<li><strong>A blog post.</strong> A changelog entry is a short, factual record of one change, whereas a blog post explains and promotes at length.</li>
<li><strong>The documentation of a change.</strong> An entry records that something changed and links out, whereas the how-to, reference, or concept is where the change is actually documented.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: the page title is Changelog.</li>
<li><strong>Description</strong>: name the product and what the changelog tracks, such as recent changes, new features, and bug fixes.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Use the Nimbus changelog recipe to generate this page. Your coding agent pulls the full page skeleton and self-review checklist, then adapts them to your product:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx @cloudflare/nimbus-docs `add content-changelog`</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/nimbus-docs `add content-changelog`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn @cloudflare/nimbus-docs `add content-changelog`</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/nimbus-docs `add content-changelog`" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm @cloudflare/nimbus-docs `add content-changelog`</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/nimbus-docs `add content-changelog`" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Adapt the frontmatter the recipe emits to Cloudflare's schema: set <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a> and <code>products</code> instead of the generic fields the recipe emits, such as <code>type</code>.</p>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/build-the-page/components/product-changelog/"><strong>ProductChangelog</strong></a> renders a product's entries on the changelog page, pulling from the entries folder so the page stays current as entries are added.</li>
<li><strong>Entries</strong> are the body: each dated MDX file in the changelog collection is one notable change, with its own title, description, and date.</li>
<li><strong>What does not fit:</strong> long-form explanation or promotion. Keep an entry short and factual, and link to the how-to or concept that covers the change in depth.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre tabindex="0"><code class="language-yaml">pcx_content_type: changelog&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="ownership">Ownership</h2>
<p>Product managers and engineers maintain changelogs manually or through an automated process that their team owns. PCX provides a review but does not own creating or writing changelogs.</p>
<h2 id="building-a-changelog">Building a changelog</h2>
<p>A changelog needs an MDX page file and a corresponding folder of changelog entries. The combination of these files allows us to:</p>
<ul>
<li>Render traditional changelog content on an <a href="/dns/changelog/">HTML page</a>.</li>
<li>Programmatically create an <a href="/changelog/rss/dns.xml">RSS feed</a> with the changelog content.</li>
<li>Pull all our changelog content into a <a href="/changelog/">Cloudflare-wide changelog</a>.</li>
</ul>
<h3 id="changelog-page">Changelog page</h3>
<p>The MDX page needs several special values to pull in the changelog information, highlighted in the sample page. For more information about the ProductChangelog component, refer to <a href="/style-guide/build-the-page/components/product-changelog/">ProductChangelog</a>.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;pcx_content_type: changelog&#10;products:&#10;  &#45; dns&#10;title: Changelog&#10;description: Track recent changes, new features, and bug fixes for Cloudflare DNS.&#10;&#45;--&#10;&#10;import { ProductChangelog } from &quot;~/components&quot;;&#10;&#10;{/* &lt;!-- Actual content lives in /src/content/changelog/dns/. --&gt; */}&#10;&#10;&lt;ProductChangelog product=&quot;dns&quot; /&gt;&#10;</code></pre>
<h3 id="changelog-entries">Changelog entries</h3>
<p>Changelog entries live in a different location of our docs, <a href="https://github.com/cloudflare/cloudflare-docs/tree/production/src/content/changelog"><code>/src/content/changelog/</code></a>. Each entry is its own MDX file, similar to the following.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Account-level DNS analytics now available via GraphQL Analytics API&#10;description: Authoritative DNS analytics can now be accessed on the account level via the GraphQL Analytics API.&#10;products:&#10;  &#45; dns&#10;date: 2025-06-19&#10;&#45;--&#10;&#10;Authoritative DNS analytics are now available on the **account level** via the [Cloudflare GraphQL Analytics API](/analytics/graphql-api/).&#10;&#10;This allows users to query DNS analytics across multiple zones in their account, by using the `accounts` filter.&#10;&#10;Here is an example to retrieve all DNS queries across all zones in an account that resulted in an `NXDOMAIN` response over a given time frame. Please replace `a30f822fcd7c401984bf85d8f2a5111c` with your actual account ID.&#10;</code></pre>
<p>query Viewer {
viewer {
accounts(filter: { accountTag: &quot;a30f822fcd7c401984bf85d8f2a5111c&quot; }) {
dnsAnalyticsAdaptive(
limit: 10
filter: {
date_geq: &quot;2025-06-16&quot;
responseCode: &quot;NXDOMAIN&quot;
date_leq: &quot;2025-06-18&quot;
}
orderBy: [datetime_DESC]
) {
zoneTag
queryName
responseCode
queryType
datetime
}
}
}
}</p>
<pre tabindex="0"><code>&#10;To learn more and get started, refer to the [DNS Analytics documentation](/dns/additional-options/analytics/#analytics).&#10;</code></pre>
<h3 id="entry-properties">Entry properties</h3>
<p>Each changelog entry has the following properties:</p>
<ul>
<li><code>title</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>Shown in the title heading and on social media embeds.</li>
</ul>
</li>
<li><code>description</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>Shown in social media embeds.</li>
</ul>
</li>
<li><code>date</code> <span class="nb-type">date</span> <span class="nb-metainfo">required</span>
<ul>
<li>This should be a date in <code>YYYY-MM-DD</code> format. For example, <code>2025-02-04</code>.</li>
</ul>
</li>
<li><code>products</code> <span class="nb-type">Array&lt;String&gt;</span> <span class="nb-metainfo">(default: current location) required</span>
<ul>
<li>The products list is case-sensitive. Only use lowercase.</li>
<li>This should be an array of strings, each referring to the name of a file in the products collection without the file extension.</li>
<li>The folder that your entry is in, such as <code>src/content/changelog/workers/2025-02-13-new-product-feature.mdx</code>, is inferred as part of this property. If you do not want to associate the entry with additional products, you can omit it from the frontmatter entirely.</li>
<li>If you wish to reference a product that does not exist in this collection, such as one that resides in the subpath of an existing product, you can create a &quot;metadata only&quot; entry:</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-yaml">name: Workers Observability&#10;&#10;product:&#10;	title: Workers Observability&#10;	url: /workers/observability/&#10;	group: Developer platform&#10;	show: false&#10;</code></pre>
<ul>
<li><code>hidden</code> <span class="nb-type">Boolean</span> <span class="nb-metainfo">(default: false) optional</span>
<ul>
<li>If <code>true</code>, this page will be accessible from the direct link, but hidden from the main <a href="/changelog/">changelog</a> page and all RSS feeds.</li>
<li>If <code>true</code>, will also add a <code>noindex</code> property so the page is not indexed by search crawlers.</li>
</ul>
</li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Dated, atomic entries.</strong> Give each change its own dated entry with a title and description, because an agent extracts and orders changes by entry rather than by scanning prose.</li>
<li><strong>Literal dates and products.</strong> Use <code>YYYY-MM-DD</code> dates and exact product names in frontmatter, so a reader or agent can filter and sort the feed reliably.</li>
<li><strong>Link out for depth.</strong> Keep the entry to the change itself and link to the how-to or concept that explains it, because the changelog records what changed, not how to use it.</li>
</ul>
