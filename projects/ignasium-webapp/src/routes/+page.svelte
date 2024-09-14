<script lang="ts">

    import { page } from '$app/stores';
    import { setBrowserLocation, setBrowserTitle } from '$lib/stores/browserStore';

    console.log('below is page');
    console.log($page.data);
    setBrowserTitle('');
    setBrowserLocation('home');
</script>


<section class="relative pt-16">
    <!-- Central Search Bar -->
    <div class="container mx-auto mt-12">
        <div class="flex justify-center">
            <div class="w-3/4">
                <div class="relative">
                    <input type="text" placeholder="검색어를 입력하세요" class="w-full border border-gray-300 rounded-full py-3 px-6 text-lg focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-transparent">
                    <button class="absolute right-4 top-3 text-gray-600">
                        🔍
                    </button>
                </div>
            </div>
        </div>
    </div>

    <div class="container mx-auto mt-8 flex space-x-8">
        <!-- Sidebar for Tags -->
        <aside class="w-1/4 bg-white shadow-md p-4 rounded-md">
            <h2 class="text-lg font-semibold mb-4">태그 목록</h2>
            <ul class="space-y-2">
                <li><a href="#" class="text-green-600">전체보기 (3)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">AI (2)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">취업 (1)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">멀티모달 (1)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">Generative UI (1)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">chatGPT (1)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">uxui (1)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">코드리뷰 (1)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">Claude (1)</a></li>
                <li><a href="#" class="text-gray-600 hover:text-green-600">클로드 (1)</a></li>
            </ul>
        </aside>

        <!-- Main Content Area -->
      <!-- Main Content Area -->
      <main class="w-3/4">
        <!-- Post List -->
        <div class="space-y-8">
            <!-- Post 1 -->
            <div class="bg-white shadow-md p-6 rounded-md">
                <!-- Image -->
                <img src="https://via.placeholder.com/800x400" alt="Main Image" class="w-full h-auto rounded-md mb-6">

                <!-- Title -->
                <h1 class="text-2xl font-semibold mb-4">컴공, 디자인 취준생 분들에게 하고 싶은 말</h1>

                <!-- Content Text -->
                <p class="text-gray-700 mb-4">
                    취업 고민들에 대해서 생각들을 정리해봤어요. 현재 취업 준비 중이신 분들에게 도움이 되었으면 합니다. 3줄 요약 - 지금 하는 그 사이드프로젝트는 하지마세요 - 전통적인 코딩, 디자인 말고 AI 적극적으로 활용하세요
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
                <img src="https://via.placeholder.com/800x400" alt="Main Image" class="w-full h-auto rounded-md mb-6">

                <!-- Title -->
                <h1 class="text-2xl font-semibold mb-4">AI를 이용한 UX 개선 방안</h1>

                <!-- Content Text -->
                <p class="text-gray-700 mb-4">
                    AI 기술이 UX 디자인에 어떻게 적용될 수 있는지에 대해 논의해봤습니다. 미래의 UX는 AI와 함께 발전할 것입니다.
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
                <img src="https://via.placeholder.com/800x400" alt="Main Image" class="w-full h-auto rounded-md mb-6">

                <!-- Title -->
                <h1 class="text-2xl font-semibold mb-4">취업 준비를 위한 멀티모달 데이터 활용 방법</h1>

                <!-- Content Text -->
                <p class="text-gray-700 mb-4">
                    멀티모달 데이터가 취업 준비에 어떻게 도움이 될 수 있는지에 대해 알아보았습니다. 다양한 데이터를 활용하는 것이 경쟁력을 높이는 데 중요합니다.
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