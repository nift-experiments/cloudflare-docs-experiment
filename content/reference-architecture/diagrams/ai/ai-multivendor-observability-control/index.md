<h2 id="introduction">Introduction</h2>
<p>The AI landscape is rapidly evolving with new models, services, and applications emerging daily. Many developers and organizations seek to enhance agility by opting for inference-as-a-service solutions like <a href="/workers-ai/">Workers AI</a>, rather than developing or managing models themselves.</p>
<p>Inference-as-a-Service is a cloud-based model that allows users to deploy and execute AI without managing underlying infrastructure. The platform handles all aspects of model serving, including scaling resources based on demand, often-times supporting both real-time and batch inference. Users can send input data to the model via API calls, with the service provider managing servers, scaling, and maintenance tasks. Typically operating on a pay-as-you-go model, inference services simplify model deployment and scaling, enabling organizations to leverage AI capabilities without infrastructure complexities.</p>
<p>As this field evolves rapidly, developers and organizations face several challenges:</p>
<ul>
<li>Fragmentation: Many inference service providers offer only a limited range of models and features. Different use cases may require multiple vendors, leading to fragmentation.</li>
<li>Availability: With increasing demand and fast-paced technological advancements, inference service providers struggle to maintain high API availability.</li>
<li>Lack of observability: Providers often offer limited analytics and logging capabilities, which vary across vendors. Gaining a unified view of AI usage proves challenging.</li>
<li>Lack of security control: Organizations encounter difficulties in maintaining adequate security measures.</li>
<li>Lack of cost control: Understanding usage insights can be challenging, and the absence of custom rate limits poses risks in public-facing AI use cases.</li>
</ul>
<p>Using a forward proxy can mitigate these challenges. Positioned between the service making inference requests and the inference service platform, it serves as a single point for observability and control. By shifting features such as rate limiting, caching, and error handling to the proxy layer, organizations can apply unified configurations across services and inference service providers.</p>
<h2 id="ai-forward-proxy-setup">AI forward proxy setup</h2>
<p>The following architecture illustrates the setup of <a href="/ai-gateway/">AI Gateway</a> as a forward proxy between a service and one or multiple AI inference providers, such as <a href="/workers-ai/">Workers AI</a></p>
<p><img src="/assets/upstream/images/reference-architecture/ai-multivendor-observability-control/ai-multi-vendor-observability-control.svg" alt="Figure 1: Multi-vendor AI architecture" title="Multi-vendor AI architecture" /></p>
<ol>
<li><strong>Inference request</strong>: Send POST request to your AI gateway.</li>
<li><strong>Request proxying</strong>: Forward <code>POST</code> request to AI Inference provider or serve response from <a href="/ai-gateway/features/caching">cache, if enabled and available</a>. During this process, both <a href="/ai-gateway/observability/analytics/">analytics</a> and <a href="/ai-gateway/observability/logging/">logs</a> are collected. Additionally, controls such as Rate Limiting are enforced.</li>
<li><strong>Error handling</strong>: In case of errors, retry request or fallback to other inference provider, depending on configuration.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ai-gateway/get-started/">AI Gateway: Get started</a></li>
<li><a href="/ai-gateway/usage/providers/">AI Gateway: Supported Providers</a></li>
</ul>
