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
