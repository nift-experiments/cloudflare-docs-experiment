---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/how-we-docs/links/
  description: How we keep links healthy with build checks, external link auditing, and background anchor link audits.
  full_title: Link maintenance · Cloudflare Style Guide
  head_html: <title>Link maintenance · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="How we keep links healthy with build checks, external link auditing, and background anchor link audits."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/how-we-docs/links/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/how-we-docs/links/index.md"><meta property="og:title" content="Link maintenance · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How we keep links healthy with build checks, external link auditing, and background anchor link audits."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/how-we-docs/links/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/how-we-docs/links/#page","headline":"Link maintenance \u00b7 Cloudflare Style Guide","description":"How we keep links healthy with build checks, external link auditing, and background anchor link audits.","url":"https://developers.cloudflare.com/style-guide/how-we-docs/links/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/how-we-docs/links/
  schema: 1
---
<p>Though <a href="/style-guide/style-and-grammar/formatting/structure/links/">links</a> are an important part of documentation, they also have their own maintenance cost.</p>
<p>We have a few strategies we use to make link maintenance easier.</p>
<h2 id="link-types">Link types</h2>
<p>Documentation uses three <a href="/style-guide/style-and-grammar/formatting/structure/links/#types-of-links">types of links</a>: external, internal, and anchor. For each type, we think through a few different aspects of the experience.</p>
<ul>
<li><strong>External</strong>:
<ul>
<li><em>Source of truth</em>: Another site.</li>
<li><em>Why does it break</em>: Another site changed its content.</li>
<li><em>Customer experience of a break</em>: <code>404</code> page on another site.</li>
</ul>
</li>
<li><strong>Internal</strong>:
<ul>
<li><em>Source of truth</em>: Your site.</li>
<li><em>Why does it break</em>: Your site changed its content.</li>
<li><em>Customer experience of a break</em>: <code>404</code> page on your site.</li>
</ul>
</li>
<li><strong>Anchor</strong>:
<ul>
<li><em>Source of truth</em>: Your site.</li>
<li><em>Why does it break</em>: Your site changed its content.</li>
<li><em>Customer experience of a break</em>: Page load on your site. Content might be further down the page or have been moved to another page.</li>
</ul>
</li>
</ul>
<h2 id="checks">Checks</h2>
<h3 id="internal-links">Internal links</h3>
<p>Of these three <a href="#link-types">link types</a>, only <strong>Internal</strong> links:</p>
<ul>
<li>Happen <em>within</em> the context of a change to your site's content.</li>
<li>Universally lead to a bad customer experience (a <code>404</code> page).</li>
<li>Are easily auditable within the current context.</li>
</ul>
<p>For these reasons, we choose to make a build <strong>fail</strong> based on broken internal links. For our implementation, we rely on <a href="https://nimbus-docs.com/">Nimbus</a>'s <code>nimbus/internal-link</code> <a href="https://nimbus-docs.com/writing/linting/">lint rule</a>, configured in <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/astro.config.ts"><code>astro.config.ts</code></a>.</p>
<p>We also make two intentional decisions about this link auditing:</p>
<ul>
<li><strong>Absolute links, not relative</strong>: We enforce absolute links (<code>/style-guide/how-we-docs/metadata/</code>) and fail on relative links (<code>../metadata/</code>) to avoid time-consuming maintenance in the future. This decision also helps with find/replace work and any future platform migrations.</li>
<li><strong>No redirects</strong>: We do not consider redirects when evaluating links. We have the current source of truth, so we should utilize that truth to its fullest (as well as helping us avoid redirect chains and future maintenance).</li>
</ul>
<h3 id="external-links">External links</h3>
<p>Though external links are not good for the customer experience, they also don't change within the context of a change to your site's content. Additionally, external link checking can be time consuming and error prone, which can slow down contributions.</p>
<p>We use an external SEO tool to help flag these broken external links for us, addressing them as needed (instead of making a build fail because of them).</p>
<h3 id="anchor-links">Anchor links</h3>
<p>Anchor links do not have as dramatic as consequences of being wrong as internal links. If you have a broken anchor link, a customer will either need to manually scroll to the header or, in some cases, go to another page.</p>
<p>Because of these characteristics, we run <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/.github/workflows/anchor-link-audit.yml">periodic, background checks</a> to flag broken anchor links, using the <code>htmltest</code> library.</p>
