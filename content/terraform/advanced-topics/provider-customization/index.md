<p>Terraform communicates with cloud and global network provider APIs such as Cloudflare through modules known as providers. These providers are <a href="/terraform/tutorial/initialize-terraform/#2-initialize-terraform-and-the-cloudflare-provider">installed automatically</a> when you run <code>terraform init</code> in a directory that has a <code>.tf</code> file containing a provider.</p>
<p>Typically, the only required parameters to the provider are those required to authenticate. However, you may want to customize the provider to your needs. The following section covers some <a href="https://www.terraform.io/docs/providers/cloudflare/#argument-reference">optional settings</a> that you can pass to the Cloudflare Terraform provider.</p>
<h2 id="adjust-the-default-cloudflare-provider-settings">Adjust the default Cloudflare provider settings</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14771.md")
</aside>
<p>You can customize the Cloudflare Terraform provider using configuration parameters, specified either in your <code>.tf</code> configuration files or via environment variables. Using environment variables may make sense when running Terraform from a CI/CD system or when the change is temporary and does not need to be persisted in your configuration history.</p>
