<script lang="ts">
	// imports
	import { onMount } from 'svelte';
    import { writable } from 'svelte/store';
	import { faGithub, faAws, faRedhat, faTwitter, faLine } from '@fortawesome/free-brands-svg-icons';
	import { faBuilding } from '@fortawesome/free-solid-svg-icons';
	import { faSave } from '@fortawesome/free-solid-svg-icons';

    // import elements
    import TagItem from './TagItem.svelte';
    import Fa from 'svelte-fa';

	// vars
	export let isExposeSaveButton = false;
	export let isExposeSearchBar = false;
	export let tagSetName = 'Companies';
	export let tags: Array<{ name: string; count: number; icon?: any; queries?: string }> = [
		{ name: 'Github', count: 2, icon: faGithub },
		{ name: 'AWS', count: 1, icon: faAws },
		{ name: 'Redhat', count: 1, icon: faRedhat },
		{ name: 'Twitter', count: 1, icon: faTwitter },
		{ name: 'Line', count: 1, icon: faLine },
		{ name: 'Anthropic', count: 1 },
		{ name: 'Perplexity', count: 1 }
	];
	export let buttonFunction = () => {};
	export let sidebarIcon = faBuilding;
	// Sidebar의 고유 식별자 추가
	export let sidebarId: string = tagSetName;
	export function getSidebarId() {
		return sidebarId;
	}
	export let visibleStandardTagsCount = 5;

	// 외부에서 접근 가능한 함수로 변경
	export function getSelectedTags() {
		return tags.reduce(
			(acc, tag) => {
				if (tagSelections[tag.name]) {
					if (tagSelections[tag.name] !== null) {
						acc[tag.name] = tagSelections[tag.name] as 'and' | 'or';
					}
				}
				return acc;
			},
			{} as { [key: string]: 'and' | 'or' }
		);
	}

	let showMoreTags = false;
	let tagSelections: { [key: string]: 'and' | 'or' | null } = {};
	let searchTerm = writable('');

	// 컴포넌트 마운트 시 모든 태그를 OR로 선택
	onMount(() => {
		tags.forEach((tag) => {
			tagSelections[tag.name] = 'or';
		});
		tagSelections = { ...tagSelections };
	});

	// functions
	// 태그 선택 함수
	function selectTag(tag: string, condition: 'and' | 'or') {
		if (tagSelections[tag] === condition) {
			tagSelections[tag] = null;
		} else {
			tagSelections[tag] = condition;
		}
		tagSelections = { ...tagSelections };
	}
	function toggleTags() {
		showMoreTags = !showMoreTags;
	}

	// 모든 태그 선택 함수 수정
	function selectAllTags(condition: 'and' | 'or') {
		const allSelected = tags.every((tag) => tagSelections[tag.name] === condition);

		tags.forEach((tag) => {
			tagSelections[tag.name] = allSelected ? null : condition;
		});
		tagSelections = { ...tagSelections };
	}

	function removeAllTags() {
		tags.forEach((tag) => {
			tagSelections[tag.name] = null;
		});
		tagSelections = { ...tagSelections };
	}

	$: filteredTags = tags.filter(
		(tag) =>
			tag.name.toLowerCase().includes($searchTerm.toLowerCase()) ||
			(tag.queries && tag.queries.toLowerCase().includes($searchTerm.toLowerCase()))
	);

	$: visibleTags = filteredTags.slice(0, visibleStandardTagsCount);
	$: hiddenTags = filteredTags.slice(visibleStandardTagsCount);
</script>

<!-- Sidebar for Tags -->

<div class="mb-5">
	<div class="flex justify-between items-center mb-2">
		<span class="flex items-center">
			<Fa icon={sidebarIcon} class="mr-2 text-gray-700" />
			<h2 class="text-lg font-semibold text-gray-700">{tagSetName}</h2>
		</span>
		{#if isExposeSaveButton}
			<button
				class="bg-blue-500 hover:bg-blue-700 text-white font-bold mt-1 py-1 px-2 rounded text-sm"
				on:click={buttonFunction}
			>
				<Fa icon={faSave} />
			</button>
		{/if}
	</div>
	{#if isExposeSearchBar}
		<div class="relative">
			<input
				type="text"
				placeholder="Find"
				bind:value={$searchTerm}
				class="w-full p-1 mb-1 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent text-xs"
			/>
		</div>
	{/if}
	<!-- and or label -->
	<div class="flex mb-2">
		<button
			type="button"
			class="w-2/12 text-center text-gray-500 font-semibold text-xs cursor-pointer hover:text-blue-600"
			on:click={() => selectAllTags('and')}
			aria-label="Select all tags with 'and' condition"
		>
			and
		</button>
		<button
			type="button"
			class="w-2/12 text-center text-gray-500 font-semibold text-xs cursor-pointer hover:text-blue-600"
			on:click={() => selectAllTags('or')}
			aria-label="Select all tags with 'or' condition"
		>
			or
		</button>
		<button
			type="button"
			class="w-4/12 text-center text-gray-500 font-semibold text-xs cursor-pointer hover:text-blue-600"
			on:click={() => removeAllTags()}
		>
			rm all
		</button>
		<div class="w-4/12"></div>
	</div>

	<ul class="space-y-1">
		{#each visibleTags as tag}
			<TagItem
				tag={tag.name}
				count={tag.count}
				selection={tagSelections[tag.name]}
				onSelect={selectTag}
				icon={tag.icon}
			/>
		{/each}
	</ul>

	<!-- Hidden Tags -->
	{#if hiddenTags.length > 0}
		<ul id="hidden-tags" class="space-y-1 mt-1 {showMoreTags ? 'block' : 'hidden'}">
			{#each hiddenTags as tag}
				<TagItem
					tag={tag.name}
					count={tag.count}
					selection={tagSelections[tag.name]}
					onSelect={selectTag}
					icon={tag.icon}
				/>
			{/each}
		</ul>

		<!-- Toggle Button -->
		<button
			id="toggle-button"
			on:click={toggleTags}
			class="text-blue-400 hover:text-blue-600 mt-1 text-xs font-medium"
		>
			{showMoreTags ? 'Hide' : 'Show More'}
		</button>
	{/if}
</div>
