---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-integrations/graylog/
  description: This tutorial explains how to analyze Cloudflare Logs using Graylog. The Graylog integration is available on GitHub.
  full_title: Graylog · Cloudflare Analytics docs
  head_html: <title>Graylog · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to analyze Cloudflare Logs using Graylog. The Graylog integration is available on GitHub."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-integrations/graylog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-integrations/graylog/index.md"><meta property="og:title" content="Graylog · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to analyze Cloudflare Logs using Graylog. The Graylog integration is available on GitHub."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-integrations/graylog/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Analytics,Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-integrations/graylog/#page","headline":"Graylog \u00b7 Cloudflare Analytics docs","description":"This tutorial explains how to analyze Cloudflare Logs using Graylog. The Graylog integration is available on GitHub.","url":"https://developers.cloudflare.com/analytics/analytics-integrations/graylog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-integrations/graylog/
  schema: 1
---
<p>This tutorial explains how to analyze <a href="https://www.cloudflare.com/products/cloudflare-logs/">Cloudflare Logs</a> using <a href="https://github.com/Graylog2/graylog-s3-lambda/blob/master/content-packs/cloudflare/cloudflare-logpush-content-pack.json">Graylog</a>.</p>
<h2 id="overview">Overview</h2>
<p>If you haven't used Cloudflare Logs before, visit our <a href="/logs/">Logs documentation</a> for
more details. Contact your Cloudflare Customer Account Team to enable logs for
your account.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before sending your Cloudflare log data to Graylog, make sure that you:</p>
<ul>
<li>Have an existing Graylog installation. Both single-node and cluster configurations are supported</li>
<li>Have a Cloudflare Enterprise account with Cloudflare Logs enabled</li>
<li>Configure <a href="/logs/logpush/">Logpush</a></li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3134.md")
</aside>
<h2 id="task-1-preparation">Task 1 - Preparation</h2>
<p>Before getting Cloudflare logs into Graylog:</p>
<ol>
<li>Configure Cloudflare <a href="/logs/logpush/">Logpush</a> to push logs with all desired fields to an AWS S3 bucket of your choice.</li>
<li>Download the latest <a href="https://github.com/Graylog2/graylog-s3-lambda/blob/master/content-packs/cloudflare/cloudflare-logpush-content-pack.json">Graylog Integration for Cloudflare</a>.</li>
<li>Decompress the zip file.</li>
</ol>
<p>Once decompressed, the integration package includes:</p>
<ul>
<li><em>graylog-s3-lambda.jar</em></li>
<li><em>content-packs/cloudflare/cloudflare-logpush-content-pack.json</em></li>
<li><em>content-packs/cloudflare/threat-lookup.csv</em></li>
</ul>
<h2 id="task-2-create-and-configure-the-aws-lambda-function">Task 2 - Create and configure the AWS Lambda Function</h2>
<ol>
<li>Navigate to the Lambda service page in the AWS web console.</li>
<li>Create a new Lambda function and specify a <em>function name</em> of your choice and the <em>Java-8 runtime</em>.</li>
<li>Create or specify an execution role with the following permissions. You can also further restrict the resource permissions as desired for your specific set-up.</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;Version&quot;: &quot;2012-10-17&quot;,&#10;  &quot;Statement&quot;: [&#10;    {&#10;      &quot;Sid&quot;: &quot;Policy&quot;,&#10;      &quot;Effect&quot;: &quot;Allow&quot;,&#10;      &quot;Action&quot;: [&#10;        &quot;logs:CreateLogGroup&quot;&#10;        &quot;s3:GetObject&quot;,&#10;        &quot;logs:CreateLogStream&quot;,&#10;        &quot;logs:PutLogEvents&quot;&#10;      ],&#10;      &quot;Resource&quot;: [&#10;        &quot;arn:aws:logs:your-region:your-account-number:*&quot;,&#10;        &quot;arn:aws:s3:your-region::cloudflare-bucket-name/*&quot;&#10;      ]&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p><strong>Note:</strong> If your Graylog cluster is running in a VPC, you may need to add the <em>AWSLambdaVPCAccessExecutionRole</em> managed role to allow the Lambda function to route traffic to the VPC.</p>
<ol start="4">
<li>
<p>Once you've created the Lambda function, upload the function code <em><strong>graylog-s3-lambda.jar</strong></em> downloaded in <a href="#task-1---preparation">Task 1</a>.  Specify the following method for the Handler: <em>org.graylog.integrations.s3.GraylogS3Function::handleRequest</em>.</p>
</li>
<li>
<p>Specify at least the following required environment variables to configure the Lambda function for your Graylog cluster:</p>
<ul>
<li>
<p><strong>CONTENT_TYPE</strong> (required) - <em>application/x.cloudflare.log</em> value to indicate that the Lambda function will process Cloudflare logs.</p>
</li>
<li>
<p><strong>COMPRESSION_TYPE</strong> <em><strong>(required</strong></em> <strong>)</strong> - <em>gzip</em> since Cloudflare logs are gzip compressed.</p>
</li>
<li>
<p><strong>GRAYLOG_HOST</strong> <em>(required)</em> - hostname or IP address of the Graylog host or cluster load balancer.</p>
</li>
<li>
<p><strong>GRAYLOG_PORT</strong> <em>(optional - defaults to 12201)</em> - The Graylog service port.</p>
</li>
<li>
<p><strong>CONNECT_TIMEOUT</strong> <em>(optional - defaults to 10000)</em> - The number of milliseconds to wait for the connection to be established.</p>
</li>
<li>
<p><strong>LOG_LEVEL</strong> <em>(optional - defaults to INFO)</em> - The level of detail to include in the CloudWatch logs generated from the Lambda function. Supported values are <em>OFF</em>, <em>ERROR</em>, <em>WARN</em>, <em>INFO</em>, <em>DEBUG</em>, <em>TRACE</em>, and <em>ALL</em>. Increase the logging level to help with troubleshooting. See <a href="https://logging.apache.org/log4j/2.0/manual/customloglevels.html">Defining Custom Log Levels in Code</a> for more information.</p>
</li>
<li>
<p><strong>CLOUDFLARE_LOGPUSH_MESSAGE_FIELDS</strong> <em>(optional - defaults to all)</em> - The fields to parse from the message. Specify as a comma-separated list of field names.</p>
</li>
<li>
<p><strong>CLOUDFLARE_LOGPUSH_MESSAGE_SUMMARY_FIELDS</strong> <em>(optional - defaults to ClientRequestHost, ClientRequestPath, OriginIP, ClientSrcPort, EdgeServerIP, EdgeResponseBytes)</em> - The fields to include in the message summary that appears above the parsed fields at the top of each message in Graylog. Specify as a comma-separated list of field names.
<img src="/assets/upstream/images/fundamentals/graylog/screenshots/graylog-environment-variables.png" alt="List of required Graylog environment variables" /></p>
<p><strong>Note:</strong> More configuration variables are available to fine-tune the function configuration in the Graylog Lambda S3 <a href="https://github.com/Graylog2/graylog-s3-lambda/blob/master/README.md#step-2-specify-configuration">README</a> file.</p>
</li>
</ul>
</li>
<li>
<p>Create an AWS S3 Trigger for the Lambda function so that the function can process each Cloudflare log field that is written. Specify the same S3 bucket from <a href="#task-1---preparation">Task 1</a> and choose the <em>All object create events</em> option. Any other desired file filters can be applied here.
<img src="/assets/upstream/images/fundamentals/graylog/screenshots/aws-s3-add-trigger.png" alt="Add trigger dialog with an example AWS S3 Trigger" /></p>
</li>
<li>
<p>If your Graylog cluster is located within a VPC, you will need to <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html">configure your Lambda function to access resources in a VPC</a>. You may also need to create a <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html#create-vpc-endpoint">VPC endpoint for the AWS S3 service</a>. This allows the Lambda function to access S3 directly when running in a VPC.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/3133.md")
</aside>
<h2 id="task-3-import-the-content-pack-in-graylog">Task 3 - Import the content pack in Graylog</h2>
<p>Importing the Cloudflare Logpush content pack into Graylog loads the
necessary configuration to receive Cloudflare logs and installs the
Cloudflare dashboards.</p>
<p>The following components install with the content pack:</p>
<ul>
<li>Cloudflare dashboards (<a href="#task-4---view-the-cloudflare-dashboards">Task 4</a>).</li>
<li>A Cloudflare GELF (TCP) input that allows Graylog to receive Cloudflare logs.</li>
<li>A Cloudflare message <a href="https://docs.graylog.org/en/3.1/pages/streams.html">stream</a>.</li>
<li><a href="https://docs.graylog.org/en/3.1/pages/pipelines/pipelines.html">Pipeline</a> rules that help to process and parse Cloudflare log fields.</li>
</ul>
<p>To import the content pack:</p>
<ol>
<li>
<p>Locate the <em>cloudflare-logpush-content-pack.json</em> file that you downloaded and extracted in <a href="#task-1---preparation">Task 1</a>.</p>
</li>
<li>
<p>In Graylog, go to <strong>System</strong> &gt; <strong>Content Packs</strong> and click <strong>Upload</strong> in the top right. Once uploaded, the Cloudflare Logpush content pack will appear in the list of uploaded content packs.
<img src="/assets/upstream/images/fundamentals/graylog/screenshots/graylog-content-packs.png" alt="Uploading Graylog content packs" /></p>
</li>
<li>
<p>Click <strong>Install</strong>.
<img src="/assets/upstream/images/fundamentals/graylog/screenshots/graylog-content-packs-uploaded.png" alt="Installing Graylog content packs" /></p>
</li>
<li>
<p>In the <strong>Install</strong> dialog, enter an optional install comment, and verify that the correct values are entered for all configuration parameters.</p>
<ul>
<li>A path is required for the MaxMind™️ database, available at <a href="https://dev.maxmind.com/geoip/">https://dev.maxmind.com/geoip/</a>.</li>
<li>A path is also required for the <em>Threat Lookup</em> CSV file, extracted in <a href="#task-1---preparation">Task 1</a>.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/graylog/screenshots/graylog-content-pack-install.png" alt="Adding an install comment and configuring parameters in Install Dialog screen" /></p>
<ol start="5">
<li>Once installed, your Graylog cluster will be ready to receive Cloudflare logs from the Lambda function.</li>
</ol>
<p>Refer to the Graylog Lambda S3 <a href="https://github.com/Graylog2/graylog-s3-lambda/blob/master/README.md">README</a> for additional information and troubleshooting tips.</p>
<h2 id="task-4-view-the-cloudflare-dashboards">Task 4 - View the Cloudflare Dashboards</h2>
<p>You can view your dashboard in the <a href="https://go.graylog.com/cloudflare">Graylog Cloudflare integration page</a>. The dashboards include:</p>
<h3 id="cloudflare-snapshot">Cloudflare - Snapshot</h3>
<p>This is an at-a-glance overview of the most important metrics from your websites and applications on the Cloudflare network. You can use dashboard filters to further slice and dice the information for granular analysis of events and trends.</p>
<p>Use this dashboard to:</p>
<ul>
<li>Monitor the most important web traffic metrics of your websites and applications on the Cloudflare network</li>
<li>View which countries and IPs your traffic is coming from, and analyze the breakdown between mobile and desktop traffic, protocol, methods, and content types</li>
</ul>
<p><img src="/assets/upstream/images/fundamentals/graylog/dashboards/snapshot-cloudflare-dashboard-graylog.png" alt="Visualizing Cloudflare log metrics in the Graylog dashboard" /></p>
<h3 id="cloudflare-security">Cloudflare - Security</h3>
<p>This overview provides insights into threats to your websites and applications, including number of threats stopped,threats over time, top threat countries, and more.</p>
<p>Use this dashboard to:</p>
<ul>
<li>Monitor the most important security and threat metrics for your websites and applications</li>
<li>Fine-tune and configure your IP firewall</li>
</ul>
<p><img src="/assets/upstream/images/fundamentals/graylog/dashboards/security-cloudflare-dashboard-graylog.png" alt="Visualizing an analysis of Cloudflare threat traffic in the Graylog dashboard" /></p>
<h3 id="cloudflare-performance">Cloudflare - Performance</h3>
<p>This dashboard helps to identify and address performance issues and caching misconfigurations. Metrics include total vs. cached bandwidth, saved bandwidth, total requests, cache ratio, top uncached requests, and more.</p>
<p>Use this dashboard to:</p>
<ul>
<li>Monitor caching behavior and identify misconfigurations</li>
<li>Improve configuration and caching ratio</li>
</ul>
<p><img src="/assets/upstream/images/fundamentals/graylog/dashboards/performance-cloudflare-dashboard-graylog.png" alt="Visualizing Cloudflare Performance metrics in the Graylog dashboard" /></p>
<h3 id="cloudflare-reliability">Cloudflare - Reliability</h3>
<p>This dashboard provides insights on the availability of your websites and applications. Metrics include origin response error ratio, origin response status over time, percentage of 3xx/4xx/5xx errors over time, and more.</p>
<p>Use this dashboard to:</p>
<ul>
<li>Investigate errors on your websites and applications by viewing edge and origin response status codes</li>
<li>Further analyze errors based on status codes by countries, client IPs, hostnames, and other metrics</li>
</ul>
<p><img src="/assets/upstream/images/fundamentals/graylog/dashboards/reliability-cloudflare-dashboard-graylog.png" alt="Graylog dashboard Cloudflare Reliability" /></p>
<h3 id="cloudflare-bots">Cloudflare - Bots</h3>
<p>Use this dashboard to detect and mitigate bad bots so that you can prevent credential stuffing, spam registration, content scraping, click fraud, inventory hoarding, and other malicious activities.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-2">Note</h3>
@markup("md", "content/.markup/bodies/3132.md")
</aside>
<p>Use this dashboard to:</p>
<ul>
<li>Investigate bot activity on your website and prevent content scraping, checkout fraud, spam registration, and other malicious activities.</li>
<li>Use insight to tune Cloudflare to prevent bots from excessive usage and abuse across websites, applications, and API endpoints.</li>
</ul>
<p><img src="/assets/upstream/images/fundamentals/graylog/dashboards/bot-management-cloudflare-dashboard-graylog.png" alt="Graylog dashboard Cloudflare Bot Management" /></p>
