---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/storage/storing-user-generated-content/
  description: Store user-generated content in R2 for fast, secure, and cost-effective architecture.
  full_title: Storing user generated content · Cloudflare Reference Architecture docs
  head_html: <title>Storing user generated content · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="Store user-generated content in R2 for fast, secure, and cost-effective architecture."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/storage/storing-user-generated-content/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/storage/storing-user-generated-content/index.md"><meta property="og:title" content="Storing user generated content · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store user-generated content in R2 for fast, secure, and cost-effective architecture."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/storage/storing-user-generated-content/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="R2,Workers,Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/storage/storing-user-generated-content/#page","headline":"Storing user generated content \u00b7 Cloudflare Reference Architecture docs","description":"Store user-generated content in R2 for fast, secure, and cost-effective architecture.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/storage/storing-user-generated-content/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/storage/storing-user-generated-content/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>User generated content (UGC) is an essential aspect of modern applications. This includes users uploading profile photos, documents, and videos, as well as AI models generating images, summaries, or structured data. Therefore, applications require a reliable, scalable, and cost-effective solution for storing and accessing this content.</p>
<p>Cloudflare <a href="/r2/">R2</a> is an S3-compatible object storage with zero egress fees, making it ideal for handling content uploads and delivery at scale. Combined with Cloudflare <a href="/workers/">Workers</a> and Cloudflare's global network, it enables fast, secure, and cost-effective workflows for ingesting and managing UGC.</p>
<p>This reference architecture explores two common UGC workflows, both optimized for performance, security, and cost efficiency:</p>
<ol>
<li><strong>Secure User Uploads to R2 via Signed URLs:</strong> Allowing users to upload files (profile images, documents, etc.) efficiently and securely without overloading backend systems.</li>
<li><strong>AI-Generated Content Stored in R2:</strong> Storing content generated by Workers AI or external AI services, ensuring inference results are persistently available for future use.</li>
</ol>
<h2 id="use-cases">Use Cases</h2>
<h3 id="use-case-1-secure-user-uploads-to-r2-via-signed-urls">Use Case 1: Secure User Uploads to R2 via Signed URLs</h3>
<p>User generated content typically starts with file uploads, including profile pictures, resumes, rich media, and documents. Applications must securely validate and store these uploads while avoiding latency, high costs, and unnecessary complexity in the backend.</p>
<p>In this architecture, we use <strong>R2</strong> as the primary storage layer and a <strong>Worker</strong> to control upload access. Files are uploaded directly from the user's browser or device to R2 using signed URLs, which are generated by the Worker after validating the user's permissions and upload intent.</p>
<p>This approach avoids routing large files through the application backend or Worker, reducing latency and operational cost—while ensuring tight control over access and security.</p>
<p>And because R2 is natively integrated with Cloudflare's global network, files stored in R2 are accessible with low latency from anywhere in the world—and <strong>without any egress fees</strong>, even as your application scales.</p>
<p><img src="/assets/upstream/images/reference-architecture/storing-user-generated-content/uploads-to-r2-via-signed-urls.svg" alt="Use Case 1: Secure User Uploads to R2 via Signed URLs" title="Use Case 1: Secure User Uploads to R2 via Signed URLs" /></p>
<p><strong>How it Works</strong></p>
<ol>
<li><strong>User initiates upload from the frontend:</strong> The app collects file details (e.g. size, name) and calls a backend API (a Cloudflare Worker) to begin the upload process.</li>
<li><strong>Worker authenticates the user and validates the request:</strong> The Worker confirms that the user is logged in, has upload permissions, and that the file is within acceptable limits (for example, 10MB max, allowed MIME types).</li>
<li><strong>Worker returns a signed PUT URL to R2:</strong> A signed URL allows the frontend to upload directly to R2 for a limited time, under a specific key or namespace. There is no need for the Worker to handle large files directly.</li>
<li><strong>Frontend uploads the file directly to R2:</strong> The file is streamed directly from the client to R2.</li>
<li><strong>(Optional) Trigger post-upload workflows:</strong> R2 offers <a href="/r2/buckets/event-notifications/">event notifications</a> to send messages to a queue when data in your R2 bucket changes, like a new upload. Example post-processing:
<ul>
<li>Scan, moderate, or transform the file.</li>
<li>Write metadata (for example, <code>user_id</code>, <code>file_path</code>, <code>timestamp</code>) to <a href="/d1/">D1</a>, Cloudflare's serverless SQL database.</li>
<li>Notify the user or update a dashboard/UI.</li>
</ul>
</li>
</ol>
<p>For more information on uploading data directly from the client to R2, refer to the documentation on <a href="/r2/api/s3/presigned-urls/">presigned URLs</a>.</p>
<h3 id="use-case-2-ai-generated-content-stored-in-r2">Use Case 2: AI-Generated Content Stored in R2</h3>
<p>Many modern applications utilize AI-generated content, which can include product descriptions, profile pictures, audio clips, and more. When this content is created in response to user actions or scheduled events, it must be stored immediately, reliably, and at scale.</p>
<p>This architecture employs <a href="/workers-ai/">Workers AI</a> to perform inference at the edge and then stores the generated output directly in Cloudflare R2, all within a single Worker.</p>
<p><img src="/assets/upstream/images/reference-architecture/storing-user-generated-content/ai-generated-content-in-r2.svg" alt="Use Case 2: AI-Generated Content Stored in R2" title="Use Case 2: AI-Generated Content Stored in R2" /></p>
<p><strong>How it Works</strong></p>
<ol>
<li><strong>User initiates content generation:</strong> The frontend sends a request to a Cloudflare Worker to create content using an AI model (for example, &quot;Create a thumbnail image for this product&quot;).</li>
<li><strong>Worker invokes Workers AI:</strong> The Worker passes the user input to a model deployed on Workers AI.</li>
<li><strong>Generated output is returned to the Worker:</strong> The response could be plain text, a Base64 image, a binary buffer, or other structured data—depending on the model type.</li>
<li><strong>Worker uploads the output to R2 directly:</strong> No signed URL or client upload is needed. The Worker performs a secure, authenticated <code>PUT</code> request to store the output in a designated bucket.</li>
<li><strong>Worker returns success and metadata to the frontend:</strong> The client receives a reference to the stored file (such as a path, object key, or signed download URL if needed).</li>
</ol>
<p>Refer to <a href="/r2/api/workers/workers-api-usage/">Use R2 from Workers</a> for more information on accessing R2 buckets via Cloudflare Workers.</p>
<h2 id="summary">Summary</h2>
<p>By storing <strong>user-generated content in Cloudflare R2</strong>, applications gain:</p>
<ul>
<li>A highly scalable storage backend</li>
<li>Fast access through Cloudflare's edge computing</li>
<li>Predictable costs with zero egress fees</li>
<li>Seamless AI + UGC workflows that maximize efficiency</li>
</ul>
<p>This architecture ensures that content is stored, processed, and delivered <strong>fast, securely, and cost-effectively</strong>.</p>
<h2 id="related-links">Related Links</h2>
<ul>
<li><a href="/r2/">Cloudflare R2 Product Page</a></li>
<li><a href="/r2/api/s3/presigned-urls/">R2 Presigned URLs</a></li>
<li><a href="/r2/api/workers/workers-api-usage/">Use R2 from Workers</a></li>
<li><a href="/r2/data-migration/">Migrating Data to R2</a></li>
<li><a href="/reference-architecture/diagrams/storage/event-notifications-for-storage/">Event notifications for storage reference architecture</a></li>
<li><a href="https://www.cloudflare.com/pg-cloudflare-r2-vs-aws-s3/">Why choose Cloudflare R2 vs Amazon S3</a></li>
</ul>
