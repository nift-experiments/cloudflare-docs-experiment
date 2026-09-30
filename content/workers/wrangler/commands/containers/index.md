<p>Interact with <a href="/containers/">Containers</a> using Wrangler.</p>
<h3 id="containers-build">build</h3>
<p>Build a Container image from a Dockerfile.</p>
<pre><code class="language-txt">wrangler containers build [PATH] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>PATH</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path for the directory containing the Dockerfile to build.</li>
</ul>
</li>
<li><code>-t, --tag</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>Name and optionally a tag (format: &quot;name:tag&quot;).</li>
</ul>
</li>
<li><code>--path-to-docker</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path to your docker binary if it's not on <code>$PATH</code>.</li>
<li>Default: &quot;docker&quot;</li>
</ul>
</li>
<li><code>-p, --push</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Push the built image to Cloudflare's managed registry.</li>
<li>Default: false</li>
</ul>
</li>
</ul>
<h3 id="containers-delete">delete</h3>
<p>Delete a Container (application).</p>
<pre><code class="language-txt">wrangler containers delete &lt;CONTAINER_ID&gt; [OPTIONS]&#10;</code></pre>
<ul>
<li><code>CONTAINER_ID</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The ID of the Container to delete.</li>
</ul>
</li>
</ul>
<h3 id="containers-images">images</h3>
<p>Perform operations on images in your containers registry.</p>
<h4 id="containers-images-list">images list</h4>
<p>List images in your containers registry.</p>
<pre><code class="language-txt">wrangler containers images list [OPTIONS]&#10;</code></pre>
<ul>
<li><code>--filter</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Regex to filter results.</li>
</ul>
</li>
<li><code>--json</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Return output as clean JSON.</li>
<li>Default: false</li>
</ul>
</li>
</ul>
<h4 id="containers-images-delete">images delete</h4>
<p>Remove an image from your containers registry.</p>
<pre><code class="language-txt">wrangler containers images delete [IMAGE] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>IMAGE</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>Image to delete of the form <code>IMAGE:TAG</code></li>
</ul>
</li>
</ul>
<h3 id="containers-registries">registries</h3>
<p>Configure and view registries available to your container.
<a href="/containers/guides/image-management/#using-amazon-ecr-container-images">Read more</a> about our currently supported external registries.</p>
<h4 id="containers-registries-list">registries list</h4>
<p>List registries your containers are able to use.</p>
<pre><code class="language-txt">wrangler containers registries list [OPTIONS]&#10;</code></pre>
<ul>
<li><code>--json</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Return output as clean JSON.</li>
<li>Default: false</li>
</ul>
</li>
</ul>
<h4 id="containers-registries-configure">registries configure</h4>
<p>Configure a new registry for your account.</p>
<pre><code class="language-txt">wrangler containers registries configure [DOMAIN] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>DOMAIN</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>Domain to configure for the registry.</li>
</ul>
</li>
<li><code>--dockerhub-username</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The Docker Hub username to authenticate with. Use with the <code>docker.io</code> domain. The secret is a Docker Hub personal access token.</li>
</ul>
</li>
<li><code>--aws-access-key-id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The AWS access key ID to authenticate with. Use with an Amazon ECR domain. The secret is the matching AWS secret access key.</li>
</ul>
</li>
<li><code>--gar-email</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The Google service account email to authenticate with. Use with a <code>*-docker.pkg.dev</code> domain.</li>
</ul>
</li>
<li><code>--secret-store-id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The ID of the secret store to use to store the registry credentials</li>
</ul>
</li>
<li><code>--secret-name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The name Wrangler should store the registry credentials under</li>
</ul>
</li>
</ul>
<p>The credential flags are mutually exclusive. Use the one that matches the registry you are configuring.</p>
<p>When run interactively, wrangler will prompt you for your secret and store it in Secrets Store.
To run non-interactively, you can send your secret value to wrangler through stdin to have
the secret created for you.</p>
<h4 id="containers-registries-delete">registries delete</h4>
<p>Remove a registry configuration from your account.</p>
<pre><code class="language-txt">wrangler containers registries delete [DOMAIN] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>DOMAIN</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>domain of the registry to delete</li>
</ul>
</li>
</ul>
<h4 id="containers-registries-credentials">registries credentials</h4>
<p>Generate temporary credentials to push or pull images from the Cloudflare managed registry (<code>registry.cloudflare.com</code>).</p>
<pre><code class="language-txt">wrangler containers registries credentials [OPTIONS]&#10;</code></pre>
<ul>
<li><code>--push</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Generate credentials with push permission.</li>
</ul>
</li>
<li><code>--pull</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Generate credentials with pull permission.</li>
</ul>
</li>
<li><code>--expiration-minutes</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>How long the credentials should be valid for (in minutes).</li>
<li>Default: 15</li>
</ul>
</li>
</ul>
<p>At least one of <code>--push</code> or <code>--pull</code> must be specified.</p>
<h3 id="containers-info">info</h3>
<p>Get information about a specific Container, including top-level details and a list of instances.</p>
<pre><code class="language-txt">wrangler containers info &lt;CONTAINER_ID&gt; [OPTIONS]&#10;</code></pre>
<ul>
<li><code>CONTAINER_ID</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The ID of the Container to get information about.</li>
</ul>
</li>
</ul>
<h3 id="containers-instances">instances</h3>
<p>List all Container instances for a given application. Displays instance ID, name, state, location, version, and creation time.</p>
<p>In interactive mode, results are paginated. Press <code>Enter</code> to load the next page or <code>Esc</code>/<code>q</code> to stop. In non-interactive environments (for example, when piping output or running in CI), all pages are fetched automatically.</p>
<p>Use the <code>--json</code> flag to return output as a flat JSON array. Each element contains the fields <code>id</code>, <code>name</code>, <code>state</code>, <code>location</code>, <code>version</code>, and <code>created</code>. This is also the default output format in non-interactive environments.</p>
<pre><code class="language-txt">wrangler containers instances &lt;APPLICATION_ID&gt; [OPTIONS]&#10;</code></pre>
<ul>
<li><code>APPLICATION_ID</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The UUID of the application to list instances for. Use <code>wrangler containers list</code> to find application IDs.</li>
</ul>
</li>
<li><code>--per-page</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Number of instances per page.</li>
<li>Default: 25</li>
</ul>
</li>
<li><code>--json</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Return output as clean JSON.</li>
<li>Default: false</li>
</ul>
</li>
</ul>
<p>For example, to list instances for an application:</p>
<pre><code class="language-sh">wrangler containers instances 12345678-abcd-1234-abcd-123456789abc&#10;</code></pre>
<pre><code class="language-sh">INSTANCE                              NAME        STATE          LOCATION  VERSION  CREATED&#10;a1b2c3d4-e5f6-7890-abcd-ef1234567890  worker-12   running        sfo06     3        2025-06-01T12:00:00Z&#10;b2c3d4e5-f6a7-8901-bcde-f12345678901  worker-47   provisioning   iad01     2        2025-06-01T13:00:00Z&#10;</code></pre>
<p>To get the same data as JSON:</p>
<pre><code class="language-sh">wrangler containers instances 12345678-abcd-1234-abcd-123456789abc --json&#10;</code></pre>
<pre><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;		&quot;name&quot;: &quot;worker-12&quot;,&#10;		&quot;state&quot;: &quot;running&quot;,&#10;		&quot;location&quot;: &quot;sfo06&quot;,&#10;		&quot;version&quot;: 3,&#10;		&quot;created&quot;: &quot;2025-06-01T12:00:00Z&quot;&#10;	}&#10;]&#10;</code></pre>
<h3 id="containers-list">list</h3>
<p>List the Containers in your account.</p>
<pre><code class="language-txt">wrangler containers list [OPTIONS]&#10;</code></pre>
<h3 id="containers-push">push</h3>
<p>Push a tagged image to a Cloudflare managed registry, which is automatically integrated with your account.</p>
<pre><code class="language-txt">wrangler containers push [TAG] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>TAG</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name and tag of the container image to push.</li>
</ul>
</li>
<li><code>--path-to-docker</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path to your docker binary if it's not on <code>$PATH</code>.</li>
<li>Default: &quot;docker&quot;</li>
</ul>
</li>
</ul>
<h3 id="containers-ssh">ssh</h3>
<p>Connect to a running Container instance using SSH. Refer to <a href="/containers/guides/ssh/">SSH</a> for configuration details.</p>
<pre><code class="language-txt">wrangler containers ssh &lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>You can also specify a command to run, instead of the default shell. For example:</p>
<pre><code class="language-txt">wrangler containers ssh &lt;INSTANCE_ID&gt; -- ls -al&#10;</code></pre>
<ul>
<li><code>INSTANCE_ID</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The ID of the Container instance to SSH into.</li>
</ul>
</li>
</ul>
