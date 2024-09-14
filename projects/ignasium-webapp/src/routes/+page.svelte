<script lang="ts">
	import { page } from '$app/stores';
	import { setBrowserLocation, setBrowserTitle } from '$lib/stores/browserStore';

	// components
	import Sidebar from '$components/SideBars/Sidebar.svelte';
	import { onMount } from 'svelte';

	let sidebarRefs: Sidebar[] = [];

	function saveAllSidebars() {
		const allSelectedTags = sidebarRefs.map((sidebar, index) => {
			return {
				// sidebarId: `sidebar${index + 1}`,
                // sidebarId: sidebar.sidebarId, // 이렇게 하면 초기화 되기 전 선언한 것이므로 sidebarId가 undefined로 나옴
                sidebarId: sidebar.getSidebarId(),
				selectedTags: sidebar.getSelectedTags()
			};
		});

		console.log("All selected tags:", allSelectedTags);
	}

	onMount(() => {
		// 컴포넌트가 마운트된 후에 sidebarRefs 배열이 채워집니다.
	});

	let techTags = [
		{ name: 'Python', count: 2 },
		{ name: 'JavaScript', count: 1 },
		{ name: 'TypeScript', count: 1 },
		{ name: 'React', count: 1 },
		{ name: 'Svelte', count: 1 },
		{ name: 'Vue', count: 1 },
		{ name: 'Next.js', count: 1 },
		{ name: 'Nuxt.js', count: 1 },
		{ name: 'Tailwind CSS', count: 1 },
		{ name: 'DevOps', count: 1 },
		{ name: 'Docker', count: 1 },
		{ name: 'Kubernetes', count: 1 },
		{ name: 'AWS', count: 1 },
		{ name: 'Azure', count: 1 },
		{ name: 'GCP', count: 1 },
		{ name: 'Firebase', count: 1 },
		{ name: 'MySQL', count: 1 },
		{ name: 'PostgreSQL', count: 1 },
	]
</script>

<section class="relative pt-16">
	<!-- Central Search Bar -->
	<div class="container mx-auto mt-12">
		<div class="flex justify-center">
			<div class="w-3/4">
				<div class="relative">
					<input
						type="text"
						placeholder="검색어를 입력하세요"
						class="w-full border border-gray-300 rounded-full py-3 px-6 text-lg focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-transparent"
					/>
					<button class="absolute right-4 top-3 text-gray-600"> 🔍 </button>
				</div>
			</div>
		</div>
	</div>

	<div class="container mx-auto mt-8 flex space-x-8">
		<!-- Sidebar for Tags -->
		<aside class="w-1/4 bg-white shadow-md p-4 rounded-md">
			<Sidebar bind:this={sidebarRefs[0]} sidebarId="companies" tagSetName="Companies" exposeSaveButton={true} buttonFunction={saveAllSidebars}  />
			<Sidebar bind:this={sidebarRefs[1]} sidebarId="technologies" tagSetName="Technologies" tags={techTags} />
		</aside>
		<!-- Main Content Area -->
		<main class="w-3/4">
			<!-- Post List -->
			<div class="space-y-8">
				<!-- Post 1 -->
				<div class="bg-white shadow-md p-6 rounded-md">
					<!-- Image -->
					<img
						src="https://via.placeholder.com/800x400"
						alt="Main Image"
						class="w-full h-auto rounded-md mb-6"
					/>

					<!-- Title -->
					<h1 class="text-2xl font-semibold mb-4">컴공, 디자인 취준생 분들에게 하고 싶은 말</h1>

					<!-- Content Text -->
					<p class="text-gray-700 mb-4">
						취업 고민들에 대해서 생각들을 정리해봤어요. 현재 취업 준비 중이신 분들에게 도움이
						되었으면 합니다. 3줄 요약 - 지금 하는 그 사이드프로젝트는 하지마세요 - 전통적인 코딩,
						디자인 말고 AI 적극적으로 활용하세요
					</p>

					<!-- Metadata (Date, Comments, Likes) -->
					<div class="flex items-center space-x-4 text-gray-500 text-sm">
						<span>취업</span>
						<span>2024년 9월 5일</span>
						<span>9개의 댓글</span>
						<span>❤️ 144</span>
					</div>
				</div>

				<!-- Post 2 -->
				<div class="bg-white shadow-md p-6 rounded-md">
					<!-- Image -->
					<img
						src="https://via.placeholder.com/800x400"
						alt="Main Image"
						class="w-full h-auto rounded-md mb-6"
					/>

					<!-- Title -->
					<h1 class="text-2xl font-semibold mb-4">AI를 이용한 UX 개선 방안</h1>

					<!-- Content Text -->
					<p class="text-gray-700 mb-4">
						AI 기술이 UX 디자인에 어떻게 적용될 수 있는지에 대해 논의해봤습니다. 미래의 UX는 AI와
						함께 발전할 것입니다.
					</p>

					<!-- Metadata (Date, Comments, Likes) -->
					<div class="flex items-center space-x-4 text-gray-500 text-sm">
						<span>AI</span>
						<span>2024년 9월 6일</span>
						<span>4개의 댓글</span>
						<span>❤️ 98</span>
					</div>
				</div>

				<!-- Post 3 -->
				<div class="bg-white shadow-md p-6 rounded-md">
					<!-- Image -->
					<img
						src="https://via.placeholder.com/800x400"
						alt="Main Image"
						class="w-full h-auto rounded-md mb-6"
					/>

					<!-- Title -->
					<h1 class="text-2xl font-semibold mb-4">취업 준비를 위한 멀티모달 데이터 활용 방법</h1>

					<!-- Content Text -->
					<p class="text-gray-700 mb-4">
						멀티모달 데이터가 취업 준비에 어떻게 도움이 될 수 있는지에 대해 알아보았습니다. 다양한
						데이터를 활용하는 것이 경쟁력을 높이는 데 중요합니다.
					</p>

					<!-- Metadata (Date, Comments, Likes) -->
					<div class="flex items-center space-x-4 text-gray-500 text-sm">
						<span>멀티모달</span>
						<span>2024년 9월 7일</span>
						<span>5개의 댓글</span>
						<span>❤️ 76</span>
					</div>
				</div>
			</div>
		</main>
	</div>
</section>

<style lang="postcss">
	:global(html) {
		background-color: cadetblue;
	}
</style>

<!-- <button 
	class="mt-4 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
	on:click={saveAllSidebars}
>
	Save All Sidebars
</button> -->
