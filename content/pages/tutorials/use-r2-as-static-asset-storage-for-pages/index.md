---
cp9:
  canonical: https://developers.cloudflare.com/pages/tutorials/use-r2-as-static-asset-storage-for-pages/
  description: This tutorial will teach you how to use R2 as a static asset storage bucket for your Pages app.
  full_title: Use R2 as static asset storage with Cloudflare Pages · Cloudflare Pages docs
  head_html: <title>Use R2 as static asset storage with Cloudflare Pages · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial will teach you how to use R2 as a static asset storage bucket for your Pages app."><link rel="canonical" href="https://developers.cloudflare.com/pages/tutorials/use-r2-as-static-asset-storage-for-pages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/tutorials/use-r2-as-static-asset-storage-for-pages/index.md"><meta property="og:title" content="Use R2 as static asset storage with Cloudflare Pages · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial will teach you how to use R2 as a static asset storage bucket for your Pages app."><meta property="og:url" content="https://developers.cloudflare.com/pages/tutorials/use-r2-as-static-asset-storage-for-pages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="R2"><meta name="pcx_tags" content="Hono,JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/tutorials/use-r2-as-static-asset-storage-for-pages/#page","headline":"Use R2 as static asset storage with Cloudflare Pages \u00b7 Cloudflare Pages docs","description":"This tutorial will teach you how to use R2 as a static asset storage bucket for your Pages app.","url":"https://developers.cloudflare.com/pages/tutorials/use-r2-as-static-asset-storage-for-pages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Hono","JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /pages/tutorials/use-r2-as-static-asset-storage-for-pages/
  schema: 1
