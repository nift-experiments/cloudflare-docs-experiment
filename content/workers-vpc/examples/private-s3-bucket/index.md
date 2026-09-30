<p>This example demonstrates how to access a private S3 bucket that is not exposed to the public internet. In this guide, we will configure a Workers VPC Service for an internal S3-compatible storage service, create a Worker that makes requests to that bucket, and deploy the Worker to validate our changes.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A private S3-compatible storage service running in your VPC/virtual network (such as AWS S3 VPC endpoint, MinIO, or similar)</li>
<li>A virtual machine/EC2 instance running in the same VPC as your S3 VPC endpoint</li>
<li>Workers account with Workers VPC access</li>
</ul>
<h2 id="1-set-up-cloudflare-tunnel"><ol>
<li>Set up Cloudflare Tunnel</li>
</ol></h2>
<p>A Cloudflare Tunnel creates a secure connection from your private network to Cloudflare. This tunnel will allow Workers to securely access your private resources.</p>
<ol>
<li>
<p>Navigate to the <a href="https://dash.cloudflare.com/?to=/:account/workers/vpc/tunnels">Workers VPC dashboard</a> and select the <strong>Tunnels</strong> tab.</p>
</li>
<li>
<p>Select <strong>Create</strong> to create a new tunnel.</p>
</li>
<li>
<p>Enter a name for your tunnel (for example, <code>s3-tunnel</code>) and select <strong>Save tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system and architecture. The dashboard will provide specific installation instructions for your environment.</p>
</li>
<li>
<p>Follow the provided commands to download and install <code>cloudflared</code> on your VM, and execute the service installation command with your unique token.</p>
</li>
</ol>
<p>The dashboard will confirm when your tunnel is successfully connected. Note the tunnel ID for the next step.</p>
<h2 id="2-create-the-workers-vpc-service"><ol start="2">
<li>Create the Workers VPC Service</li>
</ol></h2>
<p>First, create a Workers VPC Service for your internal S3 storage:</p>
<pre><code class="language-bash">npx wrangler vpc service create s3-storage \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-hostname s3.us-west-2.amazonaws.com&#10;</code></pre>
<p>You can also create a Workers VPC Service using an IP address (for example, if using MinIO):</p>
<pre><code class="language-bash">npx wrangler vpc service create s3-storage \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-ipv4 10.0.1.60 \&#10;  &#45;-http-port 9000&#10;</code></pre>
<p>Note the service ID returned for the next step.</p>
<h2 id="3-configure-s3-bucket-policy"><ol start="3">
<li>Configure S3 bucket policy</li>
</ol></h2>
<p>Configure your S3 bucket to allow anonymous access from your VPC endpoint. This works for unencrypted S3 objects:</p>
<pre><code class="language-json">{&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Sid&quot;: &quot;AllowAnonymousAccessFromVPCE&quot;,&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Principal&quot;: &quot;*&quot;,&#10;			&quot;Action&quot;: [&quot;s3:GetObject&quot;, &quot;s3:ListBucket&quot;],&#10;			&quot;Resource&quot;: [&#10;				&quot;arn:aws:s3:::your-bucket-name&quot;,&#10;				&quot;arn:aws:s3:::your-bucket-name/*&quot;&#10;			],&#10;			&quot;Condition&quot;: {&#10;				&quot;StringEquals&quot;: {&#10;					&quot;aws:sourceVpce&quot;: &quot;vpce-your-endpoint-id&quot;&#10;				}&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h3 id="testing-s3-access-directly">Testing S3 access directly</h3>
<p>You can test S3 access directly from the VM where your Cloudflare Tunnel is running to verify the bucket policy is working correctly. These commands should work without any AWS credentials:</p>
<pre><code class="language-bash">&#35; Test listing bucket contents&#10;curl -i https://s3.us-west-2.amazonaws.com/your-bucket-name/&#10;&#10;&#35; Test downloading a specific file&#10;curl -i https://your-bucket-name.s3.us-west-2.amazonaws.com/test-file.txt&#10;</code></pre>
<h2 id="4-configure-your-worker"><ol start="4">
<li>Configure your Worker</li>
</ol></h2>
<p>Update your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15875.md")
</div>
<h2 id="5-implement-the-worker"><ol start="5">
<li>Implement the Worker</li>
</ol></h2>
<p>In your Workers code, use the Workers VPC Service binding in order to send requests to the service:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		try {&#10;			// Fetch a file from the private S3 bucket via VPC endpoint&#10;			const response = await env.S3_STORAGE.fetch(&quot;https://s3.us-west-2.amazonaws.com/my-bucket/data.json&quot;);&#10;&#10;			// Use the response from S3 to perform more logic in Workers, before returning the final response&#10;			return response;&#10;		} catch (error) {&#10;			return new Response(&quot;Storage unavailable&quot;, { status: 503 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<p>This guide demonstrates how you could access private object storage from your Workers. You could use Workers VPC Services to fetch files directly and manipulate the responses to enable you to build more full-stack and backend functionality on Workers.</p>
<h2 id="6-deploy-and-test"><ol start="6">
<li>Deploy and test</li>
</ol></h2>
<p>Now, you can deploy and test your Worker that you have created:</p>
<pre><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<pre><code class="language-bash">&#35; Test GET request&#10;curl https://private-s3-gateway.workers.dev&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Add <a href="/workers/examples/auth-with-headers/">authentication and authorization</a></li>
<li>Implement <a href="/durable-objects/api/">rate limiting</a></li>
<li>Set up <a href="/analytics/analytics-engine/">monitoring and alerting</a></li>
<li>Explore <a href="/workers-vpc/examples/">other examples</a></li>
</ul>
