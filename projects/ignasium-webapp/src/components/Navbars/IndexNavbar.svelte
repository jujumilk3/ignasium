<script lang="ts">
	import { onMount } from 'svelte';
	import IndexDropdown from '$components/Dropdowns/IndexDropdown.svelte';
	import { page } from '$app/stores';
	import { configs } from '$lib/constants/configs';

	let y: number;
	let lastY: number = 0;
	let headerHeight: number = 64; // 헤더의 높이를 픽셀 단위로 설정
	let isVisible: boolean = true;

	$: {
		if (y > lastY && y > headerHeight) {
			isVisible = false;
		} else {
			isVisible = true;
		}
		lastY = y;
	}

	onMount(() => {
		const header = document.querySelector('header');
		if (header) {
			headerHeight = header.offsetHeight;
		}
	});

	let navbarOpen = false;
	function setNavbarOpen() {
		navbarOpen = !navbarOpen;
	}
</script>

<svelte:window bind:scrollY={y} />

<nav
	class="top-0 fixed z-50 w-full flex flex-wrap items-center justify-between px-2 py-3 navbar-expand-lg transition-transform duration-300 ease-in-out
	 {$page.url.pathname === '/signin' || $page.url.pathname === '/signup' ? '' : 'bg-white shadow'}"
	style="transform: translateY({isVisible ? '0' : `-${headerHeight}px`});"
>
	<div class="container px-4 mx-auto flex flex-wrap items-center justify-between">
		<div class="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start">
			<a
				class="{$page.url.pathname === '/signin' || $page.url.pathname === '/signup'
					? 'text-white'
					: 'text-blueGray-700'} text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase"
				href="/"
			>
				{configs.PAGE_DEFAULT_TITLE}
			</a>
			<button
				class="cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
				type="button"
				on:click={setNavbarOpen}
			>
				<i class="fas fa-bars" />
			</button>
		</div>
		<div
			class="lg:flex flex-grow items-center {navbarOpen ? 'block' : 'hidden'}"
			id="example-navbar-warning"
		>
			<ul class="flex flex-col lg:flex-row list-none mr-auto">
				<li class="flex items-center">
					<a
						class="hover:text-blueGray-500 {$page.url.pathname === '/signin' ||
						$page.url.pathname === '/signup'
							? 'text-white'
							: 'text-blueGray-700'}  px-3 py-2 flex items-center text-xs uppercase font-bold"
						href="/document"
					>
						<i
							class="{$page.url.pathname === '/signin' || $page.url.pathname === '/signup'
								? 'text-white'
								: 'text-blueGray-400'} far fa-file-alt text-lg leading-lg mr-2"
						/>
						Docs
					</a>
				</li>
			</ul>
			<ul class="flex flex-col lg:flex-row list-none lg:ml-auto">
				<li class="flex items-center">
					<IndexDropdown />
				</li>
				<li class="flex items-center">
					<a href="/signin">
						<button
							class="{$page.url.pathname === '/signin' || $page.url.pathname === '/signup'
								? 'text-white active:bg-blueGray-600'
								: 'text-gray-500 active:bg-red-200'}  text-xs font-bold uppercase px-4 py-2 rounded hover:shadow-lg outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150"
							type="button"
						>
							Sign-in
						</button>
					</a>
				</li>
				<li class="flex items-center">
					<a href="/signup">
						<button
							class="bg-blueGray-200 {$page.url.pathname === '/signin' ||
							$page.url.pathname === '/signup'
								? 'text-blueGray-700 active:bg-blueGray-600'
								: 'text-gray-500 active:bg-red-200'} text-xs font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150"
							type="button"
						>
							Sign-up
						</button>
					</a>
				</li>
			</ul>
		</div>
	</div>
</nav>
