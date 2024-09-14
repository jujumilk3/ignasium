<script lang="ts">
    import { onMount } from 'svelte';
    import TagItem from './TagItem.svelte';

    // vars
    export let exposeSaveButton = false;
    export let tagSetName = 'Companies';
    export let tags = [
        { name: 'Github', count: 2 },
        { name: 'AWS', count: 1 },
        { name: 'OpenAI', count: 1 },
        { name: 'Line', count: 1 },
        { name: 'Anthropic', count: 1 },
        { name: 'Perplexity', count: 1 }
    ];
    let showMoreTags = false;
    let tagSelections: { [key: string]: 'and' | 'or' | null } = {};

    // 컴포넌트 마운트 시 모든 태그를 OR로 선택
    onMount(() => {
        tags.forEach(tag => {
            tagSelections[tag.name] = 'or';
        });
        tagSelections = {...tagSelections};
    });

    // functions
    // 태그 선택 함수
    function selectTag(tag: string, condition: 'and' | 'or') {
        if (tagSelections[tag] === condition) {
            tagSelections[tag] = null;
        } else {
            tagSelections[tag] = condition;
        }
        tagSelections = {...tagSelections};
    }    
    function toggleTags() {
        showMoreTags = !showMoreTags;
    }

    // 모든 태그 선택 함수 수정
    function selectAllTags(condition: 'and' | 'or') {
        const allSelected = tags.every(tag => tagSelections[tag.name] === condition);
        
        tags.forEach(tag => {
            tagSelections[tag.name] = allSelected ? null : condition;
        });
        tagSelections = {...tagSelections};
    }

    // Sidebar의 고유 식별자 추가
    export let sidebarId: string = tagSetName;

    function saveTagSet() {
        const selectedTags = tags.reduce((acc, tag) => {
            if (tagSelections[tag.name]) {
                acc[tag.name] = tagSelections[tag.name];
            }
            return acc;
        }, {} as {[key: string]: 'and' | 'or'});

        console.log(`Selected tags for ${sidebarId}:`, selectedTags);
    }

    // 외부에서 접근 가능한 함수로 변경
    export function getSelectedTags() {
        return tags.reduce((acc, tag) => {
            if (tagSelections[tag.name]) {
                acc[tag.name] = tagSelections[tag.name];
            }
            return acc;
        }, {} as {[key: string]: 'and' | 'or'});
    }

    $: visibleTags = tags.slice(0, 5);
    $: hiddenTags = tags.slice(5);
</script>

<!-- Sidebar for Tags -->
    

<div class="flex justify-between items-center mb-2">
    <h2 class="text-lg font-semibold">{tagSetName}</h2>
    {#if exposeSaveButton}
        <button 
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-1 px-2 rounded text-sm"
            on:click={saveTagSet}
    >
        Save
    </button>
    {/if}
</div>
<div class="flex mb-2">
    <div class="w-2/12 text-center font-semibold text-xs cursor-pointer hover:text-green-600" on:click={() => selectAllTags('and')}>AND</div>
    <div class="w-2/12 text-center font-semibold text-xs cursor-pointer hover:text-green-600" on:click={() => selectAllTags('or')}>OR</div>
    <div class="w-8/12"></div>
</div>

    <ul class="space-y-1">
        {#each visibleTags as tag}
            <TagItem 
                tag={tag.name}
                count={tag.count}
                selection={tagSelections[tag.name]}
                onSelect={selectTag}
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
                />
            {/each}
        </ul>

        <!-- Toggle Button -->
        <button id="toggle-button" on:click={toggleTags} class="text-green-600 hover:text-green-500 mt-4">
            {showMoreTags ? 'Hide' : 'Show More'}
        </button>
    {/if}


<style>
    li {
        padding: 0.15rem 0;
    }
</style>