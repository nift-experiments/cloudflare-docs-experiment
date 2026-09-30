<h2 id="introduction">Introduction</h2>
<p>An AI-powered coding platform (sometimes referred to as a <a href="https://www.cloudflare.com/learning/ai/ai-vibe-coding/">“vibe coding”</a> platform) enables users to build applications by describing what they want in natural language. These platforms allow anyone to build applications by handling everything from code generation, testing and debugging, to project deployment.</p>
<p>Building the infrastructure for such a platform introduces a unique set of challenges. AI-generated code is inherently untrusted and must be executed in a secure, sandbox to prevent abuse and ensure isolation between users. To support rapid, conversational development, the platform must provide near-instantaneous feedback loops with live previews and real-time debugging. Finally, the platform needs a way to deploy and host the thousands or millions of applications its users will create, without running up the costs of traditional server infrastructure.</p>
<p>Cloudflare has all the components required to build one of these platforms — from middleware that connects to AI models, to secure sandboxes for code execution, and a serverless deployment platform that scales to millions of applications.</p>
<p><img src="/assets/upstream/images/reference-architecture/ai-vibe-coding/cf-vibe-plat.svg" alt="Figure 1: AI Vibe Coding Platform on Cloudflare" /></p>
<p>To get started with a reference implementation of an AI vibe coding platform immediately, deploy this <a href="https://github.com/cloudflare/vibesdk">starter template</a> to your Cloudflare account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/vibesdk"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare Workers" /></a></p>
<h2 id="core-architecture-components">Core Architecture Components</h2>
<p><img src="/assets/upstream/images/reference-architecture/ai-vibe-coding/vibe-hosting-overview.svg" alt="Figure 2: Vibe Hosting Overview" /></p>
<p>To build an AI-powered coding platform, you will need these key components:</p>
<ul>
<li><strong>AI for Code Generation:</strong> Integrate with AI models to interpret user prompts and automatically generate code.</li>
<li><strong>Secure Execution Sandbox:</strong> Provide a secure, isolated environment where users can instantly run and test untrusted, AI-generated code.</li>
<li><strong>Scalable Application Deployment :</strong> Deploy and host AI-generated applications at scale.</li>
<li><strong>Analytics &amp; Observability:</strong> Collect logs and metrics to monitor AI usage, application performance, and platform costs.</li>
</ul>
<h2 id="ai-integration-and-code-generation">AI Integration and Code generation</h2>
<h4 id="connecting-to-ai-providers-for-code-generation">Connecting to AI Providers for Code Generation</h4>
<p>The first step is processing a user's natural language prompt and securely routing it to an AI model to generate code.</p>
<p>When using various AI providers, you need visibility into costs, the ability to cache responses to reduce expenses, and failover capabilities to ensure reliability. <a href="/ai-gateway/">AI Gateway</a> acts as a unified control point between your platform and AI providers to deliver these capabilities, enabling:</p>
<ul>
<li>A <a href="/ai-gateway/usage/chat-completion/">unified access point</a> to route requests across LLM providers, allowing you to use <a href="/workers-ai/models/">models</a> from a range of providers (OpenAI, Anthropic, Google, and others)</li>
<li><a href="/ai-gateway/features/caching/">Caching</a> for popular responses, so when someone asks to &quot;build a todo list app&quot;, the gateway can serve a cached response instead of going to the provider (saving inference costs)</li>
<li><a href="/ai-gateway/observability/analytics/">Observability</a> into the requests, tokens used, and response times across all providers in one place</li>
<li><a href="/ai-gateway/observability/costs/">Cost tracking</a> across AI providers</li>
</ul>
<h4 id="making-your-ai-better-at-building-on-cloudflare">Making your AI better at building on Cloudflare</h4>
<p>If you’re building an AI code generator and want it to be more knowledgeable about how to best build applications on Cloudflare, there are two tools we recommend using:</p>
<ul>
<li><strong><a href="/workers/get-started/prompting/#build-workers-using-a-prompt">Cloudflare Workers Prompt</a>:</strong> Structured prompt with examples that teach AI models about Cloudflare's APIs, configuration patterns, and best practices. Include these in your AI system for higher quality code output.</li>
<li><strong><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/docs-ai-search">Cloudflare’s Documentation MCP server</a>:</strong> If your AI tool supports <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a>, connect it to Cloudflare's documentation MCP server to get up-to-date knowledge about Cloudflare’s platform.</li>
</ul>
<h2 id="development-environment-for-executing-ai-generated-code">Development environment for executing AI-generated code</h2>
<p>Both <a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> provide secure, isolated environments for executing untrusted AI-generated code. They offer:</p>
<ul>
<li><strong>Strong isolation and sandboxing controls</strong> to prevent malicious or buggy code from affecting other instances</li>
<li><strong>Fast startup times</strong> to enable rapid iteration cycles with real-time feedback</li>
<li><strong>Real-time output streaming</strong> of logs and results for live progress updates and debugging</li>
<li><strong>Preview URLs</strong> to allow users to test applications during development</li>
<li><strong>Global edge deployment</strong> on Cloudflare's network for low-latency execution worldwide</li>
</ul>
<p><strong>Sandboxes provide a fully-managed solution</strong> that works out-of-the-box, with <a href="/sandbox/api/">pre-built APIs</a> for code execution, output formatting, and developer tools, making them ideal for most AI code execution use cases.</p>
<p><img src="/assets/upstream/images/reference-architecture/ai-vibe-coding/ai-platform-sandbox.svg" alt="Figure 3: Vibe Code Development - Sandbox SDK" /></p>
<p><strong>Containers offer complete runtime control</strong> through custom Docker images, allowing you to run any language or framework with up to 4GB RAM and dedicated vCPU and are best when you need custom runtimes or resource-intensive workloads.</p>
<p><img src="/assets/upstream/images/reference-architecture/ai-vibe-coding/BYO-sandbox.svg" alt="Figure 4: Isolated Containers" /></p>
<h2 id="deploying-applications-to-production">Deploying applications to production</h2>
<p>When building an AI-powered coding platform, you need to be able to deploy and host the thousands to millions of applications that the platform will generate.</p>
<p><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> provides this infrastructure by enabling you to deploy unlimited applications, with each application running in its own isolated Worker instance, preventing one application from impacting others.</p>
<p><strong>With Workers for Platforms, you get:</strong></p>
<ul>
<li><strong>Isolation and multitenancy</strong> — every application runs in its own dedicated Worker, a secure and isolated sandbox environment</li>
<li><strong>Egress control and usage limits</strong> — Configure firewall policies for all outgoing requests through an <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">outbound worker</a> and <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/">custom usage limits</a> to prevent abuse</li>
<li><strong>Dedicated resources per project:</strong> Attach a KV store or database to each application, enabling more powerful functionality while ensuring <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">resources</a> are only accessible by the application they’re attached to.</li>
<li><strong>Logging &amp; Observability</strong> across the platform to gather insights, monitor performance, and troubleshoot issues across applications</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/ai-vibe-coding/vibe-hosting-analytics.svg" alt="Figure 5: Complete Vibe Coding Platform" /></p>
<h2 id="conclusion">Conclusion</h2>
<p>Cloudflare provides a complete set of services needed for building AI-powered platforms that need to run, test, and deploy untrusted code at scale.</p>
<p>Cloudflare has a template AI vibe coding platform that you can deploy, so you can get started with a complete example that handles everything from code generation, sandboxes development with a preview environment, and integration with Workers for Platforms for deploying and hosting the applications at scale.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/vibesdk"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare Workers" /></a></p>
