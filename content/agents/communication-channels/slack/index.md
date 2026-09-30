<p>Slack is a communication channel for agents that need to participate in team conversations. A Slack-connected agent can receive events from Slack, route each message to the right agent instance, and respond back to direct messages or channel mentions.</p>
<p>Use Slack when you want an agent to:</p>
<ul>
<li>Respond to direct messages from Slack users.</li>
<li>Reply when mentioned in public channels.</li>
<li>Maintain context inside Slack threads.</li>
<li>Serve multiple Slack workspaces from one deployment.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Slack sends events to your Worker through the <a href="https://api.slack.com/apis/events-api">Slack Events API</a>. Your Worker verifies each request, identifies the installed workspace, and routes the event to an agent instance.</p>
<p>Common Slack events include:</p>
<table>
<thead>
<tr>
<th>Event</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>message.im</code></td>
<td>Direct messages to the bot</td>
</tr>
<tr>
<td><code>app_mention</code></td>
<td>Mentions in channels</td>
</tr>
</tbody>
</table>
<p>For multi-workspace Slack apps, store each workspace installation separately and route events by team or enterprise ID. Each workspace can map to an isolated agent instance with its own Durable Object-backed state.</p>
<h2 id="build-a-slack-agent">Build a Slack agent</h2>
<p>For a complete walkthrough, including Slack app setup, OAuth, event subscriptions, and deployment, use the Slack agent example.</p>
<p><a class="nb-card nb-link-card" href="/agents/examples/slack-agent/"><h3 id="card-slack-agent-agents-examples-slack-agent">Slack agent</h3><p>Build and deploy an AI-powered Slack bot on Cloudflare Workers using the Agents SDK.</p></a></p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="https://api.slack.com/apis/events-api"><h3 id="card-slack-events-api-https-api-slack-com-apis-events-api">Slack Events API</h3><p>Receive events when users message, mention, or interact with a Slack app.</p></a></p>
<p><a class="nb-card nb-link-card" href="https://api.slack.com/authentication"><h3 id="card-slack-app-authentication-https-api-slack-com-authentication">Slack app authentication</h3><p>Configure OAuth, bot tokens, signing secrets, and request verification for Slack apps.</p></a></p>
