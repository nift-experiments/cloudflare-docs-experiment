<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 13, 2026</time><h2 id="post-title">Containers and Sandboxes are now generally available</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Cloudflare <a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> are now generally available.</p>
<p>Containers let you run more workloads on the Workers platform, including resource-intensive applications, different languages, and CLI tools that need full Linux environments.</p>
<p>Since the initial launch of Containers, there have been significant improvements to Containers' performance, stability, and feature set. Some highlights include:</p>
<ul>
<li><a href="/changelog/post/2026-02-25-higher-container-resource-limits/">Higher limits</a> allow you to run thousands of containers concurrently.</li>
<li><a href="/changelog/post/2025-11-21-new-cpu-pricing/">Active-CPU pricing</a> means that you only pay for used CPU cycles.</li>
<li><a href="/changelog/post/2026-03-26-outbound-workers/">Easy connections to Workers and other bindings</a> via hostnames help you extend your Containers with additional functionality.</li>
<li><a href="/changelog/post/2026-03-24-docker-hub-images/">Docker Hub support</a> makes it easy to use your existing images and registries.</li>
<li><a href="/changelog/post/2026-03-12-ssh-support/">SSH support</a> helps you access and debug issues in live containers.</li>
</ul>
<p>The <a href="/sandbox/">Sandbox SDK</a> provides isolated environments for running untrusted code securely, with a simple TypeScript API for executing commands, managing files, and exposing services. This makes it easier to secure and manage your agents at scale. Some additions since launch include:</p>
<ul>
<li><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Live preview URLs</a> so agents can run long-lived services and verify in-flight changes.</li>
<li><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Persistent code interpreters</a> for Python, JavaScript, and TypeScript, with rich structured outputs.</li>
<li><a href="/changelog/post/2026-02-09-pty-terminal-support/">Interactive PTY terminals</a> for real browser-based terminal access with multiple isolated shells per sandbox.</li>
<li><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore APIs</a> to snapshot a workspace and quickly restore an agent's coding session without repeating expensive setup steps.</li>
<li><a href="/changelog/post/2026-03-03-sandbox-watch-file-events/">Real-time filesystem watching</a> so apps and agents can react immediately to file changes inside a sandbox.</li>
</ul>
<p>For more information, refer to <a href="/containers/">Containers</a> and <a href="/sandbox/">Sandbox SDK</a> documentation.</p>
</div></article></div>
