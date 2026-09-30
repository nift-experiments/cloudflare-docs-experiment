<p>Members of the Cloudflare developer community and broader developer ecosystem have built and/or contributed tooling — including ORMs (Object Relational Mapper) libraries, query builders, and CLI tools — that build on top of D1.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7338.md")
</aside>
<h2 id="projects">Projects</h2>
<h3 id="sutando-orm">Sutando ORM</h3>
<p>Sutando is an ORM designed for Node.js. With Sutando, each table in a database has a corresponding model that handles CRUD (Create, Read, Update, Delete) operations.</p>
<ul>
<li><a href="https://github.com/sutandojs/sutando">GitHub</a></li>
<li><a href="https://github.com/sutandojs/sutando-examples/tree/main/typescript/rest-hono-cf-d1">D1 with Sutando ORM Example</a></li>
</ul>
<h3 id="knex-cloudflare-d1">knex-cloudflare-d1</h3>
<p>knex-cloudflare-d1 is the Cloudflare D1 dialect for Knex.js. Note that this is not an official dialect provided by Knex.js.</p>
<ul>
<li><a href="https://github.com/kiddyuchina/knex-cloudflare-d1">GitHub</a></li>
</ul>
<h3 id="prisma-orm">Prisma ORM</h3>
<p><a href="https://www.prisma.io/orm">Prisma ORM</a> is a next-generation JavaScript and TypeScript ORM that unlocks a new level of developer experience when working with databases thanks to its intuitive data model, automated migrations, type-safety and auto-completion.</p>
<ul>
<li><a href="/d1/tutorials/d1-and-prisma-orm/">Tutorial</a></li>
<li><a href="https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare#d1">Docs</a></li>
</ul>
<h3 id="d1-adapter-for-kysely-orm">D1 adapter for Kysely ORM</h3>
<p>Kysely is a type-safe and autocompletion-friendly typescript SQL query builder. With this adapter you can interact with D1 with the familiar Kysely interface.</p>
<ul>
<li><a href="https://github.com/koskimas/kysely">Kysely GitHub</a></li>
<li><a href="https://github.com/aidenwallis/kysely-d1">D1 adapter</a></li>
</ul>
<h3 id="feathers-kysely">feathers-kysely</h3>
<p>The <code>feathers-kysely</code> database adapter follows the FeathersJS Query Syntax standard and works with any framework. It is built on the D1 adapter for Kysely and supports passing queries directly from client applications. Since the FeathersJS query syntax is a subset of MongoDB's syntax, this is a great tool for MongoDB users to use Cloudflare D1 without previous SQL experience.</p>
<ul>
<li><a href="https://www.npmjs.com/package/feathers-kysely">feathers-kysely on npm</a></li>
<li><a href="https://github.com/marshallswain/feathers-kysely">feathers-kysely on GitHub</a></li>
</ul>
<h3 id="drizzle-orm">Drizzle ORM</h3>
<p>Drizzle is a headless TypeScript ORM with a head which runs on Node, Bun and Deno. Drizzle ORM lives on the Edge and it is a JavaScript ORM too. It comes with a drizzle-kit CLI companion for automatic SQL migrations generation. Drizzle automatically generates your D1 schema based on types you define in TypeScript, and exposes an API that allows you to query your database directly.</p>
<ul>
<li><a href="https://orm.drizzle.team/docs">Docs</a></li>
<li><a href="https://github.com/drizzle-team/drizzle-orm">GitHub</a></li>
<li><a href="https://orm.drizzle.team/docs/connect-cloudflare-d1">D1 example</a></li>
</ul>
<h3 id="workers-qb">workers-qb</h3>
<p><code>workers-qb</code> is a zero-dependency query builder that provides a simple standardized interface while keeping the benefits and speed of using raw queries over a traditional ORM. While not intended to provide ORM-like functionality, <code>workers-qb</code> makes it easier to interact with your database from code for direct SQL access.</p>
<ul>
<li><a href="https://github.com/G4brym/workers-qb">GitHub</a></li>
<li><a href="https://workers-qb.massadas.com/">Documentation</a></li>
</ul>
<h3 id="d1-console">d1-console</h3>
<p>Instead of running the <code>wrangler d1 execute</code> command in your terminal every time you want to interact with your database, you can interact with D1 from within the <code>d1-console</code>. Created by a Discord Community Champion, this gives the benefit of executing multi-line queries, obtaining command history, and viewing a cleanly formatted table output.</p>
<ul>
<li><a href="https://github.com/isaac-mcfadyen/d1-console">GitHub</a></li>
</ul>
<h3 id="l1">L1</h3>
<p><code>L1</code> is a package that brings some Cloudflare Worker ecosystem bindings into PHP and Laravel via the Cloudflare API. It provides interaction with D1 via PDO, KV and Queues, with more services to add in the future, making PHP integration with Cloudflare a real breeze.</p>
<ul>
<li><a href="https://github.com/renoki-co/l1">GitHub</a></li>
<li><a href="https://packagist.org/packages/renoki-co/l1">Packagist</a></li>
</ul>
<h3 id="staff-directory-a-d1-based-demo">Staff Directory - a D1-based demo</h3>
<p>Staff Directory is a demo project using D1, <a href="https://github.com/honojs/honox">HonoX</a>, and <a href="/pages/">Cloudflare Pages</a>. It uses D1 to store employee data, and is an example of a full-stack application built on top of D1.</p>
<ul>
<li><a href="https://github.com/lauragift21/staff-directory">GitHub</a></li>
<li><a href="https://github.com/lauragift21/staff-directory/blob/main/app/db.ts">D1 functionality</a></li>
</ul>
<h3 id="nuxthub">NuxtHub</h3>
<p><code>NuxtHub</code> is a Nuxt module that brings Cloudflare Worker bindings into your Nuxt application with no configuration. It leverages the <a href="/workers/wrangler/api/#getplatformproxy">Wrangler Platform Proxy</a> in development and direct binding in production to interact with <a href="/d1/">D1</a>, <a href="/kv/">KV</a> and <a href="/r2/">R2</a> with server composables (<code>hubDatabase()</code>, <code>hubKV()</code> and <code>hubBlob()</code>).</p>
<p><code>NuxtHub</code> also provides a way to use your remote D1 database in development using the <code>npx nuxt dev --remote</code> command.</p>
<ul>
<li><a href="https://github.com/nuxt-hub/core">GitHub</a></li>
<li><a href="https://hub.nuxt.com">Documentation</a></li>
<li><a href="https://github.com/Atinux/nuxt-todos-edge">Example</a></li>
</ul>
<h2 id="feedback">Feedback</h2>
<p>To report a bug or file feature requests for these community projects, create an issue directly on the project's repository.</p>
