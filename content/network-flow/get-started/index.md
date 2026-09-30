---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/get-started/
  description: Set up Network Flow to monitor network traffic patterns.
  full_title: Get started · Cloudflare Network Flow docs
  head_html: <title>Get started · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Network Flow to monitor network traffic patterns."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Network Flow to monitor network traffic patterns."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Network Flow"><meta name="pcx_tags" content="NetFlow,AWS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/get-started/#page","headline":"Get started \u00b7 Cloudflare Network Flow docs","description":"Set up Network Flow to monitor network traffic patterns.","url":"https://developers.cloudflare.com/network-flow/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["NetFlow","AWS"]}</script>
  markdown: true
  noindex: false
  route: /network-flow/get-started/
  schema: 1
---
<p>Network Flow (formerly Magic Network Monitoring) includes an onboarding workflow that guides you step-by-step through the product configuration process. If you are unable to complete the configuration in one session, you can exit the workflow and resume it at any time.</p>
<p>After completing the setup, you can view traffic analytics, create rules to monitor traffic thresholds, and receive alerts when those thresholds are exceeded. To begin, complete the list of tasks below.</p>
<ul>
<li><a href="#netflow-and-sflow-guide">NetFlow and sFlow guide</a></li>
<li><a href="#vpc-flow-log-guide">VPC flow log guide (beta)</a></li>
</ul>
<p>If you are an Enterprise customer, Cloudflare can significantly accelerate the onboarding timeline during active-attack scenarios.</p>
<p>Enterprise customers that would like to use Network Flow and Magic Transit On Demand together can begin by <a href="/magic-transit/get-started/">configuring Magic Transit</a>.</p>
<h2 id="netflow-and-sflow-guide">NetFlow and sFlow guide</h2>
<h3 id="1-verify-netflow-or-sflow-capabilities"><ol>
<li>Verify NetFlow or sFlow capabilities</li>
</ol></h3>
<p>Verify your routers are capable of exporting <span class="nb-glossary-tooltip" title="NetFlow">NetFlow</span> or <span class="nb-glossary-tooltip" title="sFlow">sFlow</span> to an IP address on Cloudflare's network. Network Flow supports NetFlow v5, NetFlow v9, IPFIX, and sFlow.</p>
<p>Refer to <a href="/network-flow/routers/supported-routers">Supported routers</a> to view a list of supported routers. The list is not exhaustive.</p>
<h3 id="2-register-your-router-with-cloudflare"><ol start="2">
<li>Register your router with Cloudflare</li>
</ol></h3>
<p>Register your router so that Cloudflare knows which IP address to expect flow data from and can associate it with your account.</p>
<ol>
<li>Go to the <strong>Network flow</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Network flow</strong>, select <strong>Configure Network flow</strong>.</li>
<li>Select the <strong>Configure routers</strong> tab.</li>
<li>(Optional) Under <strong>IP Address</strong>, enter your router's public IP address.</li>
<li>Under <strong>Default router sampling rate</strong>, enter a value for the <span class="nb-glossary-tooltip" title="sampling">sampling</span> rate. The value should match the sampling rate of your NetFlow or sFlow configuration.</li>
<li>Select <strong>Next</strong>.</li>
</ol>
<h3 id="3-configure-your-router"><ol start="3">
<li>Configure your router</li>
</ol></h3>
<p>Next, configure your router to send NetFlow or sFlow data to Cloudflare. For this step, you will also need to have your router's configuration menu open to input the values shown in the Cloudflare dashboard.</p>
<p>Refer to the <a href="/network-flow/routers/netflow-ipfix-config/">NetFlow and IPFIX configuration guide</a> or the <a href="/network-flow/routers/sflow-config/">sFlow configuration guide</a> for more information.</p>
<ol>
<li>From <strong>Configure routers</strong> in the dashboard, select either <strong>NetFlow Configuration</strong> or <strong>sFlow configuration</strong>.</li>
<li>Follow the configuration steps for the selected configuration type.</li>
<li>Enter the values shown in your router's configuration.</li>
<li>Select <strong>Next</strong>.</li>
</ol>
<h3 id="4-check-your-router-configuration"><ol start="4">
<li>Check your router configuration</li>
</ol></h3>
<p>After setting up your router, confirm the configuration was successfully set up.</p>
<p>From the <strong>Check routers</strong> page on the dashboard, you can view the status of your routers. Router data typically takes five to ten minutes to appear in the Cloudflare dashboard.</p>
<p>Refer to <strong>Router status description</strong> to confirm whether data is successfully being sent.</p>
<p>When you are done with router configuration, select <strong>Finish onboarding</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/723.md")
</aside>
<h3 id="5-create-rules"><ol start="5">
<li>Create rules</li>
</ol></h3>
<p>Create rules to analyze data for a specific set of destinations or to implement thresholds. Refer to <a href="/network-flow/rules/">Rules</a> for more information.</p>
<h2 id="vpc-flow-log-guide">VPC flow log guide <span class="nb-badge">Beta</span></h2>
<h3 id="1-verify-cloud-flow-log-capabilities"><ol>
<li>Verify cloud flow log capabilities</li>
</ol></h3>
<p>Verify that your Amazon Web Services (AWS) account is capable of exporting AWS Virtual Private Cloud (VPC) flow logs through AWS Firehose. Currently, Network Flow only supports VPC flow log ingestion for AWS.</p>
<h3 id="2-set-up-aws-firehose-to-export-vpc-flow-logs-to-cloudflare"><ol start="2">
<li>Set up AWS Firehose to export VPC flow logs to Cloudflare</li>
</ol></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/722.md")
</aside>
<ol>
<li>Create an authorization token using <a href="/api/resources/magic_network_monitoring/subresources/vpc_flows/subresources/tokens/methods/create/">Cloudflare's API for Network Flow</a>. This authorization token allows Cloudflare to identify and verify the account sending VPC flow logs to our endpoint.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/mnm/vpc-flows/token \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<ol start="2">
<li>
<p>In your AWS Firehose stream configuration, set the <code>HTTP Headers - X-Amz-Firehose-Access-Key</code> to the authorization token generated in the previous step.</p>
</li>
<li>
<p>Send your AWS Firehose VPC flow log stream towards <code>https://aws-flow-logs.cloudflare.com/</code>.</p>
</li>
<li>
<p>Select all of the AWS VPC flow log data fields that you want to send to Cloudflare. You should select the highest number AWS VPC flow log version that supports all the fields you want to export to Cloudflare (refer to <a href="https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html">AWS flow log documentation</a> for more information). For example, if you need a version 8 field like <code>reject-reason</code>, you must export all fields from versions 1 through 8. Cloudflare supports all seven templates for AWS VPC Flow logs.</p>
</li>
</ol>
<h3 id="3-verify-your-cloud-traffic-via-analytics"><ol start="3">
<li>Verify your cloud traffic via analytics</li>
</ol></h3>
<p>After setting up AWS Firehose to send VPC flow logs to Network Flow, you can confirm that Cloudflare is receiving the logs as expected by searching for your cloud traffic data in the analytics page of the Network Flow dashboard.</p>
<ol>
<li>Go to the <strong>Network flow</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>The default view will be the analytics dashboard for Network Flow.</li>
</ol>
