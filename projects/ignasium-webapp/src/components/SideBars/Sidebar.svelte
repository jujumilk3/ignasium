<script lang="ts">
    import TagItem from './TagItem.svelte';

    let showMoreTags = false;
    export let tagSetName = 'Companies';

    function toggleTags() {
        showMoreTags = !showMoreTags;
    }

    // 태그 선택 상태를 저장할 객체
    let tagSelections: { [key: string]: 'and' | 'or' | null } = {};

    // 태그 선택 함수
    function selectTag(tag: string, condition: 'and' | 'or') {
        if (tagSelections[tag] === condition) {
            tagSelections[tag] = null;
        } else {
            tagSelections[tag] = condition;
        }
        tagSelections = {...tagSelections};
    }

    // 태그 데이터 (실제로는 props나 store에서 가져올 수 있습니다)
    const tags = [
        { name: 'Github', count: 2 },
        { name: 'AWS', count: 1 },
        // 다른 태그들...
    ];
</script>

<!-- Sidebar for Tags -->
<aside class="w-1/4 bg-white shadow-md p-4 rounded-md">
    <h2 class="text-lg font-semibold mb-2">{tagSetName}</h2>
    
    <div class="flex mb-2">
        <div class="w-1/12 text-center font-semibold text-xs">AND</div>
        <div class="w-1/12 text-center font-semibold text-xs">OR</div>
        <div class="w-10/12"></div>
    </div>

    <ul class="space-y-1">
        {#each tags as tag}
            <TagItem 
                tag={tag.name}
                count={tag.count}
                selection={tagSelections[tag.name]}
                onSelect={selectTag}
            />
        {/each}
    </ul>

    <!-- Hidden Tags -->
    <ul id="hidden-tags" class="space-y-1 mt-1 {showMoreTags ? 'block' : 'hidden'}">
        <!-- 숨겨진 태그들에 대해서도 같은 방식으로 적용 -->
    </ul>

    <!-- Toggle Button -->
    <button id="toggle-button" on:click={toggleTags} class="text-green-600 hover:text-green-500 mt-4">
        더보기
    </button>
</aside>

<style>
    li {
        padding: 0.15rem 0;
    }
</style>