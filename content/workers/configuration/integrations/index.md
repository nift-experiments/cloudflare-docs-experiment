<p>One of the key features of Cloudflare Workers is the ability to integrate with other services and products. In this document, we will explain the types of integrations available with Cloudflare Workers and provide step-by-step instructions for using them.</p>
<h2 id="types-of-integrations">Types of integrations</h2>
<p>Cloudflare Workers offers several types of integrations, including:</p>
<ul>
<li><a href="/workers/databases/">Databases</a>: Cloudflare Workers can be integrated with a variety of databases, including SQL and NoSQL databases. This allows you to store and retrieve data from your databases directly from your Cloudflare Workers code.</li>
<li><a href="/workers/configuration/integrations/apis/">APIs</a>: Cloudflare Workers can be used to integrate with external APIs, allowing you to access and use the data and functionality exposed by those APIs in your own code.</li>
<li><a href="/workers/configuration/integrations/external-services/">Third-party services</a>: Cloudflare Workers can be used to integrate with a wide range of third-party services, such as payment gateways, authentication providers, and more. This makes it possible to use these services in your Cloudflare Workers code.</li>
</ul>
<h2 id="how-to-use-integrations">How to use integrations</h2>
<p>To use any of the available integrations:</p>
<ul>
<li>Determine which integration you want to use and make sure you have the necessary accounts and credentials for it.</li>
<li>In your Cloudflare Workers code, import the necessary libraries or modules for the integration.</li>
<li>Use the provided APIs and functions to connect to the integration and access its data or functionality.</li>
<li>Store necessary secrets and keys using secrets via <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret put &lt;KEY&gt;</code></a>.</li>
</ul>
<h2 id="tips-and-best-practices">Tips and best practices</h2>
<p>To help you get the most out of using integrations with Cloudflare Workers:</p>
<ul>
<li>Secure your integrations and protect sensitive data. Ensure you use secure authentication and authorization where possible, and ensure the validity of libraries you import.</li>
<li>Use <a href="/workers/reference/how-the-cache-works">caching</a> to improve performance and reduce the load on an external service.</li>
<li>Split your Workers into service-oriented architecture using <a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> to make your application more modular, easier to maintain, and more performant.</li>
<li>Use <a href="/workers/configuration/routing/custom-domains/">Custom Domains</a> when communicating with external APIs and services, which create a DNS record on your behalf and treat your Worker as an application instead of a proxy.</li>
</ul>
