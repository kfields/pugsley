<template>
  <q-page padding>
    <div style="width: 500px; max-width: 90vw;">
      <q-list>
        <q-item-label style="font-size: 1.25rem;">YOUR MOST RECENT EDITS</q-item-label>
        <q-item v-for="edge in allPosts.edges" :key="edge.id" :to="`/posts/${edge.node.id}`">
          <q-item-section avatar>
            <q-icon name="mdi-file-document-outline" inverted color="grey-6" />
          </q-item-section>
          <q-item-section>
            {{ edge.node.title }}
          </q-item-section>
      </q-item>
      </q-list>
    </div>
  </q-page>
</template>

<style>
</style>

<script>
import { UiMixin, PageMixin } from 'src/mixins'

import gql from 'graphql-tag'
const postQuery = gql`
query postQuery {
  allPosts {
    edges {
      node {
        id
        title
        slug
      }
    }
  }
}
`
export default {
  name: 'Home',
  mixins: [ UiMixin, PageMixin ],

  data () {
    return {
      title: 'Home',
      authorId: this.$route.params.authorId
    }
  },
  apollo: {
    // Simple query that will update the 'article' vue property
    allPosts: {
      query: postQuery,
      prefetch: false,
      variables () {
        return { authorId: this.authorId }
      }
    }
  }
}
</script>
