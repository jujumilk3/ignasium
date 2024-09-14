<script lang="ts">
    // vars
    export let tagSetName = 'Companies';
    let showMoreTags = false;
    // 태그 선택 상태를 저장할 객체
    let tagSelections: { [key: string]: 'and' | 'or' | null } = {};
    // 태그 데이터 업데이트
    const tags = [
        { name: 'Github', count: 2 },
        { name: 'AWS', count: 1 },
        { name: 'OpenAI', count: 1 },
        { name: 'Line', count: 1 },
        { name: 'Anthropic', count: 1 },
        { name: 'Perplexity', count: 1 }
    ];

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

    // 모든 태그 선택 함수 추가
    function selectAllTags(condition: 'and' | 'or') {
        tags.forEach(tag => {
            tagSelections[tag.name] = condition;
        });
        tagSelections = {...tagSelections};
    }

    // components
    import TagItem from './TagItem.svelte';

    $: visibleTags = tags.slice(0, 5);
    $: hiddenTags = tags.slice(5);
</script>

<!-- Sidebar for Tags -->
<aside class="w-1/4 bg-white shadow-md p-4 rounded-md">
    <h2 class="text-lg font-semibold mb-2">{tagSetName}</h2>
    
    <div class="flex mb-2">
        <div class="w-1/12 text-center font-semibold text-xs cursor-pointer hover:text-green-600" on:click={() => selectAllTags('and')}>AND</div>
        <div class="w-1/12 text-center font-semibold text-xs cursor-pointer hover:text-green-600" on:click={() => selectAllTags('or')}>OR</div>
        <div class="w-10/12"></div>
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
            {showMoreTags ? '접기' : '더보기'}
        </button>
    {/if}
</aside>

<style>
    li {
        padding: 0.15rem 0;
    }
</style>