---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/
  description: Use Cloudflare Workers or an external service to monitor for notifications about data changes and then handle them appropriately.
  full_title: Event notifications for storage · Cloudflare Reference Architecture docs
  head_html: <title>Event notifications for storage · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare Workers or an external service to monitor for notifications about data changes and then handle them appropriately."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/index.md"><meta property="og:title" content="Event notifications for storage · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare Workers or an external service to monitor for notifications about data changes and then handle them appropriately."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="R2,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/#page","headline":"Event notifications for storage \u00b7 Cloudflare Reference Architecture docs","description":"Use Cloudflare Workers or an external service to monitor for notifications about data changes and then handle them appropriately.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/storage/event-notifications-for-storage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/storage/event-notifications-for-storage/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Cloudflare <a href="/r2/">R2</a> Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services. The lifecycle of data in object storage often extends beyond uploading, modifying, or deleting the data. There may be a requirement to transform, analyze, or perform post-processing on the data. R2 provides <a href="/r2/buckets/event-notifications/">event notifications</a> to manage these event-driven workflows.</p>
<p>This document walks through how to use our built in serverless <a href="/workers/">Cloudflare Workers</a> or an external service to monitor for notifications about data changes and then handle them appropriately.</p>
<h2 id="push-based-consumer-worker">Push-based consumer Worker</h2>
<p>Event notifications function by sending messages to a <a href="/queues/">queue</a> whenever there is a change to your data. These messages are then handled by a <a href="/queues/reference/how-queues-works/#consumers">consumer Worker</a>. A consumer Worker is the term for a client that is subscribing to or consuming messages from a queue. The consumer Worker will automatically receive these messages, allowing you to define any subsequent actions that need to be taken.</p>
<p>For instance, you can configure a notification to trigger when new images are uploaded to your R2 bucket. This notification can then automatically start an AI workload that performs an action on the image, such as converting the image to text.</p>
<p>Consider the example below of push-based post-processing: when a user uploads a new object into R2, we want to log and store that event into a separate R2 bucket. You can create this scenario yourself by following this tutorial: <a href="/r2/tutorials/upload-logs-event-notifications/">Log and store upload events in R2 with event notifications</a>.</p>
<p><img src="/assets/upstream/images/reference-architecture/event-notifications-for-storage/pushed-based-event-notification.svg" alt="Figure 1: Push-Based R2 Event Notifications" title="Figure 1: Push-Based R2 Event Notifications" /></p>
<ol>
<li>A user uploads a new object directly to R2.</li>
<li>An event notification is sent to the queue.</li>
<li>The consumer Worker is pushed the new work from the queue.</li>
<li>The Worker inserts a log event into R2.</li>
</ol>
<h2 id="pull-based-http-consumer">Pull-based HTTP consumer</h2>
<p>Alternatively, you can establish a <a href="/queues/configuration/pull-consumers/">pull-based consumer</a>, where you pull from a queue over HTTP from any environment. Use a pull-based consumer if you need to consume messages from existing infrastructure outside of Cloudflare where you need to carefully control how fast messages are consumed.</p>
<p>A pull-based consumer must explicitly make a call to pull (and then acknowledge) messages from the queue, only when it is ready to do so.</p>
<p>Consider the scenario below: A user initiates a delete from R2. An external service needs to be informed of the deletion, so a pull-based queue has been established for the external service to retrieve notifications.</p>
<p><img src="/assets/upstream/images/reference-architecture/event-notifications-for-storage/pull-based-event-notification.svg" alt="Figure 2: Pull-Based R2 Event Notifications" title="Figure 2: Pull-Based R2 Event Notifications" /></p>
<ol>
<li>A user initiates a delete from R2.</li>
<li>An event notification is sent to the queue.</li>
<li>The external service, when ready to process the request, makes an HTTP POST request to the queue to pull the message.</li>
<li>The queue sends the message in response to the POST request from step 3.</li>
<li>The external service must acknowledge that the message has been received.</li>
</ol>
<p>You can follow the steps here to <a href="/queues/configuration/pull-consumers/#1-enable-http-pull">configure a pull-based consumer</a>.</p>
<h2 id="additional-example-use-cases">Additional example use cases</h2>
<ul>
<li>Send an email to an administrator any time objects are deleted from R2.</li>
<li>When a video or podcast is uploaded to R2, it automatically processes the content using one of Cloudflare's Automatic Speech Recognition (ASR) AI models to generate subtitles or even translate the content.</li>
<li>Remove related database entries if an object in R2 is deleted.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/r2/tutorials/upload-logs-event-notifications/">Tutorial: Log and store upload events in R2 with event notifications</a></li>
<li><a href="/r2/buckets/event-notifications/">Event Notifications documentation</a></li>
<li><a href="/r2/">Cloudflare R2 overview</a></li>
<li><a href="/queues/">Cloudflare Queues overview</a></li>
<li><a href="/queues/configuration/pull-consumers/">Cloudflare Queues Pull Consumers</a></li>
</ul>
