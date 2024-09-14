import { writable } from 'svelte/store';
import { configs } from '$lib/constants/configs';

import type { BrowserData } from '$lib/interfaces/browser.interface';

export const browserData = writable<BrowserData>({});

export const setBrowserTitle = (title: string) => {
	title = title ? `${title} | ${configs.PAGE_DEFAULT_TITLE}` : `${configs.PAGE_DEFAULT_TITLE}`;
	browserData.update((oldData) => {
		return { ...oldData, title };
	});
};

export const setBrowserLocation = (location: string) => {
	location = location || '';
	browserData.update((oldData) => {
		return { ...oldData, location };
	});
};
