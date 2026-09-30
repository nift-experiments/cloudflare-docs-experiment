---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/branch-build-controls/
  description: Control which branches trigger automatic deployments in your Cloudflare Pages project.
  full_title: Branch deployment controls · Cloudflare Pages docs
  head_html: <title>Branch deployment controls · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Control which branches trigger automatic deployments in your Cloudflare Pages project."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/branch-build-controls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/branch-build-controls/index.md"><meta property="og:title" content="Branch deployment controls · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control which branches trigger automatic deployments in your Cloudflare Pages project."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/branch-build-controls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/branch-build-controls/#page","headline":"Branch deployment controls \u00b7 Cloudflare Pages docs","description":"Control which branches trigger automatic deployments in your Cloudflare Pages project.","url":"https://developers.cloudflare.com/pages/configuration/branch-build-controls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/branch-build-controls/
  schema: 1
---
<p>When connected to your git repository, Pages allows you to control which environments and branches you would like to automatically deploy to. By default, Pages will trigger a deployment any time you commit to either your production or preview environment. However, with branch deployment controls, you can configure automatic deployments to suit your preference on a per project basis.</p>
<h2 id="production-branch-control">Production branch control</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="direct-upload">Direct Upload</h3>
@markup("md", "content/.markup/bodies/11081.md")
</aside>
<p>To configure deployment options, go to your Pages project &gt; <strong>Settings</strong> &gt; <strong>Builds &amp; deployments</strong> &gt; <strong>Configure Production deployments</strong>. Pages will default to setting your production environment to the branch you first push, but you can set your production to another branch if you choose.</p>
<p>You can also enable or disable automatic deployment behavior on the production branch by checking the <strong>Enable automatic production branch deployments</strong> box. You must save your settings in order for the new production branch controls to take effect.</p>
<h2 id="preview-branch-control">Preview branch control</h2>
<p>When configuring automatic preview deployments, there are three options to choose from.</p>
<ul>
<li><strong>All non-Production branches</strong>: By default, Pages will automatically deploy any and every commit to a preview branch.</li>
<li><strong>None</strong>: Turns off automatic builds for all preview branches.</li>
<li><strong>Custom branches</strong>: Customize the automatic deployments of certain preview branches.</li>
</ul>
<h3 id="custom-preview-branch-control">Custom preview branch control</h3>
<p>By selecting <strong>Custom branches</strong>, you can specify branches you wish to include and exclude from automatic deployments in the provided configuration fields. The configuration fields can be filled in two ways:</p>
<ul>
<li><strong>Static branch names</strong>: Enter the precise name of the branch you are looking to include or exclude (for example, staging or dev).</li>
<li><strong>Wildcard syntax</strong>: Use wildcards to match multiple branches. You can specify wildcards at the start or end of your rule. The order of execution for the configuration is (1) Excludes, (2) Includes, (3) Skip. Pages will process the exclude configuration first, then go to the include configuration. If a branch does not match either then it will be skipped.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wildcard-syntax">Wildcard syntax</h3>
@markup("md", "content/.markup/bodies/11080.md")
</aside>
<p><strong>Example 1:</strong></p>
<p>If you want to enforce branch prefixes such as <code>fix/</code>, <code>feat/</code>, or <code>chore/</code> with wildcard syntax, you can include and exclude certain branches with the following rules:</p>
<ul>
<li>
<p>Include Preview branches:
<code>fix/*</code>, <code>feat/*</code>, <code>chore/*</code></p>
</li>
<li>
<p>Exclude Preview branches:
``</p>
</li>
</ul>
<p>Here Pages will include any branches with the indicated prefixes and exclude everything else. In this example, the excluding option is left empty.</p>
<p><strong>Example 2:</strong></p>
<p>If you wanted to prevent <a href="https://github.com/dependabot">dependabot</a> from creating a deployment for each PR it creates, you can exclude those branches with the following:</p>
<ul>
<li>
<p>Include Preview branches:
<code>*</code></p>
</li>
<li>
<p>Exclude Preview branches:
<code>dependabot/*</code></p>
</li>
</ul>
<p>Here Pages will include all branches except any branch starting with <code>dependabot</code>. In this example, the excluding option means any <code>dependabot/</code> branches will not be built.</p>
<p><strong>Example 3:</strong></p>
<p>If you only want to deploy release-prefixed branches, then you could use the following rules:</p>
<ul>
<li>
<p>Include Preview branches:
<code>release/*</code></p>
</li>
<li>
<p>Exclude Preview branches:
<code>*</code></p>
</li>
</ul>
<p>This will deploy only branches starting with <code>release/</code>.</p>
