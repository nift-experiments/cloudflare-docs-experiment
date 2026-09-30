<p>When Email security detects a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8571.md")
</div> email, the metadata of the detection can be sent directly to Splunk. This document outlines the steps required to integrate with Splunk Cloud.
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/open-splunk.png" alt="A diagram outlining what happens when Email security detects a phishing email and sends it to Splunk." /></p>
<h2 id="1-configure-splunk-http-event-collector"><ol>
<li>Configure Splunk HTTP Event Collector</li>
</ol></h2>
<ol>
<li>
<p><a href="https://login.splunk.com/">Log in to Splunk</a> with an administrator account.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> &gt; <strong>Data inputs</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/step2-data-inputs.png" alt="Go to Data inputs to configure your settings." /></p>
<ol start="3">
<li>In <strong>Local inputs</strong> &gt; <strong>Type</strong>, select <strong>HTTP Event Collector</strong> to access this configuration and create a new collector.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/step3-type.png" alt="Select HTTP Event Collectors as the type of your collector." /></p>
<ol start="4">
<li>
<p>Select the <strong>New Token</strong> button to start the configuration.</p>
</li>
<li>
<p>Provide a descriptive name for the Email security (formerly Area 1) token (for example, <code>Email security (formerly Area 1) Email Detections</code>), and leave the <strong>Enable indexer acknowledgement</strong> unchecked.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/step5-token.png" alt="Enter a descriptive name for your new token, but leave Enable indexer acknowledgement checkbox unchecked." /></p>
<ol start="6">
<li>
<p>Select <strong>Next</strong> to continue.</p>
</li>
<li>
<p>Configure the Input Settings for the HTTP Event Collector based on your environment.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/step7-input-settings.png" alt="Configure the Input Settings based on your environment" /></p>
<ol start="8">
<li>You may also select <strong>Create a new index</strong> to create new settings for Email security events, with a <strong>Max Size of Entire Index</strong> and <strong>Retention (days)</strong> that fits your environment.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/step8-new-index.png" alt="Optionally, create a new index for Email security events" /></p>
<ol start="9">
<li>For this example, we created a new <code>area1_index</code> index, and added it to the configuration.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/step9-new-index.png" alt="Example of a new index added to the configuration" /></p>
<ol start="10">
<li>
<p>Select <strong>Review</strong> &gt; <strong>Submit</strong> to review your settings and create the collector.</p>
</li>
<li>
<p>Take note of the token value in this next screen. This value is required for the Email security configuration in the next step. You can also retrieve the token from the HTTP Event Collector configuration panel, in <strong>Settings</strong> &gt; <strong>Data inputs</strong> &gt; <strong>HTTP Event Collector</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/step11-token-value.png" alt="Example of a new index added to the configuration" /></p>
<h2 id="2-test-your-http-event-collector"><ol start="2">
<li>Test your HTTP Event Collector</li>
</ol></h2>
<p>To test your the HTTP Event Collector, you can manually inject an event into Splunk by using the following cURL command:</p>
<pre><code class="language-bash">curl https://{host}:8088/services/collector/event \&#10;&#45;-header &quot;Authorization: Splunk &lt;YOUR_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&#10;    &quot;sourcetype&quot;: &quot;&lt;YOUR_SOURCE_TYPE&gt;&quot;,&#10;    &quot;event&quot;: &quot;Hello, World!&quot;&#10;    }&#x27;&#10;</code></pre>
<h3 id="request-formats">Request formats</h3>
<p>When creating requests to Splunk, the URL and port number change according to the type of Splunk setup:</p>
<ul>
<li><strong>Splunk Cloud Platform free trial</strong>: <code>&lt;protocol&gt;://http-inputs-&lt;host&gt;.splunkcloud.com:8088/&lt;endpoint&gt;</code></li>
<li><strong>Splunk Cloud Platform</strong>: <code>&lt;protocol&gt;://http-inputs-&lt;host&gt;.splunkcloud.com:443/&lt;endpoint&gt;</code></li>
<li><strong>Splunk Enterprise</strong>: <code>&lt;protocol&gt;://&lt;host&gt;:8088/&lt;endpoint&gt;</code></li>
</ul>
<p>Refer to the <a href="https://docs.splunk.com/Documentation/Splunk/8.2.2/Data/UsetheHTTPEventCollector">Splunk documentation</a> for more information.</p>
<p>If your instance is on-premise, specify the appropriate hostname and ensure that your firewall allows the configured port through to your instance. The connections will be coming from this <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IP addresses</a>, if you need them for your access control lists (ACLs)</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8570.md")
</aside>
<p>If all the requirements are met, you will receive the following response back to the cURL command:</p>
<pre><code class="language-txt">{&quot;text&quot;:&quot;Success&quot;,&quot;code&quot;:0}&#10;</code></pre>
<p>Additionally, you can search your instance of Splunk for the test event with <code>index</code> or other search criteria (for example, <code>index=&quot;area1_index&quot;</code>):</p>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/search-instance.png" alt="Example of a new index added to the configuration" /></p>
<h2 id="3-configure-email-security"><ol start="3">
<li>Configure Email security</li>
</ol></h2>
<p>The next step is to configure Email security to push the Email Detection Event to the Splunk HTTP Event Collector.</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Alert Webhooks</strong>, and select <strong>New Webhook</strong>.</li>
<li>In the Add Webhooks page, enter the following settings:
<ul>
<li><strong>App type</strong>: Select <strong>SIEM</strong> &gt; <strong>Splunk</strong>, and enter the auth code you took note of the previous step.</li>
<li><strong>Target</strong>: Enter the target URI of your Splunk instance. It will typically have the <code>https://&lt;host&gt;:8088/services/collector</code> format. Refer to <a href="#request-formats">Request formats</a> to learn more about how your Splunk subscription affects the URI.</li>
<li>For the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
</li>
</ol>
@markup("md", "content/.markup/bodies/8572.md")
</div> (`MALICIOUS`, `SUSPICIOUS`, `SPOOF`, `SPAM`, `BULK`) choose which (if any) you want to send to the webhook. Sending `SPAM` and `BULK` dispositions will generate a high number of events.
4. Select **Publish Webhook**.
<p>Your Splunk integration will now show up in the All Webhooks panel.</p>
<p><img src="/assets/upstream/images/email-security/siem-integration/splunk/splunk-webhook-integrations.png" alt="The All Webhooks section will show your Splunk webhook" /></p>
<p>It will take about ten minutes or so for the configuration to fully propagate through the infrastructure of Email security (formerly Area 1), and for events to start to appear in your searches. Once the configuration is propagated, events will start to appear in your instance of Splunk.</p>
