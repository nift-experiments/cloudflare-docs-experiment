<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17361.md")
</aside>
<p><strong>Miniflare</strong> is a simulator for developing and testing
<a href="https://workers.cloudflare.com/"><strong>Cloudflare Workers</strong></a>. It's written in
TypeScript, and runs your code in a sandbox implementing Workers' runtime APIs.</p>
<ul>
<li>🎉 <strong>Fun:</strong> develop Workers easily with detailed logging, file watching and
pretty error pages supporting source maps.</li>
<li>🔋 <strong>Full-featured:</strong> supports most Workers features, including KV, Durable
Objects, WebSockets, modules and more.</li>
<li>⚡ <strong>Fully-local:</strong> test and develop Workers without an Internet connection.
Reload code on change quickly.</li>
</ul>
<p><a class="nb-link-button" href="/workers/testing/miniflare/get-started">Get Started</a>
<a class="nb-link-button" href="https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare">GitHub</a>
<a class="nb-link-button" href="https://npmjs.com/package/miniflare">NPM</a></p>
<hr />
<p>These docs primarily cover Miniflare specific things. For more information on
runtime APIs, refer to the
<a href="/workers">Cloudflare Workers docs</a>.</p>
<p>If you find something that doesn't behave as it does in the production Workers
environment (and this difference isn't documented), or something's wrong in
these docs, please
<a href="https://github.com/cloudflare/workers-sdk/issues/new/choose">open a GitHub issue</a>.</p>
<ul class="directory-listing"><li><a href="/workers/testing/miniflare/get-started/">Get Started</a><p>Install and configure the Miniflare API to dispatch events and test Cloudflare Workers locally.</p></li><li><a href="/workers/testing/miniflare/writing-tests/">Writing tests</a><p>Write integration tests against Workers using Miniflare.</p></li><li><a href="/workers/testing/miniflare/core/">Core</a><p>Core Miniflare features for testing Cloudflare Workers, including fetch events and compatibility settings.</p></li><li><a href="/workers/testing/miniflare/developing/">Developing</a><p>Development tools for Miniflare, including debugger support and live reload for Cloudflare Workers.</p></li><li><a href="/workers/testing/miniflare/migrations/">Migrations</a><p>Review migration guides for specific versions of Miniflare.</p></li><li><a href="/workers/testing/miniflare/storage/">Storage</a><p>Configure and manage local storage simulators in Miniflare for Workers bindings like KV, R2, and D1.</p></li></ul>
