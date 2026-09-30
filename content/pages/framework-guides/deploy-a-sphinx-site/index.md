<p><a href="https://www.sphinx-doc.org/">Sphinx</a> is a tool that makes it easy to create documentation and was originally made for the publication of Python documentation. It is well known for its simplicity and ease of use.</p>
<p>In this guide, you will create a new Sphinx project and deploy it using Cloudflare Pages.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>
<p>Python 3 - Sphinx is based on Python, therefore you must have Python installed</p>
</li>
<li>
<p><a href="https://pypi.org/project/pip/">pip</a> - The PyPA recommended tool for installing Python packages</p>
</li>
<li>
<p><a href="https://pipenv.pypa.io/en/latest/">pipenv</a> - automatically creates and manages a virtualenv for your projects</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11028.md")
</aside>
<p>The latest version of Python 3.7 is 3.7.11:</p>
<p><a href="https://www.python.org/downloads/release/python-3711/">Python 3.7.11</a></p>
<h3 id="installing-python">Installing Python</h3>
<p>Refer to the official Python documentation for installation guidance:</p>
<ul>
<li><a href="https://www.python.org/downloads/windows/">Windows</a></li>
<li><a href="https://www.python.org/downloads/source/">Linux/UNIX</a></li>
<li><a href="https://www.python.org/downloads/macos/">macOS</a></li>
<li><a href="https://www.python.org/download/other/">Other</a></li>
</ul>
<h3 id="installing-pipenv">Installing Pipenv</h3>
<p>If you already had an earlier version of Python installed before installing version 3.7, other global packages you may have installed could interfere with the following steps to install Pipenv, or your other Python projects which depend on global packages.</p>
<p><a href="https://pipenv.pypa.io/en/latest/">Pipenv</a> is a Python-based package manager that makes managing virtual environments simple. This guide will not require you to have prior experience with or knowledge of Pipenv to complete your Sphinx site deployment. Cloudflare Pages natively supports the use of Pipenv and, by default, has the latest version installed.</p>
<p>The quickest way to install Pipenv is by running the command:</p>
<pre><code class="language-sh">pip install --user pipenv&#10;</code></pre>
<p>This command will install Pipenv to your user level directory and will make it accessible via your terminal. You can confirm this by running the following command and reviewing the expected output:</p>
<pre><code class="language-sh">pipenv --version&#10;</code></pre>
<pre><code class="language-sh">pipenv, version 2021.5.29&#10;</code></pre>
<h3 id="creating-a-sphinx-project-directory">Creating a Sphinx project directory</h3>
<p>From your terminal, run the following commands to create a new directory and navigate to it:</p>
<pre><code class="language-sh">mkdir my-wonderful-new-sphinx-project&#10;cd my-wonderful-new-sphinx-project&#10;</code></pre>
<h3 id="pipenv-with-python-3-7">Pipenv with Python 3.7</h3>
<p>Pipenv allows you to specify which version of Python to associate with a virtual environment. For the purpose of this guide, the virtual environment for your Sphinx project must use Python 3.7.</p>
<p>Use the following command:</p>
<pre><code class="language-sh">pipenv --python 3.7&#10;</code></pre>
<p>You should see the following output:</p>
<pre><code class="language-bash">Creating a virtualenv for this project...&#10;Pipfile: /home/ubuntu/my-wonderful-new-sphinx-project/Pipfile&#10;Using /usr/bin/python3.7m (3.7.11) to create virtualenv...&#10;⠸ Creating virtual environment...created virtual environment CPython3.7.11.final.0-64 in 1598ms&#10;  creator CPython3Posix(dest=/home/ubuntu/.local/share/virtualenvs/my-wonderful-new-sphinx-project-Y2HfWoOr, clear=False, no_vcs_ignore=False, global=False)&#10;  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/ubuntu/.local/share/virtualenv)&#10;    added seed packages: pip==21.1.3, setuptools==57.1.0, wheel==0.36.2&#10;  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator&#10;&#10;✔ Successfully created virtual environment!&#10;Virtualenv location: /home/ubuntu/.local/share/virtualenvs/my-wonderful-new-sphinx-project-Y2HfWoOr&#10;Creating a Pipfile for this project...&#10;</code></pre>
<p>List the contents of the directory:</p>
<pre><code class="language-sh">ls&#10;</code></pre>
<pre><code class="language-sh">Pipfile&#10;</code></pre>
<h3 id="installing-sphinx">Installing Sphinx</h3>
<p>Before installing Sphinx, create the directory you want your project to live in.</p>
<p>From your terminal, run the following command to install Sphinx:</p>
<pre><code class="language-sh">pipenv install sphinx&#10;</code></pre>
<p>You should see output similar to the following:</p>
<pre><code class="language-bash">Installing sphinx...&#10;Adding sphinx to Pipfile&#x27;s [packages]...&#10;✔ Installation Succeeded&#10;Pipfile.lock not found, creating...&#10;Locking [dev-packages] dependencies...&#10;Locking [packages] dependencies...&#10;Building requirements...&#10;Resolving dependencies...&#10;✔ Success!&#10;Updated Pipfile.lock (763aa3)!&#10;Installing dependencies from Pipfile.lock (763aa3)...&#10;  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00&#10;To activate this project&#x27;s virtualenv, run pipenv shell.&#10;Alternatively, run a command inside the virtualenv with pipenv run.&#10;</code></pre>
<p>This will install Sphinx into a new virtual environment managed by Pipenv. You should see a directory structure like this:</p>
<pre><code class="language-bash">my-wonderful-new-sphinx-project&#10;|--Pipfile&#10;|--Pipfile.lock&#10;</code></pre>
<h2 id="creating-a-new-project">Creating a new project</h2>
<p>With Sphinx installed, you can now run the quickstart command to create a template project for you. This command will only work within the Pipenv environment you created in the previous step. To enter that environment, run the following command from your terminal:</p>
<pre><code class="language-sh">pipenv shell&#10;</code></pre>
<pre><code class="language-sh">Launching subshell in virtual environment...&#10;ubuntu@sphinx-demo:~/my-wonderful-new-sphinx-project$  . /home/ubuntu/.local/share/virtualenvs/my-wonderful-new-sphinx-project-Y2HfWoOr/bin/activate&#10;</code></pre>
<p>Now run the following command:</p>
<pre><code class="language-sh">sphinx-quickstart&#10;</code></pre>
<p>You will be presented with a number of questions, please answer them in the following:</p>
<pre><code class="language-sh">Separate source and build directories (y/n) [n]: Y&#10;Project name: &lt;Your project name&gt;&#10;Author name(s): &lt;You Author Name&gt;&#10;Project release []: &lt;You can accept default here or provide a version&gt;&#10;Project language [en]: &lt;You can accept en here or provide a regional language code&gt;&#10;</code></pre>
<p>This will create four new files in your active directory, <code>source/conf.py</code>, <code>index.rst</code>, <code>Makefile</code> and <code>make.bat</code>:</p>
<pre><code class="language-bash">my-wonderful-new-sphinx-project&#10;|--Pipfile&#10;|--Pipfile.lock&#10;|--source&#10;|----_static&#10;|----_templates&#10;|----conf.py&#10;|----index.rst&#10;|--Makefile&#10;|--make.bat&#10;</code></pre>
<p>You now have everything you need to start deploying your site to Cloudflare Pages. For learning how to create documentation with Sphinx, refer to the official <a href="https://www.sphinx-doc.org/en/master/usage/quickstart.html">Sphinx documentation</a>.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="creating-a-github-repository">Creating a GitHub repository</h2>
<p>In a separate terminal window that is not within the pipenv shell session, verify that SSH key-based authentication is working:</p>
<pre><code class="language-sh">eval &quot;$(ssh-agent)&quot;&#10;ssh-add -T ~/.ssh/id_rsa.pub&#10;ssh -T git@github.com&#10;</code></pre>
<pre><code class="language-sh">&#10;The authenticity of host &#x27;github.com (140.82.113.4)&#x27; can&#x27;t be established.&#10;RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.&#10;Are you sure you want to continue connecting (yes/no/[fingerprint])? yes&#10;Warning: Permanently added &#x27;github.com,140.82.113.4&#x27; (RSA) to the list of known hosts.&#10;Hi yourgithubusername! You&#x27;ve successfully authenticated, but GitHub does not provide shell access.&#10;</code></pre>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After your repository is set up, push your application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git init&#10;git config user.name &quot;Your Name&quot;&#10;git config user.email &quot;username@domain.com&quot;&#10;git remote add origin git@github.com:yourgithubusername/githubrepo.git&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<p>To deploy your site to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application**.
3. Select the **Pages** tab.
4. Select **Import an existing Git repository**.
5. Select the new GitHub repository that you created and then select **Begin setup**.
6. In the **Set up builds and deployments** section, provide the following information:
<div>
<table>
<thead>
<tr>
<th>Configuration option</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Production branch</td>
<td><code>main</code></td>
</tr>
<tr>
<td>Build command</td>
<td><code>make html</code></td>
</tr>
<tr>
<td>Build directory</td>
<td><code>build/html</code></td>
</tr>
</tbody>
</table>
</div>
<p>Below the configuration, make sure to set the environment variable for specifying the <code>PYTHON_VERSION</code>.</p>
<p>For example:</p>
<div>
<table>
<thead>
<tr>
<th>Variable name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>PYTHON_VERSION</td>
<td>3.7</td>
</tr>
</tbody>
</table>
</div>
<p>After configuring your site, you can begin your first deploy. You should see Cloudflare Pages installing <code>Pipenv</code>, your project dependencies, and building your site, before deployment.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11027.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>. Every time you commit new code to your Sphinx site, Cloudflare Pages will automatically rebuild your project and deploy it.</p>
<p>You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Sphinx site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
