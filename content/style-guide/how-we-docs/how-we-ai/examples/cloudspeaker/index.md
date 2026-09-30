---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/examples/cloudspeaker/
  description: Use Cloudspeaker for documentation announcements.
  full_title: Cloudspeaker · Cloudflare Style Guide
  head_html: <title>Cloudspeaker · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudspeaker for documentation announcements."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/examples/cloudspeaker/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/examples/cloudspeaker/index.md"><meta property="og:title" content="Cloudspeaker · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudspeaker for documentation announcements."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/examples/cloudspeaker/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/examples/cloudspeaker/#page","headline":"Cloudspeaker \u00b7 Cloudflare Style Guide","description":"Use Cloudspeaker for documentation announcements.","url":"https://developers.cloudflare.com/style-guide/how-we-docs/how-we-ai/examples/cloudspeaker/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/how-we-docs/how-we-ai/examples/cloudspeaker/
  schema: 1
---
<p>One of the greatest challenges at any scale is understanding what your customers are <em>really</em> saying. At Cloudflare, we collect massive amounts of customer feedback every day. This feedback is a goldmine of insight, but it is scattered across dozens of disparate, public-facing channels: our own Cloudflare community forum, Reddit, X (formerly Twitter), GitHub, Discord, HackerNews, and more.</p>
<p>Individually, these posts are anecdotes. Collectively, they are a strategic asset. The problem is that the sheer size of these datasets makes it impossible to manually process them for product, content, and design insights. This mass of unorganized feedback was an underutilized opportunity to see cross-functional trends.</p>
<p>To solve this, we built CloudSpeaker, an internal tool created to amplify the voice of the user. Its purpose is to save time, increase efficiency, and consolidate public feedback from all these external communities into a single, unified view.</p>
<h2 id="the-goal-turning-unstructured-noise-into-actionable-insight">The goal: Turning unstructured noise into actionable insight</h2>
<p>CloudSpeaker was designed to give any stakeholder at Cloudflare — from product managers and engineers to our user experience teams — a quick way to &quot;check the pulse&quot; of the products and features they own.</p>
<p>The tool allows anyone to see:</p>
<ul>
<li>A combined view of product feedback from many channels.</li>
<li>Recurring issues and customer pain points.</li>
<li>General sentiment for a product over time.</li>
</ul>
<p>This consolidated view is now a key part of our planning cycles, informing everything from user research and persona creation to feature requests and quarterly backlog prioritization.</p>
<h2 id="how-it-is-built-an-ai-powered-data-pipeline">How it is built: An AI-powered data pipeline</h2>
<p>CloudSpeaker is built entirely on our own products. The real power, however, comes from its AI-driven data pipeline, managed by our Data Intelligence team.</p>
<p>Here is how it works:</p>
<ol>
<li><strong>Ingestion:</strong> On a daily basis, our pipelines ingest new community content from our various public sources.</li>
<li><strong>AI classification:</strong> This new, unstructured content is fed into our AI Content Pipeline. We use Large Language Models (LLMs) via <a href="/workers-ai/">Workers AI</a> to automatically classify every single post. Each post is tagged with three key pieces of information:
<ul>
<li><strong>Product(s) mentioned:</strong> It identifies which of the 60+ Cloudflare products are being discussed.</li>
<li><strong>Sentiment:</strong> The model analyzes the text to determine the user's sentiment, classifying it on a spectrum from <code>negative</code> to <code>neutral</code> to <code>positive</code>.</li>
<li><strong>Post type:</strong> It categorizes the intent of the post, such as a <code>help request</code>, <code>feature request</code>, or <code>bug report</code>.</li>
</ul>
</li>
<li><strong>Storage and display:</strong> Once the AI completes its inference, these new classifications are stored in our D1 database and become viewable in the CloudSpeaker UI.</li>
</ol>
<h2 id="the-workflow-on-demand-ai-analysis">The workflow: On-demand AI analysis</h2>
<p>The backend classification pipeline solves the problem of manual processing. The frontend application solves the problem of accessibility.</p>
<p>In the CloudSpeaker dashboard, a product manager can filter the entire dataset — spanning up to six months — by any combination of product, sentiment, post type, or date range. If they want to see all <code>negative</code> sentiment posts about a specific product that were <code>feature requests</code> in the last quarter, they can do so in seconds.</p>
<p>Furthermore, we added a second layer of AI directly into the UI. After filtering down to a set of comments, the user can select a <strong>Summarize</strong> button. This uses Workers AI to generate an on-the-fly summary of the currently displayed comments, providing an instant, qualitative overview of quantitative data.</p>
<p>CloudSpeaker is a powerful example of using AI not to generate content, but to analyze and structure the vast amounts of content our users generate every day. It transforms what was once an impossible manual task into a critical source of automated, actionable insights.</p>
