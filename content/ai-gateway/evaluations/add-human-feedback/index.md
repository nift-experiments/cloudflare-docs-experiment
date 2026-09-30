<p>Human feedback is a valuable metric to assess the performance of your AI models. By incorporating human feedback, you can gain deeper insights into how the model's responses are perceived and how well it performs from a user-centric perspective. This feedback can then be used in evaluations to calculate performance metrics, driving optimization and ultimately enhancing the reliability, accuracy, and efficiency of your AI application.</p>
<p>Human feedback measures the performance of your dataset based on direct human input. The metric is calculated as the percentage of positive feedback (thumbs up) given on logs, which are annotated in the Logs tab of the Cloudflare dashboard. This feedback helps refine model performance by considering real-world evaluations of its output.</p>
<p>This tutorial will guide you through the process of adding human feedback to your evaluations in AI Gateway using the Cloudflare dashboard.</p>
<p>On the next guide, you can <a href="/ai-gateway/evaluations/add-human-feedback-api/">learn how to add human feedback via the API</a>.</p>
<h2 id="1-log-in-to-the-dashboard"><ol>
<li>Log in to the dashboard</li>
</ol></h2>
<p>In the Cloudflare dashboard, go to the <strong>AI Gateway</strong> page.</p>
<div class="nb-dash-button"></div>
<h2 id="2-access-the-logs-tab"><ol start="2">
<li>Access the Logs tab</li>
</ol></h2>
<ol>
<li>Go to <strong>Logs</strong>.</li>
<li>The Logs tab displays all logs associated with your datasets. These logs show key information, including:
<ul>
<li>Timestamp: When the interaction occurred.</li>
<li>Status: Whether the request was successful, cached, or failed.</li>
<li>Model: The model used in the request.</li>
<li>Tokens: The number of tokens consumed by the response.</li>
<li>Cost: The cost based on token usage.</li>
<li>Duration: The time taken to complete the response.</li>
<li>Feedback: Where you can provide human feedback on each log.</li>
</ul>
</li>
</ol>
<h2 id="3-provide-human-feedback"><ol start="3">
<li>Provide human feedback</li>
</ol></h2>
<ol>
<li>Click on the log entry you want to review. This expands the log, allowing you to see more detailed information.</li>
<li>In the expanded log, you can view additional details such as:
<ul>
<li>The user prompt.</li>
<li>The model response.</li>
<li>HTTP response details.</li>
<li>Endpoint information.</li>
</ul>
</li>
<li>You will see two icons:
<ul>
<li>Thumbs up: Indicates positive feedback.</li>
<li>Thumbs down: Indicates negative feedback.</li>
</ul>
</li>
<li>Click either the thumbs up or thumbs down icon based on how you rate the model response for that particular log entry.</li>
</ol>
<h2 id="4-evaluate-human-feedback"><ol start="4">
<li>Evaluate human feedback</li>
</ol></h2>
<p>After providing feedback on your logs, it becomes a part of the evaluation process.</p>
<p>When you run an evaluation (as outlined in the <a href="/ai-gateway/evaluations/set-up-evaluations/">Set Up Evaluations</a> guide), the human feedback metric will be calculated based on the percentage of logs that received thumbs-up feedback.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/2849.md")
</aside>
<h2 id="5-review-results"><ol start="5">
<li>Review results</li>
</ol></h2>
<p>After running the evaluation, review the results on the Evaluations tab.
You will be able to see the performance of the model based on cost, speed, and now human feedback, represented as the percentage of positive feedback (thumbs up).</p>
<p>The human feedback score is displayed as a percentage, showing the distribution of positively rated responses from the database.</p>
<p>For more information on running evaluations, refer to the documentation <a href="/ai-gateway/evaluations/set-up-evaluations/">Set Up Evaluations</a>.</p>
