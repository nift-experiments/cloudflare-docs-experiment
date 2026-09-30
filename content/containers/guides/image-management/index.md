---
cp9:
  canonical: https://developers.cloudflare.com/containers/guides/image-management/
  description: Learn how to use Cloudflare Registry, Docker Hub, and Amazon ECR images with Containers.
  full_title: Image Management · Cloudflare Containers docs
  head_html: <title>Image Management · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Cloudflare Registry, Docker Hub, and Amazon ECR images with Containers."><link rel="canonical" href="https://developers.cloudflare.com/containers/guides/image-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/guides/image-management/index.md"><meta property="og:title" content="Image Management · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Cloudflare Registry, Docker Hub, and Amazon ECR images with Containers."><meta property="og:url" content="https://developers.cloudflare.com/containers/guides/image-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/guides/image-management/#page","headline":"Image Management \u00b7 Cloudflare Containers docs","description":"Learn how to use Cloudflare Registry, Docker Hub, and Amazon ECR images with Containers.","url":"https://developers.cloudflare.com/containers/guides/image-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/guides/image-management/
  schema: 1
---
<h2 id="push-images-during-wrangler-deploy">Push images during <code>wrangler deploy</code></h2>
<p>When running <code>wrangler deploy</code>, if you set the <code>image</code> attribute in your <a href="/workers/wrangler/configuration/#containers">Wrangler configuration</a> to a path to a Dockerfile, Wrangler will build your container image locally using Docker, then push it to a registry run by Cloudflare.
This registry is integrated with your Cloudflare account and is backed by <a href="/r2/">R2</a>. All authentication is handled automatically by
Cloudflare both when pushing and pulling images.</p>
<p>Just provide the path to your Dockerfile:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7109.md")
</div>
<p>And deploy your Worker with <code>wrangler deploy</code>. No other image management is necessary.</p>
<p>On subsequent deploys, Wrangler will only push image layers that have changed, which saves space and time.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7108.md")
</aside>
<h2 id="use-pre-built-container-images">Use pre-built container images</h2>
<p>Containers support images from the Cloudflare managed registry at <code>registry.cloudflare.com</code>, <a href="https://hub.docker.com/">Docker Hub</a>, <a href="https://aws.amazon.com/ecr/">Amazon ECR</a>, and <a href="https://cloud.google.com/artifact-registry">Google Artifact Registry</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7107.md")
</aside>
<h3 id="use-public-docker-hub-images">Use public Docker Hub images</h3>
<p>To use a public Docker Hub image, set <code>image</code> to a fully qualified Docker Hub image reference in your Wrangler configuration.</p>
<p>For example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7110.md")
</div>
<p>Public Docker Hub images do not require registry configuration.</p>
<p>Private Docker Hub images use the private registry configuration flow described next.</p>
<p>If Docker Hub credentials have been configured, those credentials are used to pull both public and private images.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7106.md")
</aside>
<h3 id="configure-private-registry-credentials">Configure private registry credentials</h3>
<p>To use a private image from Docker Hub, Amazon ECR, or Google Artifact Registry, run <a href="/workers/wrangler/commands/containers/#containers-registries-configure"><code>wrangler containers registries configure</code></a> for the registry domain.</p>
<p>Wrangler prompts for the secret and stores it in <a href="/secrets-store">Secrets Store</a>. If you do not already have a Secrets Store store, Wrangler prompts you to create one first.</p>
<p>Use <code>--secret-name</code> to name or reuse a secret, <code>--secret-store-id</code> to target a specific Secrets Store store, and <code>--skip-confirmation</code> for non-interactive runs. In CI or scripts, pass the secret through <code>stdin</code>.</p>
<h3 id="use-private-docker-hub-images">Use private Docker Hub images</h3>
<p>Configure Docker Hub in Wrangler using these values:</p>
<ul>
<li>registry domain: <code>docker.io</code></li>
<li>username flag: <code>--dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt;</code></li>
<li>secret: Docker Hub personal access token with read-only access</li>
</ul>
<p>To create a Docker Hub personal access token:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7111.md")
</div>
<p>Interactive:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler containers registries configure docker.io --dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler containers registries configure docker.io --dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler containers registries configure docker.io --dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler containers registries configure docker.io --dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler containers registries configure docker.io --dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler containers registries configure docker.io --dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt;" aria-label="Copy to clipboard">Copy</button></div></div>
<p>CI or scripts:</p>
<pre tabindex="0"><code class="language-bash">printf &#x27;%s&#x27; &quot;$DOCKERHUB_PAT&quot; | npx wrangler containers registries configure docker.io --dockerhub-username=&lt;YOUR_DOCKERHUB_USERNAME&gt; --secret-name=&lt;SECRET_NAME&gt; --skip-confirmation&#10;</code></pre>
<p>After you configure the registry, use the same fully qualified Docker Hub image reference shown above.</p>
<h3 id="use-private-amazon-ecr-images">Use private Amazon ECR images</h3>
<p>Configure Amazon ECR in Wrangler using these values:</p>
<ul>
<li>registry domain: <code>&lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com</code></li>
<li>access key flag: <code>--aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;</code></li>
<li>secret: matching AWS secret access key</li>
</ul>
<p>Public ECR images are not supported.
To generate the required credentials, create an IAM user with a read-only policy. The following example grants access to all image repositories in AWS account <code>123456789012</code> in <code>us-east-1</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;Version&quot;: &quot;2012-10-17&quot;,&#10;	&quot;Statement&quot;: [&#10;		{&#10;			&quot;Action&quot;: [&quot;ecr:GetAuthorizationToken&quot;],&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Resource&quot;: &quot;*&quot;&#10;		},&#10;		{&#10;			&quot;Effect&quot;: &quot;Allow&quot;,&#10;			&quot;Action&quot;: [&#10;				&quot;ecr:BatchCheckLayerAvailability&quot;,&#10;				&quot;ecr:GetDownloadUrlForLayer&quot;,&#10;				&quot;ecr:BatchGetImage&quot;&#10;			],&#10;			// arn:${Partition}:ecr:${Region}:${Account}:repository/${Repository-name}&#10;			&quot;Resource&quot;: [&#10;				&quot;arn:aws:ecr:us-east-1:123456789012:repository/*&quot;&#10;				// &quot;arn:aws:ecr:us-east-1:123456789012:repository/example-repo&quot;&#10;			]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>After you create the IAM user, use its credentials to <a href="/workers/wrangler/commands/containers/#containers-registries-configure">configure the registry in Wrangler</a>. Wrangler prompts you to create a Secrets Store store if one does not already exist, then stores the secret there.</p>
<p>Interactive:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler containers registries configure &lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com --aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler containers registries configure &lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com --aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler containers registries configure &lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com --aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler containers registries configure &lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com --aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler containers registries configure &lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com --aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler containers registries configure &lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com --aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt;" aria-label="Copy to clipboard">Copy</button></div></div>
<p>CI or scripts:</p>
<pre tabindex="0"><code class="language-bash">printf &#x27;%s&#x27; &quot;$AWS_SECRET_ACCESS_KEY&quot; | npx wrangler containers registries configure &lt;AWS_ACCOUNT_ID&gt;.dkr.ecr.&lt;AWS_REGION&gt;.amazonaws.com --aws-access-key-id=&lt;AWS_ACCESS_KEY_ID&gt; --secret-name=&lt;SECRET_NAME&gt; --skip-confirmation&#10;</code></pre>
<p>After you configure the registry, use the fully qualified Amazon ECR image reference in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7112.md")
</div>
<h3 id="use-private-google-artifact-registry-images">Use private Google Artifact Registry images</h3>
<p>Configure Google Artifact Registry in Wrangler using these values:</p>
<ul>
<li>registry domain: <code>&lt;REGION&gt;-docker.pkg.dev</code></li>
<li>Google service account email flag: <code>--gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt;</code></li>
<li>secret: the service account JSON key</li>
</ul>
<p>The public credential is the service account email, supplied with <code>--gar-email</code>. It must match the <code>client_email</code> field in the service account key.</p>
<p>The private credential is the service account JSON key.
Provide it through <code>stdin</code> (a file path, raw JSON, or base64) or the interactive prompt (a file path or base64).
Wrangler stores the key base64-encoded in Secrets Store.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7105.md")
</aside>
<p>To generate the required credentials, create a service account with the <strong>Artifact Registry Reader</strong> role and download its JSON key:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7113.md")
</div>
<p>Interactive:
Wrangler prompts for the key, where you enter a file path or base64-encoded JSON:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt;" aria-label="Copy to clipboard">Copy</button></div></div>
<p>CI or scripts:
Pipe the key through <code>stdin</code> (the key contents as raw JSON or base64, or a path to the key file)</p>
<pre tabindex="0"><code class="language-bash">cat &lt;PATH_TO_KEY&gt; | npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt; --secret-name=&lt;SECRET_NAME&gt; --skip-confirmation&#10;</code></pre>
<p>If you have already stored the key in Secrets Store, reference the existing secret and omit the key:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt; --secret-name=&lt;EXISTING_SECRET_NAME&gt; --skip-confirmation&#10;</code></pre>
<p>After you configure the registry, use the fully qualified Google Artifact Registry image reference in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7114.md")
</div>
<h3 id="use-images-from-other-registries">Use images from other registries</h3>
<p>If you want to use a pre-built image from another registry provider, first make sure it exists locally, then push it to the Cloudflare Registry:</p>
<pre tabindex="0"><code class="language-bash">docker pull &lt;PUBLIC_IMAGE&gt;&#10;docker tag &lt;PUBLIC_IMAGE&gt; &lt;IMAGE&gt;:&lt;TAG&gt;&#10;</code></pre>
<p>Wrangler provides a command to push images to the Cloudflare Registry:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler containers push &lt;IMAGE&gt;:&lt;TAG&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler containers push &lt;IMAGE&gt;:&lt;TAG&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler containers push &lt;IMAGE&gt;:&lt;TAG&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler containers push &lt;IMAGE&gt;:&lt;TAG&gt;" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler containers push &lt;IMAGE&gt;:&lt;TAG&gt;</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler containers push &lt;IMAGE&gt;:&lt;TAG&gt;" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Or, you can use the <code>-p</code> flag with <code>wrangler containers build</code> to build and push an image in one step:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler containers build -p -t &lt;TAG&gt; .</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler containers build -p -t &lt;TAG&gt; ." aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler containers build -p -t &lt;TAG&gt; .</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler containers build -p -t &lt;TAG&gt; ." aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler containers build -p -t &lt;TAG&gt; .</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler containers build -p -t &lt;TAG&gt; ." aria-label="Copy to clipboard">Copy</button></div></div>
<p>This will output an image registry URI that you can then use in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7115.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7104.md")
</aside>
<h2 id="push-images-with-ci">Push images with CI</h2>
<p>To use an image built in a continuous integration environment, install <code>wrangler</code> then
build and push images using either <code>wrangler containers build</code> with the <code>--push</code> flag, or
using the <code>wrangler containers push</code> command.</p>
<h2 id="registry-limits">Registry limits</h2>
<p>Images are limited in size by available disk of the configured <a href="/containers/platform/limits/#instance-types">instance type</a> for a Container.</p>
<p>Delete images with <code>wrangler containers images delete</code> to free up space, but reverting a
Worker to a previous version that uses a deleted image will then error.</p>
