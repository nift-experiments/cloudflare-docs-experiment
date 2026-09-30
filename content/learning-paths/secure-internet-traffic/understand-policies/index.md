<p>Before you begin building security policies, there are a few key details about Gateway to review.</p>
<p>The next few modules will cover the breadth of types of policies and actions that can be accomplished by sending traffic through the Cloudflare Gateway inspection engine. This implementation guide assumes that your goals are to block threat actors from using attack vectors on your user base (such as malware, complex phishing attempts, and credential theft), as well as detection and prevention of threats to your corporate data (data loss prevention). These security threats may take internal and external forms. Separately, we will detail building threat prevention that uses our Remote Browser Isolation technology to maximally reduce the theoretical attack surface for your users.</p>
<p>This guide will provide you with a baseline of recommended policies to build and address common questions about policy building and accomplishing explicit outcomes.</p>
<h2 id="objectives">Objectives</h2>
<p>By the end of this module, you will be able to:</p>
<ul>
<li>Understand the order Gateway enforces policies for filtering traffic.</li>
<li>Create reusable lists for Gateway policies.</li>
<li>Subscribe to indicator feeds for advanced threat intelligence.</li>
</ul>
