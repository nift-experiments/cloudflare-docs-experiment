<p>Run <a href="https://docs.devin.ai/onboard-devin/outposts">Devin agents</a> on Cloudflare. Each Devin session runs in its own isolated sandbox backed by Cloudflare Containers.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>A Devin Enterprise organization with permission to manage outposts and service users</li>
<li>A Cloudflare account with access to Workers, Containers, and R2</li>
<li>For manual deployment, <a href="https://nodejs.org/">Node.js 24</a> and a running <a href="https://www.docker.com/">Docker</a> daemon</li>
</ul>
<h3 id="get-your-devin-credentials">Get your Devin credentials</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13318.md")
</div>
<p>For more information about outposts, refer to the <a href="https://docs.devin.ai/onboard-devin/outposts">Devin Outposts overview</a>.</p>
<h2 id="deploy-with-one-click">Deploy with one click</h2>
<p>The fastest setup uses the <strong>Deploy to Cloudflare</strong> button. The deployment flow prompts for your Devin Outpost ID and API token. It also creates and configures the required containers.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/sandbox-sdk/tree/main/devin"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>Enter these credentials when prompted:</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>DEVIN_OUTPOST_ID</code></td>
<td>Your Devin Outpost ID</td>
</tr>
<tr>
<td><code>DEVIN_API_TOKEN</code></td>
<td>A Devin service-user token with the <strong>Run outpost workers</strong> permission</td>
</tr>
</tbody>
</table>
<p>After the deployment finishes, your outpost is ready to run Devin sessions on Cloudflare by selecting it from the Virtual environment menu.</p>
<h2 id="customize-and-deploy-manually">Customize and deploy manually</h2>
<p>Use the following procedure when you need to add dependencies, tools, or environment variables to the template.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13319.md")
</div>
<h2 id="run-a-devin-session">Run a Devin session</h2>
<p>In Devin, create a session and select your outpost from the <strong>Virtual environment</strong> menu. The worker polls Devin once per minute, so you may need to wait up to one minute for the session container to start.</p>
<h2 id="how-the-template-works">How the template works</h2>
<p>The template manages the lifecycle of each Devin session:</p>
<ul>
<li><strong>Poll:</strong> A cron trigger runs once per minute. The worker checks the current session statuses for your Devin Outpost.</li>
<li><strong>Start:</strong> Each pending or running session receives its own container. The container runs the official Devin worker command.</li>
<li><strong>Suspend:</strong> When a session suspends, the container archives <code>/root</code>, <code>/workspace</code>, and <code>/opt/devin-persistent</code> to R2. The container restores the checkpoint when the session resumes.</li>
<li><strong>Terminate:</strong> When a session terminates, the worker removes its container and R2 checkpoint.</li>
</ul>
<p>The worker coordinates the containers. Devin continues to manage session assignment and the session runtime.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13317.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://docs.devin.ai/onboard-devin/outposts">Devin Outposts overview</a></li>
<li><a href="https://github.com/cloudflare/sandbox-sdk/tree/main/devin">Devin Outpost deployment template</a></li>
<li><a href="/containers/">Cloudflare Containers</a></li>
<li><a href="/r2/">R2</a></li>
</ul>
