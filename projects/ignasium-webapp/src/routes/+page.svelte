<script lang="ts">

import { page } from '$app/stores';
import { setBrowserLocation, setBrowserTitle } from '$lib/stores/browserStore';

console.log('below is page');
console.log($page.data);
setBrowserTitle('');
setBrowserLocation('home');
</script>


<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<h1 class="text-3xl font-bold underline">
    Hello world!
</h1>

<style lang="postcss">
:global(html) {
    background-color: cadetblue;
}
</style> 