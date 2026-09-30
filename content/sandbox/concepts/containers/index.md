<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13575.md")
</aside>
<p>Each sandbox runs in an isolated Linux container with Python, Node.js, and common development tools pre-installed. For a complete list of pre-installed software and how to customize the container image, see <a href="/sandbox/configuration/dockerfile/">Dockerfile reference</a>.</p>
<h2 id="runtime-software-installation">Runtime software installation</h2>
<p>Install additional software at runtime using standard package managers:</p>
<pre><code class="language-bash">&#35; Python packages&#10;pip install scikit-learn tensorflow&#10;&#10;&#35; Node.js packages&#10;npm install express&#10;&#10;&#35; System packages (requires apt-get update first)&#10;apt-get update &amp;&amp; apt-get install -y redis-server&#10;</code></pre>
<h2 id="filesystem">Filesystem</h2>
<p>The container provides a standard Linux filesystem. You can read and write anywhere you have permissions.</p>
<p><strong>Standard directories</strong>:</p>
<ul>
<li><code>/workspace</code> - Default working directory for user code</li>
<li><code>/tmp</code> - Temporary files</li>
<li><code>/home</code> - User home directory</li>
<li><code>/usr/bin</code>, <code>/usr/local/bin</code> - Executable binaries</li>
</ul>
<p><strong>Example</strong>:</p>
<pre><code class="language-typescript">await sandbox.writeFile(&#x27;/workspace/app.py&#x27;, &#x27;print(&quot;Hello&quot;)&#x27;);&#10;await sandbox.writeFile(&#x27;/tmp/cache.json&#x27;, &#x27;{}&#x27;);&#10;await sandbox.exec(&#x27;ls -la /workspace&#x27;);&#10;</code></pre>
<h2 id="process-management">Process management</h2>
<p>Processes run as you'd expect in a regular Linux environment.</p>
<p><strong>Foreground processes</strong> (<code>exec()</code>):</p>
<pre><code class="language-typescript">const result = await sandbox.exec(&#x27;npm test&#x27;);&#10;// Waits for completion, returns output&#10;</code></pre>
<p><strong>Background processes</strong> (<code>startProcess()</code>):</p>
<pre><code class="language-typescript">const process = await sandbox.startProcess(&#x27;node server.js&#x27;);&#10;// Returns immediately, process runs in background&#10;</code></pre>
<h2 id="network-capabilities">Network capabilities</h2>
<p><strong>Outbound connections</strong> work:</p>
<pre><code class="language-bash">curl https://api.example.com/data&#10;pip install requests&#10;npm install express&#10;</code></pre>
<p><strong>Inbound connections</strong> require port exposure:</p>
<pre><code class="language-typescript">const { hostname } = new URL(request.url);&#10;await sandbox.startProcess(&#x27;python -m http.server 8000&#x27;);&#10;const exposed = await sandbox.exposePort(8000, { hostname });&#10;console.log(exposed.url); // Public URL&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="local-development">Local development</h3>
@markup("md", "content/.markup/bodies/13574.md")
</aside>
<p><strong>Localhost</strong> works within sandbox:</p>
<pre><code class="language-bash">redis-server &amp;      # Start server&#10;redis-cli ping      # Connect locally&#10;</code></pre>
<h2 id="security">Security</h2>
<p><strong>Between sandboxes</strong> (isolated):</p>
<ul>
<li>Each sandbox is a separate container</li>
<li>Filesystem, memory and network are all isolated</li>
</ul>
<p><strong>Within sandbox</strong> (shared):</p>
<ul>
<li>All processes see the same files</li>
<li>Processes can communicate with each other</li>
<li>Environment variables are session-scoped</li>
</ul>
<p>To run untrusted code, use separate sandboxes per user:</p>
<pre><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, `user-${userId}`);&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<p><strong>Cannot</strong>:</p>
<ul>
<li>Load kernel modules or access host hardware</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a> - Deploy and keep package and image aligned</li>
<li><a href="/containers/guides/deploy/">Deploy Containers</a> - Containers deploy path</li>
<li><a href="/sandbox/concepts/architecture/">Architecture</a> - How containers fit in the system</li>
<li><a href="/sandbox/concepts/security/">Security model</a> - Container isolation details</li>
<li><a href="/sandbox/concepts/sandboxes/">Sandbox lifecycle</a> - Container lifecycle management</li>
<li><a href="/sandbox/guides/docker-in-docker/">Docker-in-Docker</a> - Run Docker containers inside a Sandbox</li>
</ul>
