<p>Guardrails help you deploy AI applications safely by intercepting and evaluating both user prompts and model responses for harmful content. Acting as a proxy between your application and <a href="/ai-gateway/usage/providers/">model providers</a> (such as OpenAI, Anthropic, DeepSeek, and others), AI Gateway's Guardrails ensure a consistent and secure experience across your entire AI ecosystem.</p>
<p>Guardrails proactively monitor interactions between users and AI models, giving you:</p>
<ul>
<li><strong>Consistent moderation</strong>: Uniform moderation layer that works across models and providers.</li>
<li><strong>Enhanced safety and user trust</strong>: Proactively protect users from harmful or inappropriate interactions.</li>
<li><strong>Flexibility and control over allowed content</strong>: Specify which categories to monitor and choose between flagging or outright blocking.</li>
<li><strong>Auditing and compliance capabilities</strong>: Receive updates on evolving regulatory requirements with logs of user prompts, model responses, and enforced guardrails.</li>
</ul>
<h2 id="video-demo">Video demo</h2>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/Its1H0jTxrQ" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="how-guardrails-work">How Guardrails work</h2>
<p>AI Gateway inspects all interactions in real time by evaluating content against predefined safety parameters. Guardrails work by:</p>
<ol>
<li>
<p>Intercepting interactions:
AI Gateway proxies requests and responses, sitting between the user and the AI model.</p>
</li>
<li>
<p>Inspecting content:</p>
<ul>
<li>User prompts: AI Gateway checks prompts against safety parameters (for example, violence, hate, or sexual content). Based on your settings, prompts can be flagged or blocked before reaching the model.</li>
<li>Model responses: Once processed, the AI model response is inspected. If hazardous content is detected, it can be flagged or blocked before being delivered to the user.</li>
</ul>
</li>
<li>
<p>Applying actions:
Depending on your configuration, flagged content is logged for review, while blocked content is prevented from proceeding.</p>
</li>
</ol>
<h2 id="related-resource">Related resource</h2>
<ul>
<li><a href="https://blog.cloudflare.com/guardrails-in-ai-gateway/">Cloudflare Blog: Keep AI interactions secure and risk-free with Guardrails in AI Gateway</a></li>
</ul>
