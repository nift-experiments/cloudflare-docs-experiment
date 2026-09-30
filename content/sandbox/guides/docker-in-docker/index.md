<p>This guide shows you how to run Docker inside a Sandbox, enabling you to build and run container images from within a secure sandbox.</p>
<h2 id="when-to-use-docker-in-docker">When to use Docker-in-Docker</h2>
<p>Use Docker-in-Docker when you need to:</p>
<ul>
<li><strong>Develop containerized applications</strong> - Run <code>docker build</code> to create images from Dockerfiles</li>
<li><strong>Run Docker as part of CI/CD</strong> - Respond to code changes and build and push images using Cloudflare Containers</li>
<li><strong>Run arbitrary container images</strong> - Start containers from an end-user provided image</li>
</ul>
<h2 id="create-a-docker-enabled-image">Create a Docker-enabled image</h2>
<p>Cloudflare Containers run without root privileges, so you must use the rootless Docker image. Create a custom Dockerfile that combines the sandbox binary with Docker:</p>
<pre><code class="language-dockerfile">FROM docker:dind-rootless&#10;USER root&#10;&#10;&#35; Use the musl build so it runs on Alpine-based docker:dind-rootless&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.4-musl /container-server/sandbox /sandbox&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.4-musl /usr/lib/libstdc++.so.6 /usr/lib/libstdc++.so.6&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.4-musl /usr/lib/libgcc_s.so.1 /usr/lib/libgcc_s.so.1&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.4-musl /bin/bash /bin/bash&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.4-musl /usr/lib/libreadline.so.8 /usr/lib/libreadline.so.8&#10;COPY --from=docker.io/cloudflare/sandbox:0.7.4-musl /usr/lib/libreadline.so.8.2 /usr/lib/libreadline.so.8.2&#10;&#10;&#35; Create startup script that starts dockerd with&#10;&#35; iptables disabled, waits for readiness, then keeps running&#10;RUN printf &#x27;#!/bin/sh\n\&#10;  set -eu\n\&#10;  dockerd-entrypoint.sh dockerd --iptables=false --ip6tables=false &amp;\n\&#10;  until docker version &gt;/dev/null 2&gt;&amp;1; do sleep 0.2; done\n\&#10;  echo &quot;Docker is ready&quot;\n\&#10;  wait\n&#x27; &gt; /home/rootless/boot-docker-for-dind.sh &amp;&amp; chmod +x /home/rootless/boot-docker-for-dind.sh&#10;&#10;ENTRYPOINT [&quot;/sandbox&quot;]&#10;CMD [&quot;/home/rootless/boot-docker-for-dind.sh&quot;]&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="working-with-disabled-iptables">Working with disabled iptables</h3>
@markup("md", "content/.markup/bodies/13471.md")
</aside>
<h2 id="use-docker-in-your-sandbox">Use Docker in your sandbox</h2>
<p>Once deployed, you can run Docker commands through the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13472.md")
</div>
<h2 id="limitations">Limitations</h2>
<p>Docker-in-Docker in Cloudflare Containers has the following limitations:</p>
<ul>
<li><strong>No iptables</strong> - Network isolation features that rely on iptables are not available</li>
<li><strong>Rootless mode only</strong> - You cannot use privileged containers or features requiring root</li>
<li><strong>Ephemeral storage</strong> - Built images and containers are lost when the sandbox sleeps. You must persist them manually.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/configuration/dockerfile/">Dockerfile reference</a> - Customize your sandbox image</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands</a> - Run commands in the sandbox</li>
<li><a href="/sandbox/guides/background-processes/">Background processes</a> - Manage long-running processes</li>
</ul>
