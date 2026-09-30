<p>Terraform ships as a single binary file. The examples below include installation information for popular operating systems.</p>
<p>For official instructions on installing Terraform, refer to <a href="https://developer.hashicorp.com/terraform/tutorials/certification-associate-tutorials/install-cli">Install Terraform</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/255.md")
</aside>
<h2 id="mac">Mac</h2>
<p>The easiest way to install Terraform on macOS is with Homebrew.</p>
<pre><code class="language-sh">brew tap hashicorp/tap&#10;brew install hashicorp/tap/terraform&#10;</code></pre>
<h2 id="linux">Linux</h2>
<p>You can install the <code>terraform</code> binary via your distribution's package manager. For example:</p>
<pre><code class="language-sh">sudo apt install terraform&#10;</code></pre>
<p>Alternatively, you can fetch a specific version directly and place the binary in your <code>PATH</code>:</p>
<pre><code class="language-sh">wget -q https://releases.hashicorp.com/terraform/1.4.5/terraform_1.4.5_linux_amd64.zip&#10;&#10;unzip terraform_1.4.5_linux_amd64.zip&#10;</code></pre>
<pre><code class="language-sh">Archive:  terraform_1.4.5_linux_amd64.zip&#10;  inflating: terraform&#10;</code></pre>
<pre><code class="language-sh">sudo mv terraform /usr/local/bin/terraform&#10;&#10;terraform version&#10;</code></pre>
<pre><code class="language-sh">Terraform v1.4.5&#10;</code></pre>
<h2 id="windows">Windows</h2>
<ol>
<li>Download the 32 or 64-bit executable from the <a href="https://developer.hashicorp.com/terraform/downloads">Download Terraform</a> page.</li>
<li>Unzip and place <code>terraform.exe</code> somewhere in your path.</li>
</ol>
<h2 id="other">Other</h2>
<p>For additional installers, refer to the <a href="https://developer.hashicorp.com/terraform/downloads">Download Terraform</a> page.</p>
