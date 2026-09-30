<ul>
<li><a href="/workers/runtime-apis/web-standards">Web Standards Reference</a></li>
<li><a href="/workers/runtime-apis/encoding">Encoding Reference</a></li>
<li><a href="/workers/runtime-apis/fetch">Fetch Reference</a></li>
<li><a href="/workers/runtime-apis/request">Request Reference</a></li>
<li><a href="/workers/runtime-apis/response">Response Reference</a></li>
<li><a href="/workers/runtime-apis/streams">Streams Reference</a></li>
<li><a href="/workers/runtime-apis/web-crypto">Web Crypto Reference</a></li>
</ul>
<h2 id="mocking-outbound-fetch-requests">Mocking Outbound <code>fetch</code> Requests</h2>
<p>When using the API, Miniflare allows you to substitute custom <code>Response</code>s for
<code>fetch()</code> calls using <code>undici</code>'s
<a href="https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentgetorigin"><code>MockAgent</code> API</a>.
This is useful for testing Workers that make HTTP requests to other services. To
enable <code>fetch</code> mocking, create a
<a href="https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentgetorigin"><code>MockAgent</code></a>
using the <code>createFetchMock()</code> function, then set this using the <code>fetchMock</code>
option.</p>
<pre><code class="language-js">import { Miniflare, createFetchMock } from &quot;miniflare&quot;;&#10;&#10;// Create `MockAgent` and connect it to the `Miniflare` instance&#10;const fetchMock = createFetchMock();&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      const res = await fetch(&quot;https://example.com/thing&quot;);&#10;      const text = await res.text();&#10;      return new Response(\`response:\${text}\`);&#10;    }&#10;  }&#10;  `,&#10;	fetchMock,&#10;});&#10;&#10;// Throw when no matching mocked request is found&#10;// (see https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentdisablenetconnect)&#10;fetchMock.disableNetConnect();&#10;&#10;// Mock request to https://example.com/thing&#10;// (see https://undici.nodejs.org/#/docs/api/MockAgent?id=mockagentgetorigin)&#10;const origin = fetchMock.get(&quot;https://example.com&quot;);&#10;// (see https://undici.nodejs.org/#/docs/api/MockPool?id=mockpoolinterceptoptions)&#10;origin&#10;	.intercept({ method: &quot;GET&quot;, path: &quot;/thing&quot; })&#10;	.reply(200, &quot;Mocked response!&quot;);&#10;&#10;const res = await mf.dispatchFetch(&quot;http://localhost:8787/&quot;);&#10;console.log(await res.text()); // &quot;response:Mocked response!&quot;&#10;</code></pre>
<h2 id="subrequests">Subrequests</h2>
<p>Miniflare does not support limiting the amount of
<a href="/workers/platform/limits#account-plan-limits">subrequests</a>.
Please keep this in mind if you make a large amount of subrequests from your
Worker.</p>
