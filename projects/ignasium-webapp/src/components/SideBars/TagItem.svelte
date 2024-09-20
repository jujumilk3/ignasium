<script lang="ts">
	import Fa from 'svelte-fa';
	export let tag: string;
	export let count: number;
	export let selection: 'and' | 'or' | null;
	export let onSelect: (tag: string, condition: 'and' | 'or') => void;
	export let icon: any;
</script>

<li class="flex items-center pb-1">
	<div class="w-2/12 flex justify-center">
		<input
			type="checkbox"
			class="checkbox-custom"
			checked={selection === 'and'}
			on:change={() => onSelect(tag, 'and')}
		/>
	</div>
	<div class="w-2/12 flex justify-center">
		<input
			type="checkbox"
			class="checkbox-custom"
			checked={selection === 'or'}
			on:change={() => onSelect(tag, 'or')}
		/>
	</div>
	<div class="w-8/12 pl-2 flex items-center">
		<button type="button" class="text-gray-600 hover:text-blue-600 flex items-center">
			<Fa {icon} class="mr-2 hover:text-blue-600 text-sm" />
			<span class="font-medium text-sm">{tag}</span>
			<span class="ml-1 text-xs">({count})</span>
		</button>
	</div>
</li>

<style>
	.checkbox-custom {
		width: 14px;
		height: 14px;
		margin: 0;
		padding: 0;
		border-radius: 20%;
		appearance: none;
		border: 1px solid #ccc;
		background-color: #fff;
		cursor: pointer;
	}

	.checkbox-custom:checked {
		background-color: #3b83f6;
		border-color: #60a5fa;
	}
</style>
