<p>This tutorial demonstrates how to secure access to Amazon S3 buckets with Cloudflare Zero Trust so that data in these buckets is not publicly exposed on the Internet. You can combine Cloudflare Access and AWS VPC endpoints. Enterprise may also use Cloudflare Gateway egress policies with dedicated egress IPs.</p>
<h2 id="method-1-via-cloudflare-access-and-vpc-endpoints">Method 1: Via Cloudflare Access and VPC endpoints</h2>
<pre><code class="language-mermaid">flowchart TB&#10;    cf1[/Cloudflare One Client or clientless users/]--Access policy--&gt;cf2{{Cloudflare}}&#10;    cf2--Cloudflare Tunnel--&gt;vpc1&#10;&#10;    subgraph VPC&#10;    vpc1[EC2 VM]--&gt;vpc2[VPC endpoint]&#10;    end&#10;    vpc2--&gt;s3_1&#10;&#10;    subgraph S3 service&#10;    s3_1([S3 bucket])&#10;    end&#10;&#10;    i1[/Users outside &lt;/br&gt; Zero Trust/]-. &quot;S3 access denied&quot; .-&gt;s3_1&#10;</code></pre>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>S3 bucket to be protected by Cloudflare Zero Trust</li>
<li>AWS VPC with one EC2 virtual machine (VM) hosting the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel daemon</a></li>
<li>S3 bucket and AWS VPC configured in the same <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html">AWS region</a></li>
</ul>
<h3 id="1-create-a-vpc-endpoint-in-aws"><ol>
<li>Create a VPC endpoint in AWS</li>
</ol></h3>
<ol>
<li>In the <a href="https://aws.amazon.com/console/">AWS dashboard</a>, go to <strong>Services</strong> &gt; <strong>Networking &amp; Content Delivery</strong> &gt; <strong>VPC</strong>.</li>
<li>Under <strong>Virtual private cloud</strong>, go to <strong>Endpoints</strong>.</li>
<li>Select <strong>Create endpoint</strong> and name the endpoint.</li>
<li>Choose <em>AWS services</em> as the service category.</li>
<li>In <strong>Services</strong>, search and select the S3 service in the same region of the VPC. For example, for the AWS region <strong>Europe (London) - eu-west-2</strong>, the corresponding S3 service is named <code>com.amazonaws.eu-west-2.s3</code> with a type of Gateway.</li>
<li>In <strong>VPC</strong>, select your VPC that contains the EC2 VM hosting the Cloudflare tunnel daemon.</li>
<li>In <strong>Route tables</strong>, select the route table associated with the VPC.</li>
<li>In <strong>Policy</strong>, choose <em>Full access</em>.</li>
<li>Select <strong>Create endpoint</strong>.</li>
</ol>
<p>After you create the VPC endpoint, a new entry in the VPC route table with the target being your VPC endpoint. The entry will have the format <code>vpce-xxxxxxxxxxxxxxxxx</code>.</p>
<h3 id="2-set-up-a-bucket-policy-for-vpc-access"><ol start="2">
<li>Set up a bucket policy for VPC access</li>
</ol></h3>
<ol>
<li>Go to <strong>Services</strong> &gt; <strong>Storage</strong> &gt; <strong>S3</strong>.</li>
<li>In Amazon S3, go to <strong>Buckets</strong> &gt; <strong>&lt;your-S3-bucket&gt;</strong> &gt; <strong>Permissions</strong>.</li>
<li>Disable <strong>Block all public access</strong>.</li>
<li>In <strong>Bucket policy</strong>, add the following policy:</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Id&quot;: &quot;VPCe&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Sid&quot;: &quot;VPCe&quot;,&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Principal&quot;: &quot;*&quot;,&#10;			&quot;Action&quot;: &quot;s3:*&quot;,&#10;			&quot;Resource&quot;: [&#10;				&quot;arn:aws:s3:::&lt;your-S3-bucket01&gt;&quot;,&#10;				&quot;arn:aws:s3:::&lt;your-S3-bucket01&gt;/*&quot;&#10;			],&#10;			&quot;Condition&quot;: {&#10;				&quot;StringEquals&quot;: {&#10;					&quot;aws:SourceVpce&quot;: &quot;&lt;your-vpc-endpoint&gt;&quot;&#10;				}&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Your bucket policy will allow your VPC to access your S3 bucket.</p>
<h3 id="3-enable-static-website-hosting-for-the-s3-bucket"><ol start="3">
<li>Enable static website hosting for the S3 bucket</li>
</ol></h3>
<ol>
<li>Return to Amazon S3, then go to <strong>Buckets</strong> &gt; <strong>&lt;your-S3-bucket01&gt;</strong> &gt; <strong>Properties</strong>.</li>
<li>In <strong>Static website hosting</strong>, select <strong>Edit</strong>.</li>
<li>Enable <strong>Static website hosting</strong>.</li>
<li>Specify the Index and Error documents for the S3 bucket.</li>
<li>Select <strong>Save changes</strong>.</li>
</ol>
<p>A bucket website endpoint will be available at <code>http://&lt;your-S3-bucket01&gt;.s3-website.&lt;aws-region&gt;.amazonaws.com</code>. Because of the bucket policy, this website endpoint will only be accessible from the VPC with the VPC endpoint configured.</p>
<h3 id="4-add-a-published-application-to-the-cloudflare-tunnel"><ol start="4">
<li>Add a published application to the Cloudflare Tunnel</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your tunnel, then go to the <strong>Routes</strong> tab.</li>
<li>Select <strong>Add route</strong>, then select <strong>Published application</strong>.</li>
<li>Enter a subdomain your organization will use to access the S3 bucket. For example, <code>s3-bucket.&lt;your-domain&gt;.com</code>.</li>
<li>In <strong>Service URL</strong>, enter <code>http://&lt;your-S3-bucket01&gt;.s3-website.&lt;aws-region&gt;.amazonaws.com</code>.</li>
<li>In <strong>Additional application settings</strong> &gt; <strong>HTTP Settings</strong>, input the <strong>HTTP Host Header</strong> as <code>&lt;your-S3-bucket01&gt;.s3-website.&lt;aws-region&gt;.amazonaws.com</code>.</li>
<li>Select <strong>Save hostname</strong>.</li>
</ol>
<p>Your Cloudflare Tunnel will terminate at the AWS VPC using your public hostname.</p>
<h3 id="5-restrict-s3-access-with-an-access-policy"><ol start="5">
<li>Restrict S3 access with an Access policy</li>
</ol></h3>
<ol>
<li>Go to <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong>.</li>
<li>Select <strong>Self-hosted and private</strong>.</li>
<li>Select <strong>Add public hostname</strong> and enter the public hostname used by your Tunnel. For example, <code>s3-bucket.&lt;your-domain&gt;.com</code>.</li>
<li>Add <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to determine which users and applications may access your bucket. You can optionally create a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a> policy to automatically authenticate access to your S3 bucket.</li>
<li>Follow the remaining <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application creation steps</a> to publish the application.</li>
</ol>
<p>Users and applications that successfully authenticate via Cloudflare Access can access your S3 bucket at <code>https://s3-bucket.&lt;your-domain&gt;.com</code>.</p>
<h2 id="method-2-via-cloudflare-gateway-egress-policies">Method 2: Via Cloudflare Gateway egress policies</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4292.md")
</aside>
<pre><code class="language-mermaid">flowchart TB&#10;    cf1[/Cloudflare One Client users/]--Egress policy--&gt;cf2{{Cloudflare}}&#10;    cf2--Egress with dedicated IP--&gt;i1[Internet]&#10;    i1--&gt;s3_1&#10;&#10;    subgraph S3 Service&#10;    s3_1([S3 bucket])&#10;    end&#10;&#10;    i2[/Users outside &lt;/br&gt; Zero Trust/]-. &quot;IPs denied&quot; .-&gt;s3_1&#10;</code></pre>
<h3 id="prerequisites-1">Prerequisites</h3>
<ul>
<li>Cloudflare Zero Trust account with <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a></li>
<li>S3 bucket to be protected by Cloudflare Zero Trust</li>
</ul>
<h3 id="1-set-up-a-bucket-policy-to-restrict-access-to-a-specific-ip-address"><ol>
<li>Set up a bucket policy to restrict access to a specific IP address</li>
</ol></h3>
<ol>
<li>In the <a href="https://aws.amazon.com/console/">AWS dashboard</a>, go to <strong>Services</strong> &gt; <strong>Storage</strong> &gt; <strong>S3</strong>.</li>
<li>Go to <strong>Buckets</strong> &gt; <strong>&lt;your-S3-bucket02&gt;</strong> &gt; <strong>Permissions</strong>.</li>
<li>Disable <strong>Block all public access</strong>.</li>
<li>In <strong>Bucket policy</strong>, add the following policy:</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Id&quot;: &quot;SourceIP&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Sid&quot;: &quot;SourceIP&quot;,&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Principal&quot;: &quot;*&quot;,&#10;			&quot;Action&quot;: &quot;s3:*&quot;,&#10;			&quot;Resource&quot;: [&#10;				&quot;arn:aws:s3:::&lt;your-S3-bucket02&gt;&quot;,&#10;				&quot;arn:aws:s3:::&lt;your-S3-bucket02&gt;/*&quot;&#10;			],&#10;			&quot;Condition&quot;: {&#10;				&quot;IpAddress&quot;: {&#10;					&quot;aws:SourceIp&quot;: &quot;&lt;your-dedicated-ip&gt;/32&quot;&#10;				}&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h3 id="2-enable-static-website-hosting-for-the-s3-bucket"><ol start="2">
<li>Enable static website hosting for the S3 bucket</li>
</ol></h3>
<ol>
<li>Return to your bucket, then go to <strong>Properties</strong>.</li>
<li>In <strong>Static website hosting</strong>, select <strong>Edit</strong>.</li>
<li>Enable <strong>Static website hosting</strong>.</li>
<li>Specify the Index and Error documents for the S3 bucket.</li>
<li>Select <strong>Save changes</strong>.</li>
</ol>
<p>A bucket website endpoint will be available at <code>http://&lt;your-S3-bucket02&gt;.s3-website.&lt;aws-region&gt;.amazonaws.com</code>. Because of the bucket policy, the website endpoint will only be accessible to traffic sourced from the dedicated egress IP specified.</p>
<h3 id="3-setup-a-dedicated-egress-ip-policy"><ol start="3">
<li>Setup a dedicated egress IP policy</li>
</ol></h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Egress policies</strong>. Select <strong>Add a policy</strong>.</li>
<li>Create a policy that specifies which proxied traffic Gateway should assign a <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IP</a> to. For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/">Egress policies</a>.</li>
<li>In <strong>Select an egress IP</strong>, choose <em>Use dedicated Cloudflare egress IPs</em>. Select the dedicated egress IP defined in your bucket policy.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>Traffic proxied by Gateway and assigned your specified egress IP can access your S3 bucket at <code>http://&lt;your-S3-bucket02&gt;.s3-website.&lt;aws-region&gt;.amazonaws.com</code>.</p>
