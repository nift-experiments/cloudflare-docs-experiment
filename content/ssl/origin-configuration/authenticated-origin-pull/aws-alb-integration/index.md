---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/
  description: Learn how to set up Cloudflare Authenticated Origin Pulls with the AWS Application Load Balancer.
  full_title: AWS integration · Cloudflare SSL/TLS docs
  head_html: <title>AWS integration · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up Cloudflare Authenticated Origin Pulls with the AWS Application Load Balancer."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/index.md"><meta property="og:title" content="AWS integration · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up Cloudflare Authenticated Origin Pulls with the AWS Application Load Balancer."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="AWS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/#page","headline":"AWS integration \u00b7 Cloudflare SSL/TLS docs","description":"Learn how to set up Cloudflare Authenticated Origin Pulls with the AWS Application Load Balancer.","url":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AWS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/
  schema: 1
---
<p>This guide will walk you through how to set up <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> authenticated origin pulls to securely connect to an AWS Application Load Balancer using <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html">mutual TLS verify</a>.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>You should already have your AWS account and <a href="https://docs.aws.amazon.com/ec2/?icmpid=docs_homepage_featuredsvcs">EC2</a> configured.</li>
<li>Note that this tutorial uses command-line interface (CLI) to generate a custom certificate, and <a href="/fundamentals/api/get-started/">API calls</a> to configure Cloudflare Authenticated Origin Pulls.</li>
<li>For the most up-to-date documentation on how to set up AWS, refer to the <a href="https://docs.aws.amazon.com/">AWS documentation</a>.</li>
</ul>
<h2 id="1-generate-a-custom-certificate"><ol>
<li>Generate a custom certificate</li>
</ol></h2>
<ol>
<li>Run the following command to generate a 4096-bit RSA private key, using AES-256 encryption. Enter a passphrase when prompted.</li>
</ol>
<pre tabindex="0"><code class="language-bash">openssl genrsa -aes256 -out rootca.key 4096&#10;</code></pre>
<ol start="2">
<li>Create the CA root certificate. When prompted, fill in the information to be included in the certificate. For the <code>Common Name</code> field, use the domain name as value, not the hostname.</li>
</ol>
<pre tabindex="0"><code class="language-bash">openssl req -x509 -new -nodes -key rootca.key -sha256 -days 1826 -out rootca.crt&#10;</code></pre>
<ol start="3">
<li>Create a Certificate Signing Request (CSR). When prompted, fill in the information to be included in the request. For the <code>Common Name</code> field, use the hostname as value.</li>
</ol>
<pre tabindex="0"><code class="language-bash">openssl req -new -nodes -out cert.csr -newkey rsa:4096 -keyout cert.key&#10;</code></pre>
<ol start="4">
<li>Sign the certificate using the <code>rootca.key</code> and <code>rootca.crt</code> created in previous steps.</li>
</ol>
<pre tabindex="0"><code class="language-bash">openssl x509 -req -in cert.csr -CA rootca.crt -CAkey rootca.key -CAcreateserial -out cert.crt -days 730 -sha256 -extfile ./cert.v3.ext&#10;</code></pre>
<ol start="5">
<li>Make sure the certificate extensions file <code>cert.v3.ext</code> specifies the following:</li>
</ol>
<pre tabindex="0"><code>basicConstraints=CA:FALSE&#10;</code></pre>
<h2 id="2-configure-aws-application-load-balancer"><ol start="2">
<li>Configure AWS Application Load Balancer</li>
</ol></h2>
<ol>
<li>Upload the <code>rootca.cert</code> to an <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html">S3 bucket</a>.</li>
<li><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html#create-trust-store">Create a trust store</a> at your EC2 console, indicating the <strong>S3 URI</strong> where you uploaded the certificate.</li>
<li>Create an EC2 instance and install an HTTPD daemon. Choose an <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">instance type</a> according to your needs - it can be a minimal instance eligible to <a href="https://aws.amazon.com/free/">AWS Free Tier</a>. This tutorial was based on an example using t2.micro and <a href="https://docs.aws.amazon.com/linux/al2023/ug/what-is-amazon-linux.html">Amazon Linux 2023</a>.</li>
</ol>
<pre tabindex="0"><code class="language-bash">sudo yum install -y httpd&#10;sudo systemctl start httpd&#10;</code></pre>
<ol start="4">
<li>Create a <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html#configure-target-group">target group</a> for your Application Load Balancer.
<ul>
<li>Choose <strong>Instances</strong> as target type.</li>
<li>Specify port <code>HTTP/80</code>.</li>
</ul>
</li>
<li>After you finish configuring the target group, confirm that the target group is <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html">healthy</a>.</li>
<li><a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html#configure-load-balancer">Configure a load balancer and a listener</a>.
<ul>
<li>Choose the <strong>Internet-facing</strong> scheme.</li>
<li>Switch the listener to port <code>443</code> so that the <strong>mTLS</strong> option is available, and select the target group created in previous steps.</li>
<li>For <strong>Default SSL/TLS server certificate</strong>, choose <strong>Import certificate</strong> &gt; <strong>Import to ACM</strong>, and add the certificate private key and body.</li>
<li>Under <strong>Client certificate handling</strong>, select <strong>Verify with trust store</strong>.</li>
</ul>
</li>
<li>Save your settings.</li>
<li>(Optional) Run the following commands to confirm that the Application Load Balancing is asking for the client certificate.</li>
</ol>
<pre tabindex="0"><code class="language-bash">openssl s_client -verify 5 -connect &lt;your-application-load-balancer&gt;:443 -quiet -state&#10;</code></pre>
<p>Since you have not yet uploaded the certificate to Cloudflare, the connection should fail (<code>read:errno=54</code>, for example).</p>
<p>You can also run <code>curl --verbose</code> and confirm <code>Request CERT (13)</code> is present within the SSL/TLS handshake:</p>
<pre tabindex="0"><code class="language-bash">curl --verbose https://&lt;your-application-load-balancer&gt;&#10;...&#10;&#42; TLSv1.2 (IN), TLS handshake, Request CERT (13):&#10;...&#10;</code></pre>
<h2 id="3-configure-cloudflare"><ol start="3">
<li>Configure Cloudflare</li>
</ol></h2>
<ol>
<li><a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/create/">Upload the certificate</a> you created in <a href="#1-generate-a-custom-certificate">Step 1</a> to Cloudflare. You should use the leaf certificate, not the root CA.</li>
</ol>
<pre tabindex="0"><code class="language-bash">MYCERT=&quot;$(cat cert.crt|perl -pe &#x27;s/\r?\n/\\n/&#x27;|sed -e &#x27;s/..$//&#x27;)&quot;&#10;MYKEY=&quot;$(cat cert.key|perl -pe &#x27;s/\r?\n/\\n/&#x27;|sed -e&#x27;s/..$//&#x27;)&quot;&#10;&#10;request_body=$(&lt; &lt;(cat &lt;&lt;EOF&#10;{&#10;&quot;certificate&quot;: &quot;$MYCERT&quot;,&#10;&quot;private_key&quot;: &quot;$MYKEY&quot;,&#10;&quot;bundle_method&quot;:&quot;ubiquitous&quot;&#10;}&#10;EOF&#10;))&#10;&#10;&#35; Push the certificate&#10;&#10;curl --silent \&#10;&quot;https://api.cloudflare.com/client/v4/zones/$ZONEID/origin_tls_client_auth/hostnames/certificates&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-header &quot;X-Auth-Email: $MYAUTHEMAIL&quot; \&#10;&#45;-header &quot;X-Auth-Key: $MYAUTHKEY&quot; \&#10;&#45;-data &quot;$request_body&quot;&#10;</code></pre>
<ol start="2">
<li><a href="/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/">Associate the certificate with the hostname</a> that should use it.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;config&quot;: [&#10;    {&#10;      &quot;enabled&quot;: true,&#10;      &quot;cert_id&quot;: &quot;&lt;CERT_ID&gt;&quot;,&#10;      &quot;hostname&quot;: &quot;&lt;YOUR_HOSTNAME&gt;&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14285.md")
</aside>
<hr />
<h2 id="roll-back-the-cloudflare-configuration">Roll back the Cloudflare configuration</h2>
<ol>
<li>Use a <a href="/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/"><code>PUT</code> request</a> to disable Authenticated Origin Pulls on the hostname.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;config&quot;: [&#10;    {&#10;      &quot;enabled&quot;: false,&#10;      &quot;cert_id&quot;: &quot;&lt;CERT_ID&gt;&quot;,&#10;      &quot;hostname&quot;: &quot;&lt;YOUR_HOSTNAME&gt;&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<ol start="2">
<li>(Optional) Use a <a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list/"><code>GET</code> request</a> to obtain a list of the client certificate IDs. You will need the ID of the certificate you want to remove for the following step.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<ol start="3">
<li>Use the <a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/">Delete hostname client certificate</a> endpoint to remove the certificate you had uploaded.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
