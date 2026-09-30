---
cp9:
  canonical: https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/
  description: Set up bindings to connect Images, R2, and Assets to your Worker
  full_title: Transform user-uploaded images before uploading to R2 · Cloudflare Images docs
  head_html: <title>Transform user-uploaded images before uploading to R2 · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up bindings to connect Images, R2, and Assets to your Worker"><link rel="canonical" href="https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/index.md"><meta property="og:title" content="Transform user-uploaded images before uploading to R2 · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up bindings to connect Images, R2, and Assets to your Worker"><meta property="og:url" content="https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/#page","headline":"Transform user-uploaded images before uploading to R2 \u00b7 Cloudflare Images docs","description":"Set up bindings to connect Images, R2, and Assets to your Worker","url":"https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/tutorials/optimize-user-uploaded-image/
  schema: 1
---
<p>In this guide, you will build an app that accepts image uploads, overlays the image with a visual watermark, then stores the transformed image in your R2 bucket.</p>
<hr />
<p>With Images, you have the flexibility to choose where your original images are stored. You can transform images that are stored outside of the Images product, like in <a href="/r2/">R2</a>.</p>
<p>When you store user-uploaded media in R2, you may want to optimize or manipulate images before they are uploaded to your R2 bucket.</p>
<p>You will learn how to connect Developer Platform services to your Worker through bindings, as well as use various optimization features in the Images API.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, you will need to do the following:</p>
<ul>
<li>Add an <a href="/images/pricing/#images-paid">Images Paid</a> subscription to your account. This allows you to bind the Images API to your Worker.</li>
<li>Create an <a href="/r2/get-started/">R2 bucket</a>, where the transformed images will be uploaded.</li>
<li>Create a new Worker project.</li>
</ul>
<p>If you are new, review how to <a href="/workers/get-started/guide/">create your first Worker</a>.</p>
<h2 id="1-set-up-your-worker-project">1: Set up your Worker project</h2>
<p>To start, you will need to set up your project to use the following resources on the Developer Platform:</p>
<ul>
<li><a href="/images/optimization/binding/">Images</a> to transform, resize, and encode images directly from your Worker.</li>
<li><a href="/r2/api/workers/workers-api-usage/">R2</a> to connect the bucket for storing transformed images.</li>
<li><a href="/workers/static-assets/binding/">Assets</a> to access a static image that will be used as the visual watermark.</li>
</ul>
<h3 id="add-the-bindings-to-your-wrangler-configuration">Add the bindings to your Wrangler configuration</h3>
<p>Configure your Wrangler configuration file to add the Images, R2, and Assets bindings:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9335.md")
</div>
Replace `<BUCKET>` with the name of the R2 bucket where you will upload the images after they are transformed. In your Worker code, you will be able to refer to this bucket using `env.R2.`
<p>Replace <code>./&lt;DIRECTORY&gt;</code> with the name of the project's directory where the overlay image will be stored. In your Worker code, you will be able to refer to these assets using <code>env.ASSETS</code>.</p>
<h3 id="set-up-your-assets-directory">Set up your assets directory</h3>
<p>Because we want to apply a visual watermark to every uploaded image, you need a place to store the overlay image.</p>
<p>The assets directory of your project lets you upload static assets as part of your Worker. When you deploy your project, these uploaded files, along with your Worker code, are deployed to Cloudflare's infrastructure in a single operation.</p>
<p>After you configure your Wrangler file, upload the overlay image to the specified directory. In our example app, the directory <code>./assets</code> contains the overlay image.</p>
<h2 id="2-build-your-frontend">2: Build your frontend</h2>
<p>You will need to build the interface for the app that lets users upload images.</p>
<p>In this example, the frontend is rendered directly from the Worker script.</p>
<p>To do this, make a new <code>html</code> variable, which contains a <code>form</code> element for accepting uploads. In <code>fetch</code>, construct a new <code>Response</code> with a <code>Content-Type: text/html</code> header to serve your static HTML site to the client:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9336.md")
</div>
<h2 id="3-read-the-uploaded-image">3: Read the uploaded image</h2>
<p>After you have a <code>form</code>, you need to make sure you can transform the uploaded images.</p>
<p>Because the <code>form</code> lets users upload directly from their disk, you cannot use <code>fetch()</code> to get an image from a URL. Instead, you will operate on the body of the image as a stream of bytes.</p>
<p>To do this, parse the uploaded file from the <code>form</code> and get its stream:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9337.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="prevent-potential-errors-when-accessing-request-body">Prevent potential errors when accessing request.body</h3>
@markup("md", "content/.markup/bodies/9334.md")
</aside>
<h2 id="4-transform-the-image">4: Transform the image</h2>
<p>For every uploaded image, you want to perform the following actions:</p>
<ul>
<li>Overlay the visual watermark that we added to our assets directory.</li>
<li>Transcode the image — with its watermark — to <code>AVIF</code>. This compresses the image and reduces its file size.</li>
<li>Upload the transformed image to R2.</li>
</ul>
<h3 id="set-up-the-overlay-image">Set up the overlay image</h3>
<p>To fetch the overlay image from the assets directory, create a function <code>assetUrl</code> then use <code>env.ASSETS</code> to retrieve the <code>watermark.png</code> image:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9338.md")
</div>
<h3 id="watermark-and-transcode-the-image">Watermark and transcode the image</h3>
<p>You can interact with the Images binding through <code>env.IMAGES</code>.</p>
<p>This is where you will put all of the optimization operations you want to perform on the image. Here, you will use the <code>.draw()</code> function to apply a visual watermark over the uploaded image, then use <code>.output()</code> to encode the image as AVIF:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9339.md")
</div>
<h2 id="5-upload-to-r2">5: Upload to R2</h2>
<p>Upload the transformed image to R2.</p>
<p>By creating a <code>fileName</code> variable, you can specify the name of the transformed image. In this example, you append the date to the name of the original image before uploading to R2.</p>
<p>Here is the full code for the example:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9340.md")
</div>
<h2 id="next-steps">Next steps</h2>
<p>In this tutorial, you learned how to connect your Worker to various resources on the Developer Platform to build an app that accepts image uploads, transform images, and uploads the output to R2.</p>
<p>Next, you can <a href="/images/optimization/features/#url-interface">set up a transformation URL</a> to dynamically optimize images that are stored in R2.</p>
