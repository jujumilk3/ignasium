<script lang="ts">
	import Fa from 'svelte-fa';
	import { faFolder, faFolderBlank, faFolderOpen } from '@fortawesome/free-regular-svg-icons';
</script>

<svelte:head>
	<title>TestPage</title>
</svelte:head>

<div class="container test">
	<h1>Font Awsome Test</h1>
	<i class="fas fa-solid fa-house" />
	<i class="fas fa-arrow-alt-circle-down" />
	<i class="fas fa-arrow-alt-circle-down" />
	<Fa icon={faFolder} />
	<Fa icon={faFolderBlank} />
	<Fa icon={faFolderOpen} />
</div>

<style>
	.test {
		margin-top: 100px;
	}
</style>
