<script lang="ts">
	import { createPopper } from '@popperjs/core';

	// core components
	let dropdownPopoverShow = false;
	let btnDropdownRef: Element;
	let popoverDropdownRef: HTMLElement;

	const toggleDropdown = (event: MouseEvent) => {
		event.preventDefault();
		if (dropdownPopoverShow) {
			dropdownPopoverShow = false;
		} else {
			dropdownPopoverShow = true;
			createPopper(btnDropdownRef, popoverDropdownRef, {
				placement: 'bottom-start'
			});
		}
	};
</script>

<div>
	<a
		class="hover:text-blueGray-500 text-blueGray-700 px-3 py-2 flex items-center text-xs uppercase font-bold"
		href="#pablo"
		bind:this={btnDropdownRef}
		on:click={toggleDropdown}
	>
		Demo Pages
	</a>
	<div
		bind:this={popoverDropdownRef}
		class="bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48 {dropdownPopoverShow
			? 'block'
			: 'hidden'}"
	>
		<span
			class="text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-nowrap bg-transparent text-blueGray-400"
		>
			Test Layout
		</span>
		<a
			href="/test"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Test
		</a>
		<a
			href="/testapi"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			TestAPI
		</a>

		<span
			class="text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-nowrap bg-transparent text-blueGray-400"
		>
			Admin Layout
		</span>
		<a
			href="/dashboard"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Dashboard
		</a>
		<a
			href="/dashboard/settings"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Settings
		</a>
		<a
			href="/dashboard/tables"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Tables
		</a>
		<a
			href="/dashboard/maps"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Maps
		</a>
		<div class="h-0 mx-4 my-2 border border-solid border-blueGray-100" />
		<span
			class="text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-nowrap bg-transparent text-blueGray-400"
		>
			Auth Layout
		</span>
		<a
			href="/signin"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Login
		</a>
		<a
			href="/signup"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Register
		</a>
		<div class="h-0 mx-4 my-2 border border-solid border-blueGray-100" />
		<span
			class="text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-nowrap bg-transparent text-blueGray-400"
		>
			No Layout
		</span>
		<a
			href="/landing"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Landing
		</a>
		<a
			href="/profile"
			class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
		>
			Profile
		</a>
	</div>
</div>
