---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/
  description: Maintain and update documentation images.
  full_title: Image maintenance · Cloudflare Style Guide
  head_html: <title>Image maintenance · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Maintain and update documentation images."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/index.md"><meta property="og:title" content="Image maintenance · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Maintain and update documentation images."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/#page","headline":"Image maintenance \u00b7 Cloudflare Style Guide","description":"Maintain and update documentation images.","url":"https://developers.cloudflare.com/style-guide/how-we-docs/image-maintenance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/how-we-docs/image-maintenance/
  schema: 1
---
<p>Though valuable for user understanding, images are difficult to maintain. We have a few strategies that we use to help make this easier.</p>
<h2 id="guidelines">Guidelines</h2>
<p>We support a few different types of images in our docs, including:</p>
<ul>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/#diagrams">Diagrams</a></li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/#screenshots">Screenshots</a></li>
</ul>
<p>Of these, we prefer Mermaid diagrams because they are searchable and easily changeable. The &quot;cost&quot; of updating a Mermaid diagram is much lower than re-taking a screenshot or working with a designer to update a diagram.</p>
<h2 id="maintenance">Maintenance</h2>
<p>The best way to improve image maintenance is to avoid using them.</p>
<p>The other way to streamline maintenance is to remove images that are no longer referenced in your documentation. This pattern becomes particularly helpful if you need to audit images for UI changes or leaked information, because then you are not wasting time looking at unused images too.</p>
<p>We do that through a combination of GitHub actions.</p>
<h3 id="flag-unused-images">Flag unused images</h3>
<p>We have a specific GitHub action to <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/.github/workflows/image-audit.yml">flag unused images</a>.</p>
<p>What the GitHub action does is:</p>
<ol>
<li>Finds all <code>.png</code> or <code>.svg</code> files in our content.</li>
<li>Checks to see if those files are referenced in any of our MDX files.</li>
<li>Creates a <a href="https://github.com/cloudflare/cloudflare-docs/issues/23343">GitHub issue</a> if there are unreferenced files.</li>
</ol>
<h3 id="evaluate-image-paths">Evaluate image paths</h3>
<p>In combination with <a href="#flag-unused-images">flagging unused images</a>, we also have logic in our <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/astro.config.ts">build process</a> to validate image paths.</p>
<pre tabindex="0"><code class="language-ts">export default defineConfig({&#10;	site: &quot;https://developers.cloudflare.com&quot;,&#10;	markdown: {&#10;		smartypants: false,&#10;		remarkPlugins: [remarkValidateImages],&#10;		rehypePlugins: [&#10;			rehypeMermaid,&#10;			rehypeExternalLinks,&#10;			rehypeHeadingSlugs,&#10;			rehypeAutolinkHeadings,&#10;			// @ts-expect-error plugins types are outdated but functional&#10;			rehypeTitleFigure,&#10;			rehypeShiftHeadings,&#10;		],&#10;	},&#10;</code></pre>
<p>This ensures that the build-time <code>nimbus/image-ref</code> lint rule validates all image paths. If the path does not exist, we throw an error and prevent the site from building.</p>
<p>When paired with <a href="#flag-unused-images">flagging unused images</a>, this path validation ensures that a tech writer can safely delete unused files in a pull request. So long as the site builds correctly, you have only deleted image files that are not referenced anywhere.</p>
