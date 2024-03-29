import Vue from "vue";
import VueRouter from "vue-router";
import Layout from "../view/Layout";
import Home from "../view/Home";
Vue.use(VueRouter);

const routes = [
    {
        path: "/demo",
        name: "home",
        redirect: "/demo/home",
        component: Layout,
        children: [
            {
                path: "home",
                component: Home
            }
        ]
    }
];
const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});
export default router;