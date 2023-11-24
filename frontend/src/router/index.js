import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",

    component: () =>
      import(/* webpackChunkName: "about" */ "../views/MainPage.vue"),
  },
  {
    path: "/database",
    name: "database",

    component: () =>
      import("../views/ReviewDataBase.vue"),
  },
  {
    path: "/notfound",
    name: "NotFound",
    component: () =>
    import( "../components/PageNotFound.vue"),
    props: true
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