---
<p>This tutorial will teach you how to use <a href="/r2/">R2</a> as a static asset storage bucket for your <a href="/pages/">Pages</a> app. This is especially helpful if you're hitting the <a href="/pages/platform/limits/#files">file limit</a> or the <a href="/pages/platform/limits/#file-size">max file size limit</a> on Pages.</p>
<p>To illustrate how this is done, we will use R2 as a static asset storage for a fictional cat blog.</p>
<h2 id="the-cat-blog">The Cat blog</h2>
<p>Imagine you run a static cat blog containing funny cat videos and helpful tips for cat owners. Your blog is growing and you need to add more content with cat images and videos.</p>
<p>The blog is hosted on Pages and currently has the following directory structure:</p>
<pre tabindex="0"><code>.&#10;├── public&#10;│   ├── index.html&#10;│   ├── static&#10;│   │   ├── favicon.ico&#10;│   │   └── logo.png&#10;│   └── style.css&#10;└── wrangler.jsonc&#10;</code></pre>
<p>Adding more videos and images to the blog would be great, but our asset size is above the <a href="/pages/platform/limits/#file-size">file limit on Pages</a>. Let us fix this with R2.</p>
<h2 id="create-an-r2-bucket">Create an R2 bucket</h2>
<p>The first step is creating an R2 bucket to store the static assets. A new bucket can be created with the dashboard or via Wrangler.</p>
<p>Using the dashboard, navigate to the R2 tab, then click on <em>Create bucket.</em> We will name the bucket for our blog <em>cat-media</em>. Always remember to give your buckets descriptive names:</p>
<p><img src="/assets/upstream/images/pages/tutorials/pages-r2/dash.png" alt="Dashboard" /></p>
<p>With the bucket created, we can upload media files to R2. I’ll drag and drop two folders with a few cat images and videos into the R2 bucket:</p>
<p><img src="/images/pages/tutorials/pages-r2/upload.gif" alt="Upload" /></p>
<p>Alternatively, an R2 bucket can be created with Wrangler from the command line by running:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket create &lt;bucket_name&gt;&#10;&#35; i.e&#10;&#35; npx wrangler r2 bucket create cat-media&#10;</code></pre>
<p>Files can be uploaded to the bucket with the following command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 object put &lt;bucket_name&gt;/&lt;file_name&gt; -f &lt;path_to_file&gt;&#10;&#35; i.e&#10;&#35; npx wrangler r2 object put cat-media/videos/video1.mp4 -f ~/Downloads/videos/video1.mp4&#10;</code></pre>
<h2 id="bind-r2-to-pages">Bind R2 to Pages</h2>
<p>To bind the R2 bucket we have created to the cat blog, we need to update the Wrangler configuration.</p>
<p>Open the <a href="/pages/functions/wrangler-configuration/">Wrangler configuration file</a>, and add the following binding to the file. <code>bucket_name</code> should be the exact name of the bucket created earlier, while <code>binding</code> can be any custom name referring to the R2 resource:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10858.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10857.md")
</aside>
<p>Save the <a href="/pages/functions/wrangler-configuration/">Wrangler configuration file</a>, and we are ready to move on to the last step.</p>
<p>Alternatively, you can add a binding to your Pages project on the dashboard by navigating to the project’s <em>Settings</em> tab &gt; <em>Functions</em> &gt; <em>R2 bucket bindings</em>.</p>
<h2 id="serve-r2-assets-from-pages">Serve R2 Assets From Pages</h2>
<p>The last step involves serving media assets from R2 on the blog. To do that, we will create a function to handle requests for media files.</p>
<p>In the project folder, create a <em>functions</em> directory. Then, create a <em>media</em> subdirectory and a file named <code>[[all]].js</code> in it. All HTTP requests to <code>/media</code> will be routed to this file.</p>
<p>After creating the folders and JavaScript file, the blog directory structure should look like:</p>
<pre tabindex="0"><code>.&#10;├── functions&#10;│   └── media&#10;│       └── [[all]].js&#10;├── public&#10;│   ├── index.html&#10;│   ├── static&#10;│   │   ├── favicon.ico&#10;│   │   └── icon.png&#10;│   └── style.css&#10;└── wrangler.jsonc&#10;</code></pre>
<p>Finally, we will add a handler function to <code>[[all]].js</code>. This function receives all media requests, and returns the corresponding file asset from R2:</p>
<pre tabindex="0"><code class="language-js">export async function onRequestGet(ctx) {&#10;	const path = new URL(ctx.request.url).pathname.replace(&quot;/media/&quot;, &quot;&quot;);&#10;	const file = await ctx.env.MEDIA.get(path);&#10;	if (!file) return new Response(null, { status: 404 });&#10;	return new Response(file.body, {&#10;		headers: { &quot;Content-Type&quot;: file.httpMetadata.contentType },&#10;	});&#10;}&#10;</code></pre>
<h2 id="deploy-the-blog">Deploy the blog</h2>
<p>Before deploying the changes made so far to our cat blog, let us add a few new posts to <code>index.html</code>. These posts depend on media assets served from R2:</p>
<pre tabindex="0"><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;	&lt;body&gt;&#10;		&lt;h1&gt;Awesome Cat Blog! 😺&lt;/h1&gt;&#10;		&lt;p&gt;Today&#x27;s post:&lt;/p&gt;&#10;		&lt;video width=&quot;320&quot; controls&gt;&#10;			&lt;source src=&quot;/media/videos/video1.mp4&quot; type=&quot;video/mp4&quot; /&gt;&#10;		&lt;/video&gt;&#10;		&lt;p&gt;Yesterday&#x27;s post:&lt;/p&gt;&#10;		&lt;img src=&quot;/media/images/cat1.jpg&quot; width=&quot;320&quot; /&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>With all the files saved, open a new terminal window to deploy the app:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Once deployed, media assets are fetched and served from the R2 bucket.</p>
<p><img src="/images/pages/tutorials/pages-r2/deployed.gif" alt="Deployed App" /></p>
<h2 id="related-resources"><strong>Related resources</strong></h2>
<ul>
<li><a href="/pages/functions/routing/">Learn how function routing works in Pages.</a></li>
<li><a href="/r2/buckets/public-buckets/">Learn how to create public R2 buckets</a>.</li>
<li><a href="/r2/api/workers/workers-api-usage/">Learn how to use R2 from Workers</a>.</li>
</ul>
