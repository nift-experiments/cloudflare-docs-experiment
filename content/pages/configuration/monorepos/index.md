<p>While some apps are built from a single repository, Pages also supports apps with more complex setups. A monorepo is a repository that has multiple subdirectories each containing its own application.</p>
<h2 id="set-up">Set up</h2>
<p>You can create multiple projects using the same repository, <a href="/pages/get-started/git-integration">in the same way that you would create any other Pages project</a>. You have the option to vary the build command and/or root directory of your project to tell Pages where you would like your build command to run. All project names must be unique even if connected to the same repository.</p>
<h2 id="builds">Builds</h2>
<p>When you connect a git repository to Pages, by default a change to any file in the repository will trigger a Pages build.</p>
<p><img src="/assets/upstream/images/pages/configuration/pages-path.png" alt="Monorepo example diagram" /></p>
<p>Take for example <code>my-monorepo</code> above with two associated Pages projects (<code>marketing-app</code> and <code>ecommerce-app</code>) and their listed dependencies. By default, if you change a file in the project directory for <code>marketing-app</code>, then a build for the <code>ecommerce-app</code> project will also be triggered, even though <code>ecommerce-app</code> and its dependencies have not changed. To avoid such duplicate builds, you can include and exclude both <a href="/pages/configuration/build-watch-paths">build watch paths</a> or <a href="/pages/configuration/branch-build-controls">branches</a> to specify if Pages should skip a build for a given project.</p>
<h2 id="git-integration">Git integration</h2>
<p>Once you've created a separate Pages project for each of the projects within your Git repository, each Git push will issue a new build and deployment for all connected projects unless specified in your build configuration.</p>
<p>GitHub will display separate comments for each project with the updated project and deployment URL if there is a Pull Request associated with the branch.</p>
<h3 id="github-check-runs-and-gitlab-commit-statuses">GitHub check runs and GitLab commit statuses</h3>
<p>If you have multiple projects associated with your repository, your <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks#checks">GitHub check run</a> or <a href="https://docs.gitlab.com/ee/user/project/merge_requests/status_checks.html">Gitlab commit status</a> will appear like the following on your repository:</p>
<p><img src="/assets/upstream/images/pages/configuration/ghcheckrun.png" alt="GitHub check run" />
<img src="/assets/upstream/images/pages/configuration/glcommitstatus.png" alt="GitLab commit status" /></p>
<p>If a build skips for any reason (i.e. CI Skip, build watch paths, or branch deployment controls), the check run/commit status will not appear.</p>
<h2 id="monorepo-management-tools">Monorepo management tools:</h2>
<p>While Pages does not provide specialized tooling for dependency management in monorepos, you may choose to bring additional tooling to help manage your repository. For simple subpackage management, you can utilize tools like <a href="https://docs.npmjs.com/cli/v8/using-npm/workspaces">npm</a>, <a href="https://pnpm.io/workspaces">pnpm</a>, and <a href="https://yarnpkg.com/features/workspaces">Yarn</a> workspaces. You can also use more powerful tools such as <a href="https://turbo.build/repo/docs">Turborepo</a>, <a href="https://nx.dev/getting-started/intro">NX</a>, or <a href="https://lerna.js.org/docs/getting-started">Lerna</a> to additionally manage dependencies and task execution.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>You must be using <a href="/pages/configuration/build-image/#v2-build-system">Build System V2</a> or later in order for monorepo support to be enabled.</li>
<li>You can configure a maximum of 5 Pages projects per repository. If you need this limit raised, contact your Cloudflare account team or use the <a href="https://docs.google.com/forms/d/e/1FAIpQLSd_fwAVOboH9SlutMonzbhCxuuuOmiU1L_I5O2CFbXf_XXMRg/viewform">Limit Increase Request Form</a>.</li>
</ul>
