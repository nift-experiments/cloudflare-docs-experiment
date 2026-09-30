<p>For most users, Cloudflare recommends using the Workers Vitest integration for unit testing Workers and <a href="/pages/functions/">Pages Functions</a> projects. <a href="https://vitest.dev/">Vitest</a> is a popular JavaScript testing framework featuring a fast watch mode, Jest compatibility, and default TypeScript support. Cloudflare provides the <code>@cloudflare/vitest-plugin</code> Vite plugin, which runs your Vitest tests inside the Workers runtime.</p>
<p>The Workers Vitest integration:</p>
<ul>
<li>Supports both <strong>unit tests</strong> and <strong>integration tests</strong>.</li>
<li>Provides direct access to Workers runtime APIs and bindings.</li>
<li>Implements isolated per-test-file storage.</li>
<li>Runs tests fully-locally using <a href="https://miniflare.dev/">Miniflare</a>.</li>
<li>Leverages Vitest's hot-module reloading for near instant reruns.</li>
<li>Supports projects with multiple Workers.</li>
</ul>
<p><a class="nb-link-button" href="/workers/testing/vitest-integration/write-your-first-test/">Write your first test</a></p>
<p>If you use <code>@cloudflare/vitest-pool-workers</code>, refer to <a href="/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/">Migrate to Vitest plugin</a>.</p>
