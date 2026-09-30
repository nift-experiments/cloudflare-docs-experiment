<p>Limits that apply to authoring, deploying, and running Agents are detailed below.</p>
<p>Many limits are inherited from those applied to Workers scripts and/or Durable Objects, and are detailed in the <a href="/workers/platform/limits/">Workers limits</a> documentation.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Max concurrent (running) Agents per account</td>
<td>Tens of millions+ <sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Max definitions per account</td>
<td>~250,000+ <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Max state stored per unique Agent</td>
<td>1 GB</td>
</tr>
<tr>
<td>Max compute time per Agent</td>
<td>30 seconds (refreshed per HTTP request / incoming WebSocket message) <sup><a href="#footnote-3">3</a></sup></td>
</tr>
<tr>
<td>Duration (wall clock) per step <sup><a href="#footnote-3">3</a></sup></td>
<td>Unlimited (for example, waiting on a database call or an LLM response)</td>
</tr>
</tbody>
</table>
<hr />
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/1860.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Yes, really. You can have tens of millions of Agents running concurrently, as each Agent is mapped to a [unique Durable Object](/durable-objects/concepts/what-are-durable-objects/) (actor).</li>
<li id="footnote-2">You can deploy up to [500 scripts per account](/workers/platform/limits/), but each script (project) can define multiple Agents. Each deployed script can be up to 10 MB on the [Workers Paid Plan](/workers/platform/pricing/#workers)</li>
<li id="footnote-3">Compute (CPU) time per Agent is limited to 30 seconds, but this is refreshed when an Agent receives a new HTTP request, runs a [scheduled task](/agents/runtime/execution/schedule-tasks/), or an incoming WebSocket message.</li></ol></section>
