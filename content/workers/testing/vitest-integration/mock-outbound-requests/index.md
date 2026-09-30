<p>Use <a href="https://github.com/mswjs/cloudflare"><code>@msw/cloudflare</code></a> to mock outbound HTTP and WebSocket requests with <code>@cloudflare/vitest-plugin</code>. The integration supports unit tests that call your Worker's exported handler and integration tests that call <code>exports.default.fetch()</code>.</p>
<h2 id="install-dependencies">Install dependencies</h2>
<p>Install Mock Service Worker (MSW) version 2.14 or later and the Cloudflare integration:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i msw@^2.14.0 @msw/cloudflare</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i msw@^2.14.0 @msw/cloudflare" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add msw@^2.14.0 @msw/cloudflare</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add msw@^2.14.0 @msw/cloudflare" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add msw@^2.14.0 @msw/cloudflare</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add msw@^2.14.0 @msw/cloudflare" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add msw@^2.14.0 @msw/cloudflare</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add msw@^2.14.0 @msw/cloudflare" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="create-a-network-mock">Create a network mock</h2>
<p>Create a shared network mock for your tests:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17323.md")
</div>
<p>In a Vitest setup file, start the mock before tests, reset handlers after each test, and stop it after tests finish:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17324.md")
</div>
<p>Add the setup file to the <code>setupFiles</code> array in your Vitest configuration.</p>
<h2 id="mock-an-http-request">Mock an HTTP request</h2>
<p>Use <code>network.use()</code> and MSW request handlers to return a response for an outbound request. This example tests a Worker that requests a greeting from an external API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17325.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17326.md")
</div>
<h2 id="mock-an-outbound-websocket">Mock an outbound WebSocket</h2>
<p>Use MSW's <code>ws.link()</code> API to mock a WebSocket connection created by your Worker. The <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/request-mocking">request-mocking fixture</a> includes HTTP, <code>exports.default.fetch()</code>, and WebSocket examples.</p>
