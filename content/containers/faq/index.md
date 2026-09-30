<h2 id="how-do-container-logs-work">How do Container logs work?</h2>
<p>To get logs in the Dashboard, including live tailing of logs, toggle <code>observability</code> to true
in your Worker's wrangler config:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1258.md")
</div>
<p>Logs are subject to the same <a href="/workers/observability/logs/workers-logs/#limits">limits as Worker logs</a>, which means that they are
retained for 3 days on Free plans and 7 days on Paid plans.</p>
<p>See <a href="/workers/observability/logs/workers-logs/#pricing">Workers Logs Pricing</a> for details on cost.</p>
<p>If you are an Enterprise user, you are able to export container logs via <a href="/logs/logpush/">Logpush</a>
to your preferred destination.</p>
<h2 id="how-are-container-instance-locations-selected">How are container instance locations selected?</h2>
<p>When initially deploying a Container, Cloudflare will select various locations across our
network to deploy instances to. These locations will span multiple regions.</p>
<p>When a Container instance is requested with <code>this.ctx.container.start</code>, the nearest free
container instance will be selected from the pre-initialized locations. This will
likely be in the same region as the external request, but may not be. Once the container
instance is running, any future requests will be routed to the initial location.</p>
<p>An Example:</p>
<ul>
<li>A user deploys a Container. Cloudflare automatically readies instances across its Network.</li>
<li>A request is made from a client in Bariloche, Argentina. It reaches the Worker in
Cloudflare's location in Neuquen, Argentina.</li>
<li>This Worker request calls <code>MY_CONTAINER.get(&quot;session-1337&quot;)</code> which brings up a Durable
Object, which then calls <code>this.ctx.container.start</code>.</li>
<li>This requests the nearest free Container instance.</li>
<li>Cloudflare recognizes that an instance is free in Buenos Aires, Argentina, and
starts it there.</li>
<li>A different user needs to route to the same container. This user's request reaches
the Worker running in Cloudflare's location in San Diego.</li>
<li>The Worker again calls <code>MY_CONTAINER.get(&quot;session-1337&quot;)</code>.</li>
<li>If the initial container instance is still running, the request is routed to the location
in Buenos Aires. If the initial container has gone to sleep, Cloudflare will once
again try to find the nearest &quot;free&quot; instance of the Container, likely
one in North America, and start an instance there.</li>
</ul>
<h2 id="how-do-container-updates-and-rollouts-work">How do container updates and rollouts work?</h2>
<p>On <code>wrangler deploy</code>, the Worker goes live first. Container instances update with a gradual rollout by default. Refer to <a href="/containers/configuration/rollouts/">Rollouts</a> for steps, grace periods, and modes. Refer to <a href="/containers/guides/deploy/">Deploy Containers</a> to run a deploy.</p>
<h2 id="how-do-workers-builds-work-with-containers">How do Workers Builds work with Containers?</h2>
<p>On the production branch, Workers Builds should run <code>wrangler deploy</code> so images and container instances can update. Non-production Workers Builds defaults to <code>wrangler versions upload</code>, which does not update images. Containers Workers implement Durable Objects, so preview URLs are not generated for them. Refer to <a href="/containers/guides/deploy/#before-production">Deploy Containers</a>.</p>
<h2 id="how-does-scaling-work">How does scaling work?</h2>
<p>Containers scale by creating or addressing specific instances. For stateless routing across a
fixed number of interchangeable instances, use the <code>getRandom</code> helper.</p>
<p>Refer to <a href="/containers/configuration/scaling-and-routing/">scaling and routing</a> for details.</p>
<h3 id="is-built-in-autoscaling-for-stateless-applications-available">Is built-in autoscaling for stateless applications available?</h3>
<p>Not today, though Cloudflare plans to add built-in autoscaling in a future release.</p>
<p>Until then, use <code>getRandom</code> for simple stateless routing and specific instance IDs when you need
explicit control over container lifecycle.</p>
<h2 id="what-are-cold-starts-how-fast-are-they">What are cold starts? How fast are they?</h2>
<p>A cold start is when a container instance is started from a completely stopped state.</p>
<p>If you call <code>env.MY_CONTAINER.get(id)</code> with a completely novel ID and launch
this instance for the first time, it will result in a cold start.</p>
<p>This will start the container image from its entrypoint for the first time. Depending
on what this entrypoint does, it will take a variable amount of time to start.</p>
<p>Container cold starts can often be in the 1-3 second range, but this is dependent
on image size and code execution time, among other factors.</p>
<h2 id="how-do-i-use-an-existing-container-image">How do I use an existing container image?</h2>
<p>Refer to <a href="/containers/guides/image-management/#use-pre-built-container-images">image management</a>.</p>
<h2 id="is-disk-persistent-what-happens-to-my-disk-when-my-container-sleeps">Is disk persistent? What happens to my disk when my container sleeps?</h2>
<p>All disk is ephemeral. When a Container instance goes to sleep, the next time
it is started, it will have a fresh disk as defined by its container image.</p>
<p>Snapshots are coming soon, which allow the user to quickly persist and restore the disk
from an entire container or a directory.</p>
<p>You can also use <a href="/containers/examples/r2-fuse-mount/">FUSE</a> to persist disk
to R2 or other object storage backends. Though you should not expect native
SSD-like performance while using FUSE.</p>
<h2 id="what-happens-if-i-run-out-of-memory">What happens if I run out of memory?</h2>
<p>If you run out of memory, your instance will throw an Out of Memory (OOM) error and
will be restarted.</p>
<p>Containers do not use swap memory.</p>
<h2 id="how-long-can-instances-run-for-what-happens-when-a-host-server-is-shut-down">How long can instances run for? What happens when a host server is shut down?</h2>
<p>Cloudflare does not stop a container instance after a fixed maximum runtime. The Container class sets <a href="/containers/reference/container-class/#sleepafter"><code>sleepAfter</code></a> to 10 minutes by default, and its default <a href="/containers/reference/container-class/#onactivityexpired"><code>onActivityExpired()</code></a> implementation signals the container to stop after that period without activity. You can change the duration or override the hook. Even if your hook keeps the instance running, another platform event can stop it. One of those cases is a host server restart, which happens on an irregular cadence. Cloudflare does not guarantee that any container instance will run for any set period of time.</p>
<p>When the platform is about to stop a container instance (including before a host moves work off a server), it:</p>
<ol>
<li>Sends <code>SIGTERM</code> to the main process in the container.</li>
<li>Waits up to 15 minutes for that process to exit.</li>
<li>Sends <code>SIGKILL</code> if the process is still running.</li>
</ol>
<p>Handle <code>SIGTERM</code> in your image if you need cleanup before exit. After a host stop, a new container instance may start on a different server when traffic needs it again.</p>
<p>Image updates during a deploy use the same stop sequence. Refer to <a href="/containers/configuration/rollouts/">Rollouts</a>.</p>
<h2 id="how-can-i-pass-secrets-to-my-container">How can I pass secrets to my container?</h2>
<p>You can use <a href="/workers/configuration/secrets/">Worker Secrets</a> or the <a href="/secrets-store/integrations/workers/">Secrets Store</a>
to define secrets for your Workers.</p>
<p>For implementation details, refer to <a href="/containers/examples/env-vars-and-secrets/">Environment variables and secrets</a>.</p>
<h2 id="can-i-run-docker-inside-a-container-docker-in-docker">Can I run Docker inside a container (Docker-in-Docker)?</h2>
<p>Yes. Use the <code>docker:dind-rootless</code> base image since Containers run without root privileges.</p>
<p>You must disable iptables when starting the Docker daemon because Containers do not support iptables manipulation:</p>
<pre><code class="language-dockerfile">FROM docker:dind-rootless&#10;&#10;&#35; Start dockerd with iptables disabled, then run your app&#10;ENTRYPOINT [&quot;sh&quot;, &quot;-c&quot;, &quot;dockerd-entrypoint.sh dockerd --iptables=false --ip6tables=false &amp; exec /path/to/your-app&quot;]&#10;</code></pre>
<p>If your application needs to wait for dockerd to become ready before using Docker, use an entrypoint script instead of the inline command above:</p>
<pre><code class="language-sh">&#35;!/bin/sh&#10;set -eu&#10;&#10;&#35; Wait for dockerd to be ready&#10;until docker version &gt;/dev/null 2&gt;&amp;1; do&#10;  sleep 0.2&#10;done&#10;&#10;exec /path/to/your-app&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="working-with-disabled-iptables">Working with disabled iptables</h3>
@markup("md", "content/.markup/bodies/1257.md")
</aside>
<p>For a complete working example, see the <a href="https://github.com/th0m/containers-dind">Docker-in-Docker Containers example</a>.</p>
<h2 id="how-do-i-allow-or-disallow-egress-from-my-container">How do I allow or disallow egress from my container?</h2>
<p>Refer to <a href="/containers/guides/outbound-traffic/">Handle outbound traffic</a> for how to control outbound traffic and internet access.</p>
