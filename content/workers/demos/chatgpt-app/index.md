<h2 id="deploy-your-first-chatgpt-app">Deploy your first ChatGPT App</h2>
<p>This guide will show you how to build and deploy an interactive ChatGPT App on Cloudflare Workers that can:</p>
<ul>
<li>Render rich, interactive UI widgets directly in ChatGPT conversations</li>
<li>Maintain real-time, multi-user state using Durable Objects</li>
<li>Enable bidirectional communication between your app and ChatGPT</li>
<li>Build multiplayer experiences that run entirely within ChatGPT</li>
</ul>
<p>You will build a real-time multiplayer chess game that demonstrates these capabilities. Players can start or join games, make moves on an interactive chessboard, and even ask ChatGPT for strategic advice—all without leaving the conversation.</p>
<p>Your ChatGPT App will use the <strong>Model Context Protocol (MCP)</strong> to expose tools and UI resources that ChatGPT can invoke on your behalf.</p>
<p>You can view the full code for this example <a href="https://github.com/cloudflare/agents/tree/main/openai-sdk/chess-app">here</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, you will need:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li><a href="https://nodejs.org/">Node.js</a> installed (v18 or later)</li>
<li>A <a href="https://chat.openai.com/">ChatGPT Plus or Team account</a> with developer mode enabled</li>
<li>Basic knowledge of React and TypeScript</li>
</ul>
<h2 id="1-enable-chatgpt-developer-mode"><ol>
<li>Enable ChatGPT Developer Mode</li>
</ol></h2>
<p>To use ChatGPT Apps (also called connectors), you need to enable developer mode:</p>
<ol>
<li>Open <a href="https://chat.openai.com/">ChatGPT</a>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Apps &amp; Connectors</strong> &gt; <strong>Advanced Settings</strong></li>
<li>Toggle <strong>Developer mode ON</strong></li>
</ol>
<p>Once enabled, you will be able to install custom apps during development and testing.</p>
<h2 id="2-create-your-chatgpt-app-project"><ol start="2">
<li>Create your ChatGPT App project</li>
</ol></h2>
<ol>
<li>Create a new project for your Chess App:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-chess-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-chess-app" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-chess-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-chess-app" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-chess-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-chess-app" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Navigate into your project:</li>
</ol>
<pre><code class="language-sh">cd my-chess-app&#10;</code></pre>
<ol start="3">
<li>Install the required dependencies:</li>
</ol>
<pre><code class="language-sh">npm install agents @modelcontextprotocol/sdk chess.js react react-dom react-chessboard&#10;</code></pre>
<ol start="4">
<li>Install development dependencies:</li>
</ol>
<pre><code class="language-sh">npm install -D @cloudflare/vite-plugin @vitejs/plugin-react vite vite-plugin-singlefile @types/react @types/react-dom&#10;</code></pre>
<h2 id="3-configure-your-project"><ol start="3">
<li>Configure your project</li>
</ol></h2>
<ol>
<li>Update your <code>wrangler.jsonc</code> to configure Durable Objects and assets:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16590.md")
</div>
<ol start="2">
<li>Create a <code>vite.config.ts</code> for building your React UI:</li>
</ol>
<pre><code class="language-ts">import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import react from &quot;@vitejs/plugin-react&quot;;&#10;import { defineConfig } from &quot;vite&quot;;&#10;import { viteSingleFile } from &quot;vite-plugin-singlefile&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [react(), cloudflare(), viteSingleFile()],&#10;	build: {&#10;		minify: false,&#10;	},&#10;});&#10;</code></pre>
<ol start="3">
<li>Update your <code>package.json</code> scripts:</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;dev&quot;: &quot;vite&quot;,&#10;		&quot;build&quot;: &quot;vite build&quot;,&#10;		&quot;deploy&quot;: &quot;vite build &amp;&amp; wrangler deploy&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="4-create-the-chess-game-engine"><ol start="4">
<li>Create the Chess game engine</li>
</ol></h2>
<ol>
<li>Create the game logic using Durable Objects at <code>src/chess.tsx</code>:</li>
</ol>
<pre><code class="language-tsx">import { Agent, callable, getCurrentAgent } from &quot;agents&quot;;&#10;import { Chess } from &quot;chess.js&quot;;&#10;&#10;type Color = &quot;w&quot; | &quot;b&quot;;&#10;&#10;type ConnectionState = {&#10;	playerId: string;&#10;};&#10;&#10;export type State = {&#10;	board: string;&#10;	players: { w?: string; b?: string };&#10;	status: &quot;waiting&quot; | &quot;active&quot; | &quot;mate&quot; | &quot;draw&quot; | &quot;resigned&quot;;&#10;	winner?: Color;&#10;	lastSan?: string;&#10;};&#10;&#10;export class ChessGame extends Agent&lt;Env, State&gt; {&#10;	initialState: State = {&#10;		board: new Chess().fen(),&#10;		players: {},&#10;		status: &quot;waiting&quot;,&#10;	};&#10;&#10;	game = new Chess();&#10;&#10;	constructor(&#10;		ctx: DurableObjectState,&#10;		public env: Env,&#10;	) {&#10;		super(ctx, env);&#10;		this.game.load(this.state.board);&#10;	}&#10;&#10;	private colorOf(playerId: string): Color | undefined {&#10;		const { players } = this.state;&#10;		if (players.w === playerId) return &quot;w&quot;;&#10;		if (players.b === playerId) return &quot;b&quot;;&#10;		return undefined;&#10;	}&#10;&#10;	@callable()&#10;	join(params: { playerId: string; preferred?: Color | &quot;any&quot; }) {&#10;		const { playerId, preferred = &quot;any&quot; } = params;&#10;		const { connection } = getCurrentAgent();&#10;		if (!connection) throw new Error(&quot;Not connected&quot;);&#10;&#10;		connection.setState({ playerId });&#10;		const s = this.state;&#10;&#10;		// Already seated? Return seat&#10;		const already = this.colorOf(playerId);&#10;		if (already) {&#10;			return { ok: true, role: already as Color, state: s };&#10;		}&#10;&#10;		// Choose a seat&#10;		const free: Color[] = ([&quot;w&quot;, &quot;b&quot;] as const).filter((c) =&gt; !s.players[c]);&#10;		if (free.length === 0) {&#10;			return { ok: true, role: &quot;spectator&quot; as const, state: s };&#10;		}&#10;&#10;		let seat: Color = free[0];&#10;		if (preferred === &quot;w&quot; &amp;&amp; free.includes(&quot;w&quot;)) seat = &quot;w&quot;;&#10;		if (preferred === &quot;b&quot; &amp;&amp; free.includes(&quot;b&quot;)) seat = &quot;b&quot;;&#10;&#10;		s.players[seat] = playerId;&#10;		s.status = s.players.w &amp;&amp; s.players.b ? &quot;active&quot; : &quot;waiting&quot;;&#10;		this.setState(s);&#10;		return { ok: true, role: seat, state: s };&#10;	}&#10;&#10;	@callable()&#10;	move(&#10;		move: { from: string; to: string; promotion?: string },&#10;		expectedFen?: string,&#10;	) {&#10;		if (this.state.status === &quot;waiting&quot;) {&#10;			return {&#10;				ok: false,&#10;				reason: &quot;not-in-game&quot;,&#10;				fen: this.game.fen(),&#10;				status: this.state.status,&#10;			};&#10;		}&#10;&#10;		const { connection } = getCurrentAgent();&#10;		if (!connection) throw new Error(&quot;Not connected&quot;);&#10;		const { playerId } = connection.state as ConnectionState;&#10;&#10;		const seat = this.colorOf(playerId);&#10;		if (!seat) {&#10;			return {&#10;				ok: false,&#10;				reason: &quot;not-in-game&quot;,&#10;				fen: this.game.fen(),&#10;				status: this.state.status,&#10;			};&#10;		}&#10;&#10;		if (seat !== this.game.turn()) {&#10;			return {&#10;				ok: false,&#10;				reason: &quot;not-your-turn&quot;,&#10;				fen: this.game.fen(),&#10;				status: this.state.status,&#10;			};&#10;		}&#10;&#10;		// Optimistic sync guard&#10;		if (expectedFen &amp;&amp; expectedFen !== this.game.fen()) {&#10;			return {&#10;				ok: false,&#10;				reason: &quot;stale&quot;,&#10;				fen: this.game.fen(),&#10;				status: this.state.status,&#10;			};&#10;		}&#10;&#10;		const res = this.game.move(move);&#10;		if (!res) {&#10;			return {&#10;				ok: false,&#10;				reason: &quot;illegal&quot;,&#10;				fen: this.game.fen(),&#10;				status: this.state.status,&#10;			};&#10;		}&#10;&#10;		const fen = this.game.fen();&#10;		let status: State[&quot;status&quot;] = &quot;active&quot;;&#10;		if (this.game.isCheckmate()) status = &quot;mate&quot;;&#10;		else if (this.game.isDraw()) status = &quot;draw&quot;;&#10;&#10;		this.setState({&#10;			...this.state,&#10;			board: fen,&#10;			lastSan: res.san,&#10;			status,&#10;			winner:&#10;				status === &quot;mate&quot; ? (this.game.turn() === &quot;w&quot; ? &quot;b&quot; : &quot;w&quot;) : undefined,&#10;		});&#10;&#10;		return { ok: true, fen, san: res.san, status };&#10;	}&#10;&#10;	@callable()&#10;	resign() {&#10;		const { connection } = getCurrentAgent();&#10;		if (!connection) throw new Error(&quot;Not connected&quot;);&#10;		const { playerId } = connection.state as ConnectionState;&#10;&#10;		const seat = this.colorOf(playerId);&#10;		if (!seat) return { ok: false, reason: &quot;not-in-game&quot;, state: this.state };&#10;&#10;		const winner = seat === &quot;w&quot; ? &quot;b&quot; : &quot;w&quot;;&#10;		this.setState({ ...this.state, status: &quot;resigned&quot;, winner });&#10;		return { ok: true, state: this.state };&#10;	}&#10;}&#10;</code></pre>
<h2 id="5-create-the-mcp-server-and-ui-resource"><ol start="5">
<li>Create the MCP server and UI resource</li>
</ol></h2>
<ol>
<li>Create your main worker at <code>src/index.ts</code>:</li>
</ol>
<pre><code class="language-ts">import { createMcpHandler } from &quot;agents/mcp&quot;;&#10;import { routeAgentRequest } from &quot;agents&quot;;&#10;import { McpServer } from &quot;@modelcontextprotocol/sdk/server/mcp.js&quot;;&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;const getWidgetHtml = async (host: string) =&gt; {&#10;	let html = await (await env.ASSETS.fetch(&quot;http://localhost/&quot;)).text();&#10;	html = html.replace(&#10;		&quot;&lt;!--RUNTIME_CONFIG--&gt;&quot;,&#10;		`&lt;script&gt;window.HOST = \`${host}\`;&lt;/script&gt;`,&#10;	);&#10;	return html;&#10;};&#10;&#10;function createServer() {&#10;	const server = new McpServer({ name: &quot;Chess&quot;, version: &quot;v1.0.0&quot; });&#10;&#10;	// Register a UI resource that ChatGPT can render&#10;	server.registerResource(&#10;		&quot;chess&quot;,&#10;		&quot;ui://widget/index.html&quot;,&#10;		{},&#10;		async (_uri, extra) =&gt; {&#10;			return {&#10;				contents: [&#10;					{&#10;						uri: &quot;ui://widget/index.html&quot;,&#10;						mimeType: &quot;text/html+skybridge&quot;,&#10;						text: await getWidgetHtml(&#10;							extra.requestInfo?.headers.host as string,&#10;						),&#10;					},&#10;				],&#10;			};&#10;		},&#10;	);&#10;&#10;	// Register a tool that ChatGPT can call to render the UI&#10;	server.registerTool(&#10;		&quot;playChess&quot;,&#10;		{&#10;			title: &quot;Renders a chess game menu, ready to start or join a game.&quot;,&#10;			annotations: { readOnlyHint: true },&#10;			_meta: {&#10;				&quot;openai/outputTemplate&quot;: &quot;ui://widget/index.html&quot;,&#10;				&quot;openai/toolInvocation/invoking&quot;: &quot;Opening chess widget&quot;,&#10;				&quot;openai/toolInvocation/invoked&quot;: &quot;Chess widget opened&quot;,&#10;			},&#10;		},&#10;		async (_, _extra) =&gt; {&#10;			return {&#10;				content: [&#10;					{ type: &quot;text&quot;, text: &quot;Successfully rendered chess game menu&quot; },&#10;				],&#10;			};&#10;		},&#10;	);&#10;&#10;	return server;&#10;}&#10;&#10;export default {&#10;	async fetch(req: Request, env: Env, ctx: ExecutionContext) {&#10;		const url = new URL(req.url);&#10;		if (url.pathname.startsWith(&quot;/mcp&quot;)) {&#10;			// Create a new server instance per request&#10;			const server = createServer();&#10;			return createMcpHandler(server)(req, env, ctx);&#10;		}&#10;&#10;		return (&#10;			(await routeAgentRequest(req, env)) ??&#10;			new Response(&quot;Not found&quot;, { status: 404 })&#10;		);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;&#10;export { ChessGame } from &quot;./chess&quot;;&#10;</code></pre>
<h2 id="6-build-the-react-ui"><ol start="6">
<li>Build the React UI</li>
</ol></h2>
<ol>
<li>Create the HTML entry point at <code>index.html</code>:</li>
</ol>
<pre><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;!--RUNTIME_CONFIG--&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;div id=&quot;root&quot; style=&quot;font-family: verdana&quot;&gt;&lt;/div&gt;&#10;		&lt;script type=&quot;module&quot; src=&quot;/src/app.tsx&quot;&gt;&lt;/script&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<ol start="2">
<li>Create the React app at <code>src/app.tsx</code>:</li>
</ol>
<pre><code class="language-tsx">import { useEffect, useRef, useState } from &quot;react&quot;;&#10;import { useAgent } from &quot;agents/react&quot;;&#10;import { createRoot } from &quot;react-dom/client&quot;;&#10;import { Chess, type Square } from &quot;chess.js&quot;;&#10;import { Chessboard, type PieceDropHandlerArgs } from &quot;react-chessboard&quot;;&#10;import type { State as ServerState } from &quot;./chess&quot;;&#10;&#10;function usePlayerId() {&#10;	const [pid] = useState(() =&gt; {&#10;		const existing = localStorage.getItem(&quot;playerId&quot;);&#10;		if (existing) return existing;&#10;		const id = crypto.randomUUID();&#10;		localStorage.setItem(&quot;playerId&quot;, id);&#10;		return id;&#10;	});&#10;	return pid;&#10;}&#10;&#10;function App() {&#10;	const playerId = usePlayerId();&#10;	const [gameId, setGameId] = useState&lt;string | null&gt;(null);&#10;	const [gameIdInput, setGameIdInput] = useState(&quot;&quot;);&#10;	const [menuError, setMenuError] = useState&lt;string | null&gt;(null);&#10;&#10;	const gameRef = useRef(new Chess());&#10;	const [fen, setFen] = useState(gameRef.current.fen());&#10;	const [myColor, setMyColor] = useState&lt;&quot;w&quot; | &quot;b&quot; | &quot;spectator&quot;&gt;(&quot;spectator&quot;);&#10;	const [pending, setPending] = useState(false);&#10;	const [serverState, setServerState] = useState&lt;ServerState | null&gt;(null);&#10;	const [joined, setJoined] = useState(false);&#10;&#10;	const host = window.HOST ?? &quot;http://localhost:5173/&quot;;&#10;&#10;	const { stub } = useAgent&lt;ServerState&gt;({&#10;		host,&#10;		name: gameId ?? &quot;__lobby__&quot;,&#10;		agent: &quot;chess&quot;,&#10;		onStateUpdate: (s) =&gt; {&#10;			if (!gameId) return;&#10;			gameRef.current.load(s.board);&#10;			setFen(s.board);&#10;			setServerState(s);&#10;		},&#10;	});&#10;&#10;	useEffect(() =&gt; {&#10;		if (!gameId || joined) return;&#10;&#10;		(async () =&gt; {&#10;			try {&#10;				const res = await stub.join({ playerId, preferred: &quot;any&quot; });&#10;				if (!res?.ok) return;&#10;&#10;				setMyColor(res.role);&#10;				gameRef.current.load(res.state.board);&#10;				setFen(res.state.board);&#10;				setServerState(res.state);&#10;				setJoined(true);&#10;			} catch (error) {&#10;				console.error(&quot;Failed to join game&quot;, error);&#10;			}&#10;		})();&#10;	}, [playerId, gameId, stub, joined]);&#10;&#10;	async function handleStartNewGame() {&#10;		const newId = crypto.randomUUID();&#10;		setGameId(newId);&#10;		setGameIdInput(newId);&#10;		setMenuError(null);&#10;		setJoined(false);&#10;	}&#10;&#10;	async function handleJoinGame() {&#10;		const trimmed = gameIdInput.trim();&#10;		if (!trimmed) {&#10;			setMenuError(&quot;Enter a game ID to join.&quot;);&#10;			return;&#10;		}&#10;		setGameId(trimmed);&#10;		setMenuError(null);&#10;		setJoined(false);&#10;	}&#10;&#10;	const handleHelpClick = () =&gt; {&#10;		window.openai?.sendFollowUpMessage?.({&#10;			prompt: `Help me with my chess game. I am playing as ${myColor} and the board is: ${fen}. Please only offer written advice.`,&#10;		});&#10;	};&#10;&#10;	function onPieceDrop({ sourceSquare, targetSquare }: PieceDropHandlerArgs) {&#10;		if (!gameId || !sourceSquare || !targetSquare || pending) return false;&#10;&#10;		const game = gameRef.current;&#10;		if (myColor === &quot;spectator&quot; || game.turn() !== myColor) return false;&#10;&#10;		const piece = game.get(sourceSquare as Square);&#10;		if (!piece || piece.color !== myColor) return false;&#10;&#10;		const prevFen = game.fen();&#10;&#10;		try {&#10;			const local = game.move({&#10;				from: sourceSquare,&#10;				to: targetSquare,&#10;				promotion: &quot;q&quot;,&#10;			});&#10;			if (!local) return false;&#10;		} catch {&#10;			return false;&#10;		}&#10;&#10;		const nextFen = game.fen();&#10;		setFen(nextFen);&#10;		setPending(true);&#10;&#10;		stub&#10;			.move({ from: sourceSquare, to: targetSquare, promotion: &quot;q&quot; }, prevFen)&#10;			.then((r) =&gt; {&#10;				if (!r.ok) {&#10;					game.load(r.fen);&#10;					setFen(r.fen);&#10;				}&#10;			})&#10;			.finally(() =&gt; setPending(false));&#10;&#10;		return true;&#10;	}&#10;&#10;	return (&#10;		&lt;div style={{ padding: &quot;20px&quot;, background: &quot;#f8fafc&quot;, minHeight: &quot;100vh&quot; }}&gt;&#10;			{!gameId ? (&#10;				&lt;div&#10;					style={{&#10;						maxWidth: &quot;420px&quot;,&#10;						margin: &quot;0 auto&quot;,&#10;						background: &quot;#fff&quot;,&#10;						borderRadius: &quot;16px&quot;,&#10;						padding: &quot;24px&quot;,&#10;					}}&#10;				&gt;&#10;					&lt;h1&gt;Ready to play?&lt;/h1&gt;&#10;					&lt;p&gt;Start a new match or join an existing game.&lt;/p&gt;&#10;					&lt;button&#10;						onClick={handleStartNewGame}&#10;						style={{&#10;							padding: &quot;12px&quot;,&#10;							background: &quot;#2563eb&quot;,&#10;							color: &quot;#fff&quot;,&#10;							border: &quot;none&quot;,&#10;							borderRadius: &quot;8px&quot;,&#10;							cursor: &quot;pointer&quot;,&#10;							width: &quot;100%&quot;,&#10;						}}&#10;					&gt;&#10;						Start a new game&#10;					&lt;/button&gt;&#10;					&lt;div style={{ marginTop: &quot;16px&quot; }}&gt;&#10;						&lt;input&#10;							placeholder=&quot;Paste a game ID&quot;&#10;							value={gameIdInput}&#10;							onChange={(e) =&gt; setGameIdInput(e.target.value)}&#10;							style={{&#10;								width: &quot;100%&quot;,&#10;								padding: &quot;10px&quot;,&#10;								borderRadius: &quot;8px&quot;,&#10;								border: &quot;1px solid #ccc&quot;,&#10;							}}&#10;						/&gt;&#10;						&lt;button&#10;							onClick={handleJoinGame}&#10;							style={{&#10;								marginTop: &quot;8px&quot;,&#10;								padding: &quot;10px&quot;,&#10;								background: &quot;#0f172a&quot;,&#10;								color: &quot;#fff&quot;,&#10;								border: &quot;none&quot;,&#10;								borderRadius: &quot;8px&quot;,&#10;								cursor: &quot;pointer&quot;,&#10;								width: &quot;100%&quot;,&#10;							}}&#10;						&gt;&#10;							Join&#10;						&lt;/button&gt;&#10;						{menuError &amp;&amp; (&#10;							&lt;p style={{ color: &quot;red&quot;, fontSize: &quot;0.85rem&quot; }}&gt;{menuError}&lt;/p&gt;&#10;						)}&#10;					&lt;/div&gt;&#10;				&lt;/div&gt;&#10;			) : (&#10;				&lt;div style={{ maxWidth: &quot;600px&quot;, margin: &quot;0 auto&quot; }}&gt;&#10;					&lt;div&#10;						style={{&#10;							background: &quot;#fff&quot;,&#10;							padding: &quot;16px&quot;,&#10;							borderRadius: &quot;16px&quot;,&#10;							marginBottom: &quot;16px&quot;,&#10;						}}&#10;					&gt;&#10;						&lt;h2&gt;Game {gameId}&lt;/h2&gt;&#10;						&lt;p&gt;Status: {serverState?.status}&lt;/p&gt;&#10;						&lt;button&#10;							onClick={handleHelpClick}&#10;							style={{&#10;								padding: &quot;10px&quot;,&#10;								background: &quot;#2563eb&quot;,&#10;								color: &quot;#fff&quot;,&#10;								border: &quot;none&quot;,&#10;								borderRadius: &quot;8px&quot;,&#10;								cursor: &quot;pointer&quot;,&#10;							}}&#10;						&gt;&#10;							Ask for help&#10;						&lt;/button&gt;&#10;					&lt;/div&gt;&#10;					&lt;div&#10;						style={{&#10;							background: &quot;#fff&quot;,&#10;							padding: &quot;16px&quot;,&#10;							borderRadius: &quot;16px&quot;,&#10;						}}&#10;					&gt;&#10;						&lt;Chessboard&#10;							position={fen}&#10;							onPieceDrop={onPieceDrop}&#10;							boardOrientation={myColor === &quot;b&quot; ? &quot;black&quot; : &quot;white&quot;}&#10;						/&gt;&#10;					&lt;/div&gt;&#10;				&lt;/div&gt;&#10;			)}&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;&#10;const root = createRoot(document.getElementById(&quot;root&quot;)!);&#10;root.render(&lt;App /&gt;);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16589.md")
</aside>
<h2 id="7-build-and-deploy"><ol start="7">
<li>Build and deploy</li>
</ol></h2>
<ol>
<li>Build your React UI:</li>
</ol>
<pre><code class="language-sh">npm run build&#10;</code></pre>
<p>This compiles your React app into a single HTML file in the <code>dist</code> directory.</p>
<ol start="2">
<li>Deploy to Cloudflare:</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>After deployment, you will see your app URL:</p>
<pre><code>https://my-chess-app.YOUR_SUBDOMAIN.workers.dev&#10;</code></pre>
<h2 id="8-connect-to-chatgpt"><ol start="8">
<li>Connect to ChatGPT</li>
</ol></h2>
<p>Now connect your deployed app to ChatGPT:</p>
<ol>
<li>Open <a href="https://chat.openai.com/">ChatGPT</a>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Apps &amp; Connectors</strong> &gt; <strong>Create</strong></li>
<li>Give your app a <strong>name</strong>, and optionally a <strong>description</strong> and <strong>icon</strong>.</li>
<li>Enter your MCP endpoint: <code>https://my-chess-app.YOUR_SUBDOMAIN.workers.dev/mcp</code>.</li>
<li>Select <strong>&quot;No authentication&quot;</strong>.</li>
<li>Select <strong>&quot;Create&quot;</strong>.</li>
</ol>
<h2 id="9-play-chess-in-chatgpt"><ol start="9">
<li>Play chess in ChatGPT</li>
</ol></h2>
<p>Try it out:</p>
<ol>
<li>In your ChatGPT conversation, type: &quot;Let's play chess&quot;.</li>
<li>ChatGPT will call the <code>playChess</code> tool and render your interactive chess widget.</li>
<li>Select <strong>&quot;Start a new game&quot;</strong> to create a game.</li>
<li>Share the game ID with a friend who can join via their own ChatGPT conversation.</li>
<li>Make moves by dragging pieces on the board.</li>
<li>Select <strong>&quot;Ask for help&quot;</strong> to get strategic advice from ChatGPT</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16588.md")
</aside>
<h2 id="key-concepts">Key concepts</h2>
<h3 id="mcp-server">MCP Server</h3>
<p>The Model Context Protocol (MCP) server defines tools and resources that ChatGPT can access. Note that we create a new server instance per request to prevent cross-client response leakage:</p>
<pre><code class="language-ts">function createServer() {&#10;	const server = new McpServer({ name: &quot;Chess&quot;, version: &quot;v1.0.0&quot; });&#10;&#10;	// Register a UI resource that ChatGPT can render&#10;	server.registerResource(&#10;		&quot;chess&quot;,&#10;		&quot;ui://widget/index.html&quot;,&#10;		{},&#10;		async (_uri, extra) =&gt; {&#10;			return {&#10;				contents: [&#10;					{&#10;						uri: &quot;ui://widget/index.html&quot;,&#10;						mimeType: &quot;text/html+skybridge&quot;,&#10;						text: await getWidgetHtml(&#10;							extra.requestInfo?.headers.host as string,&#10;						),&#10;					},&#10;				],&#10;			};&#10;		},&#10;	);&#10;&#10;	// Register a tool that ChatGPT can call to render the UI&#10;	server.registerTool(&#10;		&quot;playChess&quot;,&#10;		{&#10;			title: &quot;Renders a chess game menu, ready to start or join a game.&quot;,&#10;			annotations: { readOnlyHint: true },&#10;			_meta: {&#10;				&quot;openai/outputTemplate&quot;: &quot;ui://widget/index.html&quot;,&#10;				&quot;openai/toolInvocation/invoking&quot;: &quot;Opening chess widget&quot;,&#10;				&quot;openai/toolInvocation/invoked&quot;: &quot;Chess widget opened&quot;,&#10;			},&#10;		},&#10;		async (_, _extra) =&gt; {&#10;			return {&#10;				content: [&#10;					{ type: &quot;text&quot;, text: &quot;Successfully rendered chess game menu&quot; },&#10;				],&#10;			};&#10;		},&#10;	);&#10;&#10;	return server;&#10;}&#10;</code></pre>
<h3 id="game-engine-with-agents">Game Engine with Agents</h3>
<p>The <code>ChessGame</code> class extends <code>Agent</code> to create a stateful game engine:</p>
<pre><code class="language-tsx">export class ChessGame extends Agent&lt;Env, State&gt; {&#10;  initialState: State = {&#10;    board: new Chess().fen(),&#10;    players: {},&#10;    status: &quot;waiting&quot;&#10;  };&#10;&#10;  game = new Chess();&#10;&#10;  constructor(&#10;    ctx: DurableObjectState,&#10;    public env: Env&#10;  ) {&#10;    super(ctx, env);&#10;    this.game.load(this.state.board);&#10;  }&#10;</code></pre>
<p>Each game gets its own Agent instance, enabling:</p>
<ul>
<li><strong>Isolated state</strong> per game</li>
<li><strong>Real-time synchronization</strong> across players</li>
<li><strong>Persistent storage</strong> that survives worker restarts</li>
</ul>
<h3 id="callable-methods">Callable methods</h3>
<p>Use the <code>@callable()</code> decorator to expose methods that clients can invoke:</p>
<pre><code class="language-ts">@callable()&#10;join(params: { playerId: string; preferred?: Color | &quot;any&quot; }) {&#10;  const { playerId, preferred = &quot;any&quot; } = params;&#10;  const { connection } = getCurrentAgent();&#10;  if (!connection) throw new Error(&quot;Not connected&quot;);&#10;&#10;  connection.setState({ playerId });&#10;  const s = this.state;&#10;&#10;  // Already seated? Return seat&#10;  const already = this.colorOf(playerId);&#10;  if (already) {&#10;    return { ok: true, role: already as Color, state: s };&#10;  }&#10;&#10;  // Choose a seat&#10;  const free: Color[] = ([&quot;w&quot;, &quot;b&quot;] as const).filter((c) =&gt; !s.players[c]);&#10;  if (free.length === 0) {&#10;    return { ok: true, role: &quot;spectator&quot; as const, state: s };&#10;  }&#10;&#10;  let seat: Color = free[0];&#10;  if (preferred === &quot;w&quot; &amp;&amp; free.includes(&quot;w&quot;)) seat = &quot;w&quot;;&#10;  if (preferred === &quot;b&quot; &amp;&amp; free.includes(&quot;b&quot;)) seat = &quot;b&quot;;&#10;&#10;  s.players[seat] = playerId;&#10;  s.status = s.players.w &amp;&amp; s.players.b ? &quot;active&quot; : &quot;waiting&quot;;&#10;  this.setState(s);&#10;  return { ok: true, role: seat, state: s };&#10;}&#10;</code></pre>
<h3 id="react-integration">React integration</h3>
<p>The <code>useAgent</code> hook connects your React app to the Durable Object:</p>
<pre><code class="language-tsx">const { stub } = useAgent&lt;ServerState&gt;({&#10;	host,&#10;	name: gameId ?? &quot;__lobby__&quot;,&#10;	agent: &quot;chess&quot;,&#10;	onStateUpdate: (s) =&gt; {&#10;		gameRef.current.load(s.board);&#10;		setFen(s.board);&#10;		setServerState(s);&#10;	},&#10;});&#10;</code></pre>
<p>Call methods on the agent:</p>
<pre><code class="language-tsx">const res = await stub.join({ playerId, preferred: &quot;any&quot; });&#10;await stub.move({ from: &quot;e2&quot;, to: &quot;e4&quot; });&#10;</code></pre>
<h3 id="bidirectional-communication">Bidirectional communication</h3>
<p>Your app can send messages to ChatGPT:</p>
<pre><code class="language-ts">const handleHelpClick = () =&gt; {&#10;	window.openai?.sendFollowUpMessage?.({&#10;		prompt: `Help me with my chess game. I am playing as ${myColor} and the board is: ${fen}. Please only offer written advice as there are no tools for you to use.`,&#10;	});&#10;};&#10;</code></pre>
<p>This creates a new message in the ChatGPT conversation with context about the current game state.</p>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have a working ChatGPT App, you can:</p>
<ul>
<li>Add more tools: Expose additional capabilities and UIs through MCP tools and resources.</li>
<li>Enhance the UI: Build more sophisticated interfaces with React.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-api-agents-runtime-agents-api">Agents API</h3><p>Complete API reference for the Agents SDK.</p></a></p>
<p><a class="nb-card nb-link-card" href="/durable-objects/"><h3 id="card-durable-objects-durable-objects">Durable Objects</h3><p>Learn about the underlying stateful infrastructure.</p></a></p>
<p><a class="nb-card nb-link-card" href="https://modelcontextprotocol.io/"><h3 id="card-model-context-protocol-https-modelcontextprotocol-io">Model Context Protocol</h3><p>MCP specification and documentation.</p></a></p>
<p><a class="nb-card nb-link-card" href="https://developers.openai.com/apps-sdk/"><h3 id="card-openai-apps-sdk-https-developers-openai-com-apps-sdk">OpenAI Apps SDK</h3><p>Official OpenAI Apps SDK reference.</p></a></p>
