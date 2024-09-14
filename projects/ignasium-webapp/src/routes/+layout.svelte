<script lang="ts">
    import '../app.css';
    import { browserData } from '$lib/stores/browserStore';
	import { page } from '$app/stores';
    import { configs } from '$lib/constants/configs';

    // Components
    import IndexNavbar from '$components/Navbars/IndexNavbar.svelte';


	let subscribingBrowserData;
	let isAuthPage = false;

	browserData.subscribe((value) => {
		// console.log('browserData from layout.svelte');
		// console.log(value);
		subscribingBrowserData = value;
		isAuthPage = $browserData.location === 'signin' || $browserData.location === 'signup';
	});
	// console.log("below is page from layout")
	// console.log(page)

	// -> 굳이 subscribe를 하지 않아도 잘 물고 다님. 하지만 값이 변하는 걸 확인하기 위해선
	// 이 컴포넌트에서 subscribe를 해서 확인할 수 있는 것임.
	page.subscribe((value) => {
		console.log('page from layout.svelte');
		console.log(value);
		console.log($page.url.pathname.indexOf('dashboard'));
		console.log($page.url.pathname.includes('dashboard'));
	});

	// import {onMount} from 'svelte';
	// onMount(() => {
	// 	console.log('onMount from layout.svelte');
	// 	console.log($browserData);
	// 	console.log(page);
	// });
</script>



<svelte:head>
	<title>{$browserData.title || configs.PAGE_DEFAULT_TITLE}</title>
</svelte:head>

<IndexNavbar />
<slot />