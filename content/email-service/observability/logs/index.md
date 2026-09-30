---
cp9:
  canonical: https://developers.cloudflare.com/email-service/observability/logs/
  description: View and analyze Email Service sending and routing activity logs with authentication and delivery details.
  full_title: Email logs · Cloudflare Email Service docs
  head_html: <title>Email logs · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="View and analyze Email Service sending and routing activity logs with authentication and delivery details."><link rel="canonical" href="https://developers.cloudflare.com/email-service/observability/logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/observability/logs/index.md"><meta property="og:title" content="Email logs · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View and analyze Email Service sending and routing activity logs with authentication and delivery details."><meta property="og:url" content="https://developers.cloudflare.com/email-service/observability/logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/observability/logs/#page","headline":"Email logs \u00b7 Cloudflare Email Service docs","description":"View and analyze Email Service sending and routing activity logs with authentication and delivery details.","url":"https://developers.cloudflare.com/email-service/observability/logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/observability/logs/
  schema: 1
---
<p class="article-summary">View and analyze email sending and routing activity logs with detailed authentication and delivery information</p>
<p>Email Service provides comprehensive logging for both email sending and routing activities. Access detailed logs through the Cloudflare dashboard to monitor email flow, troubleshoot delivery issues, and analyze authentication status.</p>
<h2 id="activity-log">Activity log</h2>
<p>The Activity log allows you to sort through all email activities and check actions taken by Email Service. In the dashboard you can filter the Activity log to a time range between 30 minutes and 30 days, or specify a custom range.</p>
<p>The Activity log surfaces the same per-event data that is also available programmatically through the <a href="/email-service/observability/metrics-analytics/"><code>emailSendingAdaptive</code> and <code>emailRoutingAdaptive</code> datasets</a> in the GraphQL Analytics API.</p>
<p>For Email Routing, you can expand an individual email in the Activity log to inspect authentication results (<a href="https://datatracker.ietf.org/doc/html/rfc7208">SPF</a>, <a href="https://datatracker.ietf.org/doc/html/rfc6376">DKIM</a>, and <a href="https://datatracker.ietf.org/doc/html/rfc7489">DMARC</a>).</p>
<h3 id="email-sending-logs">Email sending logs</h3>
<p>For outbound emails sent through Email Service:</p>
<ul>
<li><strong>Sent</strong>: Email successfully accepted and queued for delivery.</li>
<li><strong>Delivered</strong>: Email successfully delivered to recipient's mail server.</li>
<li><strong>Delivery failed</strong>: Email bounced (hard or soft bounce). This corresponds to the <code>deliveryFailed</code> status in the <a href="/email-service/observability/metrics-analytics/">GraphQL Analytics API</a>.</li>
<li><strong>Rejected</strong>: Email was not sent because the recipient is on your account's <a href="/email-service/concepts/suppressions/">suppression list</a>.</li>
<li><strong>Failed</strong>: Email failed to send due to configuration or authentication issues.</li>
</ul>
<h3 id="email-routing-logs">Email routing logs</h3>
<p>For inbound emails processed through Email Routing:</p>
<ul>
<li><strong>Forwarded</strong>: Email successfully forwarded to destination address.</li>
<li><strong>Handled</strong>: Email processed by a Worker handler.</li>
<li><strong>Dropped</strong>: Email dropped due to filtering rules or configuration.</li>
<li><strong>Rejected</strong>: Email rejected due to SPF, DKIM, or DMARC failures.</li>
<li><strong>Delivery failed</strong>: Email could not be delivered to the destination address.</li>
<li><strong>Error</strong>: Email could not be processed due to an internal error.</li>
</ul>
<h2 id="viewing-email-details">Viewing email details</h2>
<p>Select any email in the Activity log to expand its details and view authentication and delivery information.</p>
<h3 id="authentication-status">Authentication status</h3>
<p>Check the status of email authentication protocols:</p>
<ul>
<li><strong>SPF status</strong>: Shows pass/fail for Sender Policy Framework validation.</li>
<li><strong>DKIM status</strong>: Shows pass/fail for DomainKeys Identified Mail signature verification.</li>
<li><strong>DMARC status</strong>: Shows pass/fail for Domain-based Message Authentication compliance.</li>
</ul>
<h3 id="delivery-information">Delivery information</h3>
<p>For sent emails, see delivery details:</p>
<ul>
<li>Recipient mail server response.</li>
<li>Delivery attempts and timestamps.</li>
<li>Bounce reason codes and categories.</li>
<li>Final delivery status.</li>
</ul>
<h3 id="message-preview">Message preview</h3>
<p>For sent emails, expand the email in the Activity log to open the <strong>Preview</strong> section and inspect the message as it was sent. The preview provides the following tabs:</p>
<ul>
<li><strong>HTML</strong>: The rendered HTML body.</li>
<li><strong>Text</strong>: The plain text body.</li>
<li><strong>Headers</strong>: The message headers.</li>
<li><strong>Attachments</strong>: Files included with the message.</li>
<li><strong>Raw</strong>: The full raw <a href="https://datatracker.ietf.org/doc/html/rfc5322">RFC 5322</a> message source.</li>
</ul>
<p>To make sent messages previewable, turn on <a href="/email-service/configuration/domains/#email-preview"><strong>Email preview</strong></a> for the sending domain. Previews cover messages sent while the setting is turned on and are retained for about seven days. New sending domains have <strong>Email preview</strong> turned on automatically.</p>
<h2 id="best-practices-for-log-monitoring">Best practices for log monitoring</h2>
<h3 id="regular-review">Regular review</h3>
<ul>
<li>Monitor logs daily during initial setup</li>
<li>Check weekly for ongoing operations</li>
<li>Review immediately after configuration changes</li>
</ul>
<h3 id="key-metrics-to-watch">Key metrics to watch</h3>
<ul>
<li>Authentication failure rates</li>
<li>Bounce patterns and trends</li>
<li>Delivery success rates</li>
</ul>
<h3 id="troubleshooting-workflow">Troubleshooting workflow</h3>
<ol>
<li>Identify the issue: Use logs to pinpoint failure types</li>
<li>Check authentication: Verify SPF, DKIM, DMARC configuration</li>
<li>Adjust configuration: Make necessary DNS or routing changes</li>
<li>Monitor improvement: Track metrics after changes</li>
</ol>
<hr />
<p>Email logs provide the visibility needed to maintain high deliverability and properly route incoming emails. Use this data to optimize your email configuration and quickly resolve any delivery issues.</p>
