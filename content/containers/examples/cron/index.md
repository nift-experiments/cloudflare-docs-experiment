<p class="article-summary">Running a container on a schedule using Cron Triggers</p>
<p>To launch a container on a schedule, you can use a Workers <a href="/workers/configuration/cron-triggers/">Cron Trigger</a>.</p>
<p>For a full example, see the <a href="https://github.com/mikenomitch/cron-container/tree/main">Cron Container Template</a>.</p>
<p>Use a cron expression in your Wrangler config to specify the schedule:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7144.md")
</div>
<p>Then in your Worker, call your Container from the &quot;scheduled&quot; handler:</p>
<pre><code class="language-ts">import { Container, getContainer } from &#x27;@cloudflare/containers&#x27;;&#10;&#10;export class CronContainer extends Container {&#10;  sleepAfter = &#x27;10s&#x27;;&#10;&#10;  override onStart() {&#10;    console.log(&#x27;Starting container&#x27;);&#10;  }&#10;&#10;  override onStop() {&#10;    console.log(&#x27;Container stopped&#x27;);&#10;  }&#10;}&#10;&#10;export default {&#10;  async fetch(): Promise&lt;Response&gt; {&#10;    return new Response(&quot;This Worker runs a cron job to execute a container on a schedule.&quot;);&#10;  },&#10;&#10;  async scheduled(_controller: any, env: { CRON_CONTAINER: DurableObjectNamespace&lt;CronContainer&gt; }) {&#10;    let container = getContainer(env.CRON_CONTAINER);&#10;    await container.start({&#10;      envVars: {&#10;				MESSAGE: &quot;Start Time: &quot; + new Date().toISOString(),&#10;      }&#10;    })&#10;  },&#10;};&#10;</code></pre>
