import { createWebHistory, createRouter } from "vue-router";

import Main from './apps/anagram-hunt/src/components/Main';
// import AnagramGame from './apps/AnagramGame.vue';
// import MathGame from './apps/MathGame.vue';

const routes = [
    {
        path: '/play/anagram-play',
        component: Main,
    },
    // {
    //     path: '/play/anagram-game',
    //     component: AnagramGame,
    // },
    // {
    //     path: '/play/math-game',
    //     component: MathGame,
    // },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});


export default router;