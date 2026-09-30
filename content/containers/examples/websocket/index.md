<p class="article-summary">Forwarding a Websocket request to a Container</p>
<p>WebSocket requests are automatically forwarded to a container using the default <code>fetch</code>
method on the <code>Container</code> class:</p>
<pre><code class="language-js">import { Container, getContainer } from &quot;@cloudflare/containers&quot;;&#10;&#10;export class MyContainer extends Container {&#10;	defaultPort = 8080;&#10;	sleepAfter = &quot;2m&quot;;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		// gets default instance and forwards websocket from outside Worker&#10;		return getContainer(env.MY_CONTAINER).fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>View a full example in the <a href="https://github.com/cloudflare/containers/tree/main/examples/websocket">Container class repository</a>.</p>
