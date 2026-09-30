---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/
  description: Control which parts of a crawled page are indexed by pairing URL glob patterns with CSS selectors.
  full_title: Content selectors · Cloudflare AI Search docs
  head_html: <title>Content selectors · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Control which parts of a crawled page are indexed by pairing URL glob patterns with CSS selectors."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/index.md"><meta property="og:title" content="Content selectors · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control which parts of a crawled page are indexed by pairing URL glob patterns with CSS selectors."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/#page","headline":"Content selectors \u00b7 Cloudflare AI Search docs","description":"Control which parts of a crawled page are indexed by pairing URL glob patterns with CSS selectors.","url":"https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/configuration/data-source/website/content-selectors/
  schema: 1
---
<p>Content selectors let you control which parts of a crawled page are indexed. Each entry pairs a URL glob pattern with a CSS selector. When a page URL matches a glob pattern, only the elements matching the corresponding CSS selector, and their descendants, are extracted and converted to Markdown for indexing.</p>
<p>The list is ordered and the <strong>first matching path wins</strong>. If a page URL matches multiple glob patterns, only the selector from the first match is applied. Order your entries from most specific to least specific.</p>
<h2 id="default-behavior">Default behavior</h2>
<p>Without content selectors, AI Search applies a default processing pipeline that removes elements such as <code>&lt;header&gt;</code>, <code>&lt;footer&gt;</code>, and <code>&lt;head&gt;</code> before converting the remaining content to Markdown. For more details on how HTML is processed, refer to <a href="/workers-ai/features/markdown-conversion/how-it-works/#html">How HTML is processed</a>.</p>
<h2 id="configure-in-the-dashboard">Configure in the dashboard</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3094.md")
</div>
<h2 id="configure-with-the-api">Configure with the API</h2>
<p>Content selectors are configured in the <code>source_params.web_crawler.parse_options.content_selector</code> field when creating or updating an AI Search instance. The field accepts an array of objects, each with a <code>path</code> and <code>selector</code> property.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;source&quot;: &quot;https://example.com&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_options&quot;: {&#10;          &quot;content_selector&quot;: [&#10;            {&#10;              &quot;path&quot;: &quot;**/blog/**&quot;,&#10;              &quot;selector&quot;: &quot;article .post-body&quot;&#10;            },&#10;            {&#10;              &quot;path&quot;: &quot;**/docs/**&quot;,&#10;              &quot;selector&quot;: &quot;main .content&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>path</code></td>
<td>string</td>
<td>Glob pattern to match against the full page URL. Uses the same glob syntax as <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>: <code>*</code> matches within a segment, <code>**</code> crosses directories. Maximum 200 characters.</td>
</tr>
<tr>
<td><code>selector</code></td>
<td>string</td>
<td>CSS selector to extract content from pages matching the path pattern. Supports standard CSS selectors including element, class, ID, and attribute selectors. Maximum 200 characters.</td>
</tr>
</tbody>
</table>
<h2 id="examples">Examples</h2>
<h3 id="extract-main-content-from-blog-pages">Extract main content from blog pages</h3>
<p>To index only the article body on blog pages and ignore navigation, sidebars, and footers:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>**/blog/**</code></td>
<td><code>article .post-body</code></td>
</tr>
</tbody>
</table>
<h3 id="target-documentation-content">Target documentation content</h3>
<p>To index the main content area of a documentation site:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>**/docs/**</code></td>
<td><code>main .content</code></td>
</tr>
</tbody>
</table>
<h3 id="different-selectors-for-different-sections">Different selectors for different sections</h3>
<p>You can define multiple entries to apply different selectors to different parts of your site. The first matching path wins, so place more specific patterns first:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>**/blog/releases/**</code></td>
<td><code>.release-notes</code></td>
</tr>
<tr>
<td><code>**/blog/**</code></td>
<td><code>article .post-body</code></td>
</tr>
<tr>
<td><code>**/docs/**</code></td>
<td><code>main .content</code></td>
</tr>
</tbody>
</table>
<p>In this example, a page at <code>https://example.com/blog/releases/v2</code> matches the first pattern and uses the <code>.release-notes</code> selector. A page at <code>https://example.com/blog/my-post</code> skips the first pattern and matches the second.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3093.md")
</aside>
<h2 id="interaction-with-other-features">Interaction with other features</h2>
<ul>
<li><strong>Path filtering</strong>: <a href="/ai-search/configuration/indexing/path-filtering/">Path filtering</a> takes priority over content selectors. Pages excluded by path filters are never crawled, so content selectors do not apply to them.</li>
<li><strong>Rendering mode</strong>: Content selectors apply to the HTML that AI Search receives. For sites that render content with JavaScript, use <a href="/ai-search/configuration/data-source/website/#rendering-mode">Rendered sites</a> mode so that selectors can target the fully rendered DOM.</li>
<li><strong>Automatic re-indexing</strong>: Updating content selectors triggers a new <a href="/ai-search/configuration/indexing/">sync job</a> immediately, so changes are applied to all indexed pages.</li>
</ul>
<h2 id="limits">Limits</h2>
<p>Refer to <a href="/ai-search/configuration/data-source/website/#limits">Website</a> for the limits that apply to content selectors.</p>
