---
cp9:
  canonical: https://developers.cloudflare.com/pages/configuration/preview-deployments/
  description: Preview new versions of your Cloudflare Pages project with unique URLs before deploying to production.
  full_title: Preview deployments · Cloudflare Pages docs
  head_html: <title>Preview deployments · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Preview new versions of your Cloudflare Pages project with unique URLs before deploying to production."><link rel="canonical" href="https://developers.cloudflare.com/pages/configuration/preview-deployments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/configuration/preview-deployments/index.md"><meta property="og:title" content="Preview deployments · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Preview new versions of your Cloudflare Pages project with unique URLs before deploying to production."><meta property="og:url" content="https://developers.cloudflare.com/pages/configuration/preview-deployments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/configuration/preview-deployments/#page","headline":"Preview deployments \u00b7 Cloudflare Pages docs","description":"Preview new versions of your Cloudflare Pages project with unique URLs before deploying to production.","url":"https://developers.cloudflare.com/pages/configuration/preview-deployments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/configuration/preview-deployments/
  schema: 1
---
<p>Preview deployments allow you to preview new versions of your project without deploying it to production. To view preview deployments:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your project and find the deployment you would like to view.</li>
</ol>
<p>Every time you open a new pull request on your GitHub repository, Cloudflare Pages will create a unique preview URL, which will stay updated as you continue to push new commits to the branch. This is only true when pull requests originate from the repository itself.</p>
<p><img src="/assets/upstream/images/pages/configuration/ghpreviewurls.png" alt="GitHub Preview URLs" /></p>
<p>For example, if you have a repository called <code>user-example</code> connected to Pages, this will give you a <code>user-example.pages.dev</code> subdomain. If <code>main</code> is your default branch, then any commits to the <code>main</code> branch will update your <code>user-example.pages.dev</code> content, as well as any <a href="/pages/configuration/custom-domains/">custom domains</a> attached to the project.</p>
<p><img src="/assets/upstream/images/pages/platform/preview-deployment-mergedone.png" alt="User-example repository's deployment status and preview" /></p>
<p>While developing <code>user-example</code>, you may push new changes to a <code>development</code> branch, for example.</p>
<p>In this example, after you create the new <code>development</code> branch, Pages will automatically generate a preview deployment for these changes available at <code>373f31e2.user-example.pages.dev</code> - where <code>373f31e2</code> is a randomly generated hash.</p>
<p>Each new branch you create will receive a new, randomly-generated hash in front of your <code>pages.dev</code> subdomain.</p>
<p><img src="/assets/upstream/images/pages/platform/preview-deployment-generated.png" alt="User-example repository's newly generated preview deployment link and status" /></p>
<p>Any additional changes to the <code>development</code> branch will continue to update this <code>373f31e2.user-example.pages.dev</code> preview address until the <code>development</code> branch is merged with the <code>main</code> production branch.</p>
<p>Any custom domains, as well as your <code>user-example.pages.dev</code> site, will not be affected by preview deployments.</p>
<h2 id="customize-preview-deployments-access">Customize preview deployments access</h2>
<p>You can use <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> to manage access to your deployment previews. By default, these deployment URLs are public. Enabling the access policy will restrict viewing project deployments to your Cloudflare account.</p>
<p>Once enabled, you can <a href="/fundamentals/manage-members/">set up a multi-user account</a> to allow other members of your team to view preview deployments.</p>
<p>By default, preview deployments are enabled and available publicly. In your project's settings, you can require visitors to authenticate to view preview deployment. This allows you to lock down access to these preview deployments to your teammates, organization, or anyone else you specify via <a href="/cloudflare-one/traffic-policies/">Access policies</a>.</p>
<p>To protect your preview deployments behind Cloudflare Access:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Pages project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>General</strong> &gt; and select <strong>Enable access policy</strong>.</li>
</ol>
<p>Note that this will only protect your preview deployments (for example, <code>373f31e2.user-example.pages.dev</code> and every other randomly generated preview link) and not your <code>*.pages.dev</code> domain or custom domain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11062.md")
</aside>
<h2 id="preview-aliases">Preview aliases</h2>
<p>When a preview deployment is published, it is given a unique, hash-based address — for example, <code>&lt;hash&gt;.&lt;project&gt;.pages.dev</code>. These are atomic and may always be visited in the future. However, Pages also creates an alias for <code>git</code> branch's name and updates it so that the alias always maps to the latest commit of that branch.</p>
<p>For example, if you push changes to a <code>development</code> branch (which is not associated with your Production environment), then Pages will deploy to <code>abc123.&lt;project&gt;.pages.dev</code> and alias <code>development.&lt;project&gt;.pages.dev</code> to it. Later, you may push new work to the <code>development</code> branch, which creates the <code>xyz456.&lt;project&gt;.pages.dev</code> deployment. At this point, the <code>development.&lt;project&gt;.pages.dev</code> alias points to the <code>xyz456</code> deployment, but <code>abc123.&lt;project&gt;.pages.dev</code> remains accessible directly.</p>
<p>Branch name aliases are lowercased and non-alphanumeric characters are replaced with a hyphen — for example, the <code>fix/api</code> branch creates the <code>fix-api.&lt;project&gt;.pages.dev</code> alias.</p>
<p>To view branch aliases within your Pages project, select <strong>View build</strong> for any preview deployment. <strong>Deployment details</strong> will display all aliases associated with that deployment.</p>
<p>You can attach a Preview alias to a custom domain by <a href="https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/">adding a custom domain to a branch</a>.</p>
<h2 id="delete-preview-deployments">Delete preview deployments</h2>
<p>To clean up old preview deployments, you can delete them using Wrangler:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages deployment delete &lt;DEPLOYMENT_ID&gt; --project-name &lt;PROJECT_NAME&gt;&#10;</code></pre>
<p>Use the <code>--force</code> (or <code>-f</code>) flag to skip the confirmation prompt, and to force deletion of aliased deployments. You can find deployment IDs by running <a href="/workers/wrangler/commands/pages/#pages-deployment-list"><code>wrangler pages deployment list</code></a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11061.md")
</aside>
<h2 id="preview-indexing-by-search-engines">Preview indexing by search engines</h2>
<p>To maintain a healthy SEO profile, it's vital to prevent search engines from finding duplicate content across the web. Because preview deployments are designed to be an exact replica of your production environment, they inherently create this exact situation. Cloudflare Pages by default ensures your search rankings are not harmed by these temporary previews.</p>
<h3 id="x-robots-tag-noindex-on-preview-deployments">X-Robots-Tag: noindex on Preview Deployments</h3>
<p>By default, every preview deployment generated by Cloudflare Pages includes the X-Robots-Tag: noindex HTTP response header. This header acts as a clear directive to search engine crawlers, instructing them to disregard the page and not include it in their search results.</p>
<p>You can easily confirm that your preview deployments are correctly configured to block indexing. Run the following curl command in your terminal, replacing the placeholder with your unique preview URL:</p>
<pre tabindex="0"><code class="language-bash">curl -I https://&lt;your-preview-url&gt;.pages.dev&#10;</code></pre>
<p>Inspect the output for the x-robots-tag: noindex line to verify that your preview site is not being indexed.</p>
