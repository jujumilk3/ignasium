<script lang="ts">
    export let tag: string;
    export let count: number;
    export let selection: 'and' | 'or' | null;
    export let onSelect: (tag: string, condition: 'and' | 'or') => void;
</script>

<li class="flex items-center">
    <div class="w-2/12 flex justify-center">
        <input type="checkbox" 
               class="checkbox-custom"
               checked={selection === 'and'}
               on:change={() => onSelect(tag, 'and')}>
    </div>
    <div class="w-2/12 flex justify-center">
        <input type="checkbox" 
               class="checkbox-custom"
               checked={selection === 'or'}
               on:change={() => onSelect(tag, 'or')}>
    </div>
    <div class="w-8/12 pl-2">
        <a href="#" class="text-gray-600 hover:text-green-600">{tag} ({count})</a>
    </div>
</li>

<style>
    .checkbox-custom {
        width: 14px;
        height: 14px;
        margin: 0;
        padding: 0;
    }
</style>