
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'posts', component: () => import('pages/Posts.vue') },
      { path: 'users', component: () => import('pages/Users.vue') }
    ]
  },
  {
    path: '/',
    component: () => import('layouts/SimpleLayout.vue'),
    children: [
      { path: 'posts/:id', component: () => import('pages/Post/Index.vue'), props: true },
      { path: 'html', component: () => import('pages/Html/Index.vue') },
      { path: 'text', component: () => import('pages/Text/Index.vue') },
      { path: 'users/:id', component: () => import('pages/User/Index.vue'), props: true }
    ]
  }

]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
