<p>You can run both your container and your Worker locally by simply running <a href="/workers/wrangler/commands/general/#dev"><code>npx wrangler dev</code></a> (or <code>vite dev</code> for Vite projects using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>) in your project's directory.</p>
<p>To develop Container-enabled Workers locally, you will need to first ensure that a
Docker compatible CLI tool and Engine are installed. For instance, you could use <a href="https://docs.docker.com/desktop/">Docker Desktop</a> or <a href="https://github.com/abiosoft/colima">Colima</a>.</p>
<p>When you start a dev session, your container image will be built or downloaded. If your
<a href="/workers/wrangler/configuration/#containers">Wrangler configuration</a> sets
the <code>image</code> attribute to a local path, the image will be built using the local Dockerfile.
If the <code>image</code> attribute is set to an image reference, the image will be pulled from the referenced registry, such as the Cloudflare Registry, Docker Hub, Amazon ECR, or Google Artifact Registry.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7103.md")
</aside>
<p>Container instances will be launched locally when your Worker code calls to create
a new container. Requests will then automatically be routed to the correct locally-running container.</p>
<p>When the dev session ends, all associated container instances should be stopped, but
local images are not removed, so that they can be reused in subsequent builds.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7102.md")
</aside>
<h2 id="fuse-support">FUSE support</h2>
<p>Miniflare automatically grants local containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to <code>wrangler dev</code>, the Cloudflare Vite plugin, and direct Miniflare use.</p>
<p>Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when <code>/dev/fuse</code> is available.</p>
<p>Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.</p>
<h2 id="iterating-on-container-code">Iterating on Container code</h2>
<p>When you develop with Wrangler or Vite, your Worker's code is automatically reloaded each time you save a change,
but code running within the container is not.</p>
<p>To rebuild your container with new code changes, you can hit the <code>[r]</code> key on your keyboard, which
triggers a rebuild. Container instances will then be restarted with the newly built images.</p>
<p>You may prefer to set up your own code watchers and reloading mechanisms, or mount a local directory
into the local container images to sync code changes. This can be done, but there is no built-in
mechanism for doing so, and best-practices will depend on the languages and frameworks
you are using in your container code.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="exposing-ports">Exposing Ports</h3>
<p>In production, all of your container's ports will be accessible by your Worker, so you do not need to specifically expose ports using the <a href="https://docs.docker.com/reference/dockerfile/#expose"><code>EXPOSE</code> instruction</a> in your Dockerfile.</p>
<p>But for local development you will need to declare any ports you need to access in your Dockerfile with the EXPOSE instruction; for example: <code>EXPOSE 4000</code>, if you will be accessing port 4000.</p>
<p>If you have not exposed any ports, you will see the following error in local development:</p>
<pre><code class="language-txt">The container &quot;MyContainer&quot; does not expose any ports. In your Dockerfile, please expose any ports you intend to connect to.&#10;</code></pre>
<p>And if you try to connect to any port that you have not exposed in your <code>Dockerfile</code> you will see the following error:</p>
<pre><code class="language-txt">connect(): Connection refused: container port not found. Make sure you exposed the port in your container definition.&#10;</code></pre>
<p>You may also see this while the container is starting up and no ports are available yet. You should retry until the ports become available.
This retry logic should be handled for you if you are using the <a href="https://github.com/cloudflare/containers/tree/main/src">containers package</a>.</p>
<h3 id="socket-configuration-internal-error">Socket configuration - <code>internal error</code></h3>
<p>If you see an opaque <code>internal error</code> when attempting to connect to your container, you may need to set the <code>DOCKER_HOST</code> environment variable to the socket path your container engine is listening on. Wrangler or Vite will attempt to automatically find the correct socket to use to communicate with your container engine, but if that does not work, you may have to set this environment variable to the appropriate socket path.</p>
<h3 id="ssl-errors-with-the-cloudflare-one-client-or-a-vpn">SSL errors with the Cloudflare One Client or a VPN</h3>
<p>If you are running the Cloudflare One Client or a VPN that performs TLS inspection, HTTPS requests made during the Docker build process may fail with SSL or certificate errors. This happens because the VPN intercepts HTTPS traffic and re-signs it with its own certificate authority, which Docker does not trust by default.</p>
<p>To resolve this, you can either:</p>
<ul>
<li>Disable the Cloudflare One Client or your VPN while running <code>wrangler dev</code> or <code>wrangler deploy</code>, then re-enable it afterwards.</li>
<li>Add the certificate to your Docker build context. The Cloudflare One Client exposes its certificate via the <code>NODE_EXTRA_CA_CERTS</code> and <code>SSL_CERT_FILE</code> environment variables on your host machine. You can pass the certificate into your Docker build as an environment variable, so that it is available during the build without being baked into the final image.</li>
</ul>
<pre><code class="language-dockerfile">RUN if [ -n &quot;$SSL_CERT_FILE&quot; ]; then \&#10;    cp &quot;$SSL_CERT_FILE&quot; /usr/local/share/ca-certificates/Custom_CA.crt &amp;&amp; \&#10;    update-ca-certificates; \&#10;    fi&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7101.md")
</aside>
<p>Wrangler invokes Docker automatically when you run <code>wrangler dev</code> or <code>wrangler deploy</code>, so if you need to pass build secrets, you will need to build and push the image manually using <code>wrangler containers push</code>.</p>
