---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/
  description: A practical example of how these services come together in a real fullstack application architecture.
  full_title: Fullstack applications · Cloudflare Reference Architecture docs
  head_html: <title>Fullstack applications · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="A practical example of how these services come together in a real fullstack application architecture."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/index.md"><meta property="og:title" content="Fullstack applications · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A practical example of how these services come together in a real fullstack application architecture."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="AI Gateway,Agents,API Shield,Bots,Containers,D1,DDoS Protection,Durable Objects,Cloudflare Images,KV,Logs,Pages,Pipelines,Queues,R2,Realtime,SSL/TLS,Stream,Vectorize,WAF,Workflows,Workers,Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/#page","headline":"Fullstack applications \u00b7 Cloudflare Reference Architecture docs","description":"A practical example of how these services come together in a real fullstack application architecture.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/serverless/fullstack-application/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/serverless/fullstack-application/
  schema: 1
---
<p>Fullstack web applications combine frontend and backend technologies to deliver complete, dynamic user experiences. These applications rely on a broad technology stack covering user interfaces, backend services, databases, integrations, and increasingly, AI-driven features to function seamlessly and scale reliably.</p>
<p>On the frontend, developers typically use HTML, CSS, and JavaScript, often alongside frameworks like React, Next.js, or Angular. These tools provide the structure and interactivity needed for modern user interfaces, helping manage state, render dynamic content, personalize experiences, and optimize performance across devices.</p>
<p>On the backend, server-side code handles tasks like processing requests, running business logic, authenticating users, integrating AI models, and interacting with databases. Developers build these services using languages like JavaScript, Python, or Java, supported by frameworks that simplify routing, middleware, and API creation.</p>
<p>Databases are critical in the stack, storing and retrieving application data. Relational databases like MySQL, PostgreSQL, and SQLite manage structured data and enforce data integrity, while NoSQL options like MongoDB or Cassandra offer flexibility for handling unstructured or large-scale datasets.</p>
<p>Modern fullstack development increasingly incorporates external services, APIs, pre-built components, and AI capabilities. This approach reduces the need to create complex features from scratch, such as content moderation, personalized recommendations, and semantic search. As a result, development teams can build applications more quickly and efficiently.</p>
<p>Cloudflare’s Developer Platform combines all these capabilities into a unified, globally distributed environment, offering developers everything they need to build, deploy, and scale modern fullstack applications with minimal operational overhead.</p>
<p><img src="/assets/upstream/images/reference-architecture/fullstack-app/developer-platform.svg" alt="Figure 1: Cloudflare Developer Platform" title="Figure 1: Cloudflare Developer Platform" /></p>
<p>Cloudflare’s platform doesn’t just offer individual services. Rather, it offers a <strong>composable ecosystem</strong>, enabling teams to build powerful applications quickly, scale seamlessly, and innovate faster without the overhead of managing infrastructure.</p>
<h2 id="fullstack-application-diagram">Fullstack application diagram</h2>
<p>In this section, we’ll present a practical example of how these services come together in a real fullstack application architecture.</p>
<p><img src="/assets/upstream/images/reference-architecture/fullstack-app/fullstack-app-base.svg" alt="Figure 2: Fullstack application" title="Figure 2: Fullstack application" /></p>
<h3 id="1-client"><ol>
<li>Client</li>
</ol></h3>
<p>Sends requests to the server. This could be through a desktop or mobile browser, or native or mobile app.</p>
<h3 id="2-security"><ol start="2">
<li>Security</li>
</ol></h3>
<p>Process incoming requests to ensure the security of an application. This includes encryption of traffic using <a href="/ssl/">SSL/TLS</a>, offering <a href="/ddos-protection/">DDOS protection</a>, filtering malicious traffic through a <a href="/waf/">web application firewall (WAF)</a>, <a href="/bots/">mitigations against automated bots</a>, and <a href="/api-shield/">API Shield</a> to identify and address your API vulnerabilities. Depending on the configuration, requests can be blocked, logged, or allowed based on a diverse set of parameters. Sensible fully managed and default configurations can be used to reduce attack surfaces with little to no overhead.</p>
<h3 id="3-performance"><ol start="3">
<li>Performance</li>
</ol></h3>
<p>Serve static requests from <a href="/cache/">global cache (CDN)</a>. This reduces latency and lowers resource utilization, as the requests are being served from cache instead of requiring a request to storage &amp; media services or compute services. Take advantage of <a href="/argo-smart-routing/">Argo Smart Routing</a> to route requests across the most efficient network path, avoiding congestion.</p>
<h3 id="4-compute"><ol start="4">
<li>Compute</li>
</ol></h3>
<p>Process dynamic requests using serverless compute with <a href="/workers/">Workers</a>. This could include authentication, routing, middleware, database interactions, and serving APIs. Moreover, <a href="/workers/static-assets/">Workers Assets</a> can be used to serve client-side or server-side rendering web frameworks such as React, Next.js, or Angular. Utilize <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> to allow users to deploy custom code on your platform or enable them to deploy their own code directly. For stateful workloads, <a href="/durable-objects/">Durable Objects</a> provide low-latency, stateful compute by running logic close to where the object's data is stored, enabling coordination, persistence, and real-time communication at the edge.</p>
<p>For workloads that require the flexibility of traditional containerization, <a href="/containers/">Containers</a> allows you to run existing Docker-compatible applications on Cloudflare’s global network. Containers is designed for applications needing more resources than a standard Worker.</p>
<h3 id="5-data-storage"><ol start="5">
<li>Data &amp; Storage</li>
</ol></h3>
<p>Introduce state to applications by persisting and retrieving data. This includes <a href="/r2/">R2</a> for object storage, <a href="/d1/">D1</a> for relational data, <a href="/kv/">KV</a> for data with high read requirements and <a href="/durable-objects/">Durable Objects</a> for strongly consistent data storage. The <a href="/workers/platform/storage-options/">storage options guide</a> can help to assess which storage option is the most suitable for a given use case.</p>
<h3 id="6-realtime-content-media"><ol start="6">
<li>Realtime content &amp; Media</li>
</ol></h3>
<p>Build real-time serverless video, audio, and data applications with <a href="/realtime/">Realtime</a>. Serve optimized images from <a href="/images/">Images</a> and on-demand videos as well as live streams from <a href="/stream/">Stream</a>.</p>
<h3 id="7-ai"><ol start="7">
<li>AI</li>
</ol></h3>
<p>With <a href="/workers-ai/">Workers AI</a>, developers can run popular open-source models for tasks like text generation, image analysis, and content moderation powered by serverless GPUs. <a href="/vectorize/">Vectorize</a> is a globally distributed vector database for similarity search, personalization, and recommendation features. <a href="/agents/">Agents</a> further extend AI capabilities - Cloudflare provides the Agents SDK that lets you build and deploy AI-powered agents that can perform tasks, interact in real time, call models, manage state, run workflows, query data, and integrate human-in-the-loop actions.</p>
<h3 id="8-orchestration-abstraction"><ol start="8">
<li>Orchestration &amp; Abstraction</li>
</ol></h3>
<p><a href="/queues/">Queues</a> enable durable, asynchronous messaging to decouple services and handle traffic spikes. <a href="/workflows/">Workflows</a> orchestrate complex processes across APIs, services, and human approvals, abstracting away infrastructure and state management. <a href="/pipelines/">Pipelines</a> let you ingest high volumes of real time data, without managing any infrastructure.</p>
<h3 id="9-cloudflare-observability"><ol start="9">
<li>Cloudflare Observability</li>
</ol></h3>
<p>Send logs from all services with <a href="/logs/logpush/">Logpush</a>, gather insights with <a href="/workers/observability/logs/">Workers Logs</a> directly in the Cloudflare dashboard, collect custom metrics from Workers using <a href="/analytics/analytics-engine/">Workers Analytics Engine</a>, or observe and control AI applications with <a href="/ai-gateway/">AI Gateway</a>.</p>
<h3 id="10-external-logs-analytics"><ol start="10">
<li>External Logs &amp; Analytics</li>
</ol></h3>
<p>Integrate Cloudflare's observability solutions with your existing third-party solutions. Logpush supports many <a href="/logs/logpush/logpush-job/enable-destinations/">destinations</a> to push logs to for storage and further analysis. Also, Cloudflare analytics can be <a href="/analytics/analytics-integrations/">integrated with analytics solutions</a>. The <a href="/analytics/graphql-api/">GraphQL Analytics API</a> allows for flexible queries and integrations.</p>
<h3 id="11-tooling-provisioning"><ol start="11">
<li>Tooling &amp; Provisioning</li>
</ol></h3>
<p>Define and manage resources and configuration using third-party tools and frameworks such as <a href="/terraform/">Terraform</a> and <a href="/pulumi/">Pulumi</a>, Cloudflare's Developer Platform command-line interface (CLI) <a href="/workers/wrangler/">Wrangler</a>, or the <a href="/api/">Cloudflare API</a>. All of these tools can be used either for manual provisioning, or automated as part of CI/CD pipelines.</p>
<h3 id="12-external-service-integrations"><ol start="12">
<li>External Service Integrations</li>
</ol></h3>
<p>Cloudflare’s Developer Platform is built for seamless <a href="/workers/configuration/integrations/">integration with external services</a>. Whether connecting to third-party APIs, databases, SaaS platforms, or cloud providers, developers can easily make outbound requests from Workers, trigger workflows based on external events, and securely exchange data across systems.</p>
