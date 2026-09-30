<p>Cloudflare Workers allows you to build serverless applications or augment existing ones by writing code that is deployed instantly across the globe. To understand the significance of Workers technology, we begin by understanding the environment in which it was developed.</p>
<p>Workers is a serverless computing provider. <a href="https://www.cloudflare.com/learning/serverless/what-is-serverless/">Serverless computing</a> refers to a cloud computing model where providers, like Cloudflare, manage servers on behalf of users, allowing developers and businesses to focus entirely on writing and deploying application logic.</p>
<h2 id="cloud-computing">Cloud computing</h2>
<p><a href="https://www.cloudflare.com/learning/cloud/what-is-the-cloud/">Cloud computing</a> is defined as hosting computing resources (such as virtual machines, storage, databases, and networking services) on third-party servers. Cloud computing service providers include Amazon Web Services, Microsoft Azure, Google Cloud Platform, and Cloudflare.</p>
<h3 id="serverless-computing">Serverless computing</h3>
<p>Serverless computing is a subset of cloud computing. Serverless computing is a method of providing backend services on an as-used basis. A serverless provider allows users to write and deploy code without the hassle of worrying about the underlying infrastructure. Serverless computing has unique characteristics that set it apart from other cloud computing models.</p>
<h4 id="resource-management">Resource management</h4>
<p>Cloud computing allows organizations to rent a fixed number of servers or server space. To prepare for seasonal or unplanned spikes in request traffic to their applications, organizations may overpurchase server space to ensure their applications do not go down because of high request volume from end users or customers.</p>
<p>In the serverless computing model, organizations and individuals are not required to calculate how much server space or machines they need to rent. Serverless computing providers take care of server management, and provisioning, allowing developers and organizations to focus on writing and deploying logic.</p>
<p>Serverless computing providers scale automatically to handle surges and low points in request traffic. The serverless computing provider is responsible for the scalability of your application and will work to match resources to the volume of requests your application is receiving, ensuring your application stays online.</p>
<h4 id="execution-model">Execution model</h4>
<p>Serverless computing providers differ in their approach to how your application's code is executed. Many serverless computing providers, like Cloudflare, use an event-driven model. When an event (such as an HTTP request or a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a>) invokes a Worker, the Worker code will execute. The total amount of time from the start to end of an invocation of a Worker is known as <a href="/workers/platform/limits/#duration">duration</a>. The amount of time the CPU actually spends doing work during a given request is known as <a href="/workers/platform/pricing/#workers">CPU time</a>.</p>
<h4 id="billing-model">Billing model</h4>
<p>Developers and organizations using serverless computing are billed on a usage model paradigm. Instead of paying for a fixed amount of computing resources that may be underutilized or exceeded, users pay as much as they use in the serverless model. Usage is defined differently per serverless computing provider. Usage in Workers is defined as CPU time.</p>
<h2 id="summary">Summary</h2>
<p>By reading this page, you have:</p>
<ul>
<li>Been introduced to the serverless computing concept that is behind Cloudflare Workers.</li>
<li>Reviewed the differences between legacy on-premise and cloud computing infrastructure.</li>
<li>Analyzed the key differences between the cloud computing and serverless computing paradigms.</li>
</ul>
<p>In the next section, you will learn about what makes Workers, a serverless computing platform that is part of the larger Cloudflare Developer Platform, unique in its architecture from other serverless computing providers.</p>
