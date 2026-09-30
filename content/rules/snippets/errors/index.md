<h2 id="error-1201-snippet-tried-to-continue-to-origin-multiple-times">Error 1201: Snippet tried to continue to origin multiple times</h2>
<p>This error occurs when a Snippet attempts to call <code>fetch(request)</code> more than once.</p>
<h3 id="resolution">Resolution</h3>
<p>Ensure that your Snippet code only calls <code>fetch(request)</code> once. This method is used to send the modified request to the origin server, and it should be called only once per Snippet to avoid conflicts.</p>
<h2 id="error-1202-snippets-exceeded-subrequests-limit">Error 1202: Snippets exceeded subrequests limit</h2>
<p>This error occurs when the number of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/12785.md")
</div> exceeds [the limit](/rules/snippets/#availability) for your Cloudflare plan.
<h3 id="resolution-1">Resolution</h3>
<p>Review your Snippet to ensure your code is within the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/12786.md")
</div> [limits](/rules/snippets/#availability) for your plan. Each subrequest counts against your limit, including any redirects within a subrequest chain.
<h2 id="error-1203-snippets-exceeded-cpu-time-limit">Error 1203: Snippets exceeded CPU time limit</h2>
<p>This error occurs when a Snippet exceeds the defined <a href="/rules/snippets/#limits">CPU time limit</a> for Snippets.</p>
<h3 id="resolution-2">Resolution</h3>
<p>Review your Snippet to ensure your code is within the CPU time limit. If you need a higher CPU time limit, consider using <a href="/workers/">Cloudflare Workers</a>. Refer to <a href="/rules/snippets/when-to-use/">When to use Snippets vs Workers</a> for details.</p>
<h2 id="error-1204-snippets-exceeded-memory-limit">Error 1204: Snippets exceeded memory limit</h2>
<p>This error occurs when a Snippet exceeds the defined <a href="/rules/snippets/#limits">memory limit</a> for Snippets.</p>
<h3 id="resolution-3">Resolution</h3>
<p>Review your Snippet to ensure your code is within the memory limit. If you need a higher memory limit, consider using <a href="/workers/">Cloudflare Workers</a>. Refer to <a href="/rules/snippets/when-to-use/">When to use Snippets vs Workers</a> for details.</p>
<h2 id="error-1205-deployment-in-progress">Error 1205: Deployment in progress</h2>
<p>A new Snippet was just deployed and is currently propagating across Cloudflare's global network. During this short window, requests may not be processed as expected.</p>
<h3 id="resolution-4">Resolution</h3>
<p>This is a temporary issue. Retry your request after a few seconds — the Snippet will be active once propagation completes.</p>
<h2 id="error-1206-snippet-threw-exception">Error 1206: Snippet threw exception</h2>
<p>The Snippet encountered an unhandled JavaScript exception during execution. This may be caused by one of the following:</p>
<ul>
<li>Runtime JavaScript errors in Snippet code</li>
<li>Unhandled promise rejections</li>
<li>Type errors or reference errors</li>
</ul>
<h3 id="resolution-5">Resolution</h3>
<ul>
<li>Review the Snippet code to identify where the exception might have occurred and fix any detected bugs.</li>
<li>Add proper error handling (<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch"><code>try...catch</code></a> blocks).</li>
</ul>
<h2 id="snippets-cannot-be-renamed">Snippets cannot be renamed</h2>
<p>The name you define when creating a Snippet will be used as the Snippet ID and cannot be edited afterwards.</p>
<h3 id="resolution-6">Resolution</h3>
<p>To change the name of your Snippet, create a new Snippet and delete the old one.</p>
