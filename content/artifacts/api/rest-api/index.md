---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/api/rest-api/
  description: Manage Artifacts repos and tokens over HTTP.
  full_title: REST API · Artifacts · Cloudflare Artifacts docs
  head_html: <title>REST API · Artifacts · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage Artifacts repos and tokens over HTTP."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/api/rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/api/rest-api/index.md"><meta property="og:title" content="REST API · Artifacts · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage Artifacts repos and tokens over HTTP."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/api/rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/api/rest-api/#page","headline":"REST API \u00b7 Artifacts \u00b7 Cloudflare Artifacts docs","description":"Manage Artifacts repos and tokens over HTTP.","url":"https://developers.cloudflare.com/artifacts/api/rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/api/rest-api/
  schema: 1
---
<p>Use the Artifacts REST API to manage repos, remotes, forks, imports, and tokens from external systems.</p>
<p>Review <a href="/artifacts/concepts/namespaces/">Namespaces</a> first, then choose the namespace name you will use in these API paths.</p>
<h2 id="base-url-and-authentication">Base URL and authentication</h2>
<p>Artifacts REST routes use this base path:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE&#10;</code></pre>
<p>Requests use Bearer authentication:</p>
<pre tabindex="0"><code class="language-txt">Authorization: Bearer $CLOUDFLARE_API_TOKEN&#10;</code></pre>
<p>Route paths below are shown relative to <code>/accounts/$ACCOUNT_ID</code>. Curl examples use <code>ARTIFACTS_BASE_URL</code> or <code>ARTIFACTS_ACCOUNT_BASE_URL</code> to keep commands shorter.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="token-types">Token types</h3>
@markup("md", "content/.markup/bodies/3339.md")
</aside>
<p>The following examples assume:</p>
<pre tabindex="0"><code class="language-sh">export ACCOUNT_ID=&quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;&#10;export ARTIFACTS_NAMESPACE=&quot;default&quot;&#10;export ARTIFACTS_REPO=&quot;starter-repo&quot;&#10;export CLOUDFLARE_API_TOKEN=&quot;&lt;YOUR_API_TOKEN&gt;&quot;&#10;export ARTIFACTS_BASE_URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE&quot;&#10;export ARTIFACTS_ACCOUNT_BASE_URL=&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts&quot;&#10;</code></pre>
<p>All JSON responses use the standard Cloudflare v4 envelope:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Successful blob, file, and raw responses return file bytes directly instead of JSON. For example, <code>GET /artifacts/namespaces/:namespace/repos/:name/file?ref=main&amp;path=README.md</code> returns the contents of <code>README.md</code> with <code>Content-Type: application/octet-stream</code>. Error responses still use the standard envelope:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 10200,&#10;			&quot;message&quot;: &quot;File not found&quot;&#10;		}&#10;	],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Returned repo tokens are secrets. Do not log them or store them in long-lived remotes unless your workflow requires it.</p>
<h2 id="shared-types">Shared types</h2>
<pre tabindex="0"><code class="language-ts">export type NamespaceName = string;&#10;export type Jurisdiction = &quot;eu&quot; | &quot;us&quot;;&#10;export type RepoName = string;&#10;export type BranchName = string;&#10;export type Scope = &quot;read&quot; | &quot;write&quot;;&#10;export type TokenState = &quot;active&quot; | &quot;expired&quot; | &quot;revoked&quot;;&#10;export type ArtifactToken = string;&#10;export type Cursor = string;&#10;export type RepoSortField =&#10;	| &quot;created_at&quot;&#10;	| &quot;updated_at&quot;&#10;	| &quot;last_push_at&quot;&#10;	| &quot;name&quot;;&#10;export type SortDirection = &quot;asc&quot; | &quot;desc&quot;;&#10;&#10;export interface ApiError {&#10;	code: number;&#10;	message: string;&#10;	documentation_url?: string;&#10;	source?: {&#10;		pointer?: string;&#10;	};&#10;}&#10;&#10;export interface CursorResultInfo {&#10;	cursor: string;&#10;	per_page: number;&#10;	count: number;&#10;}&#10;&#10;export interface OffsetResultInfo {&#10;	page: number;&#10;	per_page: number;&#10;	total_pages: number;&#10;	count: number;&#10;	total_count: number;&#10;}&#10;&#10;export type ResultInfo = CursorResultInfo | OffsetResultInfo;&#10;&#10;export interface ApiEnvelope&lt;T&gt; {&#10;	result: T | null;&#10;	success: boolean;&#10;	errors: ApiError[];&#10;	messages: ApiError[];&#10;	result_info?: ResultInfo;&#10;}&#10;&#10;export interface RepoInfo {&#10;	id: string;&#10;	name: RepoName;&#10;	description: string | null;&#10;	default_branch: string;&#10;	created_at: string;&#10;	updated_at: string;&#10;	last_push_at: string | null;&#10;	source: string | null;&#10;	read_only: boolean;&#10;}&#10;&#10;export interface RepoWithRemote extends RepoInfo {&#10;	remote: string;&#10;}&#10;&#10;export interface TokenInfo {&#10;	id: string;&#10;	scope: Scope;&#10;	state: TokenState;&#10;	created_at: string;&#10;	expires_at: string;&#10;}&#10;</code></pre>
<h2 id="namespaces">Namespaces</h2>
<h3 id="create-a-namespace">Create a namespace</h3>
<p>Route: <code>POST /artifacts/namespaces</code></p>
<p>Use the account-level base URL.</p>
<p>Request body:</p>
<ul>
<li><code>namespace</code> <span class="nb-type">NamespaceName</span> <span class="nb-metainfo">required</span></li>
<li><code>jurisdiction</code> <span class="nb-type">eu&quot; | &quot;us</span> <span class="nb-metainfo">optional (default: unrestricted)</span></li>
</ul>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;$ARTIFACTS_ACCOUNT_BASE_URL/namespaces&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;namespace&quot;: &quot;my-eu-namespace&quot;,&#10;    &quot;jurisdiction&quot;: &quot;eu&quot;&#10;  }&#x27;&#10;</code></pre>
<p>The jurisdiction applies to every repo in the namespace and cannot be changed after creation. If you omit <code>jurisdiction</code>, Artifacts creates an unrestricted namespace.</p>
<p>For more information, refer to <a href="/artifacts/guides/data-localization/">Data localization</a>.</p>
<h3 id="list-namespaces">List namespaces</h3>
<p>Route: <code>GET /artifacts/namespaces?limit=&amp;cursor=</code></p>
<p>Use the account-level base URL.</p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_ACCOUNT_BASE_URL/namespaces?limit=20&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h3 id="get-a-namespace">Get a namespace</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace</code></p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_ACCOUNT_BASE_URL/namespaces/$ARTIFACTS_NAMESPACE&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h2 id="repos">Repos</h2>
<h3 id="create-a-repo">Create a repo</h3>
<p>Route: <code>POST /artifacts/namespaces/:namespace/repos</code></p>
<p>Request body:</p>
<ul>
<li><code>name</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span></li>
<li><code>description</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li><code>default_branch</code> <span class="nb-type">BranchName</span> <span class="nb-metainfo">optional</span></li>
<li><code>read_only</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
</ul>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface CreateRepoRequest {&#10;	name: RepoName;&#10;	description?: string;&#10;	default_branch?: BranchName;&#10;	read_only?: boolean;&#10;}&#10;&#10;export interface CreateRepoResult {&#10;	id: string;&#10;	name: RepoName;&#10;	description: string | null;&#10;	default_branch: string;&#10;	remote: string;&#10;	token: ArtifactToken;&#10;}&#10;&#10;export type CreateRepoResponse = ApiEnvelope&lt;CreateRepoResult&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;$ARTIFACTS_BASE_URL/repos&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;name&quot;: &quot;starter-repo&quot;,&#10;    &quot;description&quot;: &quot;Repository for automation experiments&quot;,&#10;    &quot;default_branch&quot;: &quot;main&quot;,&#10;    &quot;read_only&quot;: false&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;repo_123&quot;,&#10;		&quot;name&quot;: &quot;starter-repo&quot;,&#10;		&quot;description&quot;: &quot;Repository for automation experiments&quot;,&#10;		&quot;default_branch&quot;: &quot;main&quot;,&#10;		&quot;remote&quot;: &quot;https://&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/default/starter-repo.git&quot;,&#10;		&quot;token&quot;: &quot;art_v1_0123456789abcdef0123456789abcdef01234567?expires=1760000000&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Create, fork, and import responses return the token string only. The token encodes its expiry directly in the <code>?expires=</code> suffix. The separate <code>POST /tokens</code> route also returns <code>expires_at</code> alongside the plaintext token.</p>
<h3 id="list-repos">List repos</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos?limit=&amp;cursor=&amp;search=&amp;sort=&amp;direction=</code></p>
<p>Query parameters:</p>
<ul>
<li><code>limit</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional (default: 50, max: 200)</span></li>
<li><code>cursor</code> <span class="nb-type">Cursor</span> <span class="nb-metainfo">optional</span></li>
<li><code>search</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li><code>sort</code> <span class="nb-type">created_at&quot; | &quot;updated_at&quot; | &quot;last_push_at&quot; | &quot;name</span> <span class="nb-metainfo">optional (default: &quot;created_at&quot;)</span></li>
<li><code>direction</code> <span class="nb-type">asc&quot; | &quot;desc</span> <span class="nb-metainfo">optional (default: &quot;desc&quot;)</span></li>
</ul>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface ListReposQuery {&#10;	limit?: number;&#10;	cursor?: Cursor;&#10;	search?: string;&#10;	sort?: RepoSortField;&#10;	direction?: SortDirection;&#10;}&#10;&#10;export type ListReposResponse = ApiEnvelope&lt;RepoWithRemote[]&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl &quot;$ARTIFACTS_BASE_URL/repos?limit=20&amp;sort=updated_at&amp;direction=desc&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;repo_123&quot;,&#10;			&quot;name&quot;: &quot;starter-repo&quot;,&#10;			&quot;description&quot;: &quot;Repository for automation experiments&quot;,&#10;			&quot;default_branch&quot;: &quot;main&quot;,&#10;			&quot;created_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;			&quot;updated_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;			&quot;last_push_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;			&quot;source&quot;: null,&#10;			&quot;read_only&quot;: false,&#10;			&quot;remote&quot;: &quot;https://&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/default/starter-repo.git&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;cursor&quot;: &quot;next-cursor&quot;,&#10;		&quot;per_page&quot;: 20,&#10;		&quot;count&quot;: 1&#10;	}&#10;}&#10;</code></pre>
<h3 id="get-a-repo">Get a repo</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name</code></p>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export type GetRepoResponse = ApiEnvelope&lt;RepoWithRemote&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;repo_123&quot;,&#10;		&quot;name&quot;: &quot;starter-repo&quot;,&#10;		&quot;description&quot;: &quot;Repository for automation experiments&quot;,&#10;		&quot;default_branch&quot;: &quot;main&quot;,&#10;		&quot;created_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;		&quot;updated_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;		&quot;last_push_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;		&quot;source&quot;: null,&#10;		&quot;read_only&quot;: false,&#10;		&quot;remote&quot;: &quot;https://&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/default/starter-repo.git&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="delete-a-repo">Delete a repo</h3>
<p>Route: <code>DELETE /artifacts/namespaces/:namespace/repos/:name</code></p>
<p>This route returns <code>202 Accepted</code>.</p>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface DeleteRepoResult {&#10;	id: string;&#10;}&#10;&#10;export type DeleteRepoResponse = ApiEnvelope&lt;DeleteRepoResult&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl --request DELETE &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;repo_123&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="fork-a-repo">Fork a repo</h3>
<p>Route: <code>POST /artifacts/namespaces/:namespace/repos/:name/fork</code></p>
<p>Request body:</p>
<ul>
<li><code>name</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span></li>
<li><code>description</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li><code>read_only</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
<li><code>default_branch_only</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
</ul>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface ForkRepoRequest {&#10;	name: RepoName;&#10;	description?: string;&#10;	read_only?: boolean;&#10;	default_branch_only?: boolean;&#10;}&#10;&#10;export interface ForkRepoResult extends CreateRepoResult {&#10;	objects: number;&#10;}&#10;&#10;export type ForkRepoResponse = ApiEnvelope&lt;ForkRepoResult&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/fork&quot; \&#10;	&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;	&#45;-header &quot;Content-Type: application/json&quot; \&#10;	&#45;-data &#x27;{&#10;	  &quot;name&quot;: &quot;starter-repo-copy&quot;,&#10;	  &quot;description&quot;: &quot;Fork for testing&quot;,&#10;	  &quot;read_only&quot;: false,&#10;	  &quot;default_branch_only&quot;: true&#10;	}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;repo_456&quot;,&#10;		&quot;name&quot;: &quot;starter-repo-copy&quot;,&#10;		&quot;description&quot;: &quot;Repository for automation experiments&quot;,&#10;		&quot;default_branch&quot;: &quot;main&quot;,&#10;		&quot;remote&quot;: &quot;https://&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/default/starter-repo-copy.git&quot;,&#10;		&quot;token&quot;: &quot;art_v1_89abcdef0123456789abcdef0123456789abcdef?expires=1760003600&quot;,&#10;		&quot;objects&quot;: 128&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="import-a-public-https-remote">Import a public HTTPS remote</h3>
<p>Route: <code>POST /artifacts/namespaces/:namespace/repos/:name/import</code></p>
<p>Request body:</p>
<ul>
<li><code>url</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></li>
<li><code>branch</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
<li><code>depth</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></li>
<li><code>read_only</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></li>
</ul>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface ImportRepoRequest {&#10;	url: string;&#10;	branch?: string;&#10;	depth?: number;&#10;	read_only?: boolean;&#10;}&#10;&#10;export type ImportRepoResponse = ApiEnvelope&lt;CreateRepoResult&gt;;&#10;</code></pre>
<p>Pass a full HTTPS Git remote URL, for example <code>https://github.com/facebook/react</code> or <code>https://gitlab.com/group/project.git</code>.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;$ARTIFACTS_BASE_URL/repos/react-mirror/import&quot; \&#10;	&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;	&#45;-header &quot;Content-Type: application/json&quot; \&#10;	&#45;-data &#x27;{&#10;	  &quot;url&quot;: &quot;https://github.com/facebook/react&quot;,&#10;	  &quot;branch&quot;: &quot;main&quot;,&#10;	  &quot;depth&quot;: 100&#10;	}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;repo_789&quot;,&#10;		&quot;name&quot;: &quot;react-mirror&quot;,&#10;		&quot;description&quot;: null,&#10;		&quot;default_branch&quot;: &quot;main&quot;,&#10;		&quot;remote&quot;: &quot;https://&lt;ACCOUNT_ID&gt;.artifacts.cloudflare.net/git/default/react-mirror.git&quot;,&#10;		&quot;token&quot;: &quot;art_v1_fedcba9876543210fedcba9876543210fedcba98?expires=1760007200&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>If a repo exists but is still importing or forking, this route can return <code>409 Conflict</code> with a retriable error message.</p>
<h2 id="repo-content">Repo content</h2>
<p>These routes read Git objects and files from an existing repo. Object routes use immutable Git SHA-1 hashes. File routes resolve a path at a branch, tag, or commit hash.</p>
<h3 id="read-commit-history">Read commit history</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name/log?ref=&amp;limit=&amp;offset=</code></p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/log?ref=main&amp;limit=10&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h3 id="read-a-commit">Read a commit</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name/commit/:hash</code></p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/commit/$COMMIT_HASH&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h3 id="read-a-tree">Read a tree</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name/tree/:hash</code></p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/tree/$TREE_HASH&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h3 id="read-a-blob">Read a blob</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name/blob/:hash</code></p>
<p>Returns raw blob bytes.</p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/blob/$BLOB_HASH&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h3 id="read-a-file">Read a file</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name/file?ref=&amp;path=</code></p>
<p>Returns raw file bytes as <code>application/octet-stream</code>.</p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/file?ref=main&amp;path=README.md&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h3 id="read-a-raw-file">Read a raw file</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name/raw/:ref/:path</code></p>
<p>Returns file bytes with a sniffed <code>Content-Type</code>.</p>
<pre tabindex="0"><code class="language-sh">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/raw/main/README.md&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h2 id="tokens">Tokens</h2>
<p>These tokens are for Git routes. They do not authenticate REST API requests.</p>
<h3 id="list-tokens-for-a-repo">List tokens for a repo</h3>
<p>Route: <code>GET /artifacts/namespaces/:namespace/repos/:name/tokens?state=&amp;per_page=&amp;page=</code></p>
<p>Query parameters:</p>
<ul>
<li><code>state</code> <span class="nb-type">active&quot; | &quot;expired&quot; | &quot;revoked&quot; | &quot;all</span> <span class="nb-metainfo">optional (default: &quot;active&quot;)</span></li>
<li><code>per_page</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional (default: 30, max: 100)</span></li>
<li><code>page</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional (default: 1)</span></li>
</ul>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface ListTokensQuery {&#10;	state?: TokenState | &quot;all&quot;;&#10;	per_page?: number;&#10;	page?: number;&#10;}&#10;&#10;export type ListTokensResponse = ApiEnvelope&lt;TokenInfo[]&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl &quot;$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO/tokens?state=all&amp;per_page=30&amp;page=1&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;0123456789abcdef&quot;,&#10;			&quot;scope&quot;: &quot;read&quot;,&#10;			&quot;state&quot;: &quot;active&quot;,&#10;			&quot;created_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;,&#10;			&quot;expires_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;&#10;		}&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result_info&quot;: {&#10;		&quot;page&quot;: 1,&#10;		&quot;per_page&quot;: 30,&#10;		&quot;total_pages&quot;: 1,&#10;		&quot;count&quot;: 1,&#10;		&quot;total_count&quot;: 1&#10;	}&#10;}&#10;</code></pre>
<h3 id="create-a-token">Create a token</h3>
<p>Route: <code>POST /artifacts/namespaces/:namespace/tokens</code></p>
<p>Request body:</p>
<ul>
<li><code>repo</code> <span class="nb-type">RepoName</span> <span class="nb-metainfo">required</span></li>
<li><code>scope</code> <span class="nb-type">read&quot; | &quot;write</span> <span class="nb-metainfo">optional (default: &quot;write&quot;)</span></li>
<li><code>ttl</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span> — Token time-to-live in seconds. Minimum 60 (1 minute), maximum 31,536,000 (1 year). Defaults to 86,400 (24 hours).</li>
</ul>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface CreateTokenRequest {&#10;	repo: RepoName;&#10;	scope?: Scope;&#10;	ttl?: number;&#10;}&#10;&#10;export interface CreateTokenResult {&#10;	id: string;&#10;	plaintext: ArtifactToken;&#10;	scope: Scope;&#10;	expires_at: string;&#10;}&#10;&#10;export type CreateTokenResponse = ApiEnvelope&lt;CreateTokenResult&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;$ARTIFACTS_BASE_URL/tokens&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;repo&quot;: &quot;starter-repo&quot;,&#10;    &quot;scope&quot;: &quot;read&quot;,&#10;    &quot;ttl&quot;: 3600&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;0123456789abcdef&quot;,&#10;		&quot;plaintext&quot;: &quot;art_v1_0123456789abcdef0123456789abcdef01234567?expires=1760000000&quot;,&#10;		&quot;scope&quot;: &quot;read&quot;,&#10;		&quot;expires_at&quot;: &quot;&lt;ISO_TIMESTAMP&gt;&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="revoke-a-token">Revoke a token</h3>
<p>Route: <code>DELETE /artifacts/namespaces/:namespace/tokens/:id</code></p>
<p>Response type:</p>
<pre tabindex="0"><code class="language-ts">export interface DeleteTokenResult {&#10;	id: string;&#10;}&#10;&#10;export type DeleteTokenResponse = ApiEnvelope&lt;DeleteTokenResult&gt;;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">curl --request DELETE &quot;$ARTIFACTS_BASE_URL/tokens/0123456789abcdef&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;0123456789abcdef&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="errors">Errors</h2>
<p>Application errors also use the v4 envelope:</p>
<pre tabindex="0"><code class="language-ts">export interface ApiError {&#10;	code: number;&#10;	message: string;&#10;	documentation_url?: string;&#10;	source?: {&#10;		pointer?: string;&#10;	};&#10;}&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-workers-binding-artifacts-api-workers-binding"><a href="/artifacts/api/workers-binding/">Workers binding</a></h3><p>Call the same Artifacts operations from a Worker through the Artifacts binding.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-git-protocol-artifacts-api-git-protocol"><a href="/artifacts/api/git-protocol/">Git protocol</a></h3><p>Use repo remotes and tokens with standard git-over-HTTPS tooling.</p></div>
