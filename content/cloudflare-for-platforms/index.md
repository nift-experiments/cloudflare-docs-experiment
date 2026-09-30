<div class="nb-description">
@markup("md", "content/.markup/bodies/1327.md")
</div>
<p>Cloudflare for Platforms is used by leading platforms big and small to:</p>
<ul>
<li>Build application development platforms tailored to specific domains, like ecommerce storefronts or mobile apps</li>
<li>Power AI coding platforms that let anyone build and deploy software</li>
<li>Customize product behavior by allowing any user to write a short code snippet</li>
<li>Offer every customer their own isolated database</li>
<li>Provide each customer with their own subdomain</li>
</ul>
<hr />
<h2 id="deploy-your-own-platform">Deploy your own platform</h2>
<p>Get a working platform running in minutes. Choose a template based on what you are building:</p>
<h3 id="platform-starter-kit">Platform Starter Kit</h3>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/worker-publisher-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>An example of a platform where users can deploy code at scale. Each snippet becomes its own isolated Worker, served at <code>example.com/{app-name}</code>. Deploying this starter kit automatically configures Workers for Platforms with routing handled for you.</p>
<p><a class="nb-link-button" href="https://worker-publisher-template.templates.workers.dev/">View demo</a>
<a class="nb-link-button" href="https://github.com/cloudflare/templates/tree/main/worker-publisher-template">View on GitHub</a></p>
<h3 id="ai-vibe-coding-platform">AI vibe coding platform</h3>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/vibesdk"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>Build an <a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">AI vibe coding platform</a> where users describe what they want and AI generates and deploys working applications. Best for: AI-powered app builders, code generation tools, or internal platforms that empower teams to build applications &amp; prototypes.</p>
<p><a href="https://github.com/cloudflare/vibesdk">VibeSDK</a> handles AI code generation, code execution in secure sandboxes, live previews, and deployment at scale.</p>
<p><a class="nb-link-button" href="https://build.cloudflare.dev/">View demo</a>
<a class="nb-link-button" href="https://github.com/cloudflare/vibesdk">View on GitHub</a></p>
<hr />
<h2 id="features">Features</h2>
<ul>
<li><strong>Isolation and multitenancy</strong> — Each of your customers runs code in their own Worker, a <a href="/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/">secure and isolated sandbox</a>.</li>
<li><strong>Programmable routing, ingress, egress, and limits</strong> — You write code that dispatches requests to your customers' code, and can control <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">ingress</a>, <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">egress</a>, and set <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/">per-customer limits</a>.</li>
<li><strong>Databases and storage</strong> — You can provide <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">databases, object storage, and more</a> to your customers as APIs they can call directly, without API tokens, keys, or external dependencies.</li>
<li><strong>Custom domains and subdomains</strong> — You <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">call an API</a> to create custom subdomains or configure custom domains for each of your customers.</li>
</ul>
<p>To learn how these components work together, refer to <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/">How Workers for Platforms works</a>.</p>
