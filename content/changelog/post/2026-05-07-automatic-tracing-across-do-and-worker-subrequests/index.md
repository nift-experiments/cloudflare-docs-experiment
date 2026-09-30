<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 7, 2026</time><h2 id="post-title">Automatic tracing across Durable Object and Worker subrequests</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now get a single unified trace across Worker-to-Worker subrequests, with trace context propagating automatically. Previously, <a href="/workers/observability/traces/">automatic tracing</a> produced disconnected traces when a Worker called another Worker through a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> or <a href="/durable-objects/">Durable Object</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-04-28-worker-to-worker-context-prop.png" alt="Unified trace showing nested spans across a Durable Object subrequest and a service binding call" /></p>
<p>This means you can:</p>
<ul>
<li>Follow a request through your entire Worker architecture in one trace view</li>
<li>See service binding and Durable Object calls as nested child spans instead of separate traces</li>
<li>Debug cross-Worker request flows in the Cloudflare dashboard or in an external observability platform via <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry</a></li>
</ul>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for traces to be recorded. Checkout <a href="/workers/observability/traces/">Workers tracing</a> to get started.</p>
<p>Up next, we are working on external trace context propagation using <a href="https://www.w3.org/TR/trace-context/">W3C Trace Context standards</a>, which will allow traces from your Workers to link with traces from services outside of Cloudflare.</p>
</div></article></div>
