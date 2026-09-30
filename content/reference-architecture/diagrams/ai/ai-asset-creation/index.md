---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-asset-creation/
  description: AI systems combine text-generation and text-to-image models to create visual content from text. They generate prompts, moderate content, and produce images for various applications.
  full_title: Content-based asset creation · Cloudflare Reference Architecture docs
  head_html: <title>Content-based asset creation · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="AI systems combine text-generation and text-to-image models to create visual content from text. They generate prompts, moderate content, and produce images for various applications."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-asset-creation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-asset-creation/index.md"><meta property="og:title" content="Content-based asset creation · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="AI systems combine text-generation and text-to-image models to create visual content from text. They generate prompts, moderate content, and produce images for various applications."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-asset-creation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="Workers AI"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-asset-creation/#page","headline":"Content-based asset creation \u00b7 Cloudflare Reference Architecture docs","description":"AI systems combine text-generation and text-to-image models to create visual content from text. They generate prompts, moderate content, and produce images for various applications.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-asset-creation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/ai/ai-asset-creation/
  schema: 1
---
<p>Combining text-generation models with text-to-image models can lead to powerful AI systems capable of generating visual content based on input prompts. This integration can be achieved through a collaborative framework where a text-generation model generates prompts for the text-to-image model based on input text.</p>
<p>Here's how the process can work:</p>
<ul>
<li>
<p>Input Text Processing: The input text is provided to the system, which can be anything from a simple sentence to multiple paragraphs. This text serves as the basis for generating visual content.</p>
</li>
<li>
<p>Prompt Generation: The text-generation model generates prompts based on the input text. These prompts are specifically crafted to guide the text-to-image model in generating images that are contextually relevant to the input text. The prompts can include descriptions, keywords, or other cues to guide the image generation process.</p>
</li>
<li>
<p>Content Moderation: Text-classification models can be employed to ensure that the generated assets comply with content policies</p>
</li>
<li>
<p>Text-to-Image Model: A text-to-image model takes the prompts generated by the text-generation model as input and produces corresponding images. The text-to-image model learns to translate textual descriptions into visual representations, aiming to capture the essence and context conveyed by the input text.</p>
</li>
</ul>
<p>Example uses of such compositions of AI models can be employed to generation visual assets for marketing, publishing, presentations, and more.</p>
<h2 id="asset-generation">Asset generation</h2>
<p><img src="/assets/upstream/images/reference-architecture/ai-asset-generation-diagrams/ai-asset-generation.svg" alt="Figure 1:Content-based asset generation" title="Figure 1: Content-based asset generation" /></p>
<ol>
<li><strong>Client upload</strong>: Send POST request with content to API endpoint.</li>
<li><strong>Prompt generation</strong>: Generate prompt for later-stage text-to-image model by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text generation models</a> with content as input.</li>
<li><strong>Safety check</strong>: Check for compliance with safety guidelines by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text classification models</a> with the previously generated prompt as input.</li>
<li><strong>Image generation</strong>: Generate image by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">text-to-image models</a> previously generated prompt.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://auto-asset.pages.dev/">Community project: content-based asset creation demo</a></li>
<li><a href="/workers-ai/models/">Workers AI: Text generation models</a></li>
<li><a href="/workers-ai/models/">Workers AI: Text-to-image models</a></li>
<li><a href="/workers-ai/models/llamaguard-7b-awq/">Workers AI: llamaguard-7b-awq</a></li>
</ul>
