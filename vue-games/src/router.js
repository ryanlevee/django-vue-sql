import { createWebHistory, createRouter } from "vue-router";

import Main from './apps/anagram-hunt/src/components/Main';

const routes = [
    {
        path: '/play/anagram-play',
        component: Main,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});


export default router;